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

/* ── Navbar builder ──────────────────────────────────────────────────────────
   Everything the panel can set maps to something the component already
   understands — a class, a data attribute or a custom property. The preview and
   the printed markup are rendered from the same state object and never from
   each other, so what you copy is always what you are looking at.

   The one deliberate difference: the stage cannot really be fixed or pinned
   inside a docs page, so positioning classes are written into the markup but
   not applied to the preview. The panel says so rather than pretending. */
(function () {
	var root = document.querySelector('[data-nav-playground]');
	if (!root) return;

	var stage = root.querySelector('[data-np-stage]');
	var media = root.querySelector('[data-np-media]');
	var shell = root.querySelector('[data-np-shell]');
	var bar = root.querySelector('[data-np-bar]');
	var out = root.querySelector('[data-np-code]');

	var val = function (n) {
		var el = root.querySelector('[name="' + n + '"]:checked') ||
			root.querySelector('[name="' + n + '"]');
		return el ? el.value : '';
	};
	var on = function (n) {
		var el = root.querySelector('[name="' + n + '"]');
		return !!(el && el.checked);
	};

	var state = function () {
		return {
			collection: val('np-collection'),
			shell: val('np-shell'),
			markPos: val('np-mark-pos'),
			linksAlign: val('np-links-align'),
			width: val('np-width'),
			height: +val('np-height'),
			radius: +val('np-radius'),
			border: on('np-border'), shadow: on('np-shadow'), blur: on('np-blur'),
			theme: val('np-theme'),
			accent: val('np-accent'), bg: val('np-bg'),
			active: val('np-active'),
			brand: val('np-brand').trim() || 'creator',
			links: val('np-links').split(',').map(function (t) { return t.trim(); })
				.filter(Boolean),
			cta: val('np-cta').trim() || 'Subscribe',
			logo: on('np-logo'), icons: on('np-icons'), news: on('np-news'),
			ctaOn: on('np-cta-on'), search: on('np-search'), burger: on('np-burger'),
			drop: val('np-drop'), burgerStyle: val('np-burger-style'),
			mobile: val('np-mobile'),
			progress: on('np-progress'), track: val('np-track'), value: val('np-value')
		};
	};

	/* The classes the bar carries, in the order a person would write them. */
	var barClasses = function (s) {
		var c = ['nav-bar'];
		if (s.collection) c.push('nav-' + s.collection);
		if (s.markPos === 'center') c.push('nav-bar-center');
		if (s.active === 'rule') c.push('nav-links-rule');
		if (s.active === 'soft') c.push('nav-links-soft');
		return c;
	};

	var shellClasses = function (s) {
		var c = ['nav-shell'];
		if (s.shell === 'fixed') c.push('nav-shell-fixed');
		if (s.shell === 'morph') c.push('nav-shell-morph');
		if (s.shell === 'auto') c.push('nav-shell-auto');
		if (s.shell === 'over') c.push('nav-over', 'nav-shell-full');
		if (s.width === 'wide') c.push('nav-s-wide');
		if (s.width === 'full') c.push('nav-shell-full');
		if (s.progress) c.push('nav-progress');
		return c;
	};

	/* Only the properties the reader actually changed — a style attribute full
	   of defaults is noise in something you are about to paste. */
	var barVars = function (s) {
		var v = [];
		if (s.height !== 56) v.push('--bar-h:' + s.height + 'px');
		if (s.radius !== 40) v.push('--bar-radius:' + (s.radius >= 40 ? 'var(--radius-pill)' : s.radius + 'px'));
		if (s.bg) v.push('--bar-bg:' + s.bg);
		if (!s.border) v.push('--bar-line:transparent');
		if (!s.blur) v.push('--bar-blur:none');
		return v;
	};

	var shellVars = function (s) {
		var v = [];
		if (s.accent) v.push('--accent:' + s.accent);
		if (s.progress) v.push('--progress:' + s.value + '%');
		return v;
	};

	var ICONS = { code: 'GitHub', chat: 'Chat', share: 'Share' };

	var actionsHTML = function (s) {
		var h = '<div class="nav-actions">';
		if (s.search) {
			h += '<button class="nav-icon" type="button" aria-label="Search">' +
				'<svg class="icon" aria-hidden="true"><use href="#i-search"/></svg></button>';
		}
		if (s.icons) {
			h += '<div class="nav-icons">';
			Object.keys(ICONS).forEach(function (k) {
				h += '<a class="nav-icon" href="#i" aria-label="' + ICONS[k] + '">' +
					'<svg class="icon" aria-hidden="true"><use href="#i-' + k + '"/></svg></a>';
			});
			h += '</div>';
		}
		if (s.news) {
			h += '<details class="nav-form"><summary aria-label="Subscribe">' +
				'<svg class="icon" aria-hidden="true"><use href="#i-mail"/></svg></summary>' +
				'<form class="nav-form__field" onsubmit="return false">' +
				'<input type="email" placeholder="you@example.com" aria-label="Email" />' +
				'<button class="btn btn-primary btn-sm btn-pill" type="submit">Join</button>' +
				'</form></details>';
		}
		if (s.ctaOn) {
			h += '<button class="btn btn-primary btn-sm btn-pill" type="button">' +
				s.cta + '</button>';
		}
		if (s.burger) {
			var cls = 'nav-burger' + (s.burgerStyle ? ' nav-burger-' + s.burgerStyle : '');
			h += '<button class="' + cls + '" type="button" aria-expanded="false" data-burger>' +
				'<span class="nav-burger__box"><span class="nav-burger__bars"></span></span>' +
				'<span class="u-sr-only">Menu</span></button>';
		}
		if (!s.search && !s.icons && !s.news && !s.ctaOn && !s.burger) {
			h += '<span class="dot dot-sm"></span>';
		}
		return h + '</div>';
	};

	var MARK = function (word) {
		var i = word.toLowerCase().indexOf('o');
		if (i === -1) return '<span class="cds-mark__word">' + word + '</span>';
		return '<span class="cds-mark__word">' + word.slice(0, i) +
			'<i class="cds-mark__o" aria-hidden="true"></i>' +
			'<span class="u-sr-only">' + word[i] + '</span>' + word.slice(i + 1) + '</span>';
	};

	var render = function () {
		var s = state();

		stage.setAttribute('data-theme', s.theme);
		media.hidden = s.shell !== 'over';
		stage.classList.toggle('np__stage-over', s.shell === 'over');

		// The shell classes that would pin the bar are written to the markup but
		// not to the stage, which is a box on a page and cannot be pinned.
		var live = shellClasses(s).filter(function (c) {
			return ['nav-shell-fixed', 'nav-shell-auto', 'nav-shell-morph'].indexOf(c) === -1;
		});
		shell.className = live.join(' ');
		shell.setAttribute('style', shellVars(s).join(';'));
		if (s.progress && s.track === 'accent') shell.setAttribute('data-track', 'accent');
		else shell.removeAttribute('data-track');

		bar.className = barClasses(s).join(' ');
		bar.setAttribute('style', barVars(s).join(';'));
		if (!s.shadow) bar.style.boxShadow = 'none';

		var linksCls = 'nav-links';
		var linkStyle = s.linksAlign === 'center' ? ' style="margin-inline:auto"'
			: (s.linksAlign === 'end' ? ' style="margin-left:auto"' : ' style="margin-right:auto"');
		var h = s.logo ? '<span class="cds-mark">' + MARK(s.brand) + '</span>' : '';
		h += '<div class="' + linksCls + '"' + linkStyle + '>';
		s.links.forEach(function (label, i) {
			var cur = i === 1 ? ' aria-current="page"' : '';
			var menu = (i === 1 && s.drop === 'hover');
			if (menu) {
				h += '<details class="nav-menu nav-menu-hover nav-menu-grow">' +
					'<summary class="nav-link"' + cur + '>' + label + '</summary>' +
					'<div class="nav-menu__panel">' +
					'<a class="dropdown__item" href="#i">Everything</a>' +
					'<a class="dropdown__item" href="#i">Latest</a></div></details>';
			} else {
				h += '<a class="nav-link" href="#i"' + cur + '>' + label + '</a>';
			}
		});
		h += '</div>' + actionsHTML(s);
		bar.innerHTML = h;

		root.querySelectorAll('[data-out]').forEach(function (o) {
			var n = o.getAttribute('data-out');
			var unit = n === 'np-value' ? '%' : 'px';
			o.textContent = val(n) + unit;
		});

		print(s);
	};

	var attr = function (name, value) { return value ? ' ' + name + '="' + value + '"' : ''; };

	var print = function (s) {
		var L = [];
		if (s.shell === 'over') L.push('<div class="nav-over__media">… your video or poster …</div>');

		L.push('<header class="' + shellClasses(s).join(' ') + '"' +
			attr('style', shellVars(s).join('; ')) +
			(s.progress && s.track === 'accent' ? ' data-track="accent"' : '') + '>');
		L.push('\t<nav class="' + barClasses(s).join(' ') + '"' +
			attr('style', barVars(s).join('; ')) + ' aria-label="Main">');

		if (s.logo) L.push('\t\t<a class="cds-mark" href="/">' + s.brand + '</a>');
		L.push('\t\t<div class="nav-links">');
		s.links.forEach(function (label, i) {
			if (i === 1 && s.drop === 'hover') {
				L.push('\t\t\t<details class="nav-menu nav-menu-hover nav-menu-grow">');
				L.push('\t\t\t\t<summary class="nav-link">' + label + '</summary>');
				L.push('\t\t\t\t<div class="nav-menu__panel">… items …</div>');
				L.push('\t\t\t</details>');
			} else {
				L.push('\t\t\t<a class="nav-link" href="/' + label.toLowerCase() + '/"' +
					(i === 1 ? ' aria-current="page"' : '') + '>' + label + '</a>');
			}
		});
		L.push('\t\t</div>');

		L.push('\t\t<div class="nav-actions">');
		if (s.search) L.push('\t\t\t<button class="nav-icon" aria-label="Search">…</button>');
		if (s.icons) L.push('\t\t\t<div class="nav-icons">… social …</div>');
		if (s.news) L.push('\t\t\t<details class="nav-form">… newsletter …</details>');
		if (s.ctaOn) L.push('\t\t\t<a class="btn btn-primary btn-sm btn-pill" href="/subscribe/">' +
			s.cta + '</a>');
		if (s.burger) {
			L.push('\t\t\t<button class="nav-burger' +
				(s.burgerStyle ? ' nav-burger-' + s.burgerStyle : '') +
				'" aria-expanded="false" aria-controls="menu">…</button>');
		}
		L.push('\t\t</div>');
		L.push('\t</nav>');
		L.push('</header>');

		if (s.burger) {
			L.push('');
			L.push(s.mobile === 'panel'
				? '<!-- .nav-panel inside the shell; data-panel-toggle on the burger -->'
				: '<dialog class="nav-sheet' + (s.mobile === 'drop' ? ' nav-sheet-drop' : '') +
				  '" id="menu">…</dialog>');
		}
		if (s.shell === 'morph' || s.shell === 'auto' || s.shell === 'over') {
			L.push('<script src="creator-design-system/src/nav.js" defer><\/script>');
		}

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

	// A collection carries its own sensible defaults; picking one stamps the
	// controls and then gets out of the way.
	var PRESETS = {
		video: { shell: 'over', bg: 'transparent', border: false, blur: false,
			icons: true, ctaOn: true, burger: true, radius: 0 },
		blog: { shell: 'auto', width: 'full', radius: 0, border: false, blur: false,
			news: true, ctaOn: false },
		'course-bar': { shell: 'island', progress: true, ctaOn: false, radius: 12 },
		shop: { shell: 'fixed', radius: 8, ctaOn: true, search: true },
		trip: { shell: 'morph', radius: 20 },
		'docs-bar': { shell: 'fixed', width: 'full', height: 44, radius: 0, search: true,
			ctaOn: false, blur: false }
	};

	var apply = function (key) {
		var conf = PRESETS[key];
		if (!conf) return;
		var set = function (name, v) {
			var el = root.querySelector('[name="' + name + '"][value="' + v + '"]') ||
				root.querySelector('[name="' + name + '"]');
			if (!el) return;
			if (el.type === 'radio') el.checked = true;
			else el.value = v;
		};
		var tick = function (name, v) {
			var el = root.querySelector('[name="' + name + '"]');
			if (el) el.checked = v;
		};
		if (conf.shell) set('np-shell', conf.shell);
		if (conf.width) set('np-width', conf.width);
		if (conf.bg !== undefined) set('np-bg', conf.bg);
		if (conf.height !== undefined) set('np-height', conf.height);
		if (conf.radius !== undefined) set('np-radius', conf.radius);
		['border', 'shadow', 'blur', 'icons', 'news', 'search', 'burger', 'progress']
			.forEach(function (k) { if (conf[k] !== undefined) tick('np-' + k, conf[k]); });
		if (conf.ctaOn !== undefined) tick('np-cta-on', conf.ctaOn);
	};

	root.addEventListener('input', function (e) {
		if (e.target.name === 'np-collection') apply(e.target.value);
		render();
	});

	render();
})();
