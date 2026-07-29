#!/usr/bin/env python3
"""Build the prompts collection's two routes.

    python3 collection/prompts/build.py

A prompt library: `.c-prompt`'s chat bubble for the list, the same bubble
plus a model tag and a copy button for the single-prompt page.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import icon, ph, page, sec, hero, meta_strip, pagination   # noqa: E402

NAME = 'Prompts'

PROMPTS = [
    ('rename-a-variable', 'Rename a variable everywhere, safely', 'Claude',
     'Rename `{old}` to `{new}` across this file and every file that imports '
     'it. Do not touch unrelated identifiers that happen to share the name.'),
    ('explain-this-regex', 'Explain a regex, plainly', 'Claude',
     'Explain what this regex matches, in plain English, one clause at a '
     'time: `{pattern}`. Then give one input it matches and one it does not.'),
    ('write-a-commit-message', 'Write a commit message from a diff', 'Claude',
     'Read this diff and write a commit message: one line under 70 '
     'characters, then a blank line, then why — not what — in 1-2 sentences.'),
    ('css-token-audit', 'Audit a stylesheet for hardcoded values', 'Claude',
     'List every hardcoded colour, spacing and font-size in this file that '
     'has an equivalent design token, with the line number and the token '
     'that should replace it.'),
    ('reduce-a-bug-report', 'Reduce a bug report to a minimal repro', 'Claude',
     'Take this bug report and strip it to the smallest steps that still '
     'reproduce the issue. Flag anything you removed that might matter.'),
]


def prompt_card(slug, title, model, body):
    return f'''<a class="c c-prompt" href="./prompt.html">
      <div class="c__bubble">{body}</div>
      <div class="c__body">
        <span class="c__model">{icon('chat')}{model}</span>
        <h3 class="c__title">{title}</h3>
      </div>
    </a>'''


def prompts_block(limit=None):
    rows = PROMPTS[:limit] if limit else PROMPTS
    return '<div class="grid-auto-sm">' + ''.join(prompt_card(*p) for p in rows) + '</div>'


def route_index():
    body = f'''
  {hero('Prompts', 'The exact wording I keep reusing, so the good version '
        'has a permalink instead of living in a scrollback somewhere.',
        'Prompt library', [(str(len(PROMPTS)), 'prompts'), ('Claude', 'model')],
        eyebrow_icon='chat', pattern='pattern-dots')}

  <div class="container section-sm" data-collection>
    {sec('All prompts')}
    {prompts_block()}
    <div class="u-mt-6">{pagination(1, 1, href='./index.html', label='Prompts')}</div>
  </div>'''
    return page(HERE, 'index.html', 'Prompts — Swarnil',
                'The exact wording I keep reusing — one permalink per prompt.',
                body, NAME, current='prompts')


def route_prompt():
    slug, title, model, prompt_body = PROMPTS[0]
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Prompts</a> <span>/</span> <span>{title}</span>
    </nav>

    <span class="c__model">{icon('chat')}{model}</span>
    <h1 class="t-display-2 u-mt-2">{title}</h1>

    <div class="c__bubble u-mt-6" style="max-width:var(--measure-lead);margin-left:0">
      {prompt_body}
    </div>
    <button class="btn btn-secondary btn-sm u-mt-4" type="button" data-copy>Copy prompt</button>

    <div class="u-mt-10">
      {sec('More prompts')}
      {prompts_block(limit=3)}
    </div>
  </div>'''
    return page(HERE, 'prompt.html', f'{title} — Prompts — Swarnil',
                f'A reusable {model} prompt — copy it, fill in the blanks.',
                body, NAME, current='prompts')


if __name__ == '__main__':
    made = [route_index(), route_prompt()]
    print('prompts: ' + ', '.join(made))
