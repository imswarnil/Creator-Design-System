"""Overrides + new pages for the reorganised docs (imported last, wins)."""
from common import tile, sec, END, ct

PAGES = {}

# ── Introduction — for creators, with the animated viewfinder ───────────────

_hero_svg = '''
		<style>
			@keyframes cds-scan { 0%,100% { transform: translateY(0); } 50% { transform: translateY(150px); } }
			@keyframes cds-blink { 0%,70%,100% { opacity: 1; } 82% { opacity: 0.25; } }
			@keyframes cds-type { 0% { width: 0; } 60%,100% { width: 190px; } }
			@keyframes cds-orbit { to { transform: rotate(360deg); } }
			.cds-illo .scan { animation: cds-scan 5s var(--ease-inout) infinite; }
			.cds-illo .dot { animation: cds-blink 2.4s linear infinite; }
			.cds-illo .type { animation: cds-type 5s var(--ease-inout) infinite; }
			.cds-illo .orbit { transform-origin: 300px 110px; animation: cds-orbit 24s linear infinite; }
			@media (prefers-reduced-motion: reduce) { .cds-illo * { animation: none !important; } }
		</style>
		<div class="surface demo-tile u-mb-8">
			<div class="demo u-p-0" style="padding:0">
				<svg class="cds-illo" viewBox="0 0 600 220" style="display:block;width:100%;height:auto" role="img" aria-label="Animated viewfinder illustration: a frame around the work, a record light, a title being typed">
					<rect width="600" height="220" fill="var(--bg-sunken)"/>
					<g stroke="var(--line-default)" stroke-width="1">
						<path d="M0 55h600M0 110h600M0 165h600M150 0v220M300 0v220M450 0v220"/>
					</g>
					<g class="orbit" fill="none" stroke="var(--line-strong)" stroke-width="1.5" stroke-dasharray="4 6">
						<circle cx="300" cy="110" r="86"/>
					</g>
					<g fill="none" stroke="var(--fg-default)" stroke-width="4" stroke-linecap="round">
						<path d="M190 55v-8a10 10 0 0 1 10-10h14M410 55v-8a10 10 0 0 0-10-10h-14M190 165v8a10 10 0 0 0 10 10h14M410 165v8a10 10 0 0 1-10-10h0" opacity="0"/>
						<path d="M186 58v-11a10 10 0 0 1 10-10h16M414 58v-11a10 10 0 0 0-10-10h-16M186 162v11a10 10 0 0 0 10 10h16M414 162v11a10 10 0 0 1-10 10h-16"/>
					</g>
					<g class="scan"><path d="M196 62h208" stroke="var(--accent)" stroke-width="1.5" opacity="0.55"/></g>
					<circle class="dot" cx="404" cy="48" r="7" fill="var(--accent)"/>
					<rect x="196" y="128" width="190" height="14" rx="3" fill="var(--line-default)"/>
					<rect class="type" x="196" y="128" height="14" rx="3" fill="var(--fg-default)"/>
					<text x="196" y="120" font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="2" fill="var(--fg-faint)">TAKE 47 · 00:12:47</text>
					<text x="470" y="205" font-family="IBM Plex Mono, monospace" font-size="10" letter-spacing="2" fill="var(--fg-faint)">REC ●</text>
				</svg>
			</div>
		</div>
'''

intro = _hero_svg + '''
		<h2 class="t-h3" style="margin:0 0 var(--space-4)">Made by a creator, for creators.</h2>
		<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">
			I publish videos, courses, build logs and trips — and I got tired of
			every page arguing about colours. This system settles the arguments
			once: a token-first foundation that is almost monochrome, so that one
			colour can mean something. It is built like a viewfinder — a frame
			around the work, and a light that says <em class="t-accent">this is
			the live thing</em>. If you make things and publish them, it was
			built for you too.
		</p>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">The three devices</h2>
		<div class="grid-3 u-mb-8">
			<div class="surface" style="padding:var(--space-5)">
				<span class="dot dot-sm dot-live"></span>
				<h3 class="t-h4 u-mt-3">The signal dot</h3>
				<p class="t-small u-fg-subtle u-mt-2">One vermilion dot per surface. It means live, active, now — never decoration.</p>
			</div>
			<div class="surface" style="padding:var(--space-5)">
				<span style="display:inline-block;width:2rem;height:1.4rem;border:2px solid currentColor;border-radius:3px"></span>
				<h3 class="t-h4 u-mt-3">The frame</h3>
				<p class="t-small u-fg-subtle u-mt-2">Viewfinder chrome around the thing being shown. It always wraps content.</p>
			</div>
			<div class="surface" style="padding:var(--space-5)">
				<span class="t-slate">TAKE 47 · 00:12:47</span>
				<h3 class="t-h4 u-mt-3">The slate</h3>
				<p class="t-small u-fg-subtle u-mt-2">Mono, uppercase, letterspaced metadata — the production voice that never shouts.</p>
			</div>
		</div>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Where to start</h2>
'''
intro += ct([
    ('<a class="t-link" href="./why.html">Why this system</a>', 'the ideology — what problem it solves for a creator'),
    ('<a class="t-link" href="./principles.html">Principles</a>', 'the rules every layer obeys'),
    ('<a class="t-link" href="./f-logo.html">Foundation</a>', 'logo, color, type, space, elevation — the tokens'),
    ('<a class="t-link" href="./usage.html">Usage</a>', 'bring your own stack: CSS, SCSS or Tailwind'),
], head=('Page', 'What you get'))

