#!/usr/bin/env python3
"""The newsletter collection — /newsletter and a single update.

Two routes, like blog: an archive and a post. This is a newsletter where
updates get shared, NOT a numbered publication — so nothing here carries an
issue number. Numbering a newsletter promises a cadence, and the promise this
one makes is the opposite: something arrives when there is something worth
sending. The date is the identifier, because the date is the only fact that
is always true.

What makes an update different from a blog post is entirely the archive card
— .c-newsletter (an envelope rule) already existed in 23-collection.css,
unused; the date tile is .itinerary__chip (the day-by-day trip composite)
reused flat, because a send date and a trip day are the same fact — a number
and a unit under it. No new CSS for either.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import (icon, ph, page, sec, hero, meta_strip, pagination,   # noqa: E402
                   comments, LIKE_SCRIPT)

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
        f'<a class="c c-newsletter" href="./post.html" data-post data-tags="update">'
        f'<div class="c__body" style="flex-direction:row;align-items:center;gap:var(--space-4)">'
        f'{date_chip(day, mon)}'
        f'<div style="min-width:0"><span class="c__issue">{mon} {day}, {yr}</span>'
        f'<h3 class="c__title" style="margin-top:2px">{subject}</h3>'
        f'<p class="c__excerpt">{excerpt}</p></div></div>'
        f'<div class="c__foot"><span>{yr}</span><span>{read}</span></div></a>'
        for n, subject, day, mon, yr, excerpt, read in rows)
    return f'<div class="stack-sm">{cards}</div>'


def subscribe_block():
    return '''
    <div class="col-widget col-widget-accent">
      <span class="col-widget__title">Get the next one</span>
      <p class="t-small">Sent when there is something to say — not weekly, not
        monthly, not on a schedule that needs filling. One click to leave.</p>
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
        <h1 class="hero__title">Updates, <em>when there are any</em>.</h1>
        <p class="hero__lead">What I am building, what broke, and what I would do
          differently — sent when there is something to say rather than on a
          schedule that needs filling.</p>
        <div class="hero__actions">
          <form onsubmit="return false" style="max-width:26rem">
            <div class="input-group">
              <input class="input" type="email" placeholder="you@example.com"
                     aria-label="Email address" />
              <button class="btn btn-primary" type="submit">Subscribe</button>
            </div>
          </form>
        </div>
        {meta_strip([('9.2k', 'readers'), ('46%', 'open rate'), ('2024', 'since'),
                     ('0', 'drip sequences')], paper=True, border=False, inline=True)}
      </div>
      <div class="hero-split__stage">
        {issues_block(limit=1)}
        <p class="hero-split__caption"><span>Most recent</span>
          <span>Jul 22, 2026</span></p>
      </div>
    </section>
  </div>

  <div data-collection>
  <section class="container section-sm">
    <div class="grid-rail">
      <div>
        {sec('Everything sent', 'Newest first. Every update is also just a post — '
             'nothing about the archive is special-cased.')}
        {issues_block()}
        <div class="u-mt-6">{pagination(1, 7, href='./index.html', label='Archive')}</div>
      </div>
      <aside>
        {subscribe_block()}
      </aside>
    </div>
  </section>
  </div>'''
    return page(HERE, 'index.html', 'Newsletter — Swarnil',
                'Updates on CSS, motion and the craft of shipping a site.',
                body, NAME, current='newsletter')


def toc_rail(items):
    """A sticky table of contents. Anchors into the article's own h2 ids, so it
    cannot list a heading the prose does not have."""
    links = ''.join(
        f'<a class="list-group__item" href="#{a}">{t}</a>' for a, t in items)
    return f'''<div class="col-widget">
      <span class="col-widget__title">In this update</span>
      <div class="list-group list-group-flush">{links}</div>
    </div>'''


def related_block(exclude=0, limit=3):
    """Other updates, at the end. A newsletter archive lives or dies on whether
    reading one leads to reading a second."""
    rows = [u for k, u in enumerate(ISSUES) if k != exclude][:limit]
    return '<div class="grid-3">' + ''.join(
        f'''<a class="card" href="./post.html">
          <div class="card__body">
            <span class="card__meta">{icon('mail')}{mon} {day}, {yr}</span>
            <h3 class="card__title">{subject}</h3>
            <p class="card__excerpt">{excerpt}</p>
            <span class="card__meta u-mt-2">{read}</span>
          </div>
        </a>''' for n, subject, day, mon, yr, excerpt, read in rows) + '</div>'


TOC = [('why', 'The row you never declared'), ('fix', 'The one line that fixes it'),
       ('rest', 'What it does not fix')]


def route_post():
    # .container-narrow centres the reading column; the rail sits outside it so
    # the prose keeps its measure while the TOC stays reachable. A newsletter is
    # read start to finish, so the measure matters more here than anywhere.
    body = f'''
  <article class="container section-sm">
    <div class="grid-rail">
      <div>
        <header class="col-post__head" style="text-align:center">
          <nav class="col-post__crumbs" aria-label="Breadcrumb"
               style="justify-content:center">
            <a href="./index.html">Newsletter</a> <span>/</span>
            <span>Jul 22, 2026</span>
          </nav>
          <div style="display:flex;justify-content:center;margin-top:var(--space-4)">
            {date_chip('22', 'Jul')}
          </div>
          <h1 class="t-display-2 u-mt-4">The grid lesson nobody asked for</h1>
          <p class="t-lead u-mt-3"
             style="max-width:var(--measure-lead);margin-inline:auto">
            Why the implicit grid is where every layout question actually starts.
          </p>
          <div class="col-post__crumbs" style="justify-content:center">
            <span>4 min read</span> <span>·</span> <span>Sent to 9.2k readers</span>
          </div>
        </header>

        <div class="content u-mt-10" style="margin-inline:auto">
          <p>Every layout question I get eventually turns out to be the same
            question: where did that extra row come from. It is always the
            implicit grid, and it is never explained in the place people go
            looking.</p>
          <h2 id="why">The row you never declared</h2>
          <p>Content that overflows the tracks you named does not vanish — it gets
            a new, implicit row, sized by <code>grid-auto-rows</code>, which
            defaults to <code>auto</code> and surprises everyone equally.</p>
          <blockquote>
            <p>The implicit grid is not a bug in your layout. It is the layout, for
              everything you forgot to name a place for.</p>
          </blockquote>
          <h2 id="fix">The one line that fixes most of it</h2>
          <p><code>grid-auto-rows: minmax(0, auto)</code> is the line I add to
            almost every grid I ship, and the line almost no tutorial mentions.</p>
          <h2 id="rest">What it does not fix</h2>
          <p>Nothing about <em>column</em> overflow, which is a different problem
            with a different answer — <code>minmax(0, 1fr)</code>, for the same
            underlying reason.</p>
        </div>

        {comments(locked=False)}
      </div>

      <aside class="col-post__rail col-rail col-rail-sticky">
        {toc_rail(TOC)}
        {subscribe_block()}
      </aside>
    </div>

    <div class="u-mt-12">
      {sec('More updates', 'Three others, newest first.')}
      {related_block(exclude=0)}
      <div class="u-mt-6">
        <a class="btn btn-secondary btn-pill" href="./index.html">
          Everything sent →</a>
      </div>
    </div>
  </article>{LIKE_SCRIPT}'''
    return page(HERE, 'post.html', 'The grid lesson nobody asked for — Newsletter',
                'Why the implicit grid is where every layout question actually starts.',
                body, NAME, current='newsletter')


if __name__ == '__main__':
    made = [route_index(), route_post()]
    print('newsletter: ' + ', '.join(made))
