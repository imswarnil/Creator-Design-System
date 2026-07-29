#!/usr/bin/env python3
"""The docs collection — a reusable documentation template.

Not the docs/_build system this repo's own site runs on — that is bespoke,
1500 lines, and knows about this specific design system's content. This is
what a COLLECTION gives you if what you're documenting is your own project:
/docs (index), a docs-section (a category of posts), a doc post, and a
component reference page, all built from the same three-column shape
laid out already — .grid-rail-left wrapping .grid-rail, exactly like the
course lesson player and the Grid & Layout "Patterns" doc page.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import icon, ph, page, sec, hero, meta_strip, pagination   # noqa: E402

NAME = 'Docs'

SECTIONS = [
    ('start', 'Getting started', 'course', 4),
    ('components', 'Components', 'take', 12),
    ('api', 'API reference', 'slate', 7),
]

DOCS = [
    ('install', 'Installation', 'start', 'Link the stylesheet, or install the package.'),
    ('quickstart', 'Quickstart', 'start', 'A working page in the time it takes to read this.'),
    ('theming', 'Theming', 'start', 'Override the semantic tier; never edit the source.'),
    ('folders', 'Folder structure', 'start', 'What each numbered layer holds, and why the order matters.'),
    ('button', 'Button', 'components', 'Six intents, three sizes, every state.'),
    ('card', 'Card', 'components', 'The base shape every collection card extends.'),
    ('modal', 'Modal', 'components', '<dialog>, for real — focus trap included by the browser.'),
    ('config', 'Configuration', 'api', 'Every token you can override, grouped by what it controls.'),
]

# id, kind (page|component), name, params — the "component" reference shape
COMPONENTS = [
    ('button', 'Button', 'components',
     '<button class="btn btn-primary">Primary</button>',
     [('btn-primary / -secondary / -ghost / -quiet', 'the six intents'),
      ('btn-sm / (default) / btn-lg', 'the three sizes'),
      (':disabled', 'the only disabled state — no .btn-disabled class')]),
]

TOC = [('why', 'Why a docs collection'), ('shape', 'The three-column shape'),
       ('reuse', 'What it reuses')]


def sections_block():
    return '<div class="col-groups">' + ''.join(
        f'<a class="col-group" href="./section.html" data-group="{s}">'
        f'<span class="col-group__ico">{icon(i, group="creator")}</span>'
        f'<span><span class="col-group__name">{n}</span>'
        f'<span class="col-group__n">{c} pages</span></span></a>'
        for s, n, i, c in SECTIONS) + '</div>'


def docs_list(section=None, limit=None):
    rows = DOCS if not section else [d for d in DOCS if d[2] == section]
    rows = rows[:limit] if limit else rows
    items = ''.join(
        f'<a class="col-post-row" href="./post.html" data-post data-of="{sec_}">'
        f'<span class="col-post-row__thumb">{ph(slug)}</span>'
        f'<span class="col-post-row__body"><span class="col-post-row__title">{title}</span>'
        f'<span class="col-post-row__note">{excerpt}</span></span></a>'
        for slug, title, sec_, excerpt in rows)
    return f'<div class="col-posts">{items}</div>'


def nav_rail(current=None):
    groups = ''
    for s, n, i, c in SECTIONS:
        rows = ''.join(
            f'<a class="list-group__item" href="./post.html"'
            f'{" aria-current=\"page\"" if slug == current else ""}>{title}</a>'
            for slug, title, sec_, excerpt in DOCS if sec_ == s)
        groups += (f'<p class="t-slate-sm u-mt-4 u-mb-2" style="color:var(--fg-faint)">{n}</p>'
                   f'<div class="list-group list-group-flush">{rows}</div>')
    return groups


def toc_rail():
    links = ''.join(f'<a href="#{s}">{t}</a>' for s, t in TOC)
    return f'<nav class="stack-xs">{links}</nav>'


def code_block(code, lang='html'):
    return (f'<figure class="codebox codebox-light u-m-0"><figcaption class="codebox__head">'
            f'<span class="codebox__lang">{lang}</span>'
            f'<button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>'
            f'<pre class="codebox__pre"><code>{code}</code></pre></figure>')


def route_index():
    body = f'''
  <div class="container">
    <section class="hero hero-split hero-sm pattern pattern-topo pattern-lg fade-corners"
             style="padding-block:var(--space-10) var(--space-8);border-radius:var(--radius-sheet);
                    max-width:calc(var(--w-site) - 4rem);margin-inline:auto">
      <div>
        <span class="hero__eyebrow">{icon('slate', group='creator')}The docs collection</span>
        <h1 class="hero__title">A docs template, <em>not a docs site</em>.</h1>
        <p class="hero__lead">Three sections, an index, a section page, a post and a
          component reference — the shape to copy for your own project's docs, not
          this system's own 130-page build.</p>
        {meta_strip([('3', 'sections'), ('8', 'pages'), ('1', 'component ref'),
                     ('2026', 'updated')], paper=True, border=False, inline=True)}
      </div>
      <div class="hero-split__stage">
        {docs_list(limit=3)}
      </div>
    </section>
  </div>

  <div data-collection>
  <section class="container section-sm">
    {sec('Sections', 'The widest cut. Pick one and the pages below narrow to it.')}
    {sections_block()}
  </section>

  <section class="container section-sm">
    {sec('All pages')}
    {docs_list()}
    <div class="u-mt-6">{pagination(1, 2, href='./index.html', label='Docs')}</div>
  </section>
  </div>'''
    return page(HERE, 'index.html', 'Docs — Swarnil',
                'A reusable documentation template: sections, posts and a '
                'component reference.', body, NAME, current='docs')


def route_section():
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Docs</a> <span>/</span> <span>Getting started</span>
    </nav>
    <h1 class="t-display-2">Getting started</h1>
    <p class="t-lead u-mt-3" style="max-width:var(--measure-lead)">Four pages, in the
      order most people actually read them.</p>
    <div class="u-mt-8">{docs_list(section='start')}</div>
  </div>'''
    return page(HERE, 'section.html', 'Getting started — Docs — Swarnil',
                'Install, quickstart, theming, folder structure.',
                body, NAME, current='docs')


def route_post():
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Docs</a> <span>/</span>
      <a href="./section.html">Getting started</a> <span>/</span> <span>Installation</span>
    </nav>

    <div class="grid-rail-left">
      <nav class="stack-xs">{nav_rail(current='install')}</nav>

      <div class="grid-rail">
        <article class="content">
          <h1>Installation</h1>
          <p class="t-lead">Link the compiled stylesheet, or install the package —
            both ship the same classes.</p>

          <h2 id="why">Why a docs collection</h2>
          <p>Every project ships with its own README that grows past what a README
            can hold. This is the point it graduates to: a real docs site, built
            from the same components the project already has.</p>

          <h2 id="shape">The three-column shape</h2>
          <p>Nav on the left, the page in the middle, a table of contents on the
            right — <code>.grid-rail-left</code> wrapping <code>.grid-rail</code>,
            the same two primitives the course lesson player composes.</p>
          {code_block('&lt;link rel="stylesheet" href="dist/creator.css" /&gt;')}

          <h2 id="reuse">What it reuses</h2>
          <p>Everything. <code>.col-groups</code> for the section grid, <code>.col-posts</code>
            for the page list, <code>.list-group</code> for the nav rail, <code>.codebox</code>
            for every snippet. Nothing here is docs-specific CSS.</p>
        </article>

        <aside>
          <p class="t-slate-sm u-mb-3" style="color:var(--fg-faint)">On this page</p>
          {toc_rail()}
        </aside>
      </div>
    </div>
  </div>'''
    return page(HERE, 'post.html', 'Installation — Docs — Swarnil',
                'Link the compiled stylesheet, or install the package.',
                body, NAME, current='docs')


def route_component():
    slug, name, section, demo, props = COMPONENTS[0]
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Docs</a> <span>/</span>
      <a href="./section.html">Components</a> <span>/</span> <span>{name}</span>
    </nav>

    <div class="grid-rail-left">
      <nav class="stack-xs">{nav_rail()}</nav>

      <div>
        <h1 class="t-display-2">{name}</h1>
        <p class="t-lead u-mt-3" style="max-width:var(--measure-lead)">The reference
          shape every component page in this collection uses: a live demo, the
          markup that made it, and the class table underneath.</p>

        <div class="surface u-mt-8" style="padding:var(--space-8);display:grid;place-items:center">
          {demo}
        </div>
        <div class="u-mt-4">{code_block(demo.replace('<', '&lt;').replace('>', '&gt;'))}</div>

        <div class="u-mt-8">
          {sec('Classes')}
          <div class="surface" style="overflow-x:auto"><table class="spec-table" style="width:100%">
            <thead><tr><th>Class</th><th>Does</th></tr></thead><tbody>
            {''.join(f'<tr><td><code class="t-code">{c}</code></td><td>{d}</td></tr>' for c, d in props)}
            </tbody></table></div>
        </div>
      </div>
    </div>
  </div>'''
    return page(HERE, 'component.html', f'{name} — Docs — Swarnil',
                f'The {name.lower()} component: demo, markup, and every class.',
                body, NAME, current='docs')


if __name__ == '__main__':
    made = [route_index(), route_section(), route_post(), route_component()]
    print('docs: ' + ', '.join(made))
