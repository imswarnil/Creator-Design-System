from common import tile, sec, END, ct

PAGES = {}

PAGES['accordion'] = ('Accordion',
    'Collapses welded into one surface, native &lt;details&gt; underneath. The signal dot marks the open panel.',
    tile('<div class="acc" style="max-width:34rem">'
         '<details class="collapse" open><summary>Why tokens before templates?</summary>'
         '<div class="collapse__body">Because a template argues about one page; a token settles it for every page at once.</div></details>'
         '<details class="collapse"><summary>Why only one accent colour?</summary>'
         '<div class="collapse__body">The dot means <em>live</em>. Two accents and neither means anything.</div></details>'
         '<details class="collapse"><summary>Why native details?</summary>'
         '<div class="collapse__body">Keyboard, screen readers and find-in-page all work before any JS loads.</div></details>'
         '</div>',
         '<b>.acc &gt; .collapse</b> — dot on the open panel, hairlines between')
    + tile('<div class="acc" style="max-width:34rem">'
           '<details class="collapse" name="acc-x" open><summary>Exclusive group — one open</summary><div class="collapse__body">These share <code class="t-code">name="acc-x"</code>, so opening one closes the rest. Platform feature, zero JS.</div></details>'
           '<details class="collapse" name="acc-x"><summary>Second panel</summary><div class="collapse__body">Opens alone.</div></details>'
           '<details class="collapse" name="acc-x"><summary>Third panel</summary><div class="collapse__body">Also alone.</div></details>'
           '</div>',
           'exclusive accordion — <b>&lt;details name="…"&gt;</b>'))

PAGES['alerts'] = ('Alerts',
    'A message with a tone. Five tones, one shape; the title is optional, the border always speaks.',
    tile('<div class="stack-sm" style="max-width:36rem">'
         '<div class="alert alert-info"><p class="alert__title">Heads up</p>Routes.yaml must be re-uploaded before /design/ resolves.</div>'
         '<div class="alert alert-success"><p class="alert__title">Shipped</p>gscan is clean — the theme is Ghost 6.x compatible.</div>'
         '<div class="alert alert-warning"><p class="alert__title">Careful</p>Ghost caches the templates map — new .hbs files need a restart.</div>'
         '<div class="alert alert-danger"><p class="alert__title">Broken</p>That embed 403s. Replace the fallback video URL.</div>'
         '<div class="alert alert-signal"><p class="alert__title">Live now</p>Streaming the build — the dot is on for a reason.</div>'
         '</div>',
         '<b>.alert + .alert-info/-success/-warning/-danger/-signal</b>')
    + tile('<div class="alert alert-info u-flex u-items-start u-gap-3" style="max-width:36rem"><div class="u-grow">Dismissable — the close button rides the corner.</div><button class="btn-close" type="button" aria-label="Dismiss" onclick="this.closest(\'.alert\').remove()"></button></div>',
           'dismissable — <b>.btn-close</b> inside the alert'))

PAGES['badge'] = ('Badge',
    'A word in a shape. Tones for status, live for the dot, chips when it\'s interactive.',
    tile('<div class="cluster-sm">'
         '<span class="badge">Default</span><span class="badge badge-signal">Signal</span>'
         '<span class="badge badge-craft">Craft</span><span class="badge badge-success">Shipped</span>'
         '<span class="badge badge-warning">In progress</span><span class="badge badge-danger">Blocked</span>'
         '<span class="badge badge-info">Note</span><span class="badge badge-inverse">Inverse</span>'
         '<span class="badge badge-live">Live</span>'
         '</div>',
         '<b>.badge + tones</b> · <b>.badge-live</b> carries the pulsing dot')
    + tile('<div class="cluster-sm">'
           '<span class="chip">travel <span class="chip__count">12</span></span>'
           '<span class="chip" aria-pressed="true">salesforce <span class="chip__count">31</span></span>'
           '<span class="chip">ghost-theme <button class="chip__x" aria-label="Remove filter">×</button></span>'
           '<span class="timecode">00:14:22</span><kbd class="kbd">⌘K</kbd>'
           '</div>',
           '<b>.chip (+__count/__x)</b> — filters · <b>.timecode · .kbd</b> — the slate family'))

PAGES['breadcrumb'] = ('Breadcrumb',
    'The trail back up. Slate voice, real nav element, current page unlinked.',
    tile('<nav class="breadcrumb" aria-label="Breadcrumb"><ol>'
         '<li><a href="#i">Home</a></li><li><a href="#i">Courses</a></li>'
         '<li><a href="#i">Handlebars without tears</a></li><li aria-current="page">Lesson 3</li>'
         '</ol></nav>',
         '<b>.breadcrumb</b> — ol in a nav, aria-current on the leaf'))

