#!/usr/bin/env python3
"""The blog collection — /blog and a single post.

A blog is the collection most people already have, so it is the useful second
one: it proves the sections are not travel-shaped. It uses no CSS of its own.
Every section here is the shared vocabulary in ../collection.css — which is the
test that vocabulary had to pass.

The two routes it needs are the index and the post. A blog's "group" is a
category and its "series" is a multi-part piece; both reuse the same routes as
travel, so they are not rebuilt here.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import icon, ph, page, sec, hero, meta_strip   # noqa: E402

NAME = 'Blog'

CATEGORIES = [('css', 'CSS & layout', 'code', 14), ('motion', 'Motion', 'play', 8),
              ('craft', 'Craft', 'pen', 11), ('notes', 'Notes', 'slate', 23)]

POSTS = [
    ('Why I stopped using a CSS framework', 'css', 'css tokens', '11 min', 'Jul 2026',
     'Three years of overriding someone else’s opinions, and what replaced them.'),
    ('The record light: one colour, rationed', 'craft', 'craft colour', '7 min', 'Jun 2026',
     'A palette closed on purpose, so a single hue can carry meaning.'),
    ('Motion that survives prefers-reduced-motion', 'motion', 'motion a11y', '9 min',
     'Jun 2026', 'If the finished state is the resting state, nothing is ever unreachable.'),
    ('Tokens are a contract, not a theme', 'css', 'css tokens', '6 min', 'May 2026',
     'Two tiers, and why one override reaches everything.'),
    ('Writing components you can delete', 'craft', 'craft', '8 min', 'Apr 2026',
     'The best component is the one that leaves no trace when it goes.'),
]

TAGS = [('css', 18), ('tokens', 12), ('motion', 9), ('a11y', 14), ('craft', 11),
        ('colour', 7), ('type', 6), ('notes', 23)]

TOC = [('why', 'Why this happened'), ('cost', 'What it cost'),
       ('replaced', 'What replaced it'), ('worth', 'Was it worth it')]


def categories_block():
    return '<div class="col-groups">' + ''.join(
        f'<button class="col-group" type="button" data-group="{s}" aria-pressed="false">'
        f'<span class="col-group__ico">{icon(i, group="creator")}</span>'
        f'<span><span class="col-group__name">{n}</span>'
        f'<span class="col-group__n">{c} posts</span></span></button>'
        for s, n, i, c in CATEGORIES) + '</div>'


def posts_block(limit=None, featured=False):
    rows = ''.join(
        f'<a class="col-post-row" href="./post.html" data-post data-of="{cat}" '
        f'data-region="{cat}" data-tags="{tags}">'
        f'<span class="col-post-row__thumb">{ph(cat)}</span>'
        f'<span class="col-post-row__body"><span class="col-post-row__title">{t}</span>'
        f'<span class="col-post-row__note">{note}</span></span>'
        f'<span class="col-post-row__meta"><span>{read}</span><span>{when}</span></span></a>'
        for t, cat, tags, read, when, note in (POSTS[:limit] if limit else POSTS))
    return ('<div class="col-posts">' + rows +
            '<p class="col-empty" data-empty-for="[data-post]" hidden>'
            'No posts match. Try clearing a filter.</p></div>')


def tags_widget(current=None):
    return ('<div class="col-widget"><span class="col-widget__title">Tags</span>'
            '<div class="col-tags">' + ''.join(
                f'<a class="col-tag" href="#i"{" aria-current=\"page\"" if t == current else ""}>'
                f'{t}<span class="col-tag__n">{n}</span></a>' for t, n in TAGS)
            + '</div></div>')


def author_widget():
    return f'''<div class="col-widget">
      <span class="col-widget__title">Written by</span>
      <div class="col-author">
        <span class="col-author__face">{ph('craft')}</span>
        <span><span class="col-author__name">Swarnil Singhai</span>
          <span class="col-author__who">Builds things, then writes down what broke.</span></span>
      </div>
      <div class="col-widget__foot">56 posts · since 2021</div>
    </div>'''


def recent_widget(title='Recent'):
    return (f'<div class="col-widget"><span class="col-widget__title">{title}</span>'
            '<div class="col-mini">' + ''.join(
                f'<a class="col-mini__item" href="./post.html">'
                f'<span class="col-mini__n">{i+1:02d}</span>'
                f'<span><span class="col-mini__title">{t}</span>'
                f'<span class="col-mini__meta">{when} · {read}</span></span></a>'
                for i, (t, _, _, read, when, _) in enumerate(POSTS[:4]))
            + '</div></div>')


def subscribe_widget():
    return '''<div class="col-widget col-widget-accent">
      <span class="col-widget__title">Newsletter</span>
      <p class="t-small">One email when something is worth reading. No schedule,
        because a schedule is how newsletters get padded.</p>
      <form class="col-sub__form" onsubmit="return false">
        <input type="email" placeholder="you@example.com" aria-label="Email address" />
        <button class="btn btn-primary btn-sm" type="submit">Subscribe</button>
      </form>
    </div>'''


def toc_widget():
    return ('<div class="col-widget"><span class="col-widget__title">On this page</span>'
            '<nav class="col-toc">' + ''.join(
                f'<a href="#{s}"{" aria-current=\"true\"" if i == 0 else ""}>{t}</a>'
                for i, (s, t) in enumerate(TOC)) + '</nav></div>')


def featured_stage():
    """The floating screen — a small, shadowed, slightly turned surface
    showing three real post rows at phone scale. Not a mockup image; the
    same .card-compact every post already renders as, just smaller."""
    rows = ''.join(
        f'<article class="card card-compact card-bare" style="border-radius:0;'
        f'border-bottom:var(--border-hair) solid var(--line-subtle)">'
        f'<div class="card__body"><p class="card__meta">{cat} · {read}</p>'
        f'<h3 class="card__title" style="font-size:var(--text-sm)">{title}</h3></div></article>'
        for title, cat, tags, read, when, note in POSTS[:3])
    return f'''
    <div class="hero-split__stage">
      <div class="surface" style="max-width:19rem;margin-inline:auto;overflow:hidden;
           border-radius:var(--radius-sheet);box-shadow:var(--shadow-3);transform:rotate(-2deg)">
        <div style="padding:var(--space-4) var(--space-4) var(--space-2)">
          <span class="t-slate-sm" style="color:var(--fg-faint)">Featured</span>
        </div>
        {rows}
      </div>
      <p class="hero-split__caption">Featured articles <span>Live preview</span></p>
    </div>'''


def route_index():
    body = f'''
  <div class="container">
    <section class="hero hero-split hero-sm pattern pattern-dots pattern-lg fade-corners"
             style="padding-block:var(--space-10) var(--space-8);border-radius:var(--radius-sheet);
                    max-width:calc(var(--w-site) - 4rem);margin-inline:auto">
      <div>
        <span class="hero__eyebrow">{icon('pen')}The blog</span>
        <h1 class="hero__title">Notes on building things, <em>and what broke</em>.</h1>
        <p class="hero__lead">Fifty-six posts about CSS, motion and the craft of shipping a
          site on your own. No schedule — one email when something is worth reading.</p>
        <div class="hero__actions">
          <div class="input-group" style="max-width:26rem">
            <input class="input" type="search" placeholder="Search the blog"
                   aria-label="Search the blog" />
            <button class="btn btn-primary" type="button">Search</button>
          </div>
        </div>
        {meta_strip([('56', 'posts'), ('4', 'categories'), ('8', 'tags'), ('2021', 'since')],
                    paper=True, border=False, inline=True)}
      </div>
      {featured_stage()}
    </section>
  </div>

  <div data-collection>
  <section class="container section-sm">
    {sec('Categories', 'The widest cut. Pick one and the posts below narrow to it.')}
    {categories_block()}
  </section>

  <section class="container section-sm">
    <div class="col-layout">
      <aside class="col-layout__side col-rail col-rail-sticky">
        <div class="col-facets">
          <div class="col-facets__group">
            <span class="col-facets__title">Filtering</span>
            <p class="t-small u-fg-subtle" data-filter-state>Everything</p>
            <button class="btn btn-quiet btn-sm" type="button" data-filter-reset hidden>
              Clear filters</button>
          </div>
          <div class="col-facets__group">
            <span class="col-facets__title">Topic</span>
            {''.join(f'<label class="col-facet"><input type="checkbox" data-facet="{t}" />'
                     f'<span>{t}</span><span class="col-facet__n">{n}</span></label>'
                     for t, n in TAGS[:5])}
          </div>
        </div>
        {subscribe_widget()}
      </aside>
      <div>
        {sec('Featured', 'The three worth reading first.')}
        {posts_block(limit=3)}
        <div class="u-mt-10">
          {sec('Everything', 'Newest first.')}
          {posts_block()}
        </div>
      </div>
    </div>
  </section>
  </div>'''
    return page(HERE, 'index.html', 'Blog — Swarnil',
                'Notes on building things, and what broke.', body, NAME, current='blog')


def route_post():
    body = f'''
  <div class="col-progress"><div class="col-progress__bar" style="--value:38%"></div></div>

  <article class="container section-sm">
    <header class="col-post__head">
      <nav class="col-post__crumbs" aria-label="Breadcrumb">
        <a href="./index.html">Blog</a> <span>/</span>
        <a href="#i">CSS &amp; layout</a> <span>/</span> <span>This post</span>
      </nav>
      <h1 class="t-display-2">Why I stopped using a CSS framework</h1>
      <p class="t-lead" style="max-width:var(--measure-lead)">
        Three years of overriding someone else's opinions, and what replaced them.
      </p>
      <div class="col-post__crumbs">
        <span>11 min read</span> <span>·</span> <span>July 2026</span>
        <span>·</span> <span>CSS &amp; layout</span>
      </div>
    </header>

    <div class="surface u-mb-8" style="aspect-ratio:16/9;overflow:hidden;border-radius:var(--radius-card)">
      {ph('css', True)}
    </div>

    <div class="col-post">
      <div class="content">
        <p>Every framework is a set of answers to questions someone else was asking.
          That is fine until your questions differ, and then every line you write is
          an argument with the defaults.</p>

        <h2 id="why">Why this happened</h2>
        <p>It started with a card. The framework had one, and it was nearly right —
          which is worse than being wrong, because nearly right gets overridden
          instead of replaced.</p>
        <blockquote>
          <p>A component you have overridden four times is a component you now own,
            with none of the benefits of owning it.</p>
        </blockquote>

        <h2 id="cost">What it cost</h2>
        <p>Forty kilobytes of CSS to ship six components, and a build step to
          remove the rest of it.</p>

        <h2 id="replaced">What replaced it</h2>
        <p>Two tiers of custom properties and about thirty components. The whole
          thing is smaller than the framework's grid system was.</p>

        <h2 id="worth">Was it worth it</h2>
        <p>The honest answer is that it was worth it the second time. The first
          attempt was a framework with my name on it.</p>
      </div>

      <aside class="col-post__rail col-rail col-rail-sticky">
        {toc_widget()}
        {author_widget()}
        {subscribe_widget()}
        {recent_widget('More on CSS')}
        {tags_widget(current='css')}
      </aside>
    </div>

    <a class="col-next u-mt-10" href="#i">
      <span class="col-next__label">Next post</span>
      <span class="col-order__title">Tokens are a contract, not a theme</span>
      <span class="t-small u-fg-subtle">Two tiers, and why one override reaches everything.</span>
    </a>
  </article>'''
    return page(HERE, 'post.html', 'Why I stopped using a CSS framework — Blog',
                'Three years of overriding someone else’s opinions.',
                body, NAME, current='blog')


if __name__ == '__main__':
    made = [route_index(), route_post()]
    print('blog: ' + ', '.join(made))
