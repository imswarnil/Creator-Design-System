from common import tile, sec, END, ct

PAGES = {}

# ── Introduction ────────────────────────────────────────────────────────────

intro = '''
		<div class="surface demo-tile u-mb-8" style="overflow:hidden">
			<div class="demo pattern pattern-grid pattern-lg fade-corners" style="padding:var(--space-10) var(--space-8)">
				<span class="t-slate" style="display:flex;align-items:center;gap:8px"><span class="dot dot-sm dot-live"></span> Creator Design System · v0.1 · proposal</span>
				<h2 class="t-display-1" style="margin-top:var(--space-4)">Frame &amp; Signal.</h2>
				<p class="t-lead" style="margin-top:var(--space-5);max-width:var(--measure-lead)">
					A token-first design system for creators building their site.
					Almost monochrome, so that one colour can mean something. Built as
					a viewfinder: a frame around the work, and a light that says
					<em class="t-accent">this is the live thing</em>.
				</p>
			</div>
		</div>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">The three devices</h2>
		<div class="grid-3 u-mb-8">
			<div class="surface" style="padding:var(--space-5)">
				<span class="dot dot-sm dot-live"></span>
				<h3 class="t-h4 u-mt-3">The signal dot</h3>
				<p class="t-small u-fg-subtle u-mt-2">One vermilion dot per surface. It means live, active, now — never decoration. If two things glow, neither is the live thing.</p>
			</div>
			<div class="surface" style="padding:var(--space-5)">
				<span style="display:inline-block;width:2rem;height:1.4rem;border:2px solid currentColor;border-radius:3px"></span>
				<h3 class="t-h4 u-mt-3">The frame</h3>
				<p class="t-small u-fg-subtle u-mt-2">Viewfinder chrome around the thing being shown. It always wraps content — a frame around nothing is decoration, and decoration is noise.</p>
			</div>
			<div class="surface" style="padding:var(--space-5)">
				<span class="t-slate">TAKE 47 · 00:12:47</span>
				<h3 class="t-h4 u-mt-3">The slate</h3>
				<p class="t-small u-fg-subtle u-mt-2">Mono, uppercase, letterspaced metadata. Timecodes, take numbers, labels — the production voice that never shouts.</p>
			</div>
		</div>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">How the system is layered</h2>
'''

intro += ct([
    ('Foundation', 'tokens and primitives: color, type, spacing, elevation, layout, patterns, logo, icons, shape, frames'),
    ('Motion', 'animation as its own layer: basics, text effects, annotations, micro-interactions, section presets, stings'),
    ('Elements &amp; Content', 'single ideas: text, tables, quotes, code — a badge is a word in a shape'),
    ('Forms &amp; Components', 'things with parts and states: fields, buttons, cards, overlays, disclosure'),
    ('Composites &amp; Sections', 'organs and bands: syllabus, build log, hero, stats, CTA, footer'),
    ('Broadcast', 'the same tokens exported to YouTube and social canvases'),
    ('Utilities', 'u-prefixed single-purpose classes off the token ladders'),
], head=('Layer', 'Holds'))

intro += '''
		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Reading these docs</h2>
		<p class="u-fg-subtle" style="max-width:var(--measure-lead)">
			One page per topic, in the sidebar's order. Under each demo, the grey
			strip names the classes. The current page's contents nest in the
			sidebar and highlight as you scroll. Every page ends in prev/next
			pagination; the sidebar collapses with the « button, and the theme
			toggle flips everything live. Start with
			<a class="t-link" href="/principles.html">Principles</a>, then
			<a class="t-link" href="/usage.html">Usage</a> if you're bringing
			your own stack.
		</p>
'''

PAGES['introduction'] = ('Creator Design System',
    'A token-first foundation for creator sites. Almost monochrome, so that one colour '
    'can mean something.',
    intro)

# ── Principles ──────────────────────────────────────────────────────────────

princ = ct([
    ('One dot per surface', 'the accent is rationed — it marks the single live thing, never decoration'),
    ('One accent word per headline', 'an &lt;em&gt; in the display voice; two accents and neither means anything'),
    ('One inverse band per view', 'contrast is earned by scarcity — usually the CTA'),
    ('One ask per page', 'a page persuades toward exactly one action, near the end'),
], head=('Rule of one', 'Meaning'))

princ += '''
		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Tokens before templates</h2>
		<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">
			Every value in every layer is a <code class="t-code">var()</code>. No raw
			hex, no magic pixel numbers. If a component needs a value that doesn't
			exist on a ladder, the component is wrong — a template argues about one
			page; a token settles it for every page at once.
		</p>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">State lives in ARIA</h2>
		<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">
			Active, selected, pressed, current, done — all driven by
			<code class="t-code">aria-current</code>, <code class="t-code">aria-selected</code>,
			<code class="t-code">aria-pressed</code>, <code class="t-code">[data-done]</code>.
			The styling and the accessibility tree can never disagree, because they
			are the same attribute.
		</p>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">The platform first</h2>
		<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">
			Accordion and collapse are <code class="t-code">&lt;details&gt;</code>.
			Modal and offcanvas are <code class="t-code">&lt;dialog&gt;</code>.
			Popovers use the Popover API; selects, checks and ranges are native
			elements dressed, never divs pretending. Keyboard, focus trapping and
			light-dismiss come from the browser, not a script.
		</p>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Motion is honest</h2>
		<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">
			Nothing over 200ms for interaction feedback; one property per
			micro-interaction; everything degrades to a fade (or nothing) under
			<code class="t-code">prefers-reduced-motion</code>. The marquee pauses
			on hover and its duplicate run is hidden from assistive tech.
		</p>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Design at thumbnail scale</h2>
		<p class="u-fg-subtle" style="max-width:var(--measure-lead)">
			Every card, thumbnail and canvas is designed to survive a 120px crop
			first (the P1 test). If the title doesn't read small, the layout is
			wrong at every size.
		</p>
'''

PAGES['principles'] = ('Principles',
    'The rules the whole system obeys. When a decision is hard, one of these settles it.',
    princ)

# ── Usage — CSS · SCSS · Tailwind ───────────────────────────────────────────