btn_body = (
    tile('<div class="cluster-sm">'
         '<button class="btn btn-primary">Primary</button><button class="btn btn-secondary">Secondary</button>'
         '<button class="btn btn-ghost">Ghost</button><button class="btn btn-soft">Soft</button>'
         '<button class="btn btn-quiet">Quiet</button><button class="btn btn-danger">Danger</button>'
         '</div>',
         '<b>six intents</b> — one primary per surface')
    + tile('<div class="cluster-sm u-items-center">'
           '<button class="btn btn-primary btn-sm">Small</button>'
           '<button class="btn btn-primary">Medium</button>'
           '<button class="btn btn-primary btn-lg">Large</button>'
           '<button class="btn btn-secondary btn-pill">Pill</button>'
           '<button class="btn btn-live">Go live</button>'
           '</div>',
           '<b>.btn-sm / (default) / .btn-lg · .btn-pill · .btn-live</b>')
    + tile('<div class="cluster-sm u-items-center">'
           '<button class="btn btn-primary"><svg class="icon btn__icon" aria-hidden="true"><use href="#i-play"/></svg> Watch now</button>'
           '<button class="btn btn-secondary">Next lesson <svg class="icon btn__icon" aria-hidden="true"><use href="#i-arrow"/></svg></button>'
           '<button class="btn btn-secondary btn-icon" aria-label="Search"><svg class="icon" aria-hidden="true"><use href="#i-search"/></svg></button>'
           '<button class="btn btn-ghost btn-icon" aria-label="Email"><svg class="icon" aria-hidden="true"><use href="#i-mail"/></svg></button>'
           '<button class="btn btn-primary btn-icon btn-sm" aria-label="Play"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg></button>'
           '</div>',
           '<b>icon variants</b> — leading, trailing, and .btn-icon squares (always aria-label)')
    + tile('<div class="cluster-sm u-items-center">'
           '<button class="btn btn-primary" data-loading>Publishing…</button>'
           '<button class="btn btn-primary" disabled>Disabled</button>'
           '<button class="btn btn-secondary" aria-pressed="true">Pressed</button>'
           '</div>'
           '<div class="u-mt-4"><button class="btn btn-primary btn-block">Block — full width</button></div>',
           '<b>[data-loading] · [disabled] · [aria-pressed] · .btn-block</b>'))

PAGES['buttons'] = ('Buttons',
    'Six intents, three sizes, icons leading/trailing/alone, and every state. '
    'The intent picks itself: primary is the one thing the screen is for.',
    btn_body)

PAGES['button-group'] = ('Button group',
    'Segmented choices. One group, one pressed member, driven by aria-pressed.',
    tile('<div class="btn-group" role="group" aria-label="View">'
         '<button class="btn" aria-pressed="true">Grid</button>'
         '<button class="btn" aria-pressed="false">List</button>'
         '<button class="btn" aria-pressed="false">Timeline</button>'
         '</div>',
         '<b>.btn-group</b> — click to move the pressed state (wired in preview.js)')
    + tile('<div class="btn-group" role="group" aria-label="Speed">'
           '<button class="btn btn-sm" aria-pressed="false">0.5×</button>'
           '<button class="btn btn-sm" aria-pressed="true">1×</button>'
           '<button class="btn btn-sm" aria-pressed="false">1.5×</button>'
           '<button class="btn btn-sm" aria-pressed="false">2×</button>'
           '</div>',
           'sizes compose — <b>.btn-sm</b> inside a group'))

