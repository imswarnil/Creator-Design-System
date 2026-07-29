"""The /components explorer — every component in one grid, preview or code."""
from common import ct

PAGES = {}

ICONS = {
 'text-elements': '<path d="M4 7h16M4 12h10M4 17h13"/>',
 'tables': '<rect x="3.5" y="4.5" width="17" height="15" rx="2"/><path d="M3.5 9.5h17M9 9.5v10"/>',
 'quotes': '<path d="M9 7c-2.2 0-4 1.8-4 4v6h6v-6H7c0-1.1.9-2 2-2V7ZM19 7c-2.2 0-4 1.8-4 4v6h6v-6h-4c0-1.1.9-2 2-2V7Z"/>',
 'code': '<path d="m8.5 8.5-4 3.7 4 3.8M15.5 8.5l4 3.7-4 3.8M13.5 5l-3 14"/>',
 'badge': '<path d="M12 3.5 20 8v8l-8 4.5L4 16V8l8-4.5Z"/>',
 'form-control': '<rect x="3.5" y="7.5" width="17" height="9" rx="2"/><path d="M7 12h2"/>',
 'select': '<rect x="3.5" y="7.5" width="17" height="9" rx="2"/><path d="m14 11 2 2 2-2"/>',
 'checks-radios': '<rect x="3.5" y="4.5" width="7" height="7" rx="2"/><path d="m5.2 8 1.4 1.4L9.2 6.5"/><circle cx="7" cy="17" r="3.5"/><circle cx="7" cy="17" r="1.4" fill="currentColor" stroke="none"/><path d="M14 8h6M14 17h6"/>',
 'range': '<path d="M4 12h16"/><circle cx="10" cy="12" r="3.2"/>',
 'input-group': '<rect x="3.5" y="8" width="10" height="8" rx="2"/><rect x="14.5" y="8" width="6" height="8" rx="2"/>',
 'floating-labels': '<rect x="3.5" y="8.5" width="17" height="9" rx="2"/><path d="M7 6.5h5"/>',
 'form-layout': '<rect x="3.5" y="4.5" width="7.5" height="6" rx="1.5"/><rect x="13" y="4.5" width="7.5" height="6" rx="1.5"/><rect x="3.5" y="13.5" width="17" height="6" rx="1.5"/>',
 'buttons': '<rect x="3" y="8" width="18" height="8" rx="4"/>',
 'button-group': '<rect x="3" y="9" width="18" height="6" rx="3"/><path d="M9 9v6M15 9v6"/>',
 'card': '<rect x="4" y="3.5" width="16" height="17" rx="2"/><path d="M4 11h16M7.5 15h6"/>',
 'collection-cards': '<rect x="3" y="5" width="8" height="14" rx="2"/><rect x="13" y="5" width="8" height="6" rx="2"/><rect x="13" y="13" width="8" height="6" rx="2"/>',
 'accordion': '<rect x="3.5" y="4" width="17" height="4.5" rx="1.5"/><rect x="3.5" y="10" width="17" height="4.5" rx="1.5"/><path d="m16 6 1.4 1.4L18.8 6"/>',
 'collapse': '<path d="M4 6h16M4 18h16M9 11l3 3 3-3"/>',
 'dropdowns': '<path d="M6 8h12"/><rect x="6" y="11" width="12" height="9" rx="2"/>',
 'modal': '<rect x="2.5" y="5" width="19" height="14" rx="2" opacity=".35"/><rect x="6.5" y="8" width="11" height="8" rx="2"/>',
 'offcanvas': '<rect x="3.5" y="4.5" width="17" height="15" rx="2"/><path d="M14 4.5v15" /><path d="M17 10v4" opacity=".5"/>',
 'popovers': '<rect x="4" y="5" width="16" height="10" rx="2"/><path d="m9 15 2 3 2-3"/>',
 'tooltips': '<rect x="4" y="6" width="16" height="7" rx="2"/><path d="m10 13 2 2.5 2-2.5"/><path d="M12 18v2" opacity=".4"/>',
 'toasts': '<rect x="3.5" y="12" width="17" height="7" rx="2"/><path d="M7 15.5h6"/>',
 'alerts': '<path d="M12 4 2.5 20h19L12 4Z"/><path d="M12 10v4M12 17h.01"/>',
 'progress': '<rect x="3" y="10" width="18" height="4" rx="2"/><path d="M3 12h9" stroke-width="3"/>',
 'spinners': '<path d="M12 4.5a7.5 7.5 0 1 0 7.5 7.5"/>',
 'list-group': '<rect x="3.5" y="4.5" width="17" height="15" rx="2"/><path d="M3.5 9.5h17M3.5 14.5h17"/>',
 'carousel': '<rect x="7" y="6" width="10" height="12" rx="2"/><path d="M3.5 9v6M20.5 9v6"/>',
 'marquee': '<path d="M2 12h20M6 8l-4 4 4 4M18 8l4 4-4 4"/>',
 'navbar': '<rect x="2.5" y="6" width="19" height="6" rx="3"/><path d="M7 9h.01M11 9h4"/>',
 'navs-tabs': '<path d="M3 15h18"/><path d="M3 15V9h6v6"/>',
 'breadcrumb': '<path d="M3 12h4l2-3 3 6 2-3h7"/>',
 'pagination': '<circle cx="5" cy="12" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="19" cy="12" r="2"/>',
 'close-button': '<circle cx="12" cy="12" r="8.5"/><path d="m9 9 6 6M15 9l-6 6"/>',
 'content': '<path d="M5 4h14M5 9h14M5 14h10M5 19h7"/>',
 'syllabus': '<path d="M4 5.5A1.5 1.5 0 0 1 5.5 4H11v16H5.5A1.5 1.5 0 0 1 4 18.5v-13ZM20 5.5A1.5 1.5 0 0 0 18.5 4H13v16h5.5a1.5 1.5 0 0 0 1.5-1.5v-13Z"/>',
 'build-log': '<circle cx="6" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><path d="M6 8v8M11 6h9M11 18h9"/>',
 'itinerary': '<path d="M20 5 4 11.5l5.5 2M20 5l-3.5 14-3-6.5M20 5 9.5 13.5"/>',
 'page-header': '<path d="M4 5h9M4 9h16"/><rect x="4" y="13" width="16" height="6" rx="1.5" opacity=".4"/>',
 'hero': '<rect x="3.5" y="4.5" width="17" height="15" rx="2"/><path d="M7 10h6M7 14h4"/><circle cx="17" cy="12" r="2.5"/>',
 'stats': '<path d="M5 19V9M12 19V5M19 19v-7"/>',
 'cta': '<rect x="3" y="7" width="18" height="10" rx="2"/><path d="M8 12h5"/><circle cx="16.5" cy="12" r="1.5" fill="currentColor" stroke="none"/>',
 'footer': '<rect x="3.5" y="4.5" width="17" height="15" rx="2" opacity=".35"/><path d="M3.5 15h17M7 18h4"/>',
}

