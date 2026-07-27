"""The Navbar page — anatomy, every variant, and how to build each one.

One page on purpose: a navbar is a single component with many shapes, and
splitting it across pages is how people miss the shape they needed.
"""
from common import tile, ct

PAGES = {}

# ── helpers ─────────────────────────────────────────────────────────────────

LOGO = '<span class="logo logo-sm">Swarn<span class="logo__i">ı<i class="logo__tittle"></i></span>l</span>'


def bar(inner, cls='nav-bar', shell='nav-shell'):
    return (f'<div class="{shell}" style="position:static;padding-inline:0;max-width:none">'
            f'<nav class="{cls}" aria-label="Demo">{inner}</nav></div>')


def links(items, extra=''):
    out = f'<div class="nav-links{" " + extra if extra else ""}">'
    for label, icon, cur in items:
        a = ' aria-current="page"' if cur else ''
        ic = f'<svg class="icon" aria-hidden="true"><use href="#i-{icon}"/></svg>' if icon else ''
        out += f'<a class="nav-link" href="#i"{a}>{ic}{label}</a>'
    return out + '</div>'


def burger(cls='', label=False):
    inner = ('<span class="nav-burger__box"><span class="nav-burger__bars"></span></span>'
             + ('Menu' if label else '<span class="u-sr-only">Menu</span>'))
    return f'<button class="nav-burger {cls}" type="button" aria-expanded="false" data-burger>{inner}</button>'


def stack(main, sub, sub_attrs=''):
    """The two-row island: site menu on top, context row beneath."""
    return ('<div class="nav-shell" style="position:static;padding-inline:0;max-width:none">'
            '<div class="nav-stack">'
            f'<nav class="nav-bar" aria-label="Demo">{main}</nav>'
            f'<div class="nav-sub nav-context"{sub_attrs}>{sub}</div>'
            '</div></div>')


def code(lang, lines, note):
    """A copyable markup block. `lines` is a list of pre-escaped strings."""
    body = ''.join(f'<span class="ln">{l}</span>' for l in lines)
    return tile(
        f'<figure class="codebox codebox-light u-m-0"><figcaption class="codebox__head">'
        f'<span class="codebox__lang">{lang}</span>'
        f'<button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>'
        f'<pre class="codebox__pre"><code>{body}</code></pre></figure>', note)


K = lambda t: f'<span class="tok-key">{t}</span>'
S = lambda t: f'<span class="tok-str">{t}</span>'
C = lambda t: f'<span class="tok-com">{t}</span>'
F = lambda t: f'<span class="tok-fn">{t}</span>'


def h2(t):
    return f'<h2 class="t-h3" style="margin:var(--space-12) 0 var(--space-4)">{t}</h2>'


def p(t):
    return f'<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">{t}</p>'


def _seg(name, options, value):
    """A segmented radio group. Radios, not buttons — arrow keys come free."""
    out = f'<div class="np__seg" role="group">'
    for val, label in options:
        cur = ' checked' if val == value else ''
        out += (f'<label class="np__opt"><input type="radio" name="{name}" value="{val}"{cur} />'
                f'<span>{label}</span></label>')
    return out + '</div>'


def _check(name, label, on=True):
    return (f'<label class="np__check"><input type="checkbox" name="{name}"'
            f'{" checked" if on else ""} /><span>{label}</span></label>')


def _row(label, control):
    return f'<div class="np__row"><span class="np__label">{label}</span>{control}</div>'


# The control panel. Everything it can set is a knob that already exists on the
# component — the panel invents nothing, so the markup it prints is the markup
# you would have written. preview.js wires it up.
PLAYGROUND = (
    '<div class="np" data-nav-playground>'
    '<div class="np__stage">'
    '<div class="nav-shell" style="position:static;padding-inline:0;max-width:none" data-np-shell>'
    '<div class="nav-stack">'
    '<nav class="nav-bar" aria-label="Playground" data-np-bar></nav>'
    '<div class="nav-sub nav-context" data-np-sub></div>'
    '</div></div></div>'

    '<div class="np__panel">'
    + _row('Preset', '<div class="np__seg" role="group">'
           + ''.join(f'<label class="np__opt"><input type="radio" name="np-preset" '
                     f'value="{v}"{" checked" if v == "series" else ""} /><span>{l}</span></label>'
                     for v, l in [('series', 'Web series'), ('docs', 'Docs'),
                                  ('course', 'Course'), ('custom', 'Custom')])
           + '</div>')
    + _row('Position', _seg('np-shell', [('island', 'Island'), ('fixed', 'Fixed'),
                                         ('morph', 'Island on scroll'),
                                         ('auto', 'Fixed on scroll')], 'island'))
    + _row('Accent', '<div class="np__swatches">'
           + ''.join(f'<label class="np__swatch" style="--sw:{c}">'
                     f'<input type="radio" name="np-accent" value="{c}"'
                     f'{" checked" if i == 0 else ""} />'
                     f'<span class="u-sr-only">{n}</span></label>'
                     for i, (n, c) in enumerate([('Record red', ''), ('Signal blue', '#3b6fe0'),
                                                 ('Field green', '#1a8a5a'),
                                                 ('Studio violet', '#6d4aff'),
                                                 ('Amber', '#c9791a')]))
           + '</div>')
    + _row('Tone', _seg('np-tone', [('paper', 'Paper'), ('ink', 'Ink'), ('accent', 'Accent')], 'paper'))
    + _row('Density', _seg('np-density', [('regular', 'Regular'), ('compact', 'Compact')], 'regular'))
    + _row('Slots', '<div class="np__checks">'
           + _check('np-back', 'Back')
           + _check('np-kind', 'Kind', False)
           + _check('np-pos', 'Position')
           + _check('np-actions', 'Actions')
           + _check('np-rail', 'Rail')
           + '</div>')
    + _row('Prefix', _seg('np-prefix', [('', 'None'), ('DAY ', 'DAY'), ('EP.', 'EP.')], ''))
    + _row('Mark position', '<div class="np__checks">' + _check('np-mark', 'Accent', False) + '</div>')
    + _row('Main bar', '<div class="np__checks">'
           + _check('np-logo', 'Logo')
           + _check('np-icons', 'Social icons', False)
           + _check('np-news', 'Newsletter', False)
           + _check('np-cta', 'CTA', False)
           + _check('np-burger', 'Burger', False)
           + '</div>')
    + _row('Progress line', '<div class="np__checks">'
           + _check('np-progress', 'Border fills', False)
           + '</div>'
           + _seg('np-track', [('grey', 'Grey track'), ('accent', 'Tinted track')], 'grey'))
    + _row('Progress', '<input class="np__range" type="range" name="np-value" '
                       'min="0" max="100" value="21" aria-label="Progress" />'
                       '<output class="np__out-val" data-np-value>21%</output>')
    + '</div>'

    '<div class="np__code" data-np-code></div>'
    '</div>')


# ── the page ────────────────────────────────────────────────────────────────

b = []

b.append(p(
    'The navbar is one component with several shapes: a site bar, a bar with menus, '
    'a mobile sheet, and a submenu row for whatever you are inside. They share a '
    'skeleton and a height, so moving between them never shifts the chrome. '
    'Everything below is on this page because you cannot pick the right shape from a '
    'page you did not know existed.'))