PAGES['card'] = ('Card',
    'The workhorse. Media, body, meta, footer — designed at thumbnail scale first so the title survives a 120px crop.',
    tile('<div class="deck deck-sm" style="grid-template-columns:repeat(auto-fill,minmax(14rem,1fr))">'
         '<article class="card"><div class="card__media pattern pattern-grid pattern-media"></div>'
         '<div class="card__body"><p class="card__meta">Blog · Jul 20</p>'
         '<h3 class="card__title"><a class="card__link" href="#i">The default card, complete</a></h3>'
         '<p class="card__excerpt">Media on top, meta whispering, title carrying, excerpt optional.</p>'
         '<p class="card__footer">4 min read</p></div></article>'
         '<article class="card card-featured"><div class="card__media pattern pattern-hatch pattern-media"></div>'
         '<div class="card__body"><p class="card__meta">Featured</p>'
         '<h3 class="card__title"><a class="card__link" href="#i">Featured — accent edge</a></h3></div></article>'
         '<article class="card card-inverse"><div class="card__body"><p class="card__meta">Series</p>'
         '<h3 class="card__title"><a class="card__link" href="#i">Inverse — cinema surface</a></h3></div></article>'
         '</div>',
         '<b>.card (+ __media/__body/__meta/__title/__excerpt/__footer)</b> · <b>.card-featured · .card-inverse</b>')
    + tile('<article class="card card-row" style="max-width:34rem"><div class="card__media pattern pattern-dots pattern-media"></div>'
           '<div class="card__body"><p class="card__meta">Row layout</p>'
           '<h3 class="card__title"><a class="card__link" href="#i">Horizontal card for lists</a></h3>'
           '<p class="card__excerpt">Media left, copy right; stacks on phones.</p></div></article>',
           '<b>.card-row</b> · also: <b>.card-compact · .card-poster · .card-bare</b>')
    + tile('<div class="deck deck-sm" style="grid-template-columns:repeat(auto-fill,minmax(11rem,1fr))">'
           '<article class="card card-poster"><div class="card__media card__media-poster pattern pattern-scanline pattern-media"></div>'
           '<div class="card__body"><h3 class="card__title"><a class="card__link" href="#i">Poster 2:3</a></h3></div></article>'
           '<article class="card card-compact"><div class="card__body"><p class="card__meta">Compact</p>'
           '<h3 class="card__title"><a class="card__link" href="#i">Dense rails</a></h3></div></article>'
           '<article class="card card-bare"><div class="card__media pattern pattern-grid pattern-media"></div>'
           '<div class="card__body" style="padding-inline:0"><h3 class="card__title"><a class="card__link" href="#i">Bare — no chrome</a></h3></div></article>'
           '</div>',
           'the whole-card link stays on the title; its ::after covers the card'))

PAGES['carousel'] = ('Carousel',
    'A scroll-snap rail — no JS engine, no stolen wheel. Vertical scrolling always keeps scrolling the page.',
    tile('<div class="carousel"><div class="carousel__track">'
         + ''.join(f'<article class="card carousel__slide"><div class="card__media pattern pattern-{p} pattern-media"></div>'
                   f'<div class="card__body"><p class="card__meta">Ep.0{i}</p><h3 class="card__title"><a class="card__link" href="#i">Slide {i}</a></h3></div></article>'
                   for i, p in enumerate(['grid', 'hatch', 'dots', 'scanline', 'grid'], 1))
         + '</div><div class="carousel__nav">'
           '<button class="carousel__dot" aria-current="true" aria-label="Page 1"></button>'
           '<button class="carousel__dot" aria-label="Page 2"></button>'
           '<button class="carousel__dot" aria-label="Page 3"></button>'
         '</div></div>',
         '<b>.carousel &gt; __track &gt; __slide</b> — snap-x · <b>__nav/__dot</b> page dots')
    + ct([('.carousel-full', 'one slide per view — billboards'),
          ('touch-action: pan-x pan-y', 'the scroll-trap fix, baked in'),
          ('scroll-snap-align: start', 'slides land on the container edge')]))

PAGES['close-button'] = ('Close button',
    'One dismiss affordance everywhere: two strokes, a hover wash, an accessible name.',
    tile('<div class="cluster u-items-center">'
         '<button class="btn-close" type="button" aria-label="Close"></button>'
         '<span class="u-bg-inverse u-rounded u-p-3 u-inline-flex"><button class="btn-close btn-close-inverse" type="button" aria-label="Close"></button></span>'
         '</div>',
         '<b>.btn-close · .btn-close-inverse</b> — always with aria-label'))

PAGES['collapse'] = ('Collapse',
    'One panel that opens. Native &lt;details&gt;: keyboard, AT and find-in-page work with zero JS.',
    tile('<details class="collapse" style="max-width:34rem"><summary>What gear shot this course?</summary>'
         '<div class="collapse__body">One camera, one lamp, the phone as a b-cam. The list is shorter than the thumbnail implies.</div></details>',
         '<b>.collapse &gt; summary + .collapse__body</b>')
    + tile('<details class="collapse" open style="max-width:34rem"><summary>Open by default</summary>'
           '<div class="collapse__body">Add the <code class="t-code">open</code> attribute server-side — state in HTML, not in a script.</div></details>',
           '<b>[open]</b> — the chevron folds'))