PAGES['introduction'] = ('Creator Design System',
    'A token-first design system for creators building their site — one page per topic, '
    'every variant shown, everything themed from the same variables.',
    intro)

# ── Why this system ─────────────────────────────────────────────────────────

PAGES['why'] = ('Why this system',
    'A creator site is not a blog with extras — it is a channel, a school, a portfolio and a '
    'travel journal wearing one identity. That only works if the identity is decided once.',
    '''
		<h2 class="t-h3" style="margin:0 0 var(--space-4)">The problem</h2>
		<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">
			Creators publish in more shapes than anyone: posts, videos, courses,
			series, products, trips. Each shape pulls the design somewhere else —
			the video page wants Netflix, the course page wants Udemy, the blog
			wants Medium. Copy all three and the site becomes a mall. The fix is
			not more design; it is fewer decisions, made higher up.
		</p>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">The ideology</h2>
'''
    + ct([
        ('Restraint is the brand', 'almost monochrome ink means the one accent is unmissable — attention is budgeted, not sprayed'),
        ('Decide with tokens', 'a template argues about one page; a token settles it for every page, thumbnail and end screen at once'),
        ('The site and the channel are one system', 'the same tokens export to YouTube thumbnails, banners and IG posts — layer 4 is not a separate brand'),
        ('The platform is the framework', 'details, dialog, popover, native inputs — the browser ships the behaviour; CSS ships the taste'),
        ('Honest by default', 'real states in ARIA, honest loading, honest motion, honest empty states — the UI never lies to a reader'),
    ], head=('Belief', 'What it means'))
    + '''
		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">What you get out of it</h2>
		<p class="u-fg-subtle" style="max-width:var(--measure-lead)">
			Change <code class="t-code">--accent</code> and your whole channel
			rebrands — site, player, course, thumbnails. Add a new collection and
			its card, header and hero already exist. Ship faster because the
			system already had the argument, and won it with a variable.
		</p>
'''
)

# ── Principles — detailed, with icons ───────────────────────────────────────

def _p(icon, title, body):
    """A principle: the words lead, the mark answers on the right and draws
    itself in as the row arrives."""
    return (f'<div class="surface u-mb-4 pr-row">'
            f'<div><h3 class="t-h4">{title}</h3>'
            f'<p class="t-small u-fg-subtle u-mt-2" style="max-width:60ch">{body}</p></div>'
            f'<span class="pr-row__art" aria-hidden="true">'
            f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" pathLength="100">{icon}</svg></span>'
            f'</div>')

_i = {
 'dot': '<circle cx="12" cy="12" r="3" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="8" stroke-dasharray="3 4"/>',
 'token': '<path d="M12 3 20 7.5v9L12 21 4 16.5v-9L12 3Z"/><path d="M12 12v9M12 12 4 7.5M12 12l8-4.5"/>',
 'aria': '<circle cx="12" cy="6" r="2.5"/><path d="M12 8.5V15M7 11h10M9 20l3-5 3 5"/>',
 'platform': '<rect x="3.5" y="4.5" width="17" height="13" rx="2"/><path d="M3.5 8.5h17M12 17.5V20M8 20h8"/>',
 'motion': '<path d="M4 12h4l2-5 3 10 2-5h5"/>',
 'thumb': '<rect x="3.5" y="5.5" width="17" height="13" rx="2"/><path d="m3.5 15 4.5-4 4 3.5 3-2.5 5.5 4.5"/><circle cx="9" cy="9.5" r="1.3"/>',
 'measure': '<path d="M4 7h16M4 12h10M4 17h13"/>',
 'a11y': '<path d="m5 12.5 4.5 4.5L19 7"/>',
}