# 1 · anatomy ────────────────────────────────────────────────────────────────
b.append(h2('1 · Anatomy'))
b.append(p(
    'Three slots: the mark on the left, the links in the middle, the actions on the '
    'right. <code class="t-code">.nav-shell</code> positions and centres; '
    '<code class="t-code">.nav-bar</code> is the island itself. The shell is sticky, '
    'so the bar is always reachable.'))
b.append(tile(bar(LOGO + links([('Blog', 'pen', True), ('Videos', 'camera', False),
                                ('Projects', 'code', False)])
              + '<div class="cluster-sm">'
                '<button class="btn btn-secondary btn-sm btn-icon" aria-label="Search">'
                '<svg class="icon" aria-hidden="true"><use href="#i-search"/></svg></button>'
                '<button class="btn btn-primary btn-sm btn-pill">Subscribe</button></div>'),
    '<b>.nav-shell &gt; .nav-bar</b> — mark · links · actions'))
b.append(code('html', [
    f'{K("&lt;header")} class={S(chr(34)+"nav-shell"+chr(34))}{K("&gt;")}',
    f'  {K("&lt;nav")} class={S(chr(34)+"nav-bar"+chr(34))} aria-label={S(chr(34)+"Main"+chr(34))}{K("&gt;")}',
    f'    {C("&lt;!-- 1 · the mark --&gt;")}',
    f'    {K("&lt;a")} class={S(chr(34)+"logo logo-sm"+chr(34))} href={S(chr(34)+"/"+chr(34))}{K("&gt;")}…{K("&lt;/a&gt;")}',
    '',
    f'    {C("&lt;!-- 2 · the links --&gt;")}',
    f'    {K("&lt;div")} class={S(chr(34)+"nav-links"+chr(34))}{K("&gt;")}',
    f'      {K("&lt;a")} class={S(chr(34)+"nav-link"+chr(34))} href={S(chr(34)+"/blog/"+chr(34))} aria-current={S(chr(34)+"page"+chr(34))}{K("&gt;")}Blog{K("&lt;/a&gt;")}',
    f'      {K("&lt;a")} class={S(chr(34)+"nav-link"+chr(34))} href={S(chr(34)+"/videos/"+chr(34))}{K("&gt;")}Videos{K("&lt;/a&gt;")}',
    f'    {K("&lt;/div&gt;")}',
    '',
    f'    {C("&lt;!-- 3 · the actions --&gt;")}',
    f'    {K("&lt;div")} class={S(chr(34)+"cluster-sm"+chr(34))}{K("&gt;")}…{K("&lt;/div&gt;")}',
    f'  {K("&lt;/nav&gt;")}',
    f'{K("&lt;/header&gt;")}',
], 'the whole skeleton — every variant below changes only what it must'))
b.append(ct([
    ('.nav-shell', 'sticky wrapper; centres the bar and sets its max width'),
    ('.nav-bar', 'the island: height, border, radius, blur, shadow'),
    ('.nav-links', 'the middle slot; a flex row of .nav-link'),
    ('.nav-link', 'one destination. Add an <code class="t-code">.icon</code> before the label'),
    ('--nav-h', 'the bar height (3.5rem). Every contextual bar inherits it'),
], head=('Class', 'Job')))

# 2 · alignment ──────────────────────────────────────────────────────────────
b.append(h2('2 · Alignment — pick deliberately'))
b.append(p(
    '“Same width as the content” means two different things, and picking silently is '
    'how a nav ends up looking 16px wrong. The island either shares its <em>border</em> '
    'with the content column edge, or shares its <em>text</em> with the page text. '
    'The shell already derives its width from <code class="t-code">--w-site</code> and '
    '<code class="t-code">--gutter</code>, the same two tokens '
    '<code class="t-code">.container</code> uses — so the edges match by construction.'))
b.append(tile(bar(LOGO + links([('Blog', None, True), ('Videos', None, False)])
                  + '<button class="btn btn-primary btn-sm btn-pill">Subscribe</button>'),
    '<b>.nav-shell</b> — DEFAULT. The island’s border meets the content edge; it reads as a floating object.'))
b.append(tile(bar(LOGO + links([('Blog', None, True), ('Videos', None, False)])
                  + '<button class="btn btn-primary btn-sm btn-pill">Subscribe</button>',
                  shell='nav-shell nav-shell-flush'),
    '<b>.nav-shell-flush</b> — the island’s CONTENT lines up with the page text, so the wordmark sits directly above the page title.'))
b.append(ct([
    ('.nav-shell', 'floating island. Use when the page has a hero or a pattern behind it'),
    ('.nav-shell-flush', 'flat bar, content-aligned. Use for docs and reading-first sites'),
    ('.nav-shell-full', 'edge-to-edge bar, inner content still capped at the site width'),
    ('[data-scrolled]', 'set it from JS past ~8px of scroll; the island tightens and gains a shadow'),
], head=('Variant', 'When')))

# 3 · active ─────────────────────────────────────────────────────────────────
b.append(h2('3 · The active link'))
b.append(p(
    '<code class="t-code">aria-current="page"</code> is the ONLY hook. Styling and the '
    'accessibility tree are then the same attribute and cannot disagree — which is '
    'exactly why a <code class="t-code">.active</code> class is banned here.'))
b.append(tile(bar(LOGO + links([('Blog', None, True), ('Videos', None, False), ('Travel', None, False)])),
    '<b>default</b> — the signal dot. One per bar, and it means “you are here”.'))
b.append(tile(bar(LOGO + links([('Overview', None, True), ('Syllabus', None, False), ('Gear', None, False)], 'nav-links-rule')),
    '<b>.nav-links-rule</b> — a 2px accent underline. For docs and dense bars where a dot reads as decoration.'))
b.append(tile(bar(LOGO + links([('All', None, True), ('Builds', None, False), ('Vlogs', None, False)], 'nav-links-soft')),
    '<b>.nav-links-soft</b> — a sunken wash, when neither dot nor rule survives the background.'))
b.append(p('<b>Setting it.</b> In Ghost, the navigation helper already knows:'))
b.append(code('handlebars', [
    f'{K("{{#foreach")} navigation{K("}}")}',
    f'  {K("&lt;a")} class={S(chr(34)+"nav-link"+chr(34))} href={S(chr(34)+"{{url}}"+chr(34))}',
    f'     {K("{{#if")} current{K("}}")}aria-current={S(chr(34)+"page"+chr(34))}{K("{{/if}}")}{K("&gt;")}{K("{{label}}")}{K("&lt;/a&gt;")}',
    f'{K("{{/foreach}}")}',
], 'Ghost exposes <b>current</b> inside <b>{{#foreach navigation}}</b> — use it and the dot is automatic'))
b.append(p(
    '<b>The trap.</b> A hardcoded fallback menu has no <code class="t-code">current</code> '
    'property, so nothing ever receives the attribute and the bar never shows where you '
    'are. If you ship a fallback, mark it on load:'))
b.append(code('js', [
    C('// mark the link whose path prefixes the current one'),
    f'{K("const")} here = location.pathname;',
    f'document.{F("querySelectorAll")}({S(chr(39)+".nav-link"+chr(39))}).{F("forEach")}(a =&gt; {{',
    f'  {K("const")} path = {K("new")} {F("URL")}(a.href).pathname;',
    f'  {K("if")} (path !== {S(chr(39)+"/"+chr(39))} &amp;&amp; here.{F("startsWith")}(path))',
    f'    a.{F("setAttribute")}({S(chr(39)+"aria-current"+chr(39))}, {S(chr(39)+"page"+chr(39))});',
    '});',
], 'longest-prefix wins, so /courses/java/lesson-1/ still lights up “Courses”'))

