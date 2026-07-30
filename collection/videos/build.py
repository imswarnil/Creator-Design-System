#!/usr/bin/env python3
"""Build the videos (YouTube) collection's two routes.

    python3 collection/videos/build.py

A channel, not a series: no seasons, no cast — just a hero that reads like a
channel banner (subscriber count, video count, total views) and a flat list
of uploads, newest first. The single video page borrows the course player
chrome (`.player`) and the transcript rail (`.col-transcript`) wholesale —
a chapter list is a transcript with fewer, longer lines, not a new component.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import (icon, ph, page, sec, hero, meta_strip, pagination,   # noqa: E402
                   comments, LIKE_SCRIPT)

NAME = 'Videos'

CHANNEL = {
    'name': 'Swarnil builds',
    'handle': '@swarnilbuilds',
    'subs': '18.4K',
    'videos': 62,
    'views': '2.1M',
}

VIDEOS = [
    ('grid-in-six-minutes', 'CSS Grid in six minutes, no filler',
     'css layout', '6:14', '128K views', '2 weeks ago'),
    ('design-system-tour', 'Building a design system live — full tour',
     'design-system', '34:02', '41K views', '3 weeks ago'),
    ('token-tier-explained', 'Why your tokens need three tiers, not one',
     'css tokens', '11:47', '76K views', '1 month ago'),
    ('view-transitions', 'Page transitions with zero JavaScript',
     'css motion', '9:23', '93K views', '1 month ago'),
    ('office-tour-2026', 'Where I actually build this (office tour)',
     'vlog', '15:08', '58K views', '2 months ago'),
    ('grid-vs-flex', 'Grid vs. Flexbox: stop guessing, use this rule',
     'css layout', '8:41', '204K views', '2 months ago'),
    ('build-a-navbar', 'Building the nav bar you are looking at right now',
     'css components', '18:55', '67K views', '3 months ago'),
    ('dark-mode-done-right', 'Dark mode without a second stylesheet',
     'css theming', '13:12', '112K views', '3 months ago'),
]

CHAPTERS = [
    ('0:00', 'The problem with one-column grids'),
    ('1:32', 'template-columns and minmax()'),
    ('3:05', 'The implicit grid, explained once and for all'),
    ('4:48', 'gap versus margin'),
    ('5:31', 'Shipping it'),
]

TAGS = ['css', 'grid', 'layout', 'tutorial']

PRODUCTS = [
    ('Sony ZV-E10', 'Camera', 'camera'),
    ('Rode NT-USB Mini', 'Microphone', 'mic'),
    ('Final Cut Pro', 'Editing', 'play'),
    ('Elgato Key Light', 'Lighting', 'sun'),
]


def video_card(slug, title, tags, runtime, views, when):
    return f'''<a class="c c-video" href="./video.html" data-post data-tags="{tags}">
      <div class="c__media" data-runtime="{runtime}">{ph(slug, True)}
        <span class="c__play">{icon('play', 'icon', group='media')}</span></div>
      <div class="c__body">
        <h3 class="c__title">{title}</h3>
        <p class="c__meta">{views} · {when}</p>
      </div>
    </a>'''


def videos_block(limit=None):
    rows = VIDEOS[:limit] if limit else VIDEOS
    return '<div class="grid-auto-sm">' + ''.join(
        video_card(*v) for v in rows) + '</div>'


def products_block():
    items = ''.join(
        f'<a class="c c-product" href="#i">'
        f'<span class="c__thumb">{icon(i, "icon", group="media")}</span>'
        f'<div class="c__body"><span class="c__title">{name}</span>'
        f'<span class="t-slate-sm">{role}</span></div></a>'
        for name, role, i in PRODUCTS)
    return f'<div class="grid-auto-sm">{items}</div>'


def route_index():
    body = f'''
  {hero('Swarnil builds', 'Design systems, CSS and the occasional office tour — '
        'a new video most weeks, unscripted and unedited-for-length.',
        'YouTube channel', [(CHANNEL['subs'], 'subscribers'),
                             (str(CHANNEL['videos']), 'videos'),
                             (CHANNEL['views'], 'total views')],
        eyebrow_icon='live', pattern='pattern-glow')}

  <div class="container section-sm" data-collection>
    {sec('All videos', 'Newest first — 62 uploads and counting.')}
    {videos_block()}
    <div class="u-mt-6">{pagination(1, 8, href='./index.html', label='Videos')}</div>
  </div>'''
    return page(HERE, 'index.html', 'Videos — Swarnil',
                'Design systems, CSS and build videos — the full upload history.',
                body, NAME, current='videos')


def route_video():
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Videos</a> <span>/</span>
      <span>CSS Grid in six minutes, no filler</span>
    </nav>

    <div class="player">
      {ph('grid-in-six-minutes', True)}
      <button class="play" type="button">
        <span class="play__disc"></span><span class="u-sr-only">Play the video</span>
      </button>
      <div class="player__bar">
        <span class="player__time">0:00</span>
        <span class="player__rail"><span class="player__played" style="--value:0%"></span></span>
        <span class="player__time">6:14</span>
      </div>
    </div>

    <div class="col-stagebar">
      <div class="col-stagebar__where">
        <span class="col-stagebar__pos">
          <span>128K views</span><span>2 weeks ago</span>
        </span>
        <h1 class="t-h3" style="margin:0">CSS Grid in six minutes, no filler</h1>
      </div>
      <span class="cluster" style="gap:var(--space-2)">
        {''.join(f'<a class="col-tag" href="#i">{t}</a>' for t in TAGS)}
      </span>
    </div>

    <div class="grid-rail-left u-mt-8">
      <aside class="col-rail col-rail-sticky">
        <span class="t-slate-sm u-mb-2" style="color:var(--fg-faint)">Chapters</span>
        <div class="col-transcript">
          {''.join(f'<a class="col-transcript__line" href="#i"'
                   f'{" aria-current=\"true\"" if i == 0 else ""}>'
                   f'<span class="col-transcript__time">{t}</span><span>{line}</span></a>'
                   for i, (t, line) in enumerate(CHAPTERS))}
        </div>
      </aside>

      <div>
        <article class="content">
          <p>Four properties are the whole system: <code>grid-template-columns</code>,
            <code>minmax()</code>, <code>gap</code> and the implicit grid. This is
            those four, in the order you actually reach for them, with nothing
            padded out to hit a run time.</p>
        </article>

        <div class="u-mt-10">
          {sec('More uploads')}
          {videos_block(limit=4)}
        </div>

        <div class="u-mt-10">
          {sec('Products I use to make these videos')}
          {products_block()}
        </div>
      </div>
    </div>
  </div>
  {comments(wrap=True)}{LIKE_SCRIPT}'''
    return page(HERE, 'video.html', 'CSS Grid in six minutes, no filler — Videos — Swarnil',
                'Four properties are the whole grid system — chaptered, six minutes.',
                body, NAME, current='videos')


if __name__ == '__main__':
    made = [route_index(), route_video()]
    print('videos: ' + ', '.join(made))