princ = (
    '<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
    'Principles are the arguments we already had, written down so they never get '
    're-argued at midnight. Each one is enforced by the system itself — a token, '
    'an attribute, a class — not by memory.</p>'
    + _p(_i['dot'], 'The rules of one',
         'One signal dot per surface — it marks the single live thing, never decoration. '
         'One accent word per headline (an <em>&lt;em&gt;</em> in the display voice). '
         'One inverse band per view, so contrast is earned by scarcity. One ask per page, '
         'near the end. When two things glow, neither is the live thing.')
    + _p(_i['token'], 'Tokens before templates',
         'Every value in every layer is a <code class="t-code">var()</code> off a ladder — '
         'colour, size, space, radius, shadow, duration. No raw hex, no magic numbers. '
         'If a component needs a value that isn\'t on a ladder, the component is wrong. '
         'This is also the entire customization API: override the token, own the system.')
    + _p(_i['aria'], 'State lives in ARIA',
         'Active, selected, pressed, current, done — all driven by '
         '<code class="t-code">aria-current</code>, <code class="t-code">aria-selected</code>, '
         '<code class="t-code">aria-pressed</code> and <code class="t-code">[data-done]</code>. '
         'Styling and the accessibility tree are the same attribute, so they can never disagree. '
         'A state class like <code class="t-code">.active</code> is a lie waiting to happen.')
    + _p(_i['platform'], 'The platform first',
         'Accordion and collapse are <code class="t-code">&lt;details&gt;</code>; modal and '
         'offcanvas are <code class="t-code">&lt;dialog&gt;</code>; popovers use the Popover API; '
         'selects, checks and ranges are native elements dressed, never divs pretending. Focus '
         'trapping, ESC, light-dismiss and find-in-page come from the browser — free, and correct.')
    + _p(_i['motion'], 'Motion is honest',
         'Interaction feedback stays under 200ms and animates one property. Entrances are drawn, '
         'not faded, when they should read as gestures (annotations). Everything degrades to a '
         'fade or to nothing under <code class="t-code">prefers-reduced-motion</code>. A marquee '
         'pauses on hover and hides its duplicate run from assistive tech.')
    + _p(_i['thumb'], 'Design at thumbnail scale',
         'Every card, poster and canvas passes the P1 test: does the title survive a 120px crop? '
         'A creator\'s work is judged in a grid of thumbnails before it is ever judged full-screen — '
         'so the small size is the real size, and the big one is the luxury.')
    + _p(_i['measure'], 'Reading is the interface',
         'Prose never exceeds its measure (65ch), leads get one size up, numbers are tabular, '
         'labels are slate. Type roles — not utility font sizes — so every page speaks with the '
         'same voice at the same volume.')
    + _p(_i['a11y'], 'Accessible is the default, not the audit',
         'Focus rings that show, skip links that work, contrast measured in both themes, targets '
         '44px, colour never the only signal, forms wired with aria-invalid/aria-describedby. '
         'Accessibility is a foundation file (08-a11y), not a launch checklist.')
)

PAGES['principles'] = ('Principles',
    'The rules every layer obeys — each enforced by a token, an attribute or a class, '
    'so the system keeps its own promises.',
    princ)

# ── Color — primary / secondary / variants, no status noise ─────────────────

def _ramp(name, steps, label):
    sw = ''.join(
        f'<div class="sw"><div class="sw__chip" style="background:var(--{name}-{s})"></div>'
        f'<div class="sw__meta"><span class="sw__name">--{name}-{s}</span></div></div>' for s in steps)
    return f'<span class="demo-label">{label}</span><div class="ramp u-mb-6">{sw}</div>'

color = (
    '<h2 class="t-h3" style="margin:0 0 var(--space-4)">Primary — signal</h2>'
    '<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">The record light. '
    'It marks live, active, now — buttons, the dot, the accent word. Rationed everywhere else.</p>'
    + _ramp('signal', [50, 100, 200, 300, 400, 500, 600, 700, 800, 900], 'signal ramp')
    + '<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Secondary — amber</h2>'
    '<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">The craft colour: '
    'construction lines, one highlighted word, tape. Max one appearance per view.</p>'
    + _ramp('amber', [50, 100, 200, 300, 400, 500, 600, 700, 800], 'amber ramp')
    + '<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Neutral — ink</h2>'
    '<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">Fourteen cool, '
    'violet-leaning greys carry everything else — text, lines, surfaces, both themes.</p>'
    + _ramp('ink', [25, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950], 'ink ramp')
    + '<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Semantic variants — what markup actually uses</h2>'
    '<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">Markup never names a '
    'ramp step. It asks for a <em>meaning</em>; the theme resolves it per mode. These are the '
    'variables you override to rebrand.</p>'
    + ct([
        ('--accent / -hover / -press / -soft / -ring', 'the primary in all its interactive states'),
        ('--fg-default / -subtle / -muted / -faint', 'the text ladder, loud → whisper'),
        ('--bg-canvas / -surface / -sunken / -raised / -inverse', 'the surface ladder'),
        ('--line-subtle / -default / -strong / -accent', 'hairlines and borders'),
        ('--fg-on-accent / --fg-on-inverse', 'text guaranteed readable on loud surfaces'),
    ], head=('Token family', 'Meaning'))
    + tile('<div class="u-flex u-gap-3 u-wrap">'
           '<button class="btn btn-primary">Primary</button>'
           '<span class="badge badge-craft">Craft</span>'
           '<span class="u-bg-inverse u-rounded u-p-3 t-slate-sm">inverse</span>'
           '<span class="dot dot-sm dot-live"></span></div>',
           'the whole palette in use — primary, secondary, ink, and the dot')
)

PAGES['f-color'] = ('Color',
    'Three families — primary signal, secondary amber, neutral ink — resolved into semantic '
    'variants that markup actually uses.',
    color)

# ── Icon set ────────────────────────────────────────────────────────────────

_GROUPS = {
    'ui': ['search', 'menu', 'close', 'arrow-right', 'external', 'check', 'copy', 'sun', 'moon'],
    'creator': ['rec', 'viewfinder', 'slate', 'take', 'sting', 'course', 'buildlog', 'trip'],
    'media': ['play', 'pause', 'camera', 'mic', 'volume', 'live'],
    'social': ['heart', 'chat', 'share', 'mail'],
}

iconset = ('<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
           'Shipped as real files in <code class="t-code">design-system/icons/&lt;group&gt;/&lt;name&gt;.svg</code> '
           '— 24×24 grid, 1.5px stroke, <code class="t-code">currentColor</code> only, so every icon follows '
           'the text colour and dark/light theming is automatic. The <b>creator</b> group is ours alone: '
           'rec, viewfinder, slate, take, sting — the production-desk icons a template like this needs.</p>')
