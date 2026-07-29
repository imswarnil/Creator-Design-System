from common import tile, sec, END, ct

PAGES = {}

# ── The composites, relocated ───────────────────────────────────────────────
# These three used to sit in their own "Composites" nav group — named after how
# they are built rather than what they are for, which put a course's curriculum
# three groups away from the only collection that renders it. Each now lives
# with its owning collection. The content is unchanged; only the slug and the
# framing moved, and the old slugs redirect.

PAGES['course/curriculum'] = ('Course · curriculum',
    'The course curriculum: native &lt;details&gt; modules, lesson rows that tick off, '
    'the current lesson ringed, progress in the head. State lives in ARIA, never a styling class.',
    tile('<section class="curriculum" style="max-width:36rem">'
         '<header class="curriculum__head"><div><h3 class="curriculum__title">Syllabus</h3>'
         '<span class="curriculum__meta">2 modules · 7 lessons · 1h 44m</span></div>'
         '<div class="progress progress-thin" style="--value:43%;flex:1 1 100%"><span class="progress__bar"></span></div></header>'
         '<details class="curriculum__module" open><summary><span class="curriculum__no">01</span>'
         '<span class="curriculum__module-title">Tokens before templates</span><span class="curriculum__count">4 · 52m</span></summary>'
         '<ol class="curriculum__lessons">'
         '<li><a class="lesson-row" href="#i" data-done><span class="lesson-row__tick"></span><span class="lesson-row__title">Why the PDF was right</span><span class="lesson-row__len">09:12</span></a></li>'
         '<li><a class="lesson-row" href="#i" data-done><span class="lesson-row__tick"></span><span class="lesson-row__title">The ink ladder</span><span class="lesson-row__len">11:04</span></a></li>'
         '<li><a class="lesson-row" href="#i" aria-current="true"><span class="lesson-row__tick"></span><span class="lesson-row__title">One accent, rationed</span><span class="lesson-row__len">14:30</span></a></li>'
         '<li><a class="lesson-row" href="#i"><span class="lesson-row__tick"></span><span class="lesson-row__title">Spacing is a ladder</span><span class="lesson-row__len">08:47</span><span class="lesson-row__free">Free</span></a></li>'
         '</ol></details>'
         '<details class="curriculum__module"><summary><span class="curriculum__no">02</span>'
         '<span class="curriculum__module-title">Shipping the system</span><span class="curriculum__count">3 · 52m</span></summary>'
         '<ol class="curriculum__lessons">'
         '<li><a class="lesson-row" href="#i"><span class="lesson-row__tick"></span><span class="lesson-row__title">The one inverse band</span><span class="lesson-row__len">15:02</span></a></li>'
         '</ol></details></section>',
         '<b>.curriculum</b> — head + progress · <b>.lesson-row</b> with [data-done] / [aria-current] / __free')
    + ct([('Course page', 'curriculum lives in the MAIN column — never the sidebar (backlog rule)'),
          ('Lesson page', 'same component in the player rail, current lesson ringed'),
          ('[data-done]', 'set server-side or from localStorage — the tick fills'),
          ('aria-current="true"', 'you are here — ring + weight')],
         head=('Where', 'How')))


PAGES['projects/build-log'] = ('Projects · build log',
    'The project timeline: ▸ start, numbered middles, ✓ ship. Walked steps fill; the current one gets the ring.',
    tile('<ol class="buildlog" style="max-width:26rem">'
         '<li class="buildlog__step" data-kind="start" data-done><span class="buildlog__node"></span>'
         '<a class="buildlog__link" href="#i">Kick-off — scope &amp; sketches<span class="buildlog__date">Day 1 · Jun 02</span></a></li>'
         '<li class="buildlog__step" data-done><span class="buildlog__node">2</span>'
         '<a class="buildlog__link" href="#i">Foundation tokens land<span class="buildlog__date">Day 4 · Jun 05</span></a></li>'
         '<li class="buildlog__step" aria-current="step"><span class="buildlog__node">3</span>'
         '<a class="buildlog__link" href="#i">Components pass<span class="buildlog__date">Day 9 · Jun 10</span></a></li>'
         '<li class="buildlog__step" data-kind="ship"><span class="buildlog__node"></span>'
         '<a class="buildlog__link" href="#i">Ship v1<span class="buildlog__date">Day 14 · target</span></a></li>'
         '</ol>',
         '<b>.buildlog &gt; __step[data-kind][data-done][aria-current] &gt; __node + __link + __date</b>'))

