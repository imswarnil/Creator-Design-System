#!/usr/bin/env python3
"""Build the products-i-use collection's two routes.

    python3 collection/products/build.py

The general "things I use" list — `.c-product`'s thumb + price row, grouped
by what the product is for. The videos collection's own products block
(`collection/videos/build.py:products_block`) is the narrow, video-specific
cut of the same idea; this is the full list with its own home.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import icon, ph, page, sec, hero, meta_strip, pagination   # noqa: E402

NAME = 'Products'

GROUPS = [
    ('hardware', 'Hardware', 'take', 5),
    ('software', 'Software', 'slate', 6),
    ('video', 'Video setup', 'camera', 4),
]

PRODUCTS = [
    ('mbp-16', 'MacBook Pro 16"', 'hardware', '$3499', 'take'),
    ('lg-ultrafine', 'LG UltraFine 5K', 'hardware', '$1299', 'take'),
    ('keychron-q1', 'Keychron Q1', 'hardware', '$179', 'take'),
    ('mx-master-3', 'Logitech MX Master 3S', 'hardware', '$99', 'take'),
    ('standing-desk', 'Fully Jarvis standing desk', 'hardware', '$699', 'take'),
    ('vs-code', 'VS Code', 'software', 'Free', 'slate'),
    ('figma', 'Figma', 'software', '$15/mo', 'slate'),
    ('claude-code', 'Claude Code', 'software', 'Usage-based', 'slate'),
    ('raycast', 'Raycast', 'software', 'Free', 'slate'),
    ('linear', 'Linear', 'software', '$8/mo', 'slate'),
    ('notion', 'Notion', 'software', '$10/mo', 'slate'),
    ('sony-zve10', 'Sony ZV-E10', 'video', '$698', 'camera'),
    ('rode-nt-usb', 'Rode NT-USB Mini', 'video', '$99', 'camera'),
    ('final-cut', 'Final Cut Pro', 'video', '$299', 'camera'),
    ('elgato-key-light', 'Elgato Key Light', 'video', '$199', 'camera'),
]


def product_card(slug, name, group, price, ico):
    return f'''<a class="c c-product" href="#i" data-post data-of="{group}">
      <span class="c__thumb">{icon(ico)}</span>
      <div class="c__body"><span class="c__title">{name}</span></div>
      <span class="c__price">{price}</span>
    </a>'''


def products_block(group=None, limit=None):
    rows = PRODUCTS if not group else [p for p in PRODUCTS if p[2] == group]
    rows = rows[:limit] if limit else rows
    return '<div class="grid-auto-sm">' + ''.join(product_card(*p) for p in rows) + '</div>'


def groups_block():
    return '<div class="col-groups">' + ''.join(
        f'<a class="col-group" href="./index.html" data-group="{g}">'
        f'<span class="col-group__ico">{icon(i)}</span>'
        f'<span><span class="col-group__name">{n}</span>'
        f'<span class="col-group__n">{c} things</span></span></a>'
        for g, n, i, c in GROUPS) + '</div>'


def route_index():
    body = f'''
  {hero('Products I use', 'What is actually on the desk and in the dock — not '
        'an affiliate list, just what stayed after everything else got returned.',
        'Now using', [(str(len(PRODUCTS)), 'things'), (str(len(GROUPS)), 'groups')],
        eyebrow_icon='take', pattern='pattern-glow')}

  <div class="container section-sm" data-collection>
    {sec('By group')}
    {groups_block()}
  </div>

  <div class="container section-sm">
    {sec('Everything')}
    {products_block()}
    <div class="u-mt-6">{pagination(1, 1, href='./index.html', label='Products')}</div>
  </div>'''
    return page(HERE, 'index.html', 'Products I use — Swarnil',
                'Hardware, software and the video setup — what actually stayed.',
                body, NAME, current='products')


if __name__ == '__main__':
    made = [route_index()]
    print('products: ' + ', '.join(made))
