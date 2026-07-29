"""The Collections pages.

The demos here import each collection's own builder and call its own section
functions, so what the docs show is the markup the routes actually ship. A docs
page that reimplements the thing it documents is a second source of truth, and
the two drift within a week.
"""
import html
import importlib.util
import pathlib
import sys

from common import tile, sec, END, ct

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent

# Every collection has a module called build.py, so they are loaded by path
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
course = _load('col_course_build', REPO / 'collection' / 'course' / 'build.py')
resume = _load('col_resume_build', REPO / 'collection' / '_pages' / 'build.py')
webseries = _load('col_webseries_build', REPO / 'collection' / 'webseries' / 'build.py')

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

  course/
    course.css       the syllabus scene, the level meter, the quiz, the cert
    build.py
    *.html           index, track, topic, course, lesson, components
''', 'four collections, and only two of them need a stylesheet')
c += p('<b>Blog has no CSS of its own, and that is deliberate.</b> If a second collection '
       'cannot be built out of the shared vocabulary, the vocabulary was really just the '
       'first collection wearing a general-sounding prefix. Travel keeps 44 lines — the '
       'globe, the flight line and the palm — because those genuinely belong to travel.')
c += p('<b>Course is the other direction.</b> Its post route has a video in it rather than '
       'prose, and five sections were missing for that. They went into the shared sheet, not '
       'into <code class="t-code">course.css</code>, because a podcast season and a video '
       'series want every one of them — and what a collection keeps for itself is the test of '
       'whether that split was honest.')
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

s += sec('stage', 'The stage — a post whose body is a video',
         'The media leads and the rest of the series sits beside it, because the second '
         'question after "play this" is always "what is after it". Course needed it first; '
         'nothing in it knows about courses.')
s += live('<div class="col-stagebar" style="border-bottom:0">'
          '<a class="btn btn-secondary btn-sm" href="#i" aria-disabled="true">← Previous</a>'
          '<div class="col-stagebar__where"><span class="col-stagebar__pos">'
          f'<span>Lesson {course.HERE_I + 1} of {course.N}</span><span>Layout</span>'
           '<span>14:02</span></span>'
          '<h3 class="t-h3" style="margin:0">Grid, in four rules</h3></div>'
          '<span class="cluster" style="gap:var(--space-2)">'
          '<button class="btn btn-quiet btn-sm" type="button">Mark complete</button>'
          '<a class="btn btn-primary btn-sm" href="#i">Next →</a></span></div>',
          '<b>.col-stage</b> · <b>.col-stagebar</b> — previous and next are the entire '
          'navigation of an ordered collection, so they get the width')
s += END

s += sec('playlist', 'The playlist',
         'The syllabus, beside a player. It <em>is</em> <code class="t-code">.curriculum</code> '
         '— the same modules, the same lesson rows, the same tick. All the modifier adds is a '
         'body that scrolls, because a contents list should not become a different component '
         'the moment it moves next to a video.')
s += live('<div style="max-width:24rem">' + course.curriculum(playlist=True) + '</div>',
          '<b>.col-playlist</b> — <code class="t-code">aria-current</code> is the lesson you '
          'are on, <code class="t-code">[data-done]</code> the ones you have watched, '
          '<code class="t-code">[data-locked]</code> the ones you have not bought')
s += END

s += sec('transcript', 'The transcript', 'Timestamps down the left, so the column of times is '
         'scannable and the line the player is on can be marked without the text moving.')
s += live('<div class="col-transcript">' + ''.join(
    f'<a class="col-transcript__line" href="#i"{" aria-current=\"true\"" if i == 1 else ""}>'
    f'<span class="col-transcript__time">{t}</span><span>{line}</span></a>'
    for i, (t, line) in enumerate(course.TRANSCRIPT[:4])) + '</div>',
    '<b>.col-transcript</b>')
s += END

s += sec('checks', 'Outcomes', 'What you will be able to do afterwards. A promise reads as a '
         'promise in a list and as marketing in a paragraph.')
s += live(course.outcomes_block(course.OUTCOMES[:4]), '<b>.col-checks</b> · <b>.col-check</b>')
s += END

s += sec('offer', 'The offer and the files',
         'The one card on a page that is asking for something, so it is the one that carries '
         'the accent. Beside it, what comes with the thing — rows, because a download is an '
         'action and actions read as a list.')
s += live('<div class="grid-2" style="gap:var(--space-6);align-items:start">'
          '<div style="max-width:20rem">' + course.offer_widget() + '</div>'
          '<div>' + course.files_block() + '</div></div>',
          '<b>.col-offer</b> · <b>.col-files</b> · <b>.col-file</b>')
s += END

s += sec('resume', 'Resume',
         'The strip at the top of an index for someone who has been here before. It outranks '
         'the hero\'s call to action, because "carry on" beats "start" for everyone it applies '
         'to and is invisible to everyone it does not.')
s += live(course.resume_strip(), '<b>.col-resume</b>')
s += END

s += sec('keys', 'Shortcuts and notes',
         'A player has shortcuts whether or not it advertises them, and advertising them is '
         'cheaper than a help page. The note box keeps nothing — it is here because the shape '
         'of the page is wrong without somewhere to put a thought.')
s += live('<div class="grid-2" style="gap:var(--space-6);align-items:start">'
          '<div style="max-width:20rem">' + course.keys_widget() + '</div>'
          '<form class="col-note" onsubmit="return false">'
          '<label class="label" for="d-note">Your note</label>'
          '<textarea class="input" id="d-note" placeholder="Timestamped to where you are."></textarea>'
          '<div class="col-note__foot"><span class="col-note__stamp">At 1:19</span>'
          '<button class="btn btn-secondary btn-sm" type="submit">Save note</button></div>'
          '</form></div>',
          '<b>.col-keys</b> uses the system\'s <code class="t-code">.kbd</code> · '
          '<b>.col-note</b>')
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
    ('.col-stage · .col-stagebar', 'post, when the body is a video — no JS'),
    ('.col-playlist', 'post — no JS'),
    ('.col-transcript', 'post — no JS'),
    ('.col-panel', 'post — <b>needs JS</b>, and stacks under its own headings without it'),
    ('.col-checks', 'series, place — no JS'),
    ('.col-offer', 'series — no JS'),
    ('.col-files', 'post, series — no JS'),
    ('.col-keys · .col-note', 'post — no JS'),
    ('.col-resume', 'index — no JS'),
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
t += ct([(f'<a href="/collection/travel/{slug}.html" target="_blank" rel="noopener">'
          f'<b>{name}</b></a> — <code class="t-code">{path}</code>', desc)
         for slug, name, path, _, desc in ROUTES], head=('Route', 'What is on it'))
t += p('<a class="btn btn-primary btn-sm" href="/collection/travel/index.html" '
       'target="_blank" rel="noopener">Open the travel collection →</a> '
       '<a class="btn btn-secondary btn-sm" href="/collection/travel/components.html" '
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

PAGES['travel/index'] = ('Travel collection',
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
d += ct([(f'<a href="/collection/_default/{f}.html" target="_blank" rel="noopener">'
          f'<b>{n}</b></a>', desc)
         for f, n, desc in [
             ('index', 'Index', 'groups, places, spots, a series card, everything'),
             ('group', 'Group', 'one cut already made — an unordered set'),
             ('place', 'Place', 'its spots, its series, its posts'),
             ('series', 'Series', 'the spine: a first, a last, an order'),
             ('post', 'Post', 'the article, with a rail')]],
        head=('Route', 'What is on it'))
d += p('<a class="btn btn-primary btn-sm" href="/collection/_default/index.html" '
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
bl += ct([('<a href="/collection/blog/index.html" target="_blank" rel="noopener"><b>Index</b></a> '
           '— <code class="t-code">/blog</code>',
           'Hero, categories, a topic filter, featured, and everything. The rail carries the '
           'subscribe widget rather than facets alone.'),
          ('<a href="/collection/blog/post.html" target="_blank" rel="noopener"><b>Post</b></a> '
           '— <code class="t-code">/blog/a-post</code>',
           'The article with a five-widget sticky rail: contents, author, subscribe, more on '
           'this topic, and tags. Reading progress across the top.')],
         head=('Route', 'What is on it'))
bl += p('<a class="btn btn-primary btn-sm" href="/collection/blog/post.html" '
        'target="_blank" rel="noopener">Open the post with its rail →</a> '
        '<a class="btn btn-secondary btn-sm" href="/collection/blog/index.html" '
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

PAGES['blog/index'] = ('Blog collection',
    'The second collection, with no CSS of its own — the proof that the section vocabulary is '
    'shared rather than travel-shaped.', bl)


# ── 6 · course ──────────────────────────────────────────────────────────────

cr = ''
cr += p('The third collection, and the one that grew the vocabulary. Travel and blog are both '
        'collections of <em>reading</em>; course was the first whose post route has a video in '
        'it instead of prose, and five sections were simply missing for that.')
cr += p('They went into the shared sheet rather than into <code class="t-code">course.css</code>, '
        'because a podcast season and a video series want every one of them: the stage, the '
        'stage bar, the playlist, the transcript and the panels. <b>What stayed behind is the '
        'test of whether the split was honest</b> — four things nothing but a course wants: the '
        'syllabus scene, the difficulty meter, the knowledge check and the certificate.')

cr += sec('mapping', 'A course is a series. A track is a group.',
          'This is the whole argument of the collection, and it is the one thing worth getting '
          'right before writing any markup.')
cr += ct([
    ('<b>index</b> — <code class="t-code">/course</code>',
     'Every course. Resume strip, tracks, the filter, the featured course, the grid, topics, '
     'free lessons, what every course includes, and the questions.'),
    ('<b>group</b> — <code class="t-code">/course/layout</code>',
     'A <b>track</b>. An unordered set of courses that share a subject — it has no first course '
     'and nothing to be halfway through.'),
    ('<b>place</b> — <code class="t-code">/course/topic/grid</code>',
     'A <b>topic</b>. One thing, taught wherever it comes up — which is exactly what a '
     'curriculum page cannot tell you.'),
    ('<b>series</b> — <code class="t-code">/course/css-from-scratch</code>',
     'The <b>course</b>. A first lesson, a last one, and a percentage through it. That is the '
     'definition of a series, and the reason this route gets a spine rather than a grid.'),
    ('<b>post</b> — <code class="t-code">/course/…/grid-in-four-rules</code>',
     'The <b>lesson player</b>. The video, the syllabus beside it, and four panels under it.'),
], head=('Route', 'What is on it'))
cr += p('Getting those two the wrong way round is what produces a course page with a grid of '
        'lessons on it — every lesson looking equally like a starting point, on a page whose '
        'entire job is to say which one is first.')
cr += p('<a class="btn btn-primary btn-sm" href="/collection/course/index.html" '
        'target="_blank" rel="noopener">Open /course →</a> '
        '<a class="btn btn-primary btn-sm" href="/collection/course/lesson.html" '
        'target="_blank" rel="noopener">Open the lesson player →</a> '
        '<a class="btn btn-secondary btn-sm" href="/collection/course/components.html" '
        'target="_blank" rel="noopener">Its sections on their own →</a>')
cr += END

cr += sec('player', 'The lesson player',
          'The media leads, the rest of the course sits beside it, and the two ways out of the '
          'lesson get the width of the bar underneath. Previous and next <em>are</em> the '
          'navigation of an ordered collection; everything else on the page is a detour.')
cr += live('<div class="col-stagebar" style="border-bottom:0">'
           '<a class="btn btn-secondary btn-sm" href="#i">← Previous</a>'
           '<div class="col-stagebar__where"><span class="col-stagebar__pos">'
           f'<span>Lesson {course.HERE_I + 1} of {course.N}</span><span>Layout</span>'
           '<span>14:02</span></span>'
           '<h3 class="t-h3" style="margin:0">Grid, in four rules</h3></div>'
           '<span class="cluster" style="gap:var(--space-2)">'
           '<button class="btn btn-quiet btn-sm" type="button">Mark complete</button>'
           '<a class="btn btn-primary btn-sm" href="#i">Next →</a></span></div>',
           '<b>.col-stagebar</b> — a disabled step keeps its place in the layout, so the bar '
           'does not change shape on the first and last lessons')
cr += END

cr += sec('playlist-c', 'The playlist is the curriculum',
          'The list beside the player and the syllabus in the middle of the course page are the '
          'same component. A contents list should not become a different thing the moment it '
          'moves next to a video — so <code class="t-code">.col-playlist</code> is '
          '<code class="t-code">.curriculum</code> with a body that scrolls, and nothing else.')
cr += live('<div class="grid-2" style="gap:var(--space-6);align-items:start">'
           '<div>' + course.curriculum(playlist=True) + '</div>'
           '<div class="col-transcript">' + ''.join(
               f'<a class="col-transcript__line" href="#i"'
               f'{" aria-current=\"true\"" if i == 1 else ""}>'
               f'<span class="col-transcript__time">{t}</span><span>{line}</span></a>'
               for i, (t, line) in enumerate(course.TRANSCRIPT)) + '</div></div>',
           'the playlist and the transcript, from '
           '<code class="t-code">/course/…/grid-in-four-rules</code>, unchanged')
cr += END

cr += sec('panels-c', 'The panels, and what happens without them',
          'Overview, transcript, resources and notes are the system\'s '
          '<code class="t-code">.tabs</code> over four <code class="t-code">.col-panel</code>s. '
          'Until the script runs, every panel is visible under its own heading — four blocks '
          'that all belong to the lesson, stacked. Only once it sets '
          '<code class="t-code">data-tabs="ready"</code> does the stylesheet start hiding the '
          'headings, which is why the no-JS page reads as a page rather than a pile of '
          'unlabelled sections.')
cr += code('html', '''
<div data-tabs>
  <div class="tabs" role="tablist">
    <button class="tab" role="tab" aria-controls="p-notes" aria-selected="false">Notes</button>
  </div>

  <div class="col-panel" id="p-notes" role="tabpanel">
    <span class="col-panel__label">Notes</span>
    …
  </div>