PAGES['travel/itinerary'] = ('Travel · itinerary',
    'The trip, day by day — same rail as the build log wearing travel clothes: day chips, notes, stop badges.',
    tile('<ol class="itinerary" style="max-width:30rem">'
         '<li class="itinerary__day"><span class="itinerary__chip"><b>1</b><span>day</span></span>'
         '<h4 class="itinerary__title">Land in Tbilisi, walk the old town</h4>'
         '<p class="itinerary__note">Sulphur baths before the jet lag wins.</p>'
         '<div class="itinerary__stops"><span class="badge">Abanotubani</span><span class="badge">Funicular</span></div></li>'
         '<li class="itinerary__day"><span class="itinerary__chip"><b>2</b><span>day</span></span>'
         '<h4 class="itinerary__title">Kazbegi day trip</h4>'
         '<p class="itinerary__note">Gergeti Trinity on foot, weather permitting.</p>'
         '<div class="itinerary__stops"><span class="badge">Ananuri</span><span class="badge">Stepantsminda</span></div></li>'
         '<li class="itinerary__day"><span class="itinerary__chip"><b>3</b><span>day</span></span>'
         '<h4 class="itinerary__title">Wine country, slow train back</h4>'
         '<div class="itinerary__stops"><span class="badge">Sighnaghi</span><span class="badge">Telavi</span></div></li>'
         '</ol>',
         '<b>.itinerary &gt; __day &gt; __chip + __title + __note + __stops</b> — trip pages use it as the overview spine'))


# ── Timeline — the generic sequence the three above are dressings of ─────────

def _tl(items, cls='tl'):
    out = ''
    for it in items:
        a = ''
        if it.get('done'):
            a += ' data-done'
        if it.get('current'):
            a += ' aria-current="step"'
        if it.get('kind'):
            a += f' data-kind="{it["kind"]}"'
        time = f'<span class="tl__time">{it["time"]}</span>' if it.get('time') else ''
        note = f'<p class="tl__note">{it["note"]}</p>' if it.get('note') else ''
        meta = ('<div class="tl__meta">' + ''.join(
            f'<span class="badge">{m}</span>' for m in it['meta']) + '</div>'
        ) if it.get('meta') else ''
        out += (f'<li class="tl__item"{a}><span class="tl__node">{it.get("node","")}</span>'
                f'<div class="tl__body">{time}<span class="tl__title">{it["title"]}</span>'
                f'{note}{meta}</div></li>')
    return f'<ol class="{cls}">{out}</ol>'


_TL_STEPS = [
    dict(time='Jun 2024', title='Foundation tokens land', kind='start', done=True,
         note='Three tiers, one rename away from a rebrand.'),
    dict(time='Sep 2024', title='Components pass', node='2', done=True),
    dict(time='Now', title='Collections and pages', current=True, node='3',
         note='Twelve collections on one shared shell.', meta=['in flight']),
    dict(time='Q4', title='Ship v1 to npm', kind='ship'),
]

