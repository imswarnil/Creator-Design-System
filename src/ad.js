/* =============================================================================
   CREATOR AD — lazy load and the reader's hide switch, in one small module.
   Same rule as nav.js and collection.js: this only ever sets an attribute the
   stylesheet (34-ad.css) already understands. No IntersectionObserver → every
   slot just loads immediately, which is the correct fallback, not a bug.

     data-ad-state   idle → loading → loaded, or hidden — on .ad itself
   ========================================================================== */
(function (global) {
	'use strict';

	var doc = global.document;
	if (!doc) return;

	function setState(el, state) {
		el.setAttribute('data-ad-state', state);
	}

	function load(el) {
		if (el.getAttribute('data-ad-state') !== 'idle') return;
		setState(el, 'loading');
		/* Real ad networks are async; a fixed 0ms "load" would make the
		   skeleton pointless. There is nothing to actually fetch here — this
		   delay is standing in for that round trip, nothing more. */
		global.setTimeout(function () {
			setState(el, 'loaded');
		}, 300 + Math.round(Math.random() * 400));
	}

	function init() {
		var ads = [].slice.call(doc.querySelectorAll('[data-ad]'));
		if (!ads.length) return;

		ads.forEach(function (el) {
			setState(el, 'idle');
			var hideBtn = el.querySelector('[data-ad-hide]');
			if (hideBtn) {
				hideBtn.addEventListener('click', function () { setState(el, 'hidden'); });
			}
		});

		if (!('IntersectionObserver' in global)) {
			ads.forEach(load);
			return;
		}

		var io = new IntersectionObserver(function (entries) {
			entries.forEach(function (entry) {
				if (entry.isIntersecting) {
					load(entry.target);
					io.unobserve(entry.target);
				}
			});
		}, { rootMargin: '200px 0px' });

		ads.forEach(function (el) { io.observe(el); });
	}

	if (doc.readyState === 'loading') {
		doc.addEventListener('DOMContentLoaded', init);
	} else {
		init();
	}
})(window);