for g, names in _GROUPS.items():
    tiles = ''.join(
        f'<div class="u-border u-rounded-lg u-p-4 u-text-center" style="display:grid;gap:var(--space-2);place-items:center">'
        f'<img src="./icons/{g}/{n}.svg" alt="" style="width:1.5rem;height:1.5rem" class="cds-ico" />'
        f'<span class="t-slate-sm" style="color:var(--fg-faint)">{n}</span></div>' for n in names)
    iconset += (f'<h2 class="t-h3" style="margin:var(--space-8) 0 var(--space-3)">{g}/</h2>'
                f'<div class="grid-auto-sm" style="display:grid;gap:var(--space-3);'
                f'grid-template-columns:repeat(auto-fill,minmax(6.5rem,1fr))">{tiles}</div>')
iconset += ('\n\t\t<style>[data-theme="dark"] .cds-ico { filter: invert(1); }</style>'
            + tile('''<figure class="codebox codebox-light u-m-0"><figcaption class="codebox__head"><span class="codebox__lang">html</span><button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>
<pre class="codebox__pre"><code><span class="ln"><span class="tok-com">&lt;!-- inline: inherits color, themes automatically --&gt;</span></span><span class="ln">&lt;<span class="tok-key">svg</span> class=<span class="tok-str">"icon"</span>&gt;…paste the file's paths…&lt;/<span class="tok-key">svg</span>&gt;</span><span class="ln"><span class="tok-com">&lt;!-- sizes ride the icon ladder --&gt;</span></span><span class="ln">.icon-sm <span class="tok-com">(16)</span> · .icon <span class="tok-com">(20)</span> · .icon-lg <span class="tok-com">(24)</span></span></code></pre></figure>''',
                   'prefer inline or a sprite — an &lt;img&gt; can\'t inherit currentColor (the grid above inverts via filter)'))

PAGES['icon-set'] = ('Icon set',
    'The system\'s own icons — grouped, stroke-consistent, currentColor, and including a '
    'creator group no stock set has.',
    iconset)

# ── Shape & Cutout ──────────────────────────────────────────────────────────

cut = ('<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
       'Where Shapes are geometry, cutouts are <em>material</em>: things that look cut, stuck, '
       'stamped or punched. This is the system\'s neo-brutal register — hard borders, hard offset '
       'shadows, honest paper. Use them for callouts, price tags, guestbook notes and anything '
       'that should feel handmade; never for body UI.</p>'
       + tile('<div class="u-flex u-gap-6 u-wrap u-items-center">'
              '<span class="cut cut-sticker">Sticker</span>'
              '<span class="cut cut-sticker cut-sticker-accent">Accent shadow</span>'
              '<button class="cut cut-sticker" type="button">Press me</button>'
              '</div>',
              '<b>.cut.cut-sticker (+ -accent)</b> — the neo-brutal core; buttons press into their shadow')
       + tile('<div class="u-flex u-gap-6 u-wrap u-items-center">'
              '<span class="cut cut-ticket">ADMIT ONE</span>'
              '<span class="cut cut-corner">Folded corner</span>'
              '<span class="cut cut-tab" data-tab="Note">A tabbed card</span>'
              '</div>',
              '<b>.cut-ticket · .cut-corner · .cut-tab[data-tab]</b>')
       + tile('<div class="u-flex u-gap-6 u-wrap u-items-center">'
              '<span class="cut cut-tape">Taped to the page</span>'
              '<span class="cut cut-punch">Ring-bound</span>'
              '<span class="cut cut-speech">A brutal speech bubble</span>'
              '</div>',
              '<b>.cut-tape · .cut-punch · .cut-speech</b>')
       + tile('<div class="u-flex u-gap-6 u-wrap u-items-center">'
              '<span class="cut cut-sm cut-sticker">cut-sm</span>'
              '<span class="cut cut-sticker">default</span>'
              '<span class="cut cut-lg cut-sticker">cut-lg</span>'
              '</div>',
              '<b>sizes</b> — .cut-sm / default / .cut-lg scale offset, border and padding together')
       + ct([('--cut-off', 'the hard-shadow offset (3/5/8px by size)'),
             ('--cut-bw', 'the border weight'),
             ('.cut-inverse / [data-surface=inverse]', 'paper shapes on a dark desk — shadow flips to accent')],
            head=('Hook', 'Does')))

PAGES['cutouts'] = ('Cutouts',
    'The neo-brutal register: sticker, ticket, stamp, tab, tape, punch, speech — named, sized, '
    'and rationed to the moments that should feel handmade.',
    cut)

# ── Page transitions ────────────────────────────────────────────────────────

