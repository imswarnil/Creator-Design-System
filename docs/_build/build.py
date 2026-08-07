#!/usr/bin/env python3
"""Creator Design System — docs site generator.

One page per topic. Two kinds of pages:
  * authored  — content_*.py modules export PAGES = {slug: (title, lead, body)}
  * fragment  — extracted legacy demos in fragments/ (see extract.py)

Re-run after editing content or fragments:
    python3 assets/design-system/preview/docs/_build/build.py
The NAV tree below drives the left sidebar, ordering and prev/next pagination.
The per-page TOC lives in the right rail beside the content, above the sponsor
card (scrollspy in preview.js).
"""
import pathlib, html, re, json

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
REPO = HERE.parent.parent
FRAG = HERE / 'fragments'
V = '?v=cds25'
SITE = 'https://creator.imswarnil.com'

import content_start, content_usage, content_collection, content_layout, content_forms, content_components, content_misc, content_extra, content_navbar, content_site, content_explorer, content_all

PAGES = {}
for mod in (content_start, content_usage, content_collection, content_layout, content_forms, content_components, content_misc, content_extra, content_navbar, content_site, content_explorer, content_all):
    PAGES.update(mod.PAGES)

# Fragment-backed pages: slug -> (folder, fragment, opts)
# opts: broadcast=True → dark default, guides toggle, 4-broadcast css, _style.css
A11Y_INTRO = """\t\t<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">
Accessibility means the site works for every reader — keyboard-only, screen-reader,
low-vision, colour-blind, motion-sensitive, on a cracked phone in sunlight. It is not
a compliance checklist bolted on at launch; it is the same craft as design: contrast
is legibility, focus order is layout, labels are copywriting. Below is the system's
contract — ten points, each demonstrated live, shipped as a foundation file
(<code class="t-code">08-a11y.css</code>) rather than an audit.</p>
"""

F, B = {}, dict(broadcast=True)
FRAGPAGES = {
    # Foundation
    'f-logo': ('foundation', 'logo', {}),
    'f-type': ('foundation', 'type', dict(intro=content_extra.TYPE_INTRO)), 'f-space': ('foundation', 'space', {}),
    'f-elevation': ('foundation', 'elevation', {}), 'f-layout': ('foundation', 'layout', {}),
    'f-pattern': ('foundation', 'pattern', {}), 'f-icons': ('foundation', 'icons', {}),
    'f-shape': ('foundation', 'shape', {}), 'f-devices': ('foundation', 'devices', {}),
    'f-frames': ('foundation', 'frames', {}), 'f-a11y': ('foundation', 'a11y', dict(intro=A11Y_INTRO)),
    # Motion
    'm-basics': ('foundation', 'motion-basics', dict(loop=True)),
    'm-text-effects': ('foundation', 'text-effects', dict(loop=True)),
    'm-annotations': ('foundation', 'annotations-the-hand-drawn-layer', dict(loop=True)),
    'm-micro': ('foundation', 'micro-interactions', dict(loop=True)),
    'm-presets': ('foundation', 'section-presets', dict(loop=True)),
    'm-stings': ('foundation', 'stings', dict(loop=True)),
    # Content extras / components extras
    'text-elements': ('elements', 'text', {}),
    'collection-cards': ('components', 'collection', {}),
    # Broadcast · YouTube
    'yt-thumbs': ('youtube', 'thumbs', B), 'yt-layouts': ('youtube', 'layouts', B),
    'yt-categories': ('youtube', 'categories', B), 'yt-series': ('youtube', 'series', B),
    'yt-livescenes': ('youtube', 'livescenes', B), 'yt-screens': ('youtube', 'screens', B),
    'yt-scenes': ('youtube', 'scenes', B), 'yt-live': ('youtube', 'live', B),
    'yt-end': ('youtube', 'end', B), 'yt-subs': ('youtube', 'subs', B),
    'yt-engage': ('youtube', 'engage', B), 'yt-brand': ('youtube', 'brand', B),
    'yt-backdrops': ('youtube', 'backdrops', B),
    # Broadcast · Social
    'ig-posts': ('social', 'posts', B), 'ig-carousel': ('social', 'carousel', B),
    'ig-story': ('social', 'story', B), 'ig-grid': ('social', 'grid', B),
    'ig-follow': ('social', 'follow', B), 'ig-share': ('social', 'share', B),
}

GROUP_ICONS = {
 'Start': '<circle cx="12" cy="12" r="3" fill="currentColor" stroke="none"/>',
 'Getting started': '<path d="M12 3v12M8 7l4-4 4 4M4 15v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/>',
 'Collections': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3Z"/>',
 'Pages': '<path d="M6 3h9l4 4v14a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1Z"/><path d="M14 3v5h5M8 12h8M8 16h5"/>',
 'Foundation': '<path d="M12 3 20 7.5v9L12 21 4 16.5v-9L12 3Z"/>',
 'Elements': '<path d="M4 7h16M4 12h10M4 17h13"/>',
 'Icons': '<circle cx="12" cy="12" r="7.5"/><path d="M12 7.5V12l3 2"/>',
 'Shape & Cutout': '<path d="M12 4l7 16H5l7-16Z"/>',
 'Grid & Layout': '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 12h16M12 4v16"/>',
 'Forms': '<rect x="4" y="5" width="16" height="5" rx="1.5"/><rect x="4" y="14" width="16" height="5" rx="1.5"/>',
 'Components': '<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/><path d="M13 7.5h7M7.5 13v7"/>',
 'Composites': '<path d="M5 6h14M5 12h14M5 18h9"/><circle cx="19" cy="18" r="1.5" fill="currentColor" stroke="none"/>',
 'Sections': '<rect x="4" y="4" width="16" height="5" rx="1"/><rect x="4" y="12" width="16" height="8" rx="1"/>',
 'Animation & Motion': '<path d="M4 12h4l2-5 3 10 2-5h5"/>',
 'Broadcast · YouTube': '<path d="M10 9.5v5l4.5-2.5L10 9.5Z" fill="currentColor" stroke="none"/><rect x="3.5" y="5.5" width="17" height="13" rx="3"/>',
 'Broadcast · Social': '<path d="M12 19.5s-7-4.4-7-9a3.9 3.9 0 0 1 7-2.4A3.9 3.9 0 0 1 19 10.5c0 4.6-7 9-7 9Z"/>',
 'Helpers & Utilities': '<path d="M14.5 6.5a4 4 0 0 0-5.6 5L4 16.5V20h3.5l5-4.9a4 4 0 0 0 5-5.6l-2.6 2.6-2.4-2.4 2.5-2.6Z"/>',
}

