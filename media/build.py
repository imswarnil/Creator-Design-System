#!/usr/bin/env python3
"""Generate the README's specimen SVGs from the system's own token values.

These are pictures of the design system, drawn with the design system's colours
and proportions, so a reader can see what they are getting before they install
anything. They are generated rather than hand-drawn for one reason: when a token
changes, the picture should change with it.

    python3 media/build.py

Every file is self-contained — GitHub loads a README image in an <img>, which
sandboxes it: no external stylesheet, no webfont, no script. So the palette is
inlined and the type falls back to system faces. The real faces are named in
the specimen itself, since the specimen cannot show them.

Each file carries both themes and switches on prefers-color-scheme, which is
the same contract the CSS makes — the picture proves the claim.
"""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent

# ── The tokens these pictures are made of ───────────────────────────────────
INK = ['#fff', '#fcfcfd', '#f8f8fa', '#f1f1f4', '#e5e5ea', '#d3d3db', '#a5a5b2',
       '#76768a', '#55556a', '#3c3c4e', '#272734', '#191922', '#101017', '#08080c']
INK_NAMES = ['0', '25', '50', '100', '200', '300', '400',
             '500', '600', '700', '800', '900', '950', '1000']
SIGNAL = ['#fff2ef', '#ffe1db', '#ffc4b8', '#ff9d89', '#fb7358', '#f04e2e',
          '#dc3514', '#b52810', '#8f2211', '#6f1f12', '#3d0d07']
SIGNAL_NAMES = ['50', '100', '200', '300', '400', '500',
                '600', '700', '800', '900', '950']
ACCENT = '#f04e2e'

DISPLAY = "system-ui,-apple-system,'Segoe UI',Roboto,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

# Light values first, dark under the media query — the same order the CSS uses.
THEME = f'''  <style>
    .bg      {{ fill: #fff; }}
    .surface {{ fill: #f8f8fa; }}
    .hair    {{ stroke: #e5e5ea; fill: none; stroke-width: 1; }}
    .hair2   {{ stroke: #f1f1f4; fill: none; stroke-width: 1; }}
    .ink     {{ fill: #191922; }}
    .sub     {{ fill: #76768a; }}
    .faint   {{ fill: #a5a5b2; }}
    .fill-surface {{ fill: #f8f8fa; }}
    .fill-line    {{ fill: #e5e5ea; }}
    .accent  {{ fill: {ACCENT}; }}
    .on-accent {{ fill: #fff; }}
    text {{ font-family: {DISPLAY}; }}
    .mono {{ font-family: {MONO}; }}
    .slate {{ font-family: {MONO}; letter-spacing: 2.5px; }}
    @media (prefers-color-scheme: dark) {{
      .bg      {{ fill: #08080c; }}
      .surface {{ fill: #101017; }}
      .hair    {{ stroke: #2a2a35; }}
      .hair2   {{ stroke: #1c1c26; }}
      .ink     {{ fill: #f8f8fa; }}
      .sub     {{ fill: #a5a5b2; }}
      .faint   {{ fill: #76768a; }}
      .fill-surface {{ fill: #16161f; }}
      .fill-line    {{ fill: #2a2a35; }}
    }}
  </style>
'''


def svg(name, w, h, body, extra_style=''):
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" role="img">\n'
           + THEME.replace('  </style>', extra_style + '  </style>' if extra_style else '  </style>')
           + f'  <rect width="{w}" height="{h}" class="bg"/>\n' + body + '</svg>\n')
    (OUT / f'{name}.svg').write_text(doc)
    return name


def label(x, y, text, cls='slate faint', size=11):
    return f'  <text x="{x}" y="{y}" class="{cls}" font-size="{size}">{text}</text>\n'