pt = ('<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
      'Between-page motion is collection-flavoured: each destination announces itself the way its '
      'medium would. Transitions are 300–500ms, skippable, and disabled entirely under reduced '
      'motion — a transition is a scene change, not a loading screen.</p>'
      + ct([
          ('Videos / YouTube', 'a beat of TV static'),
          ('Web series', 'the ident sting (see Logo sting) — ends on the wordmark'),
          ('Projects', 'terminal run: prompt, command, enter'),
          ('Travel', 'take-off / landing sweep; single trips get the paper plane'),
          ('Courses', 'study pop — pen to table'),
          ('Timeline', 'years passing, motion-blurred'),
          ('Newsletter', 'envelope opens'),
          ('Resume', 'paper unfolds'),
      ], head=('Destination', 'Flavour'))
      + tile('<div class="u-flex u-gap-4 u-wrap u-items-center">'
             '<div class="frame frame-ink" data-surface="inverse" style="width:12rem;aspect-ratio:16/9;display:grid;place-items:center;overflow:hidden">'
             '<div class="pattern pattern-scanline" style="position:absolute;inset:0;opacity:.5"></div>'
             '<span class="t-slate" style="color:#fff">STATIC</span></div>'
             '<div class="frame" style="width:12rem;aspect-ratio:16/9;display:grid;place-items:center">'
             '<span class="t-slate">✈ TAKE-OFF</span></div>'
             '</div>',
             'flavour boards — the real overlays live in the theme; the system ships the vocabulary')
      + '<p class="u-fg-subtle u-mt-6" style="max-width:var(--measure-lead)">'
        'Implementation note: use the View Transitions API where available '
        '(<code class="t-code">@view-transition { navigation: auto }</code>) with the flavour as a '
        '<code class="t-code">::view-transition-old/new</code> animation; fall back to no transition, '
        'never to a blocking overlay.</p>')

PAGES['page-transitions'] = ('Page transitions',
    'Scene changes between collections — each destination announces itself in its own medium, '
    'briefly, skippably, honestly.',
    pt)

# ── Introduction v2 — richer: what / why / for whom / magic values ──────────

_ic = lambda p: (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
                 f'stroke-linecap="round" stroke-linejoin="round" '
                 f'style="width:1.5rem;height:1.5rem;flex:none;color:var(--accent)">{p}</svg>')

_IC = {
 'rec': '<rect x="3.5" y="3.5" width="17" height="17" rx="3"/><circle cx="16.5" cy="7.5" r="1.8" fill="currentColor" stroke="none"/>',
 'scissors': '<circle cx="6.5" cy="6.5" r="2.5"/><circle cx="6.5" cy="17.5" r="2.5"/><path d="M8.5 8 20 19M8.5 16 20 5"/>',
 'broll': '<rect x="3.5" y="7.5" width="12" height="9" rx="2"/><path d="m15.5 10.5 5-2.5v8l-5-2.5"/>',
 'take': '<path d="M4 18.5 15 7.5a2.4 2.4 0 0 1 3.4 3.4L7.5 22H4v-3.5Z"/><path d="M13 9.5 17.5 14"/>',
 'site': '<rect x="3.5" y="4.5" width="17" height="15" rx="2"/><path d="M3.5 9h17M8 9v10.5"/>',
 'brand': '<circle cx="12" cy="12" r="3" fill="currentColor" stroke="none"/><path d="M12 2.5v4M12 17.5v4M2.5 12h4M17.5 12h4"/>',
 'ship': '<path d="M12 3v12M8 7l4-4 4 4"/><path d="M4 15v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/>',
}

def _card(icon, title, body):
    return (f'<div class="surface" style="padding:var(--space-5);display:flex;gap:var(--space-4);align-items:flex-start">'
            f'{_ic(icon)}<div><h3 class="t-h4">{title}</h3>'
            f'<p class="t-small u-fg-subtle u-mt-2">{body}</p></div></div>')