NAV = [
    ('Start', [('introduction', 'Introduction'), ('why', 'Why this system'),
               ('principles', 'Principles'), ('usage', 'Usage — CSS · SCSS · Tailwind'),
               ('components', 'Components explorer'), ('all', 'All pages')]),
    ('Getting started', [('install', 'Installation'), ('setup', 'Setup & theming')]),
    ('Foundation', [('f-logo', 'Logo'), ('f-color', 'Color'), ('f-type', 'Typography'),
                    ('f-space', 'Spacing & radius'), ('f-elevation', 'Elevation'),
                    ('f-pattern', 'Patterns'), ('breakpoints', 'Breakpoints'),
                    ('f-a11y', 'Accessibility')]),
    ('Elements', [('reboot', 'Reboot'), ('typography', 'Type roles'),
                  ('text-elements', 'Text elements'), ('images', 'Images & figures'),
                  ('tables', 'Tables'), ('quotes', 'Quotes'), ('code', 'Code & syntax'),
                  ('content', 'Long-form content')]),
    ('Icons', [('f-icons', 'Guidelines'), ('icon-set', 'Icon set')]),
    ('Shape & Cutout', [('f-shape', 'Shapes'), ('cutouts', 'Cutouts')]),
    ('Grid & Layout', [('containers', 'Containers'), ('grid', 'Grid'),
                       ('columns', 'Columns & gutters'), ('f-layout', 'Composition'),
                       ('z-index', 'Z-index'), ('layout-patterns', 'Patterns')]),
    ('Forms', [('forms', 'Overview'), ('form-control', 'Form control'), ('select', 'Select'),
               ('checks-radios', 'Checks & radios'), ('range', 'Range'),
               ('input-group', 'Input group'), ('floating-labels', 'Floating labels'),
               ('form-layout', 'Layout')]),
    ('Components', [('accordion', 'Accordion'), ('ads', 'Ads'), ('alerts', 'Alerts'), ('badge', 'Badge'),
                    ('breadcrumb', 'Breadcrumb'), ('buttons', 'Buttons'),
                    ('button-group', 'Button group'), ('card', 'Card'),
                    ('collection-cards', 'Collection cards'), ('carousel', 'Carousel'),
                    ('close-button', 'Close button'), ('collapse', 'Collapse'),
                    ('f-devices', 'Devices'), ('dropdowns', 'Dropdowns'),
                    ('f-frames', 'Frames'), ('list-group', 'List group'),
                    ('marquee', 'Marquee'), ('modal', 'Modal'), ('navbar', 'Navbar'),
                    ('navs-tabs', 'Navs & tabs'), ('offcanvas', 'Offcanvas'),
                    ('pagination', 'Pagination'), ('popovers', 'Popovers'),
                    ('progress', 'Progress'), ('scrollspy', 'Scrollspy'),
                    ('spinners', 'Spinners'), ('toasts', 'Toasts'), ('tooltips', 'Tooltips')]),
    ('Sections', [('page-header', 'Page header'), ('hero', 'Hero'), ('stats', 'Stats'),
                  ('cta', 'CTA'), ('footer', 'Footer')]),
    # There was a "Composites" group here holding syllabus, build log and
    # itinerary. It was a group named after how those three are BUILT rather
    # than what they are FOR, which put a course's curriculum three groups away
    # from the course collection that is the only thing that renders it. Each
    # now sits with its owning collection; the generic sequence they are all
    # variations of is the timeline, which is a component and lives with them.
    ('Collections', [('collections', 'The contract'), ('col-sections', 'Sections'),
                     ('timeline', 'Timeline'),
                     ('col-default', 'Default'), ('travel/index', 'Travel'),
                     ('travel/itinerary', 'Travel · itinerary'),
                     ('blog/index', 'Blog'), ('course/index', 'Course'),
                     ('course/curriculum', 'Course · curriculum'),
                     ('projects/index', 'Projects'),
                     ('projects/build-log', 'Projects · build log'),
                     ('webseries/index', 'Webseries'),
                     ('prompts/index', 'Prompts'), ('snippets/index', 'Snippets'),
                     ('products/index', 'Products'), ('docs/index', 'Docs template')]),
    ('Pages', [('pages/index', 'Pages'), ('pages/home', 'Homepage'),
              ('pages/about', 'About'), ('pages/contact', 'Contact'),
              ('pages/archive', 'Archive'), ('pages/now', 'Now'),
              ('resume/index', 'Résumé'), ('pages/legal', 'Terms & privacy'),
              ('pages/welcome', 'Welcome, subscriber')]),
    ('Animation & Motion', [('m-basics', 'Motion basics'), ('m-text-effects', 'Text effects'),
                ('m-annotations', 'Annotations'), ('m-micro', 'Micro-interactions'),
                ('m-presets', 'Section presets'), ('m-stings', 'Logo sting'),
                ('page-transitions', 'Page transitions')]),
    ('Broadcast · YouTube', [('yt-thumbs', 'Thumbnails'), ('yt-layouts', 'Thumb layouts'),
                             ('yt-categories', 'Categories'), ('yt-series', 'Series art'),
                             ('yt-livescenes', 'Live scenes'), ('yt-screens', 'Screens'),
                             ('yt-scenes', 'Scenes'), ('yt-live', 'Live'),
                             ('yt-end', 'End screens'), ('yt-subs', 'Subscribe'),
                             ('yt-engage', 'Engagement'), ('yt-brand', 'Branding'),
                             ('yt-backdrops', 'Backdrops')]),
    ('Broadcast · Social', [('ig-posts', 'Posts'), ('ig-carousel', 'Carousel'),
                            ('ig-story', 'Stories'), ('ig-grid', 'Grid'),
                            ('ig-follow', 'Follow'), ('ig-share', 'Share')]),
    ('Helpers & Utilities', [('u-background', 'Background'), ('u-borders', 'Borders'),
                   ('u-colors', 'Colors'), ('u-display', 'Display'), ('u-flex', 'Flex'),
                   ('u-float', 'Float'), ('u-interactions', 'Interactions'),
                   ('u-overflow', 'Overflow'), ('u-position', 'Position'),
                   ('u-shadows', 'Shadows'), ('u-sizing', 'Sizing'), ('u-spacing', 'Spacing'),
                   ('u-text', 'Text'), ('u-valign', 'Vertical align'),
                   ('u-visibility', 'Visibility')]),
]

ORDER = [(s, l, g) for g, items in NAV for s, l in items]