_tl_body = (
    '<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
    'An ordered sequence with a rail through it. <b>27-composite.css</b> opens by saying its '
    'four organs are "the same idea — an ordered list that knows where you are — wearing its '
    'collection\'s clothes"; this is that idea with no clothes on, so a page that needs a plain '
    'sequence does not borrow a build log and override every part that says <i>project</i>.</p>'

    + sec('axis', 'The axis is the only structural decision',
          'Vertical reads as a list and takes any length. Horizontal reads as a process, is '
          'bounded, scrolls rather than wraps — a horizontal timeline that wraps to a second '
          'row has stopped being one line of time — and folds back to vertical under 48rem '
          'rather than crushing itself.')
    + tile(_tl(_TL_STEPS), '<b>.tl</b> — vertical, the default')
    + tile(_tl(_TL_STEPS, 'tl tl-h'),
           '<b>.tl.tl-h</b> — horizontal. Narrow this window past 48rem and it becomes the '
           'one above')
    + END

    + sec('state', 'State is ARIA, never a styling class',
          'The node fills behind you, takes the accent ring where you are, and goes dashed '
          'ahead of you — so "how far along is this" survives with CSS off, and the '
          'accessibility tree and the styling can never disagree.')
    + ct([
        ('[data-done]', 'behind you — the node fills and shows a tick'),
        ('aria-current="step"', 'you are here — accent ring. <code class="t-code">step</code>, '
                                'not <code class="t-code">true</code>: this is a position in a '
                                'process, not the current page'),
        ('[data-kind]', '<code class="t-code">start</code> ▸ · <code class="t-code">ship</code> ✓ '
                        '· <code class="t-code">now</code> filled accent. Glyph only — the node '
                        'geometry never changes'),
        ('~ selector', 'everything after the current item recedes automatically. No class on '
                       'the future items'),
    ], head=('Hook', 'What it does'))
    + END

    + sec('variants', 'Four modifiers, both axes')
    + tile(_tl(_TL_STEPS[:3], 'tl tl-compact'),
           '<b>.tl-compact</b> — tighter rhythm, no notes expected. For a rail beside content')
    + tile(_tl([dict(time='2021 — 2024', title='Senior Product Engineer',
                     note='Design systems, and the sites that run on them.'),
                dict(time='2019 — 2021', title='Frontend Engineer',
                     note='Component library, then the migration onto it.')], 'tl tl-ranged'),
           '<b>.tl-ranged</b> — the node becomes a capsule that fills its row. A role held for '
           'three years is a bar, not a dot, which is what makes a CV read as duration')
    + tile(_tl(_TL_STEPS, 'tl tl-alt'),
           '<b>.tl-alt</b> — items alternate sides of a centred rail. Vertical only, and only '
           'above 48rem; below that it collapses to the plain rail rather than shrinking two '
           'columns into nothing')
    + tile(_tl(_TL_STEPS[:3], 'tl tl-lg'), '<b>.tl-lg</b> — roomier, for the three or four '
           'milestones that actually matter')
    + END

    + sec('who', 'Who wears which clothes',
          'The three collection composites are not replaced by this — each keeps a device that '
          'is genuinely about its subject. This is what to reach for when you have none of '
          'those subjects.')
    + ct([
        ('<code class="t-code">.tl</code>', 'a plain sequence — a roadmap, a changelog, a '
                                            'career history, "what happens next"'),
        ('<code class="t-code">.buildlog</code>', 'a project — ▸ start, numbered middles, ✓ ship. '
                                                  '<a href="/projects/build-log.html">Projects → '
                                                  'build log</a>'),
        ('<code class="t-code">.itinerary</code>', 'a trip — the day chip and a photo strip per '
                                                   'day. <a href="/travel/itinerary.html">Travel '
                                                   '→ itinerary</a>'),
        ('<code class="t-code">.curriculum</code>', 'a course — collapsible modules, tickable '
                                                    'lesson rows. <a href="/course/curriculum.html">'
                                                    'Course → curriculum</a>'),
        ('<code class="t-code">.col-order</code>', 'a collection\'s own series spine — already '
                                                   'in <b>collection.css</b>, used by trips, '
                                                   'seasons and the archive'),
    ], head=('Reach for', 'When'))
    + END

    + sec('print', 'It prints',
          'Horizontal folds to vertical, alternating collapses to one column, and the accent '
          'ring drops — a résumé is the most likely thing to be printed, and a two-column '
          'zig-zag does not survive a page break.')
    + END
)

PAGES['timeline'] = ('Timeline',
    'An ordered sequence with a rail through it — vertical or horizontal, four modifiers, '
    'state in ARIA, and it prints. The generic form the curriculum, build log and itinerary '
    'are all dressings of.', _tl_body)

# ── Sections ────────────────────────────────────────────────────────────────

PAGES['page-header'] = ('Page header',
    'How a collection opens: kicker with icon, display title, one line, quiet meta. '
    'Compact for child pages; the band header opens homepage sections.',
    tile('<header class="page-head" style="padding-top:0">'
         '<span class="page-head__kicker"><svg class="icon" aria-hidden="true"><use href="#i-camera"/></svg> Collection · Videos</span>'
         '<h1 class="page-head__title">Everything I\'ve filmed, framed.</h1>'
         '<p class="page-head__desc">Tutorials, build vlogs and the occasional over-produced answer to a simple question.</p>'
         '<div class="page-head__meta"><span class="page-head__count"><b>48</b> videos · updated Jul 2026</span>'
         '<div class="cluster-sm"><span class="chip" aria-pressed="true">All</span><span class="chip">Builds</span><span class="chip">Vlogs</span></div></div>'
         '</header>',
         '<b>.page-head</b> — kicker · title · desc · meta')
    + tile('<div class="sec-head-row" style="margin-bottom:0"><div>'
           '<span class="sec-head-row__kicker"><span class="dot dot-sm dot-live"></span> Fresh this week</span>'
           '<h2 class="sec-head-row__title">Most recent on swarnil</h2></div>'
           '<a class="sec-head-row__more" href="#i">View all <svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg></a></div>',
           '<b>.sec-head-row</b> — a band\'s opening line; one action allowed · <b>.page-head-sm</b> for child pages'))