intro2 = _hero_svg + '''
		<h2 class="t-h3" style="margin:0 0 var(--space-4)">What this is</h2>
		<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">
			A complete, practical design system for a creator's website: tokens,
			elements, components, sections, whole page layouts — and the same
			language exported to YouTube thumbnails, banners and social art.
			Plain CSS, no framework required, themed end-to-end by variables.
		</p>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Why I built it</h2>
		<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">
			I'm a creator too — I publish videos, courses, build logs and trips,
			and every new page restarted the same arguments: which grey, which
			radius, where the curriculum goes, what a thumbnail looks like.
			So I settled the arguments once, wrote them down as tokens and rules,
			and this documentation is the receipt. Nothing here is theoretical:
			every component exists because a real page on a real creator site
			needed it.
		</p>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Who it's for — and what you can do</h2>
		<div class="grid-2 u-mb-6" style="gap:var(--space-4)">''' + \
    _card(_IC['site'], 'Build your whole site', 'Home, blog, videos, courses with syllabus, series with episode players, projects with build logs, travel with itineraries — every layout is a documented floor plan.') + \
    _card(_IC['brand'], 'Rebrand in three variables', 'Change --accent, --font-display and --radius-card and the entire site, player and thumbnail set follow. The token contract is the whole API.') + \
    _card(_IC['broll'], 'Design your channel with it', 'The Broadcast layers export thumbnails, series art, end screens, banners and IG posts from the same tokens — site and channel stay one brand.') + \
    _card(_IC['ship'], 'Ship with any stack', 'Vanilla CSS, SCSS or Tailwind — same variables, same classes. See Getting started for the five-minute install.') + '''
		</div>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">The four magic values</h2>
		<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">
			Like any good studio, the system has house values — short enough to
			say mid-edit, real enough to decide with.</p>
		<div class="grid-2 u-mb-8" style="gap:var(--space-4)">''' + \
    _card(_IC['rec'], '1 · Press record', 'Done beats perfect. Ship the page with defaults, iterate in public — the system’s defaults are good enough to publish with on day one.') + \
    _card(_IC['scissors'], '2 · Cut the noise', 'Every element must earn its frame. One accent, one ask, one inverse band — restraint is the brand, deletion is a feature.') + \
    _card(_IC['broll'], '3 · Show the b-roll', 'Build in public, document honestly: real states, honest loading, honest empty pages. The process is content; the UI never lies.') + \
    _card(_IC['take'], '4 · One more take', 'Craft is iteration. Tokens make retakes cheap — refine the variable, and every page that used it gets the better take.') + '''
		</div>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">The three devices</h2>
		<div class="grid-3 u-mb-8">
			<div class="surface" style="padding:var(--space-5)">
				<span class="dot dot-sm dot-live"></span>
				<h3 class="t-h4 u-mt-3">The signal dot</h3>
				<p class="t-small u-fg-subtle u-mt-2">One vermilion dot per surface. It means live, active, now — never decoration.</p>
			</div>
			<div class="surface" style="padding:var(--space-5)">
				<span style="display:inline-block;width:2rem;height:1.4rem;border:2px solid currentColor;border-radius:3px"></span>
				<h3 class="t-h4 u-mt-3">The frame</h3>
				<p class="t-small u-fg-subtle u-mt-2">Viewfinder chrome around the thing being shown. It always wraps content.</p>
			</div>
			<div class="surface" style="padding:var(--space-5)">
				<span class="t-slate">TAKE 47 · 00:12:47</span>
				<h3 class="t-h4 u-mt-3">The slate</h3>
				<p class="t-small u-fg-subtle u-mt-2">Mono, uppercase, letterspaced metadata — the production voice that never shouts.</p>
			</div>
		</div>

		<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Why · How · For whom</h2>
''' + ct([
    ('Why', 'so one person can run a channel-sized brand without re-deciding it nightly — <a class="t-link" href="./why.html">the full ideology</a>'),
    ('How', 'tokens → elements → components → sections → layouts, all plain CSS — <a class="t-link" href="./install.html">install in five minutes</a>'),
    ('For whom', 'creator-builders: people who film, write, teach or build in public and want their site to look decided'),
    ('Rules', 'the eight <a class="t-link" href="./principles.html">principles</a> every layer obeys'),
], head=('Question', 'Answer'))

PAGES['introduction'] = ('Creator Design System',
    'A token-first design system made by a creator, for creators — practical, opinionated, '
    'and themed end-to-end from the same variables.',
    intro2)

# ── Getting started: Installation + Setup ───────────────────────────────────

PAGES['install'] = ('Installation',
    'Five minutes from zero: get the files, link the layers, see the system render.',
    '''
		<h2 class="t-h3" style="margin:0 0 var(--space-4)">1 · Get the files</h2>
		<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">
			Today: copy the <code class="t-code">design-system/</code> folder into your
			project. Soon: <code class="t-code">npm i creator-design-system</code> and a
			jsDelivr CDN link (see <code class="t-code">instruction.md</code> in the repo).
		</p>
		<h2 class="t-h3" style="margin:var(--space-8) 0 var(--space-4)">2 · Link the layers</h2>
''' + tile('''<figure class="codebox codebox-light u-m-0"><figcaption class="codebox__head"><span class="codebox__lang">html</span><button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>
<pre class="codebox__pre"><code><span class="ln">&lt;<span class="tok-key">link</span> rel="stylesheet" href=<span class="tok-str">"design-system/1-foundation/index.css"</span>&gt;</span><span class="ln">&lt;<span class="tok-key">link</span> rel="stylesheet" href=<span class="tok-str">"design-system/2-elements/index.css"</span>&gt;</span><span class="ln">&lt;<span class="tok-key">link</span> rel="stylesheet" href=<span class="tok-str">"design-system/3-components/index.css"</span>&gt;</span><span class="ln">&lt;<span class="tok-key">link</span> rel="stylesheet" href=<span class="tok-str">"design-system/5-sections/index.css"</span>&gt;</span><span class="ln">&lt;<span class="tok-key">link</span> rel="stylesheet" href=<span class="tok-str">"design-system/6-utilities/index.css"</span>&gt;</span></code></pre></figure>''',
       'later layers require earlier ones — take foundation alone, or the whole stack') + '''
		<h2 class="t-h3" style="margin:var(--space-8) 0 var(--space-4)">3 · The fonts</h2>
''' + tile('<span class="copy-line"><code>fonts.googleapis.com/css2?family=Space+Grotesk:wght@400..700&family=Inter:wght@400..700&family=IBM+Plex+Mono:wght@400..600</code><button type="button" data-copy>Copy</button></span>',
           'Space Grotesk displays · Inter reads · IBM Plex Mono slates — or override --font-* with your own') + '''
		<h2 class="t-h3" style="margin:var(--space-8) 0 var(--space-4)">4 · First render</h2>
''' + tile('<div class="hero hero-statement" style="padding-block:var(--space-6)">'
           '<span class="hero__eyebrow"><span class="dot dot-sm dot-live"></span> It works</span>'
           '<h1 class="hero__title" style="font-size:var(--text-4xl)">Hello, <em>creator</em>.</h1>'
           '<div class="hero__actions"><button class="btn btn-primary">Press record</button>'
           '<button class="btn btn-secondary">Read the docs</button></div></div>',
           'paste any demo from these docs — markup + linked CSS is the whole runtime, no JS build'))