# Pages that ship but do not belong in the docs sidebar: they are the project's
# own pages, reached from the site bar, not steps in the reading order. They
# still need an eyebrow label and they are simply skipped by the pager.
OFF_NAV = {'showcase': 'Project', 'templates': 'Project', 'sponsor': 'Project'}

SPRITE = '''<svg class="icon-sprite" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg">
<symbol id="i-play" viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5-11-6.5Z"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h13M13 7l5 5-5 5"/></symbol>
<symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="6"/><path d="m15.5 15.5 4 4"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><rect x="3.5" y="5.5" width="17" height="13" rx="2"/><path d="m4 7 8 5.5L20 7"/></symbol>
<symbol id="i-camera" viewBox="0 0 24 24"><path d="M3 8.5A2.5 2.5 0 0 1 5.5 6h1.7l1.2-2h6.2l1.2 2h1.7A2.5 2.5 0 0 1 20 8.5v8A2.5 2.5 0 0 1 17.5 19h-11A2.5 2.5 0 0 1 4 16.5v-8Z"/><circle cx="12" cy="12.5" r="3.2"/></symbol>
<symbol id="i-code" viewBox="0 0 24 24"><path d="m8.5 8.5-4 3.7 4 3.8M15.5 8.5l4 3.7-4 3.8M13.5 5l-3 14"/></symbol>
<symbol id="i-book" viewBox="0 0 24 24"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4H11v16H5.5A1.5 1.5 0 0 1 4 18.5v-13ZM20 5.5A1.5 1.5 0 0 0 18.5 4H13v16h5.5a1.5 1.5 0 0 0 1.5-1.5v-13Z"/></symbol>
<symbol id="i-plane" viewBox="0 0 24 24"><path d="M20 5 4 11.5l5.5 2M20 5l-3.5 14-3-6.5M20 5 9.5 13.5v4.2l3-3.7"/></symbol>
<symbol id="i-pen" viewBox="0 0 24 24"><path d="M4 20l1-4L16.5 4.5a2.1 2.1 0 0 1 3 3L8 19l-4 1Z"/><path d="m13.5 7.5 3 3"/></symbol>
<symbol id="i-heart" viewBox="0 0 24 24"><path d="M12 19.5s-7-4.4-7-9a3.9 3.9 0 0 1 7-2.4A3.9 3.9 0 0 1 19 10.5c0 4.6-7 9-7 9Z"/></symbol>
<symbol id="i-chat" viewBox="0 0 24 24"><path d="M4.5 6.5A2 2 0 0 1 6.5 4.5h11a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2H10l-4 3.5v-3.5H6.5a2 2 0 0 1-2-2v-7Z"/></symbol>
<symbol id="i-share" viewBox="0 0 24 24"><circle cx="17.5" cy="6.5" r="2.5"/><circle cx="6.5" cy="12" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/><path d="m8.8 10.8 6.4-3.1M8.8 13.2l6.4 3.1"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="7.5"/><path d="M12 7.5V12l3 2"/></symbol>
<symbol id="i-grid" viewBox="0 0 24 24"><rect x="4" y="4" width="7" height="7" rx="2"/><rect x="13" y="4" width="7" height="7" rx="2"/><rect x="4" y="13" width="7" height="7" rx="2"/><rect x="13" y="13" width="7" height="7" rx="2"/></symbol>
<symbol id="i-layout" viewBox="0 0 24 24"><rect x="4" y="4.5" width="16" height="15" rx="2"/><path d="M4 9.5h16M10.5 9.5v10"/></symbol>
</svg>'''


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:48]


def keywords(body, lead):
    """Searchable extras: every class name named in a .spec strip, plus the lead."""
    specs = re.findall(r'<p class="spec">(.*?)</p>', body, re.S)
    specs += re.findall(r'<code class="t-code">(.*?)</code>', body, re.S)
    words = set()
    for sp in specs:
        for m in re.findall(r'\.[a-z][a-z0-9_-]*(?:__[a-z0-9-]+)?|kg-[a-z-]+|--[a-z-]+', sp):
            words.add(m)
    txt = html.unescape(re.sub(r'<[^>]+>', ' ', lead))
    # The prose in the spec strips is the most useful text on the page —
    # "iris open", "scanline sweep" — so it is searchable too.
    prose = ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', sp)) for sp in specs)
    prose = re.sub(r'\s+', ' ', prose).strip()[:600]
    return sorted(words)[:40], (re.sub(r'\s+', ' ', txt).strip()[:160] + ' ' + prose).strip()


def add_heading_ids(body):
    """Give ids to prose headings and collect the TOC. `t-h*` is the docs voice;
    `sec-head-row__title` is the landing voice — both are section headings a
    reader would want in the rail, so both are indexed."""
    toc, seen = [], set()

    def repl(m):
        tag, attrs, text = m.group(1), m.group(2), m.group(3)
        if 'data-no-toc' in attrs:   # a heading inside a card, not a section of the page
            return m.group(0)
        if 't-h' not in attrs and 'sec-head-row__title' not in attrs:
            return m.group(0)
        plain = html.unescape(re.sub(r'<[^>]+>', '', text)).strip()
        if not plain or len(plain) > 60:
            return m.group(0)
        idm = re.search(r'id="([^"]+)"', attrs)
        hid = idm.group(1) if idm else slugify(plain)
        base, n = hid, 2
        while hid in seen:
            hid, n = f'{base}-{n}', n + 1
        seen.add(hid)
        if not idm:
            attrs += f' id="{hid}"'
        toc.append((hid, plain))
        return f'<{tag}{attrs}>{text}</{tag}>'

    body = re.sub(r'<(h[23])([^>]*)>(.*?)</\1>', repl, body, flags=re.S)
    return body, toc


def strip_fragment_head(frag):
    """Remove the legacy section's own numbered heading; mine its intro as lead."""
    lead = ''
    frag = frag.lstrip()
    m = re.match(r'<(header|div) class="sec-head">(.*?)</\1>', frag, re.S)
    if m:
        pm = re.search(r'<p class="t-(?:subtle|lead)"[^>]*>(.*?)</p>', m.group(2), re.S)
        if pm:
            lead = re.sub(r'\s+', ' ', pm.group(1)).strip()
        frag = frag[m.end():]
    else:
        frag = re.sub(r'<span class="sec-num">.*?</span>\s*', '', frag, count=1)
        hm = re.match(r'\s*<h[23][^>]*>.*?</h[23]>', frag, re.S)
        if hm:
            frag = frag[hm.end():]
        pm = re.match(r'\s*<p class="t-(?:subtle|lead)"[^>]*>(.*?)</p>', frag, re.S)
        if pm:
            lead = re.sub(r'\s+', ' ', pm.group(1)).strip()
            frag = frag[pm.end():]
        frag = re.sub(r'^\s*</(?:div|header)>', '', frag, count=1)
    return frag.strip(), lead


