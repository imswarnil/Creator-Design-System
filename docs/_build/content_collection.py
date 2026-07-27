"""The Collections pages.

The demos here import the travel collection's own builder and call its own
section functions, so what the docs show is the markup the routes actually
ship. A docs page that reimplements the thing it documents is a second source
of truth, and the two drift within a week.
"""
import html
import importlib.util
import pathlib
import sys

from common import tile, sec, END, ct

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent

# Both collections have a module called build.py, so they are loaded by path
# under distinct names rather than by import — otherwise the second one to be
# imported silently returns the first.
sys.path.insert(0, str(REPO / 'collection'))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


travel = _load('col_travel_build', REPO / 'collection' / 'travel' / 'build.py')
blog = _load('col_blog_build', REPO / 'collection' / 'blog' / 'build.py')

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
  collection.css     the col- vocabulary - every section, once
  collection.js      the linked filters - the only thing CSS cannot do
  shell.py           the head, navbar and footer every route shares

  _default/          the starting point: cp -r it and rename
    build.py         five routes with no subject in them
    *.html

  travel/
    travel.css       only what travel needs: globe, flight line, palm
    build.py
    *.html           index, region, country, trip, post, components

  blog/
    build.py         no CSS of its own - which is the test
    *.html           index, post
''', 'three collections, and only one of them needs a stylesheet')
c += p('<b>Blog has no CSS of its own, and that is deliberate.</b> If a second collection '
       'cannot be built out of the shared vocabulary, the vocabulary was really just the '
       'first collection wearing a general-sounding prefix. Travel keeps 44 lines — the '
       'globe, the flight line and the palm — because those genuinely belong to travel.')
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

c += sec('starting', 'Starting a new one',
         'The default collection exists to be copied. It has five working routes and nothing '
         'subject-specific in them, so the first thing you see is the shape rather than '
         'somebody else\'s content.')
c += code('bash', '''
cp -r collection/_default collection/podcast
python3 collection/podcast/build.py
''', 'change the six lists at the top of build.py and the collection is yours')
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


s += sec('widgets', 'Widgets — the rail beside a post',
         'Every widget is the same object: a label, a body, sometimes a footer. Six of them '
         'read as one column rather than six competing boxes. A blog needs them most, but a '
         'course rail and a trip rail want the same shape — so they are shared.')
s += live('<div class="col-rail" style="max-width:19rem">'
          + blog.toc_widget() + blog.author_widget() + blog.subscribe_widget() + '</div>',
          '<b>.col-widget</b> · <b>.col-widget__title</b> · <b>.col-widget-accent</b> for the '
          'one that is the point rather than a note')
s += END

s += sec('mini', 'Numbered lists', 'Recent, popular, next. Numbers rather than bullets, '
         'because in these lists the order <em>is</em> the information.')
s += live('<div style="max-width:19rem">' + blog.recent_widget() + '</div>',
          '<b>.col-mini</b> · <b>.col-mini__item</b>')
s += END

s += sec('tags', 'Tags', 'A count beside each, so the shape of the cloud is data rather than '
         'decoration.')
s += live('<div style="max-width:26rem">' + blog.tags_widget(current='css') + '</div>',
          '<b>.col-tags</b> · <b>.col-tag</b> — <code class="t-code">aria-current</code> marks '
          'the one you are filtered to')
s += END

s += sec('progress', 'Reading progress',
         'The same idea as the navbar hairline: a line already on the page doing a second job, '
         'rather than a new piece of chrome.')
s += live('<div style="position:relative;background:var(--bg-sunken);border-radius:var(--radius-md);'
          'overflow:hidden"><div class="col-progress" style="position:static">'
          '<div class="col-progress__bar" style="--value:62%"></div></div>'
          '<p class="t-small u-fg-subtle" style="padding:var(--space-4)">62% read</p></div>',
          '<b>.col-progress</b> — drive <code class="t-code">--value</code> from scroll')
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
    ('.col-rail · .col-widget', 'post rails everywhere — no JS'),
    ('.col-mini', 'widgets — no JS'),
    ('.col-tags · .col-tag', 'post, index — no JS'),
    ('.col-toc', 'post — needs JS only for scrollspy'),
    ('.col-progress', 'post — <b>needs JS</b>'),
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


# ── 4 · the default collection ──────────────────────────────────────────────

d = ''
d += p('The starting point. Five working routes with nothing subject-specific in them — no '
       'globe, no widgets, no content pretending to be yours. Copy the folder, rename it, '
       'change the six lists at the top of its <code class="t-code">build.py</code>, and you '
       'have a collection before you have designed anything.')
d += p('It is also the test. If a section works <em>here</em> — with no collection stylesheet '
       'at all — it is genuinely shared. If it only works once travel\'s CSS is loaded, it '
       'belongs to travel and the prefix was a lie.')

d += sec('routes-d', 'The five routes, empty')
d += ct([(f'<a href="./collection/_default/{f}.html" target="_blank" rel="noopener">'
          f'<b>{n}</b></a>', desc)
         for f, n, desc in [
             ('index', 'Index', 'groups, places, spots, a series card, everything'),
             ('group', 'Group', 'one cut already made — an unordered set'),
             ('place', 'Place', 'its spots, its series, its posts'),
             ('series', 'Series', 'the spine: a first, a last, an order'),
             ('post', 'Post', 'the article, with a rail')]],
        head=('Route', 'What is on it'))
d += p('<a class="btn btn-primary btn-sm" href="./collection/_default/index.html" '
       'target="_blank" rel="noopener">Open the default collection →</a>')
d += END

d += sec('copy', 'Copying it')
d += code('bash', '''
cp -r collection/_default collection/podcast
python3 collection/podcast/build.py
''', 'five routes, immediately')
d += p('Then change these, at the top of the new <code class="t-code">build.py</code>: '
       '<code class="t-code">NAME</code>, <code class="t-code">GROUPS</code>, '
       '<code class="t-code">PLACES</code>, <code class="t-code">SPOTS</code>, '
       '<code class="t-code">FACETS</code>, <code class="t-code">POSTS</code> and '
       '<code class="t-code">SERIES</code>. Nothing below that line refers to the subject.')
d += END

PAGES['col-default'] = ('Default collection',
    'The starting point: five working routes with no subject in them, and the test of whether '
    'a section is genuinely shared.', d)


# ── 5 · blog ────────────────────────────────────────────────────────────────

bl = ''
bl += p('The second collection, and the one that proves the vocabulary is not travel-shaped. '
        '<b>It ships no CSS of its own.</b> Every section on both of its routes is the shared '
        '<code class="t-code">col-</code> vocabulary — which is exactly the test that '
        'vocabulary had to pass before a third collection could trust it.')

bl += sec('routes-b', 'Its routes',
          'A blog needs two. Its "group" is a category and its "series" is a multi-part piece, '
          'and both reuse the same routes travel already has — so they are not rebuilt.')
bl += ct([('<a href="./collection/blog/index.html" target="_blank" rel="noopener"><b>Index</b></a> '
           '— <code class="t-code">/blog</code>',
           'Hero, categories, a topic filter, featured, and everything. The rail carries the '
           'subscribe widget rather than facets alone.'),
          ('<a href="./collection/blog/post.html" target="_blank" rel="noopener"><b>Post</b></a> '
           '— <code class="t-code">/blog/a-post</code>',
           'The article with a five-widget sticky rail: contents, author, subscribe, more on '
           'this topic, and tags. Reading progress across the top.')],
         head=('Route', 'What is on it'))
bl += p('<a class="btn btn-primary btn-sm" href="./collection/blog/post.html" '
        'target="_blank" rel="noopener">Open the post with its rail →</a> '
        '<a class="btn btn-secondary btn-sm" href="./collection/blog/index.html" '
        'target="_blank" rel="noopener">Open /blog →</a>')
bl += END

bl += sec('rail-b', 'The rail', 'Five widgets, one shape. The accent one is the ask; the rest '
          'are notes beside the writing.')
bl += live('<div class="col-rail" style="max-width:19rem">' + blog.toc_widget()
           + blog.author_widget() + blog.subscribe_widget() + blog.recent_widget('More on CSS')
           + blog.tags_widget(current='css') + '</div>',
           'the whole rail from <code class="t-code">/blog/a-post</code>, unchanged')
bl += END

bl += sec('cats-b', 'Categories', 'A blog\'s widest cut is a category, which is the same '
          'section travel uses for a region.')
bl += live(blog.categories_block(), '<b>.col-groups</b> — same section, different subject')
bl += END

PAGES['col-blog'] = ('Blog collection',
    'The second collection, with no CSS of its own — the proof that the section vocabulary is '
    'shared rather than travel-shaped.', bl)