PAGES['hero'] = ('Hero',
    'A hero states, it does not list: one headline, one accent word, at most two actions. '
    'Four shapes — the fourth being the cinematic one.',
    tile('<div class="hero hero-statement" style="padding-block:var(--space-6)">'
         '<span class="hero__eyebrow"><span class="dot dot-sm dot-live"></span> Salesforce engineer · Budapest</span>'
         '<h1 class="hero__title" style="font-size:var(--text-5xl)">Frame the <em>work</em> — and cut the noise.</h1>'
         '<p class="hero__lead">Courses, build logs, and the occasional trip — documented on camera.</p>'
         '<div class="hero__actions"><a class="btn btn-primary" href="#i"><svg class="icon btn__icon" aria-hidden="true"><use href="#i-play"/></svg> Watch the story</a>'
         '<a class="btn btn-secondary" href="#i">Read the blog</a></div></div>',
         '<b>.hero.hero-statement</b> — centred manifesto')
    + tile('<div class="hero hero-split" style="padding-block:var(--space-4)"><div>'
           '<span class="hero__eyebrow">Now shooting · S02</span>'
           '<h1 class="hero__title" style="font-size:var(--text-4xl)">The theme is the <em>episode</em>.</h1>'
           '<div class="hero__actions"><a class="btn btn-primary btn-sm" href="#i">Play E07</a><a class="btn btn-quiet btn-sm" href="#i">All episodes</a></div></div>'
           '<div class="hero-split__stage"><div class="frame frame-ink" style="aspect-ratio:16/9;display:grid;place-items:center" data-surface="inverse">'
           '<span class="play play-sm"><span class="play__disc"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg></span></span></div>'
           '<p class="hero-split__caption"><span>S02 · E07</span><span class="timecode">14:22</span></p></div></div>',
           '<b>.hero-split</b> — copy left, framed stage right')
    + tile('<div class="hero-band hero-band-media pattern pattern-topo" data-surface="inverse" style="min-height:16rem">'
           '<div class="hero-band__media"></div>'
           '<span class="hero__eyebrow">Travel · 4 countries</span>'
           '<h1 class="hero__title" style="font-size:var(--text-4xl)">Leave the desk. <em>Keep</em> the camera.</h1>'
           '<div class="hero__actions"><a class="btn btn-primary btn-sm" href="#i">All trips</a></div></div>',
           '<b>.hero-band.hero-band-media</b> — the inverse billboard, copy bottom-anchored')
    + '<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-2)">The cinematic one</h2>'
    + '<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
      'Two more modifiers on the same band, added because the travel collection had this '
      'shape as forty lines of inline style that no other page could reach: '
      '<code class="t-code">.hero-band-full</code> takes it to the full viewport and pulls '
      'it up under the floating nav, and <code class="t-code">.hero-band__scan</code> lays '
      'a film over the footage. Put any <code class="t-code">.pattern-scanline</code> inside '
      'the scan layer; add <code class="t-code">data-ripple</code> and '
      '<code class="t-code">nav.js</code> tracks the pointer through it via '
      '<code class="t-code">--mx</code>/<code class="t-code">--my</code>. With the script '
      'blocked the mask rests centred — a vignette, not a broken effect — and under '
      '<code class="t-code">prefers-reduced-motion</code> the film stops chasing, the '
      'displacement freezes and looping footage pauses.</p>'
    + tile('<div class="hero hero-band hero-band-media pattern pattern-topo"'
           ' data-surface="inverse" style="min-height:18rem;position:relative">'
           '<div class="hero-band__media"></div>'
           '<div class="hero-band__scan" data-ripple aria-hidden="true">'
           '<div class="pattern pattern-scanline pattern-media pattern-lg"></div></div>'
           '<div style="position:relative;z-index:1">'
           '<span class="hero__eyebrow">The travel collection</span>'
           '<h1 class="hero__title" style="font-size:var(--text-4xl)">'
           'Every road, <em>in order</em>.</h1>'
           '<p class="hero__lead">Move the pointer across the frame.</p></div></div>',
           '<b>.hero-band__scan[data-ripple]</b> — the film, revealed where the pointer is. '
           'Shown here at 18rem rather than the real <b>.hero-band-full</b> 100dvh, which '
           'would take the whole docs viewport')
    + ct([
        ('.hero-band-full', 'full viewport, full bleed, pulled up under the island nav'),
        ('.hero-band__scan', 'the film layer — holds a <code class="t-code">.pattern-*</code>, '
                             'blends over the footage'),
        ('[data-ripple]', 'nav.js tracks the pointer; CSS masks the film to a soft circle '
                          'around it'),
        ('--mx / --my', 'the only two things the script writes. Every visual decision stays '
                        'in CSS'),
    ], head=('Class', 'What it adds')))

