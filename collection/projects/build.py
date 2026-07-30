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

from shell import (icon, ph, page, sec, hero, meta_strip, pagination,   # noqa: E402
                   stats, cta_sponsor, timeline, win_browser, alert, REL)

NAME = 'Projects'

# slug, name, description, language, language colour, stars, forks, updated,
# topics, live demo URL (None = nothing deployed), licence
PROJECTS = [
    ('creator-design-system', 'Creator Design System',
     'A token-first CSS design system for creators — tokens, components, '
     'sections and twelve collections built on top of them.',
     'CSS', '#563d7c', 128, 14, '2d ago',
     ['css', 'design-system', 'design-tokens', 'ui-kit'],
     'creator.imswarnil.com', 'MIT'),
    ('fieldnote', 'Fieldnote',
     'A marketing site rebuilt on a token-first stylesheet with no framework, '
     'shipping two thirds less CSS than the version it replaced.',
     'CSS', '#563d7c', 64, 6, '3mo ago',
     ['css', 'performance', 'static-site'], 'fieldnote.dev', 'MIT'),
    ('component-playground', 'Component Playground',
     'An internal tool for previewing every component in both themes before '
     'it ships anywhere real.',
     'JavaScript', '#f1e05a', 41, 3, '5mo ago',
     ['javascript', 'accessibility', 'tooling'], None, 'MIT'),
    ('creator-cli', 'creator-cli',
     'A small CLI that scaffolds a new collection from the default one and '
     'wires it into the docs build.',
     'Python', '#3572A5', 19, 2, '7mo ago',
     ['python', 'cli', 'codegen'], None, 'MIT'),
]

# The language breakdown for the featured repo — .progress-split, the one thing
# a GitHub repo page has that this system had no atom for.
LANGUAGES = [('CSS', 62.4, '#563d7c'), ('Python', 28.1, '#3572A5'),
             ('JavaScript', 8.2, '#f1e05a'), ('Other', 1.3, '#8b949e')]

RELEASES = [('v0.1.0', 'Jul 22, 2026', 'Latest'), ('v0.0.9', 'Jun 30, 2026', ''),
            ('v0.0.8', 'Jun 12, 2026', '')]

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


def project_card(slug, name, desc, lang, color, stars, forks, updated, topics,
                 demo, licence, wide=False):
    """The repo card, read off a real GitHub listing: owner/name, a Public
    chip, the description, topics as pills, then the footer line — language
    dot, stars, forks, licence, last activity. `.c-project` already shipped the
    logo tile and the stack row; what was missing was everything in the footer
    that makes a repo card a repo card rather than a blog card with a logo."""
    live = (f'<span>{icon("external", group="ui")}'
            f'<span class="u-sr-only">Live at </span>{demo}</span>') if demo else ''
    return f'''
    <a class="c c-project{' c-project-wide' if wide else ''}" href="./project.html">
      <span class="c__logo">{ph(slug)}</span>
      <div class="c__body">
        <h3 class="c__title"><span class="u-fg-faint"
          style="font-weight:var(--weight-regular)">imswarnil/</span>{slug}</h3>
        <p class="c__excerpt">{desc}</p>
        <div class="c__stack">{''.join(
            f'<span class="badge badge-info">{t}</span>' for t in topics)}</div>
      </div>
      <div class="c__foot">
        <span><span class="dot dot-sm" style="background:{color}"></span>{lang}</span>
        <span>{icon('star', group='ui')}{stars}</span>
        <span>{icon('copy', group='ui')}{forks}</span>
        <span>{licence}</span>
        {live}
        <span>Updated {updated}</span>
      </div>
    </a>'''


def projects_block(limit=None, cols=3):
    """A three-up grid by default — a portfolio is compared, and comparing means
    seeing several at once. `cols=1` switches to the wide row variant, which is
    a different card rather than the same one stretched."""
    rows = PROJECTS[:limit] if limit else PROJECTS
    if cols == 1:
        return ('<div class="stack-sm">'
                + ''.join(project_card(*p, wide=True) for p in rows) + '</div>')
    return (f'<div class="grid-{cols}">'
            + ''.join(project_card(*p) for p in rows) + '</div>')


