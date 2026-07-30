/* =============================================================================
   COLLECTION BEHAVIOUR
   Three independent modules, in this file because they ship together and none
   of them is big enough to be a file:

     1. the linked filters   — region narrows countries, country narrows cities
     2. the panels           — the tabs under a player
     3. the lesson player    — mark complete, and the shortcuts it advertises

   All three obey the same rule as src/nav.js: they only ever set attributes the
   stylesheet already understands. Blocked, the filters show everything, the
   panels stack under their own headings and the player is still a list of
   links — which is the correct fallback for each.
   ========================================================================== */


/* =============================================================================
   1 · FILTERS
   Region narrows countries, country narrows cities, facets narrow everything.
   Nothing here is travel-specific: it reads data attributes, so any collection
   with groups, places and spots gets the same behaviour for free.

     data-group="asia"              on a group button
     data-place="japan" data-of="asia"      on a place (data-of may be a list)
     data-spot="tokyo"  data-of="japan"     on a spot
     data-facet="beach"             on a facet checkbox
     data-tags="beach city"         on anything a facet should match

   The script only ever sets data-filtered="out"; the stylesheet decides that
   this means display:none. With the script blocked, everything shows — which
   is the correct fallback for a page whose job is listing things.
   ========================================================================== */
(function () {
	'use strict';

	var root = document.querySelector('[data-collection]');
	if (!root) return;

	var state = { group: null, place: null, facets: [] };

	var all = function (sel) { return [].slice.call(root.querySelectorAll(sel)); };

	var show = function (el, on) {
		if (on) el.removeAttribute('data-filtered');
		else el.setAttribute('data-filtered', 'out');
	};

	/* A thing survives the facets if it carries at least one selected tag.
	   Or-within-a-facet is the honest reading of "beach, mountains": someone
	   ticking both wants either, not somewhere that is somehow both. */
	/* A place can sit in more than one group — a trip that crossed a border,
	   a post tagged with two countries — so the parent attributes are read as
	   lists. One value is just a list of one. */
	var inList = function (attr, want) {
		if (!want) return true;
		return (attr || '').split(/\s+/).indexOf(want) !== -1;
	};

	var passesFacets = function (el) {
		if (!state.facets.length) return true;
		var tags = (el.getAttribute('data-tags') || '').split(/\s+/);
		return state.facets.some(function (f) { return tags.indexOf(f) !== -1; });
	};

	var apply = function () {
		all('[data-place]').forEach(function (el) {
			var inGroup = inList(el.getAttribute('data-of'), state.group);
			show(el, inGroup && passesFacets(el));
			if (!inGroup) el.setAttribute('aria-pressed', 'false');
		});

		// A city belongs to a country, and a country to a region — so a city
		// survives only if its country did.
		all('[data-spot]').forEach(function (el) {
			var of = el.getAttribute('data-of');
			var parent = root.querySelector('[data-place="' + of + '"]');
			var parentShown = !parent || !parent.hasAttribute('data-filtered');
			var inPlace = !state.place || of === state.place;
			show(el, parentShown && inPlace && passesFacets(el));
		});

		all('[data-post]').forEach(function (el) {
			var of = el.getAttribute('data-of');
			var region = el.getAttribute('data-region');
			var okGroup = inList(region, state.group);
			var okPlace = inList(of, state.place);
			show(el, okGroup && okPlace && passesFacets(el));
		});

		all('[data-group]').forEach(function (el) {
			el.setAttribute('aria-pressed', String(el.getAttribute('data-group') === state.group));
		});
		all('[data-place]').forEach(function (el) {
			el.setAttribute('aria-pressed', String(el.getAttribute('data-place') === state.place));
		});

		// Every list says when it has nothing left, rather than collapsing.
		all('[data-empty-for]').forEach(function (msg) {
			var sel = msg.getAttribute('data-empty-for');
			var left = all(sel).filter(function (el) { return !el.hasAttribute('data-filtered'); });
			msg.hidden = left.length > 0;
		});

		// What the reader has narrowed to, in words, plus a way back out.
		var crumb = root.querySelector('[data-filter-state]');
		if (crumb) {
			var bits = [];
			if (state.group) bits.push(label('[data-group="' + state.group + '"]'));
			if (state.place) bits.push(label('[data-place="' + state.place + '"]'));
			if (state.facets.length) bits.push(state.facets.map(facetLabel).join(' · '));
			crumb.textContent = bits.length ? bits.join(' → ') : 'Everywhere';
		}
		var reset = root.querySelector('[data-filter-reset]');
		if (reset) reset.hidden = !(state.group || state.place || state.facets.length);
	};

	/* A facet's value is an id — often a slug the reader never sees. The crumb
	   should say what the checkbox says, so read the label back off the DOM. */
	var facetLabel = function (v) {
		var box = root.querySelector('[data-facet="' + v + '"]');
		var wrap = box && box.closest('label');
		var text = wrap && wrap.querySelector('span:not(.col-facet__n)');
		return text ? text.textContent.trim() : v;
	};

	var label = function (sel) {
		var el = root.querySelector(sel);
		if (!el) return '';
		var n = el.querySelector('.col-group__name, .col-place__name');
		return (n ? n.textContent : el.textContent).trim();
	};

	root.addEventListener('click', function (e) {
		var g = e.target.closest('[data-group]');
		if (g) {
			var gv = g.getAttribute('data-group');
			// Choosing a different region drops the country under the old one,
			// which would otherwise filter to nothing and look broken.
			state.group = state.group === gv ? null : gv;
			state.place = null;
			apply();
			return;
		}

		var p = e.target.closest('[data-place]');
		if (p) {
			var pv = p.getAttribute('data-place');
			state.place = state.place === pv ? null : pv;
			if (state.place) state.group = p.getAttribute('data-of');
			apply();
			return;
		}

		if (e.target.closest('[data-filter-reset]')) {
			state = { group: null, place: null, facets: [] };
			all('[data-facet]').forEach(function (f) { f.checked = false; });
			apply();
		}
	});

	root.addEventListener('change', function (e) {
		if (!e.target.matches('[data-facet]')) return;
		state.facets = all('[data-facet]:checked').map(function (f) {
			return f.getAttribute('data-facet');
		});
		apply();
	});

	apply();
})();


