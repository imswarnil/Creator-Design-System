"""The Collections pages.

The demos here import the travel collection's own builder and call its own
section functions, so what the docs show is the markup the routes actually
ship. A docs page that reimplements the thing it documents is a second source
of truth, and the two drift within a week.
"""
import html
import pathlib
import sys

from common import tile, sec, END, ct

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / 'collection' / 'travel'))

import build as travel          # noqa: E402  — the collection's own builder

PAGES = {}

ROUTES = [
    ('index', 'Index', '/travel', 'what is here?',
     'The whole collection: hero, regions, countries, cities, the latest trip, '
     'featured, and every post. The only route with all three cuts on it.'),
    ('region', 'Group', '/travel/asia', 'what is here, of this kind?',
     'One cut already made. Same sections, fewer things in them — an unordered '
     'set that share an attribute.'),
    ('country', 'Place', '/travel/japan', 'what is here about this one thing?',
     'The cities inside it, the trips through it, and its posts.'),
    ('trip', 'Series', '/travel/india-2026', 'what is here, in order?',
     'A trip. The one route with a first, a last and a sequence — so it gets a '
     'spine instead of a grid.'),
    ('post', 'Post', '/travel/the-train-south', 'the thing itself',
     'The article, a rail that says which series it belongs to, and what to '
     'read next.'),
]


def code(lang, text, note=''):
    body = html.escape(text.strip('\n'))
    fig = ('<figure class="codebox codebox-light u-m-0"><figcaption class="codebox__head">'
           f'<span class="codebox__lang">{lang}</span>'
           '<button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>'
           f'<pre class="codebox__pre"><code>{body}</code></pre></figure>')
    return tile(fig, note) if note else f'\t\t<div class="u-mb-6">{fig}</div>'


def p(text):
    return f'\t\t<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">{text}</p>'


def live(markup, note):
    """A section, running, with the strip that names it."""
    return tile(markup, note)


# ── 1 · the contract ────────────────────────────────────────────────────────

c = ''
c += p('A collection is a kind of thing you publish — travel, courses, a video series, '
       'a shop. Each one gets a folder holding the routes it needs, the sections those '
       'routes are built from, and one stylesheet written entirely in the system\'s tokens.')
c += p('The point of doing it this way: <b>a collection is not a new design.</b> It is the '
       'same tokens, the same cards and the same type scale, arranged for a different '
       'subject. If a collection needs a colour or a spacing the system does not have, that '
       'is a question about the system — not a licence to invent one locally.')

c += sec('routes', 'The five routes every collection has',
         'Every collection answers the same five questions, so every collection has the same '
         'five routes. The names change; the shape does not.')
c += ct([(f'<b>{name}</b>', f'{q}<br><span class="t-slate-sm" style="color:var(--fg-faint)">'
          f'travel: <code class="t-code">{path}</code></span>')
         for _, name, path, q, _ in ROUTES], head=('Route', 'The question it answers'))
c += p('<b>Series is the one worth being careful about.</b> A series is an ordered set of '
       'posts made as one body of work — a trip, a course, a season. A <b>group</b> is an '
       'unordered set that share an attribute — a region, a subject, a tag. They look similar '
       'and behave differently: a series has a first and a last and a progress through it; a '
       'group has none of those. That is why the series route gets a spine and the group route '
       'gets a grid.')
c += END

c += sec('folder', 'What a collection folder holds')
c += code('text', '''
collection/
  README.md          the shared contract
  travel/
    README.md        its routes, its sections, its data shape
    travel.css       its components - tokens only, no new primitives
    collection.js    only what CSS cannot do (the linked filters)
    build.py         generates the routes from one set of demo data
    *.html           one file per route, openable with no build
''', 'the first collection, in full')
c += END

c += sec('rules', 'The rules')
c += ct([
    ('Tokens only', 'every value is a <code class="t-code">var(--…)</code>. A collection that '
                    'hard-codes a colour cannot be rebranded, and has quietly left the system'),
    ('Prefix once', 'shared sections are <code class="t-code">col-</code>; a collection\'s own '
                    'extras take its name (<code class="t-code">trv-</code>). Anything useful '
                    'twice graduates from one to the other'),
    ('Reuse before adding', 'a place card <em>is</em> a card. If a section is 90% an existing '
                            'component, it is that component with a modifier'),
    ('JS is additive', 'the filters degrade to showing everything. Every route must be '
                       'readable and navigable with the script blocked'),
    ('State in ARIA', '<code class="t-code">aria-pressed</code> on a filter, '
                      '<code class="t-code">aria-current</code> on the current item. Never an '
                      '<code class="t-code">.active</code> class'),
], head=('Rule', 'Why'))
c += END

PAGES['collections'] = ('Collections',
    'A collection is a kind of thing you publish. Five routes, one section vocabulary, and '
    'one rule: it is the same design system arranged for a different subject.', c)


# ── 2 · the sections ────────────────────────────────────────────────────────

