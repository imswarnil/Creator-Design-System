from common import tile, sec, END, ct

PAGES = {}

# ── Layout ──────────────────────────────────────────────────────────────────

PAGES['breakpoints'] = ('Breakpoints',
    'Four widths, defined by content, not devices. Rems, so user zoom moves them.',
    ct([('— &lt; 40rem', 'phone — single column, stacked heroes, drawer nav'),
        ('40rem (sm)', 'big phone / small tablet — 2-up decks'),
        ('48rem (md)', 'tablet — footer grid gains the brand column'),
        ('64rem (lg)', 'desktop — split heroes, rails, the docs sidebar docks'),
        ('86rem (xl)', 'wide — rail ads, leaderboard slots')],
       head=('Breakpoint', 'What changes'))
    + tile('<div class="u-flex u-gap-2 u-wrap">'
           '<span class="badge">u-md-down-none</span><span class="badge">u-md-up-none</span>'
           '<span class="badge">u-lg-down-none</span><span class="badge">u-lg-up-none</span></div>',
           'the only responsive display utilities — resize to test'))

PAGES['containers'] = ('Containers',
    'Five measures. Content picks the narrowest container that fits its job.',
    ct([('.container', 'var(--w-site) — the default page column'),
        ('.container-narrow', 'var(--w-narrow) — forms, sign-in, 404 copy'),
        ('.container-prose', 'var(--w-prose) — article measure'),
        ('.container-wide', 'var(--w-wide) — poster walls, big decks'),
        ('.container-full', 'edge to edge, gutters only')])
    + tile('<div class="stack-sm">'
           '<div class="u-bg-accent-soft u-border u-border-accent u-rounded u-p-2 u-text-center t-slate-sm">container</div>'
           '<div class="u-bg-accent-soft u-border u-border-accent u-rounded u-p-2 u-text-center t-slate-sm" style="max-width:75%">container-prose</div>'
           '<div class="u-bg-accent-soft u-border u-border-accent u-rounded u-p-2 u-text-center t-slate-sm" style="max-width:55%">container-narrow</div>'
           '</div>', 'relative widths, to scale'))

PAGES['grid'] = ('Grid',
    'Fixed grids for known counts, auto grids for card decks, rail grids for content + sidebar.',
    tile('<div class="grid-3 grid-demo"><div>1</div><div>2</div><div>3</div></div>',
         '<b>.grid-2 / -3 / -4 / -6 / -12</b> — fixed columns, collapse on small screens')
    + tile('<div class="grid-auto grid-demo"><div>auto</div><div>auto</div><div>auto</div><div>auto</div></div>',
           '<b>.grid-auto (-sm / -lg)</b> — as many columns as fit the min width')
    + tile('<div class="grid-rail grid-demo"><div style="min-height:4rem">main</div><div>rail</div></div>',
           '<b>.grid-rail / .grid-rail-left</b> — the content + sticky sidebar shape')
    + tile('<div class="grid-editorial grid-demo"><div>text measure</div></div>',
           '<b>.grid-editorial</b> — prose · wide · full-bleed tracks for article layouts'))

PAGES['columns'] = ('Columns & gutters',
    'Gaps come off the same 4px ladder as everything else — never invent a gutter.',
    tile('<div class="u-grid u-gap-2 grid-demo" style="grid-template-columns:1fr 1fr 1fr"><div>gap-2</div><div>gap-2</div><div>gap-2</div></div>'
         '<div class="u-grid u-gap-6 grid-demo u-mt-4" style="grid-template-columns:1fr 1fr 1fr"><div>gap-6</div><div>gap-6</div><div>gap-6</div></div>',
         '<b>.u-gap-1…8</b> — gutter ladder')
    + tile('<div class="grid-12 grid-demo"><div style="grid-column:span 8">span 8</div><div style="grid-column:span 4">span 4</div></div>',
           '<b>.grid-12</b> + <b>grid-column: span n</b> — the asymmetric splits')
    + ct([('.stack / .stack-sm / .stack-lg', 'vertical rhythm between siblings'),
          ('.cluster / .cluster-sm / .cluster-lg', 'horizontal wrap groups'),
          ('.row-between', 'space-between row, centred items'),
          ('.flow', 'owl-spaced prose blocks')]))