/* =============================================================================
   2 · PANELS
   The tabs under a player. Markup:

     <div data-tabs>
       <div class="tabs" role="tablist">
         <button class="tab" role="tab" aria-controls="p-notes">Notes</button>
       <div class="col-panel" id="p-notes" role="tabpanel">
         <span class="col-panel__label">Notes</span>

   Until this runs, every panel is visible under its own heading — four blocks
   of content that all belong to the lesson, stacked. Only once the script sets
   data-tabs="ready" does the stylesheet hide the headings, which is why the
   no-JS page is readable rather than a pile of unlabelled sections.
   ========================================================================== */
(function () {
	'use strict';

	[].slice.call(document.querySelectorAll('[data-tabs]')).forEach(function (root) {
		var tabs = [].slice.call(root.querySelectorAll('[role="tab"]'));
		if (!tabs.length) return;

		var panelOf = function (tab) {
			return document.getElementById(tab.getAttribute('aria-controls'));
		};

		var select = function (tab, focus) {
			tabs.forEach(function (t) {
				var on = t === tab;
				t.setAttribute('aria-selected', String(on));
				// Only the selected tab is in the tab order; the arrows move
				// between them. That is the tablist pattern, and it is why a
				// four-tab strip costs one Tab press rather than four.
				t.tabIndex = on ? 0 : -1;
				var p = panelOf(t);
				if (p) p.hidden = !on;
			});
			if (focus) tab.focus();
		};

		root.setAttribute('data-tabs', 'ready');
		select(tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0] || tabs[0]);

		root.addEventListener('click', function (e) {
			var t = e.target.closest('[role="tab"]');
			if (t) { e.preventDefault(); select(t); }
		});

		root.addEventListener('keydown', function (e) {
			var i = tabs.indexOf(e.target);
			if (i === -1) return;
			var step = { ArrowRight: 1, ArrowLeft: -1, Home: -i, End: tabs.length - 1 - i }[e.key];
			if (step === undefined) return;
			e.preventDefault();
			select(tabs[(i + step + tabs.length) % tabs.length], true);
		});
	});
})();


/* =============================================================================
   3 · THE LESSON PLAYER
   Marking a lesson done, and the shortcuts the page tells you about.

     [data-player]                  the stage
     [data-done-toggle]             the button
     .lesson-row[aria-current]      the lesson it applies to
     [data-progress]                the bar to redraw   (--value)
     [data-progress-count]          "12 of 42" next to it
     [data-step="next"|"prev"]      the two links the shortcuts follow

   Nothing is stored. A real course puts this on the server, and a demo that
   wrote to localStorage would be teaching a persistence trick rather than a
   design system.
   ========================================================================== */
