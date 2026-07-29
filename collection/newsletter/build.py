#!/usr/bin/env python3
"""The newsletter collection — /newsletter and a single issue.

Two routes, like blog: an archive and a post. What makes an issue different
from a blog post is entirely the archive card — .c-newsletter (issue number
+ envelope rule) already existed in 23-collection.css, unused; the date tile
is .itinerary__chip (the day-by-day trip composite) reused flat, because a
send date and a trip day are the same fact — a number and a unit under it.
No new CSS for either.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import icon, ph, page, sec, hero, meta_strip, pagination   # noqa: E402

NAME = 'Newsletter'

ISSUES = [
    ('41', 'The grid lesson nobody asked for', '22', 'Jul', '2026',
     'Why the implicit grid is where every layout question actually starts.', '4 min'),
    ('40', 'Two tiers of tokens, one override', '15', 'Jul', '2026',
     'Semantic tokens are the only tier a theme should ever touch.', '3 min'),
    ('39', 'A colour rationed on purpose', '08', 'Jul', '2026',
     'What "almost monochrome" buys you that a full palette can\'t.', '5 min'),
    ('38', 'Shipping without a framework', '01', 'Jul', '2026',
     'Forty kilobytes of CSS to remove, and what actually replaced it.', '6 min'),
    ('37', 'The record light, explained', '24', 'Jun', '2026',
     'One colour, one dot, and why it means "live" everywhere in the system.', '4 min'),
    ('36', 'Motion under prefers-reduced-motion', '17', 'Jun', '2026',
     'The finished state is the resting state — nothing is ever unreachable.', '5 min'),
]

PATTERNS = ['pattern-grid', 'pattern-hatch', 'pattern-dots', 'pattern-waveform']


def date_chip(day, month):
    """.itinerary__chip, flattened — the trip composite's day tile is
    already a number over a unit; a send date is the same shape."""
    return (f'<span class="itinerary__chip" style="position:static;width:3rem;height:3rem">'
            f'<b>{day}</b><span>{month}</span></span>')


def issues_block(limit=None):
    rows = ISSUES[:limit] if limit else ISSUES
    cards = ''.join(
        f'<a class="c c-newsletter" href="./post.html" data-post data-tags="issue">'
        f'<div class="c__body" style="flex-direction:row;align-items:center;gap:var(--space-4)">'
        f'{date_chip(day, mon)}'
        f'<div style="min-width:0"><span class="c__issue">Issue #{n}</span>'
        f'<h3 class="c__title" style="margin-top:2px">{subject}</h3>'
        f'<p class="c__excerpt">{excerpt}</p></div></div>'
        f'<div class="c__foot"><span>{yr}</span><span>{read}</span></div></a>'
        for n, subject, day, mon, yr, excerpt, read in rows)
    return f'<div class="stack-sm">{cards}</div>'


def subscribe_block():
    return '''
    <div class="col-widget col-widget-accent">
      <span class="col-widget__title">Get the next one</span>
      <p class="t-small">Weekly, whenever there is something worth forty-one issues
        of practice behind it. No spam, one click to leave.</p>
      <form class="col-sub__form" onsubmit="return false">
        <input type="email" placeholder="you@example.com" aria-label="Email address" />
        <button class="btn btn-primary btn-sm" type="submit">Subscribe</button>
      </form>
    </div>'''


def route_index():
    body = f'''
  <div class="container">
    <section class="hero hero-split hero-sm pattern pattern-waveform pattern-lg fade-corners"
             style="padding-block:var(--space-10) var(--space-8);border-radius:var(--radius-sheet);
                    max-width:calc(var(--w-site) - 4rem);margin-inline:auto">
      <div>
        <span class="hero__eyebrow">{icon('mail')}The newsletter</span>
        <h1 class="hero__title">Forty-one issues, <em>and counting</em>.</h1>
        <p class="hero__lead">One email when something is worth forty-one issues of
          practice behind it. No schedule beyond that — no padding either.</p>
        <div class="hero__actions">
          <form onsubmit="return false" style="max-width:26rem">
            <div class="input-group">
              <input class="input" type="email" placeholder="you@example.com"
                     aria-label="Email address" />
              <button class="btn btn-primary" type="submit">Subscribe</button>
            </div>
          </form>
        </div>
        {meta_strip([('41', 'issues'), ('9.2k', 'subscribers'), ('46%', 'open rate'),
                     ('2024', 'since')], paper=True, border=False, inline=True)}
      </div>
      <div class="hero-split__stage">
        {issues_block(limit=1)}
        <p class="hero-split__caption">Latest issue <span>#41</span></p>
      </div>
    </section>
  </div>

  <div data-collection>
  <section class="container section-sm">
    <div class="grid-rail">
      <div>
        {sec('All issues', 'Newest first. Every issue is also just a post — nothing '
             'about the archive is special-cased.')}
        {issues_block()}
        <div class="u-mt-6">{pagination(1, 7, href='./index.html', label='Issue archive')}</div>
      </div>
      <aside>
        {subscribe_block()}
      </aside>
    </div>
  </section>
  </div>'''
    return page(HERE, 'index.html', 'Newsletter — Swarnil',
                'Forty-one issues on CSS, motion and the craft of shipping a site.',
                body, NAME, current='newsletter')


def route_post():
    body = f'''
  <article class="container section-sm">
    <header class="col-post__head">
      <nav class="col-post__crumbs" aria-label="Breadcrumb">
        <a href="./index.html">Newsletter</a> <span>/</span> <span>Issue 41</span>
      </nav>
      {date_chip('22', 'Jul')}
      <h1 class="t-display-2 u-mt-4">The grid lesson nobody asked for</h1>
      <p class="t-lead" style="max-width:var(--measure-lead)">
        Why the implicit grid is where every layout question actually starts.
      </p>
      <div class="col-post__crumbs">
        <span>4 min read</span> <span>·</span> <span>Issue #41</span>
        <span>·</span> <span>22 Jul 2026</span>
      </div>
    </header>

    <div class="col-post">
      <div class="content">
        <p>Every layout question I get eventually turns out to be the same question:
          where did that extra row come from. It is always the implicit grid, and it
          is never explained in the place people go looking.</p>
        <h2>The row you never declared</h2>
        <p>Content that overflows the tracks you named does not vanish — it gets a
          new, implicit row, sized by <code>grid-auto-rows</code>, which defaults to
          <code>auto</code> and surprises everyone equally.</p>
        <blockquote>
          <p>The implicit grid is not a bug in your layout. It is the layout, for
            everything you forgot to name a place for.</p>
        </blockquote>
        <h2>The one line that fixes most of it</h2>
        <p><code>grid-auto-rows: minmax(0, auto)</code> is the line I add to almost
          every grid I ship, and the line almost no tutorial mentions.</p>
      </div>

      <aside class="col-post__rail col-rail col-rail-sticky">
        {subscribe_block()}
      </aside>
    </div>

    <a class="col-next u-mt-10" href="./index.html">
      <span class="col-next__label">Back to</span>
      <span class="col-order__title">All issues</span>
    </a>
  </article>'''
    return page(HERE, 'post.html', 'The grid lesson nobody asked for — Newsletter',
                'Why the implicit grid is where every layout question actually starts.',
                body, NAME, current='newsletter')


if __name__ == '__main__':
    made = [route_index(), route_post()]
    print('newsletter: ' + ', '.join(made))