PAGES['z-index'] = ('Z-index',
    'A five-step ladder. If two things fight, one of them is on the wrong step.',
    ct([('--z-below · .u-z-below', 'behind the canvas (pattern layers)'),
        ('--z-raised · .u-z-raised', 'card cover links, badges over media'),
        ('--z-nav · .u-z-nav', 'the nav island, this sidebar'),
        ('--z-overlay · .u-z-overlay', 'modals, offcanvas, toasts'),
        ('--z-top · .u-z-top', 'skip link, debug chrome')],
       head=('Step', 'Owns')))

# ── Content ─────────────────────────────────────────────────────────────────

PAGES['reboot'] = ('Reboot',
    'The foundation reset: box-sizing everywhere, media that can\'t overflow, '
    'fonts that inherit, margins zeroed so ladders own the rhythm.',
    ct([('*, ::before, ::after', 'box-sizing: border-box'),
        ('img, video, svg, canvas', 'display block · max-width 100%'),
        ('h1–h6, p, figure, blockquote', 'margin 0 — spacing comes from .stack/.flow'),
        ('button, input, select, textarea', 'font: inherit, color: inherit'),
        ('body', 'bg-canvas · fg-default · font-body · antialiased'),
        (':focus-visible', 'the one focus ring, accent, 2px offset')],
       head=('Selector', 'Rule'))
    + tile('<figure class="u-m-0"><div class="u-bg-sunken u-rounded u-p-4 t-slate-sm">Anything inside a fresh element starts unstyled and inherits ink.</div></figure>',
           '00-reboot.css — runs before every layer'))

PAGES['typography'] = ('Typography',
    'Three faces with jobs: Space Grotesk displays, Inter reads, IBM Plex Mono slates. '
    'Roles, not sizes — markup asks for a voice.',
    tile('<p class="t-display-2">Display — the statement voice</p>'
         '<p class="t-h2 u-mt-4">Heading two</p><p class="t-h3 u-mt-2">Heading three</p><p class="t-h4 u-mt-2">Heading four</p>',
         '<b>.t-display-1/-2 · .t-h1–h4</b> — Space Grotesk, tight tracking')
    + tile('<p class="t-lead">Lead — the first paragraph earns a size up.</p>'
           '<p class="t-body u-mt-3" style="max-width:var(--measure-prose)">Body — Inter at reading measure. The paragraph is the unit of thought, and the measure caps at 65 characters so lines can be re-found.</p>'
           '<p class="t-small u-fg-subtle u-mt-3">Small — captions and metadata prose.</p>',
           '<b>.t-lead · .t-body · .t-small</b>')
    + tile('<p class="t-slate">SLATE · TAKE 47 · 00:12:47</p>'
           '<p class="t-quote u-mt-4">“The quote voice gets the serif treatment and a hanging quote.”</p>'
           '<p class="u-mt-4">Inline: <a class="t-link" href="#type">a link</a>, <code class="t-code">code</code>, <mark class="mark">marked</mark>, <kbd class="kbd">⌘K</kbd>, <span class="t-accent">the accent word</span>.</p>',
           '<b>.t-slate · .t-quote · .t-link · .t-code · .mark · .kbd</b>'))