def sidebar(current):
    """Pages only. This page's own headings live in the right rail now, so the
    left rail stays a stable map of the system rather than shifting per page."""
    out = []
    for group, items in NAV:
        active = any(sl == current for sl, _ in items)
        gic = GROUP_ICONS.get(group, '')
        gsvg = (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
                f'stroke-linecap="round" stroke-linejoin="round">{gic}</svg>') if gic else ''
        out.append(f'\t\t\t<details class="doc-group"{" open" if active else ""}>'
                   f'<summary><span class="doc-group__l">{gsvg}{group}</span></summary>')
        for slug, label in items:
            cur = ' aria-current="page"' if slug == current else ''
            out.append(f'\t\t\t<a href="/{slug}.html"{cur}>{label}</a>')
        out.append('\t\t\t</details>')
    return '\n'.join(out)


SPONSOR_CARD = '''\t\t\t<div class="doc-sponsor">
				<span class="doc-sponsor__eyebrow">Support</span>
				<p class="doc-sponsor__lead">Creator Design System is free, MIT, and built in the
				open. Sponsoring keeps the next release coming.</p>
				<a class="btn btn-primary btn-sm btn-pill doc-sponsor__cta"
				   href="https://github.com/sponsors/imswarnil" rel="noopener" target="_blank">
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"
					     stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
						<path d="M12 19.5s-7-4.4-7-9a3.9 3.9 0 0 1 7-2.4A3.9 3.9 0 0 1 19 10.5c0 4.6-7 9-7 9Z"/>
					</svg>Sponsor my project</a>
				<a class="doc-sponsor__alt" href="/sponsor.html">What sponsorship pays for →</a>
			</div>'''


def aside(toc, slug=None):
    """The right rail: this page's headings, then the sponsor card. The rail is
    rendered even with an empty TOC so the sponsor ask is on every page — bar
    the sponsor page, which is already the ask."""
    if toc:
        links = '\n'.join(f'\t\t\t\t\t<a href="#{hid}">{html.escape(htext)}</a>' for hid, htext in toc)
        nav = ('\t\t\t<nav class="doc-toc" aria-label="On this page">\n'
               '\t\t\t\t<span class="doc-toc__title">On this page</span>\n'
               f'\t\t\t\t<div class="doc-toc__links">\n{links}\n\t\t\t\t</div>\n'
               '\t\t\t</nav>')
    else:
        nav = ''
    card = '' if slug == 'sponsor' else SPONSOR_CARD
    return '\n'.join(p for p in (nav, card) if p)


def jsonld(current):
    """SiteNavigationElement for the site bar, and BreadcrumbList for where this
    page sits. Search engines read the nav the way a reader does — as a named
    list of destinations — only if you say so; the markup alone does not."""
    site = [('Docs', 'introduction'), ('Components', 'components'),
            ('Showcase', 'showcase'), ('Templates', 'templates'), ('Sponsor', 'sponsor')]
    nav = {'@context': 'https://schema.org', '@type': 'ItemList',
           'name': 'Creator Design System', 'itemListElement': [
               {'@type': 'SiteNavigationElement', 'position': i + 1,
                'name': label, 'url': f'./{slug}.html'}
               for i, (label, slug) in enumerate(site)]}

    if current == 'index':
        trail = {'@context': 'https://schema.org', '@type': 'BreadcrumbList',
                 'itemListElement': [{'@type': 'ListItem', 'position': 1,
                                      'name': 'Home', 'item': f'{SITE}/'}]}
        dump = lambda d: json.dumps(d, separators=(',', ':'), ensure_ascii=False)
        return (f'<script type="application/ld+json">{dump(nav)}</script>\n'
                f'<script type="application/ld+json">{dump(trail)}</script>')

    label, group = {s: (l, g) for s, l, g in ORDER}.get(
        current, (current, OFF_NAV.get(current, '')))
    crumbs = [('Docs', './introduction.html')]
    if group:
        crumbs.append((group, None))
    crumbs.append((label, f'./{current}.html'))
    trail = {'@context': 'https://schema.org', '@type': 'BreadcrumbList',
             'itemListElement': []}
    for i, (name, url) in enumerate(crumbs):
        item = {'@type': 'ListItem', 'position': i + 1, 'name': name}
        if url:
            item['item'] = url
        trail['itemListElement'].append(item)

    dump = lambda d: json.dumps(d, separators=(',', ':'), ensure_ascii=False)
    return (f'<script type="application/ld+json">{dump(nav)}</script>\n'
            f'<script type="application/ld+json">{dump(trail)}</script>')


def pager(current):
    idx = next((i for i, (s, _, _) in enumerate(ORDER) if s == current), None)
    if idx is None:
        return ''
    parts = []
    if idx > 0:
        s, l, _ = ORDER[idx - 1]
        parts.append(f'<a class="docs-pager__link" href="/{s}.html">'
                     f'<span class="docs-pager__dir">← Previous</span><span class="docs-pager__title">{l}</span></a>')
    else:
        parts.append('<span></span>')
    if idx < len(ORDER) - 1:
        s, l, _ = ORDER[idx + 1]
        parts.append(f'<a class="docs-pager__link docs-pager__link-next" href="/{s}.html">'
                     f'<span class="docs-pager__dir">Next →</span><span class="docs-pager__title">{l}</span></a>')
    else:
        parts.append('<span></span>')
    return '\n\t\t\t'.join(parts)