# 4 · dropdown ───────────────────────────────────────────────────────────────
b.append(h2('4 · Dropdown'))
b.append(p(
    'A native <code class="t-code">&lt;details&gt;</code>: keyboard, Escape and '
    'click-away come from the browser. <b>One level only</b> — a second level is a mega '
    'panel, not a fly-out, because fly-outs are unusable on touch.'))
b.append(tile(bar(LOGO +
    '<div class="nav-links">'
    '<a class="nav-link" href="#i">Blog</a>'
    '<details class="nav-menu"><summary class="nav-link">Learn</summary>'
    '<div class="nav-menu__panel">'
    '<a class="dropdown__item" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-book"/></svg> Courses</a>'
    '<a class="dropdown__item" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-pen"/></svg> Guides</a>'
    '<hr class="dropdown__divider" />'
    '<a class="dropdown__item" href="#i">Docs</a>'
    '</div></details>'
    '<a class="nav-link" href="#i">Travel</a></div>'),
    '<b>.nav-menu</b> — click “Learn”. The caret is drawn by CSS from the open state.'))
b.append(code('html', [
    f'{K("&lt;details")} class={S(chr(34)+"nav-menu"+chr(34))}{K("&gt;")}',
    f'  {K("&lt;summary")} class={S(chr(34)+"nav-link"+chr(34))}{K("&gt;")}Learn{K("&lt;/summary&gt;")}',
    f'  {K("&lt;div")} class={S(chr(34)+"nav-menu__panel"+chr(34))}{K("&gt;")}',
    f'    {K("&lt;a")} class={S(chr(34)+"dropdown__item"+chr(34))} href={S(chr(34)+"/courses/"+chr(34))}{K("&gt;")}Courses{K("&lt;/a&gt;")}',
    f'    {K("&lt;hr")} class={S(chr(34)+"dropdown__divider"+chr(34))} {K("/&gt;")}',
    f'  {K("&lt;/div&gt;")}',
    f'{K("&lt;/details&gt;")}',
], 'reuses <b>.dropdown__item</b> / <b>__divider</b> / <b>__head</b> from the Dropdowns component'))

# 5 · mega ───────────────────────────────────────────────────────────────────
b.append(h2('5 · Mega panel'))
b.append(p(
    'A full-width sheet under the island: link columns plus one featured cell. '
    'A mega menu that is only links is a dropdown wearing a costume — the featured '
    'cell is what earns the extra space. Add <code class="t-code">.nav-mega</code> '
    'beside <code class="t-code">.nav-menu</code>; it goes '
    '<code class="t-code">position: static</code> so the panel can span the whole bar.'))
b.append(tile('<div class="nav-shell" style="position:relative;padding-inline:0;max-width:none">'
    '<nav class="nav-bar">' + LOGO +
    '<div class="nav-links"><a class="nav-link" href="#i">Blog</a>'
    '<details class="nav-menu nav-mega" open><summary class="nav-link">Everything</summary>'
    '<div class="nav-mega__panel">'
    '<div class="nav-mega__col"><span class="nav-mega__title">Watch</span>'
    '<a class="nav-mega__link" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-camera"/></svg><span><b>Videos</b><span>Tutorials and build vlogs</span></span></a>'
    '<a class="nav-mega__link" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg><span><b>Web series</b><span>Shot like a season</span></span></a></div>'
    '<div class="nav-mega__col"><span class="nav-mega__title">Learn</span>'
    '<a class="nav-mega__link" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-book"/></svg><span><b>Courses</b><span>A syllabus you can finish</span></span></a>'
    '<a class="nav-mega__link" href="#i"><svg class="icon" aria-hidden="true"><use href="#i-pen"/></svg><span><b>Guides</b><span>Step by step</span></span></a></div>'
    '<a class="nav-mega__feature" href="#i"><span class="pattern pattern-grid pattern-media"></span>'
    '<span class="t-slate-sm" style="color:var(--fg-faint)">FEATURED</span>'
    '<b>Rebuilding my theme from tokens</b></a>'
    '</div></details></div></nav></div><div style="height:13rem"></div>',
    '<b>.nav-mega__panel</b> — shown open. Columns auto-fit; the feature cell is a link, not a card.'))
b.append(code('html', [
    f'{K("&lt;details")} class={S(chr(34)+"nav-menu nav-mega"+chr(34))}{K("&gt;")}',
    f'  {K("&lt;summary")} class={S(chr(34)+"nav-link"+chr(34))}{K("&gt;")}Everything{K("&lt;/summary&gt;")}',
    f'  {K("&lt;div")} class={S(chr(34)+"nav-mega__panel"+chr(34))}{K("&gt;")}',
    f'    {K("&lt;div")} class={S(chr(34)+"nav-mega__col"+chr(34))}{K("&gt;")}',
    f'      {K("&lt;span")} class={S(chr(34)+"nav-mega__title"+chr(34))}{K("&gt;")}Watch{K("&lt;/span&gt;")}',
    f'      {K("&lt;a")} class={S(chr(34)+"nav-mega__link"+chr(34))} href={S(chr(34)+"/videos/"+chr(34))}{K("&gt;")}',
    f'        {K("&lt;svg")} class={S(chr(34)+"icon"+chr(34))}{K("&gt;")}…{K("&lt;/svg&gt;")}',
    f'        {K("&lt;span&gt;&lt;b&gt;")}Videos{K("&lt;/b&gt;&lt;span&gt;")}Tutorials{K("&lt;/span&gt;&lt;/span&gt;")}',
    f'      {K("&lt;/a&gt;")}',
    f'    {K("&lt;/div&gt;")}',
    f'    {K("&lt;a")} class={S(chr(34)+"nav-mega__feature"+chr(34))} href={S(chr(34)+"…"+chr(34))}{K("&gt;")}…{K("&lt;/a&gt;")}',
    f'  {K("&lt;/div&gt;")}',
    f'{K("&lt;/details&gt;")}',
], 'the <b>.nav-shell</b> must be <b>position: relative</b> for the panel to span it'))

# 6 · hamburger ──────────────────────────────────────────────────────────────
b.append(h2('6 · Hamburger'))
b.append(p(
    'Three bars that become an X — one element and two pseudo-elements, no icon font '
    'and no swapped SVG. State lives in <code class="t-code">aria-expanded</code>, the '
    'same attribute a screen reader announces. <b>Click them.</b>'))
b.append(tile('<div class="u-flex u-gap-6 u-items-center u-wrap">'
    + ''.join(f'<span class="u-text-center"><span class="u-block u-mb-2">{bt}</span>'
              f'<span class="t-slate-sm" style="color:var(--fg-faint)">{n}</span></span>'
              for bt, n in [(burger(), 'default'), (burger('nav-burger-squeeze'), 'squeeze'),
                            (burger('nav-burger-aperture'), 'aperture'),
                            (burger('nav-burger-bare'), 'bare'),
                            (burger('nav-burger-labelled', label=True), 'labelled')])
    + '</div>',
    '<b>.nav-burger</b> + <b>-squeeze / -aperture / -bare / -labelled</b>'))