PAGES['dropdowns'] = ('Dropdowns',
    'A &lt;details&gt; wearing a menu. Light-dismiss via the platform, items are real links.',
    tile('<div class="u-flex u-gap-4 u-wrap" style="min-height:16rem">'
         '<details class="dropdown"><summary class="btn btn-secondary">Collections</summary>'
         '<div class="dropdown__menu">'
         '<span class="dropdown__head">Watch</span>'
         '<a class="dropdown__item" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-camera"/></svg> Videos</a>'
         '<a class="dropdown__item" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg> Web series</a>'
         '<hr class="dropdown__divider" />'
         '<span class="dropdown__head">Read</span>'
         '<a class="dropdown__item" href="#i" aria-current="true"><svg class="icon" aria-hidden="true"><use href="#i-pen"/></svg> Blog</a>'
         '<a class="dropdown__item" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-book"/></svg> Docs</a>'
         '</div></details>'
         '<details class="dropdown dropdown-end"><summary class="btn btn-ghost">Sort ▾-less</summary>'
         '<div class="dropdown__menu">'
         '<a class="dropdown__item" href="#i">Newest first</a>'
         '<a class="dropdown__item" href="#i">Longest first</a>'
         '<a class="dropdown__item" href="#i">A → Z</a>'
         '</div></details>'
         '</div>',
         '<b>.dropdown &gt; summary.btn + .dropdown__menu</b> · <b>__item / __head / __divider</b> · <b>.dropdown-end</b> right-aligns'))

PAGES['list-group'] = ('List group',
    'Rows in one surface. Links, buttons or static; the current row gets the accent inset.',
    tile('<div class="list-group" style="max-width:26rem" role="list">'
         '<a class="list-group__item" href="#i" aria-current="true">Foundation <span class="badge">13 files</span></a>'
         '<a class="list-group__item" href="#i">Elements <span class="badge">5</span></a>'
         '<a class="list-group__item" href="#i">Components <span class="badge">11</span></a>'
         '<span class="list-group__item" aria-disabled="true">Broadcast (locked)</span>'
         '</div>',
         '<b>.list-group &gt; __item</b> — aria-current inset · badges ride the right edge')
    + tile('<div class="list-group list-group-flush" style="max-width:26rem">'
           '<span class="list-group__item">Flush — no outer chrome</span>'
           '<span class="list-group__item">For rails and card bodies</span>'
           '</div>',
           '<b>.list-group-flush</b>'))

PAGES['marquee'] = ('Marquee',
    'The looping strip, done honestly: duplicate the run, hide the twin from assistive tech, '
    'pause on hover, fall back to a scrollable row under reduced motion.',
    tile('<div class="marquee"><div class="marquee__run">'
         '<span class="t-slate">#salesforce</span><span class="t-slate">#ghost-theme</span>'
         '<span class="t-slate">#budapest</span><span class="t-slate">#build-log</span>'
         '<span class="t-slate">#travel</span><span class="t-slate">#courses</span>'
         '</div><div class="marquee__run" aria-hidden="true">'
         '<span class="t-slate">#salesforce</span><span class="t-slate">#ghost-theme</span>'
         '<span class="t-slate">#budapest</span><span class="t-slate">#build-log</span>'
         '<span class="t-slate">#travel</span><span class="t-slate">#courses</span>'
         '</div></div>',
         '<b>.marquee &gt; .marquee__run ×2</b> — the twin is aria-hidden')
    + tile('<div class="marquee marquee-fast marquee-reverse"><div class="marquee__run">'
           '<span class="badge">EP.01</span><span class="badge">EP.02</span><span class="badge">EP.03</span>'
           '<span class="badge">EP.04</span><span class="badge">EP.05</span><span class="badge">EP.06</span>'
           '</div><div class="marquee__run" aria-hidden="true">'
           '<span class="badge">EP.01</span><span class="badge">EP.02</span><span class="badge">EP.03</span>'
           '<span class="badge">EP.04</span><span class="badge">EP.05</span><span class="badge">EP.06</span>'
           '</div></div>',
           '<b>.marquee-fast / -slow / -reverse</b> · hover pauses'))