s = ''
s += p('The vocabulary a route is assembled from. Every section below is a block you can drop '
       'into any route of any collection — that is what makes them worth having rather than '
       'being page-specific markup.')
s += p('Each demo is the travel collection\'s own markup, called from its own builder. If a '
       'section only looks right inside one route, it is not a section yet.')

s += sec('hero', 'Collection hero', 'A collection index has to say what it is before it starts '
         'listing. The art does the saying, so the copy can be short. It is decoration, so it '
         'is aria-hidden and it stops dead under reduced motion.')
s += live('<div class="col-hero" style="min-height:15rem">' + travel.GLOBE +
          '<div class="col-hero__in" style="padding:var(--space-8)">'
          '<span class="col-hero__eyebrow">' + travel.icon('pin') + 'The travel collection</span>'
          '<h3 class="col-hero__title" style="font-size:var(--text-3xl)">'
          'Every road, <em>in order</em>.</h3>'
          '<p class="col-hero__lead">The lead sits under it.</p></div></div>',
          '<b>.col-hero</b> · <b>.col-hero__art</b> — the globe turns, the flight draws itself, '
          'the palm leans')
s += END

s += sec('search', 'Search and the call', 'People arrive at an index knowing roughly what they '
         'want, so search leads and browsing follows.')
s += live('<div class="col-hero" style="padding:var(--space-6)">'
          '<form class="col-search" onsubmit="return false">'
          '<label class="col-search__field"><span class="u-sr-only">Search</span>'
          + travel.icon('compass') +
          '<input type="search" placeholder="Where do you want to go?" /></label>'
          '<button class="btn btn-primary btn-pill" type="submit">Search</button></form></div>',
          '<b>.col-search</b> — one field, one button, on the hero surface')
s += END

s += sec('meta', 'The meta strip', '"How much is here" is the second question after "what is '
         'this", so the numbers sit directly under the hero copy.')
s += live('<div class="col-meta col-meta-paper" style="border-top:0;padding-top:0">'
          + ''.join(f'<div><span class="col-meta__n">{n}</span>'
                    f'<span class="col-meta__l">{l}</span></div>'
                    for n, l in [('31', 'posts'), ('6', 'countries'),
                                 ('4', 'trips'), ('18', 'cities')]) + '</div>',
          '<b>.col-meta</b> — add <b>.col-meta-paper</b> when it is not on the dark hero')
s += END

s += sec('groups', 'Groups — the widest cut', 'Icon, name, count. Anything more and it competes '
         'with the places below it.')
s += live(travel.regions_block(), '<b>.col-groups</b> · <b>.col-group</b> — press one; '
          '<code class="t-code">aria-pressed</code> carries the state')
s += END

s += sec('places', 'Places — a picture, a name, a sentence',
         'The same three parts every collection card has, in a travel-shaped body.')
s += live('<div class="col-places">' + ''.join(
    f'<button class="col-place" type="button" aria-pressed="false">'
    f'<span class="col-place__media">{travel.ph(slug)}'
    f'<span class="col-place__tag">{code_}</span></span>'
    f'<span class="col-place__body"><span class="col-place__name">{name}</span>'
    f'<span class="col-place__note">{note}</span></span>'
    f'<span class="col-place__foot"><span>{n} posts</span></span></button>'
    for slug, name, _, note, _, n, code_ in travel.COUNTRIES[:3]) + '</div>',
    '<b>.col-places</b> · <b>.col-place</b> — the art is a placeholder, not a photograph, '
    'so the demo never depends on one')
s += END

s += sec('spots', 'Spots — the narrowest cut', 'The smallest shape, so thirty of them can sit '
         'in a row without the page becoming a grid nobody reads.')
s += live(travel.cities_block(), '<b>.col-spots</b> · <b>.col-spot</b>')
s += END

s += sec('series-card', 'A series card', 'It shows the shape of the whole body of work: how '
         'many parts, over how long, and where it went.')
s += live(travel.series_card(), '<b>.col-series</b>')
s += END

s += sec('order', 'The order — a series, laid out', 'The one thing a series has that a group '
         'does not is sequence, so it gets a spine. The rule stops at the last item rather '
         'than trailing into nothing.')
s += live('<div class="col-order">' + ''.join(
    f'<a class="col-order__item" href="#i"{" aria-current=\"page\"" if i == 1 else ""}>'
    f'<span class="col-order__num"><span class="col-order__dot"></span>{i + 1:02d}</span>'
    f'<span class="col-order__body"><span class="col-order__title">{t}</span>'
    f'<span class="col-order__note">{note}</span></span></a>'
    for i, (t, note, _, _) in enumerate(travel.TRIP[:3])) + '</div>',
    '<b>.col-order</b> — <code class="t-code">aria-current</code> marks where the reader is')
s += END

s += sec('posts', 'Post rows', 'The list every route ends with. A row rather than a card, '
         'because by this point the reader is scanning titles, not looking at pictures.')
s += live(travel.posts_block(limit=3), '<b>.col-posts</b> · <b>.col-post-row</b>')
s += END

