"""The /components explorer — every component in one grid, preview or code."""
from common import ct

PAGES = {}

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
        ('episode-panel', 'Episode panel', 'list beside a player'),
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
        f'<a class="card card-compact" href="./{slug}.html">'
        f'<div class="card__body"><h3 class="card__title">{name}</h3>'
        f'<p class="card__excerpt">{desc}</p></div></a>'
        for slug, name, desc in items)
    body += (f'<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">{group}</h2>'
             f'<div class="deck-c deck-c-sm">{cards}</div>')

PAGES['components'] = ('Components',
    'Every component in one place — open any of them and switch between the preview '
    'and its markup.',
    body)