PAGES['stats'] = ('Stats',
    'Display-face tabular numbers, slate labels, hairlines not boxes. One surface, not four cards.',
    tile('<div class="stats">'
         '<div class="stat"><span class="stat__value">214</span><span class="stat__label">Posts published</span><span class="stat__note" data-trend="up">↑ 12 this quarter</span></div>'
         '<div class="stat"><span class="stat__value">48</span><span class="stat__label">Videos</span><span class="stat__note">last upload Sat</span></div>'
         '<div class="stat stat-live"><span class="stat__value">3<small>live</small></span><span class="stat__label"><span class="dot dot-sm dot-live"></span> Projects rolling</span></div>'
         '<div class="stat"><span class="stat__value">11<small>yrs</small></span><span class="stat__label">Making things</span></div>'
         '</div>',
         '<b>.stats &gt; .stat (+ __value/__label/__note)</b> · <b>.stat-live</b>')
    + tile('<div class="stats stats-bare">'
           '<div class="stat"><span class="stat__value">6</span><span class="stat__label">Collections</span></div>'
           '<div class="stat"><span class="stat__value">1.2k</span><span class="stat__label">Subscribers</span></div>'
           '<div class="stat"><span class="stat__value">37</span><span class="stat__label">Countries read</span></div>'
           '</div>',
           '<b>.stats-bare</b> — no chrome, for heroes and footers · <b>.stats-inverse</b> on ink'))

PAGES['cta'] = ('CTA',
    'One ask per page, near the end — the only inverse band in view. The sponsor strip stays on the paper.',
    tile('<div class="cta cta-newsletter pattern pattern-grid" data-surface="inverse">'
         '<span class="cta__kicker"><svg class="icon" aria-hidden="true" style="width:1rem;height:1rem"><use href="#i-mail"/></svg> The newsletter</span>'
         '<h2 class="cta__title">One honest email, <em>every</em> other Sunday.</h2>'
         '<form class="cta-newsletter__form" onsubmit="return false">'
         '<input class="input" type="email" placeholder="you@example.com" aria-label="Email" />'
         '<button class="btn btn-primary" type="button">Subscribe</button></form>'
         '<p class="cta__fine">1,204 readers · unsubscribe anytime</p></div>',
         '<b>.cta.cta-newsletter</b> — kicker, one accent word, form, honest fine print')
    + tile('<div class="cta-sponsor"><div><span class="cta__kicker">Sponsorship</span>'
           '<h3 class="cta__title">Put your product in front of people who build.</h3></div>'
           '<div class="cta__actions"><a class="btn btn-secondary" href="#i">Media kit</a>'
           '<a class="btn btn-primary" href="#i">Sponsor an issue</a></div></div>',
           '<b>.cta-sponsor</b> — bordered, on the paper: money asks politely · <b>.cta-left</b> for column layouts'))

