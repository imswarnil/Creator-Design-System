#!/usr/bin/env python3
"""The course collection — /course, and the lesson player.

The third collection, and the one that tested whether the vocabulary could
carry a route whose body is a video rather than prose. It could not, quite:
five sections were missing, and they are now in ../collection.css because a
podcast season and a video series want every one of them. What is left here is
genuinely course-shaped — the syllabus scene, the difficulty meter, the
knowledge check and the certificate.

The five routes, mapped:

    index    /course                       every course
    group    /course/layout                a track — an unordered set of courses
    place    /course/topic/grid            a topic — what is taught about one thing
    series   /course/css-from-scratch      THE COURSE. It has a first, a last and
                                           a progress through it, which is the
                                           definition of a series and the reason
                                           it gets a spine rather than a grid.
    post     /course/css-from-scratch/grid the lesson player

A course being the *series* route is the whole argument of the collection. A
track is a group: it has no first lesson and no progress. Getting those two the
wrong way round is what produces a course page with a grid on it.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import icon, ph, page, sec, hero, meta_strip   # noqa: E402

NAME = 'Courses'


def ic(n, cls='icon'):
    """Course reaches for creator and media icons before travel's."""
    return icon(n, cls, group='creator')


# ── The data ────────────────────────────────────────────────────────────────

TRACKS = [('layout', 'Layout & CSS', 'course', 3), ('motion', 'Motion', 'play', 1),
          ('brand', 'Brand & identity', 'viewfinder', 1),
          ('publish', 'Publishing', 'slate', 1)]

# slug, name, track, note, tags, lessons, length, level (1–3), price
COURSES = [
    ('css-from-scratch', 'CSS From Scratch', 'layout',
     'Tokens, layout and type — the whole system, built in front of you.',
     'beginner free', 15, '2h 06m', 1, 'Free'),
    ('grid-and-flex', 'Grid & Flexbox, properly', 'layout',
     'Every layout you actually ship, and why the other twelve properties exist.',
     'intermediate', 28, '4h 05m', 2, '$49'),
    ('type-for-screens', 'Type For Screens', 'layout',
     'A scale, a measure and a rhythm you can defend in a design review.',
     'intermediate', 19, '2h 40m', 2, '$39'),
    ('motion-that-lasts', 'Motion That Lasts', 'motion',
     'Under 200ms, one property at a time, and nothing unreachable without it.',
     'intermediate free', 24, '3h 10m', 2, 'Free'),
    ('one-colour', 'Brand In One Colour', 'brand',
     'An almost-monochrome system, so a single hue can carry meaning.',
     'advanced', 16, '2h 15m', 3, '$39'),
    ('ship-the-site', 'Ship The Site', 'publish',
     'From a folder of CSS to a domain, a build and a changelog nobody dreads.',
     'beginner', 31, '4h 45m', 1, '$49'),
]

# slug, name, the course it sits in, tags, lessons about it
TOPICS = [('tokens', 'Design tokens', 'css-from-scratch', 'beginner', 12),
          ('grid', 'Grid', 'grid-and-flex', 'intermediate', 9),
          ('a11y', 'Accessibility', 'css-from-scratch', 'beginner', 8),
          ('scale', 'Type scale', 'type-for-screens', 'intermediate', 7),
          ('easing', 'Easing', 'motion-that-lasts', 'intermediate', 6),
          ('deploy', 'Deploying', 'ship-the-site', 'beginner', 6),
          ('contrast', 'Contrast', 'one-colour', 'advanced', 5)]

# slug, name, level (0 = not a level), count. The glyph beside a level facet is
# the same three bars the cards carry, so the filter and the thing it filters
# are recognisably the same fact — an icon here would only be decoration.
FACETS = [('beginner', 'Beginner', 1, 2), ('intermediate', 'Intermediate', 2, 3),
          ('advanced', 'Advanced', 3, 1)]

# Price is its own cut, not a fourth level — "free" is not a difficulty.
PRICE_FACETS = [('free', 'Free', 'play', 2), ('paid', 'Paid', 'take', 4)]

LEVELS = {1: 'Beginner', 2: 'Intermediate', 3: 'Advanced'}

# The curriculum of the featured course. state: done · now · free · preview
# (locked, but this one can be watched anyway) · locked · '' (available)
MODULES = [
    ('Foundations', [
        ('What a design system actually is', '6:12', 'done'),
        ('Two tiers of tokens', '11:40', 'done'),
        ('One colour, rationed', '9:05', 'done'),
        ('The type scale', '12:20', 'done'),
    ]),
    ('Layout', [
        ('The container and the gutter', '8:44', 'done'),
        ('Grid, in four rules', '14:02', 'now'),
        ('Flex, and when not to reach for it', '10:18', 'free'),
        ('The rail, the stack and the cluster', '9:36', ''),
    ]),
    ('Type & rhythm', [
        ('Measure and leading', '7:50', ''),
        ('Headings that scale with the page', '8:12', 'preview'),
        ('Long-form content', '11:26', 'locked'),
    ]),
    ('Shipping', [
        ('The build step you may not need', '6:40', 'preview'),
        ('Writing a changelog', '5:55', 'locked'),
        ('What to do after this', '4:10', 'locked'),
    ]),
]

FLAT = [(m, t, ln, st) for m, ls in MODULES for t, ln, st in ls]
DONE = sum(1 for _, _, _, st in FLAT if st == 'done')
HERE_I = [i for i, (_, _, _, st) in enumerate(FLAT) if st == 'now'][0]
PCT = round(DONE / len(FLAT) * 100)
N = len(FLAT)


def hms(seconds):
    return f'{seconds // 3600}h {seconds % 3600 // 60:02d}m'


def secs(text):
    """'14:02' → 842; '2h 06m' → 7560. Both spellings appear in the data and
    both have to add up, or the page starts contradicting itself."""
    if 'h' in text:
        h, m = text.replace('m', '').split('h')
        return int(h) * 3600 + int(m) * 60
    m, s = text.split(':')
    return int(m) * 60 + int(s)