# ── 1 · the hero ────────────────────────────────────────────────────────────
def hero():
    b = ['  <rect width="1200" height="380" fill="#08080c"/>\n']
    b.append('  <g stroke="#ffffff" stroke-opacity="0.07" stroke-width="1">'
             '<path d="M0 95h1200M0 190h1200M0 285h1200M300 0v380M600 0v380M900 0v380"/></g>\n')
    # the viewfinder
    b.append('  <g fill="none" stroke="#ffffff" stroke-opacity="0.85" stroke-width="4" '
             'stroke-linecap="round"><path d="M56 96V70a12 12 0 0 1 12-12h28M1144 96V70a12 12 0 0 0-12-12h-28'
             'M56 284v26a12 12 0 0 0 12 12h28M1144 284v26a12 12 0 0 1-12 12h-28"/></g>\n')
    # The o IS the record light. The two halves of the word are drawn either
    # side of it and the dot takes the space the glyph would have filled —
    # measured at this size and letter-spacing, not eyeballed, so the word
    # still reads as one word rather than three pieces.
    b.append(f'  <text x="104" y="176" font-family="{DISPLAY}" font-size="72" font-weight="700" '
             f'fill="#fff" letter-spacing="-2.5">creat</text>\n')
    b.append(f'  <circle cx="281" cy="158" r="11" fill="{ACCENT}"/>\n')
    b.append(f'  <text x="300" y="176" font-family="{DISPLAY}" font-size="72" font-weight="700" '
             f'fill="#fff" letter-spacing="-2.5">r</text>\n')
    b.append(f'  <text x="107" y="214" font-family="{MONO}" font-size="19" fill="#ffffff" '
             f'fill-opacity="0.45" letter-spacing="5">DESIGN SYSTEM</text>\n')
    b.append(f'  <text x="104" y="268" font-family="{DISPLAY}" font-size="24" fill="#ffffff" '
             f'fill-opacity="0.72">Frame &amp; Signal — token-first, dependency-free CSS.</text>\n')
    b.append(f'  <text x="104" y="300" font-family="{DISPLAY}" font-size="24" fill="#ffffff" '
             f'fill-opacity="0.72">Almost monochrome, so one colour can mean '
             f'<tspan fill="{ACCENT}">live</tspan>.</text>\n')
    # the ramp, as proof rather than decoration
    x = 700
    for i, c in enumerate(INK[2:12]):
        b.append(f'  <rect x="{x + i * 34}" y="120" width="30" height="30" rx="4" fill="{c}"/>\n')
    for i, c in enumerate(SIGNAL[2:8]):
        b.append(f'  <rect x="{x + i * 34}" y="160" width="30" height="30" rx="4" fill="{c}"/>\n')
    b.append(f'  <text x="{x}" y="112" font-family="{MONO}" font-size="10" fill="#ffffff" '
             f'fill-opacity="0.4" letter-spacing="2.5">INK · THE WHOLE SITE</text>\n')
    b.append(f'  <text x="{x}" y="212" font-family="{MONO}" font-size="10" fill="#ffffff" '
             f'fill-opacity="0.4" letter-spacing="2.5">SIGNAL · RATIONED TO ONE MEANING</text>\n')
    # a button and a badge, at real size
    b.append(f'  <rect x="{x}" y="238" width="132" height="38" rx="19" fill="{ACCENT}"/>\n')
    b.append(f'  <text x="{x + 66}" y="263" font-family="{DISPLAY}" font-size="15" font-weight="600" '
             f'fill="#fff" text-anchor="middle">Subscribe</text>\n')
    b.append(f'  <rect x="{x + 144}" y="242" width="86" height="30" rx="15" fill="none" '
             f'stroke="#ffffff" stroke-opacity="0.28"/>\n')
    b.append(f'  <circle cx="{x + 163}" cy="257" r="4" fill="{ACCENT}"/>\n')
    b.append(f'  <text x="{x + 175}" y="262" font-family="{MONO}" font-size="11" fill="#ffffff" '
             f'fill-opacity="0.75" letter-spacing="1.5">LIVE</text>\n')
    return svg('hero', 1200, 380, ''.join(b))