PAGES['setup'] = ('Setup & theming',
    'Make it yours: override tokens, pick your dark-mode strategy, swap the mark.',
    '''
		<h2 class="t-h3" style="margin:0 0 var(--space-4)">Your brand in one block</h2>
''' + tile('''<figure class="codebox codebox-light u-m-0"><figcaption class="codebox__head"><span class="codebox__lang">css</span><button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>
<pre class="codebox__pre"><code><span class="ln"><span class="tok-com">/* after the imports — this is the entire API */</span></span><span class="ln"><span class="tok-fn">:root</span> {</span><span class="ln">  <span class="tok-key">--accent</span>: <span class="tok-str">#6d4aff</span>;</span><span class="ln">  <span class="tok-key">--font-display</span>: <span class="tok-str">'Clash Display', sans-serif</span>;</span><span class="ln">  <span class="tok-key">--radius-card</span>: <span class="tok-num">1.25rem</span>;</span><span class="ln">}</span></code></pre></figure>''',
       'never edit source — override tokens; every component reads them live in both themes') + '''
		<h2 class="t-h3" style="margin:var(--space-8) 0 var(--space-4)">Dark mode</h2>
		<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">
			Themes ride <code class="t-code">data-theme="light|dark"</code> on
			<code class="t-code">&lt;html&gt;</code>. Set it from the OS with a
			two-line script, persist the choice in localStorage — exactly what the
			toggle in this sidebar does.
		</p>
		<h2 class="t-h3" style="margin:var(--space-8) 0 var(--space-4)">Swap the mark</h2>
		<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">
			The logo is markup, not an image (<a class="t-link" href="./f-logo.html">Logo</a>):
			put your own word in, keep the tittle. Icons live in
			<code class="t-code">design-system/icons/</code> — currentColor, so they
			follow your ink automatically.
		</p>
		<h2 class="t-h3" style="margin:var(--space-8) 0 var(--space-4)">Checklist</h2>
''' + ct([
    ('Tokens overridden', '--accent, faces, radii — after the imports'),
    ('data-theme wired', 'OS default + persisted toggle'),
    ('Fonts self-hosted or linked', 'or --font-* pointed at yours'),
    ('Favicon', 'assets/favicon.svg pattern: mark + prefers-color-scheme ink'),
    ('State via ARIA', 'aria-current / aria-pressed / [data-done] — never .active'),
], head=('Item', 'Detail')))

# ── Color v2 + full type scale ──────────────────────────────────────────────

def _named(name, var, note):
    return (f'<div class="sw"><div class="sw__chip" style="background:var({var})"></div>'
            f'<div class="sw__meta"><span class="sw__name">{name}</span>'
            f'<span class="sw__val">{var} · {note}</span></div></div>')

color2 = (
    '<h2 class="t-h3" style="margin:0 0 var(--space-4)">Monochrome scale</h2>'
    '<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">'
    'Ink · Paper · Mist · Line · Silver — the whole palette is grey. Five named '
    'roles carry every surface, border and letter; colour is reserved for meaning.</p>'
    '<div class="ramp u-mb-8">'
    + _named('Ink', '--fg-default', 'text, the near-black')
    + _named('Paper', '--bg-canvas', 'the page')
    + _named('Mist', '--bg-sunken', 'recessed panels')
    + _named('Line', '--line-default', 'hairlines')
    + _named('Silver', '--fg-faint', 'quiet metadata')
    + '</div>'
    + _ramp('ink', [25, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950], 'the full ink ramp behind the five roles')
    + '<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Accent &amp; REC red</h2>'
    '<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">'
    'Accent is monochrome ink; the one hue is the record-red. It marks live, '
    'active, now — the dot, the primary button, the accent word — and nothing else.</p>'
    + _ramp('signal', [50, 100, 200, 300, 400, 500, 600, 700, 800, 900], 'record-red ramp')
    + tile('<div class="u-flex u-gap-4 u-wrap u-items-center">'
           '<button class="btn btn-primary">Primary</button>'
           '<span class="dot dot-sm dot-live"></span>'
           '<span class="t-accent u-weight-semibold">the accent word</span></div>',
           'the three legal appearances of the hue')
    + '<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Dark mode</h2>'
    '<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">'
    'Ink &amp; paper flip; the record-red is the ONE hue that stays. Flip the '
    'toggle in the sidebar — every swatch above re-resolves live.</p>'
    + tile('<div class="grid-2">'
           '<div class="u-border u-rounded-lg u-p-5 u-bg-canvas"><span class="t-slate-sm" style="color:var(--fg-faint)">THIS THEME</span>'
           '<p class="u-mt-2">Ink on paper <span class="dot dot-sm dot-live"></span></p></div>'
           '<div class="u-rounded-lg u-p-5 u-bg-inverse"><span class="t-slate-sm" style="opacity:.6">FLIPPED</span>'
           '<p class="u-mt-2">Paper on ink <span class="dot dot-sm dot-live"></span></p></div>'
           '</div>',
           'both sides, one red — the dot never changes')
    + '<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Semantic variants</h2>'
    + ct([
        ('--accent / -hover / -press / -soft / -ring', 'the record-red in all its interactive states'),
        ('--fg-default / -subtle / -muted / -faint', 'the text ladder, ink → silver'),
        ('--bg-canvas / -surface / -sunken / -raised / -inverse', 'paper → mist → ink'),
        ('--line-subtle / -default / -strong / -accent', 'hairlines and borders'),
    ], head=('Token family', 'Meaning')))