# The featured course's own numbers are the curriculum's, counted — never a
# figure typed twice. Three of the four places they appear are prose.
LEN = hms(sum(secs(ln) for _, _, ln, _ in FLAT))
COURSES[0] = COURSES[0][:5] + (N, LEN) + COURSES[0][7:]

TOTAL_LESSONS = sum(c[5] for c in COURSES)
TOTAL_LEN = hms(sum(secs(c[6]) for c in COURSES))

OUTCOMES = [
    'Read a design system as two tiers of tokens rather than a pile of classes',
    'Build a layout with four grid properties instead of a framework',
    'Set a type scale you can defend in a review',
    'Ration one accent colour so it still means something on page forty',
    'Ship motion that is honest under prefers-reduced-motion',
    'Write CSS a second person can delete without asking you',
]

TRANSCRIPT = [
    ('0:00', 'A grid is not a layout system you switch on. It is four properties, '
             'and everything else in the specification is a shorthand for them.'),
    ('0:24', 'The first is grid-template-columns. Nearly every layout you ship is '
             'this one property with minmax in it.'),
    ('0:51', 'The second is gap — and gap is the reason margins mostly leave your '
             'stylesheet when grid arrives.'),
    ('1:19', 'Third: the implicit grid. Rows you never declared. This is where '
             'most of the confusion lives, so we are going to sit here a while.'),
    ('2:04', 'And fourth, alignment. Two axes, four keywords, and the fact that '
             'align-items defaults to stretch — which is what makes cards match.'),
    ('2:47', 'Everything after this is naming. Areas, lines, spans: useful, and '
             'none of it necessary to lay out a page today.'),
]

FILES = [('starter-files', 'zip', 'Starter files', 'The stylesheet at the state this lesson begins', '18 KB'),
         ('grid-cheatsheet', 'pdf', 'Grid cheatsheet', 'One page, the four properties', '96 KB'),
         ('lesson-06', 'css', 'The finished stylesheet', 'What we end on, commented', '4 KB')]

KEYS = [('Next lesson', ['N']), ('Previous lesson', ['P']), ('Mark complete', ['M'])]

TRACK_NAMES = dict((s, n) for s, n, _, _ in TRACKS)

FAQ = [('Do I need to know CSS already?',
        'For this one, no. It starts at what a token is. The layout and motion '
        'courses assume you have written a stylesheet before.'),
       ('How long do I have access?',
        'Once you have a course, you have it. There is no renewal, because a '
        'renewal would make the course a subscription wearing a price tag.'),
       ('Is there a certificate?',
        'Yes, at the end of each course. It is a page with your name on it — '
        'useful for a manager, and honest about being exactly that.'),
       ('What if it is not for me?',
        'Thirty days, no questions, no form asking why. Email and it is done.')]

# ── The art ─────────────────────────────────────────────────────────────────
# A ring that draws to three quarters, a column of lessons ticking over, and a
# caret. The argument of the page in one picture: a course is a finite thing
# you get to the end of. All decoration, so all aria-hidden.

SCENE = '''
  <svg class="col-hero__art" viewBox="0 0 1200 520" preserveAspectRatio="xMaxYMid slice"
       aria-hidden="true" focusable="false">
    <defs>
      <radialGradient id="crs-sky" cx="78%" cy="24%" r="88%">
        <stop offset="0%" stop-color="#1d2231"/>
        <stop offset="60%" stop-color="#12151f"/>
        <stop offset="100%" stop-color="#0b0d13"/>
      </radialGradient>
      <!-- The copy has to win. Everything left of two thirds fades into the
           sky, so the art never has to be dodged by a line of text. -->
      <linearGradient id="crs-veil" x1="0" x2="1">
        <stop offset="0%" stop-color="#12151f" stop-opacity="1"/>
        <stop offset="52%" stop-color="#12151f" stop-opacity="0.92"/>
        <stop offset="100%" stop-color="#12151f" stop-opacity="0"/>
      </linearGradient>
    </defs>
    <rect width="1200" height="520" fill="url(#crs-sky)"/>

    <g transform="translate(918 96)">
      <g class="crs-row"><rect width="150" height="10" rx="5" fill="#fff" opacity="0.3"/>
        <circle cx="-24" cy="5" r="7" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="2"/></g>
      <g class="crs-row" transform="translate(0 34)"><rect width="118" height="10" rx="5" fill="#fff" opacity="0.3"/>
        <circle cx="-24" cy="5" r="7" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="2"/></g>
      <g class="crs-row" transform="translate(0 68)"><rect width="164" height="10" rx="5" fill="#fff" opacity="0.3"/>
        <circle cx="-24" cy="5" r="7" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="2"/></g>
      <g class="crs-row" transform="translate(0 102)"><rect width="132" height="10" rx="5" fill="#fff" opacity="0.3"/>
        <circle cx="-24" cy="5" r="7" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="2"/></g>
      <g class="crs-row" transform="translate(0 136)"><rect width="146" height="10" rx="5" fill="#fff" opacity="0.3"/>
        <circle cx="-24" cy="5" r="7" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="2"/></g>
      <g class="crs-row" transform="translate(0 170)"><rect width="104" height="10" rx="5" fill="#fff" opacity="0.3"/>
        <circle cx="-24" cy="5" r="7" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="2"/></g>
      <!-- The tick lands on row two, which is the row the column is on. -->
      <g class="crs-check" transform="translate(-24 39)">
        <path d="M-4 0l3 3 5-6" fill="none" stroke="var(--accent)" stroke-width="2.5"
              stroke-linecap="round" stroke-linejoin="round"/>
      </g>
    </g>

    <g transform="translate(1010 392)" fill="none" stroke-linecap="round">
      <circle r="72" stroke="rgb(255 255 255 / 0.10)" stroke-width="8"/>
      <circle class="crs-ring" r="72" stroke="var(--accent)" stroke-width="8"
              transform="rotate(-90)"/>
      <g class="crs-cap" stroke="rgb(255 255 255 / 0.5)" stroke-width="3">
        <path d="M-24 -4 0 -15l24 11-24 11z"/>
        <path d="M16 2v13"/>
      </g>
    </g>

    <!-- Sitting at the end of the last row, where the writing stopped. -->
    <rect class="crs-caret" x="1032" y="260" width="3" height="22" fill="var(--accent)"/>
    <rect width="1200" height="520" fill="url(#crs-veil)"/>
  </svg>
'''