PAGES['modal'] = ('Modal',
    'A real &lt;dialog&gt;. showModal() traps focus, ESC closes, ::backdrop scrims — the platform does the hard parts.',
    tile('<button class="btn btn-primary" type="button" data-dialog="demo-modal">Open modal</button>'
         '<dialog class="modal" id="demo-modal">'
         '<div class="modal__head"><h2 class="modal__title">Delete this take?</h2>'
         '<button class="btn-close" type="button" data-dialog-close aria-label="Close"></button></div>'
         '<div class="modal__body">Take 47 goes to the trash. The film survives; the blooper reel mourns.</div>'
         '<div class="modal__foot"><button class="btn btn-quiet" type="button" data-dialog-close>Keep it</button>'
         '<button class="btn btn-danger" type="button" data-dialog-close>Delete take</button></div>'
         '</dialog>',
         '<b>dialog.modal</b> — __head / __body / __foot · opened by <b>[data-dialog]</b>, closed by <b>[data-dialog-close]</b> or ESC')
    + tile('<button class="btn btn-secondary" type="button" data-dialog="demo-modal-lg">Open large modal</button>'
           '<dialog class="modal modal-lg" id="demo-modal-lg">'
           '<div class="modal__head"><h2 class="modal__title">Season two, planned</h2>'
           '<button class="btn-close" type="button" data-dialog-close aria-label="Close"></button></div>'
           '<div class="modal__body">The wide variant for forms and pickers. Width caps at 44rem; on phones both sizes meet the same gutters.</div>'
           '<div class="modal__foot"><button class="btn btn-primary" type="button" data-dialog-close>Sounds right</button></div>'
           '</dialog>',
           '<b>.modal-lg</b>'))

PAGES['navbar'] = ('Navbar',
    'The island, in every mode the theme ships: default, blog (current page marked), '
    'course player, and the series bar that is always cinema-dark.',
    tile('<header class="nav-shell" style="position:static"><nav class="nav-bar" aria-label="Demo default">'
         '<span class="logo logo-sm">Swarn<span class="logo__i">ı<i class="logo__tittle"></i></span>l</span>'
         '<div class="nav-links">'
         '<a class="nav-link" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-pen"/></svg>Blog</a>'
         '<a class="nav-link" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-camera"/></svg>Videos</a>'
         '<a class="nav-link" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-code"/></svg>Projects</a>'
         '<a class="nav-link" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-book"/></svg>Courses</a>'
         '</div>'
         '<div class="cluster-sm"><button class="btn btn-primary btn-sm btn-pill">Subscribe</button></div>'
         '</nav></header>',
         '<b>.nav-shell &gt; .nav-bar</b> — the default island, iconified links', pad=False)
    + tile('<header class="nav-shell" style="position:static"><nav class="nav-bar" aria-label="Demo blog">'
           '<span class="logo logo-sm">Swarn<span class="logo__i">ı<i class="logo__tittle"></i></span>l</span>'
           '<div class="nav-links">'
           '<a class="nav-link" href="#i" aria-current="page"><svg class="icon" aria-hidden="true"><use href="#i-pen"/></svg>Blog</a>'
           '<a class="nav-link" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-camera"/></svg>Videos</a>'
           '<a class="nav-link" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-plane"/></svg>Travel</a>'
           '</div>'
           '<div class="cluster-sm"><button class="btn btn-secondary btn-sm btn-icon" aria-label="Search"><svg class="icon" aria-hidden="true"><use href="#i-search"/></svg></button></div>'
           '</nav></header>',
           'collection context — <b>[aria-current="page"]</b> gets the dot, not a fill', pad=False)
    + tile('<nav class="nav-bar nav-course" aria-label="Demo course" style="border:var(--border-hair) solid var(--line-default);border-radius:var(--radius-pill)">'
           '<button class="btn-close" type="button" aria-label="Close course"></button>'
           '<span class="t-slate-sm u-grow u-text-center">HANDLEBARS WITHOUT TEARS · LESSON 3 OF 14</span>'
           '<div class="cluster-sm">'
           '<button class="btn btn-quiet btn-sm">← Prev</button><button class="btn btn-primary btn-sm">Next →</button>'
           '</div>'
           '<span class="nav-rail" style="--value:21%"></span>'
           '</nav>',
           '<b>.nav-course</b> — player chrome: ✕ close, position slate, pager, progress rail on the bottom edge', pad=False)
    + tile('<nav class="nav-bar nav-series" aria-label="Demo series" style="border-radius:var(--radius-pill)">'
           '<span class="logo logo-sm" style="color:#fff">S<span class="logo__i">ı</span>l</span>'
           '<div class="nav-links">'
           '<a class="nav-link" href="#i">Episodes</a>'
           '<a class="nav-link" href="#i" aria-current="page">S02</a>'
           '<a class="nav-link" href="#i">About</a>'
           '</div>'
           '<div class="cluster-sm"><span class="badge badge-live">Live</span>'
           '<button class="btn-close btn-close-inverse" type="button" aria-label="Exit series"></button></div>'
           '</nav>',
           '<b>.nav-series</b> — always ink, ignores the theme: it is cinema', pad=False))