TEMPLATE = '''<!DOCTYPE html>
<html lang="en" data-theme="{theme}">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{page_title}</title>
<meta name="description" content="{meta_desc}" />
<link rel="canonical" href="{canonical}" />
<link rel="alternate" type="text/plain" href="{site}/llms.txt" title="Creator Design System for LLMs" />
<meta property="og:type" content="{og_type}" />
<meta property="og:site_name" content="Creator Design System" />
<meta property="og:title" content="{page_title}" />
<meta property="og:description" content="{meta_desc}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="{site}/og.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{page_title}" />
<meta name="twitter:description" content="{meta_desc}" />
<meta name="twitter:image" content="{site}/og.png" />
{jsonld}
<link rel="icon" href="/favicon.svg{v}" type="image/svg+xml" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/src/1-foundation/index.css{v}" />
<link rel="stylesheet" href="/src/2-elements/index.css{v}" />
<link rel="stylesheet" href="/src/3-components/index.css{v}" />
<link rel="stylesheet" href="/src/5-sections/index.css{v}" />
<link rel="stylesheet" href="/src/6-utilities/index.css{v}" />{broadcast_css}
<link rel="stylesheet" href="/preview.css{v}" />{collection_css}
<script src="/src/highlight.js{v}" defer></script>
<script src="/src/nav.js{v}" defer></script>
<script src="/src/ad.js{v}" defer></script>
<script src="/preview.js{v}" defer></script>{extra_style}
</head>
<body class="{body_class} has-side">
<a class="skip-link" href="#main">Skip to content</a>
{sprite}
<header class="cds-bar cds-bar-wide">
	<div class="cds-bar__in u-relative">
		<a class="cds-mark" href="/index.html"><span class="cds-mark__word">creat<i class="cds-mark__o" aria-hidden="true"></i><span class="u-sr-only">o</span>r</span><span class="cds-mark__sub">design system</span></a>
		<nav class="cds-bar__links" aria-label="Site">
			<a href="/introduction.html"><svg class="icon icon-sm" aria-hidden="true"><use href="#i-book"/></svg>Docs</a>
			<a href="/components.html"><svg class="icon icon-sm" aria-hidden="true"><use href="#i-grid"/></svg>Components</a>
			<a href="/showcase.html"><svg class="icon icon-sm" aria-hidden="true"><use href="#i-camera"/></svg>Showcase</a>
			<a href="/templates.html"><svg class="icon icon-sm" aria-hidden="true"><use href="#i-layout"/></svg>Templates</a>
			<a href="/sponsor.html"><svg class="icon icon-sm" aria-hidden="true"><use href="#i-heart"/></svg>Sponsor</a>
		</nav>
		<div class="cds-bar__end">
	<div class="doc-search">
		<svg class="icon" aria-hidden="true"><use href="#i-search"/></svg>
		<input id="docSearch" type="search" placeholder="Search…" aria-label="Search the design system"
		       autocomplete="off" role="combobox" aria-expanded="false" aria-controls="docResults" />
		<kbd class="kbd">/</kbd>
	</div>
	<div class="doc-results" id="docResults" role="listbox" hidden></div>
			<button class="doc-btn" id="themeToggle" type="button" aria-pressed="{dark}">
				<span class="dot dot-sm" aria-hidden="true"></span><span id="themeLabel">{theme_label}</span>
			</button>
			<button class="nav-burger nav-burger-aperture cds-bar__burger" type="button"
			        aria-expanded="false" aria-controls="cds-menu" data-dialog="cds-menu" data-menu-burger>
				<span class="nav-burger__box"><span class="nav-burger__bars"></span></span>
				<span class="u-sr-only">Menu</span>
			</button>
			<a class="cds-gh" href="https://github.com/imswarnil/Creator-Design-System" rel="noopener" target="_blank">
				<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7C6.73 19.91 6.14 18 6.14 18a2.7 2.7 0 0 0-1.13-1.49c-.92-.63.07-.62.07-.62a2.14 2.14 0 0 1 1.56 1.05 2.17 2.17 0 0 0 2.96.85 2.18 2.18 0 0 1 .65-1.37c-2.23-.25-4.57-1.11-4.57-4.95a3.88 3.88 0 0 1 1.03-2.69 3.6 3.6 0 0 1 .1-2.65s.84-.27 2.75 1.03a9.47 9.47 0 0 1 5 0c1.91-1.3 2.75-1.03 2.75-1.03a3.6 3.6 0 0 1 .1 2.65 3.87 3.87 0 0 1 1.03 2.69c0 3.85-2.34 4.7-4.57 4.95a2.43 2.43 0 0 1 .69 1.88v2.79c0 .27.18.58.69.48A10 10 0 0 0 12 2Z"/></svg><span>GitHub</span><span class="cds-gh__stars" data-gh-stars>★</span>
			</a>{guides_btn}
		</div>
	</div>
</header>
<dialog class="nav-sheet" id="cds-menu">
	<div class="nav-sheet__in">
		<span class="nav-sheet__scan" aria-hidden="true"></span>
		<div class="nav-sheet__head">
			<span class="cds-mark"><span class="cds-mark__word">creat<i class="cds-mark__o" aria-hidden="true"></i><span class="u-sr-only">o</span>r</span></span>
			<button class="btn-close" type="button" data-dialog-close aria-label="Close menu"></button>
		</div>
		<nav class="nav-sheet__links" aria-label="Site">
			<a class="nav-sheet__link" style="--i:0" href="/introduction.html"><svg class="icon" aria-hidden="true"><use href="#i-book"/></svg>Docs</a>
			<a class="nav-sheet__link" style="--i:1" href="/components.html"><svg class="icon" aria-hidden="true"><use href="#i-grid"/></svg>Components</a>
			<a class="nav-sheet__link" style="--i:2" href="/showcase.html"><svg class="icon" aria-hidden="true"><use href="#i-camera"/></svg>Showcase</a>
			<a class="nav-sheet__link" style="--i:3" href="/templates.html"><svg class="icon" aria-hidden="true"><use href="#i-layout"/></svg>Templates</a>
			<a class="nav-sheet__link" style="--i:4" href="/sponsor.html"><svg class="icon" aria-hidden="true"><use href="#i-heart"/></svg>Sponsor</a>
		</nav>
		<div class="nav-sheet__foot">
			<span class="t-slate-sm" style="color:var(--fg-faint)"><span class="dot dot-sm dot-live"></span> still rolling</span>
			<a class="btn btn-primary btn-sm btn-pill" href="https://github.com/imswarnil/Creator-Design-System" rel="noopener">GitHub</a>
		</div>
	</div>
</dialog>
<aside class="doc-side">
	<div class="doc-side__head">
		<span class="t-slate-sm" style="color:var(--fg-faint)">Contents</span>
		<button class="doc-btn doc-side__hide" type="button" data-side-toggle aria-label="Hide menu" title="Hide menu">«</button>
	</div>

	<nav class="doc-side__nav" aria-label="Creator Design System">
{nav}
	</nav>
</aside>
<div class="doc-scrim" aria-hidden="true"></div>
<button class="doc-btn doc-reopen" type="button" data-side-toggle aria-label="Show menu">☰</button>
<header class="doc-top">
	<button class="doc-btn" type="button" data-nav-toggle aria-label="Open navigation">☰ Contents</button>
	<span class="t-slate-sm" style="color:var(--fg-faint)">{title}</span>
</header>
<main id="main">
	<div class="container-wide section">
{head_html}

		<div class="doc-split">
			<div class="doc-split__main">
{body}
{pager_html}
			</div>
			<aside class="doc-rail">
				<div class="doc-rail__in">
{aside}
				</div>
			</aside>
		</div>

		<footer class="section-sm" style="padding-bottom:0">
			<hr class="rule" style="margin-bottom:var(--space-6)" />
			<div class="row-between">
				<p class="t-slate" style="display:flex;align-items:center;gap:8px">Creator Design System <span class="dot dot-sm"></span></p>
				<p class="t-slate-sm">Frame &amp; Signal · for creators building their site.</p>
			</div>
		</footer>
	</div>
</main>
<script>
(function () {{
	var root = document.documentElement, btn = document.getElementById('themeToggle'),
		label = document.getElementById('themeLabel');
	var sync = function () {{
		var d = root.getAttribute('data-theme') === 'dark';
		label.textContent = d ? 'Dark' : 'Light';
		btn.setAttribute('aria-pressed', String(d));
	}};
	sync();
	btn.addEventListener('click', function () {{
		var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
		root.setAttribute('data-theme', next);
		try {{ localStorage.setItem('cds-theme', next); }} catch (e) {{}}
		sync();
	}});
	try {{ var t = localStorage.getItem('cds-theme'); if (t) {{ root.setAttribute('data-theme', t); sync(); }} }} catch (e) {{}}

	var stars = document.querySelector('[data-gh-stars]');
	if (stars) {{
		fetch('https://api.github.com/repos/imswarnil/Creator-Design-System')
			.then(function (r) {{ return r.ok ? r.json() : null; }})
			.then(function (d) {{ if (d && typeof d.stargazers_count === 'number') stars.textContent = d.stargazers_count.toLocaleString(); }})
			.catch(function () {{}});
	}}
}})();
</script>
</body>
</html>
'''