# ── Sections ────────────────────────────────────────────────────────────────

def bars(n):
    """The three-bar glyph on its own, for anywhere the word is already there."""
    return (f'<span class="crs-level" data-level="{n}"><span class="crs-level__bars">'
            + '<i></i>' * 3 + '</span></span>')


def level_chip(n):
    return (f'<span class="crs-level" data-level="{n}"><span class="crs-level__bars">'
            + '<i></i>' * 3 + f'</span>{LEVELS[n]}</span>')


def tracks_block():
    return '<div class="col-groups">' + ''.join(
        f'<button class="col-group" type="button" data-group="{s}" aria-pressed="false">'
        f'<span class="col-group__ico">{ic(i)}</span>'
        f'<span><span class="col-group__name">{n}</span>'
        f'<span class="col-group__n">{c} course{"s" if c != 1 else ""}</span></span></button>'
        for s, n, i, c in TRACKS) + '</div>'


def courses_block(only=None, limit=None):
    rows = [c for c in COURSES if only is None or c[2] == only][:limit]
    return '<div class="col-places">' + ''.join(
        f'<a class="col-place" href="./course.html" data-place="{s}" data-of="{tr}" '
        f'data-tags="{tags}">'
        f'<span class="col-place__media">{ph(s)}'
        f'<span class="col-place__tag">{price}</span></span>'
        f'<span class="col-place__body"><span class="col-place__name">{n}</span>'
        f'<span class="col-place__note">{note}</span></span>'
        f'<span class="col-place__foot"><span>{lessons} lessons · {length}</span>'
        f'{level_chip(lvl)}</span></a>'
        for s, n, tr, note, tags, lessons, length, lvl, price in rows) + (
        '<p class="col-empty" data-empty-for="[data-place]" hidden>'
        'No course matches. Try clearing a filter.</p></div>')


def topics_block():
    return '<div class="col-spots">' + ''.join(
        f'<a class="col-spot" href="./topic.html" data-spot="{s}" data-of="{of}" '
        f'data-tags="{tags}">{n}<span class="col-spot__n">{c}</span></a>'
        for s, n, of, tags, c in TOPICS) + (
        '<p class="col-empty" data-empty-for="[data-spot]" hidden>Nothing here.</p></div>')


def facets_block():
    return f'''
    <aside class="col-layout__side col-rail col-rail-sticky">
      <div class="col-facets">
        <div class="col-facets__group">
          <span class="col-facets__title">Filtering</span>
          <p class="t-small u-fg-subtle" data-filter-state>Everything</p>
          <button class="btn btn-quiet btn-sm" type="button" data-filter-reset hidden>
            Clear filters</button>
        </div>
        <div class="col-facets__group">
          <span class="col-facets__title">Level</span>
          {''.join(f'<label class="col-facet"><input type="checkbox" data-facet="{s}" />'
                   f'{bars(lvl)}'
                   f'<span>{n}</span><span class="col-facet__n">{c}</span></label>'
                   for s, n, lvl, c in FACETS)}
        </div>
        <div class="col-facets__group">
          <span class="col-facets__title">Price</span>
          {''.join(f'<label class="col-facet"><input type="checkbox" data-facet="{s}" />'
                   f'{ic(icn)}<span>{n}</span><span class="col-facet__n">{c}</span></label>'
                   for s, n, icn, c in PRICE_FACETS)}
        </div>
      </div>
      {offer_widget(compact=True)}
    </aside>'''


def lessons_block(limit=None, free_only=False):
    """Post rows, where a post is a lesson. The index lists the free ones,
    because a free lesson is the only page on the site that can argue for the
    course better than the course page can."""
    rows = [(m, t, ln, st) for m, t, ln, st in FLAT
            if not free_only or st in ('free', 'done', 'now')][:limit]
    return ('<div class="col-posts">' + ''.join(
        f'<a class="col-post-row" href="./lesson.html" data-post data-of="css-from-scratch" '
        f'data-region="layout" data-tags="beginner free">'
        f'<span class="col-post-row__thumb">{ph(t)}</span>'
        f'<span class="col-post-row__body"><span class="col-post-row__title">{t}</span>'
        f'<span class="col-post-row__note">{mod} · CSS From Scratch</span></span>'
        f'<span class="col-post-row__meta"><span>{ln}</span>'
        f'<span>{({"free": "Free", "locked": "Locked", "preview": "Preview"}).get(st, "")}</span>'
        f'</span></a>' for mod, t, ln, st in rows) +
        '<p class="col-empty" data-empty-for="[data-post]" hidden>'
        'No lesson matches. Try clearing a filter.</p></div>')


def featured_card():
    s, n, tr, note, tags, lessons, length, lvl, price = COURSES[0]
    return f'''
    <a class="col-series" href="./course.html">
      <span class="col-series__media">{ph(s, True)}</span>
      <span class="col-series__body">
        <span class="col-hero__eyebrow" style="color:var(--fg-faint)">{ic('course')}The course</span>
        <span class="col-series__title">{n}</span>
        <span class="t-small u-fg-subtle">{note} A course is the collection's
          <b>series</b> route: it has a first lesson, a last one, and a progress
          through it. A track has none of those, which is why a track is a group.</span>
        <span class="col-series__stats">
          <span>{ic('course')}{lessons} lessons</span>
          <span>{ic('take')}{length}</span>
          <span>{level_chip(lvl)}</span>
        </span>
        <span class="col-series__stats" style="display:block">
          <div class="progress-labelled">
            <div class="progress__label"><span>Your progress</span><span>{PCT}%</span></div>
            <div class="progress"><div class="progress__bar" style="--value:{PCT}%"></div></div>
          </div>
        </span>
      </span>
    </a>'''