PAGES['navs-tabs'] = ('Navs & tabs',
    'Tabs for peer views, driven by aria-selected. The underline is the state; the panel is yours.',
    tile('<div class="tabs" role="tablist" aria-label="Course views">'
         '<button class="tab" role="tab" aria-selected="true">Curriculum</button>'
         '<button class="tab" role="tab" aria-selected="false">Reviews</button>'
         '<button class="tab" role="tab" aria-selected="false">Gear</button>'
         '<button class="tab" role="tab" aria-selected="false" disabled>Certificates</button>'
         '</div>',
         '<b>.tabs &gt; .tab[role=tab]</b> — click moves aria-selected (preview.js)')
    + tile('<nav class="pagination" aria-label="Vertical nav demo" style="display:block;max-width:16rem">'
           '<div class="list-group list-group-flush">'
           '<a class="list-group__item" href="#i" aria-current="true">Overview</a>'
           '<a class="list-group__item" href="#i">Syllabus</a>'
           '<a class="list-group__item" href="#i">Instructor</a>'
           '</div></nav>',
           'vertical nav = <b>.list-group-flush</b> with aria-current — no separate component'))

PAGES['offcanvas'] = ('Offcanvas',
    'A drawer that is also a &lt;dialog&gt; — same focus trap, same ESC, docked to an edge.',
    tile('<div class="cluster-sm">'
         '<button class="btn btn-secondary" type="button" data-dialog="demo-off-end">Open right drawer</button>'
         '<button class="btn btn-quiet" type="button" data-dialog="demo-off-start">Open left drawer</button>'
         '</div>'
         '<dialog class="offcanvas" id="demo-off-end">'
         '<div class="offcanvas__head"><span class="offcanvas__title">Episode list</span>'
         '<button class="btn-close" type="button" data-dialog-close aria-label="Close"></button></div>'
         '<div class="offcanvas__body stack-sm">'
         '<a class="episode" href="#i" aria-current="true"><span class="episode__thumb pattern pattern-grid pattern-media"></span><span><span class="episode__title">Rebuilding from tokens</span><span class="episode__meta">Ep.07 · 14:22</span></span></a>'
         '<a class="episode" href="#i"><span class="episode__thumb pattern pattern-hatch pattern-media"></span><span><span class="episode__title">One query, six hours</span><span class="episode__meta">Ep.06 · 09:41</span></span></a>'
         '</div></dialog>'
         '<dialog class="offcanvas offcanvas-start" id="demo-off-start">'
         '<div class="offcanvas__head"><span class="offcanvas__title">Filters</span>'
         '<button class="btn-close" type="button" data-dialog-close aria-label="Close"></button></div>'
         '<div class="offcanvas__body stack-sm">'
         '<label class="check"><input type="checkbox" checked /> <span>Videos</span></label>'
         '<label class="check"><input type="checkbox" /> <span>Courses</span></label>'
         '<label class="check"><input type="checkbox" /> <span>Travel</span></label>'
         '</div></dialog>',
         '<b>dialog.offcanvas (+ -start)</b> — slides from the edge, scrim included'))

PAGES['pagination'] = ('Pagination',
    'Two shapes: numbered pages for archives, the prev/next pager for sequences (it also ends every docs page).',
    tile('<nav class="pagination" aria-label="Pages"><a class="btn btn-quiet btn-sm" href="#i">← Newer</a>'
         '<span class="pagination__pages">'
         '<a class="page-dot" href="#i">1</a><a class="page-dot" href="#i" aria-current="page">2</a>'
         '<a class="page-dot" href="#i">3</a><span class="page-dot" aria-hidden="true">…</span><a class="page-dot" href="#i">12</a>'
         '</span><a class="btn btn-quiet btn-sm" href="#i">Older →</a></nav>',
         '<b>.pagination · .page-dot</b> — numbered, aria-current on the page you\'re on')
    + tile('<nav class="pager" aria-label="Lessons"><a class="pager__item" href="#i">'
           '<span class="pager__dir">← Previous</span><span class="pager__title">The ink ladder</span></a>'
           '<a class="pager__item pager__item-next" href="#i">'
           '<span class="pager__dir">Next →</span><span class="pager__title">Spacing is a ladder</span></a></nav>',
           '<b>.pager &gt; .pager__item (+ -next)</b> — the sequence shape'))