b.append(code('html', [
    f'{K("&lt;button")} class={S(chr(34)+"nav-burger"+chr(34))} type={S(chr(34)+"button"+chr(34))}',
    f'        aria-expanded={S(chr(34)+"false"+chr(34))} aria-controls={S(chr(34)+"site-menu"+chr(34))}{K("&gt;")}',
    f'  {K("&lt;span")} class={S(chr(34)+"nav-burger__box"+chr(34))}{K("&gt;")}',
    f'    {K("&lt;span")} class={S(chr(34)+"nav-burger__bars"+chr(34))}{K("&gt;&lt;/span&gt;")}',
    f'  {K("&lt;/span&gt;")}',
    f'  {K("&lt;span")} class={S(chr(34)+"u-sr-only"+chr(34))}{K("&gt;")}Menu{K("&lt;/span&gt;")}',
    f'{K("&lt;/button&gt;")}',
], 'the bars are decorative — the button still needs a name, hence <b>.u-sr-only</b>'))
b.append(ct([
    ('aria-expanded', 'toggle it in JS when the sheet opens/closes; CSS draws the X from it'),
    ('aria-controls', 'the sheet’s id, so the relationship is announced'),
    ('.nav-burger-aperture', 'rotates as one — pair it with the sheet’s iris open'),
    ('.nav-burger-bare', 'no ring, for bars that already have a border'),
], head=('Hook', 'Why')))

# 7 · mobile sheet ───────────────────────────────────────────────────────────
b.append(h2('7 · Mobile sheet'))
b.append(p(
    'A real <code class="t-code">&lt;dialog&gt;</code>, so focus trapping and Escape '
    'are the platform’s job. It opens like a lens: the panel <b>irises out</b> from the '
    'button corner, a <b>scanline sweeps</b> once, and the rows <b>rack into focus</b> '
    'in sequence — blur to sharp, staggered. All of it is disabled under '
    '<code class="t-code">prefers-reduced-motion</code>.'))
b.append(tile('<button class="btn btn-secondary" type="button" data-dialog="nav-sheet-demo">Open the mobile sheet</button>'
    '<dialog class="nav-sheet" id="nav-sheet-demo">'
    '<div class="nav-sheet__in">'
    '<span class="nav-sheet__scan" aria-hidden="true"></span>'
    '<div class="nav-sheet__head">' + LOGO +
    '<button class="btn-close" type="button" data-dialog-close aria-label="Close menu"></button></div>'
    '<nav class="nav-sheet__links">'
    + ''.join(f'<a class="nav-sheet__link" href="#i" style="--i:{i}"'
              + (' aria-current="page"' if i == 0 else '') +
              f'><svg class="icon" aria-hidden="true"><use href="#i-{ic}"/></svg>{lbl}</a>'
              for i, (lbl, ic) in enumerate([('Blog', 'pen'), ('Videos', 'camera'), ('Courses', 'book'),
                                             ('Projects', 'code'), ('Travel', 'plane'), ('Topics', 'tag')]))
    + '</nav>'
    '<div class="nav-sheet__foot"><span class="t-slate-sm" style="color:var(--fg-faint)">'
    '<span class="dot dot-sm dot-live"></span> still rolling</span>'
    '<button class="btn btn-primary btn-sm btn-pill">Subscribe</button></div>'
    '</div></dialog>',
    '<b>dialog.nav-sheet</b> — press the button; Escape closes it'))
b.append(code('html', [
    f'{K("&lt;dialog")} class={S(chr(34)+"nav-sheet"+chr(34))} id={S(chr(34)+"site-menu"+chr(34))}{K("&gt;")}',
    f'  {K("&lt;div")} class={S(chr(34)+"nav-sheet__in"+chr(34))}{K("&gt;")}',
    f'    {K("&lt;span")} class={S(chr(34)+"nav-sheet__scan"+chr(34))} aria-hidden={S(chr(34)+"true"+chr(34))}{K("&gt;&lt;/span&gt;")}',
    f'    {K("&lt;div")} class={S(chr(34)+"nav-sheet__head"+chr(34))}{K("&gt;")}… mark + .btn-close …{K("&lt;/div&gt;")}',
    f'    {K("&lt;nav")} class={S(chr(34)+"nav-sheet__links"+chr(34))}{K("&gt;")}',
    f'      {C("&lt;!-- --i is the stagger index --&gt;")}',
    f'      {K("&lt;a")} class={S(chr(34)+"nav-sheet__link"+chr(34))} style={S(chr(34)+"--i:0"+chr(34))} href={S(chr(34)+"/blog/"+chr(34))}{K("&gt;")}Blog{K("&lt;/a&gt;")}',
    f'    {K("&lt;/nav&gt;")}',
    f'    {K("&lt;div")} class={S(chr(34)+"nav-sheet__foot"+chr(34))}{K("&gt;")}…{K("&lt;/div&gt;")}',
    f'  {K("&lt;/div&gt;")}',
    f'{K("&lt;/dialog&gt;")}',
], 'set <b>--i</b> per row for the stagger; open with <b>.showModal()</b>, never by toggling a class'))
b.append(code('js', [
    f'{K("const")} sheet = document.{F("getElementById")}({S(chr(39)+"site-menu"+chr(39))});',
    f'{K("const")} btn   = document.{F("querySelector")}({S(chr(39)+".nav-burger"+chr(39))});',
    '',
    f'btn.{F("addEventListener")}({S(chr(39)+"click"+chr(39))}, () =&gt; {{',
    f'  sheet.{F("showModal")}();',
    f'  btn.{F("setAttribute")}({S(chr(39)+"aria-expanded"+chr(39))}, {S(chr(39)+"true"+chr(39))});',
    '});',
    f'sheet.{F("addEventListener")}({S(chr(39)+"close"+chr(39))}, () =&gt;',
    f'  btn.{F("setAttribute")}({S(chr(39)+"aria-expanded"+chr(39))}, {S(chr(39)+"false"+chr(39))}));',
], 'the <b>close</b> event fires for Escape too, so the burger always returns to bars'))

# 8 · responsive ─────────────────────────────────────────────────────────────
b.append(h2('8 · Responsive collapse'))
b.append(p(
    'Put <code class="t-code">.nav-collapse</code> on the island: the link row hides '
    'below 48rem and the burger appears. No duplicate markup, no JS, no breakpoint '
    'classes in the template. <b>Narrow this window</b> to watch it swap.'))
b.append(tile(bar(LOGO + links([('Blog', 'pen', True), ('Videos', 'camera', False),
                                ('Courses', 'book', False), ('Travel', 'plane', False)])
                  + '<div class="cluster-sm">' + burger()
                  + '<button class="btn btn-primary btn-sm btn-pill">Subscribe</button></div>',
                  'nav-bar nav-collapse'),
    '<b>.nav-collapse</b> — links above 48rem, burger below'))

# 9 · the submenu row ────────────────────────────────────────────────────────
b.append(h2('9 · The submenu row'))
b.append(p(
    'When you are inside something — a lesson, an episode, a trip — the site menu '
    '<b>stays</b> and a second row appears beneath it, in the same island. The way out '
    'never disappears, and opening a lesson no longer swaps a whole bar out from under '
    'the reader. Wrap the two rows in <code class="t-code">.nav-stack</code>: the island '
    'stops being a pill and becomes one card holding both.'))
b.append(p(
    'There is no class per collection. One design, three knobs — '
    '<code class="t-code">data-tone</code>, <code class="t-code">data-density</code> and '
    '<code class="t-code">--value</code> — because a course and a trip differ in the words '
    'they put in the slots, not in their CSS.'))