# ── 2 · colour ──────────────────────────────────────────────────────────────
def colour():
    b = []
    b.append(label(40, 46, 'INK — 14 STEPS, THE WHOLE SITE'))
    w = 76
    for i, c in enumerate(INK):
        x = 40 + i * (w + 4)
        b.append(f'  <rect x="{x}" y="60" width="{w}" height="56" rx="6" fill="{c}" '
                 f'class="{"hair" if i < 3 else ""}"/>\n')
        b.append(f'  <text x="{x}" y="132" class="mono faint" font-size="10">{INK_NAMES[i]}</text>\n')
    b.append(label(40, 186, 'SIGNAL — ONE HUE, SPENT CAREFULLY'))
    for i, c in enumerate(SIGNAL):
        x = 40 + i * (w + 4)
        b.append(f'  <rect x="{x}" y="200" width="{w}" height="56" rx="6" fill="{c}"/>\n')
        b.append(f'  <text x="{x}" y="272" class="mono faint" font-size="10">{SIGNAL_NAMES[i]}</text>\n')
    b.append(f'  <rect x="{40 + 5 * (w + 4)}" y="196" width="{w}" height="64" rx="8" fill="none" '
             f'stroke="{ACCENT}" stroke-width="2"/>\n')
    b.append(f'  <text x="{40 + 5 * (w + 4) + w / 2}" y="292" class="mono accent" font-size="10" '
             f'text-anchor="middle" letter-spacing="1">--accent</text>\n')
    return svg('colour', 1200, 320, ''.join(b))


# ── 3 · type ────────────────────────────────────────────────────────────────
def type_scale():
    b = [label(40, 44, 'THREE FACES, THREE JOBS')]
    b.append('  <text x="40" y="118" class="ink" font-size="54" font-weight="700" '
             'letter-spacing="-1.5">Display carries the idea</text>\n')
    b.append('  <text x="40" y="146" class="faint mono" font-size="11" '
             'letter-spacing="2">SPACE GROTESK · --font-display · HEADINGS ONLY</text>\n')
    b.append('  <text x="40" y="206" class="ink" font-size="21">Body is for reading — a measure you '
             'can follow to the end of the line without losing it.</text>\n')
    b.append('  <text x="40" y="234" class="faint mono" font-size="11" '
             'letter-spacing="2">INTER · --font-body · EVERYTHING YOU READ</text>\n')
    b.append('  <text x="40" y="286" class="sub mono" font-size="15" letter-spacing="1">'
             '.nav-shell · --space-4 · 00:12:47</text>\n')
    b.append('  <text x="40" y="312" class="faint mono" font-size="11" '
             'letter-spacing="2">IBM PLEX MONO · --font-slate · LABELS, CODE, TIMECODE</text>\n')
    return svg('type', 1200, 340, ''.join(b))


# ── 4 · space and shape ─────────────────────────────────────────────────────
def space():
    b = [label(40, 44, 'SPACING — ONE LADDER, NO IMPROVISED GAPS')]
    steps = [(1, 4), (2, 8), (3, 12), (4, 16), (5, 20), (6, 24), (8, 32), (10, 48), (12, 64)]
    x = 40
    for n, px in steps:
        b.append(f'  <rect x="{x}" y="64" width="{px}" height="44" rx="2" class="accent" '
                 f'fill-opacity="0.85"/>\n')
        b.append(f'  <text x="{x}" y="126" class="mono faint" font-size="10">{n}</text>\n')
        b.append(f'  <text x="{x}" y="140" class="mono faint" font-size="9">{px}</text>\n')
        x += px + 46
    b.append(label(40, 196, 'RADIUS — FROM A CHIP TO A SHEET'))
    radii = [('sm', 4), ('md', 8), ('lg', 12), ('xl', 20), ('pill', 32)]
    x = 40
    for name, r in radii:
        b.append(f'  <rect x="{x}" y="212" width="64" height="64" rx="{r}" class="fill-surface hair"/>\n')
        b.append(f'  <text x="{x}" y="296" class="mono faint" font-size="10">{name}</text>\n')
        x += 88
    return svg('space', 1200, 320, ''.join(b))