def resume_strip():
    mod, title, length, _ = FLAT[HERE_I]
    return f'''
    <a class="col-resume" href="./lesson.html">
      <span class="col-resume__thumb">{ph(title)}</span>
      <span class="col-resume__body">
        <span class="col-resume__label">{ic('play')}Continue · CSS From Scratch</span>
        <span class="col-resume__title">{title}</span>
        <span class="t-small u-fg-subtle">{mod} · lesson {HERE_I + 1} of {N} ·
          {DONE} watched</span>
      </span>
      <span class="btn btn-primary btn-pill">Resume</span>
    </a>'''


def outcomes_block(items=None):
    return '<div class="col-checks">' + ''.join(
        f'<span class="col-check"><span class="col-check__tick">{icon("check", group="ui")}</span>'
        f'<span>{o}</span></span>' for o in (items or OUTCOMES)) + '</div>'


TESTIMONIALS = [
    ('Priya Nair', 'Frontend engineer', 'The grid lesson alone was worth the price of the '
     'whole track. I stopped Googling minmax() the same week.'),
    ('Marcus Webb', 'Design lead', 'First course that explained why a token exists, not '
     'just how to use one. My team quotes the "two tiers" lesson constantly.'),
    ('Yuki Tanaka', 'Indie hacker', 'Shipped my whole site in a weekend using nothing but '
     'what this course covers. No framework, no regrets.'),
]


def testimonials_block():
    """Not a new component — .surface for the card and .col-author (blog's
    byline) for the name and role, the same pairing a post already ends on."""
    cards = ''.join(
        f'<div class="surface" style="padding:var(--space-6);display:grid;gap:var(--space-5)">'
        f'<p class="t-lead" style="font-size:var(--text-base);margin:0">&ldquo;{quote}&rdquo;</p>'
        f'<div class="col-author"><span class="col-author__face">{ph(name)}</span>'
        f'<span><span class="col-author__name">{name}</span>'
        f'<span class="col-author__who">{role}</span></span></div></div>'
        for name, role, quote in TESTIMONIALS)
    return f'<div class="grid-3">{cards}</div>'


def curriculum(playlist=False, open_module=1):
    """The syllabus. The same component whether it is the middle of a course
    page or the list beside a player — only the scroll changes."""
    mods = ''
    n = 0
    for mi, (mod, lessons) in enumerate(MODULES):
        rows = ''
        for title, length, st in lessons:
            n += 1
            attrs = ''
            if st == 'done':
                attrs += ' data-done'
            if st == 'now':
                attrs += ' aria-current="true"'
            if st == 'locked':
                attrs += ' data-locked'
            tail = ''
            if st == 'free':
                tail = '<span class="badge badge-success">Free</span>'
            elif st == 'preview':
                tail = '<span class="badge">Preview</span>'
            elif st == 'locked':
                tail = f'<span class="col-lock">{ic("slate")}</span>'
            rows += (f'<li><a class="lesson-row" href="./lesson.html"{attrs}>'
                     f'<span class="lesson-row__tick"></span>'
                     f'<span class="lesson-row__title">{title}</span>{tail}'
                     f'<span class="lesson-row__len">{length}</span></a></li>')
        total = len(lessons)
        done = sum(1 for _, _, s in lessons if s == 'done')
        mods += (f'<details class="curriculum__module"{" open" if mi == open_module else ""}>'
                 f'<summary><span class="curriculum__no">{mi + 1:02d}</span>'
                 f'<span class="curriculum__module-title">{mod}</span>'
                 f'<span class="curriculum__count" data-module-count>{done}/{total}</span>'
                 f'</summary>'
                 f'<ol class="curriculum__lessons">{rows}</ol></details>')

    if playlist:
        return f'''
      <section class="curriculum col-playlist">
        <header class="curriculum__head">
          <span class="curriculum__title">CSS From Scratch</span>
          <span class="curriculum__meta" data-progress-count="{{done}} of {{all}}">
            {DONE} of {N}</span>
          <div class="progress" role="progressbar" aria-label="Course progress"
               aria-valuenow="{PCT}" aria-valuemin="0" aria-valuemax="100">
            <div class="progress__bar" data-progress style="--value:{PCT}%"></div>
          </div>
        </header>
        <div class="col-playlist__scroll">{mods}</div>
        <div class="col-playlist__foot">
          <span data-progress-count="{{pct}}% complete">{PCT}% complete</span>
          <span>{LEN} total</span>
        </div>
      </section>'''

    return f'''
      <section class="curriculum">
        <header class="curriculum__head">
          <span class="curriculum__title">The curriculum</span>
          <span class="curriculum__meta">{len(MODULES)} modules · {N} lessons · {LEN}</span>
          <div class="progress-labelled">
            <div class="progress__label"><span>Your progress</span><span>{DONE} of {N}</span></div>
            <div class="progress"><div class="progress__bar" style="--value:{PCT}%"></div></div>
          </div>
        </header>
        {mods}
      </section>'''


def offer_widget(compact=False):
    extras = [('course', f'{N} lessons, {LEN}'), ('slate', 'Starter files for every lesson'),
              ('take', 'Certificate at the end'), ('trip', 'Yours once you have it')]
    if compact:
        return f'''<div class="col-widget col-widget-accent">
      <span class="col-widget__title">The first course</span>
      <p class="t-small">CSS From Scratch is free, in full. It is the argument for
        the other five, and an argument is cheaper to make than to describe.</p>
      <a class="btn btn-primary btn-sm" href="./course.html">Start it</a>
    </div>'''
    return f'''<div class="col-widget col-widget-accent">
      <span class="col-widget__title">Enrol</span>
      <div class="col-offer">
        <div class="col-offer__price">
          <span class="col-offer__now">Free</span>
          <span class="col-offer__was">$49</span>
        </div>
        <div class="col-offer__list">
          {''.join(f'<span>{ic(i)}<span>{t}</span></span>' for i, t in extras)}
        </div>
        <a class="btn btn-primary" href="./lesson.html">Start lesson one</a>
        <p class="t-small" style="opacity:0.75">Thirty days, no questions. The
          refund form does not ask why.</p>
      </div>
    </div>'''