b.append(tile(stack(
    LOGO + links([('Watch', None, False), ('Learn', None, True), ('Build', None, False)])
    + '<div class="cluster-sm">' + burger('nav-burger-bare') + '</div>',
    '<a class="nav-context__back" href="#i">← Course</a>'
    '<span class="nav-context__where"><span class="nav-context__title">Handlebars without tears</span>'
    '<span class="nav-context__pos">Lesson 3 of 14</span></span>'
    '<div class="nav-context__actions"><button class="btn btn-quiet btn-sm">← Prev</button>'
    '<button class="btn btn-primary btn-sm">Next →</button></div>'
    '<span class="nav-rail" style="--value:21%"></span>',
    sub_attrs=' data-mark="pos" style="--value:21%"'),
    '<b>.nav-stack</b> — the site menu on top, the lesson beneath it; one object, two rows'))

b.append(tile(stack(
    LOGO + links([('Watch', None, True), ('Learn', None, False), ('Build', None, False)]),
    '<a class="nav-context__back" href="#i">← Series</a>'
    '<span class="nav-context__where"><span class="nav-context__kind">Episode</span>'
    '<span class="nav-context__title">The Build Season</span>'
    '<span class="nav-context__pos">07</span></span>'
    '<div class="nav-context__actions"><span class="badge badge-live">Live</span>'
    '<button class="btn btn-quiet btn-sm">Episodes</button></div>',
    sub_attrs=' data-tone="ink" data-density="compact"'),
    '<b>data-tone="ink"</b> — the same row, in cinema tone; the site menu above stays paper'))

b.append(code('html', [
    f'{K("&lt;div")} class={S(chr(34)+"nav-shell"+chr(34))}{K("&gt;")}',
    f'  {K("&lt;div")} class={S(chr(34)+"nav-stack"+chr(34))}{K("&gt;")}',
    f'    {K("&lt;nav")} class={S(chr(34)+"nav-bar"+chr(34))}{K("&gt;")}… site menu …{K("&lt;/nav&gt;")}',
    f'    {K("&lt;div")} class={S(chr(34)+"nav-sub nav-context"+chr(34))} data-tone={S(chr(34)+"ink"+chr(34))}',
    f'         style={S(chr(34)+"--value:21%; --pos-prefix:&#39;DAY &#39;"+chr(34))}{K("&gt;")}',
    f'      {K("&lt;a")} class={S(chr(34)+"nav-context__back"+chr(34))} href={S(chr(34)+"/course"+chr(34))}{K("&gt;")}← Course{K("&lt;/a&gt;")}',
    f'      {K("&lt;span")} class={S(chr(34)+"nav-context__where"+chr(34))}{K("&gt;")}',
    f'        {K("&lt;span")} class={S(chr(34)+"nav-context__title"+chr(34))}{K("&gt;")}Course name{K("&lt;/span&gt;")}',
    f'        {K("&lt;span")} class={S(chr(34)+"nav-context__pos"+chr(34))}{K("&gt;")}3 of 14{K("&lt;/span&gt;")}',
    f'      {K("&lt;/span&gt;")}',
    f'      {K("&lt;div")} class={S(chr(34)+"nav-context__actions"+chr(34))}{K("&gt;")}… prev / next …{K("&lt;/div&gt;")}',
    f'      {K("&lt;span")} class={S(chr(34)+"nav-rail"+chr(34))}{K("&gt;&lt;/span&gt;")}',
    f'    {K("&lt;/div&gt;")}',
    f'  {K("&lt;/div&gt;")}',
    f'{K("&lt;/div&gt;")}',
], 'drive the rail with <b>--value</b>; it transitions on its own'))

b.append(ct([
    ('data-tone', '<code class="t-code">paper</code> (default) · <code class="t-code">ink</code> · <code class="t-code">accent</code>'),
    ('data-density', '<code class="t-code">regular</code> (default) · <code class="t-code">compact</code> for players'),
    ('data-mark="pos"', 'the accent marks the position — for players, where “where am I” is the point'),
    ('--value', 'the progress rail, <code class="t-code">0%</code>–<code class="t-code">100%</code>'),
    ('--pos-prefix', 'the word in front of the number — <code class="t-code">\'DAY \'</code>, <code class="t-code">\'EP.\'</code>'),
], head=('Knob', 'Values')))

# 10 · shell behaviour ───────────────────────────────────────────────────────
b.append(h2('10 · How the bar behaves on scroll'))
b.append(p(
    'Four behaviours, none of which change the markup. Put the class on the shell; '
    '<code class="t-code">nav.js</code> sets <code class="t-code">data-scrolled</code> and '
    '<code class="t-code">data-dir</code>, and every visible decision after that is CSS.'))
b.append(ct([
    ('.nav-shell', 'the default — a sticky island that never changes shape'),
    ('.nav-shell-fixed', 'pinned to the top, always there'),
    ('.nav-shell-auto', 'hides on the way down, returns on the way up — reading gets the screen, '
                        'navigating gets the bar'),
    ('.nav-shell-morph', 'full-bleed at rest; contracts into the island once the page has moved'),
], head=('Class', 'Behaviour')))
b.append(tile(
    '<div class="np__scroller" data-scroll-demo>'
    '<div class="np__scroller-in">'
    '<div class="nav-shell nav-shell-morph" data-scroll-at="12" style="position:sticky">'
    + f'<nav class="nav-bar" aria-label="Morph demo">{LOGO}'
    + '<div class="nav-links"><a class="nav-link" href="#i" aria-current="page">Watch</a>'
      '<a class="nav-link" href="#i">Learn</a><a class="nav-link" href="#i">Build</a></div>'
      '<div class="nav-actions"><button class="btn btn-primary btn-sm btn-pill">Subscribe</button></div>'
      '</nav></div>'
    '<div class="np__filler"><p class="t-slate-sm">scroll this panel ↓</p></div>'
    '</div></div>',
    '<b>.nav-shell-morph</b> — full width at the top, an island once you move; scroll inside the box'))
b.append(code('html', [
    f'{K("&lt;header")} class={S(chr(34)+"nav-shell nav-shell-morph"+chr(34))} data-scroll-at={S(chr(34)+"24"+chr(34))}{K("&gt;")}',
    f'  {K("&lt;nav")} class={S(chr(34)+"nav-bar"+chr(34))}{K("&gt;")}…{K("&lt;/nav&gt;")}',
    f'{K("&lt;/header&gt;")}',
    '',
    C('&lt;!-- nav.js adds data-scrolled past data-scroll-at (default 24px) --&gt;'),
], 'one class, plus <b>nav.js</b>; no inline handlers and no scroll maths in your theme'))

# 11 · the line is the progress ──────────────────────────────────────────────
b.append(h2('11 · The line is the progress'))
b.append(p(
    'The island already has a hairline. Rather than add a second piece of chrome under it, '
    'the line itself fills: the read part is the accent, the rest is the accent at a whisper. '
    'Set <code class="t-code">--progress</code> and the border does the rest — it works on the '
    'plain bar and on the two-row stack alike.'))
b.append(tile(
    '<div class="nav-shell nav-progress" style="position:static;padding-inline:0;max-width:none;--progress:64%">'
    + f'<nav class="nav-bar" aria-label="Progress demo">{LOGO}'
    + '<div class="nav-links"><a class="nav-link" href="#i" aria-current="page">Read</a>'
      '<a class="nav-link" href="#i">Notes</a></div>'
      '<div class="nav-actions"><span class="t-slate-sm" style="color:var(--fg-faint)">64%</span></div>'
      '</nav></div>',
    '<b>.nav-progress</b> — <code class="t-code">--progress:64%</code>; the border is the bar'))
