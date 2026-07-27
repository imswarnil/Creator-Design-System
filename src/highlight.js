/* =============================================================================
   CREATOR HIGHLIGHT — the system's own syntax highlighter.
   No dependency, no build step, no theme of its own: it only emits the five
   token roles the design system already ships (see 2-elements/15-syntax.css),
   so code coloured here obeys the same light/dark contract as everything else.

   Scanners are tiny state machines rather than one mega-regex, because HTML
   and CSS both need to know *where* they are — a name means "tag" inside a
   tag and "text" outside it; a word means "property" inside a block and
   "selector" outside it. Five languages: html, css, js, json, bash.

   Use:
     CreatorHighlight.highlight(code, 'css')   -> token HTML string
     CreatorHighlight.el(codeElement)          -> highlights it in place
     CreatorHighlight.scan(root)               -> does every [data-lang] under root

   Markup contract: language comes from data-lang on the <code>, or from the
   .codebox__lang caption of the enclosing .codebox. Add data-play to a
   .codebox and it settles in the first time it scrolls into view.
   ========================================================================== */
(function (global) {
	'use strict';

	var ENT = { '&': '&amp;', '<': '&lt;', '>': '&gt;' };

	function esc(s) {
		return s.replace(/[&<>]/g, function (c) { return ENT[c]; });
	}

	/* A token that straddles a newline (block comment, template string) is
	   emitted as one span per line, so the caller can split the finished HTML
	   on \n without ever cutting a span in half. */
	function emit(text, cls) {
		if (!cls) return esc(text);
		return text.split('\n').map(function (line) {
			return line ? '<span class="' + cls + '">' + esc(line) + '</span>' : '';
		}).join('\n');
	}

	/* Ordered rules, sticky-matched at the cursor. A rule may carry `when`
	   (skip unless the state says so) and `then` (mutate the state after). */
	function scanner(rules) {
		return function (src) {
			var out = '', i = 0, n = src.length, state = {};
			while (i < n) {
				var hit = null;
				for (var r = 0; r < rules.length; r++) {
					var rule = rules[r];
					if (rule.when && !rule.when(state)) continue;
					rule.re.lastIndex = i;
					var m = rule.re.exec(src);
					if (m && m[0]) { hit = { rule: rule, text: m[0] }; break; }
				}
				if (!hit) { out += esc(src[i]); i += 1; continue; }
				out += emit(hit.text, typeof hit.rule.cls === 'function'
					? hit.rule.cls(state, hit.text) : hit.rule.cls);
				if (hit.rule.then) hit.rule.then(state, hit.text);
				i += hit.text.length;
			}
			return out;
		};
	}

	var y = function (source) { return new RegExp(source, 'y'); };

	/* ── HTML ───────────────────────────────────────────────────────────────
	   Outside a tag everything is text. Inside, the first name is the tag and
	   every later name is an attribute. */
	var inTag = function (s) { return s.tag; };
	var outTag = function (s) { return !s.tag; };

	var HTML = scanner([
		{ re: y('<!--[\\s\\S]*?-->'), cls: 'tok-com' },
		{ re: y('<!\\[CDATA\\[[\\s\\S]*?\\]\\]>'), cls: 'tok-com' },
		{ re: y('<!doctype[^>]*>|<!DOCTYPE[^>]*>'), cls: 'tok-key' },
		{ re: y('</?'), cls: 'tok-punc', when: outTag,
		  then: function (s) { s.tag = true; s.named = false; } },
		{ re: y('[^<]+'), cls: '', when: outTag },
		{ re: y('/?>'), cls: 'tok-punc', when: inTag,
		  then: function (s) { s.tag = false; } },
		{ re: y('"[^"]*"|\'[^\']*\''), cls: 'tok-str', when: inTag },
		{ re: y('='), cls: 'tok-punc', when: inTag },
		{ re: y('[A-Za-z_][\\w:.-]*'), when: inTag,
		  cls: function (s) { return s.named ? 'tok-attr' : 'tok-tag'; },
		  then: function (s) { s.named = true; } },
		{ re: y('\\s+'), cls: '', when: inTag }
	]);

	/* ── CSS ────────────────────────────────────────────────────────────────
	   The same word is a property inside a declaration block and a selector
	   outside one, so depth alone is not enough: `@media` opens a block that
	   still holds selectors. The scanner keeps a stack of block kinds — a
	   brace opened while an at-rule is pending is a group, anything else is a
	   declaration block — plus a paren depth, because a media feature
	   (`min-width: 40rem`) is a property written in selector context. */
	var blockKind = function (s) { return s.stack && s.stack[s.stack.length - 1]; };
	var feature = function (s) { return s.at && s.paren > 0; };
	var inDecl = function (s) { return blockKind(s) === 'decl' || feature(s); };
	var inSel = function (s) { return blockKind(s) !== 'decl' && !feature(s); };

	var CSS = scanner([
		{ re: y('/\\*[\\s\\S]*?\\*/'), cls: 'tok-com' },
		{ re: y('"[^"\\n]*"|\'[^\'\\n]*\''), cls: 'tok-str' },
		{ re: y('--[\\w-]+'), cls: 'tok-var' },
		{ re: y('@[\\w-]+'), cls: 'tok-key', then: function (s) { s.at = true; } },
		{ re: y('#[\\da-fA-F]{3,8}\\b'), cls: 'tok-num' },
		{ re: y('!important\\b'), cls: 'tok-key' },
		{ re: y('[a-zA-Z-]+(?=\\s*:)'), cls: 'tok-prop', when: inDecl },
		{ re: y('[a-zA-Z-]+(?=\\()'), cls: 'tok-fn' },
		{ re: y('[.#][\\w-]+|::?[\\w-]+(?![\\w-]*\\s*:)'), cls: 'tok-sel', when: inSel },
		{ re: y('[A-Za-z][\\w-]*(?=[\\s,.:#\\[{>+~])'), cls: 'tok-tag', when: inSel },
		{ re: y('-?\\d*\\.?\\d+(?:e[+-]?\\d+)?(?:[a-z%]+)?\\b'), cls: 'tok-num' },
		{ re: y('\\{'), cls: 'tok-punc', then: function (s) {
			(s.stack = s.stack || []).push(s.at ? 'group' : 'decl');
			s.at = false;
		} },
		{ re: y('\\}'), cls: 'tok-punc', then: function (s) {
			if (s.stack) s.stack.pop();
		} },
		{ re: y('\\('), cls: 'tok-punc', then: function (s) { s.paren = (s.paren || 0) + 1; } },
		{ re: y('\\)'), cls: 'tok-punc', then: function (s) { s.paren = Math.max(0, (s.paren || 0) - 1); } },
		{ re: y(';'), cls: 'tok-punc', then: function (s) { s.at = false; } },
		{ re: y('[\\[\\],]'), cls: 'tok-punc' }
	]);

	var JS_KEY = 'const|let|var|function|return|if|else|for|while|do|switch|case|default|' +
		'break|continue|new|class|extends|super|this|typeof|instanceof|in|of|try|catch|' +
		'finally|throw|await|async|yield|import|export|from|delete|void|null|undefined|' +
		'true|false';

	var JS = scanner([
		{ re: y('//[^\\n]*|/\\*[\\s\\S]*?\\*/'), cls: 'tok-com' },
		{ re: y('`(?:\\\\[\\s\\S]|[^`\\\\])*`'), cls: 'tok-str' },
		{ re: y('"(?:\\\\.|[^"\\\\\\n])*"|\'(?:\\\\.|[^\'\\\\\\n])*\''), cls: 'tok-str' },
		{ re: y('0[xXbBoO][\\da-fA-F_]+\\b|\\d[\\d_]*(?:\\.\\d+)?(?:[eE][+-]?\\d+)?\\b'), cls: 'tok-num' },
		{ re: y('(?:' + JS_KEY + ')\\b'), cls: 'tok-key' },
		{ re: y('[A-Za-z_$][\\w$]*(?=\\s*\\()'), cls: 'tok-fn' },
		{ re: y('[A-Za-z_$][\\w$]*'), cls: '' },
		{ re: y('[{}()\\[\\];,.]'), cls: 'tok-punc' }
	]);

	var JSON_ = scanner([
		{ re: y('"(?:\\\\.|[^"\\\\])*"(?=\\s*:)'), cls: 'tok-attr' },
		{ re: y('"(?:\\\\.|[^"\\\\])*"'), cls: 'tok-str' },
		{ re: y('-?\\d+(?:\\.\\d+)?(?:[eE][+-]?\\d+)?'), cls: 'tok-num' },
		{ re: y('true|false|null'), cls: 'tok-key' },
		{ re: y('[{}\\[\\]:,]'), cls: 'tok-punc' }
	]);

	/* ── Shell ──────────────────────────────────────────────────────────────
	   The first word of a line (or after a pipe) is the command; flags read as
	   attributes; $VARS as variables. */
	var SH_KEY = 'if|then|elif|else|fi|for|in|do|done|while|case|esac|function|return|export|local|set';
	var freshLine = function (s) { return !s.cmd; };

	var SH = scanner([
		{ re: y('#[^\\n]*'), cls: 'tok-com' },
		{ re: y('"(?:\\\\.|[^"\\\\])*"|\'[^\']*\''), cls: 'tok-str' },
		{ re: y('\\$[\\w{}]+'), cls: 'tok-var' },
		{ re: y('(?:' + SH_KEY + ')\\b'), cls: 'tok-key' },
		{ re: y('--?[A-Za-z][\\w-]*'), cls: 'tok-attr' },
		{ re: y('[\\w./-]+'), when: freshLine, cls: 'tok-fn',
		  then: function (s) { s.cmd = true; } },
		{ re: y('[\\n|;&]+'), cls: 'tok-punc',
		  then: function (s) { s.cmd = false; } },
		{ re: y('\\d+\\b'), cls: 'tok-num' }
	]);

	var LANGS = {
		html: HTML, xml: HTML, svg: HTML, vue: HTML, markup: HTML,
		css: CSS, scss: CSS, less: CSS,
		js: JS, javascript: JS, jsx: JS, ts: JS, typescript: JS, mjs: JS,
		json: JSON_,
		bash: SH, sh: SH, shell: SH, zsh: SH, console: SH, terminal: SH
	};

	function normalise(lang) {
		return String(lang || '').trim().toLowerCase().replace(/^\./, '');
	}

	/* Public: code string -> token HTML. Unknown languages come back escaped
	   but unstyled, which is the honest outcome — never mis-coloured. */
	function highlight(code, lang) {
		var fn = LANGS[normalise(lang)];
		return fn ? fn(String(code)) : esc(String(code));
	}

	/* Split the finished HTML into .ln rows — what the line numbers count.
	   Safe because emit() never lets a span cross a newline. */
	function lines(code, lang) {
		return highlight(code, lang).split('\n').map(function (line) {
			return '<span class="ln">' + (line || ' ') + '</span>';
		}).join('');
	}

	function langOf(el) {
		var box = el.closest ? el.closest('.codebox') : null;
		var cap = box && box.querySelector('.codebox__lang');
		var cls = (el.className || '').match(/(?:language|lang)-([\w-]+)/);
		return normalise(el.getAttribute('data-lang') ||
			(cls && cls[1]) || (cap && cap.textContent) || '');
	}

	/* Highlight one <code> in place. Idempotent: the raw text is kept on the
	   element so a re-run (theme swap, re-render) never highlights markup that
	   is already token spans. */
	function el(node, opts) {
		if (!node) return;
		var o = opts || {};
		var raw = node.getAttribute('data-raw');
		if (raw === null) {
			raw = node.textContent.replace(/\n$/, '');
			node.setAttribute('data-raw', raw);
		}
		var lang = o.lang || langOf(node);
		var box = node.closest ? node.closest('.codebox') : null;
		// Inside a codebox, always emit rows: they are what the line numbers
		// count and what the playback staggers on.
		var wantLines = o.lines !== undefined ? o.lines
			: node.classList.contains('codebox__ln') || !!box;
		node.innerHTML = wantLines ? lines(raw, lang) : highlight(raw, lang);
		node.setAttribute('data-highlighted', lang || 'text');
		if (box && box.hasAttribute('data-play')) play(box);
	}

	/* One short settle on first view, so a code block reads as having arrived
	   rather than always having been there. One shot per box, and never for
	   readers who asked for less motion. */
	function play(box) {
		if (!box || box.hasAttribute('data-played')) return;
		box.setAttribute('data-played', '');
		var still = global.matchMedia && global.matchMedia('(prefers-reduced-motion: reduce)').matches;
		if (still || !('IntersectionObserver' in global)) {
			box.classList.add('is-played');
			return;
		}
		var io = new IntersectionObserver(function (entries) {
			entries.forEach(function (e) {
				if (!e.isIntersecting) return;
				io.disconnect();
				box.classList.add('is-playing');
				global.setTimeout(function () {
					box.classList.remove('is-playing');
					box.classList.add('is-played');
				}, 400);
			});
		}, { rootMargin: '0px 0px -10% 0px' });
		io.observe(box);
	}

	/* Let a block settle in on first view. Used for hand-written line markup as
	   much as for our own output — a block coloured by hand still arrives. */
	function prepare(box) {
		if (!box.querySelector('.codebox__pre .ln')) return false;
		if (box.getAttribute('data-play') === 'off') return false;
		box.setAttribute('data-play', '');
		play(box);
		return true;
	}

	/* Every <code> that declares a language, plus every .codebox caption that
	   names one. Runs on DOMContentLoaded; call again after injecting markup.

	   Code that already carries markup is left exactly as it is: a block whose
	   lines or tokens were written by hand is a deliberate act, and reading it
	   back as text would flatten the line structure it depends on. Such blocks
	   still get numbered and still play — they just keep their own colours. */
	function scan(root) {
		var scope = root || document;
		var plain = [];
		scope.querySelectorAll('code[data-lang], code[class*="language-"], code[class*="lang-"]')
			.forEach(function (c) { plain.push(c); });
		scope.querySelectorAll('.codebox[data-lang], .codebox .codebox__lang').forEach(function (n) {
			var box = n.classList.contains('codebox') ? n : n.closest('.codebox');
			var c = box && box.querySelector('pre code');
			if (c && plain.indexOf(c) === -1) plain.push(c);
		});
		plain.forEach(function (c) {
			if (c.hasAttribute('data-highlighted') || c.children.length) return;
			el(c);
		});
		scope.querySelectorAll('.codebox').forEach(prepare);
	}

	var api = { highlight: highlight, lines: lines, el: el, scan: scan, play: play, languages: LANGS };
	global.CreatorHighlight = api;
	if (typeof module === 'object' && module.exports) module.exports = api;

	if (typeof document !== 'undefined') {
		if (document.readyState === 'loading') {
			document.addEventListener('DOMContentLoaded', function () { scan(); });
		} else {
			scan();
		}
	}
})(typeof window !== 'undefined' ? window : this);