s += sec('facets', 'The facet sidebar', 'Checkboxes, because more than one can be true at '
         'once, and native inputs so the keyboard works for free.')
s += live('<div style="max-width:17rem">'
          + travel.facets_block().replace('<aside class="col-layout__side">', '<div>')
                                 .replace('</aside>', '</div>') + '</div>',
          '<b>.col-facets</b> · <b>.col-facet</b> — or-within-a-facet: ticking beach and '
          'mountains means either, not both')
s += END

s += sec('next', 'Next in series')
s += live('<a class="col-next" href="#i"><span class="col-next__label">Next · Part 4</span>'
          '<span class="col-order__title">Goa is two places</span>'
          '<span class="t-small u-fg-subtle">North and south, and the road between them.</span></a>',
          '<b>.col-next</b>')
s += END

s += sec('registry', 'The registry',
         'Every section, where it is used, and whether it needs JavaScript. A section is only '
         'done when it works in both themes, at every width, and with the script blocked '
         'unless it is listed as needing it.')
s += ct([
    ('.col-hero', 'index — no JS'),
    ('.col-search', 'index, group — no JS'),
    ('.col-meta', 'index, group, series — no JS'),
    ('.col-groups', 'index — no JS'),
    ('.col-places', 'index, group — no JS'),
    ('.col-spots', 'index, group, place — no JS'),
    ('.col-facets', 'index, group — <b>needs JS</b>'),
    ('.col-series', 'index, place — no JS'),
    ('.col-order', 'series — no JS'),
    ('.col-posts', 'everywhere — no JS'),
    ('.col-post', 'post — no JS'),
    ('.col-next', 'post, series — no JS'),
    ('.col-map', 'planned'),
    ('.col-gallery', 'planned'),
    ('.col-figures', 'planned'),
], head=('Section', 'Used on'))
s += END

PAGES['col-sections'] = ('Collection sections',
    'The vocabulary a collection route is assembled from — every block, running, with the '
    'markup the real routes ship.', s)


# ── 3 · travel ──────────────────────────────────────────────────────────────

t = ''
t += p('The first collection, and the one the sections were designed against. Five routes over '
       'a deliberately small demo dataset — five countries and seven cities is enough to prove '
       'the filters link up, and forty would only be a data-entry exercise.')

t += sec('routes-t', 'The five routes', 'Each one opens in a new tab. They are plain files: no '
         'server, no build, no framework.')
t += ct([(f'<a href="./collection/travel/{slug}.html" target="_blank" rel="noopener">'
          f'<b>{name}</b></a> — <code class="t-code">{path}</code>', desc)
         for slug, name, path, _, desc in ROUTES], head=('Route', 'What is on it'))
t += p('<a class="btn btn-primary btn-sm" href="./collection/travel/index.html" '
       'target="_blank" rel="noopener">Open the travel collection →</a> '
       '<a class="btn btn-secondary btn-sm" href="./collection/travel/components.html" '
       'target="_blank" rel="noopener">Its sections on their own →</a>')
t += END

t += sec('filters-t', 'How the filtering links up',
         'Region narrows countries, country narrows cities, and the facets narrow everything. '
         'None of it is travel-specific: the script reads data attributes, so any collection '
         'with groups, places and spots gets the same behaviour.')
t += code('html', '''
<div data-collection>
  <button data-group="asia">Asia</button>

  <button data-place="japan" data-of="asia" data-tags="city food">Japan</button>

  <a data-spot="tokyo" data-of="japan" data-tags="city food party">Tokyo</a>

  <a data-post data-of="japan" data-region="asia" data-tags="city">A post</a>

  <label><input type="checkbox" data-facet="beach"> Beach</label>

  <p data-empty-for="[data-post]" hidden>Nothing matches.</p>
</div>
''', 'the script only ever sets <b>data-filtered="out"</b>; the stylesheet decides what that means')
t += p('With the script blocked, every item shows — which is the correct fallback for a page '
       'whose job is listing things. A city belongs to a country and a country to a region, so '
       'a city survives a filter only if its country did.')
t += END

t += sec('icons-t', 'Travel icons',
         'Sixteen, on the same 24×24 grid at 1.5px, <code class="t-code">currentColor</code> '
         'only — so they follow the text colour and theme themselves.')
t += tile('<div class="cluster" style="gap:var(--space-5);flex-wrap:wrap">' + ''.join(
    f'<span style="display:grid;gap:var(--space-2);justify-items:center;width:4.5rem">'
    f'{travel.icon(n, "icon")}'
    f'<span class="t-slate-sm" style="color:var(--fg-faint)">{n}</span></span>'
    for n in ['globe', 'beach', 'mountain', 'city', 'compass', 'passport', 'backpack',
              'route', 'pin', 'party', 'food', 'tent', 'plane', 'train', 'sun', 'visa'])
    + '</div>', '<b>icons/travel/</b> — inline them, or use a sprite when you need theming')
t += END

PAGES['col-travel'] = ('Travel collection',
    'The first collection: five routes, sixteen icons and a linked filter, over a demo dataset '
    'small enough to read.', t)