def log_timeline(entries, linkable=False):
    """.buildlog, unmodified — a project log already is "a beat, then
    another beat, then ship". The generic `.tl` in 35-timeline.css is what to
    reach for when the sequence is NOT a project; here the ▸/✓ glyphs and the
    "walked" rail are exactly the subject, so the dressed version wins."""
    items = ''.join(
        f'<li class="buildlog__step" data-kind="{kind}"{" data-done" if kind else ""}>'
        f'<span class="buildlog__node"></span>'
        f'<a class="buildlog__link" href="{"./log.html" if linkable else "#i"}">{title}'
        f'<span class="buildlog__date">{date}</span></a></li>'
        for lid, date, title, body, kind in entries)
    return f'<ol class="buildlog">{items}</ol>'


def language_bar(langs=LANGUAGES):
    """`.progress-split` + `.progress__key` — the proportional breakdown, with
    the legend that makes the colours mean something."""
    segs = ''.join(f'<span class="progress__seg" style="--value:{pct}%;--seg:{c}"></span>'
                   for _, pct, c in langs)
    key = ''.join(f'<span><span class="dot dot-sm" style="background:{c}"></span>'
                  f'{n} <span class="u-fg-faint">{pct}%</span></span>'
                  for n, pct, c in langs)
    return (f'<div class="progress progress-split">{segs}</div>'
            f'<div class="progress__key">{key}</div>')


def log_rail(active=None):
    """The build log as a rail list. `.list-group` draws the rows; the walked /
    current marking comes from `.log-rail__item[aria-current]` so the rail and
    the log itself never disagree about where you are."""
    rows = ''.join(
        f'<a class="list-group__item log-rail__item" href="./log.html"'
        f'{" aria-current=\"page\"" if lid == active else ""}>'
        f'<span class="log-rail__no">{lid:02d}</span>'
        f'<span><span style="display:block">{title}</span>'
        f'<span class="t-slate-sm" style="color:var(--fg-faint)">{date}</span></span></a>'
        for lid, date, title, body, kind in LOG)
    return f'<div class="list-group list-group-flush">{rows}</div>'


def related_block(exclude=0, limit=3):
    """Other projects, at the end of a project page. A portfolio's job is to
    keep someone reading — a project page that dead-ends is a page that ends
    the visit."""
    rows = [p for i, p in enumerate(PROJECTS) if i != exclude][:limit]
    return '<div class="grid-3">' + ''.join(project_card(*p) for p in rows) + '</div>'


def log_pager(active):
    """Prev / next between log entries. LOG is newest-first, so "older" is a
    HIGHER index and "newer" a lower one — the labels say which, because
    ← and → alone are ambiguous on a list sorted this way."""
    ids = [l[0] for l in LOG]
    i = ids.index(active)
    newer = LOG[i - 1] if i > 0 else None
    older = LOG[i + 1] if i < len(LOG) - 1 else None

    def side(entry, label, cls):
        if not entry:
            return (f'<span class="btn btn-quiet btn-sm" aria-disabled="true" '
                    f'tabindex="-1">{label}</span>')
        return (f'<a class="btn {cls} btn-sm" href="./log.html">'
                f'{label}<span class="u-sr-only">: {entry[2]}</span></a>')

    return f'''<nav class="pagination u-mt-10" aria-label="Log entries">
      {side(newer, '← Newer entry', 'btn-secondary')}
      <span class="pagination__pages">
        <span class="t-slate-sm" style="color:var(--fg-faint)">
          Entry {i + 1} of {len(LOG)}</span>
      </span>
      {side(older, 'Older entry →', 'btn-secondary')}
    </nav>'''