PAGES['images'] = ('Images & figures',
    'Media is always framed, always ratio\'d, never allowed to reflow the page.',
    tile('<div class="grid-2">'
         '<figure class="figure u-m-0"><div class="pattern pattern-grid pattern-media u-rounded-lg u-border" style="aspect-ratio:16/9"></div>'
         '<figcaption class="figure__caption">.figure — media + slate caption</figcaption></figure>'
         '<figure class="figure u-m-0"><div class="frame frame-4 pattern pattern-hatch" style="aspect-ratio:16/9"></div>'
         '<figcaption class="figure__caption">.frame — the viewfinder device</figcaption></figure>'
         '</div>',
         '<b>.figure · .figure__caption · .frame</b>')
    + tile('<div class="u-flex u-gap-4 u-items-end u-wrap">'
           '<div class="pattern pattern-dots u-border u-rounded-lg" style="width:9rem;aspect-ratio:1"></div>'
           '<div class="pattern pattern-dots u-border u-rounded-lg" style="width:12rem;aspect-ratio:4/5"></div>'
           '<div class="pattern pattern-dots u-border u-rounded-lg" style="width:16rem;aspect-ratio:21/9"></div>'
           '</div>',
           'ratios from the token sheet: 1:1 · 4:5 · 16:9 · 21:9 — set <b>aspect-ratio</b>, let the image cover')
    + ct([('width/height attrs', 'always — CLS is a layout bug, not a perf stat'),
          ('loading="lazy" decoding="async"', 'everything below the fold'),
          ('.u-object-cover / .u-object-contain', 'fill the frame vs letterbox in it')],
         head=('Rule', 'Why')))

PAGES['tables'] = ('Tables',
    'Hairlines and alignment do all the work. Numbers right-aligned and tabular; wrap wide tables, never the page.',
    tile('<div class="table-wrap"><table class="table" style="width:100%"><thead><tr>'
         '<th>Episode</th><th>Published</th><th style="text-align:right">Runtime</th><th style="text-align:right">Views</th></tr></thead><tbody>'
         '<tr><td>Rebuilding from tokens</td><td>Jul 19</td><td style="text-align:right" class="u-tabular">14:22</td><td style="text-align:right" class="u-tabular">8,412</td></tr>'
         '<tr><td>One query, six hours saved</td><td>Jul 12</td><td style="text-align:right" class="u-tabular">09:41</td><td style="text-align:right" class="u-tabular">12,077</td></tr>'
         '<tr><td>The curriculum question</td><td>Jul 05</td><td style="text-align:right" class="u-tabular">12:03</td><td style="text-align:right" class="u-tabular">6,930</td></tr>'
         '</tbody></table></div>',
         '<b>.table</b> in a <b>.table-wrap</b> — the wrap scrolls, the page never does')
    + tile('<table class="table table-compact" style="width:100%"><tbody>'
           '<tr><td>Compact rows</td><td class="u-fg-subtle">for dense reference data</td></tr>'
           '<tr><td>Definition list twin</td><td class="u-fg-subtle">.dl for label:value pairs</td></tr>'
           '</tbody></table>',
           '<b>.table-compact · .dl · .rule-list · .steps</b> — the list family'))

PAGES['quotes'] = ('Quotes',
    'Three grades of borrowed words: inline, block, and the pullquote that interrupts the page.',
    tile('<p style="max-width:var(--measure-prose)">Inline quoting stays in the sentence — <q>make something people love</q> — and the browser brings the marks.</p>',
         '<b>&lt;q&gt;</b> — inline')
    + tile('<blockquote class="pullquote u-m-0"><p class="pullquote__text">Life looks better when you make something people love — because what you make is who you are.</p>'
           '<footer class="pullquote__cite">— the site\'s one thesis</footer></blockquote>',
           '<b>.pullquote · .pullquote__text · .pullquote__cite</b>')
    + tile('<blockquote class="u-m-0 u-border-top u-border-bottom u-py-6 u-text-center">'
           '<p class="t-quote">“A quote big enough to be a section break earns hairlines, not a box.”</p></blockquote>',
           'the section-break grade — rules above and below, nothing else'))