GUIDES_BTN = '''
		<button class="doc-btn" id="guideToggle" type="button" aria-pressed="false" title="Overlay the export safe areas">
			<span id="guideLabel">Guides off</span>
		</button>'''


def render(slug, title, group, lead, body, opts, return_toc=False):
    if opts.get('intro'):
        body = opts['intro'] + body
    body, toc = add_heading_ids(body)
    broadcast = opts.get('broadcast', False)
    style_folder = opts.get('style', 'youtube' if broadcast and slug.startswith('yt') else
                            ('social' if broadcast else None))
    extra = ''
    if style_folder:
        css = FRAG / style_folder / '_style.css'
        if css.exists():
            out_css = OUT / 'broadcast-frag' / f'{style_folder}.css'
            out_css.parent.mkdir(parents=True, exist_ok=True)
            out_css.write_text(css.read_text())
            extra = f'\n<link rel="stylesheet" href="/broadcast-frag/{style_folder}.css{V}" />'
    lead_html = (f'\n\t\t\t<p class="t-lead" style="margin-top:var(--space-4);'
                 f'max-width:var(--measure-lead)">{lead}</p>') if lead else ''
    esc_title = html.escape(title)
    head_html = ('\t\t<header class="docs-head">\n'
                 f'\t\t\t<span class="t-slate" style="color:var(--fg-faint)">{group} · Creator Design System</span>\n'
                 f'\t\t\t<h1 class="t-display-2" style="margin-top:var(--space-3)">{esc_title}</h1>{lead_html}\n'
                 '\t\t</header>')
    pg = pager(slug)
    pager_html = ('\n\t\t\t\t<nav class="docs-pager" aria-label="Pages">\n'
                  f'\t\t\t\t\t{pg}\n\t\t\t\t</nav>') if pg else ''
    # The lead is the page's own sentence; it makes a better description than
    # anything generic, and it is already written.
    plain_lead = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', lead))).strip()
    meta_desc = html.escape(plain_lead[:155] if plain_lead else
                            f'{title} — Creator Design System, a token-first, '
                            'dependency-free CSS design system for creators.')

    out = TEMPLATE.format(
        page_title=esc_title if 'Creator Design System' in esc_title else esc_title + ' — Creator Design System',
        title=esc_title, head_html=head_html, body=body, og_type='article',
        meta_desc=meta_desc, canonical=f'{SITE}/{slug}.html', site=SITE,
        nav=sidebar(slug), pager_html=pager_html, aside=aside(toc, slug),
        jsonld=jsonld(slug), sprite=SPRITE, v=V,
        theme='light',
        theme_label='Light',
        dark='false',
        guides_btn='',
        broadcast_css=f'\n<link rel="stylesheet" href="/src/4-broadcast/index.css{V}" />' if broadcast else '',
        extra_style=extra, body_class='loop-demos' if opts.get('loop') else '',
        collection_css=(
            f'\n<link rel="stylesheet" href="/collection/collection.css{V}" />'
            f'\n<link rel="stylesheet" href="/collection/travel/travel.css{V}" />'
            f'\n<link rel="stylesheet" href="/collection/course/course.css{V}" />'
            f'\n<link rel="stylesheet" href="/collection/_pages/pages.css{V}" />'
            f'\n<link rel="stylesheet" href="/collection/projects/projects.css{V}" />'
            f'\n<link rel="stylesheet" href="/collection/guides/guides.css{V}" />'
            if slug.startswith('col-') or slug == 'collections'
            or slug.split('/')[0] in ('travel', 'course', 'blog', 'resume', 'webseries',
                                       'pages', 'projects', 'newsletter', 'videos',
                                       'guides', 'prompts', 'snippets', 'products',
                                       'docs') else ''))
    return (out, toc) if return_toc else out


def render_home(title, head, body):
    """The homepage runs the docs shell — left sidebar, right rail — with the
    hero standing in for the docs-head. A front door that is already the map:
    the system's contents are visible before you have clicked anything, and the
    page's own sections feed 'On this page' exactly as a docs page does."""
    body, toc = add_heading_ids(body)
    return TEMPLATE.format(
        page_title=html.escape(title), title='Home', head_html=head, body=body,
        og_type='website',
        meta_desc='Frame &amp; Signal — a token-first, dependency-free CSS design '
                  'system for creators building their site. Videos, courses, build '
                  'logs and trips, decided once in tokens.',
        canonical=f'{SITE}/', site=SITE,
        nav=sidebar('index'), pager_html='', aside=aside(toc, 'index'),
        jsonld=jsonld('index'), sprite=SPRITE, v=V,
        theme='light', theme_label='Light', dark='false', guides_btn='',
        broadcast_css='', extra_style='', body_class='lp', collection_css='')