PAGES['footer'] = ('Footer',
    'The end credits: brand + exhaustive sitemap over a hairline, then the sign-off where the dot ends the page.',
    tile('<footer class="footer" style="margin-top:0;padding-top:var(--space-4)">'
         '<div class="footer__grid"><div class="footer__brand">'
         '<span class="logo logo-sm">Swarn<span class="logo__i">ı<i class="logo__tittle"></i></span>l</span>'
         '<p class="footer__tag">Documenting the work — code, camera, and the road between.</p>'
         '<div class="footer__social">'
         '<a class="btn btn-quiet btn-sm btn-icon" href="#i" aria-label="YouTube"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg></a>'
         '<a class="btn btn-quiet btn-sm btn-icon" href="#i" aria-label="GitHub"><svg class="icon" aria-hidden="true"><use href="#i-code"/></svg></a>'
         '</div></div>'
         '<div><h4 class="footer__head">Watch</h4><div class="footer__links"><a href="#i">Videos</a><a href="#i">Web series</a></div></div>'
         '<div><h4 class="footer__head">Learn</h4><div class="footer__links"><a href="#i">Courses</a><a href="#i">Guides</a><a href="#i">Docs</a></div></div>'
         '<div><h4 class="footer__head">Meta</h4><div class="footer__links"><a href="#i">About</a><a href="#i">Resume</a><a href="#i">Sponsor</a></div></div>'
         '</div><div class="footer__signoff"><span>© 2026 Swarnil Singhai · Ghost</span>'
         '<span class="footer__rec"><span class="dot dot-sm dot-live"></span> still rolling</span></div></footer>',
         '<b>.footer</b> — __grid/__brand/__head/__links/__signoff/__rec · <b>.footer-inverse</b> to end on ink'))

# ── Utilities ───────────────────────────────────────────────────────────────

def upage(slug, title, lead, rows, demo=None):
    body = ct(rows)
    if demo:
        body += demo
    PAGES[slug] = (title, lead, body)

upage('u-background', 'Background', 'Semantic surfaces only — markup never names a ramp step.',
      [('.u-bg-canvas / -surface / -sunken / -raised', 'the elevation ladder'),
       ('.u-bg-inverse', 'ink band; sets --fg-on-inverse too'),
       ('.u-bg-accent / .u-bg-accent-soft', 'the rationed loud pair'),
       ('.u-bg-transparent', 'strip an inherited surface')],
      tile('<div class="u-flex u-gap-3 u-wrap">'
           '<span class="u-bg-surface u-border u-rounded u-p-3 t-slate-sm">surface</span>'
           '<span class="u-bg-sunken u-border u-rounded u-p-3 t-slate-sm">sunken</span>'
           '<span class="u-bg-inverse u-rounded u-p-3 t-slate-sm">inverse</span>'
           '<span class="u-bg-accent u-rounded u-p-3 t-slate-sm">accent</span>'
           '<span class="u-bg-accent-soft u-rounded u-p-3 t-slate-sm">accent-soft</span></div>',
           'the surface family'))

upage('u-borders', 'Borders', 'Hairlines and the radius ladder.',
      [('.u-border / .u-border-0', 'hairline on, off'),
       ('.u-border-top / -bottom', 'one edge'),
       ('.u-border-subtle / -strong / -accent', 'line weight by color'),
       ('.u-rounded-sm/-/-lg/-card/-pill/-full', 'the radius ladder')],
      tile('<div class="u-flex u-gap-3 u-wrap u-items-center">'
           '<span class="u-border u-rounded-sm u-p-3 t-slate-sm">sm</span>'
           '<span class="u-border u-rounded u-p-3 t-slate-sm">md</span>'
           '<span class="u-border u-rounded-lg u-p-3 t-slate-sm">lg</span>'
           '<span class="u-border u-rounded-card u-p-3 t-slate-sm">card</span>'
           '<span class="u-border u-rounded-pill u-px-4 u-py-2 t-slate-sm">pill</span>'
           '<span class="u-border u-border-accent u-rounded u-p-3 t-slate-sm">accent</span></div>',
           'radii, to scale'))

upage('u-colors', 'Colors', 'Foreground utilities — semantic, both themes, verified contrast.',
      [('.u-fg-default', 'primary ink'), ('.u-fg-subtle', 'supporting copy'),
       ('.u-fg-muted / .u-fg-faint', 'meta, disabled'),
       ('.u-fg-accent', 'the accent as text — sparingly'),
       ('.u-fg-on-inverse', 'text on ink bands')],
      tile('<p class="u-fg-default">default ink</p><p class="u-fg-subtle">subtle</p>'
           '<p class="u-fg-muted">muted</p><p class="u-fg-faint">faint</p><p class="u-fg-accent">accent</p>',
           'the text ladder — flip the theme to verify both'))

