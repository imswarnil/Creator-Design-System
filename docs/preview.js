/* Preview chrome behaviour: drawer + scrollspy. Chrome only — nothing here
   ships in the theme. */
(function () {
	// Drawer (small screens) + sidebar collapse (desktop, persisted)
	try {
		if (localStorage.getItem('cds-side') === 'collapsed') {
			document.body.classList.add('side-collapsed');
		}
	} catch (e) {}
	document.addEventListener('click', function (e) {
		if (e.target.closest('[data-nav-toggle]')) {
			document.body.classList.toggle('nav-open');
		} else if (e.target.closest('[data-side-toggle]')) {
			var collapsed = document.body.classList.toggle('side-collapsed');
			try { localStorage.setItem('cds-side', collapsed ? 'collapsed' : 'open'); } catch (err) {}
		} else if (e.target.closest('.doc-scrim') || e.target.closest('.doc-side__nav a')) {
			document.body.classList.remove('nav-open');
		}
	});

	// Replay chips (animation pages): restart every CSS animation in the tile.
	document.addEventListener('click', function (e) {
		var rp = e.target.closest('[data-replay],[data-replay2],[data-replay-an],[data-replay-sec],[data-replay-sting],[data-replay-tx]');
		if (!rp) return;
		var scope = rp.closest('.demo-tile, .surface, section') || document.body;
		var all = scope.querySelectorAll('*');
		all.forEach(function (el) { el.style.animation = 'none'; });
		void scope.offsetWidth;
		all.forEach(function (el) { el.style.animation = ''; });
	});

	// The menu burger mirrors the sheet's state, so it always returns to bars.
	var menu = document.getElementById('cds-menu');
	if (menu) {
		var mb = document.querySelector('[data-menu-burger]');
		menu.addEventListener('close', function () {
			if (mb) mb.setAttribute('aria-expanded', 'false');
		});
		document.addEventListener('click', function (e) {
			if (e.target.closest('[data-menu-burger]')) mb.setAttribute('aria-expanded', 'true');
		});
	}

	// Guides toggle (broadcast pages): overlay export safe areas.
	var gBtn = document.getElementById('guideToggle');
	if (gBtn) {
		var gLabel = document.getElementById('guideLabel');
		var gOn = false;
		gBtn.addEventListener('click', function () {
			gOn = !gOn;
			gLabel.textContent = gOn ? 'Guides on' : 'Guides off';
			gBtn.setAttribute('aria-pressed', String(gOn));
			document.querySelectorAll('.yt[data-guide]').forEach(function (el) {
				el.classList.toggle('yt-guides', gOn);
			});
		});
	}

	// Copy-code buttons: [data-copy] copies its codebox/copy-line's <code>,
	// or the element named by the attribute value.
	document.addEventListener('click', function (e) {
		var btn = e.target.closest('[data-copy]');
		if (btn) {
			var sel = btn.getAttribute('data-copy');
			var src = sel
				? document.querySelector(sel)
				: (btn.closest('.codebox, .copy-line') || {}).querySelector
					? btn.closest('.codebox, .copy-line').querySelector('code')
					: null;
			// Highlighted code keeps its own source on data-raw — reading
			// textContent off token spans would lose the line breaks.
			var text = src ? (src.getAttribute('data-raw') || src.textContent).trim() : '';
			navigator.clipboard.writeText(text).then(function () {
				var label = btn.textContent;
				btn.setAttribute('data-copied', '');
				btn.textContent = 'Copied';
				setTimeout(function () {
					btn.removeAttribute('data-copied');
					btn.textContent = label;
				}, 1600);
			});
		}

		// Dialog openers/closers: [data-dialog="id"] / [data-dialog-close]
		var opener = e.target.closest('[data-dialog]');
		if (opener) {
			var dlg = document.getElementById(opener.getAttribute('data-dialog'));
			if (dlg && dlg.showModal) dlg.showModal();
		}
		var closer = e.target.closest('[data-dialog-close]');
		if (closer) {
			var host = closer.closest('dialog');
			if (host) host.close();
		}
	});

	// Scrollspy — highlight the section link whose section owns the viewport.
	// The headings live in the right rail now; the left rail is pages only.
	var links = Array.prototype.slice.call(
		document.querySelectorAll(".doc-toc a[href^='#']")
	);
	if (!links.length || !('IntersectionObserver' in window)) return;

	var byId = {};
	links.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });

	var current = null;
	var observer = new IntersectionObserver(
		function (entries) {
			entries.forEach(function (entry) {
				if (!entry.isIntersecting) return;
				if (current) current.classList.remove('is-active');
				current = byId[entry.target.id];
				if (current) {
					current.classList.add('is-active');
					current.scrollIntoView({ block: 'nearest' });
				}
			});
		},
		{ rootMargin: '-10% 0px -70% 0px' }
	);

	Object.keys(byId).forEach(function (id) {
		var sec = document.getElementById(id);
		if (sec) observer.observe(sec);
	});
})();

