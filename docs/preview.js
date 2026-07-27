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
			var text = src ? src.textContent.trim() : '';
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
	var links = Array.prototype.slice.call(
		document.querySelectorAll(".doc-side__nav a[href^='#']")
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
   tidied and escaped, in a copyable block — so the docs can never drift from
   what is actually rendered. */
(function () {
	var tiles = document.querySelectorAll('.demo-tile');
	if (!tiles.length) return;

	var tidy = function (html) {
		// Strip the artefacts of generated markup so the copy is paste-ready.
		return html
			.replace(/<!--[\s\S]*?-->/g, '')
			.replace(/\s+data-(dialog|dialog-close|copy|burger|replay[a-z-]*|install-[a-z]+)(="[^"]*")?/g, '')
			.split('\n').map(function (l) { return l.replace(/\s+$/, ''); })
			.filter(function (l) { return l.trim(); })
			.join('\n');
	};

	var esc = function (s) {
		return s.replace(/[&<>]/g, function (c) {
			return { '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c];
		});
	};

	tiles.forEach(function (tile) {
		var demo = tile.querySelector('.demo');
		if (!demo) return;

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
					'<figure class="codebox codebox-light u-m-0">' +
					'<figcaption class="codebox__head"><span class="codebox__lang">html</span>' +
					'<button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>' +
					'<pre class="codebox__pre"><code>' + esc(tidy(demo.innerHTML)) + '</code></pre></figure>';
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