def sidebar(slug, name, desc, lang, color, stars, forks, updated, topics,
            demo, licence, log=True):
    """The repo sidebar — GitHub's "About" rail, which is where the live URL,
    the topics and the counts actually belong. Everything in it is an existing
    widget: `.col-widget`, `.stats-bare`, `.progress-split`, `.list-group`."""
    live = (f'<a class="btn btn-primary btn-sm u-w-full" href="https://{demo}" '
            f'target="_blank" rel="noopener">{icon("external", group="ui")}'
            f'Live demo</a>') if demo else (
            f'<p class="t-slate-sm" style="color:var(--fg-faint)">'
            f'Nothing deployed — it is a CLI.</p>')
    rels = ''.join(
        f'<a class="list-group__item" href="#i">{tag}'
        f'{f" <span class=\"badge badge-live\">{note}</span>" if note else ""}'
        f'<span class="u-ms-auto t-slate-sm" style="color:var(--fg-faint)">{when}</span></a>'
        for tag, when, note in RELEASES)
    # The build log lives in the rail on a project page — it is navigation
    # between log entries, and navigation belongs beside the content rather
    # than as a block halfway down it. .col-rail-scroll lets the rail keep its
    # own end reachable once six entries make it taller than the viewport.
    logw = f'''
      <div class="col-widget">
        <span class="col-widget__title">Build log</span>
        {log_rail()}
      </div>''' if log else ''

    return f'''<aside class="col-rail col-rail-sticky col-rail-scroll">
      <div class="col-widget">
        <span class="col-widget__title">About</span>
        <p class="t-small u-fg-subtle">{desc}</p>
        <div class="cluster u-mt-4" style="gap:var(--space-1)">
          {''.join(f'<a class="col-tag" href="#i">{t}</a>' for t in topics)}
        </div>
        <div class="stack-sm u-mt-5">
          {live}
          <a class="btn btn-secondary btn-sm u-w-full"
             href="https://github.com/imswarnil/{slug}" target="_blank" rel="noopener">
            {icon('external', group='ui')}Repository</a>
        </div>
      </div>

      <div class="col-widget">
        <span class="col-widget__title">Activity</span>
        {stats([(str(stars), 'Stars'), (str(forks), 'Forks'), (licence, 'Licence')],
               bare=True)}
      </div>

      <div class="col-widget">
        <span class="col-widget__title">Languages</span>
        {language_bar()}
      </div>

      <div class="col-widget">
        <span class="col-widget__title">Releases</span>
        <div class="list-group list-group-flush">{rels}</div>
      </div>
      {logw}

      <!-- The ask. A project page is the most likely place someone decides
           they want to work with you, so this is where it goes — not buried
           on the contact page. -->
      <div class="col-widget col-widget-accent">
        <span class="col-widget__title">Available for work</span>
        <p class="t-small">Design-system work — tokens, component libraries, and
          migrating a site onto one.</p>
        <div class="stack-sm u-mt-4">
          <a class="btn btn-primary btn-sm u-w-full" href="{REL}/collection/_pages/contact.html">
            Hire me →</a>
          <a class="btn btn-quiet btn-sm u-w-full" href="{REL}/collection/_pages/resume.html">
            {icon('briefcase', group='resume')}Check my résumé</a>
        </div>
      </div>
    </aside>'''


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
    total_stars = sum(p[5] for p in PROJECTS)
    # The hero shows the flagship project actually running, in browser chrome,
    # rather than describing it — a projects index whose hero is a paragraph is
    # the one page where "show, don't tell" is free.
    body = f'''
  <div class="container">
    <section class="hero hero-split pattern pattern-circuit pattern-lg fade-corners"
             style="padding-block:var(--space-12) var(--space-10);
                    border-radius:var(--radius-sheet);
                    max-width:calc(var(--w-site) - 4rem);margin-inline:auto">
      <div>
        <span class="hero__eyebrow">{icon('take', group='creator')}The projects collection</span>
        <h1 class="hero__title">Things I built, <em>and kept building</em>.</h1>
        <p class="hero__lead">{len(PROJECTS)} repos, each with its own log — a beat at a
          time, in the order the code actually shipped.</p>
        <div class="hero__actions">
          <a class="btn btn-primary btn-pill" href="./project.html">
            Read the flagship →</a>
          <a class="btn btn-secondary btn-pill" href="{REL}/collection/_pages/contact.html">
            Hire me</a>
        </div>
        {meta_strip([(str(len(PROJECTS)), 'projects'), (str(total_stars), 'stars'),
                     (str(len(LOG)), 'log entries'), ('MIT', 'licence')],
                    paper=True, border=False, inline=True)}
      </div>
      <div class="hero-split__stage">
        {win_browser('creator.imswarnil.com',
                     f'<div class="pattern pattern-topo pattern-media">{ph("tokens", tall=True)}</div>')}
        <p class="hero-split__caption"><span>The flagship, deployed</span>
          <span class="timecode">v0.1.0</span></p>
      </div>
    </section>
  </div>

  <div data-collection>
  <section class="container section-sm">
    {sec('All projects', 'Newest activity first — the same card GitHub would show you.')}
    {projects_block()}
    <div class="u-mt-6">{pagination(1, 1, href='./index.html', label='Projects')}</div>
  </section>

  <section class="container section-sm">
    {sec('Where the time went', 'Every project on one rail — the generic '
         '<code class="t-code">.tl</code>, because across four repos this is a '
         'history rather than the build log of any one of them.')}
    {timeline([
        dict(time='2026', title='Creator Design System', kind='now',
             note='Twelve collections on one shared shell. Still shipping.',
             meta=['CSS', 'Python'], href='./project.html'),
        dict(time='2026', title='creator-cli', done=True,
             note='Scaffolds a collection and wires it into the docs build.',
             meta=['Python']),
        dict(time='2025', title='Component Playground', done=True,
             note='Every component, both themes, before it ships anywhere real.',
             meta=['JavaScript']),
        dict(time='2025', title='Fieldnote', done=True, kind='start',
             note='Two thirds less CSS than the version it replaced.',
             meta=['CSS']),
    ], axis='h')}
  </section>

  <section class="container section-sm">
    {cta_sponsor('Building something that needs a design system?',
        kicker=f'{icon("take", group="creator")}Available for work',
        actions=f'<a class="btn btn-primary" href="{REL}/collection/_pages/contact.html">'
                f'Hire me →</a>'
                f'<a class="btn btn-secondary" href="{REL}/collection/_pages/resume.html">'
                f'Check my résumé</a>')}
  </section>
  </div>'''
    return page(HERE, 'index.html', 'Projects — Swarnil',
                f'{len(PROJECTS)} repos, each with its own build log.', body, NAME,
                own_css='projects.css', current='projects')