/* ── Docs search ─────────────────────────────────────────────────────────────
   Filters a generated index (search-index.json) of every page title, its
   group, and its headings. Keyboard: "/" focuses, ↑/↓ move, Enter opens,
   Escape clears. */
(function () {
	var input = document.getElementById('docSearch');
	var out = document.getElementById('docResults');
	if (!input || !out) return;

	var rows = [], sel = -1, loading = null;

	// One shared promise: every keystroke awaits the SAME fetch, so an early
	// keystroke can't resolve later and render a stale query.
	var load = function () {
		if (!loading) {
			loading = fetch('./search-index.json')
				.then(function (r) { return r.json(); })
				.then(function (d) { rows = d; })
				.catch(function () { rows = []; });
		}
		return loading;
	};

	var esc = function (s) { return s.replace(/[&<>"]/g, function (c) {
		return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };

	var hit = function (text, q) {
		var i = text.toLowerCase().indexOf(q);
		if (i === -1) return null;
		return esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + q.length)) +
			'</mark>' + esc(text.slice(i + q.length));
	};

	var render = function (q) {
		if (!q) { out.hidden = true; input.setAttribute('aria-expanded', 'false'); return; }
		var found = [];
		rows.forEach(function (r) {
			var t = hit(r.t, q);
			if (t) { found.push({ href: './' + r.s + '.html', main: t, sub: r.g }); return; }
			for (var i = 0; i < r.h.length; i++) {
				var h = hit(r.h[i], q);
				if (h) { found.push({ href: './' + r.s + '.html', main: h, sub: r.g + ' · ' + esc(r.t) }); return; }
			}
			// Class names from the spec strips — searching ".btn" should find Buttons.
			for (var j = 0; j < (r.k || []).length; j++) {
				var k = hit(r.k[j], q);
				if (k) { found.push({ href: './' + r.s + '.html', main: esc(r.t) + ' — ' + k, sub: r.g }); return; }
			}
			var d = r.d && hit(r.d, q);
			if (d) found.push({ href: './' + r.s + '.html', main: esc(r.t), sub: r.g });
		});
		found = found.slice(0, 12);
		out.innerHTML = found.length
			? found.map(function (f) { return '<a href="' + f.href + '">' + f.main + '<small>' + f.sub + '</small></a>'; }).join('')
			: '<p class="doc-results__none">Nothing matches “' + esc(q) + '”.</p>';
		out.hidden = false;
		input.setAttribute('aria-expanded', 'true');
		sel = -1;
	};

	input.addEventListener('input', function () {
		// Re-read the value when the index arrives — never the captured one.
		load().then(function () { render(input.value.trim().toLowerCase()); });
	});

	input.addEventListener('keydown', function (e) {
		var items = out.querySelectorAll('a');
		if (e.key === 'Escape') { input.value = ''; out.hidden = true; input.blur(); return; }
		if (!items.length) return;
		if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
			e.preventDefault();
			sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + items.length) % items.length;
			items.forEach(function (a) { a.classList.remove('is-sel'); });
			items[sel].classList.add('is-sel');
			items[sel].scrollIntoView({ block: 'nearest' });
		} else if (e.key === 'Enter' && sel > -1) {
			e.preventDefault();
			window.location.href = items[sel].getAttribute('href');
		}
	});

	// "/" from anywhere focuses search.
	document.addEventListener('keydown', function (e) {
		if (e.key !== '/' || /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) return;
		e.preventDefault();
		document.body.classList.remove('side-collapsed');
		input.focus();
	});

	document.addEventListener('click', function (e) {
		if (!e.target.closest('.doc-search') && !e.target.closest('.doc-results')) out.hidden = true;
	});
})();

