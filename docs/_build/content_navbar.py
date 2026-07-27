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


# ── the page ────────────────────────────────────────────────────────────────

b = []

b.append(p(
    'The navbar is one component with several shapes: a site bar, a bar with menus, '
    'a mobile sheet, and a contextual bar for each container module. They share a '
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

# 9 · contextual ─────────────────────────────────────────────────────────────
b.append(h2('9 · Contextual bars — one per collection'))
b.append(p(
    'Inside a container module the site bar is <b>replaced</b>, never stacked on. One '
    'base — <code class="t-code">.nav-context</code> — with four slots: close, '
    'where-you-are, actions, and a progress rail. Skins change only what the medium '
    'demands, so cutting from a blog bar to a lesson player never moves the chrome.'))
b.append(tile(bar('<button class="btn-close" type="button" aria-label="Close course"></button>'
    '<span class="nav-context__where"><span class="nav-context__title">Handlebars without tears</span>'
    '<span class="nav-context__pos">Lesson 3 of 14</span></span>'
    '<div class="cluster-sm"><button class="btn btn-quiet btn-sm">← Prev</button>'
    '<button class="btn btn-primary btn-sm">Next →</button></div>'
    '<span class="nav-rail" style="--value:21%"></span>', 'nav-bar nav-context nav-lesson'),
    '<b>.nav-context.nav-lesson</b> — course player: close · position · pager · progress rail'))
b.append(tile(bar('<button class="btn-close btn-close-inverse" type="button" aria-label="Exit series"></button>'
    '<span class="nav-context__where"><span class="nav-context__title">The Build Season</span>'
    '<span class="nav-context__pos">EP.07</span></span>'
    '<div class="cluster-sm"><span class="badge badge-live">Live</span>'
    '<button class="btn btn-quiet btn-sm">Episodes</button></div>', 'nav-bar nav-context nav-episode'),
    '<b>.nav-context.nav-episode</b> — always ink; it is cinema, and cinema is dark'))
b.append(tile(bar('<button class="btn-close" type="button" aria-label="Close trip"></button>'
    '<span class="nav-context__where"><span class="nav-context__title">Georgia, in eight days</span>'
    '<span class="nav-context__pos">3</span></span>'
    '<div class="cluster-sm"><button class="btn btn-quiet btn-sm">Itinerary</button></div>'
    '<span class="nav-rail" style="--value:38%"></span>', 'nav-bar nav-context nav-trip'),
    '<b>.nav-context.nav-trip</b> — the day counter prefixes itself'))
b.append(tile(bar(LOGO + links([('Overview', None, True), ('Build log', None, False), ('Repo', None, False)], 'nav-links-rule')
    + '<div class="cluster-sm"><span class="badge badge-success">Shipped</span></div>', 'nav-bar nav-docs'),
    '<b>.nav-docs</b> — dense bars take the rule, not the dot'))
b.append(code('html', [
    f'{K("&lt;nav")} class={S(chr(34)+"nav-bar nav-context nav-lesson"+chr(34))}{K("&gt;")}',
    f'  {K("&lt;button")} class={S(chr(34)+"btn-close"+chr(34))} aria-label={S(chr(34)+"Close course"+chr(34))}{K("&gt;&lt;/button&gt;")}',
    f'  {K("&lt;span")} class={S(chr(34)+"nav-context__where"+chr(34))}{K("&gt;")}',
    f'    {K("&lt;span")} class={S(chr(34)+"nav-context__title"+chr(34))}{K("&gt;")}Course name{K("&lt;/span&gt;")}',
    f'    {K("&lt;span")} class={S(chr(34)+"nav-context__pos"+chr(34))}{K("&gt;")}Lesson 3 of 14{K("&lt;/span&gt;")}',
    f'  {K("&lt;/span&gt;")}',
    f'  {K("&lt;div")} class={S(chr(34)+"cluster-sm"+chr(34))}{K("&gt;")}… prev / next …{K("&lt;/div&gt;")}',
    f'  {K("&lt;span")} class={S(chr(34)+"nav-rail"+chr(34))} style={S(chr(34)+"--value:21%"+chr(34))}{K("&gt;&lt;/span&gt;")}',
    f'{K("&lt;/nav&gt;")}',
], 'drive the rail with <b>--value</b>; it transitions on its own'))
b.append(ct([
    ('.nav-lesson', 'course players — accent marks the position'),
    ('.nav-course · .nav-guide', 'container overviews — paper, with a rail'),
    ('.nav-episode', 'episodes and series — always ink, regardless of theme'),
    ('.nav-video', 'video pages — keeps the site links; you are still browsing'),
    ('.nav-trip', 'trips — the position renders as “DAY n”'),
    ('.nav-docs', 'documentation — pair with <code class="t-code">.nav-links-rule</code>'),
    ('.nav-shop', 'shop — actions pushed to the end'),
], head=('Skin', 'Used by')))

# 10 · rules ─────────────────────────────────────────────────────────────────
b.append(h2('10 · Rules'))
b.append('<div class="grid-2 u-mb-6" style="gap:var(--space-4)">'
    '<div class="surface u-p-5"><h3 class="t-h4 u-mb-3">Do</h3>'
    '<ul class="t-small u-fg-subtle" style="padding-left:1.1rem;display:grid;gap:var(--space-2)">'
    '<li>Mark the current page with <code class="t-code">aria-current="page"</code>.</li>'
    '<li>Keep one dot per bar — it means “you are here”, not “this is nice”.</li>'
    '<li>Replace the bar inside a container module; never stack two bars.</li>'
    '<li>Use <code class="t-code">&lt;details&gt;</code> and <code class="t-code">&lt;dialog&gt;</code> so keyboard and Escape work for free.</li>'
    '<li>Give every icon-only control an accessible name.</li>'
    '</ul></div>'
    '<div class="surface u-p-5"><h3 class="t-h4 u-mb-3">Don’t</h3>'
    '<ul class="t-small u-fg-subtle" style="padding-left:1.1rem;display:grid;gap:var(--space-2)">'
    '<li>Use an <code class="t-code">.active</code> class — it can disagree with the a11y tree.</li>'
    '<li>Fill the active link with a coloured pill.</li>'
    '<li>Nest a second dropdown level; promote it to a mega panel.</li>'
    '<li>Duplicate the menu markup for mobile — <code class="t-code">.nav-collapse</code> already handles it.</li>'
    '<li>Change the bar’s height per context; the chrome must not jump.</li>'
    '</ul></div></div>')

PAGES['navbar'] = ('Navbar',
    'The site chrome, end to end: anatomy, alignment, the active link, dropdown, mega '
    'panel, hamburger, the mobile sheet, responsive collapse, and one contextual bar '
    'per collection — with the markup for each.',
    '\n'.join(b))
