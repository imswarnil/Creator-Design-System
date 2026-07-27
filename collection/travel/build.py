#!/usr/bin/env python3
"""Build the travel collection's six routes.

    python3 collection/travel/build.py

Generated rather than hand-written for the same reason the docs are: six pages
share a head, a navbar, a footer and one set of demo data, and six copies of
those drift apart within a week.

Every page is openable straight from disk — the stylesheets are linked by
relative path, so nothing needs serving to look at it.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
REL = '../..'          # from collection/travel/*.html back to the repo root

# ── The demo data ───────────────────────────────────────────────────────────
# Deliberately small. A demo with forty countries in it is a data-entry
# exercise; five is enough to prove the filtering links up.

REGIONS = [
    ('asia', 'Asia', 'globe', 3),
    ('europe', 'Europe', 'compass', 2),
    ('americas', 'Americas', 'mountain', 1),
]

COUNTRIES = [
    ('japan', 'Japan', 'asia', 'Trains that leave on the second, and a country '
     'built to be seen from one.', 'city food mountains', 6, 'JP'),
    ('vietnam', 'Vietnam', 'asia', 'Coast road, coffee, and the best food you '
     'will eat sitting on a plastic stool.', 'beach food city', 4, 'VN'),
    ('portugal', 'Portugal', 'europe', 'Atlantic light, tiled walls, and hills '
     'that punish a heavy backpack.', 'beach city party', 5, 'PT'),
    ('georgia', 'Georgia', 'europe', 'Caucasus on one side, wine on the other, '
     'and eight days that were not enough.', 'mountains food party', 8, 'GE'),
    ('peru', 'Peru', 'americas', 'Altitude, ruins, and a bus timetable that is '
     'more of a suggestion.', 'mountains food', 3, 'PE'),
]

CITIES = [
    ('tokyo', 'Tokyo', 'japan', 'city food party', 4),
    ('kyoto', 'Kyoto', 'japan', 'city food', 2),
    ('hanoi', 'Hanoi', 'vietnam', 'city food', 3),
    ('lisbon', 'Lisbon', 'portugal', 'city beach party', 3),
    ('porto', 'Porto', 'portugal', 'city food', 2),
    ('tbilisi', 'Tbilisi', 'georgia', 'city food party', 5),
    ('cusco', 'Cusco', 'peru', 'mountains city', 3),
]

FACETS = [
    ('beach', 'Beach', 'beach', 12),
    ('mountains', 'Mountains', 'mountain', 16),
    ('city', 'Cities', 'city', 24),
    ('party', 'Nightlife', 'party', 9),
    ('food', 'Food', 'food', 21),
]

POSTS = [
    ('Getting an Indian visa without losing a week', 'india', 'asia',
     'city', '8 min', 'Mar 2026'),
    ('Goa is two places, and only one of them is on Instagram', 'india', 'asia',
     'beach party', '11 min', 'Mar 2026'),
    ('The night train to Tbilisi', 'georgia', 'europe', 'mountains', '6 min', 'Feb 2026'),
    ('Eight days in Georgia, and the map I would redraw', 'georgia', 'europe',
     'mountains food', '14 min', 'Feb 2026'),
    ('Kyoto in the rain is the correct Kyoto', 'japan', 'asia', 'city food', '9 min', 'Nov 2025'),
    ('What a month in Lisbon actually costs', 'portugal', 'europe',
     'city beach', '12 min', 'Sep 2025'),
]

TRIP = [
    ('Getting an Indian visa without losing a week', 'The paperwork, in the order '
     'it actually happens.', 'Day 0 · Delhi', 'visa'),
    ('Landing in Delhi at 2am', 'Airport to old city, and why not to book the '
     'first night in advance.', 'Day 1 · Delhi', 'plane'),
    ('The train south', 'Sixteen hours, three classes, and which one to book.',
     'Day 3 · Goa', 'train'),
    ('Goa is two places', 'North and south, and the road between them.',
     'Day 4 · Goa', 'beach'),
    ('What eight days cost', 'Every rupee, with the things I would skip.',
     'Day 8 · Home', 'route'),
]


def icon(name, cls='icon'):
    """Inline the real icon file so it inherits currentColor."""
    p = REPO / 'icons' / 'travel' / f'{name}.svg'
    if not p.exists():
        p = REPO / 'icons' / 'ui' / f'{name}.svg'
    svg = p.read_text().strip() if p.exists() else ''
    return svg.replace('<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1)


# A placeholder that cannot 404. Each place gets its own hue off the same
# ladder, so the grid reads as a set rather than a pile of stock photos.
def ph(seed, tall=False):
    hues = {'japan': 8, 'vietnam': 150, 'portugal': 205, 'georgia': 265,
            'peru': 32, 'india': 340, 'default': 220}
    h = hues.get(seed, hues['default'])
    return (f'<span class="col-ph" style="--h:{h}"'
            f'{" data-tall" if tall else ""} aria-hidden="true"></span>')


HEAD = '''<!doctype html>
<html lang="en" data-theme="light">
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
<link rel="stylesheet" href="{rel}/collection/collection.css" />
<link rel="stylesheet" href="./travel.css" />
<script src="{rel}/src/nav.js" defer></script>
<script src="{rel}/collection/collection.js" defer></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="nav-shell">
  <nav class="nav-bar" aria-label="Main">
    <a class="logo logo-sm" href="{rel}/docs/index.html">Swarnil</a>
    <div class="nav-links">
      <a class="nav-link" href="./index.html"{cur_index}>Travel</a>
      <a class="nav-link" href="{rel}/collection/blog/index.html">Blog</a>
      <a class="nav-link" href="#i">Watch</a>
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
      <p class="t-slate">Travel — a collection</p>
      <p class="t-slate-sm"><a href="{rel}/collection/README.md">Built from the collection contract</a></p>
    </div>
  </div>
</footer>
</body>
</html>
'''


def page(name, title, desc, body, cur_index=False):
    html = (HEAD.format(title=title, desc=desc, rel=REL,
                        cur_index=' aria-current="page"' if cur_index else '')
            + body + FOOT.format(rel=REL))
    (HERE / name).write_text(html)
    return name


# ── The hero art ────────────────────────────────────────────────────────────
# A night sky, a turning globe, a flight arcing off it and a palm leaning in
# from the edge. All decoration, so the whole thing is aria-hidden — and every
# moving part stops under prefers-reduced-motion.

GLOBE = '''
  <svg class="col-hero__art" viewBox="0 0 1200 520" preserveAspectRatio="xMaxYMid slice"
       aria-hidden="true" focusable="false">
    <defs>
      <radialGradient id="trv-sky" cx="30%" cy="20%" r="90%">
        <stop offset="0%" stop-color="#1b2030"/>
        <stop offset="55%" stop-color="#0e1119"/>
        <stop offset="100%" stop-color="#08080c"/>
      </radialGradient>
      <linearGradient id="trv-sea" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#1d3a4a"/>
        <stop offset="100%" stop-color="#0b1520"/>
      </linearGradient>
      <clipPath id="trv-ball"><circle cx="905" cy="250" r="150"/></clipPath>
    </defs>

    <rect width="1200" height="520" fill="url(#trv-sky)"/>

    <!-- stars -->
    <g fill="#fff">
      <circle class="trv-star" cx="660" cy="70" r="1.6" style="animation-delay:0s"/>
      <circle class="trv-star" cx="760" cy="40" r="1.2" style="animation-delay:.6s"/>
      <circle class="trv-star" cx="820" cy="96" r="1.7" style="animation-delay:1.2s"/>
      <circle class="trv-star" cx="700" cy="50" r="1.2" style="animation-delay:1.8s"/>
      <circle class="trv-star" cx="1050" cy="70" r="1.5" style="animation-delay:2.4s"/>
      <circle class="trv-star" cx="700" cy="150" r="1.1" style="animation-delay:3s"/>
      <circle class="trv-star" cx="1130" cy="180" r="1.3" style="animation-delay:1.5s"/>
    </g>

    <!-- the globe: a lit ball, a turning grid, one continent hint -->
    <circle cx="905" cy="250" r="150" fill="#11161f"/>
    <circle cx="905" cy="250" r="150" fill="none" stroke="#ffffff" stroke-opacity=".22"/>
    <g clip-path="url(#trv-ball)">
      <g class="trv-globe__grid" style="transform-origin:905px 250px">
        <g fill="none" stroke="#ffffff" stroke-opacity=".14">
          <ellipse cx="905" cy="250" rx="52" ry="150"/>
          <ellipse cx="905" cy="250" rx="104" ry="150"/>
          <ellipse cx="905" cy="250" rx="148" ry="150"/>
        </g>
        <path d="M790 210q60-28 118-6t120-10" fill="none" stroke="#f04e2e" stroke-opacity=".55" stroke-width="2"/>
        <path d="M800 300q70 26 130 4t118 6" fill="none" stroke="#ffffff" stroke-opacity=".12" stroke-width="2"/>
      </g>
      <g fill="none" stroke="#ffffff" stroke-opacity=".14">
        <path d="M755 200h300M755 250h300M755 300h300"/>
      </g>
    </g>

    <!-- the flight: an arc that draws itself, with the plane riding the end -->
    <path class="trv-route" d="M700 336C752 252 800 200 862 196"
          fill="none" stroke="#f04e2e" stroke-width="2.5"
          stroke-linecap="round" stroke-dasharray="260"/>
    <circle cx="700" cy="336" r="5" fill="#f04e2e"/>
    <g class="trv-plane" transform="translate(838 176) rotate(18) scale(1.5)">
      <path d="M20 5 4 11.5l5.5 2M20 5l-3.5 14-3-6.5M20 5 9.5 13.5v4.2l3-3.7"
            fill="none" stroke="#fff" stroke-width="1.5"
            stroke-linecap="round" stroke-linejoin="round"/>
    </g>

    <!-- the shore -->
    <path d="M0 430c120 18 260 22 420 12s300-26 420-14 240 24 360 18v74H0Z" fill="url(#trv-sea)"/>
    <path d="M0 448c140 16 280 18 430 8s310-22 430-12 220 20 340 16" fill="none"
          stroke="#ffffff" stroke-opacity=".12"/>

    <!-- the palm, leaning in from the edge -->
    <g class="trv-palm" style="transform-origin:1108px 474px" stroke="#ffffff"
       stroke-opacity=".45" fill="none" stroke-width="3" stroke-linecap="round">
      <path d="M1108 474c-4-40-2-70 8-96"/>
      <path d="M1116 378c-26-14-48-10-64 6M1116 378c26-16 50-12 66 6M1116 378c-14-26-10-48 4-64M1116 378c22-20 46-22 62-12"/>
    </g>
    <ellipse cx="1108" cy="476" rx="32" ry="6" fill="#000" opacity=".35"/>
  </svg>
'''


def hero(title, lead, eyebrow, meta, search=True, art=True):
    m = ''.join(
        f'<div><span class="col-meta__n">{n}</span>'
        f'<span class="col-meta__l">{l}</span></div>' for n, l in meta)
    s = ('''
      <form class="col-search" onsubmit="return false">
        <label class="col-search__field">
          <span class="u-sr-only">Search destinations</span>
          ''' + icon('compass') + '''
          <input type="search" placeholder="Where do you want to go?" />
        </label>
        <button class="btn btn-primary btn-pill" type="submit">Search</button>
        <a class="btn btn-ghost btn-pill" href="#trips">Latest trip →</a>
      </form>''') if search else ''
    return f'''
  <section class="container u-mt-6">
   <div class="col-hero">
    {GLOBE if art else ''}
    <div class="col-hero__in">
      <span class="col-hero__eyebrow">{icon('pin')}{eyebrow}</span>
      <h1 class="col-hero__title">{title}</h1>
      <p class="col-hero__lead">{lead}</p>
      {s}
      <div class="col-meta">{m}</div>
    </div>
   </div>
  </section>
'''


def sec(title, note='', extra=''):
    n = f'<p class="t-subtle u-mt-2" style="max-width:var(--measure-lead)">{note}</p>' if note else ''
    return (f'<div class="row-between u-mb-5"><div><h2 class="t-h3">{title}</h2>{n}</div>'
            f'{extra}</div>')


def regions_block():
    out = ['<div class="col-groups">']
    for slug, name, ico, n in REGIONS:
        out.append(
            f'<button class="col-group" type="button" data-group="{slug}" aria-pressed="false">'
            f'<span class="col-group__ico">{icon(ico)}</span>'
            f'<span><span class="col-group__name">{name}</span>'
            f'<span class="col-group__n">{n} {"country" if n == 1 else "countries"}'
            f'</span></span></button>')
    return '\n'.join(out) + '</div>'


def countries_block():
    out = ['<div class="col-places">']
    for slug, name, region, note, tags, n, code in COUNTRIES:
        out.append(
            f'<button class="col-place" type="button" data-place="{slug}" data-of="{region}" '
            f'data-tags="{tags}" aria-pressed="false">'
            f'<span class="col-place__media">{ph(slug)}'
            f'<span class="col-place__tag">{code}</span></span>'
            f'<span class="col-place__body">'
            f'<span class="col-place__name">{name}</span>'
            f'<span class="col-place__note">{note}</span></span>'
            f'<span class="col-place__foot"><span>{n} posts</span>'
            f'<span>{tags.split()[0]}</span></span></button>')
    out.append('<p class="col-empty" data-empty-for="[data-place]" hidden>'
               'No country matches that combination.</p>')
    return '\n'.join(out) + '</div>'


def cities_block():
    out = ['<div class="col-spots">']
    for slug, name, of, tags, n in CITIES:
        out.append(f'<a class="col-spot" href="./country.html" data-spot="{slug}" '
                   f'data-of="{of}" data-tags="{tags}">{name}'
                   f'<span class="col-spot__n">{n}</span></a>')
    out.append('<p class="col-empty" data-empty-for="[data-spot]" hidden>'
               'No city under that filter yet.</p>')
    return '\n'.join(out) + '</div>'


def facets_block():
    rows = ''.join(
        f'<label class="col-facet">'
        f'<input type="checkbox" data-facet="{slug}" />'
        f'{icon(ico)}<span>{name}</span><span class="col-facet__n">{n}</span></label>'
        for slug, name, ico, n in FACETS)
    return f'''
    <aside class="col-layout__side">
      <div class="col-facets">
        <div class="col-facets__group">
          <span class="col-facets__title">Filtering</span>
          <p class="t-small u-fg-subtle" data-filter-state>Everywhere</p>
          <button class="btn btn-quiet btn-sm" type="button" data-filter-reset hidden>
            Clear filters
          </button>
        </div>
        <div class="col-facets__group">
          <span class="col-facets__title">Kind of place</span>
          {rows}
        </div>
        <div class="col-facets__group">
          <span class="col-facets__title">Regions</span>
          {''.join(f'<label class="col-facet"><input type="checkbox" data-facet="{s}" />{icon(i)}<span>{n}</span></label>' for s, n, i, _ in REGIONS)}
        </div>
      </div>
    </aside>'''


def posts_block(limit=None):
    rows = []
    for title, of, region, tags, read, when in (POSTS[:limit] if limit else POSTS):
        rows.append(
            f'<a class="col-post-row" href="./post.html" data-post data-of="{of}" '
            f'data-region="{region}" data-tags="{tags}">'
            f'<span class="col-post-row__thumb">{ph(of)}</span>'
            f'<span class="col-post-row__body">'
            f'<span class="col-post-row__title">{title}</span>'
            f'<span class="col-post-row__note">{tags.replace(" ", " · ")}</span></span>'
            f'<span class="col-post-row__meta"><span>{read}</span><span>{when}</span></span></a>')
    rows.append('<p class="col-empty" data-empty-for="[data-post]" hidden>'
                'No posts match. Try clearing a filter.</p>')
    return '<div class="col-posts">' + '\n'.join(rows) + '</div>'


def series_card():
    stats = ''.join(f'<span>{icon(i)}{t}</span>' for i, t in
                    [('route', '5 parts'), ('sun', '8 days'), ('pin', 'India')])
    return f'''
    <a class="col-series" href="./trip.html">
      <span class="col-series__media">{ph('india', True)}</span>
      <span class="col-series__body">
        <span class="col-hero__eyebrow" style="color:var(--fg-faint)">{icon('route')}Latest trip</span>
        <span class="col-series__title">India, in eight days and five posts</span>
        <span class="t-small u-fg-subtle">A trip is a collection of posts that were
          made as one body of work — so it has a first, a last, and an order.</span>
        <span class="col-series__stats">{stats}</span>
      </span>
    </a>'''


# ── 1 · /travel — the collection index ──────────────────────────────────────

def route_index():
    body = hero(
        'Every road I have been down, <em>in order</em>.',
        'Six countries, thirty-one posts and the receipts. Start with a region, '
        'narrow to a country, then pick the city — or just read the latest trip.',
        'The travel collection',
        [('31', 'posts'), ('6', 'countries'), ('4', 'trips'), ('18', 'cities')])

    body += f'''
  <div data-collection>
  <section class="container section-sm">
    {sec('Regions', 'The widest cut. Pick one and everything below narrows to it.')}
    {regions_block()}
  </section>

  <section class="container section-sm">
    <div class="col-layout">
      {facets_block()}
      <div>
        {sec('Countries', 'Selecting a country narrows the cities and the posts.')}
        {countries_block()}

        <div class="u-mt-10">
          {sec('Cities', 'The narrowest cut — and the one people actually search for.')}
          {cities_block()}
        </div>

        <div class="u-mt-10" id="trips">
          {sec('Latest trip')}
          {series_card()}
        </div>

        <div class="u-mt-10">
          {sec('Featured', 'The three worth reading first.')}
          {posts_block(limit=3)}
        </div>

        <div class="u-mt-10">
          {sec('All travel posts')}
          {posts_block()}
        </div>
      </div>
    </div>
  </section>
  </div>
'''
    return page('index.html', 'Travel — Swarnil',
                'Six countries, thirty-one posts and the receipts.', body, cur_index=True)


# ── 2 · /travel/asia — a group ──────────────────────────────────────────────

def route_region():
    countries = [c for c in COUNTRIES if c[2] == 'asia']
    cards = '\n'.join(
        f'<a class="col-place" href="./country.html" data-tags="{tags}">'
        f'<span class="col-place__media">{ph(slug)}'
        f'<span class="col-place__tag">{code}</span></span>'
        f'<span class="col-place__body"><span class="col-place__name">{name}</span>'
        f'<span class="col-place__note">{note}</span></span>'
        f'<span class="col-place__foot"><span>{n} posts</span></span></a>'
        for slug, name, _, note, tags, n, code in countries)

    body = hero(
        'Asia', 'Two countries so far, ten posts, and a strong opinion about '
        'night trains. The region page is the same collection with one cut already made.',
        'Region', [('10', 'posts'), ('2', 'countries'), ('3', 'cities')],
        search=False)

    body += f'''
  <section class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Travel</a> <span>/</span> <span>Asia</span>
    </nav>
    <div class="col-layout" data-collection>
      {facets_block()}
      <div>
        {sec('Countries in Asia')}
        <div class="col-places">{cards}</div>

        <div class="u-mt-10">
          {sec('Cities')}
          <div class="col-spots">
            {''.join(f'<a class="col-spot" href="./country.html" data-tags="{t}">{n}<span class="col-spot__n">{c}</span></a>' for _, n, of, t, c in CITIES if of in ('japan', 'vietnam'))}
          </div>
        </div>

        <div class="u-mt-10">
          {sec('Posts from Asia')}
          {posts_block()}
        </div>
      </div>
    </div>
  </section>
'''
    return page('region.html', 'Asia — Travel — Swarnil',
                'Every travel post from Asia.', body)


# ── 3 · /travel/japan — a place ─────────────────────────────────────────────

def route_country():
    cities = [c for c in CITIES if c[2] == 'japan']
    body = hero(
        'Japan', 'Six posts, two cities, and the one country where I stopped '
        'planning and just took trains.', 'Country · Asia',
        [('6', 'posts'), ('2', 'cities'), ('21', 'days'), ('2', 'trips')],
        search=False)

    body += f'''
  <section class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Travel</a> <span>/</span>
      <a href="./region.html">Asia</a> <span>/</span> <span>Japan</span>
    </nav>

    {sec('Cities', 'Where the posts actually happen.')}
    <div class="col-places u-mb-10">
      {''.join(f"""<a class="col-place" href="#i">
        <span class="col-place__media">{ph('japan')}</span>
        <span class="col-place__body"><span class="col-place__name">{name}</span>
        <span class="col-place__note">{n} posts · {tags.replace(' ', ' · ')}</span></span>
      </a>""" for _, name, _, tags, n in cities)}
    </div>

    {sec('Trips through Japan')}
    <div class="u-mb-10">{series_card()}</div>

    {sec('All posts from Japan')}
    {posts_block()}
  </section>
'''
    return page('country.html', 'Japan — Travel — Swarnil',
                'Every travel post from Japan.', body)


# ── 4 · /travel/india-2026 — a series ───────────────────────────────────────

def route_trip():
    items = '\n'.join(
        f'<a class="col-order__item" href="./post.html"{" aria-current=\"page\"" if i == 2 else ""}>'
        f'<span class="col-order__num"><span class="col-order__dot"></span>{i + 1:02d}</span>'
        f'<span class="col-order__body">'
        f'<span class="col-order__title">{title}</span>'
        f'<span class="col-order__note">{note}</span>'
        f'<span class="col-order__meta"><span>{icon(ico)}</span><span>{when}</span></span>'
        f'</span></a>'
        for i, (title, note, when, ico) in enumerate(TRIP))

    body = hero(
        'India, in eight days<br>and five posts',
        'A trip is a series: it has a first post, a last one, and an order that '
        'matters. Read it top to bottom, or jump to the part you came for.',
        'Trip · March 2026',
        [('5', 'parts'), ('8', 'days'), ('2', 'cities'), ('₹41k', 'total')],
        search=False)

    body += f'''
  <section class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Travel</a> <span>/</span> <span>India 2026</span>
    </nav>

    <div class="col-layout">
      <aside class="col-layout__side">
        <div class="col-facets">
          <div class="col-facets__group">
            <span class="col-facets__title">In this trip</span>
            {''.join(f'<a class="col-facet" href="#i">{icon(ico)}<span>{title[:26]}…</span></a>' for title, _, _, ico in TRIP)}
          </div>
          <div class="col-facets__group">
            <span class="col-facets__title">Where it went</span>
            <div class="col-spots">
              <a class="col-spot" href="#i">Delhi</a>
              <a class="col-spot" href="#i">Goa</a>
            </div>
          </div>
        </div>
      </aside>
      <div>
        {sec('The trip, in order', 'Every post that was made as part of this one body of work.')}
        <div class="col-order">{items}</div>
      </div>
    </div>
  </section>
'''
    return page('trip.html', 'India 2026 — Travel — Swarnil',
                'A trip: five posts, in the order they happened.', body)


# ── 5 · a post ──────────────────────────────────────────────────────────────

def route_post():
    body = f'''
  <article class="container section-sm">
    <header class="col-post__head">
      <nav class="col-post__crumbs" aria-label="Breadcrumb">
        <a href="./index.html">Travel</a> <span>/</span>
        <a href="./region.html">Asia</a> <span>/</span>
        <a href="./trip.html">India 2026</a> <span>/</span> <span>Part 3</span>
      </nav>
      <h1 class="t-display-2">The train south</h1>
      <p class="t-lead" style="max-width:var(--measure-lead)">
        Sixteen hours, three classes, and which one to book if you would like to
        arrive able to walk.
      </p>
      <div class="col-post__crumbs">
        <span>6 min read</span> <span>·</span> <span>March 2026</span>
        <span>·</span> <span>Part 3 of 5</span>
      </div>
    </header>

    <div class="surface u-mb-8" style="aspect-ratio:16/9;overflow:hidden;border-radius:var(--radius-card)">
      {ph('india', True)}
    </div>

    <div class="col-post">
      <div class="content">
        <p>The sleeper class is not the adventure people tell you it is, and 3AC is
          not the luxury the price suggests. The honest answer is 2AC on an overnight
          and sleeper on anything under six hours.</p>
        <h2>Booking it</h2>
        <p>IRCTC wants an Indian number for the OTP. There are two ways around that,
          and only one of them still works.</p>
        <blockquote class="quote">
          <p>Book the ticket before the visa. The trains fill up faster than the
            consulate does.</p>
        </blockquote>
        <h2>What it actually costs</h2>
        <p>Sixteen hours, two meals, and a berth you can lie flat in came to less
          than a taxi across Delhi.</p>
      </div>

      <aside class="col-post__rail">
        <div class="col-post__rail-card">
          <span class="col-facets__title">This post is part of</span>
          <a class="col-order__title" href="./trip.html">India, in eight days</a>
          <p class="t-small u-fg-subtle">Part 3 of 5</p>
          <a class="btn btn-secondary btn-sm" href="./trip.html">See the whole trip</a>
        </div>
        <div class="col-post__rail-card u-mt-4">
          <span class="col-facets__title">Filed under</span>
          <div class="col-spots">
            <a class="col-spot" href="./country.html">India</a>
            <a class="col-spot" href="#i">Trains</a>
            <a class="col-spot" href="#i">Budget</a>
          </div>
        </div>
      </aside>
    </div>

    <a class="col-next u-mt-10" href="#i">
      <span class="col-next__label">Next in this trip · Part 4</span>
      <span class="col-order__title">Goa is two places</span>
      <span class="t-small u-fg-subtle">North and south, and the road between them.</span>
    </a>
  </article>
'''
    return page('post.html', 'The train south — Travel — Swarnil',
                'Sixteen hours, three classes, and which one to book.', body)


# ── 6 · the components, on their own ────────────────────────────────────────

def route_components():
    def demo(title, note, markup):
        return (f'<section class="u-mb-10"><h2 class="t-h3 u-mb-2">{title}</h2>'
                f'<p class="t-subtle u-mb-5" style="max-width:var(--measure-lead)">{note}</p>'
                f'<div class="surface" style="padding:var(--space-6);border-radius:var(--radius-card)">'
                f'{markup}</div></section>')

    body = f'''
  <div class="container section-sm">
    <header class="u-mb-10">
      <span class="t-slate" style="color:var(--fg-faint)">Collection · Travel</span>
      <h1 class="t-display-2 u-mt-3">The sections, on their own</h1>
      <p class="t-lead u-mt-4" style="max-width:var(--measure-lead)">
        Every block the five travel routes are assembled from, out of context and
        with nothing else on the page. If a section only looks right inside one
        route, it is not a section yet.
      </p>
    </header>

    {demo('col-hero', 'The collection hero. The art is decoration and is aria-hidden; '
          'everything readable is markup.', '<div class="col-hero" style="min-height:16rem">'
          + GLOBE + '<div class="col-hero__in" style="padding:var(--space-8)">'
          '<span class="col-hero__eyebrow">' + icon('pin') + 'Eyebrow</span>'
          '<h3 class="col-hero__title" style="font-size:var(--text-3xl)">The title</h3>'
          '<p class="col-hero__lead">The lead.</p></div></div>')}

    {demo('col-groups', 'The widest cut. Icon, name, count — nothing more, or it '
          'competes with the places below it.', regions_block())}

    {demo('col-places', 'A picture, a name, a sentence. Press one to filter.',
          '<div class="col-places">' + ''.join(
              f'<button class="col-place" type="button" aria-pressed="false">'
              f'<span class="col-place__media">{ph(s)}<span class="col-place__tag">{c}</span></span>'
              f'<span class="col-place__body"><span class="col-place__name">{n}</span>'
              f'<span class="col-place__note">{note}</span></span>'
              f'<span class="col-place__foot"><span>{p} posts</span></span></button>'
              for s, n, _, note, _, p, c in COUNTRIES[:3]) + '</div>')}

    {demo('col-spots', 'The narrowest cut gets the smallest shape, so thirty of '
          'them can sit in a row.', cities_block())}

    {demo('col-series', 'A series card shows the shape of the whole body of work: '
          'how many parts, over how long, and where.', series_card())}

    {demo('col-order', 'The spine of a series. The rule stops at the last item '
          'rather than trailing off.',
          '<div class="col-order">' + ''.join(
              f'<a class="col-order__item" href="#i"{" aria-current=\"page\"" if i == 1 else ""}>'
              f'<span class="col-order__num"><span class="col-order__dot"></span>{i+1:02d}</span>'
              f'<span class="col-order__body"><span class="col-order__title">{t}</span>'
              f'<span class="col-order__note">{note}</span></span></a>'
              for i, (t, note, _, _) in enumerate(TRIP[:3])) + '</div>')}

    {demo('col-posts', 'The list every route ends with. A row, not a card — by '
          'here the reader is scanning titles.', posts_block(limit=3))}

    {demo('col-facets', 'Checkboxes, because more than one can be true at once, '
          'and native inputs so the keyboard works.',
          '<div style="max-width:16rem">' + facets_block().replace('<aside class="col-layout__side">', '<div>').replace('</aside>', '</div>') + '</div>')}

    {demo('col-next', 'What to read after this one.',
          '<a class="col-next" href="#i"><span class="col-next__label">Next · Part 4</span>'
          '<span class="col-order__title">Goa is two places</span></a>')}
  </div>
'''
    return page('components.html', 'Travel sections — Swarnil',
                'Every section the travel routes are built from.', body)


if __name__ == '__main__':
    made = [route_index(), route_region(), route_country(),
            route_trip(), route_post(), route_components()]
    print('wrote ' + ', '.join(made))