/* Burger demos on the navbar docs page: toggle aria-expanded so the X works. */
document.addEventListener('click', function (e) {
	var b = e.target.closest('[data-burger]');
	if (!b) return;
	b.setAttribute('aria-expanded', b.getAttribute('aria-expanded') === 'true' ? 'false' : 'true');
});

/* ── Preview ⇄ Code on every demo ────────────────────────────────────────────
   Each .demo-tile gets a toggle. Code view prints the demo's own markup,
   tidied and coloured by the system's own highlighter, in a copyable block —
   so the docs can never drift from what is actually rendered. The block rolls
   in line by line the first time it is opened, the way footage plays. */
(function () {
	var tiles = document.querySelectorAll('.demo-tile');
	if (!tiles.length) return;

	/* What the demo looked like before the page touched it. The highlighter has
	   already rewritten any code block inside the demo into token spans and
	   marked the box for playback; printing that back would show the reader
	   our plumbing instead of their markup. Every code element keeps its own
	   source on data-raw, so the original is always recoverable. */
	var pristine = function (demo) {
		var clone = demo.cloneNode(true);
		clone.querySelectorAll('code[data-raw]').forEach(function (c) {
			c.textContent = c.getAttribute('data-raw');
			c.removeAttribute('data-raw');
			c.removeAttribute('data-highlighted');
		});
		clone.querySelectorAll('.codebox').forEach(function (b) {
			b.removeAttribute('data-play');
			b.removeAttribute('data-played');
			b.classList.remove('is-playing', 'is-played');
		});
		return clone.innerHTML;
	};

	var tidy = function (html) {
		// Strip the artefacts of generated markup so the copy is paste-ready.
		return html
			.replace(/<!--[\s\S]*?-->/g, '')
			.replace(/\s+data-(dialog|dialog-close|copy|burger|replay[a-z-]*|install-[a-z]+)(="[^"]*")?/g, '')
			.split('\n').map(function (l) { return l.replace(/\s+$/, ''); })
			.filter(function (l) { return l.trim(); })
			.join('\n');
	};

	var VOID = /^(?:area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)$/i;

	/* One element per line, indented by nesting. The demos are authored as a
	   single run of markup — readable to write, unreadable to copy — and a
	   block that is one 900-character line has nothing for the playback to
	   roll through either. Elements holding nothing but text stay on one line;
	   breaking `<button>Primary</button>` across three helps no one. */
	var format = function (html) {
		var parts = html.replace(/>\s+</g, '><').split(/(<[^>]+>)/)
			.filter(function (t) { return t.trim(); });
		var rows = [], depth = 0;
		parts.forEach(function (t) {
			var pad = new Array(depth + 1).join('\t');
			if (/^<\//.test(t)) {
				depth = Math.max(0, depth - 1);
				rows.push({ pad: new Array(depth + 1).join('\t'), text: t, kind: 'close' });
			} else if (/^</.test(t)) {
				rows.push({ pad: pad, text: t, kind: 'open' });
				var name = (t.match(/^<([\w-]+)/) || [])[1];
				if (name && !VOID.test(name) && !/\/>$/.test(t)) depth += 1;
			} else {
				rows.push({ pad: pad, text: t.trim(), kind: 'text' });
			}
		});

		var out = [];
		for (var i = 0; i < rows.length; i += 1) {
			if (rows[i].kind === 'open' && rows[i + 1] && rows[i + 1].kind === 'text' &&
				rows[i + 2] && rows[i + 2].kind === 'close') {
				out.push(rows[i].pad + rows[i].text + rows[i + 1].text + rows[i + 2].text);
				i += 2;
			} else {
				out.push(rows[i].pad + rows[i].text);
			}
		}
		return out.join('\n');
	};

	tiles.forEach(function (tile) {
		var demo = tile.querySelector('.demo');
		if (!demo) return;

		// A tile that is already a code block has nothing to toggle to: the
		// preview and the code are the same thing, and offering the switch
		// only invites a click that changes nothing.
		if (demo.querySelector(':scope > .codebox, :scope > figure.codebox')) return;

		var bar = document.createElement('div');
		bar.className = 'demo-switch';
		bar.innerHTML =
			'<button class="demo-switch__btn" type="button" aria-pressed="true">Preview</button>' +
			'<button class="demo-switch__btn" type="button" aria-pressed="false">Code</button>';

		var code = document.createElement('div');
		code.className = 'demo-code';
		code.hidden = true;

		tile.insertBefore(bar, tile.firstChild);
		demo.insertAdjacentElement('afterend', code);

		var btns = bar.querySelectorAll('button');
		btns[1].addEventListener('click', function () {
			if (!code.dataset.filled) {
				code.innerHTML =
					'<figure class="codebox codebox-light u-m-0" data-play>' +
					'<figcaption class="codebox__head"><span class="codebox__lang">html</span>' +
					'<button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>' +
					'<pre class="codebox__pre"><code class="codebox__ln"></code></pre></figure>';
				// textContent, not innerHTML: the highlighter takes the source
				// and owns every span in the block from here on.
				code.querySelector('code').textContent = format(tidy(pristine(demo)));
				if (window.CreatorHighlight) {
					window.CreatorHighlight.el(code.querySelector('code'), { lang: 'html', lines: true });
				}
				code.dataset.filled = '1';
			}
			demo.hidden = true; code.hidden = false;
			btns[0].setAttribute('aria-pressed', 'false');
			btns[1].setAttribute('aria-pressed', 'true');
		});
		btns[0].addEventListener('click', function () {
			demo.hidden = false; code.hidden = true;
			btns[0].setAttribute('aria-pressed', 'true');
			btns[1].setAttribute('aria-pressed', 'false');
		});
	});
})();

/* ── Navbar playground ───────────────────────────────────────────────────────
   Renders the submenu row from the control panel, then prints the markup that
   would produce it. Both come from the same state object, so the preview and
   the copy can never disagree — which is the only reason a playground is worth
   more than a screenshot. */
(function () {
	var root = document.querySelector('[data-nav-playground]');
	if (!root) return;

	var sub = root.querySelector('[data-np-sub]');
	var bar = root.querySelector('[data-np-bar]');
	var shell = root.querySelector('[data-np-shell]');
	var out = root.querySelector('[data-np-code]');
	var readout = root.querySelector('[data-np-value]');

	var val = function (name) {
		var el = root.querySelector('[name="' + name + '"]:checked') ||
			root.querySelector('[name="' + name + '"]');
		return el ? el.value : '';
	};
	var on = function (name) {
		var el = root.querySelector('[name="' + name + '"]');
		return !!(el && el.checked);
	};

	// A preset is a starting point, not a mode: it stamps the controls and then
	// gets out of the way, so the next change is the reader's, not the preset's.
	var PRESETS = {
		series: { tone: 'ink', density: 'compact', prefix: 'EP.', mark: false,
			back: true, kind: true, pos: true, actions: true, rail: false,
			logo: true, icons: true, news: false, cta: true, burger: true,
			progress: false, shell: 'morph' },
		docs: { tone: 'paper', density: 'compact', prefix: '', mark: false,
			back: true, kind: false, pos: false, actions: false, rail: false,
			logo: true, icons: true, news: false, cta: false, burger: false,
			progress: true, shell: 'fixed' },
		course: { tone: 'paper', density: 'regular', prefix: '', mark: true,
			back: true, kind: false, pos: true, actions: true, rail: true,
			logo: true, icons: false, news: true, cta: false, burger: false,
			progress: false, shell: 'island' }
	};

	var apply = function (preset) {
		var conf = PRESETS[preset];
		if (!conf) return;
		var radio = function (name, value) {
			var el = root.querySelector('[name="' + name + '"][value="' + value + '"]');
			if (el) el.checked = true;
		};
		var check = function (name, on) {
			var el = root.querySelector('[name="' + name + '"]');
			if (el) el.checked = on;
		};
		radio('np-tone', conf.tone);
		radio('np-density', conf.density);
		radio('np-prefix', conf.prefix);
		radio('np-shell', conf.shell);
		['mark', 'back', 'kind', 'pos', 'actions', 'rail',
			'logo', 'icons', 'news', 'cta', 'burger', 'progress'].forEach(function (k) {
			check('np-' + k, conf[k]);
		});
	};

	var state = function () {
		return {
			tone: val('np-tone'),
			density: val('np-density'),
			prefix: val('np-prefix'),
			mark: on('np-mark'),
			back: on('np-back'),
			kind: on('np-kind'),
			pos: on('np-pos'),
			actions: on('np-actions'),
			rail: on('np-rail'),
			value: root.querySelector('[name="np-value"]').value,
			logo: on('np-logo'),
			icons: on('np-icons'),
			news: on('np-news'),
			cta: on('np-cta'),
			burger: on('np-burger'),
			progress: on('np-progress'),
			shell: val('np-shell'),
			track: val('np-track'),
			accent: val('np-accent')
		};
	};

	// The attributes the row carries, in the order they read best.
	var attrs = function (s) {
		var a = [];
		if (s.tone !== 'paper') a.push(['data-tone', s.tone]);
		if (s.density !== 'regular') a.push(['data-density', s.density]);
		if (s.mark) a.push(['data-mark', 'pos']);
		var style = [];
		if (s.rail) style.push('--value:' + s.value + '%');
		if (s.prefix) style.push("--pos-prefix:'" + s.prefix + "'");
		if (style.length) a.push(['style', style.join('; ')]);
		return a;
	};

	var LOGO = '<span class="logo logo-sm">Swarn<span class="logo__i">\u0131' +
		'<i class="logo__tittle"></i></span>l</span>';

	var ICON = function (id, label) {
		return '<a class="nav-icon" href="#i" aria-label="' + label + '">' +
			'<svg class="icon" aria-hidden="true"><use href="#i-' + id + '"/></svg></a>';
	};

	var mainRow = function (s) {
		var html = s.logo ? LOGO : '';
		html += '<div class="nav-links"><a class="nav-link" href="#i">Watch</a>' +
			'<a class="nav-link" href="#i" aria-current="page">Learn</a>' +
			'<a class="nav-link" href="#i">Build</a></div>';
		html += '<div class="nav-actions">';
		if (s.icons) {
			html += '<div class="nav-icons">' + ICON('code', 'GitHub') +
				ICON('chat', 'Chat') + ICON('share', 'Share') + '</div>';
		}
		if (s.news) {
			html += '<details class="nav-form"><summary aria-label="Subscribe">' +
				'<svg class="icon" aria-hidden="true"><use href="#i-mail"/></svg></summary>' +
				'<form class="nav-form__field" onsubmit="return false">' +
				'<input type="email" placeholder="you@example.com" aria-label="Email" />' +
				'<button class="btn btn-primary btn-sm btn-pill" type="submit">Join</button>' +
				'</form></details>';
		}
		if (s.cta) html += '<button class="btn btn-primary btn-sm btn-pill" type="button">Subscribe</button>';
		if (s.burger) {
			html += '<button class="nav-burger nav-burger-rec" type="button" aria-expanded="false" ' +
				'data-burger><span class="nav-burger__box"><span class="nav-burger__bars"></span>' +
				'</span><span class="u-sr-only">Menu</span></button>';
		}
		if (!s.icons && !s.news && !s.cta && !s.burger) html += '<span class="dot dot-sm"></span>';
		return html + '</div>';
	};

	var render = function () {
		var s = state();

		bar.innerHTML = mainRow(s);

		// The stage is a box on a docs page, so it cannot actually be fixed —
		// the class is set for the markup's sake and the demo stays static.
		shell.classList.remove('nav-shell-fixed', 'nav-shell-morph', 'nav-shell-auto');
		if (s.shell !== 'island') shell.classList.add('nav-shell-' + s.shell);

		if (s.accent) shell.style.setProperty('--accent', s.accent);
		else shell.style.removeProperty('--accent');

		if (s.track === 'accent') shell.setAttribute('data-track', 'accent');
		else shell.removeAttribute('data-track');

		shell.classList.toggle('nav-progress', s.progress);
		if (s.progress) shell.style.setProperty('--progress', s.value + '%');
		else shell.style.removeProperty('--progress');

		sub.setAttribute('class', 'nav-sub nav-context');
		['data-tone', 'data-density', 'data-mark', 'style'].forEach(function (k) {
			sub.removeAttribute(k);
		});
		attrs(s).forEach(function (pair) { sub.setAttribute(pair[0], pair[1]); });

		var html = '';
		if (s.back) html += '<a class="nav-context__back" href="#i">← Courses</a>';
		html += '<span class="nav-context__where">';
		if (s.kind) html += '<span class="nav-context__kind">Course</span>';
		html += '<span class="nav-context__title">Handlebars without tears</span>';
		if (s.pos) html += '<span class="nav-context__pos">3 of 14</span>';
		html += '</span>';
		if (s.actions) {
			html += '<div class="nav-context__actions">' +
				'<button class="btn btn-quiet btn-sm" type="button">← Prev</button>' +
				'<button class="btn btn-primary btn-sm" type="button">Next →</button></div>';
		}
		if (s.rail) html += '<span class="nav-rail"></span>';
		sub.innerHTML = html;

		if (readout) readout.textContent = s.value + '%';
		print(s);
	};

	// The markup, built from the same state — never serialised from the DOM,
	// so nothing the browser normalises leaks into what people paste.
	var print = function (s) {
		var attrText = attrs(s).map(function (p) {
			return ' ' + p[0] + '="' + p[1] + '"';
		}).join('');

		var shellCls = 'nav-shell' +
			(s.shell !== 'island' ? ' nav-shell-' + s.shell : '') +
			(s.progress ? ' nav-progress' : '');
		var styles = [];
		if (s.progress) styles.push('--progress:' + s.value + '%');
		if (s.accent) styles.push('--accent:' + s.accent);
		var shellStyle = styles.length ? ' style="' + styles.join('; ') + '"' : '';
		if (s.progress && s.track === 'accent') shellCls += '" data-track="accent';

		var L = ['<div class="' + shellCls + '"' + shellStyle + '>', '\t<div class="nav-stack">'];
		L.push('\t\t<nav class="nav-bar" aria-label="Main">');
		if (s.logo) L.push('\t\t\t<a class="logo logo-sm" href="/">…</a>');
		L.push('\t\t\t<div class="nav-links">… links …</div>');
		L.push('\t\t\t<div class="nav-actions">');
		if (s.icons) L.push('\t\t\t\t<div class="nav-icons">… social …</div>');
		if (s.news) L.push('\t\t\t\t<details class="nav-form">… newsletter …</details>');
		if (s.cta) L.push('\t\t\t\t<button class="btn btn-primary btn-sm btn-pill">Subscribe</button>');
		if (s.burger) L.push('\t\t\t\t<button class="nav-burger nav-burger-rec" aria-expanded="false">…</button>');
		L.push('\t\t\t</div>');
		L.push('\t\t</nav>');
		L.push('\t\t<div class="nav-sub nav-context"' + attrText + '>');
		if (s.back) L.push('\t\t\t<a class="nav-context__back" href="/courses">← Courses</a>');
		L.push('\t\t\t<span class="nav-context__where">');
		if (s.kind) L.push('\t\t\t\t<span class="nav-context__kind">Course</span>');
		L.push('\t\t\t\t<span class="nav-context__title">Handlebars without tears</span>');
		if (s.pos) L.push('\t\t\t\t<span class="nav-context__pos">3 of 14</span>');
		L.push('\t\t\t</span>');
		if (s.actions) {
			L.push('\t\t\t<div class="nav-context__actions">');
			L.push('\t\t\t\t<button class="btn btn-quiet btn-sm">← Prev</button>');
			L.push('\t\t\t\t<button class="btn btn-primary btn-sm">Next →</button>');
			L.push('\t\t\t</div>');
		}
		if (s.rail) L.push('\t\t\t<span class="nav-rail"></span>');
		L.push('\t\t</div>', '\t</div>', '</div>');

		if (!out.firstChild) {
			out.innerHTML =
				'<figure class="codebox codebox-light u-m-0" data-play="off">' +
				'<figcaption class="codebox__head"><span class="codebox__lang">html</span>' +
				'<button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>' +
				'<pre class="codebox__pre"><code class="codebox__ln"></code></pre></figure>';
		}
		var codeEl = out.querySelector('code');
		codeEl.removeAttribute('data-raw');
		codeEl.textContent = L.join('\n');
		if (window.CreatorHighlight) {
			window.CreatorHighlight.el(codeEl, { lang: 'html', lines: true });
		}
	};

	root.addEventListener('input', function (e) {
		if (e.target.name === 'np-preset') {
			apply(e.target.value);
		} else if (e.target.name) {
			var custom = root.querySelector('[name="np-preset"][value="custom"]');
			if (custom) custom.checked = true;
		}
		render();
	});

	apply('series');
	render();
})();