def instructor_widget():
    return f'''<div class="col-widget">
      <span class="col-widget__title">Taught by</span>
      <div class="col-author">
        <span class="col-author__face">{ph('craft')}</span>
        <span><span class="col-author__name">Swarnil Singhai</span>
          <span class="col-author__who">Wrote the system these courses are about.</span></span>
      </div>
      <div class="col-widget__foot">6 courses · 133 lessons</div>
    </div>'''


def keys_widget():
    return ('<div class="col-widget"><span class="col-widget__title">Shortcuts</span>'
            '<div class="col-keys">' + ''.join(
                f'<span class="col-key"><span>{what}</span><span class="col-key__combo">'
                + ''.join(f'<kbd class="kbd">{k}</kbd>' for k in keys)
                + '</span></span>' for what, keys in KEYS) +
            '</div><div class="col-widget__foot">They do nothing while you are typing</div></div>')


def upnext_widget():
    return ('<div class="col-widget"><span class="col-widget__title">Up next</span>'
            '<div class="col-mini">' + ''.join(
                f'<a class="col-mini__item" href="./lesson.html">'
                f'<span class="col-mini__n">{HERE_I + i + 2:02d}</span>'
                f'<span><span class="col-mini__title">{t}</span>'
                f'<span class="col-mini__meta">{mod} · {ln}</span></span></a>'
                for i, (mod, t, ln, _) in enumerate(FLAT[HERE_I + 1:HERE_I + 5]))
            + '</div></div>')


def files_block():
    return '<div class="col-files">' + ''.join(
        f'<a class="col-file" href="#i" download><span class="col-file__ext">{ext}</span>'
        f'<span><span class="col-file__name">{name}</span>'
        f'<span class="col-file__note">{note}</span></span>'
        f'<span class="col-file__size">{size}</span></a>'
        for _, ext, name, note, size in FILES) + '</div>'


def faq_block():
    return '<div class="acc">' + ''.join(
        f'<details class="collapse"{" open" if i == 0 else ""}>'
        f'<summary>{q}</summary><div class="collapse__body">'
        f'<p class="t-subtle">{a}</p></div></details>'
        for i, (q, a) in enumerate(FAQ)) + '</div>'


CRUMBS = ('<nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">'
          '<a href="./index.html">Courses</a> <span>/</span> <span>{here}</span></nav>')


# ── Routes ──────────────────────────────────────────────────────────────────

def route_index():
    body = f'''
  <div class="container">
    <section class="hero hero-split hero-sm pattern pattern-crosshatch pattern-lg fade-corners"
             style="padding-block:var(--space-10) var(--space-8);border-radius:var(--radius-sheet);
                    max-width:calc(var(--w-site) - 4rem);margin-inline:auto">
      <div>
        <span class="hero__eyebrow">{ic('course')}The course collection</span>
        <h1 class="hero__title">Learn the system, <em>in order</em>.</h1>
        <p class="hero__lead">Six courses on the craft of building and shipping a site on
          your own — tokens, layout, type, motion, brand and the deploy. The first one is
          free in full, because that is a better argument than this paragraph.</p>
        <div class="hero__actions">
          <div class="input-group" style="max-width:26rem">
            <input class="input" type="search" placeholder="Search {TOTAL_LESSONS} lessons"
                   aria-label="Search {TOTAL_LESSONS} lessons" />
            <button class="btn btn-primary" type="button">Search</button>
          </div>
        </div>
        {meta_strip([('6', 'courses'), (str(TOTAL_LESSONS), 'lessons'),
                     ('19h', 'of video'), ('4', 'tracks')],
                    paper=True, border=False, inline=True)}
      </div>
      <div class="hero-split__stage">
        {featured_card()}
      </div>
    </section>
  </div>

  <div data-collection>
  <section class="container section-sm">
    {sec('Tracks', 'The widest cut. A track is a group — an unordered set of courses '
         'that share a subject. Press one and everything below narrows to it.')}
    {tracks_block()}
  </section>

  <section class="container section-sm">
    <div class="col-layout">
      {facets_block()}
      <div>
        {sec('Every course', 'Six of them. The chip on each picture is the price; the '
               'three bars are the level, which is comparable at a glance in a way that '
               'the word "intermediate" is not.')}
        {courses_block()}

        <div class="u-mt-10">
          {sec('Topics', 'The narrowest cut: one thing, taught across whichever courses '
               'cover it.')}
          {topics_block()}
        </div>

        <div class="u-mt-10">
          {sec('Free lessons', 'Watchable without an account. A free lesson argues for the '
               'course better than the course page can.')}
          {lessons_block(limit=6)}
        </div>
      </div>
    </div>
  </section>
  </div>

  <section class="container section-sm">
    {sec('Every course includes', 'The same four things, so there is nothing to compare '
         'between them except the subject.')}
    {outcomes_block(['Lifetime access — no renewal, because a renewal makes it a subscription',
                     'Starter files at the state each lesson begins',
                     'A full transcript, searchable, with timestamps',
                     'A certificate at the end, honest about being a page with your name on it',
                     'Thirty-day refund, and the form does not ask why',
                     'Every course works on a phone, offline transcripts included'])}
  </section>

  <section class="container section-sm">
    {sec('What students say', 'Three people who took the free one first.')}
    {testimonials_block()}
  </section>

  <section class="container section-sm">
    <div class="grid-rail grid-rail-wide">
      <div>
        {sec('Questions')}
        {faq_block()}
      </div>
      <aside class="col-rail">
        {instructor_widget()}
        {offer_widget(compact=True)}
      </aside>
    </div>
  </section>'''
    return page(HERE, 'index.html', 'Courses — Swarnil',
                'Six courses on tokens, layout, type, motion, brand and shipping.',
                body, NAME, own_css='course.css', current='course')