# ── 5 · components ──────────────────────────────────────────────────────────
def components():
    b = [label(40, 44, 'ONE PRIMARY PER SURFACE — THE REST RECEDE')]
    btns = [('Primary', ACCENT, '#fff', None),
            ('Secondary', None, None, 'strong'),
            ('Ghost', None, None, 'hair'),
            ('Soft', '#fff2ef', '#b52810', None)]
    x = 40
    for lbl, bg, fg, mode in btns:
        w = 118
        if bg:
            b.append(f'  <rect x="{x}" y="62" width="{w}" height="40" rx="20" fill="{bg}"/>\n')
            b.append(f'  <text x="{x + w / 2}" y="88" font-size="15" font-weight="600" '
                     f'fill="{fg}" text-anchor="middle">{lbl}</text>\n')
        else:
            stroke = '#191922' if mode == 'strong' else None
            cls = 'hair' if mode == 'hair' else ''
            extra = f'stroke="{stroke}" fill="none"' if stroke else ''
            b.append(f'  <rect x="{x}" y="62" width="{w}" height="40" rx="20" class="{cls}" {extra}/>\n')
            b.append(f'  <text x="{x + w / 2}" y="88" class="ink" font-size="15" font-weight="600" '
                     f'text-anchor="middle">{lbl}</text>\n')
        x += w + 14
    # badges
    b.append(label(40, 152, 'BADGES CARRY STATE, NEVER DECORATION'))
    chips = [('LIVE', ACCENT, True), ('SHIPPED', None, False), ('DRAFT', None, False)]
    x = 40
    for lbl, col, dot in chips:
        w = 96
        b.append(f'  <rect x="{x}" y="166" width="{w}" height="28" rx="14" class="hair fill-surface"/>\n')
        if dot:
            b.append(f'  <circle cx="{x + 18}" cy="180" r="4" fill="{col}"/>\n')
        b.append(f'  <text x="{x + (30 if dot else 16)}" y="185" class="mono sub" font-size="10" '
                 f'letter-spacing="1.5">{lbl}</text>\n')
        x += w + 12
    # a card
    b.append('  <rect x="700" y="56" width="460" height="216" rx="16" class="fill-surface hair"/>\n')
    b.append('  <rect x="700" y="56" width="460" height="96" rx="16" class="fill-line"/>\n')
    b.append('  <rect x="700" y="136" width="460" height="16" class="fill-line"/>\n')
    b.append(f'  <circle cx="930" cy="104" r="22" fill="{ACCENT}"/>\n')
    b.append('  <path d="M923 95v18l15-9-15-9Z" fill="#fff"/>\n')
    b.append('  <text x="726" y="184" class="mono faint" font-size="10" letter-spacing="2">'
             'BUILD LOG · 12 MIN</text>\n')
    b.append('  <text x="726" y="214" class="ink" font-size="22" font-weight="700" '
             'letter-spacing="-0.5">Rebuilding my theme from tokens</text>\n')
    b.append('  <rect x="726" y="234" width="300" height="8" rx="4" class="fill-line"/>\n')
    b.append('  <rect x="726" y="250" width="220" height="8" rx="4" class="fill-line"/>\n')
    b.append(label(40, 236, 'A CARD IS THE SAME OBJECT IN EVERY COLLECTION'))
    return svg('components', 1200, 300, ''.join(b))