def mirror_assets():
    """Copy src/ and icons/ into docs/ so every path is relative to the web
    root — the same whether you serve docs/ locally or deploy it to Pages.
    All three are gitignored; this runs on every build and in CI."""
    import shutil
    for name in ('src', 'icons', 'collection'):
        srcdir, dstdir = REPO / name, OUT / name
        if srcdir.exists():
            shutil.rmtree(dstdir, ignore_errors=True)
            shutil.copytree(srcdir, dstdir)

    # The pages link index.css with ?v=…, but an @import inside it names its
    # children with no query at all — so the browser happily serves a month-old
    # 33-navbar.css behind a freshly-versioned index. Stamp the version onto
    # every @import in the COPY (never the source) so a rebuild is actually
    # visible without a hard reload.
    for css in (OUT / 'src').rglob('*.css'):
        text = css.read_text()
        stamped = re.sub(r"@import url\('(\./[^']+\.css)'\)",
                         lambda m: f"@import url('{m.group(1)}{V}')", text)
        if stamped != text:
            css.write_text(stamped)
    dist = REPO / 'dist'
    if dist.exists() and any(dist.iterdir()):
        shutil.rmtree(OUT / 'dist', ignore_errors=True)
        shutil.copytree(dist, OUT / 'dist')


# Old flat slug -> where it moved to, when a page's URL changes shape (e.g. moving
# a collection's docs into its own folder). Kept as a generated redirect rather than
# a hand-written stub so the target can never drift from the real new path.
REDIRECTS = {
    'col-travel': 'travel/index',
    'col-course': 'course/index',
    'col-blog': 'blog/index',
    'col-pages': 'pages/index',
    'pages/components': 'pages/index',
    # The dissolved "Composites" group.
    'syllabus': 'course/curriculum',
    'build-log': 'projects/build-log',
    'itinerary': 'travel/itinerary',
}


def write_redirects():
    for old, new in REDIRECTS.items():
        url = f'/{new}.html'
        out = OUT / f'{old}.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            '<!doctype html>\n<html lang="en"><head><meta charset="utf-8" />\n'
            f'<title>Moved — Creator Design System</title>\n'
            f'<meta http-equiv="refresh" content="0; url={url}" />\n'
            f'<link rel="canonical" href="{SITE}{url}" />\n'
            '</head><body>\n'
            f'<p>This page moved to <a href="{url}">{url}</a>.</p>\n'
            '</body></html>\n')


# Short, memorable entry points into the one Usage page's per-flavour
# sections — real URLs for "how do I use this with X", rather than asking
# everyone to land on /usage.html and scroll. The content lives in one place
# (content_usage.py) so plain-CSS, Tailwind and SCSS never drift into three
# competing explanations of the same token contract.
FLAVOUR_ROUTES = {
    'css': ('usage', 'getting-it', 'Using it with plain CSS'),
    'tailwind': ('usage', 'tailwind', 'Using it with Tailwind'),
    'scss': ('usage', 'scss', 'Using it with SCSS'),
}


def write_flavour_routes():
    for slug, (target, anchor, label) in FLAVOUR_ROUTES.items():
        url = f'/{target}.html#{anchor}'
        out = OUT / f'{slug}.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            '<!doctype html>\n<html lang="en"><head><meta charset="utf-8" />\n'
            f'<title>{label} — Creator Design System</title>\n'
            f'<meta http-equiv="refresh" content="0; url={url}" />\n'
            f'<link rel="canonical" href="{SITE}{url}" />\n'
            '</head><body>\n'
            f'<p><a href="{url}">{label}</a> — part of the '
            f'<a href="/{target}.html">Usage</a> guide.</p>\n'
            '</body></html>\n')


def write_seo(slugs):
    """sitemap.xml, robots.txt and CNAME. The sitemap is generated from what was
    actually built, so a page cannot be listed and missing, or built and unlisted.
    CNAME is what tells GitHub Pages the site answers on its own domain."""
    urls = ['<url><loc>%s/</loc><priority>1.0</priority></url>' % SITE]
    for slug in sorted(slugs):
        # The landing page is "/", not "/index.html" — listing both splits the
        # signal between two URLs for one page.
        if slug == 'index':
            continue
        pri = '0.8' if slug in ('introduction', 'components', 'install', 'usage') else '0.5'
        urls.append(f'<url><loc>{SITE}/{slug}.html</loc><priority>{pri}</priority></url>')

    (OUT / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + '\n'.join(urls) + '\n</urlset>\n')

    (OUT / 'robots.txt').write_text(
        f'User-agent: *\nAllow: /\n\n'
        f'# Written for machines: the system in one read.\n'
        f'# {SITE}/llms.txt\n'
        f'# {SITE}/llms-full.txt\n\n'
        f'Sitemap: {SITE}/sitemap.xml\n')

    (OUT / 'CNAME').write_text(SITE.split('//')[1] + '\n')

    # Pages would otherwise run the output through Jekyll, which silently drops
    # every directory beginning with an underscore — including _build.
    (OUT / '.nojekyll').write_text('')