PAGES['code'] = ('Code & syntax',
    'Five token roles, line numbers, line highlights, and a copy button that says so. '
    'Dark slab by default; a light twin for prose.',
    tile('''<figure class="codebox u-m-0"><figcaption class="codebox__head"><span class="codebox__lang">handlebars</span>
<button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>
<pre class="codebox__pre"><code><span class="ln"><span class="tok-com">{{!-- the film, fetched once --}}</span></span><span class="ln"><span class="tok-key">{{#get</span> <span class="tok-str">"posts"</span> filter=<span class="tok-str">"tag:hash-trip"</span> limit=<span class="tok-num">"1"</span> <span class="tok-key">as</span> |film|<span class="tok-key">}}</span></span><span class="ln ln-hl">  <span class="tok-key">{{#if</span> film.length<span class="tok-key">}}</span><span class="tok-fn">{{> hero-film}}</span><span class="tok-key">{{/if}}</span></span><span class="ln"><span class="tok-key">{{/get}}</span></span></code></pre></figure>''',
         '<b>.codebox</b> — head + lang + <b>[data-copy]</b> · <b>.ln</b> numbers · <b>.ln-hl</b> highlight · <b>.tok-key/-str/-num/-fn/-com</b>')
    + tile('''<figure class="codebox codebox-light u-m-0"><figcaption class="codebox__head"><span class="codebox__lang">css</span>
<button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>
<pre class="codebox__pre"><code><span class="ln"><span class="tok-com">/* one accent, rationed */</span></span><span class="ln"><span class="tok-fn">.hero__title</span> em { <span class="tok-key">color</span>: <span class="tok-str">var(--accent)</span>; }</span></code></pre></figure>''',
           '<b>.codebox-light</b> — the prose-friendly twin, own token colours')
    + tile('<span class="copy-line"><code>npm run build && npx gscan .</code><button type="button" data-copy>Copy</button></span>',
           '<b>.copy-line</b> — one-liners with the copy chip'))

# ── Layouts overview ────────────────────────────────────────────────────────

_CATS = [
    ('l-core', 'Core', 'Home, post, page, collection index, tag, tags, archive, 404 — the pages every site has.'),
    ('l-watch', 'Watch', 'Videos wall, video player page, series billboard, episode player.'),
    ('l-learn', 'Learn', 'Course overview, lesson player, docs, guide steps.'),
    ('l-build', 'Build', 'Projects, project overview, build-log steps, products.'),
    ('l-road', 'Road', 'Travel index, trip overview, travel story, timeline.'),
    ('l-pages', 'Pages', 'About, resume, contact, sign in/up, guestbook, sponsor — the one-offs.'),
]

_ov = ('\t\t<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
       'Each category page draws its layouts as wireframes: grey is content, '
       '<span style="color:var(--accent)">accent</span> is the container\'s organ '
       '(curriculum, build log, itinerary), hatched is media, ink is an inverse band. '
       'Rails are sticky unless noted.</p>\n'
       '\t\t<div class="list-group u-mb-6" style="max-width:36rem">')
for _s, _l, _d in _CATS:
    _ov += (f'<a class="list-group__item" href="./{_s}.html" style="align-items:baseline">'
            f'<span class="u-weight-semibold" style="flex:0 0 5rem">{_l}</span>'
            f'<span class="t-small u-fg-subtle u-grow">{_d}</span>'
            f'<svg class="icon u-shrink-0" aria-hidden="true" style="width:1rem;height:1rem"><use href="#i-arrow"/></svg></a>')
_ov += '</div>'
_ov += ('\n\t\t<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">The contract</h2>'
        '\n\t\t<p class="u-fg-subtle" style="max-width:var(--measure-lead)">'
        'A layout is a promise, not a suggestion: the course page keeps its curriculum in the '
        'MAIN column; the episode page keeps its list on the RIGHT; prose never exceeds its '
        'measure. Templates converge on these floor plans as the system lands.</p>')

PAGES['layouts'] = ('Layouts',
    'Every template a creator site needs, drawn as floor plans — grouped into six '
    'categories, each with its own page and variants.',
    _ov)