# ── 6 · the navbar ──────────────────────────────────────────────────────────
def navbar():
    b = [label(40, 40, 'ONE BAR, A STYLE PER COLLECTION')]

    # 1 · the island, with its hairline doing double duty as the read-through.
    b.append('  <rect x="40" y="56" width="1120" height="60" rx="30" class="fill-surface"/>\n')
    b.append('  <rect x="40" y="56" width="1120" height="60" rx="30" class="hair"/>\n')
    b.append(f'  <path d="M70 56h330" stroke="{ACCENT}" stroke-width="2" fill="none" '
             f'stroke-linecap="round"/>\n')
    b.append('  <text x="72" y="94" class="ink" font-size="21" font-weight="700" '
             'letter-spacing="-0.8">creat</text>\n')
    b.append(f'  <circle cx="140" cy="83" r="3.8" fill="{ACCENT}"/>\n')
    b.append('  <text x="149" y="94" class="ink" font-size="21" font-weight="700" '
             'letter-spacing="-0.8">r</text>\n')
    for i, (lbl, cur) in enumerate([('Watch', False), ('Learn', True), ('Build', False)]):
        x = 500 + i * 96
        b.append(f'  <text x="{x}" y="93" class="{"ink" if cur else "sub"}" font-size="15" '
                 f'font-weight="{"600" if cur else "400"}">{lbl}</text>\n')
        if cur:
            b.append(f'  <circle cx="{x - 12}" cy="88" r="3.5" fill="{ACCENT}"/>\n')
    b.append(f'  <rect x="1000" y="70" width="118" height="32" rx="16" fill="{ACCENT}"/>\n')
    b.append('  <text x="1059" y="91" font-size="14" font-weight="600" fill="#fff" '
             'text-anchor="middle">Subscribe</text>\n')
    b.append(label(40, 140, 'THE HAIRLINE IS THE READ-THROUGH BAR  ·  --progress:30%'))

    # 2 · the series bar, which is not an island at all.
    b.append('  <rect x="40" y="168" width="1120" height="104" rx="12" fill="#12121a"/>\n')
    b.append('  <path d="M40 168h1120v52H40Z" fill="#000" fill-opacity="0.35"/>\n')
    b.append('  <text x="72" y="204" fill="#fff" font-size="21" font-weight="700" '
             'letter-spacing="-0.8">creat</text>\n')
    b.append(f'  <circle cx="140" cy="193" r="3.8" fill="{ACCENT}"/>\n')
    b.append('  <text x="149" y="204" fill="#fff" font-size="21" font-weight="700" '
             'letter-spacing="-0.8">r</text>\n')
    for i, (lbl, cur) in enumerate([('Watch', True), ('Extras', False), ('About', False)]):
        x = 500 + i * 96
        b.append(f'  <text x="{x}" y="203" fill="#ffffff" fill-opacity="{1 if cur else 0.6}" '
                 f'font-size="15" font-weight="{"600" if cur else "400"}">{lbl}</text>\n')
        if cur:
            b.append(f'  <circle cx="{x - 12}" cy="198" r="3.5" fill="{ACCENT}"/>\n')
    b.append(f'  <rect x="1000" y="180" width="118" height="32" rx="16" fill="{ACCENT}"/>\n')
    b.append('  <text x="1059" y="201" font-size="14" font-weight="600" fill="#fff" '
             'text-anchor="middle">Subscribe</text>\n')
    b.append(f'  <text x="600" y="252" font-family="{MONO}" font-size="11" fill="#ffffff" '
             f'fill-opacity="0.32" letter-spacing="2.5" text-anchor="middle">YOUR FOOTAGE</text>\n')
    b.append(label(40, 296, '.nav-video IN .nav-over — NO PLATE, NO BORDER, OVER THE FILM'))
    return svg('navbar', 1200, 320, ''.join(b))


