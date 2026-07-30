#!/usr/bin/env python3
"""Build the prompts collection's two routes.

    python3 collection/prompts/build.py

A prompt library: `.c-prompt`'s chat bubble for the list, the same bubble
plus a model tag and a copy button for the single-prompt page.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import (icon, ph, page, sec, hero, meta_strip, pagination,   # noqa: E402
                   comments, LIKE_SCRIPT, alert)

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


def mark_slots(text):
    """`{placeholder}` is the part you are meant to change, so it is marked
    rather than left for the reader to find. Dotted underline as well as colour,
    so it survives greyscale."""
    return re.sub(r'\{(\w+)\}', r'<span class="slot">{\1}</span>', text)


def prompt_card(slug, title, model, body):
    return f'''<a class="c c-prompt" href="./prompt.html">
      <div class="c__bubble">{mark_slots(body)}</div>
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
                body, NAME, own_css='prompts.css', current='prompts')


def route_prompt():
    slug, title, model, prompt_body = PROMPTS[0]
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Prompts</a> <span>/</span> <span>{title}</span>
    </nav>

    <div class="grid-rail">
      <div>
        <span class="c__model">{icon('chat')}{model}</span>
        <h1 class="t-display-2 u-mt-2">{title}</h1>
        <p class="t-lead u-mt-3" style="max-width:var(--measure-lead)">
          Edit it in place, then copy. The highlighted parts are the ones meant
          to change.</p>

        <!-- The prompt as a field, not a code block: a prompt is a template with
             holes in it, so the useful action is "fill this in, then copy" rather
             than "copy this". The textarea carries no chrome of its own — the
             bubble takes the focus ring — because this is prose, not a form. -->
        <div class="c__bubble prompt-field u-mt-6" style="margin:var(--space-6) 0 0">
          <label class="u-sr-only" for="prompt-text">Prompt text, editable</label>
          <textarea class="prompt-edit" id="prompt-text" data-copy-src
                    rows="5" spellcheck="false">{prompt_body}</textarea>
        </div>

        <div class="prompt-bar">
          <span class="t-slate-sm" style="color:var(--fg-faint)">
            Edits stay on this page — nothing is saved or sent.</span>
          <span class="cluster" style="gap:var(--space-2)">
            <button class="btn btn-quiet btn-sm" type="button" data-reset>Reset</button>
            <button class="btn btn-primary btn-sm" type="button" data-copy>
              {icon('copy', group='ui')}Copy prompt</button>
          </span>
        </div>

        <div class="u-mt-8">
          {alert('The slots are named rather than numbered — <code class="t-code">'
                 '{{old}}</code> and <code class="t-code">{{new}}</code> beat '
                 '<code class="t-code">$1</code> and <code class="t-code">$2</code> '
                 'when you are reading a prompt back a month later.',
                 tone='info', ico='search')}
        </div>

        <div class="u-mt-10">
          {sec('More prompts')}
          {prompts_block(limit=3)}
        </div>

        {comments()}
      </div>

      <aside class="col-rail col-rail-sticky">
        <div class="col-widget">
          <span class="col-widget__title">Slots</span>
          <div class="list-group list-group-flush">
            {''.join(f'<span class="list-group__item"><code class="t-code">{{{{{s_}}}}}</code>'
                     f'<span class="u-ms-auto t-slate-sm" '
                     f'style="color:var(--fg-faint)">{d}</span></span>'
                     for s_, d in [('old', 'the current name'),
                                   ('new', 'what to rename it to')])}
          </div>
        </div>

        <div class="col-widget">
          <span class="col-widget__title">Works with</span>
          <div class="cluster" style="gap:var(--space-1)">
            <span class="badge badge-info">Claude</span>
            <span class="badge badge-info">Any coding agent</span>
          </div>
        </div>

        <div class="col-widget col-widget-accent">
          <span class="col-widget__title">The whole library</span>
          <p class="t-small">{len(PROMPTS)} prompts, all copy-ready.</p>
          <a class="btn btn-primary btn-sm u-w-full u-mt-4" href="./index.html">
            Browse prompts →</a>
        </div>
      </aside>
    </div>
  </div>

  <script>
  (function () {{
    // Reset puts the original text back. Kept out of the copy handler so a
    // reader can edit, copy, and still get back to the shipped version.
    var ta = document.getElementById('prompt-text');
    var btn = document.querySelector('[data-reset]');
    if (!ta || !btn) return;
    var original = ta.value;
    btn.addEventListener('click', function () {{ ta.value = original; ta.focus(); }});
  }})();
  </script>{LIKE_SCRIPT}'''
    return page(HERE, 'prompt.html', f'{title} — Prompts — Swarnil',
                f'A reusable {model} prompt — edit the slots, then copy.',
                body, NAME, own_css='prompts.css', current='prompts')


if __name__ == '__main__':
    made = [route_index(), route_prompt()]
    print('prompts: ' + ', '.join(made))