def route_track():
    inside = [c for c in COURSES if c[2] == 'layout']
    body = hero('Layout &amp; CSS',
                'A track is an unordered set of courses that share a subject. Three of '
                'them here, in no particular order — because a track has no first '
                'course and no progress through it. That is the whole difference '
                'between a track and a course.',
                'Track', [(str(len(inside)), 'courses'),
                          (str(sum(c[5] for c in inside)), 'lessons'),
                          (hms(sum(secs(c[6]) for c in inside)), 'of video')],
                eyebrow_icon='course')
    body += f'''
  <div data-collection>
  <section class="container section-sm">
    {CRUMBS.format(here='Layout &amp; CSS')}
    <div class="col-layout">
      {facets_block()}
      <div>
        {sec('Courses in this track')}
        {courses_block(only='layout')}
        <div class="u-mt-10">{sec('Topics it covers')}{topics_block()}</div>
        <div class="u-mt-10">{sec('Lessons')}{lessons_block(limit=5)}</div>
      </div>
    </div>
  </section>
  </div>'''
    return page(HERE, 'track.html', 'Layout & CSS — Courses',
                'A track: three courses that share a subject.',
                body, NAME, own_css='course.css', current='course')


def route_topic():
    body = hero('Grid',
                'A topic is one thing, taught wherever it comes up. Nine lessons across '
                'two courses touch this one — which is exactly the sort of thing a '
                'curriculum page cannot tell you and a topic page can.',
                'Topic · Layout &amp; CSS',
                [('9', 'lessons'), ('2', 'courses'), ('1h 12m', 'of video')],
                eyebrow_icon='course')
    body += f'''
  <section class="container section-sm">
    {CRUMBS.format(here='Grid')}
    {sec('Courses that cover it')}
    <div class="u-mb-10">{courses_block(only='layout', limit=2)}</div>
    {sec('What you will be able to do', 'Six promises. A promise reads as a promise in '
         'a list and as marketing in a paragraph.')}
    <div class="u-mb-10">{outcomes_block(OUTCOMES[:4])}</div>
    {sec('Lessons on this topic')}
    {lessons_block(limit=5)}
  </section>'''
    return page(HERE, 'topic.html', 'Grid — Courses', 'One topic, across the courses.',
                body, NAME, own_css='course.css', current='course')


def route_course():
    body = hero('CSS From Scratch',
                'Tokens, layout and type — the whole system, built in front of you. '
                'Fifteen lessons, two hours, and a stylesheet at the end that you '
                'could hand to somebody else.',
                'Course · Layout &amp; CSS',
                [(str(N), 'lessons'), (LEN, 'of video'), (str(len(MODULES)), 'modules'),
                 ('Free', 'in full')],
                art=SCENE, eyebrow_icon='course')

    body += f'''
  <section class="container section-sm">
    {CRUMBS.format(here='CSS From Scratch')}
    <div class="grid-rail grid-rail-wide">
      <div>
        {sec('What you will be able to do', 'Six of them, and the course is judged '
             'against these rather than against its running time.')}
        <div class="u-mb-10">{outcomes_block()}</div>

        {sec('The curriculum', 'Four modules with a first and a last. This is the series '
             'route, so it gets a spine — the order is the information.')}
        <div class="u-mb-10">{curriculum()}</div>

        {sec('When you finish')}
        <div class="crs-cert pattern pattern-grid pattern-lg pattern-faint u-mb-10">
          <span class="crs-cert__seal">{icon('check', group='ui')}</span>
          <span class="crs-cert__name">CSS From Scratch</span>
          <span class="crs-cert__rule"></span>
          <p class="t-subtle" style="max-width:26rem">A page with your name on it and the
            date you finished. Useful for a manager, and honest about being exactly that.</p>
          <span class="crs-cert__meta">{N} lessons · {LEN} · issued on completion</span>
        </div>

        {sec('Questions')}
        {faq_block()}
      </div>

      <aside class="col-rail col-rail-sticky">
        {offer_widget()}
        <div class="col-widget">
          <span class="col-widget__title">This course</span>
          <div class="col-offer__list">
            <span>{bars(1)}<span>{LEVELS[1]} — no CSS assumed</span></span>
            <span>{ic('course')}<span>{N} lessons · {LEN}</span></span>
            <span>{ic('slate')}<span>Last updated July 2026</span></span>
          </div>
          <div class="col-widget__foot">Part of the Layout &amp; CSS track</div>
        </div>
        {instructor_widget()}
        <div class="col-widget">
          <span class="col-widget__title">Files</span>
          {files_block()}
        </div>
      </aside>
    </div>

    <a class="col-next u-mt-10" href="./lesson.html">
      <span class="col-next__label">Start · Lesson 01</span>
      <span class="col-order__title">{FLAT[0][1]}</span>
      <span class="t-small u-fg-subtle">Six minutes, and nothing to install first.</span>
    </a>
  </section>'''
    return page(HERE, 'course.html', 'CSS From Scratch — Courses',
                'Tokens, layout and type — the whole system, built in front of you.',
                body, NAME, own_css='course.css', current='course')


