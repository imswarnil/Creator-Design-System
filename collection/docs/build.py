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

# slug, name, icon, one-line summary. The COUNT is deliberately not here — it is
# derived from DOCS below, because a hardcoded count is a number that goes wrong
# silently the first time a page is added. This list used to claim 4/12/7 while
# actually holding 4/3/1.
SECTIONS = [
    ('start', 'Getting started', 'course',
     'Install it, ship a page, then make it yours.'),
    ('components', 'Components', 'take',
     'Every component, with the markup and the full class table.'),
    ('patterns', 'Patterns', 'slate',
     'Whole layouts assembled from the components above.'),
    ('api', 'API reference', 'slate',
     'Every token and every hook you can override.'),
]

# slug, title, section, summary, read time
DOCS = [
    ('install', 'Installation', 'start',
     'Link the stylesheet, or install the package.', '2 min'),
    ('quickstart', 'Quickstart', 'start',
     'A working page in the time it takes to read this.', '5 min'),
    ('theming', 'Theming', 'start',
     'Override the semantic tier; never edit the source.', '6 min'),
    ('folders', 'Folder structure', 'start',
     'What each numbered layer holds, and why the order matters.', '4 min'),
    ('upgrading', 'Upgrading', 'start',
     'What changes between minor versions, and what never will.', '3 min'),

    ('button', 'Button', 'components',
     'Six intents, three sizes, every state.', '4 min'),
    ('card', 'Card', 'components',
     'The base shape every collection card extends.', '5 min'),
    ('modal', 'Modal', 'components',
     'A real &lt;dialog&gt; — focus trap included by the browser.', '4 min'),
    ('form', 'Form controls', 'components',
     'Native inputs, native validation, one label rule.', '7 min'),
    ('timeline', 'Timeline', 'components',
     'Vertical, horizontal, and four modifiers.', '5 min'),
    ('navbar', 'Navbar', 'components',
     'One component, a style per collection, six variables.', '8 min'),

    ('page-layouts', 'Page layouts', 'patterns',
     'The rail, the split rail, and when each one is wrong.', '6 min'),
    ('dark-mode', 'Dark mode', 'patterns',
     'One set of variables, two themes, no second stylesheet.', '4 min'),
    ('printing', 'Printing', 'patterns',
     'What survives a page break, and what to hide.', '3 min'),

    ('tokens', 'Token reference', 'api',
     'Every token you can override, grouped by what it controls.', '12 min'),
    ('js-hooks', 'JavaScript hooks', 'api',
     'The data attributes nav.js sets, and what CSS does with them.', '5 min'),
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


def in_section(s):
    """Every doc belonging to one section. The single place that mapping lives,
    so counts, lists and the nav rail can never disagree about it."""
    return [d for d in DOCS if d[2] == s]


def sections_block():
    """Each section card carries its real page count and total read time, both
    derived — and the first few page titles under it, so a section is browsable
    from the index without a second click to find out what is inside."""
    out = ''
    for s, n, i, summary in SECTIONS:
        pages = in_section(s)
        mins = sum(int(d[4].split()[0]) for d in pages)
        peek = ''.join(
            f'<a class="list-group__item" href="./post.html">{d[1]}'
            f'<span class="u-ms-auto t-slate-sm" style="color:var(--fg-faint)">'
            f'{d[4]}</span></a>' for d in pages[:3])
        more = (f'<a class="list-group__item" href="./section.html">'
                f'<span style="color:var(--fg-accent)">'
                f'+{len(pages) - 3} more →</span></a>') if len(pages) > 3 else ''
        out += f'''
        <article class="card">
          <div class="card__body">
            <span class="card__meta">{icon(i, group="creator")}{n}</span>
            <h3 class="card__title"><a class="card__link" href="./section.html">{n}</a></h3>
            <p class="card__excerpt">{summary}</p>
            <div class="col-meta col-meta-inline u-mt-3" style="border-top:0;padding-top:0">
              <div><span class="col-meta__n">{len(pages)}</span>
                <span class="col-meta__l">pages</span></div>
              <div><span class="col-meta__n">{mins}</span>
                <span class="col-meta__l">min read</span></div>
            </div>
            <div class="list-group list-group-flush u-mt-4">{peek}{more}</div>
          </div>
        </article>'''
    return f'<div class="grid-auto-sm">{out}</div>'


def docs_list(section=None, limit=None):
    rows = in_section(section) if section else DOCS
    rows = rows[:limit] if limit else rows
    labels = {s: n for s, n, _, _ in SECTIONS}
    items = ''.join(
        f'<a class="col-post-row" href="./post.html" data-post data-of="{sec_}">'
        f'<span class="col-post-row__thumb">{ph(slug)}</span>'
        f'<span class="col-post-row__body"><span class="col-post-row__title">{title}</span>'
        f'<span class="col-post-row__note">{excerpt}</span>'
        f'<span class="col-post-row__meta"><span class="badge badge-info">'
        f'{labels[sec_]}</span><span>{read}</span></span></span></a>'
        for slug, title, sec_, excerpt, read in rows)
    return f'<div class="col-posts">{items}</div>'


def nav_rail(current=None):
    """The left rail: every section, every page under it, with the count beside
    the section name so the rail says how much is in each without expanding."""
    groups = ''
    for s, n, i, summary in SECTIONS:
        pages = in_section(s)
        rows = ''.join(
            f'<a class="list-group__item" href="./post.html"'
            f'{" aria-current=\"page\"" if d[0] == current else ""}>{d[1]}</a>'
            for d in pages)
        groups += (f'<p class="row-between t-slate-sm u-mt-5 u-mb-2" '
                   f'style="color:var(--fg-faint)"><span>{n}</span>'
                   f'<span>{len(pages)}</span></p>'
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
  <div class="container-wide">
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
  <section class="container-wide section-sm">
    {sec('Sections',
         f'{len(SECTIONS)} sections, {len(DOCS)} pages. Each card shows what is '
         f'inside it and how long it takes, both counted from the pages '
         f'themselves rather than typed in by hand.')}
    {sections_block()}
  </section>

  <section class="container-wide section-sm">
    {sec('All pages', f'All {len(DOCS)}, with the section each belongs to.')}
    {docs_list()}
    <div class="u-mt-6">{pagination(1, 2, href='./index.html', label='Docs')}</div>
  </section>
  </div>'''
    return page(HERE, 'index.html', 'Docs — Swarnil',
                'A reusable documentation template: sections, posts and a '
                'component reference.', body, NAME, current='docs')


def route_section():
    """One section, its pages, and the nav rail — full width, because a docs
    section with a rail beside it in a narrow column is a rail squeezing the
    content it is meant to support."""
    slug, name, ico, summary = SECTIONS[0]
    pages = in_section(slug)
    mins = sum(int(d[4].split()[0]) for d in pages)
    body = f'''
  <div class="container-wide section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Docs</a> <span>/</span> <span>{name}</span>
    </nav>

    <div class="grid-rail-left">
      <nav class="col-rail col-rail-sticky" aria-label="Documentation">
        {nav_rail()}
      </nav>

      <div>
        <span class="hero__eyebrow">{icon(ico, group='creator')}Section</span>
        <h1 class="t-display-2 u-mt-2">{name}</h1>
        <p class="t-lead u-mt-3" style="max-width:var(--measure-lead)">{summary}</p>

        <!-- The count is derived, so it cannot disagree with the list below. -->
        {meta_strip([(str(len(pages)), 'pages'), (f'{mins}', 'min read'),
                     (str(len(SECTIONS)), 'sections in all')],
                    paper=True, border=False, inline=True)}

        <div class="u-mt-8">{docs_list(section=slug)}</div>

        <div class="u-mt-10">
          {sec('Other sections', 'The rest of the documentation.')}
          <div class="col-groups">
            {''.join(f'<a class="col-group" href="./section.html">'
                     f'<span class="col-group__ico">{icon(i, group="creator")}</span>'
                     f'<span><span class="col-group__name">{n}</span>'
                     f'<span class="col-group__n">{len(in_section(s))} pages</span>'
                     f'</span></a>'
                     for s, n, i, _ in SECTIONS if s != slug)}
          </div>
        </div>
      </div>
    </div>
  </div>'''
    return page(HERE, 'section.html', f'{name} — Docs — Swarnil', summary,
                body, NAME, current='docs')


def route_post():
    body = f'''
  <div class="container-wide section-sm">
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
  <div class="container-wide section-sm">
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
          <div class="table-wrap"><table class="table">
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