upage('u-display', 'Display', 'Display modes plus the four responsive hiders.',
      [('.u-block / .u-inline / .u-inline-block', 'flow modes'),
       ('.u-flex / .u-inline-flex / .u-grid', 'layout modes'),
       ('.u-none', 'gone'), ('.u-contents', 'unwrap a wrapper'),
       ('.u-md-down-none / .u-md-up-none', 'hide below / from 48rem'),
       ('.u-lg-down-none / .u-lg-up-none', 'hide below / from 64rem')])

upage('u-flex', 'Flex', 'Direction, wrap, alignment, growth — the flexbox vocabulary.',
      [('.u-row / .u-col', 'direction'), ('.u-wrap / .u-nowrap-flex', 'wrapping'),
       ('.u-items-start/-center/-end/-baseline', 'cross-axis'),
       ('.u-justify-start/-center/-end/-between', 'main axis'),
       ('.u-grow / .u-grow-0 / .u-shrink-0 / .u-flex-1', 'growth'),
       ('.u-self-start/-center/-end/-stretch', 'per-item override'),
       ('.u-order-first / .u-order-last', 'visual order (use rarely — AT reads DOM order)')],
      tile('<div class="u-flex u-gap-2 u-items-center u-border u-rounded u-p-3">'
           '<span class="badge">a</span><span class="badge u-grow u-text-center">grow</span><span class="badge">c</span></div>',
           'a row with one growing member'))

upage('u-float', 'Float', 'For prose intrusions only — layout belongs to flex and grid.',
      [('.u-float-start / .u-float-end', 'logical floats'),
       ('.u-float-none', 'cancel'), ('.u-clearfix', 'contain floats')],
      tile('<div class="u-clearfix u-border u-rounded u-p-4" style="max-width:30rem">'
           '<span class="u-float-end u-bg-accent-soft u-rounded u-p-2 t-slate-sm" style="margin-left:var(--space-3)">floats end</span>'
           '<p class="t-small u-fg-subtle">The paragraph wraps around the floated chip the way a pullquote intrudes into an article — the one legitimate float.</p></div>',
           '.u-float-end inside .u-clearfix'))

upage('u-interactions', 'Interactions', 'Cursor, pointer-events, selection, touch.',
      [('.u-pointer / .u-cursor-default / .u-not-allowed', 'cursor states'),
       ('.u-pe-none / .u-pe-auto', 'pointer-events off/on (decorative overlays)'),
       ('.u-select-none / -all / -text', 'selection behaviour'),
       ('.u-touch-pan', 'pan-x pan-y — the carousel scroll-trap fix')],
      tile('<div class="cluster-sm">'
           '<span class="badge u-pointer">pointer</span>'
           '<span class="badge u-not-allowed">not-allowed</span>'
           '<code class="t-code u-select-all">u-select-all: click selects me whole</code></div>',
           'try the cursors and the one-click select'))

upage('u-overflow', 'Overflow', 'Clip it, scroll it, or let it breathe — per axis.',
      [('.u-overflow-auto / -hidden / -visible', 'both axes'),
       ('.u-overflow-x-auto / .u-overflow-y-auto', 'one axis'),
       ('.u-scroll-thin', 'thin scrollbars where they must show')],
      tile('<div class="u-overflow-x-auto u-scroll-thin u-border u-rounded u-p-3" style="max-width:22rem">'
           '<div class="u-flex u-gap-2" style="width:40rem">'
           + ''.join(f'<span class="badge">chip {i}</span>' for i in range(1, 11))
           + '</div></div>',
           'a row that scrolls inside its container — the page never scrolls sideways'))

upage('u-position', 'Position', 'Placement plus the sticky helper.',
      [('.u-static / .u-relative / .u-absolute / .u-fixed', 'position modes'),
       ('.u-sticky', 'sticky with the standard top offset'),
       ('.u-inset-0 / .u-top-0 / .u-bottom-0 / .u-start-0 / .u-end-0', 'edges (logical)')],
      tile('<div class="u-relative u-border u-rounded-lg pattern pattern-dots" style="height:8rem">'
           '<span class="badge badge-signal u-absolute" style="top:var(--space-2);inset-inline-end:var(--space-2)">u-absolute</span></div>',
           'a badge pinned to a relative parent'))

