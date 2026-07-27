/* =============================================================================
   COLLECTION FILTERS
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
			if (state.facets.length) bits.push(state.facets.join(' · '));
			crumb.textContent = bits.length ? bits.join(' → ') : 'Everywhere';
		}
		var reset = root.querySelector('[data-filter-reset]');
		if (reset) reset.hidden = !(state.group || state.place || state.facets.length);
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