b.append(code('html', [
    f'{K("&lt;header")} class={S(chr(34)+"nav-shell nav-progress"+chr(34))} style={S(chr(34)+"--progress:64%"+chr(34))}{K("&gt;")}',
    f'  {K("&lt;nav")} class={S(chr(34)+"nav-bar"+chr(34))}{K("&gt;")}…{K("&lt;/nav&gt;")}',
    f'{K("&lt;/header&gt;")}',
], 'the ring is masked to the border, so the radius survives the gradient'))

# 12 · three more shapes ─────────────────────────────────────────────────────
b.append(h2('12 · Centred, inverse, compact'))
b.append(p(
    'Three shapes that are token swaps rather than layouts of their own. The inverse bar takes '
    'the light mark for free — the logo is markup reading <code class="t-code">currentColor</code>, '
    'so it inverts with the bar and needs no second asset.'))
b.append(tile(bar(
    '<div class="nav-links"><a class="nav-link" href="#i" aria-current="page">Work</a>'
    '<a class="nav-link" href="#i">About</a></div>'
    + LOGO +
    '<div class="nav-actions"><button class="btn btn-secondary btn-sm btn-pill">Contact</button></div>',
    'nav-bar nav-bar-center'),
    '<b>.nav-bar-center</b> — the mark takes the middle, links and actions balance it'))
b.append(tile(bar(
    LOGO + '<div class="nav-links"><a class="nav-link" href="#i" aria-current="page">Watch</a>'
    '<a class="nav-link" href="#i">Learn</a><a class="nav-link" href="#i">Build</a></div>'
    '<div class="nav-actions"><button class="btn btn-primary btn-sm btn-pill">Subscribe</button></div>',
    'nav-bar nav-bar-center nav-bar-inverse'),
    '<b>.nav-bar-inverse</b> — ink whatever the theme; the mark inverts with it'))
b.append(tile(bar(
    LOGO + '<div class="nav-links"><a class="nav-link" href="#i" aria-current="page">Index</a>'
    '<a class="nav-link" href="#i">Archive</a></div>'
    '<div class="nav-actions"><span class="dot dot-sm"></span></div>',
    'nav-bar nav-bar-compact'),
    '<b>.nav-bar-compact</b> — 2.75rem; for docs and players where the bar is chrome'))

# 13 · the record burger ─────────────────────────────────────────────────────
b.append(h2('13 · The burger, as a record light'))
b.append(p(
    'Three bars becoming an X says nothing about what this site is. Here they collapse into the '
    'record light the whole system is built around, and the light unfolds into a play head: closed '
    'is <em>ready</em>, open is <em>rolling</em>. Same markup as every other burger — '
    '<code class="t-code">aria-expanded</code> drives it, so the glyph and the accessibility tree '
    'can never disagree.'))
b.append(tile(
    '<div class="cluster" style="gap:var(--space-6);align-items:center">'
    + burger('nav-burger-rec') + burger('nav-burger-aperture') + burger('nav-burger-squeeze')
    + burger('nav-burger-bare') +
    '</div>',
    '<b>.nav-burger-rec</b> · .nav-burger-aperture · .nav-burger-squeeze · .nav-burger-bare — click each'))

# 14 · dropdowns that grow ───────────────────────────────────────────────────
b.append(h2('14 · Dropdowns — hover, click, and a second level'))
b.append(p(
    'Pointer users open on hover with an intent delay, everyone else on click, and both land on the '
    'same <code class="t-code">&lt;details open&gt;</code> — one open state, not two. Touch is left '
    'alone, because there the first tap <em>is</em> the hover and stealing it costs the reader their '
    'click. The panel grows to its content rather than jumping to it.'))
b.append(tile(bar(
    LOGO +
    '<div class="nav-links">'
    '<a class="nav-link" href="#i">Watch</a>'
    '<details class="nav-menu nav-menu-hover nav-menu-grow"><summary class="nav-link">Learn</summary>'
    '<div class="nav-menu__panel">'
    '<a class="dropdown__item" href="#i">All courses</a>'
    '<a class="dropdown__item" href="#i">Free lessons</a>'
    '<details class="nav-sub-menu"><summary>By subject</summary>'
    '<div class="nav-sub-menu__items"><div>'
    '<a class="dropdown__item" href="#i">CSS &amp; layout</a>'
    '<a class="dropdown__item" href="#i">Motion</a>'
    '<a class="dropdown__item" href="#i">Video craft</a>'
    '</div></div></details>'
    '</div></details>'
    '<a class="nav-link" href="#i">Build</a></div>'
    + '<div class="nav-actions"><span class="dot dot-sm"></span></div>'),
    '<b>.nav-menu-hover.nav-menu-grow</b> + <b>.nav-sub-menu</b> — hover it, then open “By subject”'))
b.append(ct([
    ('.nav-menu-hover', 'opens on hover for fine pointers, with a 120ms intent delay'),
    ('.nav-menu-grow', 'the panel animates to its own height (0fr → 1fr), no fixed max-height'),
    ('.nav-sub-menu', 'a second level, disclosed in place — never a fly-out'),
], head=('Class', 'What it adds')))

# 15 · opening on small screens ──────────────────────────────────────────────
b.append(h2('15 · Three ways to open on a phone'))
b.append(p(
    'The full-screen sheet is one answer, not the only one. All three take the same link markup, '
    'so choosing between them is a class rather than a rewrite.'))
b.append(ct([
    ('.nav-sheet', 'full-screen dialog; irises open from the button, scanline sweeps once'),
    ('.nav-sheet-drop', 'full-width panel hinged at the top edge — the page stays visible beneath'),
    ('.nav-panel', 'no dialog at all: the island itself grows into the panel'),
], head=('Class', 'Opens as')))
b.append(tile(
    '<div class="nav-shell" style="position:static;padding-inline:0;max-width:none">'
    '<div class="nav-stack">'
    + f'<nav class="nav-bar" aria-label="Panel demo">{LOGO}'
    + '<div class="nav-links"><a class="nav-link" href="#i" aria-current="page">Watch</a>'
      '<a class="nav-link" href="#i">Learn</a></div>'
      '<div class="nav-actions">'
      '<button class="nav-burger nav-burger-rec" type="button" aria-expanded="false" '
      'data-panel-toggle><span class="nav-burger__box"><span class="nav-burger__bars"></span></span>'
      '<span class="u-sr-only">Menu</span></button></div></nav>'
    '<div class="nav-panel"><div class="nav-panel__in">'
    '<div class="nav-panel__links">'
    '<a class="nav-panel__link" href="#i" aria-current="page">Watch<span class="t-slate-sm">128</span></a>'
    '<a class="nav-panel__link" href="#i">Learn<span class="t-slate-sm">14</span></a>'
    '<a class="nav-panel__link" href="#i">Build<span class="t-slate-sm">31</span></a>'
    '<a class="nav-panel__link" href="#i">Travel<span class="t-slate-sm">9</span></a>'
    '</div>'
    '<div class="nav-panel__aside">'
    '<span class="nav-panel__label">Latest</span>'
    '<p class="t-small">Handlebars without tears — lesson 3 is up.</p>'
    '<span class="nav-panel__label" style="margin-top:var(--space-2)">Newsletter</span>'
    '<form class="cluster-sm" onsubmit="return false">'
    '<input class="input input-sm" type="email" placeholder="you@example.com" aria-label="Email" />'
    '<button class="btn btn-primary btn-sm" type="submit">Join</button></form>'
    '</div></div></div>'
    '</div></div>',
    '<b>.nav-panel</b> — press the burger: the island grows, nothing covers the page'))