# ── 7 · the layers ──────────────────────────────────────────────────────────
def layers():
    rows = [
        ('6-utilities', 'u- prefixed, single purpose'),
        ('5-sections', 'header · hero · stats · CTA · footer'),
        ('4-broadcast', 'YouTube and Instagram canvases'),
        ('3-components', 'parts and states: buttons → navbar'),
        ('2-elements', 'single ideas: text · badge · table · syntax'),
        ('1-foundation', 'tokens: colour · type · space · motion'),
    ]
    b = [label(40, 40, 'SIX LAYERS — TAKE THE WHOLE STACK OR ONE FLOOR')]
    for i, (name, desc) in enumerate(rows):
        y = 56 + i * 46
        inset = i * 14
        b.append(f'  <rect x="{40 + inset}" y="{y}" width="{900 - inset * 2}" height="38" rx="8" '
                 f'class="fill-surface hair"/>\n')
        b.append(f'  <text x="{60 + inset}" y="{y + 24}" class="mono ink" font-size="13">{name}</text>\n')
        b.append(f'  <text x="{200 + inset}" y="{y + 24}" class="sub" font-size="13">{desc}</text>\n')
    b.append(f'  <path d="M975 70v240" class="hair"/>\n')
    b.append(f'  <text x="995" y="180" class="mono faint" font-size="11" letter-spacing="2">'
             f'EACH LAYER NEEDS ONLY</text>\n')
    b.append(f'  <text x="995" y="198" class="mono faint" font-size="11" letter-spacing="2">'
             f'THE ONES BELOW IT</text>\n')
    return svg('layers', 1200, 340, ''.join(b))


# ── 8 · the highlighter ─────────────────────────────────────────────────────
def code():
    tok = {'key': '#c22557', 'str': '#1a7f4e', 'num': '#9c6a10',
           'fn': '#1d5fbf', 'com': '#a5a5b2', 'sel': '#a2451b', 'var': '#6b3fc4'}
    dark = {'key': '#ff8fa5', 'str': '#6ee7ad', 'num': '#f2d795',
            'fn': '#93c2ff', 'com': '#5b5b6b', 'sel': '#ffc59c', 'var': '#c7b6ff'}
    style = ''.join(f'    .t-{k} {{ fill: {v}; }}\n' for k, v in tok.items())
    style += '    @media (prefers-color-scheme: dark) {\n'
    style += ''.join(f'      .t-{k} {{ fill: {v}; }}\n' for k, v in dark.items())
    style += '    }\n'

    b = [label(40, 40, 'THE SYSTEM COLOURS ITS OWN CODE — FIVE ROLES, BOTH THEMES')]
    b.append('  <rect x="40" y="56" width="1120" height="200" rx="12" class="fill-surface hair"/>\n')
    b.append('  <path d="M40 92h1120" class="hair2"/>\n')
    b.append(f'  <circle cx="64" cy="74" r="4" fill="{ACCENT}"/>\n')
    b.append('  <text x="78" y="79" class="mono faint" font-size="10" letter-spacing="2">CSS</text>\n')
    lines = [
        [('/* one colour means live */', 'com')],
        [('.dot-live', 'sel'), (' {', None)],
        [('  background', 'fn'), (': ', None), ('var(--accent)', 'var'), (';', None)],
        [('  animation', 'fn'), (': ', None), ('rec 2.4s', 'num'), (' ', None), ('infinite', 'key'), (';', None)],
        [('}', None)],
    ]
    y = 122
    for n, parts in enumerate(lines):
        b.append(f'  <text x="62" y="{y}" class="mono faint" font-size="12">{n + 1}</text>\n')
        x = 92
        for text, role in parts:
            cls = f't-{role}' if role else 'ink'
            esc = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            b.append(f'  <text x="{x}" y="{y}" class="mono {cls}" font-size="13" '
                     f'xml:space="preserve">{esc}</text>\n')
            x += len(text) * 7.8
        y += 26
    return svg('code', 1200, 280, ''.join(b), extra_style=style)


if __name__ == '__main__':
    made = [hero(), colour(), type_scale(), space(), components(), navbar(), layers(), code()]
    print('wrote ' + ', '.join(f'{m}.svg' for m in made))