PAGES['popovers'] = ('Popovers',
    'The Popover API: light-dismiss, top layer and toggling come from the platform. '
    'CSS Anchor positioning places them when supported.',
    tile('<button class="btn btn-secondary" popovertarget="demo-pop" style="anchor-name:--pop-a">What counts as live?</button>'
         '<div class="pop" id="demo-pop" popover style="position-anchor:--pop-a;top:anchor(bottom);left:anchor(left);margin-top:8px">'
         '<p class="pop__head">The signal dot</p>'
         '<p class="pop__body">Live means happening now — a stream, a current lesson, an active build. One dot per surface, never decoration.</p>'
         '</div>',
         '<b>[popover] + .pop</b> — click outside or ESC dismisses; anchored where supported')
    + ct([('popovertarget="id"', 'the trigger, no JS'),
          ('.pop__head / .pop__body', 'title strip + prose'),
          ('.tip (tooltips page)', 'for one-liners — a popover earns its title')]))

PAGES['progress'] = ('Progress',
    'Determinate fills, thin rails, labels, and the honest indeterminate scan.',
    tile('<div class="stack" style="max-width:28rem">'
         '<div class="progress" style="--value:65%"><span class="progress__bar"></span></div>'
         '<div class="progress progress-thin" style="--value:30%"><span class="progress__bar"></span></div>'
         '<div class="progress progress-labelled" style="--value:80%"><span class="progress__bar"></span><span class="progress__label">12 of 15 lessons</span></div>'
         '<div class="progress progress-indeterminate"><span class="progress__bar"></span></div>'
         '</div>',
         '<b>.progress (+ -thin / -labelled / -indeterminate)</b> — --value drives the fill'))

PAGES['scrollspy'] = ('Scrollspy',
    'The sidebar\'s “on this page” links highlight as sections pass — an IntersectionObserver in preview.js, '
    'not a scroll handler. This page spies on itself.',
    sec('spy-how', 'How it works',
        'Links matching <code class="t-code">.doc-side__nav a[href^="#"]</code> map to their sections; the observer\'s '
        'rootMargin (-10% top, -70% bottom) makes the “current” band the upper third of the viewport.')
    + tile('''<figure class="codebox codebox-light u-m-0"><figcaption class="codebox__head"><span class="codebox__lang">js</span><button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>
<pre class="codebox__pre"><code><span class="ln"><span class="tok-key">new</span> <span class="tok-fn">IntersectionObserver</span>(mark, {</span><span class="ln">  rootMargin: <span class="tok-str">'-10% 0px -70% 0px'</span></span><span class="ln">}).<span class="tok-fn">observe</span>(section)</span></code></pre></figure>''',
           'the whole engine — no scroll listener, no jank')
    + END
    + sec('spy-a', 'Watch the sidebar', 'Scroll this page: “How it works”, this section and the next trade the highlight.')
    + tile('<div class="pattern pattern-grid u-border u-rounded-lg" style="height:14rem"></div>', 'filler section A')
    + END
    + sec('spy-b', 'Section B', '')
    + tile('<div class="pattern pattern-dots u-border u-rounded-lg" style="height:14rem"></div>', 'filler section B')
    + END)

PAGES['spinners'] = ('Spinners',
    'Waiting has grades: the spinner for a moment, the scan for a region, the skeleton for a layout.',
    tile('<div class="cluster u-items-center">'
         '<span class="spinner" role="status" aria-label="Loading"></span>'
         '<button class="btn btn-primary" data-loading>Publishing…</button>'
         '<span class="loading-scan" style="width:10rem"></span>'
         '</div>',
         '<b>.spinner · [data-loading] · .loading-scan</b>')
    + tile('<div class="u-flex u-gap-3 u-items-center" style="max-width:24rem">'
           '<span class="skeleton skeleton-avatar"></span>'
           '<span class="u-grow stack-sm"><span class="skeleton skeleton-title"></span><span class="skeleton skeleton-text"></span></span>'
           '</div><div class="skeleton skeleton-media u-mt-4" style="max-width:24rem"></div>',
           '<b>.skeleton (+ -avatar/-title/-text/-media)</b> — shaped like the truth'))