(function () {
	'use strict';

	var root = document.querySelector('[data-player]');
	if (!root) return;

	var rows = function () {
		return [].slice.call(root.querySelectorAll('.lesson-row'));
	};

	var redraw = function () {
		var all = rows();
		var done = all.filter(function (r) { return r.hasAttribute('data-done'); }).length;
		var pct = all.length ? Math.round((done / all.length) * 100) : 0;

		var bar = root.querySelector('[data-progress]');
		if (bar) {
			bar.style.setProperty('--value', pct + '%');
			var meter = bar.closest('[role="progressbar"]') || bar.parentElement;
			if (meter) meter.setAttribute('aria-valuenow', String(pct));
		}
		[].slice.call(root.querySelectorAll('[data-progress-count]')).forEach(function (el) {
			el.textContent = el.getAttribute('data-progress-count')
				.replace('{done}', done).replace('{all}', all.length).replace('{pct}', pct);
		});

		// A module's own count has to move with the total, or the header says
		// 1/4 next to two ticked rows and the reader trusts neither number.
		[].slice.call(root.querySelectorAll('[data-module-count]')).forEach(function (el) {
			var mod = el.closest('details');
			var in_ = mod ? [].slice.call(mod.querySelectorAll('.lesson-row')) : [];
			el.textContent = in_.filter(function (r) {
				return r.hasAttribute('data-done');
			}).length + '/' + in_.length;
		});

		var btn = root.querySelector('[data-done-toggle]');
		var here = root.querySelector('.lesson-row[aria-current]');
		if (btn && here) {
			var on = here.hasAttribute('data-done');
			btn.setAttribute('aria-pressed', String(on));
			btn.textContent = on ? 'Completed' : 'Mark complete';
		}
	};

	var toggle = function () {
		var here = root.querySelector('.lesson-row[aria-current]');
		if (!here) return;
		if (here.hasAttribute('data-done')) here.removeAttribute('data-done');
		else here.setAttribute('data-done', '');
		redraw();
	};

	root.addEventListener('click', function (e) {
		if (e.target.closest('[data-done-toggle]')) { e.preventDefault(); toggle(); }
	});

	// The shortcuts the keys widget lists. Typing a note must not skip the
	// lesson, so anything with a caret in it keeps its keystrokes.
	document.addEventListener('keydown', function (e) {
		if (e.metaKey || e.ctrlKey || e.altKey) return;
		var t = e.target;
		if (t.closest('input, textarea, select, [contenteditable]')) return;

		if (e.key === 'm') { e.preventDefault(); toggle(); return; }

		var dir = { n: 'next', p: 'prev' }[e.key];
		if (!dir) return;
		var step = root.querySelector('[data-step="' + dir + '"]');
		if (step && step.getAttribute('aria-disabled') !== 'true') {
			e.preventDefault();
			step.click();
		}
	});

	redraw();
})();


/* ── Copy to clipboard ────────────────────────────────────────────────────────
   [data-copy] copies text and says so. Delegated from the document, so it works
   for buttons added after load.

   Where the text comes from, in order:
     data-copy="<selector>"  the matched element's text
     [data-copy-src]         the nearest one inside the same container
     otherwise               the nearest <pre>/<code> in the same figure/card

   This lived only in docs/preview.js before, which meant every copy button on a
   collection page rendered and did nothing — the worst kind of broken, because
   it looks fine.
   ------------------------------------------------------------------------- */
(function () {
	var doc = document;

	function sourceFor(btn) {
		var sel = btn.getAttribute('data-copy');
		if (sel) {
			var bySel = doc.querySelector(sel);
			if (bySel) return bySel;
		}
		var scope = btn.closest('figure, .card, .c, .col-widget, form, section') || doc;
		return scope.querySelector('[data-copy-src]') ||
			scope.querySelector('textarea, pre code, pre, code');
	}

	function textOf(el) {
		if (!el) return '';
		// A textarea/input holds its value, which is what an edited prompt needs.
		return ('value' in el && el.value !== undefined) ? el.value : el.innerText;
	}

	function flash(btn, msg) {
		if (btn.dataset.busy) return;
		btn.dataset.busy = '1';
		var was = btn.textContent;
		btn.textContent = msg;
		btn.setAttribute('aria-live', 'polite');
		setTimeout(function () {
			btn.textContent = was;
			delete btn.dataset.busy;
		}, 1400);
	}

	doc.addEventListener('click', function (e) {
		var btn = e.target.closest('[data-copy]');
		if (!btn) return;
		e.preventDefault();

		var text = textOf(sourceFor(btn)).trim();
		if (!text) return;

		if (navigator.clipboard && navigator.clipboard.writeText) {
			navigator.clipboard.writeText(text)
				.then(function () { flash(btn, 'Copied'); })
				.catch(function () { flash(btn, 'Press ⌘C'); });
		} else {
			// No clipboard API (or no secure context): select it so the keyboard
			// shortcut works rather than failing silently.
			var ta = doc.createElement('textarea');
			ta.value = text;
			ta.setAttribute('readonly', '');
			ta.style.cssText = 'position:fixed;top:-1000px';
			doc.body.appendChild(ta);
			ta.select();
			var ok = false;
			try { ok = doc.execCommand('copy'); } catch (err) { ok = false; }
			doc.body.removeChild(ta);
			flash(btn, ok ? 'Copied' : 'Press ⌘C');
		}
	});
})();