def route_lesson():
    mod, title, length, _ = FLAT[HERE_I]
    prev_t = FLAT[HERE_I - 1][1]
    next_t = FLAT[HERE_I + 1][1]

    tabs = [('overview', 'Overview'), ('transcript', 'Transcript'),
            ('resources', 'Resources'), ('notes', 'Notes')]

    body = f'''
  <div data-player>
  <section class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./index.html">Courses</a> <span>/</span>
      <a href="./track.html">Layout &amp; CSS</a> <span>/</span>
      <a href="./course.html">CSS From Scratch</a> <span>/</span>
      <span>{mod}</span>
    </nav>

    <!-- Full width: the video is the page's whole first act, not half a row
         shared with the playlist — the playlist is navigation, and navigation
         moves to the rail below rather than competing with the player. -->
    <div class="player">
      {ph(title, True)}
      <button class="play" type="button">
        <span class="play__disc"></span><span class="u-sr-only">Play the lesson</span>
      </button>
      <div class="player__bar">
        <span class="player__time">4:18</span>
        <span class="player__rail"><span class="player__played" style="--value:31%"></span></span>
        <span class="player__time">{length}</span>
      </div>
    </div>

    <div class="col-stagebar">
      <a class="btn btn-secondary btn-sm" href="./lesson.html" data-step="prev">
        ← Previous</a>
      <div class="col-stagebar__where">
        <span class="col-stagebar__pos">
          <span>Lesson {HERE_I + 1} of {N}</span>
          <span>{mod}</span>
          <span>{length}</span>
        </span>
        <h1 class="t-h3" style="margin:0">{title}</h1>
      </div>
      <span class="cluster" style="gap:var(--space-2)">
        <button class="btn btn-quiet btn-sm" type="button" data-done-toggle
                aria-pressed="false">Mark complete</button>
        <a class="btn btn-primary btn-sm" href="./lesson.html" data-step="next">
          Next →</a>
      </span>
    </div>

    <div class="grid-rail-left u-mt-8">
      <aside class="col-rail col-rail-sticky">
        {curriculum(playlist=True)}
        {keys_widget()}
        {upnext_widget()}
        {instructor_widget()}
      </aside>

      <div data-tabs>
        <div class="tabs" role="tablist" aria-label="About this lesson">
          {''.join(f'<button class="tab" type="button" role="tab" id="t-{s}" '
                   f'aria-controls="p-{s}" aria-selected="{str(i == 0).lower()}">{n}</button>'
                   for i, (s, n) in enumerate(tabs))}
        </div>

        <div class="col-panel" id="p-overview" role="tabpanel" aria-labelledby="t-overview">
          <span class="col-panel__label">Overview</span>
          <div class="content">
            <p>A grid is not a layout system you switch on. It is four properties,
              and everything else in the specification is a shorthand for one of
              them. This lesson is those four, in the order you will reach for them.</p>
            <h2>The four</h2>
            <p><code>grid-template-columns</code> with <code>minmax()</code> in it is
              most of the layouts you will ever ship. <code>gap</code> is why margins
              mostly leave your stylesheet once grid arrives. The implicit grid is
              where the confusion lives. Alignment is two axes and four keywords, and
              the fact that <code>align-items</code> defaults to <code>stretch</code>
              is what makes a row of cards match without you asking.</p>
            <blockquote>
              <p>Naming areas is a readability decision, not a layout one. You can
                build every page on this site without ever writing one.</p>
            </blockquote>
          </div>
          <div class="u-mt-8">
            {sec('In this lesson')}
            {outcomes_block(['Lay out a responsive grid with one property',
                             'Say what the implicit grid is doing and why',
                             'Choose between gap and margin without guessing',
                             'Match a row of cards without setting a height'])}
          </div>
          <div class="u-mt-8">
            {sec('Knowledge check', 'One question. It is not marked and it is not stored — '
                 'it is here because answering something is how you find out whether you '
                 'were following.')}
            <form class="crs-quiz" onsubmit="return false">
              <p class="crs-quiz__q">Which property creates the rows you never declared?</p>
              <div class="crs-quiz__options">
                <label class="crs-quiz__option"><input type="radio" name="q1" />
                  <span>grid-template-rows</span></label>
                <label class="crs-quiz__option"><input type="radio" name="q1" />
                  <span>grid-auto-rows</span></label>
                <label class="crs-quiz__option"><input type="radio" name="q1" />
                  <span>align-content</span></label>
              </div>
              <div class="crs-quiz__foot">
                <span class="t-slate-sm" style="color:var(--fg-faint)">Not marked, not stored</span>
                <button class="btn btn-secondary btn-sm" type="submit">Check</button>
              </div>
            </form>
          </div>
        </div>

        <div class="col-panel" id="p-transcript" role="tabpanel" aria-labelledby="t-transcript">
          <span class="col-panel__label">Transcript</span>
          <div class="col-transcript">
            {''.join(f'<a class="col-transcript__line" href="#i"'
                     f'{" aria-current=\"true\"" if i == 1 else ""}>'
                     f'<span class="col-transcript__time">{t}</span><span>{line}</span></a>'
                     for i, (t, line) in enumerate(TRANSCRIPT))}
          </div>
        </div>

        <div class="col-panel" id="p-resources" role="tabpanel" aria-labelledby="t-resources">
          <span class="col-panel__label">Resources</span>
          {files_block()}
        </div>

        <div class="col-panel" id="p-notes" role="tabpanel" aria-labelledby="t-notes">
          <span class="col-panel__label">Notes</span>
          <form class="col-note" onsubmit="return false">
            <label class="label" for="note">Your note on this lesson</label>
            <textarea class="input" id="note" placeholder="Timestamped to where you are."></textarea>
            <div class="col-note__foot">
              <span class="col-note__stamp">At 1:19 · {title}</span>
              <button class="btn btn-secondary btn-sm" type="submit">Save note</button>
            </div>
          </form>
          <p class="t-small u-fg-subtle u-mt-4" style="max-width:var(--measure-lead)">
            This demo keeps nothing. A real course saves notes on the server, and a
            demo that wrote to localStorage would be teaching a persistence trick
            rather than a design system.</p>
        </div>
      </div>
    </div>

    <a class="col-next u-mt-10" href="./lesson.html" data-step="next">
      <span class="col-next__label">Next · Lesson {HERE_I + 2}</span>
      <span class="col-order__title">{next_t}</span>
      <span class="t-small u-fg-subtle">After {prev_t.lower()}, this is where grid
        stops being a mystery.</span>
    </a>
  </section>
  </div>'''
    return page(HERE, 'lesson.html', f'{title} — CSS From Scratch',
                'The lesson player: the video, the syllabus beside it, and the '
                'transcript under it.',
                body, NAME, own_css='course.css', current='course')