PAGES['f-color'] = ('Color',
    'Ink, paper and three greys — plus one hue: the record-red. Everything else is restraint.',
    color2)

def _spec(label, cls, text, style=''):
    return (f'<div style="display:grid;grid-template-columns:9rem 1fr;gap:var(--space-4);'
            f'align-items:baseline;padding:var(--space-3) 0;border-bottom:var(--border-hair) solid var(--line-subtle)">'
            f'<span class="t-slate-sm" style="color:var(--fg-faint)">{label}</span>'
            f'<span class="{cls}" style="{style}">{text}</span></div>')

TYPE_INTRO = (
    '\t\t<h2 class="t-h3" style="margin:0 0 var(--space-4)">Display &amp; headings</h2>'
    '<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">'
    'Space Grotesk, tight tracking, near-black ink. Inter carries the reading; '
    'IBM Plex Mono slates the metadata. The full scale, as specimens:</p>'
    '<div class="surface demo-tile u-mb-8"><div class="demo">'
    + _spec('H1 · 700', 't-h1', 'Rebuilding my theme')
    + _spec('H2 · 600', 't-h2', 'From the blog')
    + _spec('H3 · 600', 't-h3', 'How I edit in one sitting')
    + _spec('H4 · 600', 't-h4', 'Field notes on shipping')
    + _spec('Lead · 400', 't-lead', 'The first paragraph runs a size up to set the tone.')
    + _spec('Body · 400', 't-body', 'Body copy is Inter at 1rem with 1.55–1.75 leading, capped to a reading measure.')
    + _spec('Small · 400', 't-small', 'Secondary UI text and dense metadata rows.')
    + _spec('Caption · 400', 't-small u-fg-faint', 'Muted captions, footnotes and helper text.')
    + _spec('Kicker · mono', 'eyebrow', 'Field notes')
    + _spec('Timecode · mono', 't-slate', 'EP.07 · 00:14:22 · 6 min read')
    + '</div><p class="spec"><b>.t-h1…h4 · .t-lead · .t-body · .t-small · .eyebrow · .t-slate</b> — the whole voice</p></div>\n')

# ── Long-form content (.content) ────────────────────────────────────────────

_content_doc = (
    '<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
    'One wrapper styles everything a rich-text editor can emit: headings, lists, '
    'quotes, rules, tables, code — and every Ghost Koenig card. Templates never '
    'style editor output themselves; they wrap it and walk away.</p>'
    + tile('<div class="content" style="max-width:none">'
           '<h2>A heading in the display face</h2>'
           '<p>Body copy sets at the reading measure with generous leading. '
           '<a href="#i">Links</a> underline on a hairline, <strong>strong</strong> '
           'goes semibold, and <mark>marked text</mark> takes the accent wash.</p>'
           '<ul><li>Lists get quiet markers</li><li>and breathing room between items</li></ul>'
           '<blockquote>The quote takes an accent rule, never a box.<cite>Frame &amp; Signal</cite></blockquote>'
           '<pre><code>const frame = (life) =&gt; life.filter(m =&gt; m.signal &gt; m.noise);</code></pre>'
           '</div>',
           '<b>.content</b> — headings · body · lists · quote · code, all inherited')
    + '<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Editor cards</h2>'
    + ct([
        ('.kg-width-wide / -full', 'break out of the prose column without the template knowing'),
        ('.kg-bookmark-card', 'title, description, metadata, thumbnail — stacks on phones'),
        ('.kg-callout-card (+ -accent)', 'emoji + text on a sunken panel'),
        ('.kg-toggle-card', 'native disclosure inside content'),
        ('.kg-button-card / .kg-btn', 'a pill button in the accent'),
        ('.kg-header-card · .kg-signup-card', 'in-content bands; signup rides the inverse surface'),
        ('.kg-gallery-card · .kg-embed-card', 'rows that keep their ratio; embeds default to 16:9'),
        ('.kg-audio-card · .kg-file-card · .kg-product-card', 'bordered surface cards'),
    ], head=('Card', 'Treatment'))
    + '<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">Why not <code class="t-code">.prose</code>?</h2>'
    '<p class="u-fg-subtle" style="max-width:var(--measure-lead)">'
    'Because <code class="t-code">@tailwindcss/typography</code> owns that class name, and it '
    'loads after most imports — its <code class="t-code">--tw-prose-*</code> colours silently '
    'win, and headings go dark in dark mode. A system that ships as a package must never fight '
    'a plugin half its users already have installed, so the component is '
    '<code class="t-code">.content</code>.</p>')

PAGES['content'] = ('Long-form content',
    'One wrapper for everything the editor emits — headings, quotes, tables, code and every '
    'Ghost card, styled from the same tokens.',
    _content_doc)
