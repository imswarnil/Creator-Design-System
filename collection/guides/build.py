#!/usr/bin/env python3
"""Build the guides collection's three routes.

    python3 collection/guides/build.py

A guide is a post series with a spine: a book-styled index (`.c-guide`, a
cover on the left, step count on the right) and a single guide page that
gets a `.stepper` — a row of filled segments — riding above the same
`.col-stagebar` pager the course lesson player and single video page already
use to move between steps.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import icon, ph, page, sec, hero, meta_strip, pagination   # noqa: E402

NAME = 'Guides'

GUIDES = [
    ('grid-from-scratch', 'Grid, from scratch', 'css',
     'Every property, in the order you actually reach for them.', 6, 'course'),
    ('tokens-that-scale', 'Tokens that scale past one theme', 'motion',
     'Three tiers, one rename away from a client rebrand.', 5, 'take'),
    ('shipping-a-design-system', 'Shipping a design system solo', 'craft',
     'What to build first, and what to skip until someone asks.', 8, 'slate'),
    ('writing-css-that-lasts', 'Writing CSS that outlives the redesign', 'notes',
     'Cascade layers, semantic tiers, and the one rule about specificity.', 4, 'pen'),
]

STEPS = [
    ('The four properties', 'template-columns and minmax() are most of the layouts '
     'you will ever ship.'),
    ('The implicit grid', 'Rows you never declared, and where they come from.'),
    ('gap versus margin', 'Why margin mostly leaves the stylesheet once grid arrives.'),
    ('Alignment, two axes', 'align-items defaults to stretch — that is the whole trick.'),
    ('Naming areas', 'A readability decision, not a layout one.'),
    ('Shipping it', 'The checklist before a grid goes into a real page.'),
]


def guide_card(slug, title, seed, note, steps, ico):
    """The row card — a cover beside the copy, for the full list."""
    return f'''<a class="c c-guide" href="./guide.html">
      <div class="c__media">{ph(seed, tall=True, blend=True)}</div>
      <div class="c__body">
        <span class="c__meta">{icon(ico)}Guide</span>
        <h3 class="c__title">{title}</h3>
        <p class="c__excerpt">{note}</p>
        <span class="c__steps" style="--value:100%">{steps} steps</span>
      </div>
    </a>'''


def book_card(slug, title, seed, note, steps, ico):
    """The cover on its own — `.book`, whose own doc comment names the guides
    as what it is for. This collection shipped a bespoke `.guide-cover` before
    anyone noticed the foundation already had a spine, a page edge and a shelf."""
    hues = {'css': 262, 'motion': 190, 'craft': 24, 'notes': 96}
    h = hues.get(seed, 220)
    return f'''<a class="book hx-sheen" href="./guide.html"
       style="background:linear-gradient(155deg, hsl({h} 62% 32%), hsl({h + 40} 54% 18%))">
      <span class="book__cover">
        <span class="book__kicker">{icon(ico)}Guide</span>
        <span class="book__title">{title}</span>
        <span class="book__foot">
          <span class="c__steps" style="--value:100%;color:inherit;opacity:.75">{steps} steps</span>
        </span>
      </span>
    </a>'''


def shelf_block(limit=None):
    """`.book-shelf` — covers stood up next to each other, every second one
    tilted by the component itself so a row reads as a shelf, not a grid."""
    rows = GUIDES[:limit] if limit else GUIDES
    return ('<div class="book-shelf" style="flex-wrap:wrap">'
            + ''.join(book_card(*g) for g in rows) + '</div>')


def guides_block(limit=None):
    rows = GUIDES[:limit] if limit else GUIDES
    return '<div class="grid-auto-sm">' + ''.join(guide_card(*g) for g in rows) + '</div>'


def stepper(current, total):
    segs = ''.join(
        f'<span class="stepper__step"'
        f'{" data-done" if i < current else " data-current" if i == current else ""}></span>'
        for i in range(total))
    return f'<div class="stepper" role="progressbar" aria-valuenow="{current + 1}" aria-valuemax="{total}">{segs}</div>'


def route_index():
    body = f'''
  {hero('Guides', 'Post series with a spine: pick one up, and the steps run in '
        'order until the thing you were trying to build actually works.',
        'Guides', [(str(len(GUIDES)), 'guides'),
                   (str(sum(g[4] for g in GUIDES)), 'steps total')],
        eyebrow_icon='course', pattern='pattern-hairline')}

  <div class="container section-sm">
    {sec('On the shelf', 'Covers, stood up — .book-shelf tilts every second one, '
         'so a row of them reads as a shelf rather than a grid.')}
    {shelf_block()}
  </div>

  <div class="container section-sm" data-collection>
    {sec('All guides', 'The same four as rows, for when you are scanning titles '
         'rather than browsing covers.')}
    {guides_block()}
    <div class="u-mt-6">{pagination(1, 1, href='./index.html', label='Guides')}</div>
  </div>'''
    return page(HERE, 'index.html', 'Guides — Swarnil',
                'Post series with a stepper — pick one up and follow it end to end.',
                body, NAME, own_css='guides.css', current='guides')


def route_guide():
    current = 1
    title, note = STEPS[current]
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Guides</a> <span>/</span> <span>Grid, from scratch</span>
    </nav>

    <h1 class="t-display-2">Grid, from scratch</h1>
    <p class="t-lead u-mt-3" style="max-width:var(--measure-lead)">Six steps, in the
      order you actually reach for them — no step skippable, none of them long.</p>

    <div class="u-mt-6">{stepper(current, len(STEPS))}</div>

    <div class="col-stagebar">
      <a class="btn btn-secondary btn-sm" href="./guide.html" data-step="prev">← Previous</a>
      <div class="col-stagebar__where">
        <span class="col-stagebar__pos">
          <span>Step {current + 1} of {len(STEPS)}</span>
        </span>
        <h2 class="t-h3" style="margin:0">{title}</h2>
      </div>
      <a class="btn btn-primary btn-sm" href="./guide.html" data-step="next">Next →</a>
    </div>

    <article class="content u-mt-8">
      <p>{note}</p>
      <p>Everything after this step assumes the grid is already on the container —
        this step is the one line that makes every other rule in the guide make sense.</p>
    </article>

    <div class="u-mt-10">
      {sec('All steps in this guide')}
      <div class="list-group">
        {''.join(f'<a class="list-group__item" href="./guide.html"'
                 f'{" aria-current=\"page\"" if i == current else ""}>{t}</a>'
                 for i, (t, _) in enumerate(STEPS))}
      </div>
    </div>
  </div>'''
    return page(HERE, 'guide.html', 'Grid, from scratch — Guides — Swarnil',
                'Six steps, in the order you actually reach for them.',
                body, NAME, own_css='guides.css', current='guides')


if __name__ == '__main__':
    made = [route_index(), route_guide()]
    print('guides: ' + ', '.join(made))