def write_llms(index):
    """llms.txt and llms-full.txt — the site, written for a machine.

    An LLM asked to "build a page with this design system" will otherwise guess
    class names, and guessed class names are the single worst failure mode for
    a CSS library: the markup looks right and renders as unstyled HTML. So the
    full file is generated from the stylesheets themselves — every custom
    property and every class the system actually defines. It cannot drift,
    because nothing here is typed by hand.

    llms.txt follows the convention: a title, a one-line summary, then link
    lists. llms-full.txt is the whole surface in one read.
    """
    src = REPO / 'src'

    def tokens_of(path):
        text = (src / path).read_text()
        # Only the :root declarations — the tier a consumer is meant to touch.
        out = []
        for block in re.findall(r':root\s*\{(.*?)\n\}', text, re.S):
            for name, value in re.findall(r'(--[\w-]+):\s*([^;]+);', block):
                out.append((name, ' '.join(value.split())))
        return out

    def classes_of(path):
        text = (src / path).read_text()
        text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
        names = re.findall(r'(?:^|[,\s>+~])\.([a-z][\w-]*)', text, re.M)
        seen, out = set(), []
        for n in names:
            if n not in seen:
                seen.add(n); out.append(n)
        return out

    LAYERS = [
        ('1-foundation', 'Tokens. Colour, type, space, elevation, motion, layout, '
                         'patterns, logo, icons, shape, cutouts, frames, a11y.'),
        ('2-elements', 'Single ideas: text roles, badge, table, indicator, syntax.'),
        ('3-components', 'Things with parts and states: buttons through navbar.'),
        ('4-broadcast', 'Export canvases for YouTube and Instagram. Not for websites.'),
        ('5-sections', 'Full-width bands: page header, hero, stats, CTA, footer.'),
        ('6-utilities', 'u- prefixed, single-purpose classes.'),
    ]

    # ── llms.txt ────────────────────────────────────────────────────────────
    L = ['# Creator Design System', '',
         '> Frame & Signal — a token-first, dependency-free CSS design system for '
         'creators. Plain CSS custom properties and classes: no framework, no '
         'runtime, no build step required to use it. Almost monochrome, so that one '
         'colour can carry meaning.', '',
         'Install: link '
         '`https://cdn.jsdelivr.net/gh/imswarnil/Creator-Design-System@main/dist/creator.min.css`, '
         'or copy dist/creator.css out of the repository. The npm package '
         '(`creator-design-system`) is not published yet; the import paths below are the ones '
         'its exports map declares.', '',
         'Customise by overriding tokens AFTER the import — never by editing source. '
         'Dark mode rides `data-theme="light|dark"` on `<html>`. State lives in ARIA '
         '(`[aria-current]`, `[aria-expanded]`), not in `.active` classes.', '',
         '## Complete reference', '',
         f'- [Full specification]({SITE}/llms-full.txt): every token, every class, '
         'and the rules that govern them. Read this before generating markup.', '',
         '## Docs', '']

    by_group = {}
    for row in index:
        by_group.setdefault(row['g'] or 'Project', []).append(row)
    for group, _ in NAV:
        for row in by_group.get(group, []):
            desc = (row['d'] or '').strip()[:120]
            L.append(f"- [{row['t']}]({SITE}/{row['s']}.html): {group} — {desc}")
    L.append('')
    (OUT / 'llms.txt').write_text('\n'.join(L))

    # ── llms-full.txt ───────────────────────────────────────────────────────
    F = ['# Creator Design System — full specification', '',
         'Generated from the stylesheets. Every name below is real; anything not '
         'listed does not exist. Do not invent class names.', '',
         '## How to use it', '',
         '1. Link `dist/creator.css` (or import a layer).',
         '2. Write plain HTML with the classes below.',
         '3. Change appearance by overriding custom properties in `:root` AFTER the '
         'import. Never edit the source files.',
         '4. Mark state with ARIA — `aria-current="page"`, `aria-expanded="true"` — '
         'and let the CSS react to it.', '',
         '## Rules', '',
         '- Active state is a dot or a 2px accent rule, never a filled pill.',
         '- One accent colour, rationed. The palette is closed on purpose.',
         '- Prefer the platform: <details>, <dialog>, the Popover API, native inputs.',
         '- Every animation is off under prefers-reduced-motion, and the finished '
         'state is the resting state.',
         '- Components read semantic tokens (--fg-muted, --accent), not primitives '
         '(--ink-500). Override the semantic tier to rebrand.', '']

    F += ['## Tokens', '',
          'Primitives are the ladders; semantic tokens name a job. Override the '
          'semantic ones.', '']
    for path in ['1-foundation/01-color.css', '1-foundation/02-typography.css',
                 '1-foundation/03-space.css', '1-foundation/04-elevation.css',
                 '1-foundation/05-motion.css', '1-foundation/06-layout.css']:
        toks = tokens_of(path)
        if not toks:
            continue
        F.append(f'### {path}')
        F.append('')
        F += [f'{n}: {v}' for n, v in toks]
        F.append('')

    F += ['## Classes', '']
    for layer, note in LAYERS:
        files = sorted((src / layer).glob('*.css'))
        F.append(f'### {layer}')
        F.append('')
        F.append(note)
        F.append('')
        for f in files:
            if f.name == 'index.css':
                continue
            names = classes_of(f'{layer}/{f.name}')
            if names:
                F.append(f'{f.name}: ' + ' '.join('.' + n for n in names))
        F.append('')

    F += ['## Optional JavaScript', '',
          'src/highlight.js — colours code blocks. CreatorHighlight.scan(root), '
          'CreatorHighlight.highlight(code, lang). Languages: html, css, js, json, bash.',
          'src/nav.js — sets data-scrolled, data-dir and data-open for the navbar. '
          'Everything visible stays in CSS. Both are additive; without them nothing '
          'breaks.', '']
    (OUT / 'llms-full.txt').write_text('\n'.join(F))


def main():
    mirror_assets()
    # The "All pages" index is generated from NAV itself.
    PAGES['all'] = ('All pages',
                    'Every page in the Creator Design System, in one list.',
                    content_all.build(NAV, FRAGPAGES))
    slug_meta = {s: (l, g) for s, l, g in ORDER}
    built = set()
    index = []

    for slug, (title, lead, body) in PAGES.items():
        label, group = slug_meta.get(slug, (title, OFF_NAV.get(slug, '')))
        page, toc = render(slug, title, group, lead, body, {}, return_toc=True)
        out = OUT / f'{slug}.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page)
        kw, ld = keywords(body, lead)
        index.append({'s': slug, 't': label or title, 'g': group,
                      'h': [h for _, h in toc], 'k': kw, 'd': ld})
        built.add(slug)

    for slug, (folder, name, opts) in FRAGPAGES.items():
        label, group = slug_meta.get(slug, (slug, ''))
        frag = (FRAG / folder / f'{name}.html').read_text()
        body, lead = strip_fragment_head(frag)
        page, toc = render(slug, label, group, lead, body, opts, return_toc=True)
        out = OUT / f'{slug}.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page)
        kw, ld = keywords(body, lead)
        index.append({'s': slug, 't': label, 'g': group,
                      'h': [h for _, h in toc], 'k': kw, 'd': ld})
        built.add(slug)

    for slug, (title, builder) in content_site.LANDING.items():
        head, body = builder()
        out = OUT / f'{slug}.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_home(title, head, body))

    write_redirects()
    write_flavour_routes()
    write_seo(built)
    write_llms(index)

    index.sort(key=lambda r: [g for g, _ in NAV].index(r['g']) if r['g'] in [g for g, _ in NAV] else 99)
    (OUT / 'search-index.json').write_text(json.dumps(index, separators=(',', ':')))
    missing = {s for s, _, _ in ORDER} - built
    print(f'built {len(built)} pages' + (f' · MISSING: {sorted(missing)}' if missing else ''))


if __name__ == '__main__':
    main()
