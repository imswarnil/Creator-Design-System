"""The shared page shell every collection builds on.

A collection's own build.py brings its data and its sections; this brings the
head, the navbar, the footer and the small helpers all of them need. Without
it, each new collection starts by copying eighty lines of <head> from the last
one, and they drift apart from the first edit.
"""
import html
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
REL = '../..'          # from collection/<name>/*.html back to the repo root


def icon(name, cls='icon', group='travel'):
    """Inline an icon file so it inherits currentColor."""
    for g in (group, 'ui', 'creator', 'media', 'social'):
        p = REPO / 'icons' / g / f'{name}.svg'
        if p.exists():
            return p.read_text().strip().replace(
                '<svg ', f'<svg class="{cls}" aria-hidden="true" ', 1)
    return ''


def ph(seed='default', tall=False):
    """A placeholder that cannot 404.

    Deliberately not a photograph: a demo that ships with stock photography
    teaches that the design needs a good photograph to work. Each seed gets its
    own hue off one ladder, so a grid still reads as a set.
    """
    hues = {'japan': 8, 'vietnam': 150, 'portugal': 205, 'georgia': 265,
            'peru': 32, 'india': 340, 'css': 262, 'motion': 190, 'craft': 24,
            'notes': 96, 'default': 220}
    return (f'<span class="col-ph" style="--h:{hues.get(seed, hues["default"])}"'
            f'{" data-tall" if tall else ""} aria-hidden="true"></span>')


HEAD = '''<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="icon" href="{rel}/docs/favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="{rel}/dist/creator.css" />
<link rel="stylesheet" href="{rel}/collection/collection.css" />{own_css}
<script src="{rel}/src/nav.js" defer></script>
<script src="{rel}/collection/collection.js" defer></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="nav-shell">
  <nav class="nav-bar" aria-label="Main">
    <a class="logo logo-sm" href="{rel}/docs/index.html">Swarnil</a>
    <div class="nav-links">
      <a class="nav-link" href="{rel}/collection/travel/index.html"{cur_travel}>Travel</a>
      <a class="nav-link" href="{rel}/collection/blog/index.html"{cur_blog}>Blog</a>
      <a class="nav-link" href="#i">Watch</a>
    </div>
    <div class="nav-actions">
      <a class="btn btn-primary btn-sm btn-pill" href="#i">Subscribe</a>
    </div>
  </nav>
</header>

<main id="main">
'''

FOOT = '''
</main>

<footer class="section-sm">
  <div class="container">
    <hr class="rule u-mb-6" />
    <div class="row-between">
      <p class="t-slate">{name} — a collection</p>
      <p class="t-slate-sm"><a href="{rel}/collection/README.md">Built from the collection contract</a></p>
    </div>
  </div>
</footer>
</body>
</html>
'''


def page(out_dir, name, title, desc, body, collection='', own_css=None, current=''):
    """Write one route. `own_css` is the collection's own stylesheet, if it has
    one — most do not need any."""
    css = f'\n<link rel="stylesheet" href="./{own_css}" />' if own_css else ''
    doc = (HEAD.format(title=html.escape(title), desc=html.escape(desc), rel=REL,
                       own_css=css,
                       cur_travel=' aria-current="page"' if current == 'travel' else '',
                       cur_blog=' aria-current="page"' if current == 'blog' else '')
           + body + FOOT.format(rel=REL, name=collection))
    (pathlib.Path(out_dir) / name).write_text(doc)
    return name


def sec(title, note='', extra=''):
    n = (f'<p class="t-subtle u-mt-2" style="max-width:var(--measure-lead)">{note}</p>'
         if note else '')
    return (f'<div class="row-between u-mb-5"><div><h2 class="t-h3">{title}</h2>{n}</div>'
            f'{extra}</div>')


def meta_strip(pairs, paper=False):
    cls = 'col-meta col-meta-paper' if paper else 'col-meta'
    return f'<div class="{cls}">' + ''.join(
        f'<div><span class="col-meta__n">{n}</span>'
        f'<span class="col-meta__l">{l}</span></div>' for n, l in pairs) + '</div>'


def hero(title, lead, eyebrow, meta, art='', search=None, eyebrow_icon='pin'):
    """The collection hero. `art` is an optional SVG the collection supplies —
    without one the hero is still a hero, just a quieter one."""
    s = ''
    if search:
        s = f'''
      <form class="col-search" onsubmit="return false">
        <label class="col-search__field">
          <span class="u-sr-only">Search</span>
          {icon('compass')}
          <input type="search" placeholder="{search}" />
        </label>
        <button class="btn btn-primary btn-pill" type="submit">Search</button>
      </form>'''
    return f'''
  <section class="container u-mt-6">
   <div class="col-hero">
    {art}
    <div class="col-hero__in">
      <span class="col-hero__eyebrow">{icon(eyebrow_icon)}{eyebrow}</span>
      <h1 class="col-hero__title">{title}</h1>
      <p class="col-hero__lead">{lead}</p>
      {s}
      {meta_strip(meta)}
    </div>
   </div>
  </section>
'''
