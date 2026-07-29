#!/usr/bin/env python3
"""Build the webseries collection's five routes.

    python3 collection/webseries/build.py

The fifth collection, and it ships no CSS of its own — a second proof, after
blog, that the shared vocabulary is not secretly shaped like the collection
that built it. Course justified the stage, the stage bar, the playlist, the
transcript and the panels by saying "a podcast season and a video series want
every one of them"; this is that video series, reusing all five unchanged.
The one new thing a season needed — a cast list — turns out to be a plain
.list-group with an avatar in it, not a new component either.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import icon, ph, page, sec, hero, meta_strip   # noqa: E402

NAME = 'Webseries'

GENRES = [
    ('comedy', 'Comedy', 'chat', 2),
    ('drama', 'Drama', 'heart', 2),
    ('docuseries', 'Docuseries', 'camera', 1),
]

SHOWS = [
    ('after-hours', 'After Hours', 'comedy',
     'A late-night writers room that never agreed on the ending.',
     'comedy city', 12, 'TV-14'),
    ('night-shift', 'Night Shift', 'comedy',
     'Four baristas, one espresso machine that hates them.',
     'comedy party', 10, 'TV-14'),
    ('the-quiet-year', 'The Quiet Year', 'drama',
     'A small town\'s year, told one season per resident.',
     'drama city', 8, 'TV-MA'),
    ('static', 'Static', 'drama',
     'A radio station\'s last year broadcasting on analog.',
     'drama', 5, 'TV-MA'),
    ('borders', 'Borders', 'docuseries',
     'Six countries, one train line, nothing scripted.',
     'docuseries mountains', 6, 'TV-PG'),
]

SEASONS = [
    ('after-hours-s1', 'Season 1', 'after-hours', 'comedy city', 6),
    ('after-hours-s2', 'Season 2', 'after-hours', 'comedy city', 6),
    ('night-shift-s1', 'Season 1', 'night-shift', 'comedy party', 10),
    ('quiet-year-s1', 'Season 1', 'the-quiet-year', 'drama city', 8),
    ('borders-s1', 'Season 1', 'borders', 'docuseries mountains', 6),
]

FACETS = [
    ('comedy', 'Comedy', 'chat', 22),
    ('drama', 'Drama', 'heart', 13),
    ('docuseries', 'Docuseries', 'camera', 6),
    ('new', 'New episodes', 'rec', 9),
]

EPISODES = [
    ('The Pitch That Almost Worked', 'after-hours', 'comedy',
     'comedy city', '24 min', 'Jul 2026'),
    ('Two Truths and a Layoff', 'night-shift', 'comedy',
     'comedy party', '22 min', 'Jul 2026'),
    ('The Last Broadcast', 'static', 'drama', 'drama', '31 min', 'Jun 2026'),
    ('Crossing at Dawn', 'borders', 'docuseries',
     'docuseries mountains', '40 min', 'Jun 2026'),
    ('What the Rain Knew', 'the-quiet-year', 'drama',
     'drama city', '29 min', 'May 2026'),
    ('Espresso Shot', 'night-shift', 'comedy', 'comedy party', '21 min', 'Apr 2026'),
]

SEASON_EPISODES = [
    ('The Pitch That Almost Worked',
     'The room agrees on nothing except the coffee order.', '24 min', 'slate'),
    ('Two Truths and a Layoff',
     'Someone is definitely lying about the inventory count.', '22 min', 'chat'),
    ('The Meeting That Should Have Been an Email',
     'Forty minutes, one decision, and it was the wrong one.', '19 min', 'slate'),
    ('Cold Open', 'The pilot\'s closing bit gets the callback it earned.', '23 min', 'rec'),
    ('The One With No Punchline',
     'The season\'s only bottle episode, and its best one.', '26 min', 'slate'),
    ('Season Finale: Last Call',
     'Every thread from the first five episodes, paid off in one long shift.',
     '30 min', 'rec'),
]

CAST = [
    ('Priya Nair', 'Dana Cho — head writer'),
    ('Marcus Webb', 'Tom Ellery — staff writer'),
    ('Yuki Tanaka', 'Sam Park — showrunner\'s assistant'),
    ('Elena Brandt', 'Ruth Okafor — network exec'),
]

TRANSCRIPT = [
    ('0:00', 'Cold open — the room, mid-argument.'),
    ('2:14', 'Dana pitches the ending nobody asked for.'),
    ('6:40', 'Tom threatens to quit for the third time this season.'),
    ('11:05', 'Sam finds the note that changes the pitch.'),
    ('18:30', 'The room agrees on nothing except the coffee order.'),
]

# A still frame standing in for a paused trailer — a gradient rather than a
# stock photo, with the scanline texture already in the system laid over it.
# No new CSS: .pattern-scanline + .pattern-media both exist, just never asked
# to cover a whole hero before.
HERO_ART = '''
  <div class="col-hero__art" aria-hidden="true" style="background:
       linear-gradient(180deg, rgb(10 8 20 / 0.35), rgb(6 4 12 / 0.94) 70%),
       radial-gradient(ellipse 60% 50% at 25% 15%, hsl(262 45% 24%), transparent 60%),
       radial-gradient(ellipse 50% 60% at 85% 70%, hsl(340 40% 20%), transparent 55%),
       hsl(230 30% 6%)">
    <div class="pattern pattern-scanline pattern-media pattern-lg" style="position:absolute;inset:0"></div>
  </div>
'''


def genres_block():
    return '<div class="col-groups">' + ''.join(
        f'<button class="col-group" type="button" data-group="{slug}" aria-pressed="false">'
        f'<span class="col-group__ico">{icon(ico, group="social" if ico in ("chat", "heart") else "media")}</span>'
        f'<span><span class="col-group__name">{name}</span>'
        f'<span class="col-group__n">{n} show{"" if n == 1 else "s"}</span></span></button>'
        for slug, name, ico, n in GENRES) + '</div>'


def shows_block(genre=None):
    rows = SHOWS if not genre else [s for s in SHOWS if s[2] == genre]
    out = ['<div class="col-places">']
    for slug, name, g, note, tags, n, rating in rows:
        out.append(
            f'<button class="col-place" type="button" data-place="{slug}" data-of="{g}" '
            f'data-tags="{tags}" aria-pressed="false">'
            f'<span class="col-place__media">{ph(slug)}'
            f'<span class="col-place__tag">{rating}</span></span>'
            f'<span class="col-place__body"><span class="col-place__name">{name}</span>'
            f'<span class="col-place__note">{note}</span></span>'
            f'<span class="col-place__foot"><span>{n} episodes</span>'
            f'<span>{tags.split()[0]}</span></span></button>')
    out.append('<p class="col-empty" data-empty-for="[data-place]" hidden>'
               'No show matches that combination.</p>')
    return '\n'.join(out) + '</div>'


def seasons_block(show=None):
    rows = SEASONS if not show else [s for s in SEASONS if s[2] == show]
    out = ['<div class="col-spots">']
    for slug, name, of, tags, n in rows:
        out.append(f'<a class="col-spot" href="./season.html" data-spot="{slug}" '
                   f'data-of="{of}" data-tags="{tags}">{name}'
                   f'<span class="col-spot__n">{n}</span></a>')
    out.append('<p class="col-empty" data-empty-for="[data-spot]" hidden>'
               'No season under that filter yet.</p>')
    return '\n'.join(out) + '</div>'


def facets_block():
    rows = ''.join(
        f'<label class="col-facet"><input type="checkbox" data-facet="{slug}" />'
        f'{icon(ico, group="social" if ico in ("chat", "heart") else ("media" if ico in ("camera", "rec") else "creator"))}'
        f'<span>{name}</span><span class="col-facet__n">{n}</span></label>'
        for slug, name, ico, n in FACETS)
    return f'''
    <aside class="col-layout__side">
      <div class="col-facets">
        <div class="col-facets__group">
          <span class="col-facets__title">Filtering</span>
          <p class="t-small u-fg-subtle" data-filter-state>Everything</p>
          <button class="btn btn-quiet btn-sm" type="button" data-filter-reset hidden>
            Clear filters
          </button>
        </div>
        <div class="col-facets__group">
          <span class="col-facets__title">Genre &amp; new</span>
          {rows}
        </div>
      </div>
    </aside>'''


def episodes_block(limit=None):
    rows = []
    for title, show, genre, tags, length, when in (EPISODES[:limit] if limit else EPISODES):
        rows.append(
            f'<a class="col-post-row" href="./episode.html" data-post data-of="{show}" '
            f'data-region="{genre}" data-tags="{tags}">'
            f'<span class="col-post-row__thumb">{ph(show)}</span>'
            f'<span class="col-post-row__body">'
            f'<span class="col-post-row__title">{title}</span>'
            f'<span class="col-post-row__note">{tags.replace(" ", " · ")}</span></span>'
            f'<span class="col-post-row__meta"><span>{length}</span><span>{when}</span></span></a>')
    rows.append('<p class="col-empty" data-empty-for="[data-post]" hidden>'
                'No episode matches. Try clearing a filter.</p>')
    return '<div class="col-posts">' + '\n'.join(rows) + '</div>'


TRENDING = [
    ('The Pitch That Almost Worked', 'after-hours', 'Comedy · After Hours', '24 min'),
    ('Crossing at Dawn', 'borders', 'Docuseries · Borders', '40 min'),
    ('What the Rain Knew', 'the-quiet-year', 'Drama · The Quiet Year', '29 min'),
    ('Two Truths and a Layoff', 'night-shift', 'Comedy · Night Shift', '22 min'),
    ('The Last Broadcast', 'static', 'Drama · Static', '31 min'),
]


def trending_block():
    """.c-series + .c-episode already existed for exactly this: a dark,
    letterboxed card with a big ghost numeral — the ranking Netflix's Top 10
    row draws, built from a component that had never been used yet."""
    cards = ''.join(
        f'<article class="c c-series c-episode">'
        f'<div class="c__media">{ph(show)}<span class="c__no">{i + 1}</span></div>'
        f'<div class="c__body"><span class="c__meta">{meta}</span>'
        f'<h3 class="c__title"><a class="c__link" href="./episode.html">{title}</a></h3></div>'
        f'<div class="c__foot"><span>{length}</span></div>'
        f'</article>'
        for i, (title, show, meta, length) in enumerate(TRENDING))
    return f'<div class="grid-auto-sm">{cards}</div>'


def season_card(show='after-hours'):
    stats = ''.join(f'<span>{icon(i, group="creator" if i in ("slate", "rec") else "media")}{t}</span>'
                    for i, t in [('slate', '6 episodes'), ('rec', 'New'), ('play', '2h 25m')])
    return f'''
    <a class="col-series" href="./season.html">
      <span class="col-series__media">{ph(show, True)}</span>
      <span class="col-series__body">
        <span class="col-hero__eyebrow" style="color:var(--fg-faint)">
          {icon('slate', group='creator')}Latest season</span>
        <span class="col-series__title">After Hours, Season 1</span>
        <span class="t-small u-fg-subtle">A season is a series: a first episode, a
          last one, and an order that matters — so it gets a spine, not a grid.</span>
        <span class="col-series__stats">{stats}</span>
      </span>
    </a>'''


def cast_block():
    rows = ''.join(
        f'<div class="list-group__item"><span class="col-author__face">{ph(name)}</span>'
        f'<span><b>{name}</b>'
        f'<span class="t-small u-fg-subtle" style="display:block">{role}</span></span></div>'
        for name, role in CAST)
    return f'<div class="list-group">{rows}</div>'


PATTERNS = ['pattern-grid', 'pattern-hatch', 'pattern-dots', 'pattern-scanline']


def episode_nav_block():
    """The list beside the player — a webseries' own navigation, not course's
    curriculum wearing a costume. .ep-panel + .episode already existed as an
    unused composite; this is what it was for."""
    rows = ''.join(
        f'<a class="episode" href="./episode.html"{" aria-current=\"true\"" if i == 0 else ""}>'
        f'<span class="episode__thumb pattern {PATTERNS[i % len(PATTERNS)]} pattern-media"></span>'
        f'<span><span class="episode__title">{title}</span>'
        f'<span class="episode__meta">Ep.{i + 1:02d} · {length}</span></span></a>'
        for i, (title, _, length, _) in enumerate(SEASON_EPISODES))
    return f'''
      <div class="ep-panel">
        <header class="ep-panel__head">
          <span class="ep-panel__title">After Hours — Season 1</span>
          <span class="ep-panel__count">{len(SEASON_EPISODES)} episodes</span>
        </header>
        <div class="ep-panel__list">{rows}</div>
      </div>'''


# ── 1 · /webseries — the collection index ───────────────────────────────────

def route_index():
    body = hero(
        'Every show, <em>in order</em>.',
        'Five shows, thirty-two episodes, and nothing to skip ahead to unless '
        'you already finished the season before it. Start with a genre, or pick '
        'up the latest one.',
        'The webseries collection',
        [('5', 'shows'), ('7', 'seasons'), ('32', 'episodes'), ('3', 'genres')],
        search='Search shows and episodes', eyebrow_icon='slate',
        art=HERO_ART, full=True)

    body += f'''
  <section class="container section-sm">
    {sec('Trending now', 'The five most-watched episodes this week, ranked.')}
    {trending_block()}
  </section>

  <div data-collection>
  <section class="container section-sm">
    {sec('Genres', 'The widest cut. Pick one and everything below narrows to it.')}
    {genres_block()}
  </section>

  <section class="container section-sm">
    <div class="col-layout">
      {facets_block()}
      <div>
        {sec('Shows', 'Selecting a show narrows the seasons and the episodes.')}
        {shows_block()}

        <div class="u-mt-10">
          {sec('Seasons', 'The narrowest cut — where the spine actually starts.')}
          {seasons_block()}
        </div>

        <div class="u-mt-10" id="seasons">
          {sec('Now streaming')}
          {season_card()}
        </div>

        <div class="u-mt-10">
          {sec('Featured', 'The three worth starting with.')}
          {episodes_block(limit=3)}
        </div>

        <div class="u-mt-10">
          {sec('All new episodes')}
          {episodes_block()}
        </div>
      </div>
    </div>
  </section>
  </div>
'''
    return page(HERE, 'index.html', 'Webseries — Swarnil',
                'Five shows, thirty-two episodes, watched in order.',
                body, NAME, current='webseries')


# ── 2 · /webseries/comedy — a group ──────────────────────────────────────────

def route_genre():
    shows = [s for s in SHOWS if s[2] == 'comedy']
    body = hero(
        'Comedy', 'Two shows so far, twenty-two episodes, and a shared belief '
        'that a cold open should never explain the joke. The genre page is the '
        'same collection with one cut already made.',
        'Genre', [('22', 'episodes'), ('2', 'shows'), ('2', 'seasons')],
        search=None)

    body += f'''
  <section class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Webseries</a> <span>/</span> <span>Comedy</span>
    </nav>
    <div class="col-layout" data-collection>
      {facets_block()}
      <div>
        {sec('Comedy shows')}
        {shows_block('comedy')}

        <div class="u-mt-10">
          {sec('Seasons')}
          {seasons_block('after-hours')}
        </div>

        <div class="u-mt-10">
          {sec('Episodes')}
          {episodes_block()}
        </div>
      </div>
    </div>
  </section>
'''
    return page(HERE, 'genre.html', 'Comedy — Webseries — Swarnil',
                'Every comedy show and episode.', body, NAME,
                current='webseries')


# ── 3 · /webseries/after-hours — a place ─────────────────────────────────────

def route_show():
    seasons = [s for s in SEASONS if s[2] == 'after-hours']
    body = hero(
        'After Hours', 'Twelve episodes, two seasons, and a writers room that '
        'has never once agreed on an ending on the first try.', 'Show · Comedy',
        [('12', 'episodes'), ('2', 'seasons'), ('TV-14', 'rating')],
        search=None)

    body += f'''
  <section class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Webseries</a> <span>/</span>
      <a href="./genre.html">Comedy</a> <span>/</span> <span>After Hours</span>
    </nav>

    {sec('Seasons', 'Where the episodes actually live.')}
    <div class="col-places u-mb-10">
      {''.join(f"""<a class="col-place" href="./season.html">
        <span class="col-place__media">{ph('after-hours')}</span>
        <span class="col-place__body"><span class="col-place__name">{name}</span>
        <span class="col-place__note">{n} episodes</span></span>
      </a>""" for _, name, _, _, n in seasons)}
    </div>

    {sec('Cast', 'Recurring, in order of the credits.')}
    <div class="u-mb-10" style="max-width:28rem">{cast_block()}</div>

    {sec('Now streaming')}
    <div class="u-mb-10">{season_card()}</div>

    {sec('All episodes')}
    {episodes_block()}
  </section>
'''
    return page(HERE, 'show.html', 'After Hours — Webseries — Swarnil',
                'Every episode of After Hours.', body, NAME,
                current='webseries')


# ── 4 · /webseries/after-hours/season-1 — a series ───────────────────────────

def route_season():
    items = '\n'.join(
        f'<a class="col-order__item" href="./episode.html"{" aria-current=\"page\"" if i == 0 else ""}>'
        f'<span class="col-order__num"><span class="col-order__dot"></span>{i + 1:02d}</span>'
        f'<span class="col-order__body">'
        f'<span class="col-order__title">{title}</span>'
        f'<span class="col-order__note">{note}</span>'
        f'<span class="col-order__meta"><span>{icon(ico, group="creator")}</span><span>{length}</span></span>'
        f'</span></a>'
        for i, (title, note, length, ico) in enumerate(SEASON_EPISODES))

    body = hero(
        'After Hours,<br>Season 1',
        'A season is a series: it has a first episode, a last one, and an '
        'order that matters. Watch it in order, or jump to the one you came for.',
        'Season · 2026', [('6', 'episodes'), ('2h 25m', 'runtime'), ('TV-14', 'rating')],
        search=None)

    body += f'''
  <section class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Webseries</a> <span>/</span>
      <a href="./show.html">After Hours</a> <span>/</span> <span>Season 1</span>
    </nav>

    <div class="col-layout">
      <aside class="col-layout__side">
        <div class="col-facets">
          <div class="col-facets__group">
            <span class="col-facets__title">In this season</span>
            {''.join(f'<a class="col-facet" href="#i">{icon(ico, group="creator")}<span>{title[:26]}…</span></a>' for title, _, _, ico in SEASON_EPISODES)}
          </div>
        </div>
      </aside>
      <div>
        {sec('Season 1, in order', 'Every episode made as part of this one body of work.')}
        <div class="col-order">{items}</div>
      </div>
    </div>
  </section>
'''
    return page(HERE, 'season.html', 'After Hours, Season 1 — Webseries — Swarnil',
                'A season: six episodes, in the order they aired.', body, NAME,
                current='webseries')


# ── 5 · an episode ───────────────────────────────────────────────────────────

def route_episode():
    tabs = [('overview', 'Overview'), ('transcript', 'Transcript'), ('cast', 'Cast')]

    body = f'''
  <div data-player>
  <section class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Webseries</a> <span>/</span>
      <a href="./show.html">After Hours</a> <span>/</span>
      <a href="./season.html">Season 1</a> <span>/</span> <span>Ep 1</span>
    </nav>

    <div class="col-stage">
      <div class="col-stage__main">
        <div class="player">
          {ph('after-hours', True)}
          <button class="play" type="button">
            <span class="play__disc"></span><span class="u-sr-only">Play the episode</span>
          </button>
          <div class="player__bar">
            <span class="player__time">6:40</span>
            <span class="player__rail"><span class="player__played" style="--value:28%"></span></span>
            <span class="player__time">24:00</span>
          </div>
        </div>

        <div class="col-stagebar">
          <a class="btn btn-secondary btn-sm" href="./episode.html" data-step="prev">
            ← Previous</a>
          <div class="col-stagebar__where">
            <span class="col-stagebar__pos">
              <span>Episode 1 of 6</span>
              <span>Season 1</span>
              <span>24 min</span>
            </span>
            <h1 class="t-h3" style="margin:0">The Pitch That Almost Worked</h1>
          </div>
          <a class="btn btn-primary btn-sm" href="./episode.html" data-step="next">
            Next →</a>
        </div>
      </div>

      <aside class="col-stage__side">
        {episode_nav_block()}
      </aside>
    </div>

    <div class="col-post u-mt-8">
      <div data-tabs>
        <div class="tabs" role="tablist" aria-label="About this episode">
          {''.join(f'<button class="tab" type="button" role="tab" id="t-{s}" '
                   f'aria-controls="p-{s}" aria-selected="{str(i == 0).lower()}">{n}</button>'
                   for i, (s, n) in enumerate(tabs))}
        </div>

        <div class="col-panel" id="p-overview" role="tabpanel" aria-labelledby="t-overview">
          <span class="col-panel__label">Overview</span>
          <div class="content">
            <p>The room has forty minutes to fix an ending nobody likes, and every
              option on the table makes somebody's least favorite character right.</p>
            <blockquote>
              <p>Dana pitches the ending nobody asked for — and by the cold open of
                episode two, it's the only one anyone remembers pitching.</p>
            </blockquote>
          </div>
        </div>

        <div class="col-panel" id="p-transcript" role="tabpanel" aria-labelledby="t-transcript">
          <span class="col-panel__label">Transcript</span>
          <div class="col-transcript">
            {''.join(f'<a class="col-transcript__line" href="#i"'
                     f'{" aria-current=\"true\"" if i == 1 else ""}>'
                     f'<span class="col-transcript__time">{t}</span><span>{line}</span></a>'
                     for i, (t, line) in enumerate(TRANSCRIPT))}
          </div>
        </div>

        <div class="col-panel" id="p-cast" role="tabpanel" aria-labelledby="t-cast">
          <span class="col-panel__label">Cast, this episode</span>
          {cast_block()}
        </div>
      </div>

      <aside class="col-post__rail col-rail col-rail-sticky">
        <div class="col-post__rail-card">
          <span class="col-facets__title">This episode is part of</span>
          <a class="col-order__title" href="./season.html">After Hours, Season 1</a>
          <p class="t-small u-fg-subtle">Episode 1 of 6</p>
          <a class="btn btn-secondary btn-sm" href="./season.html">See the whole season</a>
        </div>
      </aside>
    </div>

    <a class="col-next u-mt-10" href="./episode.html" data-step="next">
      <span class="col-next__label">Next · Episode 2</span>
      <span class="col-order__title">Two Truths and a Layoff</span>
      <span class="t-small u-fg-subtle">Someone is definitely lying about the
        inventory count.</span>
    </a>
  </section>
  </div>'''
    return page(HERE, 'episode.html', 'The Pitch That Almost Worked — After Hours',
                'The episode player: the video, the season playlist beside it, '
                'and the transcript under it.', body, NAME,
                current='webseries')


if __name__ == '__main__':
    made = [route_index(), route_genre(), route_show(), route_season(), route_episode()]
    print('webseries: ' + ', '.join(made))
