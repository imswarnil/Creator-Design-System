#!/usr/bin/env python3
"""The default collection — the starting point for a new one.

    cp -r collection/_default collection/<name>

Five routes with nothing collection-specific in them: no globe, no widgets, no
subject. Copy the folder, rename it, change the data at the top, and you have a
working collection before you have designed anything.

It also serves as the reference: if a section works here, with no collection
CSS of its own, it is genuinely shared.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import icon, ph, page, sec, hero, meta_strip   # noqa: E402

# ── Change these four lists and the collection is yours ─────────────────────

NAME = 'Collection'
GROUPS = [('one', 'Group one', 'globe', 4), ('two', 'Group two', 'compass', 3),
          ('three', 'Group three', 'mountain', 2)]
PLACES = [('alpha', 'Alpha', 'one', 'A sentence about this place.', 'kind-a', 5),
          ('beta', 'Beta', 'one', 'A sentence about this place.', 'kind-b', 3),
          ('gamma', 'Gamma', 'two', 'A sentence about this place.', 'kind-a', 4),
          ('delta', 'Delta', 'three', 'A sentence about this place.', 'kind-c', 2)]
SPOTS = [('a1', 'Spot A1', 'alpha', 'kind-a', 3), ('a2', 'Spot A2', 'alpha', 'kind-b', 2),
         ('g1', 'Spot G1', 'gamma', 'kind-a', 4), ('d1', 'Spot D1', 'delta', 'kind-c', 1)]
FACETS = [('kind-a', 'Kind A', 'pin', 9), ('kind-b', 'Kind B', 'route', 6),
          ('kind-c', 'Kind C', 'compass', 4)]
POSTS = [('The first post', 'alpha', 'one', 'kind-a', '6 min'),
         ('The second post', 'gamma', 'two', 'kind-a', '9 min'),
         ('The third post', 'beta', 'one', 'kind-b', '4 min'),
         ('The fourth post', 'delta', 'three', 'kind-c', '11 min')]
SERIES = [('Part one', 'What happens first.'), ('Part two', 'What happens next.'),
          ('Part three', 'How it ends.')]


def groups_block():
    return '<div class="col-groups">' + ''.join(
        f'<button class="col-group" type="button" data-group="{s}" aria-pressed="false">'
        f'<span class="col-group__ico">{icon(i)}</span>'
        f'<span><span class="col-group__name">{n}</span>'
        f'<span class="col-group__n">{c} places</span></span></button>'
        for s, n, i, c in GROUPS) + '</div>'


def places_block():
    return '<div class="col-places">' + ''.join(
        f'<button class="col-place" type="button" data-place="{s}" data-of="{of}" '
        f'data-tags="{tags}" aria-pressed="false">'
        f'<span class="col-place__media">{ph(s)}</span>'
        f'<span class="col-place__body"><span class="col-place__name">{n}</span>'
        f'<span class="col-place__note">{note}</span></span>'
        f'<span class="col-place__foot"><span>{c} posts</span></span></button>'
        for s, n, of, note, tags, c in PLACES) + (
        '<p class="col-empty" data-empty-for="[data-place]" hidden>Nothing here.</p></div>')


def spots_block():
    return '<div class="col-spots">' + ''.join(
        f'<a class="col-spot" href="./place.html" data-spot="{s}" data-of="{of}" '
        f'data-tags="{tags}">{n}<span class="col-spot__n">{c}</span></a>'
        for s, n, of, tags, c in SPOTS) + (
        '<p class="col-empty" data-empty-for="[data-spot]" hidden>Nothing here.</p></div>')


def facets_block():
    return f'''
    <aside class="col-layout__side">
      <div class="col-facets">
        <div class="col-facets__group">
          <span class="col-facets__title">Filtering</span>
          <p class="t-small u-fg-subtle" data-filter-state>Everything</p>
          <button class="btn btn-quiet btn-sm" type="button" data-filter-reset hidden>
            Clear filters</button>
        </div>
        <div class="col-facets__group">
          <span class="col-facets__title">Kind</span>
          {''.join(f'<label class="col-facet"><input type="checkbox" data-facet="{s}" />'
                   f'{icon(i)}<span>{n}</span><span class="col-facet__n">{c}</span></label>'
                   for s, n, i, c in FACETS)}
        </div>
      </div>
    </aside>'''


def posts_block(limit=None):
    rows = ''.join(
        f'<a class="col-post-row" href="./post.html" data-post data-of="{of}" '
        f'data-region="{g}" data-tags="{tags}">'
        f'<span class="col-post-row__thumb">{ph(of)}</span>'
        f'<span class="col-post-row__body"><span class="col-post-row__title">{t}</span>'
        f'<span class="col-post-row__note">{tags}</span></span>'
        f'<span class="col-post-row__meta"><span>{read}</span></span></a>'
        for t, of, g, tags, read in (POSTS[:limit] if limit else POSTS))
    return ('<div class="col-posts">' + rows +
            '<p class="col-empty" data-empty-for="[data-post]" hidden>'
            'Nothing matches. Try clearing a filter.</p></div>')


def series_card():
    return f'''
    <a class="col-series" href="./series.html">
      <span class="col-series__media">{ph('default', True)}</span>
      <span class="col-series__body">
        <span class="col-hero__eyebrow" style="color:var(--fg-faint)">{icon('route')}A series</span>
        <span class="col-series__title">Something made as one body of work</span>
        <span class="t-small u-fg-subtle">A series has a first, a last and an order.
          A group has none of those — that is the whole difference.</span>
        <span class="col-series__stats"><span>{icon('route')}3 parts</span></span>
      </span>
    </a>'''


CRUMBS = ('<nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">'
          '<a href="./index.html">{name}</a> <span>/</span> <span>{here}</span></nav>')


# A dummy screenshot — a card, a header row, two content blocks, three lines
# and a button — every shape drawn in tokens, so it re-themes with the page
# instead of shipping as a fixed-colour PNG. Stands in for wherever a real
# product shot goes once the collection has one.
STAGE_ART = '''
<svg viewBox="0 0 400 300" fill="none" xmlns="http://www.w3.org/2000/svg"
     aria-hidden="true" focusable="false" style="width:100%;height:100%;display:block">
  <rect x="0.5" y="0.5" width="399" height="299" rx="12" fill="var(--bg-surface)" stroke="var(--line-default)"/>
  <circle cx="34" cy="34" r="6" fill="var(--line-strong)"/>
  <rect x="52" y="30" width="90" height="8" rx="4" fill="var(--line-strong)"/>
  <rect x="20" y="60" width="360" height="1" fill="var(--line-subtle)"/>
  <rect x="20" y="80" width="170" height="104" rx="8" fill="var(--accent-soft)"/>
  <rect x="200" y="80" width="180" height="48" rx="8" fill="var(--bg-sunken)"/>
  <rect x="200" y="136" width="180" height="48" rx="8" fill="var(--bg-sunken)"/>
  <rect x="20" y="200" width="110" height="10" rx="5" fill="var(--line-default)"/>
  <rect x="20" y="220" width="360" height="8" rx="4" fill="var(--line-subtle)"/>
  <rect x="20" y="236" width="300" height="8" rx="4" fill="var(--line-subtle)"/>
  <rect x="20" y="258" width="92" height="26" rx="13" fill="var(--accent)"/>
</svg>
'''


def route_index():
    body = f'''
  <div class="container">
    <section class="hero hero-split hero-sm pattern pattern-grid pattern-lg fade-corners"
             style="padding-block:var(--space-10) var(--space-8);border-radius:var(--radius-sheet);
                    max-width:calc(var(--w-site) - 4rem);margin-inline:auto">
      <div>
        <span class="hero__eyebrow">{icon('pin')}Index</span>
        <h1 class="hero__title">The collection</h1>
        <p class="hero__lead">One sentence saying what is in here and why anyone would
          read it. Replace this, the data at the top of build.py, and you have a
          collection.</p>
        <div class="hero__actions">
          <form onsubmit="return false" style="max-width:26rem">
            <div class="input-group">
              <input class="input" type="search" placeholder="Search this collection"
                     aria-label="Search this collection" />
              <button class="btn btn-primary" type="submit">Search</button>
            </div>
          </form>
        </div>
        {meta_strip([('14', 'posts'), ('4', 'places'), ('3', 'groups'), ('1', 'series')],
                    paper=True, border=False, inline=True)}
      </div>
      <div class="hero-split__stage">
        <div class="frame frame-4 frame-ink" style="aspect-ratio:4/3">
          <span class="frame__tr"></span><span class="frame__bl"></span>
          {STAGE_ART}
        </div>
        <p class="hero-split__caption">Dummy placeholder <span>SVG · swap for a real shot</span></p>
      </div>
    </section>
  </div>'''
    body += f'''
  <div data-collection>
  <section class="container section-sm">
    {sec('Groups', 'The widest cut. Pick one and everything below narrows to it.')}
    {groups_block()}
  </section>
  <section class="container section-sm">
    <div class="col-layout">
      {facets_block()}
      <div>
        {sec('Places')}{places_block()}
        <div class="u-mt-10">{sec('Spots')}{spots_block()}</div>
        <div class="u-mt-10">{sec('Latest series')}{series_card()}</div>
        <div class="u-mt-10">{sec('Everything')}{posts_block()}</div>
      </div>
    </div>
  </section>
  </div>'''
    return page(HERE, 'index.html', f'{NAME} — the default collection',
                'The starting point for a new collection.', body, NAME)


def route_group():
    body = hero('Group one', 'A group is an unordered set that share an attribute. Same '
                'sections as the index, fewer things in them.', 'Group',
                [('7', 'posts'), ('2', 'places')])
    body += f'''
  <div data-collection>
  <section class="container section-sm">
    {CRUMBS.format(name=NAME, here='Group one')}
    <div class="col-layout">
      {facets_block()}
      <div>
        {sec('Places in this group')}{places_block()}
        <div class="u-mt-10">{sec('Posts')}{posts_block()}</div>
      </div>
    </div>
  </section>
  </div>'''
    return page(HERE, 'group.html', f'Group — {NAME}', 'One cut already made.', body, NAME)


def route_place():
    body = hero('Alpha', 'A place is one thing the collection is about. Its spots, its '
                'series, and its posts.', 'Place · Group one',
                [('5', 'posts'), ('2', 'spots')])
    body += f'''
  <section class="container section-sm">
    {CRUMBS.format(name=NAME, here='Alpha')}
    {sec('Spots')}<div class="u-mb-10">{spots_block()}</div>
    {sec('Series here')}<div class="u-mb-10">{series_card()}</div>
    {sec('Posts')}{posts_block()}
  </section>'''
    return page(HERE, 'place.html', f'Alpha — {NAME}', 'One place.', body, NAME)


def route_series():
    items = ''.join(
        f'<a class="col-order__item" href="./post.html"'
        f'{chr(32) + chr(97) + "ria-current=" + chr(34) + "page" + chr(34) if i == 1 else ""}>'
        f'<span class="col-order__num"><span class="col-order__dot"></span>{i+1:02d}</span>'
        f'<span class="col-order__body"><span class="col-order__title">{t}</span>'
        f'<span class="col-order__note">{note}</span></span></a>'
        for i, (t, note) in enumerate(SERIES))
    body = hero('A series', 'An ordered body of work. It has a first, a last, and a '
                'progress through it — which is why it gets a spine and not a grid.',
                'Series', [('3', 'parts')], eyebrow_icon='route')
    body += f'''
  <section class="container section-sm">
    {CRUMBS.format(name=NAME, here='A series')}
    {sec('In order')}
    <div class="col-order">{items}</div>
  </section>'''
    return page(HERE, 'series.html', f'A series — {NAME}', 'An ordered body of work.',
                body, NAME)


def route_post():
    body = f'''
  <article class="container section-sm">
    <header class="col-post__head">
      <nav class="col-post__crumbs" aria-label="Breadcrumb">
        <a href="./index.html">{NAME}</a> <span>/</span>
        <a href="./series.html">A series</a> <span>/</span> <span>Part 2</span>
      </nav>
      <h1 class="t-display-2">The post itself</h1>
      <p class="t-lead" style="max-width:var(--measure-lead)">The standfirst sits here.</p>
      <div class="col-post__crumbs"><span>6 min read</span> <span>·</span>
        <span>Part 2 of 3</span></div>
    </header>
    <div class="surface u-mb-8" style="aspect-ratio:16/9;overflow:hidden;border-radius:var(--radius-card)">
      {ph('default', True)}
    </div>
    <div class="col-post">
      <div class="content">
        <p>The body of the post. Everything in here is the system's long-form content
          styling — this collection adds nothing to it.</p>
        <h2>A heading</h2>
        <p>And a paragraph under it.</p>
      </div>
      <aside class="col-post__rail col-rail">
        <div class="col-widget">
          <span class="col-widget__title">Part of</span>
          <a class="col-order__title" href="./series.html">A series</a>
          <p class="t-small u-fg-subtle">Part 2 of 3</p>
        </div>
        <div class="col-widget">
          <span class="col-widget__title">Filed under</span>
          <div class="col-tags">
            <a class="col-tag" href="#i">Kind A</a>
            <a class="col-tag" href="#i">Alpha</a>
          </div>
        </div>
      </aside>
    </div>
    <a class="col-next u-mt-10" href="#i">
      <span class="col-next__label">Next · Part 3</span>
      <span class="col-order__title">How it ends</span>
    </a>
  </article>'''
    return page(HERE, 'post.html', f'The post — {NAME}', 'A single post.', body, NAME)


if __name__ == '__main__':
    made = [route_index(), route_group(), route_place(), route_series(), route_post()]
    print('default: ' + ', '.join(made))
