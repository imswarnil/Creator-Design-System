"""The shared page shell every collection builds on.

A collection's own build.py brings its data and its sections; this brings the
head, the navbar, the footer and the small helpers all of them need. Without
it, each new collection starts by copying eighty lines of <head> from the last
one, and they drift apart from the first edit.
"""
import html
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
REL = '../..'          # from collection/<name>/*.html back to the repo root


def icon(name, cls='icon', group='travel'):
    """Inline an icon file so it inherits currentColor."""
    for g in (group, 'ui', 'creator', 'media', 'social', 'resume'):
        p = REPO / 'icons' / g / f'{name}.svg'
        if p.exists():
            return p.read_text().strip().replace(
                '<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1)
    return ''


def ph(seed='default', tall=False, blend=False):
    """A placeholder that cannot 404.

    Deliberately not a photograph: a demo that ships with stock photography
    teaches that the design needs a good photograph to work. Each seed gets its
    own hue off one ladder, so a grid still reads as a set.

    `blend=True` layers a second, offset hue over the first via
    `mix-blend-mode` (see `collection/guides/guides.css`) — a book cover
    wants two colours meeting, not one flat tile.
    """
    hues = {'japan': 8, 'vietnam': 150, 'portugal': 205, 'georgia': 265,
            'peru': 32, 'india': 340, 'css': 262, 'motion': 190, 'craft': 24,
            'notes': 96, 'default': 220}
    # An unnamed seed still gets a stable hue rather than falling back to the
    # one default — otherwise a collection with a dozen slugs is a dozen
    # identical rectangles, which reads as a loading state.
    h = hues.get(seed) if seed in hues else sum(map(ord, seed)) * 37 % 360
    return (f'<span class="col-ph" style="--h:{h}"'
            f'{" data-tall" if tall else ""}{" data-blend" if blend else ""}'
            f' aria-hidden="true"></span>')


HEAD = '''<!doctype html>
<html lang="en" data-theme="light"{transition_attr}>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="icon" href="{rel}/docs/favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="{rel}/dist/creator.css" />
<link rel="stylesheet" href="{rel}/collection/collection.css" />{own_css}
<script src="{rel}/src/nav.js" defer></script>
<script src="{rel}/collection/collection.js" defer></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="nav-shell">
  <nav class="nav-bar" aria-label="Main">
    <a class="logo logo-sm" href="{rel}/collection/_pages/home.html">Swarnil</a>
    <div class="nav-links">
      <a class="nav-link" href="{rel}/collection/course/index.html"{cur_course}>Courses</a>
      <a class="nav-link" href="{rel}/collection/travel/index.html"{cur_travel}>Travel</a>
      <a class="nav-link" href="{rel}/collection/blog/index.html"{cur_blog}>Blog</a>
      <a class="nav-link" href="{rel}/collection/webseries/index.html"{cur_webseries}>Series</a>
      <a class="nav-link" href="{rel}/collection/newsletter/index.html"{cur_newsletter}>Newsletter</a>
      <a class="nav-link" href="{rel}/collection/projects/index.html"{cur_projects}>Projects</a>
      <a class="nav-link" href="{rel}/collection/_pages/resume.html"{cur_resume}>Résumé</a>
    </div>
    <div class="nav-actions">
      <a class="btn btn-primary btn-sm btn-pill" href="#i">Subscribe</a>
    </div>
  </nav>
</header>

<main id="main">
'''

FOOT = '''
</main>

<footer class="section-sm">
  <div class="container">
    <hr class="rule u-mb-6" />
    <div class="row-between">
      <p class="t-slate">{name} — a collection</p>
      <p class="t-slate-sm"><a href="{rel}/collection/README.md">Built from the collection contract</a></p>
    </div>
  </div>
</footer>
</body>
</html>
'''


# Which page-transition flavour (src/1-foundation/05-motion.css) a collection
# arrives with — set once here rather than per route, since every route of a
# collection is the same destination "medium".
TRANSITIONS = {
    'travel': 'takeoff',
    'course': 'pop',
    'resume': 'unfold',
    'blog': 'type',
    'webseries': 'slate',
    'newsletter': 'envelope',
    'projects': 'terminal',
    'videos': 'static',
    'guides': 'turn',
}


def page(out_dir, name, title, desc, body, collection='', own_css=None, current=''):
    """Write one route. `own_css` is the collection's own stylesheet, if it has
    one — most do not need any."""
    css = f'\n<link rel="stylesheet" href="./{own_css}" />' if own_css else ''
    transition = TRANSITIONS.get(current, '')
    doc = (HEAD.format(title=html.escape(title), desc=html.escape(desc), rel=REL,
                       own_css=css,
                       transition_attr=f' data-transition="{transition}"' if transition else '',
                       cur_travel=' aria-current="page"' if current == 'travel' else '',
                       cur_blog=' aria-current="page"' if current == 'blog' else '',
                       cur_course=' aria-current="page"' if current == 'course' else '',
                       cur_resume=' aria-current="page"' if current == 'resume' else '',
                       cur_webseries=' aria-current="page"' if current == 'webseries' else '',
                       cur_newsletter=' aria-current="page"' if current == 'newsletter' else '',
                       cur_projects=' aria-current="page"' if current == 'projects' else '')
           + body + FOOT.format(rel=REL, name=collection))
    (pathlib.Path(out_dir) / name).write_text(doc)
    return name


def sec(title, note='', extra=''):
    n = (f'<p class="t-subtle u-mt-2" style="max-width:var(--measure-lead)">{note}</p>'
         if note else '')
    return (f'<div class="row-between u-mb-5"><div><h2 class="t-h3">{title}</h2>{n}</div>'
            f'{extra}</div>')


def meta_strip(pairs, paper=False, border=True, inline=False):
    cls = 'col-meta'
    if paper:
        cls += ' col-meta-paper'
    if inline:
        cls += ' col-meta-inline'
    style = ' style="border-top:0;padding-top:0"' if not border else ''
    return f'<div class="{cls}"{style}>' + ''.join(
        f'<div><span class="col-meta__n">{n}</span>'
        f'<span class="col-meta__l">{l}</span></div>' for n, l in pairs) + '</div>'


def pagination(page, total, href='./index.html', label='Pages'):
    """.pagination + .page-dot, unchanged — every collection index that lists
    more than it shows on one page reaches for this, not its own version.
    `page` is 1-indexed. Collapses to first/last/neighbours + an ellipsis
    once there are more than 5 pages, so a 40-page archive doesn't print 40
    links into the DOM."""
    def dot(n):
        cur = ' aria-current="page"' if n == page else ''
        return f'<a class="page-dot" href="{href}"{cur}>{n}</a>'

    nums = list(range(1, total + 1))
    if total > 5:
        keep = {1, total, page, page - 1, page + 1}
        shown, prev_n = [], 0
        for n in nums:
            if n in keep and 1 <= n <= total:
                if prev_n and n - prev_n > 1:
                    shown.append('…')
                shown.append(n)
                prev_n = n
        nums = shown
    pages = ''.join(dot(n) if n != '…' else '<span class="page-dot" aria-hidden="true">…</span>'
                    for n in nums)
    prev_dis = ' aria-disabled="true" tabindex="-1"' if page <= 1 else ''
    next_dis = ' aria-disabled="true" tabindex="-1"' if page >= total else ''
    return f'''<nav class="pagination" aria-label="{label}">
      <a class="btn btn-quiet btn-sm" href="{href}"{prev_dis}>← Newer</a>
      <span class="pagination__pages">{pages}</span>
      <a class="btn btn-quiet btn-sm" href="{href}"{next_dis}>Older →</a>
    </nav>'''


def hero(title, lead, eyebrow, meta, art='', search=None, eyebrow_icon='pin',
         full=False, narrow=False, pattern=''):
    """The collection hero. `art` is an optional SVG the collection supplies —
    without one the hero is still a hero, just a quieter one.

    `full=True` pulls it out from under the island nav rather than starting
    below it: edge to edge, no radius (a rounded corner on a bleed is a card
    pretending to be a banner), and pulled up by the nav's own height so the
    floating island reads as sitting ON the hero, not above it.

    `narrow=True` sits the boxed hero in `.container-narrow` instead of the
    full site width — a quieter, smaller card rather than a banner.

    `pattern` adds one or more of the foundation's own background-pattern
    classes (e.g. `'pattern-glow pattern-hairline'`) straight onto `.col-hero`
    — it already has the `position:relative; isolation:isolate` a pattern
    needs, so nothing new is required to carry one. A hairline border in the
    same translucent white `.c-series` already uses for a permanently-dark
    card rides along with it."""
    s = ''
    if search:
        s = f'''
      <form class="col-search" onsubmit="return false">
        <label class="col-search__field">
          <span class="u-sr-only">Search</span>
          {icon('compass')}
          <input type="search" placeholder="{search}" />
        </label>
        <button class="btn btn-primary btn-pill" type="submit">Search</button>
      </form>'''
    if full:
        return f'''
  <section class="col-hero" style="border-radius:0;margin-top:calc(-1 * (var(--nav-h) + var(--space-3) * 2))">
    {art}
    <div class="col-hero__in" style="max-width:var(--w-site);margin-inline:auto;
         padding-top:calc(var(--nav-h) + var(--space-24))">
      <span class="col-hero__eyebrow">{icon(eyebrow_icon)}{eyebrow}</span>
      <h1 class="col-hero__title">{title}</h1>
      <p class="col-hero__lead">{lead}</p>
      {s}
      {meta_strip(meta)}
    </div>
  </section>
'''
    container_cls = 'container-narrow' if narrow else 'container'
    pattern_cls = f' pattern {pattern}' if pattern else ''
    pattern_style = (' style="border:var(--border-hair) solid rgb(255 255 255 / 0.10)"'
                     if pattern else '')
    return f'''
  <section class="{container_cls} u-mt-6">
   <div class="col-hero{pattern_cls}"{pattern_style}>
    {art}
    <div class="col-hero__in">
      <span class="col-hero__eyebrow">{icon(eyebrow_icon)}{eyebrow}</span>
      <h1 class="col-hero__title">{title}</h1>
      <p class="col-hero__lead">{lead}</p>
      {s}
      {meta_strip(meta)}
    </div>
   </div>
  </section>
'''


def page_head(title, lead='', eyebrow='', actions='', small=False):
    """`.page-head` — the quiet heading band a page that is not making a case
    opens with. A hero states; a page head just labels. Defined in
    05-sections/30-header.css and, until now, used by nothing."""
    e = (f'<span class="hero__eyebrow">{eyebrow}</span>' if eyebrow else '')
    l = (f'<p class="t-lead u-mt-3" style="max-width:var(--measure-lead)">{lead}</p>'
         if lead else '')
    a = f'<div class="hero__actions">{actions}</div>' if actions else ''
    cls = 'page-head page-head-sm' if small else 'page-head'
    return f'''
  <header class="{cls}">
    {e}
    <h1 class="t-display-2">{title}</h1>
    {l}
    {a}
  </header>'''


def stats(rows, bare=False, inverse=False):
    """`.stats` — numbers as one surface, not four cards. Each row is
    (value, label) or (value, label, note); a note starting with '+' gets the
    up-trend colour. `bare=True` drops the chrome for use inside a hero."""
    cls = 'stats'
    if bare:
        cls += ' stats-bare'
    if inverse:
        cls += ' stats-inverse'
    cells = ''
    for row in rows:
        value, label = row[0], row[1]
        note = row[2] if len(row) > 2 else ''
        trend = ' data-trend="up"' if note.startswith('+') else ''
        n = f'<span class="stat__note"{trend}>{note}</span>' if note else ''
        cells += (f'<div class="stat"><span class="stat__label">{label}</span>'
                  f'<span class="stat__value">{value}</span>{n}</div>')
    return f'<div class="{cls}">{cells}</div>'


def cta(title, body='', kicker='', actions='', fine='', left=False,
        newsletter=False, pattern=''):
    """`.cta` — the ask. One per page, near the end, and it earns its contrast
    by being the only inverse band in view.

    `newsletter=True` swaps the actions for the email form; `left=True` is the
    column-layout variant. `pattern` takes a foundation background-pattern
    class, which the band already has the `position:relative` to carry."""
    cls = 'cta' + (' cta-left' if left else '')
    if pattern:
        cls += f' pattern {pattern}'
    k = f'<span class="cta__kicker">{kicker}</span>' if kicker else ''
    b = f'<p class="cta__body">{body}</p>' if body else ''
    f = f'<p class="cta__fine">{fine}</p>' if fine else ''
    if newsletter:
        act = ('<form class="cta-newsletter__form" onsubmit="return false">'
               '<label class="u-sr-only" for="cta-email">Email</label>'
               '<input class="input" id="cta-email" type="email" '
               'placeholder="you@example.com" autocomplete="email" />'
               '<button class="btn btn-primary" type="submit">Subscribe</button></form>')
    else:
        act = f'<div class="cta__actions">{actions}</div>' if actions else ''
    return f'''
  <section class="{cls}">
    {k}
    <h2 class="cta__title">{title}</h2>
    {b}
    {act}
    {f}
  </section>'''


def cta_sponsor(title, kicker='', actions=''):
    """The quiet one — bordered, on the paper, not inverse. Money asks
    politely, so this is the only CTA shape that does not take the contrast."""
    k = f'<span class="cta__kicker">{kicker}</span>' if kicker else ''
    return f'''
  <section class="cta-sponsor">
    <div>{k}<h2 class="cta__title">{title}</h2></div>
    <div class="cta__actions">{actions}</div>
  </section>'''


def cine_hero(title, lead, eyebrow, video, actions='', meta=None,
              eyebrow_icon='pin', scan='pattern-scanline', ripple=True,
              filter_id='cine'):
    """The cinematic hero: footage, a scrim, a scanline film over it, and an
    optional pointer-tracked ripple through the film.

    Every part of this used to be inline in travel/build.py. It is
    `.hero-band.hero-band-media.hero-band-full` plus `.hero-band__scan` — no
    new CSS, and nothing here is travel-specific any more. `filter_id` only
    needs changing if two cinematic heroes ever share one page.
    """
    rip = ' data-ripple' if ripple else ''
    m = f'\n      {meta_strip(meta)}' if meta else ''
    a = f'\n      <div class="hero__actions">{actions}</div>' if actions else ''
    # The displacement filter is what makes the film ripple rather than just
    # brighten. It is decoration, so the whole <svg> is aria-hidden and its
    # <animate> is frozen by nav.js under reduced motion.
    return f'''
  <section class="hero hero-band hero-band-media hero-band-full">
    <div class="hero-band__media">
      <video autoplay muted loop playsinline aria-hidden="true">
        <source src="{video}" type="video/mp4" />
      </video>
    </div>

    <div class="hero-band__scan"{rip} aria-hidden="true"
         style="filter:url(#{filter_id}-ripple)">
      <div class="pattern {scan} pattern-media pattern-lg"></div>
    </div>

    <svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
      <filter id="{filter_id}-ripple" x="-20%" y="-20%" width="140%" height="140%">
        <feTurbulence type="fractalNoise" baseFrequency="0.012 0.05" numOctaves="2"
                      seed="7" result="{filter_id}-noise">
          <animate attributeName="baseFrequency" dur="7s"
                   values="0.010 0.045;0.018 0.06;0.010 0.045" repeatCount="indefinite" />
        </feTurbulence>
        <feDisplacementMap in="SourceGraphic" in2="{filter_id}-noise" scale="22"
                           xChannelSelector="R" yChannelSelector="G" />
      </filter>
    </svg>

    <div class="container">
      <span class="hero__eyebrow">{icon(eyebrow_icon)}{eyebrow}</span>
      <h1 class="hero__title">{title}</h1>
      <p class="hero__lead">{lead}</p>{a}{m}
    </div>
  </section>
'''