def route_project():
    p = PROJECTS[0]
    slug, name, desc, lang, color, stars, forks, updated, topics, demo, licence = p
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Projects</a> <span>/</span> <span>{name}</span>
    </nav>

    <header class="proj-hero surface u-mb-8"
            style="padding:var(--space-8);border-radius:var(--radius-sheet)">
      <div class="u-flex u-gap-6 u-wrap" style="align-items:flex-start">
        <span class="c__logo" style="width:4.5rem;height:4.5rem;overflow:hidden;
              display:grid;place-items:center;border-radius:var(--radius-md);
              background:var(--bg-muted);flex:none">{ph(slug)}</span>
        <div style="flex:1;min-width:16rem">
          <span class="t-slate-sm" style="color:var(--fg-faint)">imswarnil / {slug}</span>
          <h1 class="t-display-2 u-mt-2">{name}</h1>
          <p class="t-lead u-mt-3" style="max-width:var(--measure-lead)">{desc}</p>
          <div class="cluster u-mt-6" style="gap:var(--space-3)">
            {star_button(stars)}
            <a class="btn btn-primary btn-sm" href="https://{demo}"
               target="_blank" rel="noopener">{icon('external', group='ui')}Live demo</a>
            <a class="btn btn-secondary btn-sm" href="https://github.com/imswarnil/{slug}"
               target="_blank" rel="noopener">GitHub →</a>
          </div>
        </div>
      </div>
    </header>

    <!-- Content in the main column, the repo's own facts in the rail. The rail
         is where the live URL, the topics, the counts and the ask belong —
         everything a reader wants to ACT on rather than read. -->
    <div class="grid-rail">
      <div>
        {sec('Showcase', 'Screens from the build, roughly in the order they happened.')}
        {gallery_block(GALLERY)}

        <div class="u-mt-10">
          {sec('Case study', 'The short version, for anyone who wants the receipts '
               'before the log.')}
          <div class="col-checks">
            {''.join(f'<span class="col-check"><span class="col-check__tick">'
                     f'{icon("check", group="ui")}</span><span>{t}</span></span>'
                     for t in [
                'Twelve collections built on one shared section vocabulary',
                'Zero new CSS for eight of the twelve — the vocabulary held',
                'One token change reaches every page, every collection',
                '37 KB gzipped, no dependencies, no build step required'])}
          </div>
        </div>

        <div class="grid-2 u-mt-10" style="gap:var(--space-8)">
          <div>
            {sec('Inspiration')}
            <p class="u-fg-subtle">Every design system I had used made the same trade:
              fast to start, expensive to rebrand. I wanted the opposite trade — a
              slower first day, and a rebrand that is one file.</p>
          </div>
          <div>
            {sec('Conclusion')}
            <p class="u-fg-subtle">Twelve collections in, the shared vocabulary has
              held. The real test was never the first collection — it was whether the
              second one needed new CSS. Eight of twelve did not.</p>
          </div>
        </div>

        <div class="u-mt-10">
          {alert('Everything on this page is generated from '
                 '<code class="t-code">collection/projects/build.py</code> — the card, '
                 'the rail, the log and the language bar all read the same list.',
                 tone='info', ico='search')}
        </div>
      </div>

      {sidebar(*p)}
    </div>

    <!-- A project page that dead-ends is a page that ends the visit. -->
    <div class="u-mt-12">
      {sec('Other projects', 'Three more, newest activity first.')}
      {related_block(exclude=0)}
      <div class="u-mt-6">
        <a class="btn btn-secondary btn-pill" href="./index.html">All projects →</a>
      </div>
    </div>
  </div>{STAR_SCRIPT}'''
    return page(HERE, 'project.html', f'{name} — Projects — Swarnil', desc, body, NAME,
                own_css='projects.css', current='projects')


def route_log():
    p = PROJECTS[0]
    slug, name, desc, lang, color, stars, forks, updated, topics, demo, licence = p
    # Entry 3 rather than the first, so the rail, the pager and the "walked"
    # rail all have something on both sides of them to show.
    entry = next(l for l in LOG if l[0] == 3)
    lid, date, title, text, kind = entry

    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Projects</a> <span>/</span>
      <a href="./project.html">{name}</a> <span>/</span> <span>Log {lid:02d}</span>
    </nav>

    <!-- The project header, kept — just short and pinned. Shares
         view-transition-name with the tall version on the project page, so
         navigating between them morphs the header instead of replacing it. -->
    <header class="proj-hero-sm surface u-mb-8"
            style="padding:var(--space-4) var(--space-5);border-radius:var(--radius-sheet);
                   display:flex;align-items:center;gap:var(--space-4);flex-wrap:wrap">
      <span class="c__logo" style="width:2.5rem;height:2.5rem;overflow:hidden;
            display:grid;place-items:center;border-radius:var(--radius-md);
            background:var(--bg-muted);flex:none">{ph(slug)}</span>
      <div style="flex:1;min-width:10rem">
        <span class="t-slate-sm" style="color:var(--fg-faint)">
          imswarnil / {slug}</span>
        <span style="display:block;font-weight:var(--weight-semibold)">{name}</span>
      </div>
      <span class="cluster" style="gap:var(--space-2)">
        <a class="btn btn-quiet btn-sm" href="https://{demo}"
           target="_blank" rel="noopener">{icon('external', group='ui')}Demo</a>
        <a class="btn btn-quiet btn-sm" href="https://github.com/imswarnil/{slug}"
           target="_blank" rel="noopener">GitHub</a>
        <a class="btn btn-secondary btn-sm" href="./project.html">← Back to project</a>
      </span>
    </header>

    <div class="grid-rail">
      <article>
        <span class="t-slate-sm" style="color:var(--fg-faint)">
          Log {lid:02d} · {date}</span>
        <h1 class="t-display-2 u-mt-2">{title}</h1>

        <div class="content u-mt-6" style="max-width:var(--measure-lead)">
          <p>{text}</p>
          <p>Each entry is its own page because each one was its own decision.
            The rail on the right is the whole log; the pager at the bottom walks
            it in order.</p>
        </div>

        {log_pager(lid)}

        <!-- The links, at the end, where someone who read the whole entry is. -->
        <div class="u-mt-10">
          {cta_sponsor('Want the code, or the person who wrote it?',
              kicker=f'{icon("take", group="creator")}This project',
              actions=f'<a class="btn btn-primary btn-sm" href="https://{demo}" '
                      f'target="_blank" rel="noopener">Live demo</a>'
                      f'<a class="btn btn-secondary btn-sm" '
                      f'href="https://github.com/imswarnil/{slug}" target="_blank" '
                      f'rel="noopener">GitHub</a>'
                      f'<a class="btn btn-quiet btn-sm" '
                      f'href="{REL}/collection/_pages/contact.html">Hire me</a>')}
        </div>
      </article>

      <aside class="col-rail col-rail-sticky col-rail-scroll">
        <div class="col-widget">
          <span class="col-widget__title">Build log</span>
          {log_rail(active=lid)}
        </div>

        <div class="col-widget">
          <span class="col-widget__title">Progress</span>
          {stats([(f'{sum(1 for l in LOG if l[4])}', 'Shipped'),
                  (str(len(LOG)), 'Entries')], bare=True)}
        </div>
      </aside>
    </div>
  </div>'''
    return page(HERE, 'log.html', f'{title} — {name} — Projects',
                text, body, NAME, own_css='projects.css', current='projects')


if __name__ == '__main__':
    made = [route_index(), route_project(), route_log()]
    print('projects: ' + ', '.join(made))