b.append(code('html', [
    f'{K("&lt;div")} class={S(chr(34)+"nav-shell"+chr(34))}{K("&gt;")}',
    f'  {K("&lt;div")} class={S(chr(34)+"nav-stack"+chr(34))}{K("&gt;")}',
    f'    {K("&lt;nav")} class={S(chr(34)+"nav-bar"+chr(34))}{K("&gt;")}',
    f'      … {K("&lt;button")} class={S(chr(34)+"nav-burger nav-burger-rec"+chr(34))}',
    f'             aria-expanded={S(chr(34)+"false"+chr(34))} data-panel-toggle{K("&gt;")}…{K("&lt;/button&gt;")}',
    f'    {K("&lt;/nav&gt;")}',
    f'    {K("&lt;div")} class={S(chr(34)+"nav-panel"+chr(34))}{K("&gt;")}',
    f'      {K("&lt;div")} class={S(chr(34)+"nav-panel__in"+chr(34))}{K("&gt;")}… links + aside …{K("&lt;/div&gt;")}',
    f'    {K("&lt;/div&gt;")}',
    f'  {K("&lt;/div&gt;")}',
    f'{K("&lt;/div&gt;")}',
], 'nav.js flips <b>data-open</b> on the stack; Escape closes it and returns focus'))

# 16 · actions ───────────────────────────────────────────────────────────────
b.append(h2('16 · Icons, the call, and the form'))
b.append(p(
    'A creator\'s bar carries more than links: where else to find them, the one thing they want you '
    'to do, and the list. The newsletter is folded into its own icon — closed it is one more chip, '
    'open it is a field that grew out of that chip. It is a '
    '<code class="t-code">&lt;details&gt;</code>, so Escape and focus come free.'))
b.append(tile(bar(
    LOGO + '<div class="nav-links"><a class="nav-link" href="#i" aria-current="page">Watch</a>'
    '<a class="nav-link" href="#i">Learn</a></div>'
    '<div class="nav-actions">'
    '<div class="nav-icons">'
    '<a class="nav-icon" href="#i" aria-label="GitHub"><svg class="icon" aria-hidden="true"><use href="#i-code"/></svg></a>'
    '<a class="nav-icon" href="#i" aria-label="Chat"><svg class="icon" aria-hidden="true"><use href="#i-chat"/></svg></a>'
    '<a class="nav-icon" href="#i" aria-label="Share"><svg class="icon" aria-hidden="true"><use href="#i-share"/></svg></a>'
    '</div>'
    '<details class="nav-form"><summary aria-label="Subscribe to the newsletter">'
    '<svg class="icon" aria-hidden="true"><use href="#i-mail"/></svg></summary>'
    '<form class="nav-form__field" onsubmit="return false">'
    '<input type="email" placeholder="you@example.com" aria-label="Email address" />'
    '<button class="btn btn-primary btn-sm btn-pill" type="submit">Join</button></form></details>'
    '<button class="btn btn-primary btn-sm btn-pill">Subscribe</button>'
    '</div>'),
    '<b>.nav-icons</b> · <b>.nav-form</b> · the CTA — press the envelope'))

# 17 · the submenu on a phone ────────────────────────────────────────────────
b.append(h2('17 · The submenu on a phone'))
b.append(p(
    'A lesson row that reads fine on a desktop becomes three competing things on a phone: where you '
    'are, how far in, and how to get anywhere else. So below 48rem the row keeps only where you are, '
    'and the rest moves behind a second burger — one that belongs to the submenu, not to the site. '
    'It opens the index, which is the point: “Lesson 3 of 14” only helps if the other thirteen are '
    'one press away.'))
b.append(tile(
    '<div class="nav-shell" style="position:static;padding-inline:0;max-width:none">'
    '<div class="nav-stack" id="np-sub-demo">'
    + f'<nav class="nav-bar" aria-label="Lesson demo">{LOGO}'
    + '<div class="nav-links"><a class="nav-link" href="#i" aria-current="page">Learn</a></div>'
      '<div class="nav-actions"><span class="dot dot-sm"></span></div></nav>'
    '<div class="nav-sub nav-context" data-mark="pos" style="--value:21%">'
    '<a class="nav-context__back" href="#i">← Courses</a>'
    '<span class="nav-context__where"><span class="nav-context__title">Handlebars without tears</span>'
    '<span class="nav-context__pos">3 of 14</span></span>'
    '<div class="nav-context__actions">'
    '<button class="btn btn-quiet btn-sm" type="button">← Prev</button>'
    '<button class="btn btn-primary btn-sm" type="button">Next →</button></div>'
    '<button class="nav-burger nav-burger-bare nav-sub__more" type="button" aria-expanded="false" '
    'data-nav-open="np-index" aria-controls="np-index">'
    '<span class="nav-burger__box"><span class="nav-burger__bars"></span></span>'
    '<span class="u-sr-only">Lessons</span></button>'
    '<button class="nav-sub__hide" type="button" data-sub-hide aria-label="Hide this row">×</button>'
    '<span class="nav-rail"></span></div>'
    '<button class="nav-sub-show" type="button" data-sub-show>Show lesson bar</button>'
    '</div></div>'
    '<dialog class="nav-sheet nav-sheet-index" id="np-index">'
    '<div class="nav-sheet__in"><div class="nav-sheet__head">'
    '<span class="t-slate-sm" style="color:var(--fg-faint)">Handlebars without tears</span>'
    '<button class="btn-close" type="button" data-nav-close aria-label="Close"></button></div>'
    '<div class="nav-sheet__links">'
    '<a class="nav-sheet__link" style="--i:0" href="#i"><span class="nav-index__num">01</span>'
    'What a template is<span class="nav-index__done"></span></a>'
    '<a class="nav-sheet__link" style="--i:1" href="#i"><span class="nav-index__num">02</span>'
    'Contexts and blocks<span class="nav-index__done"></span></a>'
    '<a class="nav-sheet__link" style="--i:2" href="#i" aria-current="page">'
    '<span class="nav-index__num">03</span>Handlebars without tears</a>'
    '<a class="nav-sheet__link" style="--i:3" href="#i"><span class="nav-index__num">04</span>Partials</a>'
    '<a class="nav-sheet__link" style="--i:4" href="#i"><span class="nav-index__num">05</span>Helpers</a>'
    '</div></div></dialog>',
    'narrow the window under <b>48rem</b>: prev/next fold into the index button · '
    '<b>×</b> hides the row, and the sliver brings it back'))
b.append(ct([
    ('.nav-sub__more', 'the submenu\'s own burger — shown under 48rem, opens the index'),
    ('.nav-sheet-index', 'the collection as a list, with position marked and done rows ticked'),
    ('[data-sub-hide] · [data-sub-show]', 'collapse the row; the choice is remembered in localStorage'),
], head=('Class', 'What it does')))