upage('u-shadows', 'Shadows', 'The elevation ladder — in dark themes it swaps for a lit top edge.',
      [('.u-shadow-0 … .u-shadow-5', 'ascending elevation'),
       ('.u-shadow-none', 'flat')],
      tile('<div class="u-flex u-gap-4 u-wrap">'
           + ''.join(f'<span class="u-bg-surface u-rounded u-p-3 u-shadow-{i} t-slate-sm">{i}</span>' for i in range(6))
           + '</div>',
           'shadow-0 through shadow-5 — flip the theme to see the dark-mode treatment'))

upage('u-sizing', 'Sizing', 'Widths, heights, and the measure caps.',
      [('.u-w-full / -fit / -min / -max', 'width modes'),
       ('.u-h-full / .u-h-dvh', 'height'),
       ('.u-max-w-full / -prose / -lead / -ui', 'caps — prose 65ch, lead 55ch, ui 40ch'),
       ('.u-min-w-0', 'let flex children truncate')],
      tile('<p class="u-max-w-prose t-small u-fg-subtle">u-max-w-prose caps this line at reading measure so it never becomes a cinemascope sentence that the eye loses on the way back to the left edge.</p>',
           'the measure caps'))

upage('u-spacing', 'Spacing', 'Margin, padding and gap off the 4px ladder — never a raw px.',
      [('.u-m-0 / .u-m-auto / .u-mx-auto', 'margin resets and centering'),
       ('.u-mt-1…16 / .u-mb-1…12', 'block margins on the ladder'),
       ('.u-ms-auto / .u-me-auto', 'logical push (flex rows)'),
       ('.u-p-0…8 / .u-px-* / .u-py-*', 'padding'),
       ('.u-gap-1…8', 'flex/grid gaps')],
      tile('<div class="u-flex u-gap-2 u-items-end">'
           + ''.join(f'<span class="u-bg-accent-soft u-rounded u-p-{i} t-slate-sm">p-{i}</span>' for i in (1, 2, 3, 4, 6, 8))
           + '</div>',
           'the padding ladder, felt'))

upage('u-text', 'Text', 'Alignment, transform, wrapping, weight — the typographic switches.',
      [('.u-text-start / -center / -end', 'alignment (logical)'),
       ('.u-uppercase / -capitalize / .u-normal-case', 'transforms'),
       ('.u-truncate', 'one line + ellipsis (needs .u-min-w-0 in flex)'),
       ('.u-nowrap / .u-break', 'wrap control'),
       ('.u-balance / .u-pretty', 'headline / paragraph wrapping'),
       ('.u-tabular', 'tabular numerals for tables and timecodes'),
       ('.u-weight-regular…bold', 'weight ladder'),
       ('.u-italic / .u-underline / .u-no-underline', 'inline styles')],
      tile('<p class="u-truncate u-border u-rounded u-p-2 t-small" style="max-width:16rem">This sentence is far too long for its container and admits it with an ellipsis.</p>',
           '.u-truncate — the honest overflow'))

upage('u-valign', 'Vertical align', 'For inline boxes and table cells — flex alignment lives on the Flex page.',
      [('.u-align-baseline / -top / -middle / -bottom', 'inline boxes'),
       ('.u-align-text-top / -text-bottom', 'relative to the line box')],
      tile('<p class="u-border u-rounded u-p-3" style="font-size:1.4rem">word'
           '<span class="badge u-align-baseline">baseline</span>'
           '<span class="badge u-align-middle">middle</span>'
           '<span class="badge u-align-top">top</span></p>',
           'badges riding one line at three alignments'))

upage('u-visibility', 'Visibility', 'Three ways to disappear, each honest about what it keeps.',
      [('.u-invisible / .u-visible', 'hidden but keeps its space and tab order off'),
       ('.u-none', 'gone from layout and the accessibility tree'),
       ('.u-sr-only', 'invisible to eyes, present to screen readers — labels, skip links')],
      tile('<div class="u-flex u-gap-2"><span class="badge">visible</span>'
           '<span class="badge u-invisible">invisible</span><span class="badge">after the gap</span></div>'
           '<p class="t-small u-fg-subtle u-mt-3">The middle badge is .u-invisible — its space survives. '
           '<span class="u-sr-only">This sentence is read aloud but never seen.</span></p>',
           'invisible keeps the gap; sr-only speaks'))
