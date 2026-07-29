#!/usr/bin/env python3
"""The projects collection — /projects, one project, and one of its logs.

Three routes rather than the usual five: an archive, a project, and a log
entry. A project has no "group" or "series" in the collection's sense — the
log IS its series, ordered by construction, so it reuses .buildlog (already
built for exactly "a beat, then another beat, then ship") instead of a new
timeline.

The GitHub-style card is .c-project — a logo tile and a stack row, both
already defined in 23-collection.css and, like .c-newsletter before it,
never used anywhere until now.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import icon, ph, page, sec, hero, meta_strip, pagination   # noqa: E402

NAME = 'Projects'

PROJECTS = [
    ('creator-design-system', 'Creator Design System',
     'A token-first CSS design system for creators — tokens, components, '
     'sections and six collections built on top of them.',
     'CSS', '#563d7c', 128, '2d ago', ['CSS', 'Python', 'Design systems']),
    ('fieldnote', 'Fieldnote',
     'A marketing site rebuilt on a token-first stylesheet with no framework, '
     'shipping two thirds less CSS than the version it replaced.',
     'CSS', '#563d7c', 64, '3mo ago', ['CSS', 'Performance']),
    ('component-playground', 'Component Playground',
     'An internal tool for previewing every component in both themes before '
     'it ships anywhere real.',
     'JavaScript', '#f1e05a', 41, '5mo ago', ['JavaScript', 'Accessibility']),
    ('creator-cli', 'creator-cli',
     'A small CLI that scaffolds a new collection from the default one and '
     'wires it into the docs build.',
     'Python', '#3572A5', 19, '7mo ago', ['Python', 'CLI']),
]

# id, date, title, body, kind (start · '' · ship)
LOG = [
    (6, 'Jul 22, 2026', 'Ship v1', 'Tagged, published to the CDN, and the '
     'install snippet in the README points at a real version number for the '
     'first time.', 'ship'),
    (5, 'Jul 18, 2026', 'Six collections, one contract',
     'Webseries proved the last of the shared sections weren\'t travel- or '
     'course-shaped. That was the bar for calling the vocabulary done.', ''),
    (4, 'Jul 09, 2026', 'The docs site',
     'Every page generated from the same content modules the components '
     'demo from — a docs page that reimplements what it documents is a '
     'second source of truth.', ''),
    (3, 'Jun 28, 2026', 'Components pass',
     'Buttons through navbar, states and all. This is where the token count '
     'stopped moving and the component count started.', ''),
    (2, 'Jun 12, 2026', 'Foundation tokens land',
     'Colour, type, space, elevation, motion, layout — the ladders '
     'everything else reads from, decided once.', ''),
    (1, 'Jun 02, 2026', 'Kick-off — scope and sketches',
     'The argument was always the same one: which grey, which radius, where '
     'the curriculum goes. So I wrote the answers down as tokens instead of '
     'having the argument again.', 'start'),
]

GALLERY = ['tokens', 'components', 'collections', 'docs', 'icons', 'motion']


def project_card(slug, name, desc, lang, color, stars, updated, tags):
    return f'''
    <a class="c c-project" href="./project.html">
      <span class="c__logo">{ph(slug)}</span>
      <div class="c__body">
        <h3 class="c__title">{name}</h3>
        <p class="c__excerpt">{desc}</p>
        <div class="c__stack">{''.join(f'<span class="badge">{t}</span>' for t in tags)}</div>
      </div>
      <div class="c__foot">
        <span><span class="dot dot-sm" style="background:{color}"></span>{lang}</span>
        <span>{icon('star', group='ui')}{stars}</span>
        <span>Updated {updated}</span>
      </div>
    </a>'''


def projects_block(limit=None):
    rows = PROJECTS[:limit] if limit else PROJECTS
    cards = ''.join(project_card(*p) for p in rows)
    return f'<div class="stack-sm">{cards}</div>'


def log_timeline(entries, linkable=False):
    """.buildlog, unmodified — a project log already is "a beat, then
    another beat, then ship"."""
    items = ''.join(
        f'<li class="buildlog__step" data-kind="{kind}"{" data-done" if kind else ""}>'
        f'<span class="buildlog__node"></span>'
        f'<a class="buildlog__link" href="{"./log.html" if linkable else "#i"}">{title}'
        f'<span class="buildlog__date">{date}</span></a></li>'
        for lid, date, title, body, kind in entries)
    return f'<ol class="buildlog">{items}</ol>'


def gallery_block(seeds):
    tiles = ''.join(
        f'<div class="surface" style="overflow:hidden;border-radius:var(--radius-card)">'
        f'<div style="aspect-ratio:4/3">{ph(s)}</div></div>' for s in seeds)
    return f'<div class="grid-auto-sm">{tiles}</div>'


def star_button(count=128):
    return f'''<button class="btn btn-secondary btn-sm btn-star" type="button"
      data-star aria-pressed="false">{icon('star', group='ui')}
      <span data-star-count>{count}</span></button>'''


STAR_SCRIPT = '''
  <script>
  (function () {
    var btn = document.querySelector('[data-star]');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var on = btn.getAttribute('aria-pressed') === 'true';
      var n = btn.querySelector('[data-star-count]');
      n.textContent = String(Number(n.textContent) + (on ? -1 : 1));
      btn.setAttribute('aria-pressed', String(!on));
    });
  })();
  </script>'''