# 18 · structured data ───────────────────────────────────────────────────────
b.append(h2('18 · Telling machines what the nav is'))
b.append(p(
    'Markup alone does not say “these five links are the site navigation”. '
    '<code class="t-code">SiteNavigationElement</code> does, and a '
    '<code class="t-code">BreadcrumbList</code> says where the current page sits inside it. '
    'Every page of these docs ships both — view source and look for '
    '<code class="t-code">application/ld+json</code>.'))
b.append(code('html', [
    f'{K("&lt;script")} type={S(chr(34)+"application/ld+json"+chr(34))}{K("&gt;")}',
    '{',
    f'  {S(chr(34)+"@context"+chr(34))}: {S(chr(34)+"https://schema.org"+chr(34))},',
    f'  {S(chr(34)+"@type"+chr(34))}: {S(chr(34)+"ItemList"+chr(34))},',
    f'  {S(chr(34)+"itemListElement"+chr(34))}: [',
    '    { ' + f'{S(chr(34)+"@type"+chr(34))}: {S(chr(34)+"SiteNavigationElement"+chr(34))},'
    + f' {S(chr(34)+"position"+chr(34))}: {F("1")},',
    f'      {S(chr(34)+"name"+chr(34))}: {S(chr(34)+"Watch"+chr(34))},'
    + f' {S(chr(34)+"url"+chr(34))}: {S(chr(34)+"/watch/"+chr(34))} ' + '}',
    '  ]',
    '}',
    f'{K("&lt;/script&gt;")}',
], 'one list per nav; the breadcrumb is a second block, not a second list'))

# 10 · rules ─────────────────────────────────────────────────────────────────
b.append(h2('19 · Rules'))
b.append('<div class="grid-2 u-mb-6" style="gap:var(--space-4)">'
    '<div class="surface u-p-5"><h3 class="t-h4 u-mb-3">Do</h3>'
    '<ul class="t-small u-fg-subtle" style="padding-left:1.1rem;display:grid;gap:var(--space-2)">'
    '<li>Mark the current page with <code class="t-code">aria-current="page"</code>.</li>'
    '<li>Keep one dot per bar — it means “you are here”, not “this is nice”.</li>'
    '<li>Keep the site menu and add a submenu row beneath it — never swap the bar out.</li>'
    '<li>Use <code class="t-code">&lt;details&gt;</code> and <code class="t-code">&lt;dialog&gt;</code> so keyboard and Escape work for free.</li>'
    '<li>Give every icon-only control an accessible name.</li>'
    '</ul></div>'
    '<div class="surface u-p-5"><h3 class="t-h4 u-mb-3">Don’t</h3>'
    '<ul class="t-small u-fg-subtle" style="padding-left:1.1rem;display:grid;gap:var(--space-2)">'
    '<li>Use an <code class="t-code">.active</code> class — it can disagree with the a11y tree.</li>'
    '<li>Fill the active link with a coloured pill.</li>'
    '<li>Nest a second dropdown level; promote it to a mega panel.</li>'
    '<li>Duplicate the menu markup for mobile — <code class="t-code">.nav-collapse</code> already handles it.</li>'
    '<li>Write a new class per collection; set <code class="t-code">data-tone</code> and fill the slots.</li>'
    '</ul></div></div>')

# ── Variants ────────────────────────────────────────────────────────────────

VARIANTS = [
    ('island', 'Island', 'nav-shell',
     'The floating pill, sticky from the first pixel. The default.'),
    ('fixed', 'Fixed', 'nav-shell nav-shell-fixed',
     'Pinned to the top and never anywhere else. For apps and dashboards, where '
     'the chrome is furniture.'),
    ('morph', 'Island on scroll', 'nav-shell nav-shell-morph',
     'Full-bleed at rest, drawing itself into the island once the page has moved. '
     'The header a site opens with, and the bar it works with.'),
    ('auto', 'Fixed on scroll', 'nav-shell nav-shell-auto',
     'In flow at the top; pinned once you scroll up, and out of the way while you '
     'read down. Reading gets the screen, navigating gets the bar.'),
]

b.append(h2('20 · Variants — four positions, one markup'))
b.append(p(
    'Not ten skins. A bar\'s <em>shape</em> is decided once in the design; where it goes '
    'when the reader scrolls is a decision about <em>behaviour</em>, and that is the one '
    'worth a variant. Put the class on the shell — the bar never changes, so switching is '
    'a class swap and never a restructure.'))
b.append(p(
    'The skins that used to be variants are the things they always were: '
    '<code class="t-code">.nav-bar-center</code>, <code class="t-code">.nav-bar-inverse</code> '
    'and <code class="t-code">.nav-bar-compact</code> for shape, '
    '<code class="t-code">.nav-shell-flush</code> and <code class="t-code">.nav-shell-full</code> '
    'for alignment, <code class="t-code">.nav-ghost</code> for a bar that materialises over a '
    'hero. Nothing was lost — the list stopped pretending “bordered” and “island” were the '
    'same kind of choice.'))
b.append(ct([(f'.{c.split()[-1] if len(c.split()) > 1 else "nav-shell"}', f'<b>{name}</b> — {desc}')
             for _, name, c, desc in VARIANTS], head=('Class', 'Position')))

for _slug, _name, _cls, _desc in VARIANTS:
    b.append(tile(
        f'<div class="{_cls}" style="position:static;padding-inline:0;max-width:none">'
        + f'<nav class="nav-bar" aria-label="{_name} demo">{LOGO}'
        + links([('Blog', None, True), ('Videos', None, False), ('Courses', None, False)])
        + '<div class="nav-actions">'
          '<button class="btn btn-primary btn-sm btn-pill">Subscribe</button></div></nav></div>',
        f'<b>{_name}</b> — {_desc}'))

b.append(h2('21 · Choosing one in a Ghost theme'))
b.append(p(
    'Two levels, and the more specific one wins: a site-wide default from a theme '
    'setting, overridden per post or page by an internal tag.'))
b.append(ct([
    ('Site default', 'Ghost Admin &rarr; Design &rarr; <b>Navbar style</b> (a <code class="t-code">select</code> in package.json)'),
    ('Per-page override', 'tag the post <code class="t-code">#navbar-ghost</code>, <code class="t-code">#navbar-inverse</code>, … — internal tags never show to readers'),
    ('Why the tag wins', 'a landing page that opens on a full-bleed hero genuinely knows better than the site default'),
], head=('Level', 'How')))
b.append(code('handlebars', [
    C('&lt;!-- partials/navbar.hbs --&gt;'),
    K('{{#has') + ' tag=' + S('"#navbar-ghost"') + K('}}') + K('{{&gt; nav/bar') + ' style=' + S('"ghost"') + K('}}'),
    K('{{else}}') + K('{{&gt; nav/bar') + ' style=@custom.navbar_style' + K('}}'),
    K('{{/has}}'),
], 'the tag override first, the theme setting as the fallback'))

# 22 · the builder ───────────────────────────────────────────────────────────
b.append(h2('22 · Navbar builder'))
b.append(p(
    'Every knob on this page, in one place. Start from a preset — a web series, a docs '
    'site, a course — then change anything: the position, the accent, what the main row '
    'carries, what the submenu says. The markup underneath rewrites itself as you go, so '
    'what you copy is what you are looking at.'))
b.append(PLAYGROUND)

PAGES['navbar'] = ('Navbar',
    'The site chrome, end to end: anatomy, alignment, the active link, dropdowns, the '
    'submenu row, four positions, three ways to open on a phone — and a builder that '
    'writes the markup for whichever combination you land on.',
    '\n'.join(b))