def _ico(slug):
    p = ICONS.get(slug, '<circle cx="12" cy="12" r="7.5"/>')
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
            f'stroke-linecap="round" stroke-linejoin="round" class="cds-card__icon">{p}</svg>')



GROUPS = [
    ('Elements', [
        ('text-elements', 'Text elements', 'blockquote · pullquote · figure · note · drop cap'),
        ('tables', 'Tables', 'table · compact · definition list · rule list · steps'),
        ('quotes', 'Quotes', 'inline · pullquote · section break'),
        ('code', 'Code & syntax', 'codebox · line numbers · copy · light twin'),
        ('badge', 'Badge', 'tones · live · chip · timecode · kbd'),
    ]),
    ('Forms', [
        ('form-control', 'Form control', 'input · textarea · states · search'),
        ('select', 'Select', 'native, dressed'),
        ('checks-radios', 'Checks & radios', 'check · radio · switch'),
        ('range', 'Range', 'accent-filled track'),
        ('input-group', 'Input group', 'prefix · suffix · button'),
        ('floating-labels', 'Floating labels', 'rest → slate caption'),
        ('form-layout', 'Form layout', 'rows · fieldsets · actions'),
    ]),
    ('Components', [
        ('buttons', 'Buttons', '6 intents · 3 sizes · icons · states'),
        ('button-group', 'Button group', 'segmented, aria-pressed'),
        ('card', 'Card', 'media · body · meta · 6 layouts'),
        ('collection-cards', 'Collection cards', 'one card per collection type'),
        ('accordion', 'Accordion', 'native details · exclusive groups'),
        ('collapse', 'Collapse', 'one panel'),
        ('dropdowns', 'Dropdowns', 'menu · heads · dividers'),
        ('modal', 'Modal', 'real dialog · focus trap'),
        ('offcanvas', 'Offcanvas', 'edge drawer'),
        ('popovers', 'Popovers', 'Popover API · anchored'),
        ('tooltips', 'Tooltips', 'CSS only, from data-tip'),
        ('toasts', 'Toasts', 'transient confirmations'),
        ('alerts', 'Alerts', '5 tones · dismissable'),
        ('progress', 'Progress', 'determinate · thin · labelled'),
        ('spinners', 'Spinners', 'spinner · scan · skeletons'),
        ('list-group', 'List group', 'rows in one surface'),
        ('carousel', 'Carousel', 'scroll-snap, no trap'),
        ('marquee', 'Marquee', 'looping strip, hover-pause'),
        ('navbar', 'Navbar', 'alignment · menus · sheet · contexts'),
        ('navs-tabs', 'Navs & tabs', 'peer views'),
        ('breadcrumb', 'Breadcrumb', 'the trail back'),
        ('pagination', 'Pagination', 'pages · pager'),
        ('close-button', 'Close button', 'one dismiss affordance'),
        ('content', 'Long-form content', 'headings … editor cards'),
    ]),
    ('Composites', [
        ('syllabus', 'Syllabus', 'course curriculum'),
        ('build-log', 'Build log', 'project timeline'),
        ('itinerary', 'Itinerary', 'the trip, day by day'),
    ]),
    ('Sections', [
        ('page-header', 'Page header', 'collection openings'),
        ('hero', 'Hero', 'statement · split · band'),
        ('stats', 'Stats', 'the number band'),
        ('cta', 'CTA', 'the one ask'),
        ('footer', 'Footer', 'end credits'),
    ]),
]

body = (
    '<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
    'Every component in the system. Open one and each demo has a '
    '<b>Preview / Code</b> toggle — flip to Code to read the markup and copy it '
    'straight out. Nothing here needs a build step: the markup plus the '
    'stylesheet is the whole runtime.</p>'
    '<div class="alert alert-info u-mb-8"><p class="alert__title">Tip</p>'
    'Press <kbd class="kbd">/</kbd> anywhere to search, or use the '
    '<b>Code</b> toggle on any demo to copy its markup.</div>')

for group, items in GROUPS:
    cards = ''.join(
        f'<a class="card card-compact cds-card" href="/{slug}.html">'
        f'<div class="card__body"><span class="cds-card__ico">{_ico(slug)}</span>'
        f'<h3 class="card__title">{name}</h3>'
        f'<p class="card__excerpt">{desc}</p></div></a>'
        for slug, name, desc in items)
    body += (f'<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">{group}</h2>'
             f'<div class="deck-c deck-c-sm">{cards}</div>')

PAGES['components'] = ('Components',
    'Every component in one place — open any of them and switch between the preview '
    'and its markup.',
    body)