def route_index():
    body = f'''
  <div class="container">
    <section class="hero hero-split hero-sm pattern pattern-circuit pattern-lg fade-corners"
             style="padding-block:var(--space-10) var(--space-8);border-radius:var(--radius-sheet);
                    max-width:calc(var(--w-site) - 4rem);margin-inline:auto">
      <div>
        <span class="hero__eyebrow">{icon('take', group='creator')}The projects collection</span>
        <h1 class="hero__title">Things I built, <em>and kept building</em>.</h1>
        <p class="hero__lead">Four repos, each with its own log — a beat at a time, the
          same way the code shipped.</p>
        {meta_strip([('4', 'projects'), ('252', 'stars'), ('6', 'log entries'),
                     ('2026', 'latest')], paper=True, border=False, inline=True)}
      </div>
      <div class="hero-split__stage">
        {project_card(*PROJECTS[0])}
      </div>
    </section>
  </div>

  <div data-collection>
  <section class="container section-sm">
    {sec('All projects', 'Newest activity first.')}
    {projects_block()}
    <div class="u-mt-6">{pagination(1, 1, href='./index.html', label='Projects')}</div>
  </section>
  </div>'''
    return page(HERE, 'index.html', 'Projects — Swarnil',
                'Four repos, each with its own build log.', body, NAME,
                own_css='projects.css', current='projects')


def route_project():
    slug, name, desc, lang, color, stars, updated, tags = PROJECTS[0]
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Projects</a> <span>/</span> <span>{name}</span>
    </nav>

    <header class="proj-hero surface u-mb-8" style="padding:var(--space-8);border-radius:var(--radius-sheet)">
      <div class="u-flex u-gap-6 u-wrap" style="align-items:flex-start">
        <span class="c__logo" style="width:4.5rem;height:4.5rem;overflow:hidden;
              display:grid;place-items:center;border-radius:var(--radius-md);
              background:var(--bg-muted);flex:none">{ph(slug)}</span>
        <div style="flex:1;min-width:16rem">
          <h1 class="t-display-2">{name}</h1>
          <p class="t-lead u-mt-3" style="max-width:var(--measure-lead)">{desc}</p>
          <div class="cluster u-mt-4">{''.join(f'<span class="badge">{t}</span>' for t in tags)}</div>
          <div class="cluster u-mt-6" style="gap:var(--space-3)">
            {star_button(stars)}
            <a class="btn btn-primary btn-sm" href="#i">{icon('external', group='ui')}Live demo</a>
            <a class="btn btn-secondary btn-sm" href="https://github.com/imswarnil/{slug}"
               target="_blank" rel="noopener">GitHub →</a>
          </div>
        </div>
      </div>
    </header>

    {sec('Showcase', 'Screens from the build, roughly in the order they happened.')}
    {gallery_block(GALLERY)}

    <div class="u-mt-10">
      {sec('Project log', 'Every entry links to its own page — the log is the series '
           'this collection does not otherwise have.')}
      {log_timeline(LOG, linkable=True)}
    </div>

    <div class="grid-2 u-mt-10" style="gap:var(--space-8)">
      <div>
        {sec('Inspiration')}
        <p class="u-fg-subtle">Every design system I'd used made the same trade: fast to
          start, expensive to rebrand. I wanted the opposite trade — a slower first day,
          and a rebrand that's one file.</p>
      </div>
      <div>
        {sec('Conclusion')}
        <p class="u-fg-subtle">Six collections in, the shared vocabulary has held. The
          real test wasn't the first collection — it was whether the second one needed
          new CSS. Four of six didn't.</p>
      </div>
    </div>

    <div class="u-mt-10">
      {sec('Case study', 'The short version, for anyone who wants the receipts before '
           'the log.')}
      <div class="col-checks">
        <span class="col-check"><span class="col-check__tick">{icon('check', group='ui')}</span>
          <span>Six collections built on one shared section vocabulary</span></span>
        <span class="col-check"><span class="col-check__tick">{icon('check', group='ui')}</span>
          <span>Zero new CSS for four of the six — the vocabulary held</span></span>
        <span class="col-check"><span class="col-check__tick">{icon('check', group='ui')}</span>
          <span>One design token change reaches every page, every collection</span></span>
      </div>
    </div>
  </div>{STAR_SCRIPT}'''
    return page(HERE, 'project.html', f'{name} — Projects — Swarnil', desc, body, NAME,
                own_css='projects.css', current='projects')


def route_log():
    slug, name, *_ = PROJECTS[0]
    entry = LOG[0]
    lid, date, title, text, kind = entry
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Projects</a> <span>/</span>
      <a href="./project.html">{name}</a> <span>/</span> <span>Log</span>
    </nav>

    <header class="proj-hero-sm surface u-mb-8"
            style="padding:var(--space-5) var(--space-6);border-radius:var(--radius-sheet);
                   display:flex;align-items:center;gap:var(--space-4)">
      <span class="c__logo" style="width:2.75rem;height:2.75rem;overflow:hidden;
            display:grid;place-items:center;border-radius:var(--radius-md);
            background:var(--bg-muted);flex:none">{ph(slug)}</span>
      <div>
        <span class="t-slate-sm" style="color:var(--fg-faint)">{name} · log #{lid}</span>
        <h1 class="t-h3" style="margin-top:2px">{title}</h1>
      </div>
      <a class="btn btn-secondary btn-sm u-ms-auto" href="./project.html">
        ← Back to project</a>
    </header>

    <div class="content" style="max-width:var(--measure-lead)">
      <p class="t-slate-sm" style="color:var(--fg-faint)">{date}</p>
      <p>{text}</p>
    </div>

    <div class="u-mt-10">
      {sec('The rest of the log')}
      {log_timeline(LOG)}
    </div>
  </div>'''
    return page(HERE, 'log.html', f'{title} — {name} — Projects',
                text, body, NAME, own_css='projects.css', current='projects')


if __name__ == '__main__':
    made = [route_index(), route_project(), route_log()]
    print('projects: ' + ', '.join(made))
