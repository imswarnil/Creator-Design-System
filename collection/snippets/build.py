#!/usr/bin/env python3
"""Build the snippets collection's two routes.

    python3 collection/snippets/build.py

A code library: `.c-snippet` for the list (language tag + a fading code
preview), `.codebox` for the single-snippet page — the same box the docs
collection's component reference already uses for a copy-able block.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import icon, ph, page, sec, hero, meta_strip, pagination   # noqa: E402

NAME = 'Snippets'

SNIPPETS = [
    ('clamp-fluid-type', 'Fluid type with one clamp()', 'css',
     'font-size: clamp(1rem, 0.9rem + 0.5vw, 1.5rem);\nline-height: 1.5;'),
    ('grid-auto-fit', 'A grid that wraps itself', 'css',
     'display: grid;\ngrid-template-columns:\n  repeat(auto-fit, minmax(16rem, 1fr));\ngap: var(--space-4);'),
    ('debounce', 'A debounce in six lines', 'js',
     'function debounce(fn, ms) {\n  let t;\n  return (...a) => {\n    clearTimeout(t);\n    t = setTimeout(() => fn(...a), ms);\n  };\n}'),
    ('view-transition-name', 'Morph one element across a navigation', 'css',
     '.hero { view-transition-name: hero; }\n\n@view-transition { navigation: auto; }'),
    ('focus-visible-ring', 'A focus ring that only shows for keyboards', 'css',
     ':focus-visible {\n  outline: 2px solid var(--accent);\n  outline-offset: 2px;\n}'),
    ('copy-to-clipboard', 'Copy to clipboard, with a fallback', 'js',
     'async function copy(text) {\n  try {\n    await navigator.clipboard.writeText(text);\n  } catch {\n    document.execCommand(\'copy\');\n  }\n}'),
]


def snippet_card(slug, title, lang, code):
    return f'''<a class="c c-snippet" href="./snippet.html" data-post data-tags="{lang}">
      <div class="c__body">
        <span class="c__lang">{lang}</span>
        <h3 class="c__title">{title}</h3>
      </div>
      <pre class="c__code">{code}</pre>
    </a>'''


def snippets_block(limit=None):
    rows = SNIPPETS[:limit] if limit else SNIPPETS
    return '<div class="grid-auto-sm">' + ''.join(snippet_card(*s) for s in rows) + '</div>'


def code_block(code, lang='css'):
    return (f'<figure class="codebox codebox-light u-m-0"><figcaption class="codebox__head">'
            f'<span class="codebox__lang">{lang}</span>'
            f'<button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>'
            f'<pre class="codebox__pre"><code>{code}</code></pre></figure>')


def route_index():
    body = f'''
  {hero('Snippets', 'The lines I copy-paste between projects often enough to '
        'give them a permalink instead — CSS first, a little JS.',
        'Code library', [(str(len(SNIPPETS)), 'snippets'), ('2', 'languages')],
        eyebrow_icon='slate', pattern='pattern-grid')}

  <div class="container section-sm" data-collection>
    {sec('All snippets')}
    {snippets_block()}
    <div class="u-mt-6">{pagination(1, 1, href='./index.html', label='Snippets')}</div>
  </div>'''
    return page(HERE, 'index.html', 'Snippets — Swarnil',
                'CSS and JS I copy-paste between projects often enough to permalink.',
                body, NAME, current='snippets')


def route_snippet():
    slug, title, lang, code = SNIPPETS[0]
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Snippets</a> <span>/</span> <span>{title}</span>
    </nav>

    <span class="c__lang">{lang}</span>
    <h1 class="t-display-2 u-mt-2">{title}</h1>
    <p class="t-lead u-mt-3" style="max-width:var(--measure-lead)">One clamp,
      one rule, and the fluid type scale everywhere on this site.</p>

    <div class="u-mt-8">{code_block(code, lang)}</div>

    <div class="u-mt-10">
      {sec('More snippets')}
      {snippets_block(limit=3)}
    </div>
  </div>'''
    return page(HERE, 'snippet.html', f'{title} — Snippets — Swarnil',
                f'A {lang} snippet — copy the block, ship it.',
                body, NAME, current='snippets')


if __name__ == '__main__':
    made = [route_index(), route_snippet()]
    print('snippets: ' + ', '.join(made))
