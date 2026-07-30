#!/usr/bin/env python3
"""Build the snippets collection's two routes.

    python3 collection/snippets/build.py

A code library: `.c-snippet` for the list (language tag + a fading code
preview), `.codebox` for the single-snippet page — the same box the docs
collection's component reference already uses for a copy-able block.
"""
import html
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import (icon, ph, page, sec, hero, meta_strip, pagination,   # noqa: E402
                   comments, LIKE_SCRIPT, alert)

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
    """Editor chrome, with the title in the window bar.

    `.win.win-code` (12-frame.css) already draws an editor — traffic lights, a
    dark body, a tab strip — and it says "this is code" before a word is read,
    which is exactly a snippet card's whole job. The old version was
    `.c-snippet`, a light card with a faded code preview; this replaces it,
    because a code library that does not look like an editor is making the
    reader work out what it is.

    The <code> carries data-lang, which is what src/highlight.js reads."""
    lines = code.split('\n')
    gutter = '<br />'.join(str(i + 1) for i in range(len(lines)))
    esc = html.escape(code)
    return f'''<a class="c win win-code snip-card" href="./snippet.html"
       data-post data-tags="{lang}">
      <span class="win__bar">
        <span class="win__dots"><span></span><span></span><span></span></span>
        <span class="win__title">{title}</span>
        <span class="snip-card__lang">{lang}</span>
      </span>
      <span class="win__body snip-card__body">
        <span class="win-code__gutter">{gutter}</span>
        <pre class="win-code__lines"><code data-lang="{lang}">{esc}</code></pre>
      </span>
    </a>'''


def snippets_block(limit=None):
    rows = SNIPPETS[:limit] if limit else SNIPPETS
    return '<div class="grid-3">' + ''.join(snippet_card(*s) for s in rows) + '</div>'


def code_block(code, lang='css', title=None):
    """`.codebox` with the language on the caption — which is both what the
    reader needs and what src/highlight.js reads to colour it. data-copy is now
    handled by collection.js, so the button actually works on these pages."""
    return (f'<figure class="codebox u-m-0"><figcaption class="codebox__head">'
            f'<span class="codebox__lang">{lang}</span>'
            f'{f"<span class=\'win__title\'>{title}</span>" if title else ""}'
            f'<button class="codebox__copy" type="button" data-copy>Copy</button>'
            f'</figcaption>'
            f'<pre class="codebox__pre"><code data-lang="{lang}">'
            f'{html.escape(code)}</code></pre></figure>')


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
                body, NAME, own_css='snippets.css', current='snippets')


def route_snippet():
    slug, title, lang, code = SNIPPETS[0]
    langs = sorted({sn[2] for sn in SNIPPETS})
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Snippets</a> <span>/</span> <span>{title}</span>
    </nav>

    <div class="grid-rail">
      <div>
        <span class="c__lang">{lang}</span>
        <h1 class="t-display-2 u-mt-2">{title}</h1>
        <p class="t-lead u-mt-3" style="max-width:var(--measure-lead)">One clamp,
          one rule, and the fluid type scale everywhere on this site.</p>

        <!-- .codebox with data-lang on the <code>: src/highlight.js colours it
             at runtime from that attribute, and collection.js makes the copy
             button work. Both shipped already; neither was wired up here. -->
        <div class="u-mt-8">{code_block(code, lang, title=f'{slug}.{lang}')}</div>

        <div class="content u-mt-8" style="max-width:var(--measure-lead)">
          <h2>Why this works</h2>
          <p>The middle value is the one doing the work: a <code>rem</code> base
            plus a <code>vw</code> term scales with the viewport, and the outer two
            stop it going anywhere silly at either end.</p>
          <h2>What to change</h2>
          <p>The <code>0.5vw</code> term. Raise it for a steeper curve, lower it
            for a flatter one — the two clamps stay as they are.</p>
        </div>

        <div class="u-mt-8">
          {alert('Copy takes the whole block including the comment. The comment is '
                 'the part you will want in six months.', tone='info', ico='search')}
        </div>

        <div class="u-mt-10">
          {sec('More snippets', 'Three others worth a permalink.')}
          {snippets_block(limit=3)}
        </div>

        {comments()}
      </div>

      <aside class="col-rail col-rail-sticky">
        <div class="col-widget">
          <span class="col-widget__title">This snippet</span>
          {meta_strip([(lang.upper(), 'language'), (str(len(code.splitlines())), 'lines'),
                       ('MIT', 'licence')], paper=True, border=False, inline=True)}
        </div>

        <div class="col-widget">
          <span class="col-widget__title">Browser support</span>
          <div class="list-group list-group-flush">
            {''.join(f'<span class="list-group__item">{b}'
                     f'<span class="u-ms-auto">{icon("check", group="ui")}</span></span>'
                     for b in ['Chrome', 'Safari', 'Firefox', 'Edge'])}
          </div>
        </div>

        <div class="col-widget">
          <span class="col-widget__title">By language</span>
          <div class="cluster" style="gap:var(--space-1)">
            {''.join(f'<a class="col-tag" href="./index.html">{l}</a>'
                     for l in langs)}
          </div>
        </div>

        <div class="col-widget col-widget-accent">
          <span class="col-widget__title">The whole library</span>
          <p class="t-small">{len(SNIPPETS)} snippets, all copy-ready.</p>
          <a class="btn btn-primary btn-sm u-w-full u-mt-4" href="./index.html">
            Browse snippets →</a>
        </div>
      </aside>
    </div>
  </div>{LIKE_SCRIPT}'''
    return page(HERE, 'snippet.html', f'{title} — Snippets — Swarnil',
                f'A {lang} snippet — copy the block, ship it.',
                body, NAME, own_css='snippets.css', current='snippets')


if __name__ == '__main__':
    made = [route_index(), route_snippet()]
    print('snippets: ' + ', '.join(made))
