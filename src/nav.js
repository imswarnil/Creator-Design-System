/* =============================================================================
   CREATOR NAV — the four things a navbar cannot do in CSS alone.
   No dependency, no build step, and nothing here invents behaviour: every
   handler sets an attribute the stylesheet already understands, so the CSS
   stays the single description of how the bar looks in each state.

     data-scrolled   on .nav-shell-morph / .nav-over — the bar has left the top
     data-dir        on .nav-shell-auto   — which way the reader is going
     data-open       on .nav-shell        — the in-place panel is open

   Plus hover-intent for dropdowns, which lands on the same <details open> the
   click path uses, so there is one open state rather than two.

   Opt out of any of it by leaving the class off. Nothing here runs unless the
   markup asked for it.
   ========================================================================== */
(function (global) {
	'use strict';

	var doc = global.document;
	if (!doc) return;

	var still = global.matchMedia && global.matchMedia('(prefers-reduced-motion: reduce)').matches;

	/* ── Scroll state ────────────────────────────────────────────────────────
	   One listener for every shell on the page, read inside rAF so a fast
	   scroll cannot queue a hundred layout reads. */
	function scroll() {
		var morph = [].slice.call(doc.querySelectorAll('.nav-shell-morph, .nav-over'));
		var auto = [].slice.call(doc.querySelectorAll('.nav-shell-auto'));
		if (!morph.length && !auto.length) return;

		var last = global.scrollY || 0;
		var ticking = false;

		var read = function () {
			var y = global.scrollY || 0;
			var delta = y - last;

			morph.forEach(function (el) {
				var on = y > (parseInt(el.getAttribute('data-scroll-at'), 10) || 24);
				if (on) el.setAttribute('data-scrolled', '');
				else el.removeAttribute('data-scrolled');
			});

			// A few pixels of jitter is not a direction. Near the top the bar is
			// always shown, or a short page could hide it with no way back.
			if (Math.abs(delta) > 6) {
				auto.forEach(function (el) {
					el.setAttribute('data-dir', y < 80 ? 'up' : (delta > 0 ? 'down' : 'up'));
				});
				last = y;
			}
			ticking = false;
		};

		global.addEventListener('scroll', function () {
			if (ticking) return;
			ticking = true;
			global.requestAnimationFrame(read);
		}, { passive: true });

		read();
	}

	/* ── Dropdown hover intent ───────────────────────────────────────────────
	   Pointer users open on hover, but only if they meant it: a cursor crossing
	   a menu on its way somewhere else should not open three panels. Touch is
	   excluded outright — there, hover means the first tap, and stealing it
	   would cost the reader their click. */
	function hover() {
		var menus = doc.querySelectorAll('.nav-menu-hover');
		if (!menus.length) return;
		if (!global.matchMedia || !global.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

		var OPEN = 120, CLOSE = 220;

		[].forEach.call(menus, function (menu) {
			var t = null;
			var clear = function () { global.clearTimeout(t); t = null; };

			menu.addEventListener('pointerenter', function () {
				clear();
				t = global.setTimeout(function () { menu.open = true; }, still ? 0 : OPEN);
			});

			menu.addEventListener('pointerleave', function () {
				clear();
				t = global.setTimeout(function () { menu.open = false; }, still ? 0 : CLOSE);
			});

			// A pointer that comes back before the close fires keeps the panel.
			menu.addEventListener('focusout', function (e) {
				if (!menu.contains(e.relatedTarget)) menu.open = false;
			});
		});
	}

	/* ── One open menu at a time ─────────────────────────────────────────────
	   Two panels open at once is never what was meant, and Escape should close
	   whatever the reader last opened. */
	function exclusive() {
		doc.addEventListener('click', function (e) {
			var inside = e.target.closest('.nav-menu, .nav-mega, .nav-form');
			doc.querySelectorAll('.nav-menu[open], .nav-mega[open], .nav-form[open]')
				.forEach(function (d) { if (d !== inside) d.open = false; });
		});

		doc.addEventListener('keydown', function (e) {
			if (e.key !== 'Escape') return;
			var open = doc.querySelectorAll('.nav-menu[open], .nav-mega[open], .nav-form[open]');
			if (!open.length) return;
			open.forEach(function (d) {
				d.open = false;
				var s = d.querySelector('summary');
				if (s && d.contains(doc.activeElement)) s.focus();
			});
		});
	}

	/* ── The in-place panel ──────────────────────────────────────────────────
	   [data-panel-toggle] flips data-open on its own shell or stack. The button
	   carries aria-expanded, which is what the burger animation reads too — so
	   the glyph and the assistive tree can never disagree. */
	function panel() {
		doc.addEventListener('click', function (e) {
			var btn = e.target.closest('[data-panel-toggle]');
			if (!btn) return;
			/* The stack first: when the island has more than one row the panel
			   is a row of the stack, not of the shell, and the open state has
			   to sit on the panel's own parent for the row to grow. */
			var host = btn.closest('.nav-stack') || btn.closest('.nav-shell');
			if (!host) return;
			var open = host.hasAttribute('data-open');
			if (open) host.removeAttribute('data-open');
			else host.setAttribute('data-open', '');
			btn.setAttribute('aria-expanded', String(!open));
		});

		doc.addEventListener('keydown', function (e) {
			if (e.key !== 'Escape') return;
			doc.querySelectorAll('.nav-shell[data-open], .nav-stack[data-open]').forEach(function (host) {
				host.removeAttribute('data-open');
				var btn = host.querySelector('[data-panel-toggle]');
				if (btn) { btn.setAttribute('aria-expanded', 'false'); btn.focus(); }
			});
		});
	}

	/* ── Dialogs ─────────────────────────────────────────────────────────────
	   [data-nav-open="id"] shows a <dialog>; [data-nav-close] closes its own.
	   aria-expanded is mirrored back on close so the burger returns to bars
	   however the dialog was dismissed — button, Escape or backdrop. */
	function dialogs() {
		doc.addEventListener('click', function (e) {
			var open = e.target.closest('[data-nav-open]');
			if (open) {
				var dlg = doc.getElementById(open.getAttribute('data-nav-open'));
				if (dlg && dlg.showModal) {
					dlg.showModal();
					open.setAttribute('aria-expanded', 'true');
					dlg.__opener = open;
				}
			}
			var close = e.target.closest('[data-nav-close]');
			if (close) {
				var host = close.closest('dialog');
				if (host) host.close();
			}
		});

		doc.querySelectorAll('dialog.nav-sheet').forEach(function (dlg) {
			dlg.addEventListener('close', function () {
				if (dlg.__opener) dlg.__opener.setAttribute('aria-expanded', 'false');
			});
			// Clicking the backdrop — the click lands on the dialog itself.
			dlg.addEventListener('click', function (e) {
				if (e.target === dlg) dlg.close();
			});
		});
	}

	function start() {
		scroll();
		hover();
		exclusive();
		panel();
		dialogs();
	}

	if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', start);
	else start();

	global.CreatorNav = { start: start };
})(typeof window !== 'undefined' ? window : this);