def route_components():
    def demo(title, note, markup):
        return (f'<section class="u-mb-10"><h2 class="t-h3 u-mb-2">{title}</h2>'
                f'<p class="t-subtle u-mb-5" style="max-width:var(--measure-lead)">{note}</p>'
                f'<div class="surface" style="padding:var(--space-6);border-radius:var(--radius-card)">'
                f'{markup}</div></section>')

    body = f'''
  <div class="container section-sm">
    <header class="u-mb-10">
      <span class="t-slate" style="color:var(--fg-faint)">Collection · Course</span>
      <h1 class="t-display-2 u-mt-3">The learning sections, on their own</h1>
      <p class="t-lead u-mt-4" style="max-width:var(--measure-lead)">
        What course added to the shared vocabulary, plus the four things that are
        genuinely its own. Everything with a <b>col-</b> prefix below is now
        available to every collection; the <b>crs-</b> ones are course's, until a
        second collection wants them.
      </p>
    </header>

    {demo('col-resume', "The strip for someone who has been here before. It outranks "
          "the hero's call to action, because &ldquo;carry on&rdquo; beats "
          "&ldquo;start&rdquo; for everyone it applies to, and is invisible to "
          "everyone it does not.", resume_strip())}

    {demo('col-stagebar', 'Under a player: where you are, and the two ways out. '
          'Previous and next are the entire navigation of an ordered collection, so '
          'they get the width.',
          '<div class="col-stagebar" style="border-bottom:0">'
          '<a class="btn btn-secondary btn-sm" href="#i" aria-disabled="true">← Previous</a>'
          '<div class="col-stagebar__where"><span class="col-stagebar__pos">'
          '<span>Lesson 1 of 15</span><span>Foundations</span><span>6:12</span></span>'
          '<h3 class="t-h3" style="margin:0">What a design system actually is</h3></div>'
          '<span class="cluster" style="gap:var(--space-2)">'
          '<button class="btn btn-quiet btn-sm" type="button">Mark complete</button>'
          '<a class="btn btn-primary btn-sm" href="#i">Next →</a></span></div>')}

    {demo('col-playlist', 'The syllabus, beside a player. It <em>is</em> .curriculum — '
          'the same modules, the same lesson rows, the same tick. All this modifier '
          'adds is a body that scrolls, because it now sits next to a video instead '
          'of running the width of a page.',
          '<div style="max-width:24rem">' + curriculum(playlist=True) + '</div>')}

    {demo('col-transcript', 'Timestamps down the left, so the column of times is '
          'scannable and the line the player is on can be marked without the text '
          'moving.',
          '<div class="col-transcript">' + ''.join(
              f'<a class="col-transcript__line" href="#i"'
              f'{" aria-current=\"true\"" if i == 1 else ""}>'
              f'<span class="col-transcript__time">{t}</span><span>{line}</span></a>'
              for i, (t, line) in enumerate(TRANSCRIPT[:4])) + '</div>')}

    {demo('col-checks', 'What you will be able to do afterwards. A promise reads as a '
          'promise in a list and as marketing in a paragraph.', outcomes_block(OUTCOMES[:4]))}

    {demo('col-offer', 'The one card on the page that is asking for something, so it '
          'is the one that carries the accent.',
          '<div style="max-width:20rem">' + offer_widget() + '</div>')}

    {demo('col-files', 'What comes with the thing. Rows, because a download is an '
          'action and actions read as a list.', files_block())}

    {demo('col-keys', 'A player has shortcuts whether or not it advertises them. '
          'Advertising them is cheaper than a help page.',
          '<div style="max-width:20rem">' + keys_widget() + '</div>')}

    {demo('crs-level', 'Three bars, one to three lit. The word "intermediate" means '
          'nothing until you have seen the other two; three bars are comparable at a '
          'glance across a grid, which is where difficulty is actually read.',
          '<span class="cluster" style="gap:var(--space-6)">'
          + ''.join(level_chip(n) for n in (1, 2, 3)) + '</span>')}

    {demo('crs-quiz', 'Native radios inside labels, so the keyboard, the grouping and '
          'the announcement all come free. The only thing added is what a chosen '
          'answer looks like.',
          '<form class="crs-quiz" onsubmit="return false" style="max-width:32rem">'
          '<p class="crs-quiz__q">Which property creates the rows you never declared?</p>'
          '<div class="crs-quiz__options">'
          '<label class="crs-quiz__option"><input type="radio" name="d1" />'
          '<span>grid-template-rows</span></label>'
          '<label class="crs-quiz__option"><input type="radio" name="d1" checked />'
          '<span>grid-auto-rows</span></label></div></form>')}

    {demo('crs-cert', 'Deliberately quiet: a hairline double border and one line of '
          'accent. A certificate that shouts is a certificate nobody believes.',
          '<div class="crs-cert pattern pattern-grid pattern-lg pattern-faint">'
          f'<span class="crs-cert__seal">{icon("check", group="ui")}</span>'
          '<span class="crs-cert__name">CSS From Scratch</span>'
          '<span class="crs-cert__rule"></span>'
          f'<span class="crs-cert__meta">{N} lessons · issued on completion</span></div>')}

    <p class="u-mt-10"><a class="btn btn-secondary" href="./index.html">← Back to /course</a>
      <a class="btn btn-primary" href="./lesson.html">Open the lesson player →</a></p>
  </div>'''
    return page(HERE, 'components.html', 'Course sections — Courses',
                'Every block the course routes are assembled from, on its own.',
                body, NAME, own_css='course.css', current='course')


if __name__ == '__main__':
    made = [route_index(), route_track(), route_topic(), route_course(),
            route_lesson(), route_components()]
    print('course: ' + ', '.join(made))