</div>
''', 'the arrows move between tabs and only the selected one is in the tab order — four tabs '
     'cost one Tab press, not four')
cr += END

cr += sec('own', 'What course kept for itself',
          'Four things, and the test of each was whether a second collection would want it. '
          'None of these passed, which is the correct outcome — a shared vocabulary that '
          'absorbs everything is just the last collection wearing a general prefix.')
cr += live('<div class="cluster" style="gap:var(--space-8);flex-wrap:wrap">'
           + ''.join(course.level_chip(n) for n in (1, 2, 3)) + '</div>',
           '<b>.crs-level</b> — the word "intermediate" means nothing until you have seen the '
           'other two; three bars are comparable at a glance across a grid, which is where '
           'difficulty is actually read')
cr += live('<div class="crs-cert pattern pattern-grid pattern-lg pattern-faint">'
           f'<span class="crs-cert__seal">{course.icon("check", group="ui")}</span>'
           '<span class="crs-cert__name">CSS From Scratch</span>'
           '<span class="crs-cert__rule"></span>'
           '<span class="crs-cert__meta">15 lessons · issued on completion</span></div>',
           '<b>.crs-cert</b> — a hairline double border and one line of accent. A certificate '
           'that shouts is a certificate nobody believes')
cr += END

cr += sec('js-c', 'What the script does, and what happens without it',
          'Three modules ship in <code class="t-code">collection.js</code>, and all three obey '
          'the same rule as <code class="t-code">src/nav.js</code>: they only ever set '
          'attributes the stylesheet already understands.')
cr += ct([
    ('Filters', 'blocked → every course, topic and lesson shows. Which is the correct fallback '
                'for a page whose job is listing things.'),
    ('Panels', 'blocked → the four panels stack, each under its own heading. Nothing is '
               'unreachable.'),
    ('Player', 'blocked → the playlist is still a list of links, the stage bar is still two '
               'links, and only <em>mark complete</em> and the <code class="t-code">N</code> / '
               '<code class="t-code">P</code> / <code class="t-code">M</code> keys are gone.'),
], head=('Module', 'With the script blocked'))
cr += p('Nothing is stored. A real course puts completion on the server, and a demo that wrote '
        'to <code class="t-code">localStorage</code> would be teaching a persistence trick '
        'rather than a design system.')
cr += END

PAGES['course/index'] = ('Course collection',
    'The third collection: /course, the lesson player, and the five sections a video-bodied '
    'post needed that reading-shaped collections never asked for.', cr)


# ── 7 · resume ────────────────────────────────────────────────────────────────

r = ''
r += p('Not a collection at all, in the end — a resume is not a group of resumes, with '
       'nothing to narrow and nothing to be halfway through, so it moved into '
       '<code class="t-code">collection/_pages/</code> with the site\'s other one-offs '
       '(home, about, contact, the legal pages). One route, a full-width summary, then a '
       'two-column <code class="t-code">.grid-rail</code>: experience, education and '
       'projects in the main column, skills in the rail.')
r += p('<a class="btn btn-primary btn-sm" href="/collection/_pages/resume.html" '
       'target="_blank" rel="noopener">Open the résumé page →</a>')
r += END

r += sec('summary-r', 'The summary',
         'Name, role, a one-line pitch and the ways to reach the person — the block every '
         'other section on the page is supporting detail for.')
r += live(resume.summary_block('Swarnil Singhai', 'Senior Product Engineer',
    'I build design systems and the sites that run on them.', resume.CONTACTS),
    '<b>.rsm-summary</b> — from <code class="t-code">/resume</code>, unchanged')
r += END

r += sec('timeline-r', 'The career timeline is .col-order',
         'A trip, a syllabus and a career all turn out to be the same shape: a first thing, a '
         'last thing, and a sequence between them. Rather than invent a timeline, the resume '
         'reuses <code class="t-code">.col-order</code> — the series route\'s spine — and adds '
         'only what it did not already have: an icon marking which kind of entry this is, in '
         'place of the plain dot.')
r += live(resume.timeline_block(resume.EXPERIENCE[:2]),
    '<b>.col-order + .rsm-order__icon</b> — the briefcase is the only new pixel')
r += END

r += sec('education-r', 'Education, the same spine again',
         'Same component, same icon treatment, a graduation cap instead of a briefcase. 10th, '
         '12th and a bachelor\'s are one row shape, not three — a school swaps a place for a '
         'stream and a percentage for a CGPA, but nothing about the shape changes.')
r += live(resume.education_block(resume.EDUCATION), '<b>.col-order</b> — unmodified')
r += END

r += sec('projects-r', 'Projects is not a new component either',
         'A project is an unordered set, not a sequence — so it is the shared '
         '<code class="t-code">.card</code>, gridded two-up, the same component travel and '
         'course already put in a row of three.')
r += live(resume.projects_block(resume.RESUME_PROJECTS[:2]), '<b>.card</b> in a <b>.grid-2</b>')
r += END

r += sec('skills-r', 'Skills is not a new component',
         'A resume\'s skill list is a cluster of the shared <code class="t-code">.badge</code>, '
         'because inventing a chip for a page that already has one would be exactly the '
         'mistake the collection contract warns against.')
r += live(resume.skills_block(resume.SKILLS[:5]), '<b>.badge</b>, in a <b>.cluster</b>')
r += END

r += sec('icons-r', 'Resume icons',
         'Five, on the same 24×24 grid at 1.5px, <code class="t-code">currentColor</code> '
         'only — briefcase, graduation cap, calendar, phone and download.')
r += tile('<div class="cluster" style="gap:var(--space-5);flex-wrap:wrap">' + ''.join(
    f'<span style="display:grid;gap:var(--space-2);justify-items:center;width:5.5rem">'
    f'{resume.icon(n, group="resume")}'
    f'<span class="t-slate-sm" style="color:var(--fg-faint)">{n}</span></span>'
    for n in ['briefcase', 'graduation-cap', 'calendar', 'phone', 'download'])
    + '</div>', '<b>icons/resume/</b> — inline them, or use a sprite when you need theming')
r += END

PAGES['resume/index'] = ('Resume collection',
    'The fourth collection, and a single page rather than five routes: a full-width summary, '
    'then experience, education and projects beside a skills rail — none of it a new '
    'component, all of it .col-order, .card and .badge.', r)


# ── 8 · webseries ─────────────────────────────────────────────────────────────

w = ''
w += p('The fifth collection, and it ships no CSS of its own — a second proof, after blog, '
       'that the shared vocabulary is not secretly shaped like the collection that built it. '
       'Course justified five sections by saying a podcast season and a video series would '
       'want them too; this is that video series, over the same five routes travel already '
       'established.')
w += p('<a class="btn btn-primary btn-sm" href="/collection/webseries/index.html" '
       'target="_blank" rel="noopener">Open /webseries →</a> '
       '<a class="btn btn-primary btn-sm" href="/collection/webseries/episode.html" '
       'target="_blank" rel="noopener">Open the episode player →</a>')
w += END

w += sec('trending-w', 'The ranked row is a component that had never shipped',
         '<code class="t-code">.c-series</code> (letterbox bars) and <code class="t-code">.c-episode</code> '
         '(a big ghost numeral) are both listed in <code class="t-code">23-collection.css</code>\'s '
         'own table of every collection\'s card — webseries is the first route that actually '
         'renders one.')
w += live(webseries.trending_block(), '<b>.c.c-series.c-episode</b> — the numeral is '
    '<code class="t-code">.c__no</code>, nothing bespoke')
w += END

w += sec('season-w', 'A season is .col-order, again',
         'The same spine a trip or a resume\'s career history uses — a first episode, a '
         'last one, an order between them — over episodes instead of days or jobs.')
w += live('<div class="col-order">' + ''.join(
    f'<a class="col-order__item" href="#i"{" aria-current=\"page\"" if i == 0 else ""}>'
    f'<span class="col-order__num"><span class="col-order__dot"></span>{i+1:02d}</span>'
    f'<span class="col-order__body"><span class="col-order__title">{t}</span>'
    f'<span class="col-order__note">{note}</span></span></a>'
    for i, (t, note, _, _) in enumerate(webseries.SEASON_EPISODES[:3])) + '</div>',
    '<b>.col-order</b> — unmodified, from <code class="t-code">/webseries/…/season.html</code>')
w += END

w += sec('player-w', 'The episode player is course\'s stage, not its playlist',
         'Same <code class="t-code">.col-stage</code>, same <code class="t-code">.col-stagebar</code> '
         '— but the list beside the video is not course\'s curriculum wearing episode numbers. '
         '<code class="t-code">.ep-panel</code> and <code class="t-code">.episode</code> already '
         'existed, unused, as a generic composite demo with nowhere that actually needed a '
         'thumbnail next to every row. A season is exactly that place.')
w += live(webseries.episode_nav_block(), '<b>.ep-panel &gt; .episode</b> — moved here from the '
    'generic Composites demo, because this is what it was for')
w += END

w += sec('transcript-w', 'The transcript, unmodified',
         'The one panel every video-bodied post wants, whatever it is an episode of.')
w += live('<div class="col-transcript">' + ''.join(
    f'<a class="col-transcript__line" href="#i"{" aria-current=\"true\"" if i == 1 else ""}>'
    f'<span class="col-transcript__time">{t}</span><span>{line}</span></a>'
    for i, (t, line) in enumerate(webseries.TRANSCRIPT)) + '</div>',
    '<b>.col-transcript</b> — from <code class="t-code">/webseries/…/episode.html</code>, unchanged')
w += END

w += sec('cast-w', 'Cast is not a new component',
         'A resume needed a career history; a webseries needs a cast list. Both turn out to '
         'be a plain <code class="t-code">.list-group</code> — this one\'s rows just happen '
         'to start with <code class="t-code">.col-author__face</code>, the round avatar blog '
         'already built for its byline.')
w += live(webseries.cast_block(), '<b>.list-group + .col-author__face</b> — no wsr- prefix, '
    'because nothing here needed one')
w += END

PAGES['webseries/index'] = ('Webseries collection',
    'The fifth collection, and the second one to ship no CSS of its own — a season\'s spine '
    'and its cast are sections travel and blog already built, and its episode navigation is '
    'a composite that had been sitting unused until this collection needed exactly it.', w)