PAGES['toasts'] = ('Toasts',
    'Transient confirmations in a fixed region. Polite by default; they never cover the thing you acted on.',
    tile('<div class="stack-sm" style="max-width:22rem">'
         '<div class="toast" role="status">Link copied to clipboard.</div>'
         '<div class="toast" role="status"><span class="dot dot-sm dot-live"></span> Going live in 10 seconds…'
         '<button class="btn-close u-ms-auto" type="button" aria-label="Dismiss"></button></div>'
         '</div>',
         '<b>.toast</b> — shown here inline; production mounts them in <b>.toast-region</b> (fixed, bottom-right)'))

PAGES['tooltips'] = ('Tooltips',
    'One line on hover/focus, CSS only, from data-tip. Anything longer is a popover.',
    tile('<div class="cluster u-items-center">'
         '<span class="tip doc-btn" tabindex="0" data-tip="Runtime 14:22">Hover or focus me</span>'
         '<span class="tip doc-btn" tabindex="0" data-tip="Published Jul 19, 2026">Another</span>'
         '<button class="tip btn btn-secondary btn-icon" data-tip="Search everything" aria-label="Search"><svg class="icon" aria-hidden="true"><use href="#i-search"/></svg></button>'
         '</div>',
         '<b>.tip[data-tip]</b> — keyboard focus shows it too; never put the only copy of anything in one'))

# ── Ads ───────────────────────────────────────────────────────────────────

def _ad(size, w, h, extra_cls=''):
    return (f'<div class="ad {size} {extra_cls}" data-ad>'
            f'<button class="ad__hide btn-close" type="button" data-ad-hide aria-label="Hide this ad"></button>'
            f'<div class="ad__skeleton skeleton skeleton-breathe" aria-hidden="true"></div>'
            f'<div class="ad__slot"><span class="ad__cta">Your ad here</span>'
            f'<span class="ad__dims">{w} × {h}</span></div></div>')

PAGES['ads'] = ('Ads',
    'Placeholder ad units that behave like real ones: a skeleton until a slot is actually on screen, '
    'a lazy load that waits for that, and a hide switch that belongs to the reader.',
    ('<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
     'Every slot below starts as <code class="t-code">.skeleton.skeleton-breathe</code> — the same '
     'shimmer this system already uses for unknown-shape content — then swaps to its placeholder '
     'creative once <code class="t-code">src/ad.js</code> decides it has "loaded". Nothing here calls '
     'a real ad network; the point is the mechanism, not the inventory.</p>'
     + sec('sizes', 'Sizes', 'IAB standard units, each capped by max-width so a desktop leaderboard '
           'still fits a phone rather than overflowing it.')
     + tile(_ad('ad-leaderboard', 728, 90), '<b>.ad-leaderboard</b> — 728 × 90')
     + tile(_ad('ad-rectangle', 300, 250), '<b>.ad-rectangle</b> — 300 × 250, the most-served unit on the web')
     + tile('<div class="cluster u-items-start u-gap-6">' + _ad('ad-skyscraper', 160, 600)
            + _ad('ad-mobile-banner', 320, 50) + '</div>',
            '<b>.ad-skyscraper</b> (160 × 600) and <b>.ad-mobile-banner</b> (320 × 50)')
     + tile(_ad('ad-responsive', 'fluid', 'auto'),
            '<b>.ad-responsive</b> — full width, a floor height, no fixed ratio')
     + sec('animate', 'Animate on load', 'The .ad-animate variant rises the creative in rather than '
           'just cross-fading it — the same fx-rise every card entrance already uses, not a new keyframe.')
     + tile(_ad('ad-rectangle', 300, 250, 'ad-animate'), '<b>.ad-animate</b> — refresh the page to see it fire')
     + sec('mechanism', 'Lazy load, skeleton, and the hide switch', '')
     + ct([
         ('data-ad', 'marks a slot for src/ad.js to manage — nothing renders without it'),
         ('data-ad-state', '"idle" → "loading" → "loaded", or "hidden" — the only thing the script writes'),
         ('IntersectionObserver', 'a slot only starts "loading" once it is within 200px of the viewport'),
         ('data-ad-hide', 'on the close button — sets data-ad-state="hidden", the slot collapses out of layout'),
         ('No IntersectionObserver support', 'every slot loads immediately — a slower reveal, never a missing ad'),
     ], head=('Hook', 'Does'))
     + '<p class="u-fg-subtle u-mt-6" style="max-width:var(--measure-lead)">'
       '<code class="t-code">.ad-animate</code> rise is skipped entirely under '
       '<code class="t-code">prefers-reduced-motion</code> — the creative still appears, it just stops '
       'moving, the same rule every other entrance in this system follows.</p>'))
