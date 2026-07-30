#!/usr/bin/env python3
"""The pages collection — the site's own one-offs.

Not a five-route collection and not trying to be one: home, about, contact,
archive, now, terms, privacy and welcome are each exactly one page, so they
share a folder instead of each inventing their own. Résumé lives here too,
moved from its own collection/ folder for the same reason — one document is
one page, not a collection.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from shell import (icon, ph, page, sec, hero, meta_strip, pagination,   # noqa: E402
                   page_head, stats, cta, cta_sponsor, cine_hero, REL,
                   win_browser, win_code, win_term, marquee, alert, vf, timeline)

NAME = 'Pages'

# title, file, note, icon — every one-off route this folder holds, in the
# order a first-time visitor would actually want them.
PAGES_LIST = [
    ('Home', 'home.html', 'The site itself — every collection and what is lately in each.', 'pin'),
    ('About', 'about.html', 'Who is building this, and why token-first.', 'take'),
    ('Contact', 'contact.html', 'One form, no ticket system behind it.', 'chat'),
    ('Archive', 'archive.html', 'Everything published, in one year-grouped timeline.', 'course'),
    ('Now', 'now.html', 'What I am actually working on this month.', 'rec'),
    ('Résumé', 'resume.html', 'Experience, education, skills — one page, print-ready.', 'briefcase'),
    ('Membership', 'membership.html', 'Three tiers, and a free one that is not a trial.', 'take'),
    ('Sign in', 'login.html', 'The centred-card auth shape.', 'check'),
    ('Create account', 'signup.html', 'The split auth shape — the form still has to sell.', 'chat'),
    ('Finish setting up', 'signup-minimal.html', 'The minimal auth shape, for one field.', 'mail'),
    ('Terms', 'terms.html', 'The legal page, kept as short as it can legally be.', 'check'),
    ('Privacy', 'privacy.html', 'What is collected, and what is not.', 'compass'),
    ('Welcome, subscriber', 'welcome.html', 'The page a new subscriber lands on.', 'mail'),
]

CONTACTS = [
    ('mail', 'hello@swarnil.dev'),
    ('phone', '+1 555 0100'),
    ('pin', 'Remote · UTC+5:30'),
    ('external', 'swarnil.dev'),
]

EXPERIENCE = [
    ('Senior Product Engineer', 'Northwind Studio', '2023 — Now',
     'Owns the design system this page is built with: tokens, components and the '
     'collections that ship on top of them.', ['Design systems', 'CSS', 'Accessibility']),
    ('Frontend Engineer', 'Fieldnote', '2021 — 2023',
     'Rebuilt the marketing site on a token-first stylesheet, cutting shipped CSS '
     'by two thirds with no framework underneath it.', ['CSS', 'Performance']),
    ('Frontend Developer', 'Loop & Co', '2019 — 2021',
     'First engineering hire. Built the component library the rest of the product '
     'grew from.', ['JavaScript', 'Component libraries']),
]

# The header's own facts — the questions a recruiter opens a résumé to answer,
# in the order they ask them. Kept as data so the header and the print view
# cannot drift.
PROFILE = [
    ('pin', 'Location', 'Remote · UTC+5:30'),
    ('flag', 'Nationality', 'Indian · EU work authorised'),
    ('globe', 'Website', 'swarnil.dev'),
    ('mail', 'Email', 'hello@swarnil.dev'),
]

SOCIALS = [
    ('github', 'GitHub', '@imswarnil', 'https://github.com/imswarnil'),
    ('linkedin', 'LinkedIn', 'in/swarnil', 'https://linkedin.com/in/swarnil'),
    ('x', 'X', '@imswarnil', 'https://x.com/imswarnil'),
    ('youtube', 'YouTube', '@swarnilbuilds', 'https://youtube.com/@swarnilbuilds'),
]

OPEN_TO_WORK = True

EDUCATION = [
    ('10th', 'Delhi Public School, R.K. Puram', 'New Delhi', '2013',
     'Percentage', '92.4%'),
    ('12th', 'Delhi Public School, R.K. Puram', 'New Delhi', '2015',
     'Percentage', '89.6%'),
    ('B.Tech', 'Indian Institute of Technology, Delhi',
     'Computer Science &amp; Engineering', '2019', 'CGPA', '8.7 / 10'),
]

RESUME_PROJECTS = [
    ('Creator Design System', 'A token-first CSS design system with six real '
     'collections built on top of it — this page is one of them.',
     ['CSS', 'Design systems', 'Python']),
    ('Fieldnote CMS migration', 'Rebuilt a marketing site\'s content layer '
     'without a framework, cutting shipped CSS by two thirds.',
     ['CSS', 'Performance']),
    ('Component playground', 'An internal tool for previewing every component '
     'in both themes before it ships.', ['JavaScript', 'Accessibility']),
]

SKILLS = ['CSS', 'Design systems', 'Accessibility', 'JavaScript', 'Performance',
          'Typography', 'Motion', 'Component libraries']

# short name, full name, issuer, year — the short name is what the seal carries
CERTIFICATIONS = [
    ('WAS', 'Web Accessibility Specialist', 'IAAP', '2023'),
    ('UX', 'Google UX Design Certificate', 'Google · Coursera', '2022'),
    ('CSS', 'Advanced CSS and Sass', 'Udemy', '2021'),
]

LANGUAGES = [
    ('English', 100, 'Native'),
    ('Hindi', 100, 'Native'),
    ('Spanish', 45, 'Conversational'),
]

LINKS = [
    ('external', 'swarnil.dev'),
    ('external', 'github.com/swarnil'),
    ('external', 'linkedin.com/in/swarnil'),
]

PATTERNS = ['pattern-grid', 'pattern-hatch', 'pattern-dots']

# For home + archive: a small, representative cross-section, not a live index.
COLLECTIONS = [
    ('Travel', 'travel', 'Six countries, thirty-one posts and the receipts.', 'pin'),
    ('Courses', 'course', 'Learn the system, in order — six courses, 132 lessons.', 'course'),
    ('Blog', 'blog', 'Notes on building things, and what broke.', 'pen'),
    ('Webseries', 'webseries', 'Five shows, thirty-two episodes, in order.', 'slate'),
    ('Newsletter', 'newsletter', 'Updates, when there are any.', 'mail'),
    ('Projects', 'projects', 'Four repos, each with its own build log.', 'take'),
    ('Videos', 'videos', 'Sixty-two uploads, newest first.', 'live'),
    ('Guides', 'guides', 'Post series with a stepper — four and counting.', 'course'),
    ('Prompts', 'prompts', 'The exact wording, so the good version has a permalink.', 'chat'),
    ('Snippets', 'snippets', 'CSS and JS copy-pasted between projects often enough.', 'slate'),
    ('Products', 'products', 'What is actually on the desk and in the dock.', 'take'),
    ('Pages', '_pages', 'Every one-off page on the site, in one list.', 'pin'),
]

# The archive mixes every collection on one page, which is the one place a
# reader cannot tell what kind of thing they are looking at from context. So
# each row carries its collection as a visual tag: an icon, a label, and a hue
# off the same ladder .col-ph uses, so twelve kinds read as one set rather than
# twelve colour decisions. `kind` keys into KINDS.
KINDS = {
    'travel':     ('Travel', 'pin', 340),
    'course':     ('Course', 'course', 262),
    'blog':       ('Blog', 'pen', 96),
    'webseries':  ('Episode', 'slate', 24),
    'newsletter': ('Newsletter', 'mail', 190),
    'projects':   ('Build log', 'take', 210),
    'videos':     ('Video', 'live', 8),
    'guides':     ('Guide', 'course', 150),
    'prompts':    ('Prompt', 'chat', 285),
    'snippets':   ('Snippet', 'slate', 205),
}

# title, href, date, kind
ARCHIVE = [
    ('2026', [
        ('Ship v1', 'projects/log.html', 'Jul 22', 'projects'),
        ('The grid lesson nobody asked for', 'newsletter/post.html', 'Jul 22', 'newsletter'),
        ('CSS Grid in six minutes, no filler', 'videos/video.html', 'Jul 16', 'videos'),
        ('Grid, in four rules', 'course/lesson.html', 'Jul 09', 'course'),
        ('Grid, from scratch', 'guides/guide.html', 'Jul 04', 'guides'),
        ('The pitch that almost worked', 'webseries/episode.html', 'Jun 30', 'webseries'),
        ('Fluid type with one clamp()', 'snippets/snippet.html', 'Jun 22', 'snippets'),
        ('Why I stopped using a CSS framework', 'blog/post.html', 'Jun 12', 'blog'),
        ('Rename a variable everywhere, safely', 'prompts/prompt.html', 'May 28', 'prompts'),
        ('The train south', 'travel/post.html', 'Mar 14', 'travel'),
    ]),
    ('2025', [
        ('Where I actually build this', 'videos/video.html', 'Nov 28', 'videos'),
        ('Kyoto in the rain is the correct Kyoto', 'travel/post.html', 'Nov 20', 'travel'),
        ('What a month in Lisbon actually costs', 'travel/post.html', 'Sep 03', 'travel'),
        ('Dark mode without a second stylesheet', 'blog/post.html', 'Aug 11', 'blog'),
    ]),
]


def summary_block(name, role, pitch, contacts, resume_href='#i'):
    rows = ''.join(
        f'<span class="rsm-summary__contact">{icon(i)}<span>{label}</span></span>'
        for i, label in contacts)
    return f'''
    <div class="rsm-summary">
      <div>
        <h1 class="rsm-summary__name">{name}</h1>
        <p class="rsm-summary__role">{role}</p>
      </div>
      <p class="rsm-summary__pitch">{pitch}</p>
      <div class="rsm-summary__contacts">{rows}</div>
      <div class="rsm-summary__actions">
        <a class="btn btn-primary btn-sm" href="{resume_href}">{icon('download')}Download résumé</a>
        <a class="btn btn-secondary btn-sm" href="#experience">See experience</a>
      </div>
    </div>'''


def timeline_block(jobs):
    """`.tl.tl-ranged` — a career history is the one sequence where the node
    should be a bar rather than a dot, because the thing being shown is
    duration. Was `.col-order` (a collection's series spine, borrowed); the
    ranged timeline is the component that actually means this."""
    return timeline([
        # The node carries the company mark rather than a bare capsule, so the
        # rail answers "where" before the copy does.
        dict(time=when, title=f'{title} · {company}', note=note, meta=tags,
             current=(when.endswith('Now')),
             node=icon('briefcase', 'icon-sm', group='resume'))
        for title, company, when, note, tags in jobs
    ], ranged=True)


def education_block(schools):
    items = ''.join(
        f'<div class="col-order__item" style="text-decoration:none">'
        f'<span class="col-order__num"><span class="rsm-order__icon">{icon("graduation-cap")}</span></span>'
        f'<div class="col-order__body">'
        f'<span class="col-order__title">{level} — {institution}</span>'
        f'<span class="col-order__note">{detail}</span>'
        f'<div class="col-order__meta"><span>{year}</span>'
        f'<span>{metric_label}: {metric_value}</span></div></div></div>'
        for level, institution, detail, year, metric_label, metric_value in schools)
    return f'<div class="col-order">{items}</div>'


def projects_block(projects):
    cards = ''.join(
        f'<article class="card"><div class="card__media pattern {PATTERNS[i % len(PATTERNS)]} pattern-media"></div>'
        f'<div class="card__body"><h3 class="card__title">{name}</h3>'
        f'<p class="t-small u-fg-subtle u-mt-2">{desc}</p>'
        f'<div class="cluster u-mt-3">' + ''.join(f'<span class="badge">{t}</span>' for t in tags)
        + '</div></div></article>'
        for i, (name, desc, tags) in enumerate(projects))
    return f'<div class="grid-2">{cards}</div>'


def skills_block(skills):
    return '<div class="cluster">' + ''.join(
        f'<span class="badge">{s}</span>' for s in skills) + '</div>'


def certifications_block(certs, quiet=True):
    """`.cert` — the scalloped seal carrying the acronym the certificate is
    actually known by, with the full title beside it. `quiet=True` drops the
    accent fill, because a rail of three accent seals is three competing
    signals rather than one."""
    cls = 'cert cert-quiet' if quiet else 'cert'
    rows = ''.join(
        f'<div class="{cls}"><span class="cert__seal">{short}</span>'
        f'<div class="cert__body"><span class="cert__name">{name}</span>'
        f'<span class="cert__issuer">{issuer} · {year}</span></div></div>'
        for short, name, issuer, year in certs)
    return f'<div class="cert-list">{rows}</div>'


def profile_block(rows=PROFILE, socials=SOCIALS, open_to_work=OPEN_TO_WORK):
    """The header's facts: where, what passport, how to reach, and whether the
    answer to "are you available" is yes — which is the one thing a résumé is
    usually missing and the reader most wants."""
    status = ('<span class="badge badge-live"><span class="dot dot-sm dot-live"></span>'
              'Open to work</span>' if open_to_work else
              '<span class="badge">Not looking right now</span>')
    facts = ''.join(
        f'<div class="rsm-summary__contact">{icon(i, group="resume")}'
        f'<span><span class="u-sr-only">{label}: </span>{value}</span></div>'
        for i, label, value in rows)
    handles = ''.join(
        f'<a class="btn btn-quiet btn-sm" href="{url}" target="_blank" rel="noopener">'
        f'{icon(i, group="social")}{handle}</a>'
        for i, label, handle, url in socials)
    return f'''
    <div class="u-mt-5">{status}</div>
    <div class="rsm-summary__contacts u-mt-4">{facts}</div>
    <div class="cluster u-mt-4" style="gap:var(--space-2)">{handles}</div>'''


def languages_block(languages):
    rows = ''.join(
        f'<div class="row-between u-mb-2"><span class="t-small">{name}</span>'
        f'<span class="t-small u-fg-subtle">{level}</span></div>'
        f'<div class="progress u-mb-4"><div class="progress__bar" style="--value:{pct}%"></div></div>'
        for name, pct, level in languages)
    return rows


def links_block(links):
    return '<div class="cluster">' + ''.join(
        f'<a class="btn btn-secondary btn-sm" href="https://{label}" target="_blank" rel="noopener">'
        f'{icon(i)}{label}</a>' for i, label in links) + '</div>'


def collections_grid():
    cards = ''.join(
        f'<a class="card" href="../{slug}/index.html">'
        f'<div class="card__media pattern {PATTERNS[i % len(PATTERNS)]} pattern-media"></div>'
        f'<div class="card__body"><span class="card__meta">{icon(ico)}{name}</span>'
        f'<p class="t-small u-fg-subtle u-mt-2">{note}</p></div></a>'
        for i, (name, slug, note, ico) in enumerate(COLLECTIONS))
    return f'<div class="grid-3">{cards}</div>'


def pages_block():
    """.c-doc — a row with a label and an arrow, no media. A one-off page is
    a fact, not a scene, so it gets the docs collection's device rather than
    a photo card."""
    rows = ''.join(
        f'<a class="c c-doc" href="./{file}">'
        f'<div class="c__body">'
        f'<span class="c__meta">{icon(ico)}{title}</span>'
        f'<p class="c__excerpt u-m-0" style="color:var(--fg-subtle)">{note}</p>'
        f'</div>'
        f'<span class="c__arrow">{icon("arrow-right")}</span></a>'
        for title, file, note, ico in PAGES_LIST)
    return f'<div class="stack-sm">{rows}</div>'


# ── Index — every one-off page, in one list ─────────────────────────────────

def route_index():
    body = f'''
  {hero('Pages', 'Not a collection of posts — the site\'s own one-offs: home, about, '
        'contact, the archive, and the pages nobody publishes twice.',
        'Site pages', [(str(len(PAGES_LIST)), 'pages')],
        eyebrow_icon='pin', pattern='pattern-hairline')}

  <div class="container section-sm" data-collection>
    {sec('Every page')}
    {pages_block()}
  </div>'''
    return page(HERE, 'index.html', 'Pages — Swarnil',
                'Every one-off page on the site — home, about, contact, archive, '
                'now, résumé, terms, privacy and the subscriber welcome page.',
                body, NAME, own_css='pages.css', current='pages')


# ── Home ─────────────────────────────────────────────────────────────────────

def route_home():
    # The cinematic hero, not the centred statement one: a homepage is the only
    # page that gets to spend a full viewport making its case, and it is the
    # page most likely to be someone's first impression of the system.
    body = cine_hero(
        'A creator\'s site, <em>built from tokens</em>.',
        f'Videos, courses, a blog, a newsletter and the trips between them — '
        f'{len(COLLECTIONS)} collections, one design system, and a build log for '
        f'all of it. Move your pointer across the frame.',
        'Swarnil Singhai',
        video=f'{REL}/video/1280x720.mp4',
        actions='<a class="btn btn-primary btn-pill" href="../travel/index.html">'
                'Start with travel →</a>'
                '<a class="btn btn-ghost btn-pill" href="./about.html">About me</a>',
        eyebrow_icon='pin', filter_id='home')

    # A marquee of what is here, straight under the hero — the one place a
    # scrolling strip is honest, because it is a list of nouns, not a headline.
    body += f'''
  <section class="section-sm">
    {marquee([f'{icon(ico)}{name}' for name, _, _, ico in COLLECTIONS], speed='slow')}
  </section>

  <section class="container section-sm">
    {alert('Version 0.1 is on npm, and the Tailwind and SCSS builds landed with it. '
           '<a href="' + REL + '/docs/usage.html">Read the usage guide →</a>',
           tone='signal', title='New this month', ico='star')}
  </section>

  <!-- The split: the case on the left, the system running in a browser window
       on the right. .win-browser is chrome that says "this is a page" before
       anyone reads a word of it. -->
  <section class="container">
    <div class="hero hero-split">
      <div>
        <span class="hero__eyebrow">{icon('slate', group='creator')}The system</span>
        <!-- .an wraps the words and holds the SVG as its own child; the stroke
             draws itself via stroke-dashoffset, so it reads as a pen rather
             than a fade. pathLength="100" is what lets one CSS rule drive it. -->
        <h2 class="hero__title" style="font-size:var(--text-4xl)">Almost monochrome,
          so <span class="an an-circle">one colour<svg viewBox="0 0 220 70"
            preserveAspectRatio="none" aria-hidden="true"><ellipse cx="110" cy="35"
            rx="103" ry="27" pathLength="100" /></svg></span> can mean something.</h2>
        <p class="hero__lead">Two ramps. Ink does the whole site; signal is rationed
          so hard that when it appears, it means live, now, here.</p>
        <div class="hero__actions">
          <a class="btn btn-primary btn-pill" href="{REL}/docs/introduction.html">Read the docs →</a>
          <a class="btn btn-quiet btn-pill" href="{REL}/docs/components.html">All components</a>
        </div>
      </div>
      <div class="hero-split__stage">
        {win_browser('creator.imswarnil.com',
                     f'<div class="pattern pattern-topo pattern-media">{ph("css", tall=True)}</div>')}
        <p class="hero-split__caption"><span>The docs, in a browser</span>
          <span class="timecode">0.1.0</span></p>
      </div>
    </div>
  </section>

  <!-- Two windows side by side: install it, then write in it. .win-term and
       .win-code, both chrome the foundation shipped and nothing had used. -->
  <section class="container section-sm">
    {sec('Two commands and a stylesheet',
         'No init step, no config file, no runtime — the whole installation.')}
    <div class="grid-2">
      {win_term([(True, 'npm install creator-design-system'),
                 (False, '<span class="tok-com">added 1 package in 1.2s</span>'),
                 (True, '')])}
      {win_code('main.css', [
          '<span class="tok-com">/* your overrides, after the import */</span>',
          '<span class="tok-key">@import</span> <span class="tok-str">"creator-design-system"</span>;',
          '',
          '<span class="tok-sel">:root</span> <span class="tok-punc">{{</span>',
          '  <span class="tok-var">--accent</span><span class="tok-punc">:</span> <span class="tok-num">#6d4aff</span>;',
          '  <span class="tok-var">--radius-card</span><span class="tok-punc">:</span> <span class="tok-num">1.25rem</span>;',
          '<span class="tok-punc">}}</span>',
      ])}
    </div>
  </section>

  <section class="container section-sm">
    {sec('Everything I publish',
         f'{len(COLLECTIONS)} collections, the same tokens underneath all of them.')}
    {collections_grid()}
  </section>

  <!-- .sec-cascade staggers its own children in on reveal, so the numbers do
       not all arrive at once. Reduced motion collapses it to a short fade. -->
  <section class="container section-sm sec-cascade">
    {sec('Lately', 'The numbers, rather than a claim about them.')}
    {stats([('132', 'Lessons', '+8 this month'), ('9.2k', 'Newsletter readers'),
            ('31', 'Travel posts'), ('62', 'Videos', '+3 this month')])}
  </section>

  <!-- The viewfinder, on the one thing that is literally footage. .vf and
       .pattern can never share an element — the pattern goes on the child. -->
  <section class="container section-sm">
    {sec('On camera', 'Sixty-two uploads, and the corners that say why this system '
         'has a creator icon group at all.')}
    <div class="grid-2">
      {vf(f'<div class="pattern pattern-filmstrip pattern-media">{ph("motion", tall=True)}</div>')}
      <div>
        <h3 class="t-h3">The frame is the brand</h3>
        <p class="t-subtle u-mt-3">Four corners, a record dot and a timecode — the
          devices a production desk already uses, so nothing had to be invented to
          make a video page look like a video page.</p>
        <div class="cluster u-mt-6" style="gap:var(--space-3)">
          <span class="badge badge-live"><span class="dot dot-sm dot-live"></span>Live</span>
          <span class="badge">TAKE 47</span>
          <span class="timecode">00:12:47</span>
        </div>
        <a class="btn btn-secondary btn-pill u-mt-6" href="../videos/index.html">
          All videos →</a>
      </div>
    </div>
  </section>

  <section class="container section-sm">
    {cta('One email when something is <em>worth it</em>.',
         'Sent when there is something to say. No drip sequence, no '
         'course funnel, and an unsubscribe link that works on the first click.',
         kicker=f'{icon("mail")}The newsletter', newsletter=True,
         fine='No spam. Unsubscribe any time.',
         pattern='pattern-glow pattern-lg')}
  </section>

  <section class="container section-sm">
    {cta_sponsor('Free, MIT-licensed, and 37 KB gzipped.',
        kicker=f'{icon("take", group="creator")}Sponsor',
        actions='<a class="btn btn-secondary" href="https://github.com/sponsors/imswarnil" '
                'target="_blank" rel="noopener">Sponsor →</a>')}
  </section>'''
    return page(HERE, 'home.html', 'Swarnil Singhai — Creator',
                'Videos, courses, a blog and the trips between them — one design '
                'system underneath all of it.', body, NAME,
                own_css='pages.css', current='home')


# ── About ────────────────────────────────────────────────────────────────────

def route_about():
    """Not the résumé with prose around it — that page already exists and links
    from here. This is the story: where it started, what changed, what it is
    for. A story is told in scenes, so the page is scenes: a hero, a journey on
    the timeline, what came out of it, and what it is all pointed at."""
    body = f'''
  <div class="container">
    <section class="hero hero-split">
      <div>
        <span class="hero__eyebrow">{icon('take', group='creator')}My story</span>
        <h1 class="hero__title">I got tired of having the <em>same argument</em>.</h1>
        <p class="hero__lead">Which grey. Which radius. Where the sidebar goes. Nine
          years of the same four arguments on every new project — so I wrote the
          answers down once, and the answers became this.</p>
        <div class="hero__actions">
          <a class="btn btn-primary btn-pill" href="#journey">The long version ↓</a>
          <a class="btn btn-secondary btn-pill" href="./resume.html">
            {icon('briefcase', group='resume')}The résumé instead</a>
        </div>
      </div>
      <div class="hero-split__stage">
        <div class="frame frame-ink">{ph('about', tall=True)}</div>
        <div class="hero-split__caption"><span>Desk, wherever it is that month</span>
          <span>2026</span></div>
      </div>
    </section>
  </div>

  <div class="container section-sm">
    {stats([('9', 'Years shipping'), ('12', 'Collections built'),
            ('37', 'KB gzipped', 'the whole system'), ('0', 'Dependencies')],
           bare=True)}
  </div>

  <!-- The journey. An alternating timeline, because a story with turns in it
       reads better zig-zagged than as a single column of dates. -->
  <section class="container section-sm" id="journey">
    {sec('How it actually went', 'Including the part where I built the wrong '
         'thing first, which is the part most of these pages leave out.')}
    {timeline([
        dict(time='2015', title='A design degree I did not finish using',
             kind='start', done=True,
             note='Learned to make one beautiful page. Learned nothing about '
                  'making the second one match it.'),
        dict(time='2019', title='First engineering hire at Loop &amp; Co', done=True,
             note='Built a component library nobody used, because I built it '
                  'before anyone had felt the pain it solved.'),
        dict(time='2021', title='The rebuild that taught me the lesson', done=True,
             note='Cut two thirds of a marketing site\'s CSS by deleting '
                  'decisions rather than code.'),
        dict(time='2023', title='Tokens before templates', done=True,
             note='Started writing the answers down instead of re-deciding them. '
                  'That file became this system.'),
        dict(time='Now', title='Twelve collections on one contract',
             current=True,
             note='Eight of the twelve needed no new CSS. That was the whole test.'),
    ], alt=True)}
  </section>

  <section class="container section-sm">
    {sec('What came out of it', 'The things I would point at if you asked what '
         'nine years bought.')}
    <div class="grid-3">
      {''.join(f'<div class="card"><div class="card__body">'
               f'<span class="card__meta">{icon(ico, group="creator")}{kind}</span>'
               f'<h3 class="card__title">{title}</h3>'
               f'<p class="card__excerpt">{note}</p></div></div>'
               for kind, title, note, ico in [
          ('Shipped', 'A system, not a stylesheet',
           'Twelve collections, one vocabulary, 37 KB — and a rebrand that is one file.', 'take'),
          ('Taught', '132 lessons, 9.2k readers',
           'Six courses and a newsletter, all built on the thing they teach.', 'course'),
          ('Held', 'Zero dependencies, nine years',
           'Nothing here breaks because something else released a major version.', 'slate'),
      ])}
    </div>
  </section>

  <!-- The mission, on the one inverse band this page gets. -->
  <section class="container section-sm">
    {cta('Fewer decisions, made <em>better</em>.',
         'A design system is not a component library. It is the set of arguments '
         'you have already had, written down so nobody has to have them again — '
         'and every hour that buys back is an hour spent on the work itself.',
         kicker=f'{icon("viewfinder", group="creator")}The mission',
         actions='<a class="btn btn-primary btn-pill" href="./contact.html">'
                 'Work with me →</a>'
                 '<a class="btn btn-ghost btn-pill" href="./now.html">What I am on now</a>',
         pattern='pattern-mesh pattern-lg')}
  </section>

  <div class="container section-sm">
    {sec('How I work', 'Three rules, and the reasons rather than the slogans.')}
    <div class="col-checks">
      {''.join(f'<span class="col-check"><span class="col-check__tick">'
               f'{icon("check", group="ui")}</span><span>{t}</span></span>'
               for t in [
          'Tokens before templates — a value used twice is a decision, not a number',
          'Accessibility as a default, because retrofitting it costs more than it saves',
          'As little JavaScript as the page can get away with, so less can break',
      ])}
    </div>
  </div>

  <div class="container section-sm">
    {cta_sponsor('The whole thing is free and MIT-licensed.',
        kicker=f'{icon("take", group="creator")}Sponsor',
        actions='<a class="btn btn-secondary" href="https://github.com/sponsors/imswarnil" '
                'target="_blank" rel="noopener">Sponsor →</a>')}
  </div>'''
    return page(HERE, 'about.html', 'About — Swarnil Singhai',
                'How a design degree, a component library nobody used and one '
                'stubborn rebuild turned into a design system.',
                body, NAME, own_css='pages.css', current='about')


# ── Contact ──────────────────────────────────────────────────────────────────

def route_contact():
    body = f'''
  <div class="container-narrow section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./home.html">Home</a> <span>/</span> <span>Contact</span>
    </nav>

    {page_head('Say hello',
        'For work, a correction on something I wrote, or just to say a lesson '
        'helped. I read everything; I don\'t always answer fast.',
        eyebrow=f'{icon("chat")}Contact')}

    <!-- Two columns: the form is the job, the rail sets expectations before
         anyone spends five minutes writing. A form with no stated response time
         is how "did that even send?" happens. -->
    <div class="grid-rail u-mt-10">
      <form class="stack" onsubmit="return false">
        <div class="field">
          <label class="label" for="c-name">Name</label>
          <input class="input" id="c-name" type="text" autocomplete="name" />
        </div>
        <div class="field">
          <label class="label" for="c-email">Email</label>
          <input class="input" id="c-email" type="email" autocomplete="email" />
        </div>
        <div class="field">
          <label class="label" for="c-subject">What is it about?</label>
          <select class="select" id="c-subject">
            <option>Work — a project or a role</option>
            <option>A correction on something I wrote</option>
            <option>A question about the design system</option>
            <option>Something else</option>
          </select>
        </div>
        <div class="field">
          <label class="label" for="c-msg">Message</label>
          <textarea class="input" id="c-msg" rows="6"></textarea>
          <span class="hint">Markdown is fine. Links are welcome.</span>
        </div>
        <button class="btn btn-primary" type="submit">Send</button>
      </form>

      <aside>
        <div class="col-widget">
          <span class="col-widget__title">What to expect</span>
          {stats([('2–4', 'Days to reply'), ('100%', 'Read')], bare=True)}
        </div>
        <div class="u-mt-6">
          {alert('Nothing here is a ticket system. It is one inbox, read by one '
                 'person, usually in the evening.', tone='info', ico='search')}
        </div>
        <!-- The handles, with the platform named rather than just an icon: a
             row of bare glyphs makes someone hover to find out which is which. -->
        <div class="col-widget u-mt-6">
          <span class="col-widget__title">Or find me elsewhere</span>
          <div class="stack-sm">
            {''.join(f'<a class="btn btn-quiet btn-sm u-w-full" href="{url}" '
                     f'target="_blank" rel="noopener" style="justify-content:flex-start">'
                     f'{icon(i, group="social")}{label}'
                     f'<span class="u-ms-auto t-slate-sm" style="color:var(--fg-faint)">'
                     f'{handle}</span></a>'
                     for i, label, handle, url in SOCIALS)}
          </div>
        </div>
      </aside>
    </div>

    <div class="u-mt-10">
      {sec('Before you write', 'Four things that come up most, answered here so a '
           'reply is not the fastest way to find out.')}
      <div class="acc">
        <details class="collapse"><summary>Do you take freelance work?</summary>
          <div class="collapse__body">Occasionally, and only design-system work —
            tokens, component libraries, and migrating a site onto one.</div></details>
        <details class="collapse"><summary>Can I use this design system commercially?</summary>
          <div class="collapse__body">Yes. It is MIT-licensed, including for client
            work, with no attribution required.</div></details>
        <details class="collapse"><summary>Will you review my CSS?</summary>
          <div class="collapse__body">If it is short and the question is specific,
            usually yes. A whole repository, usually no.</div></details>
        <details class="collapse"><summary>Are the courses paid?</summary>
          <div class="collapse__body">Some are. Every paid one has a thirty-day
            refund, no questions.</div></details>
      </div>
    </div>
  </div>'''
    return page(HERE, 'contact.html', 'Contact — Swarnil Singhai',
                'Get in touch — work, corrections, or just to say hello.',
                body, NAME, own_css='pages.css', current='contact')


# ── Archive ──────────────────────────────────────────────────────────────────

def archive_row(title, href, when, kind):
    """One archive row, carrying its collection as a visual tag.

    The tag is three signals at once — icon, label, and a hue on the node — so
    it survives greyscale, colour-blindness and CSS-off. The hue rides the same
    ladder `ph()` uses, which is why twelve kinds read as one set instead of
    twelve separate colour decisions."""
    label, ico, hue = KINDS[kind]
    return (f'<a class="col-order__item" href="../{href}" data-post data-tags="{kind}">'
            f'<span class="col-order__num">'
            f'<span class="col-order__dot" style="background:hsl({hue} 52% 46%)"></span>'
            f'</span>'
            f'<div class="col-order__body">'
            f'<span class="col-order__title">{title}</span>'
            f'<div class="col-order__meta">'
            f'<span class="badge badge-info">{icon(ico)}{label}</span>'
            f'<span>{when}</span></div></div></a>')


def route_archive():
    counts = {}
    for _, items in ARCHIVE:
        for *_rest, k in items:
            counts[k] = counts.get(k, 0) + 1
    total = sum(counts.values())

    years = ''.join(
        f'{sec(year, f"{len(items)} things")}<div class="col-order">'
        + ''.join(archive_row(*it) for it in items) + '</div>'
        for year, items in ARCHIVE)

    # Chips filter by collection — data-tags on each row, which collection.js
    # already understands, so this needs no new script.
    chips = ''.join(
        f'<a class="col-tag" href="./archive.html">{icon(KINDS[k][1])}'
        f'{KINDS[k][0]} <span class="u-fg-faint">{n}</span></a>'
        for k, n in sorted(counts.items(), key=lambda kv: -kv[1]))
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./home.html">Home</a> <span>/</span> <span>Archive</span>
    </nav>
    {page_head('Everything, in order',
        'Every post, episode, update and log entry, across every collection, '
        'newest first.', eyebrow=f'{icon("course")}Archive')}

    <!-- An archive is the one page where search beats browsing: people arrive
         knowing roughly what they want, so the field leads and the year groups
         follow. Both are the collection vocabulary, unchanged. -->
    <form class="col-search u-mt-8" onsubmit="return false">
      <label class="col-search__field">
        <span class="u-sr-only">Search the archive</span>
        {icon('search', group='ui')}
        <input type="search" placeholder="Search everything published…" />
      </label>
      <button class="btn btn-primary btn-pill" type="submit">Search</button>
    </form>

    <div class="col-tags u-mt-6" data-collection>
      <a class="col-tag" href="./archive.html" aria-current="page">
        Everything <span class="u-fg-faint">{total}</span></a>
      {chips}
    </div>

    <div class="u-mt-8">
      {stats([(str(total), 'Things here'), (str(len(counts)), 'Kinds'),
              (str(len(ARCHIVE)), 'Years'), ('2019', 'Since')], bare=True)}
    </div>

    <div class="u-mt-10">{years}</div>

    <!-- What the next page looks like before it arrives. .skeleton is the one
         component that should ship visible in a demo: it is what a reader sees
         first, and it is the easiest thing to leave untested. -->
    <div class="u-mt-8" aria-hidden="true">
      {''.join('''<div class="col-order__item" style="pointer-events:none">
        <span class="col-order__num"><span class="skeleton skeleton-avatar"
              style="width:.9rem;height:.9rem"></span></span>
        <div class="col-order__body" style="gap:var(--space-2)">
          <span class="skeleton skeleton-title" style="max-width:22rem"></span>
          <span class="skeleton skeleton-text" style="max-width:7rem"></span>
        </div></div>''' for _ in range(3))}
    </div>

    <div class="u-mt-8">{pagination(1, 4, href='./archive.html', label='Archive')}</div>
  </div>'''
    return page(HERE, 'archive.html', 'Archive — Swarnil Singhai',
                'Every post, episode, update and log entry, newest first.',
                body, NAME, own_css='pages.css', current='archive')


# ── Now ──────────────────────────────────────────────────────────────────────

def route_now():
    """A now page is a status, so it gets a status page's shape: the narrative
    in the main column, and the facts that change independently of it — where,
    what is playing, what is next — in a rail beside it."""
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./home.html">Home</a> <span>/</span> <span>Now</span>
    </nav>

    {page_head("What I am doing now",
        'Updated by hand, roughly monthly. If the date looks stale, the work '
        'below probably shipped.',
        eyebrow=f'{icon("rec", group="creator")}Now · Jul 2026', small=True)}

    <div class="grid-rail u-mt-8">
      <div>
        <div class="content">
          <p>Mostly this: closing the gap between the collections that ship no CSS
            of their own and the ones that still owe the vocabulary something.</p>
        </div>

        <div class="u-mt-8">
          {sec('In flight', 'The one place a progress bar is honest — these are '
               'real, and the numbers move by hand.')}
          {''.join(f'''<div class="progress-labelled u-mb-4">
            <span class="progress__label"><span>{what}</span><span>{pct}%</span></span>
            <div class="progress"><div class="progress__bar" style="--value:{pct}%"></div></div>
            <span class="t-slate-sm" style="color:var(--fg-faint)">{note}</span>
          </div>''' for what, pct, note in [
              ('The pages collection', 90, 'home, about, archive, the legal pages'),
              ('The next newsletter', 60, 'on grid-auto-rows: minmax(0, auto)'),
              ('npm package + Tailwind/SCSS builds', 35, 'the last roadmap item'),
          ])}
        </div>

        <div class="content u-mt-10">
          <h2>Building</h2>
          <p>The pages collection — home, about, archive, and the legal pages
            nobody reads but every site needs anyway.</p>
          <h2>Writing</h2>
          <p>The next newsletter, on why <code>grid-auto-rows: minmax(0, auto)</code>
            fixes more layouts than any tutorial mentions.</p>
          <h2>Reading</h2>
          <p>Old CSS specs, mostly, looking for the one line that explains a
            behaviour everyone works around instead of naming.</p>
          <h2>Not doing</h2>
          <p>Client work until the npm release is out. Saying that out loud is the
            only thing that has ever made it true.</p>
        </div>

        <div class="u-mt-8">
          {alert('This page is a status, not a commitment. Anything here can be '
                 'dropped without ceremony, which is the point of having it.',
                 tone='warning', ico='search')}
        </div>
      </div>

      <aside class="col-rail col-rail-sticky">
        <div class="col-widget">
          <span class="col-widget__title">Where</span>
          <div class="rsm-summary__contacts">
            {''.join(f'<div class="rsm-summary__contact">{icon(i, group="resume")}'
                     f'<span>{v}</span></div>'
                     for i, l, v in PROFILE[:2])}
          </div>
        </div>

        <div class="col-widget">
          <span class="col-widget__title">This month</span>
          {stats([('3', 'Shipping'), ('1', 'Writing')], bare=True)}
        </div>

        <div class="col-widget">
          <span class="col-widget__title">On repeat</span>
          <div class="list-group list-group-flush">
            {''.join(f'<span class="list-group__item">{t}'
                     f'<span class="u-ms-auto t-slate-sm" '
                     f'style="color:var(--fg-faint)">{w}</span></span>'
                     for t, w in [('Old CSS specs', 'reading'),
                                  ('Ambient, no lyrics', 'listening'),
                                  ('Berlin, for now', 'living')])}
          </div>
        </div>

        <div class="col-widget col-widget-accent">
          <span class="col-widget__title">Next up</span>
          <p class="t-small">The npm release, then the Tailwind and SCSS builds.</p>
          <a class="btn btn-primary btn-sm u-w-full u-mt-4" href="../projects/index.html">
            Follow the build log →</a>
        </div>
      </aside>
    </div>
  </div>'''
    return page(HERE, 'now.html', 'Now — Swarnil Singhai',
                'What I am building, writing and reading right now.',
                body, NAME, own_css='pages.css', current='now')


# ── Legal ────────────────────────────────────────────────────────────────────

def _legal_page(slug, title, lead, body_html, toc=(), updated='Jul 2026', summary=''):
    """One shell, two bodies. A legal page nobody can navigate is the same as a
    legal page nobody reads, so this one gets a sticky TOC rail, a visible
    last-updated date, and an `.alert` carrying the plain-English summary above
    the prose — the three things that make a wall of legal text usable."""
    rail = ''.join(f'<a class="list-group__item" href="#{a}">{t}</a>' for a, t in toc)
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./home.html">Home</a> <span>/</span> <span>{title}</span>
    </nav>

    {page_head(title, lead, eyebrow=f'{icon("check", group="ui")}Legal', small=True)}

    <div class="grid-rail u-mt-8">
      <div>
        {alert(summary, tone='info', title='The short version', ico='check')}
        <div class="content u-mt-8">{body_html}</div>
      </div>
      <aside class="col-rail col-rail-sticky">
        <div class="col-widget">
          <span class="col-widget__title">On this page</span>
          <div class="list-group list-group-flush">{rail}</div>
        </div>
        <p class="t-slate-sm u-mt-4" style="color:var(--fg-faint)">
          Last updated {updated}</p>
      </aside>
    </div>
  </div>'''
    return page(HERE, f'{slug}.html', f'{title} — Swarnil Singhai', lead, body,
                NAME, own_css='pages.css', current=slug)


def route_terms():
    return _legal_page('terms', 'Terms & conditions',
        'Plain terms, because a contract nobody reads is not a contract, it is a trap.',
        '<p>This site and everything on it is provided as-is. Course and newsletter '
        'content is for personal use; do not resell it. Code samples are MIT-licensed '
        'unless a file says otherwise.</p>'
        '<h2 id="accounts">Accounts</h2><p>Free accounts do not expire. Paid course '
        'access is lifetime, tied to the email you purchased with.</p>'
        '<h2 id="refunds">Refunds</h2><p>Thirty days, no questions, on any paid '
        'course.</p>'
        '<h2 id="licence">Licence</h2><p>The design system itself is MIT-licensed, '
        'including for commercial and client work, with no attribution required.</p>',
        toc=[('accounts', 'Accounts'), ('refunds', 'Refunds'), ('licence', 'Licence')],
        summary='Use the system for anything, including client work. Do not resell '
                'the courses. Thirty-day refund, no questions.')


def route_privacy():
    return _legal_page('privacy', 'Privacy policy',
        'What is collected, why, and the short list of things that never leave this '
        'server.',
        '<p>The newsletter form collects an email address and nothing else. Analytics '
        'are aggregate and cookie-free. No data is sold, ever.</p>'
        '<h2 id="stored">What is stored</h2><p>Email address, subscription date, and '
        'which list you are on. Course progress, if you are signed in.</p>'
        '<h2 id="third-parties">Third parties</h2><p>The email provider that sends the '
        'newsletter, and the payment processor for paid courses. Neither receives '
        'anything beyond what a transaction needs.</p>'
        '<h2 id="rights">Your rights</h2><p>Ask for a copy of everything held about '
        'you, or its deletion, at any time. Both are done by hand within a week.</p>',
        toc=[('stored', 'What is stored'), ('third-parties', 'Third parties'),
             ('rights', 'Your rights')],
        summary='An email address if you subscribe, and nothing else. No cookies, '
                'no tracking, nothing sold. Ask for deletion any time.')


# ── Welcome subscriber ───────────────────────────────────────────────────────

# ── Auth ─────────────────────────────────────────────────────────────────────
# Three shapes for the same job, because the right one depends on what the page
# is for: a centred card when signing in is the whole task, a split when the
# product still has to sell itself, and a minimal one for a page reached from an
# email where the decision is already made.

def oauth_row(verb='Continue'):
    """Third-party sign-in. Above the form, because most people use it — a
    provider row placed under the form is a row most readers never see."""
    return '<div class="stack-sm">' + ''.join(
        f'<button class="btn btn-secondary u-w-full" type="button" '
        f'style="justify-content:center">{icon(i, group="social")}{verb} with {n}</button>'
        for i, n in [('github', 'GitHub'), ('x', 'X')]) + '</div>'


def auth_divider(text='or'):
    """A rule with a word in it. Two hairlines and a label, no new CSS."""
    return (f'<div class="cluster u-mt-5 u-mb-5" style="gap:var(--space-3)">'
            f'<hr class="rule" style="flex:1" />'
            f'<span class="t-slate-sm" style="color:var(--fg-faint)">{text}</span>'
            f'<hr class="rule" style="flex:1" /></div>')


def auth_form(mode='login'):
    signup = mode == 'signup'
    name_field = ('''
      <div class="field">
        <label class="label" for="a-name">Name</label>
        <input class="input" id="a-name" type="text" autocomplete="name" required />
      </div>''' if signup else '')
    pw_label = ('<label class="label" for="a-pw">Password</label>' if signup else
                '<div class="row-between"><label class="label" for="a-pw">Password</label>'
                '<a class="t-slate-sm" href="#i">Forgot?</a></div>')
    hint = ('<span class="hint">At least 12 characters. A passphrase beats a '
            'clever substitution.</span>' if signup else '')
    terms = ('''
      <label class="check">
        <input type="checkbox" required />
        <span>I agree to the <a href="./terms.html">terms</a> and
          <a href="./privacy.html">privacy policy</a></span>
      </label>''' if signup else '''
      <label class="check">
        <input type="checkbox" />
        <span>Keep me signed in</span>
      </label>''')
    return f'''
    <form class="stack" onsubmit="return false">{name_field}
      <div class="field">
        <label class="label" for="a-email">Email</label>
        <input class="input" id="a-email" type="email" autocomplete="email" required />
      </div>
      <div class="field">
        {pw_label}
        <input class="input" id="a-pw" type="password"
               autocomplete="{'new-password' if signup else 'current-password'}" required />
        {hint}
      </div>
      {terms}
      <button class="btn btn-primary u-w-full" type="submit"
              style="justify-content:center">{'Create account' if signup else 'Sign in'}</button>
    </form>'''


def route_login():
    """Variant 1 — the centred card. Signing in is the whole task, so the page
    is one column and nothing competes with it."""
    body = f'''
  <div class="container-narrow section" style="max-width:26rem">
    <div class="u-text-center">
      <a class="logo" href="./home.html">Swarnil</a>
      <h1 class="t-h2 u-mt-5">Welcome back</h1>
      <p class="t-subtle u-mt-2">Sign in to pick up where the last lesson stopped.</p>
    </div>

    <div class="surface u-mt-8" style="padding:var(--space-6);border-radius:var(--radius-card)">
      {oauth_row('Continue')}
      {auth_divider('or with email')}
      {auth_form('login')}
    </div>

    <p class="t-small u-fg-subtle u-text-center u-mt-6">
      No account? <a href="./signup.html">Create one</a> — it is free, and the
      free tier is not a trial.</p>
  </div>'''
    return page(HERE, 'login.html', 'Sign in — Swarnil Singhai',
                'Sign in to your account.', body, NAME,
                own_css='pages.css', current='login')


def route_signup():
    """Variant 2 — the split. A signup page still has to sell, so the left
    column carries the reasons and the right one carries the form."""
    body = f'''
  <div class="container">
    <div class="hero hero-split">
      <div>
        <span class="hero__eyebrow">{icon('take', group='creator')}Free account</span>
        <h1 class="hero__title" style="font-size:var(--text-4xl)">
          Start with the <em>whole</em> system.</h1>
        <p class="hero__lead">Every course, the newsletter archive and the
          component reference. No card, and the free tier is not a trial.</p>
        <ul class="plan__features u-mt-6" style="border-top:0;padding-top:0">
          <li>132 lessons across six courses</li>
          <li>The full newsletter archive</li>
          <li>Every snippet and prompt, copy-ready</li>
          <li data-off>Source files and Figma — Member tier</li>
        </ul>
        <div class="u-mt-8">
          {stats([('9.2k', 'Members'), ('4.9', 'Average rating')], bare=True)}
        </div>
      </div>

      <div class="hero-split__stage">
        <div class="surface" style="padding:var(--space-6);border-radius:var(--radius-card)">
          {oauth_row('Sign up')}
          {auth_divider('or with email')}
          {auth_form('signup')}
        </div>
        <p class="t-small u-fg-subtle u-mt-4 u-text-center">
          Already have an account? <a href="./login.html">Sign in</a></p>
      </div>
    </div>
  </div>'''
    return page(HERE, 'signup.html', 'Create an account — Swarnil Singhai',
                'Start free — every course, the newsletter archive and the '
                'component reference.', body, NAME,
                own_css='pages.css', current='signup')


def route_signup_minimal():
    """Variant 3 — minimal, on the inverse band. For a page reached from an
    email, where the decision is already made and the only job left is one
    field. Fewest possible decisions on screen."""
    body = f'''
  <div class="container u-mt-6">
    <section class="hero hero-band hero-statement pattern pattern-mesh pattern-lg">
      <span class="hero__eyebrow">{icon('mail')}One field left</span>
      <h1 class="hero__title">Finish setting up.</h1>
      <p class="hero__lead">Pick a password and the account is live. Your email is
        already confirmed.</p>
      <form class="u-mt-8" onsubmit="return false"
            style="max-width:22rem;margin-inline:auto">
        <div class="input-group">
          <input class="input" type="password" placeholder="Choose a password"
                 aria-label="Choose a password" autocomplete="new-password" />
          <button class="btn btn-primary" type="submit">Finish</button>
        </div>
      </form>
      <p class="cta__fine u-mt-4">Signing in as hello@swarnil.dev ·
        <a href="#i">not you?</a></p>
    </section>
  </div>

  <div class="container section-sm">
    {alert('The three shapes on this page, this one and '
           '<a href="./login.html">login</a> are the same form. Which one to reach '
           'for depends on whether the page still has to sell, and how many '
           'decisions the reader has already made.', tone='info', ico='search',
           title='Three variants, one form')}
  </div>'''
    return page(HERE, 'signup-minimal.html', 'Finish setting up — Swarnil Singhai',
                'One field left — pick a password and the account is live.',
                body, NAME, own_css='pages.css', current='signup')


# ── Membership ───────────────────────────────────────────────────────────────

PLANS = [
    ('Free', '$0', '', 'Everything public, forever. Not a trial.',
     [(True, 'Every published lesson'), (True, 'The newsletter archive'),
      (True, 'Snippets and prompts'), (False, 'Source files'),
      (False, 'Private build logs')], 'Create a free account', 'btn-secondary', False),
    ('Member', '$9', '/month', 'The source, the logs, and the next thing early.',
     [(True, 'Everything in Free'), (True, 'Source files for every course'),
      (True, 'Private build logs'), (True, 'New work a week early'),
      (False, 'A review of your own system')], 'Become a member', 'btn-primary', True),
    ('Studio', '$49', '/month', 'For a team putting this into production.',
     [(True, 'Everything in Member'), (True, 'Up to 10 seats'),
      (True, 'A review of your own system'), (True, 'Priority answers'),
      (True, 'Commercial licence in writing')], 'Talk to me', 'btn-secondary', False),
]


def plan_card(name, price, period, note, features, cta, cta_cls, featured):
    flag = '<span class="plan__flag">Most popular</span>' if featured else ''
    rows = ''.join(f'<li{"" if on else " data-off"}>{t}</li>' for on, t in features)
    return f'''
    <article class="plan{' plan-featured' if featured else ''}">
      {flag}
      <span class="plan__name">{name}</span>
      <p class="plan__price">{price}<span class="plan__period">{period}</span></p>
      <p class="plan__note">{note}</p>
      <ul class="plan__features">{rows}</ul>
      <a class="btn {cta_cls} plan__cta" href="./signup.html">{cta}</a>
    </article>'''


def route_membership():
    body = f'''
  <div class="container section-sm">
    {page_head('Membership',
        'Everything public is free, forever — not a trial with a countdown on it. '
        'Membership buys the source, the logs, and the next thing early.',
        eyebrow=f'{icon("take", group="creator")}Membership')}

    <div class="plan-grid u-mt-10">
      {''.join(plan_card(*p) for p in PLANS)}
    </div>

    <div class="u-mt-8">
      {alert('Every paid tier has a thirty-day refund, no questions and no form. '
             'Cancel from the account page in one click — no email to write.',
             tone='success', ico='check', title='Thirty days, no questions')}
    </div>

    <div class="u-mt-12">
      {sec('What members actually get', 'The honest version, since every pricing '
           'page claims the same four things.')}
      <div class="grid-2">
        {win_code('tokens.css', [
            '<span class="tok-com">/* Members get the source, not a build. */</span>',
            '<span class="tok-sel">:root</span> <span class="tok-punc">{</span>',
            '  <span class="tok-var">--ink-500</span><span class="tok-punc">:</span> <span class="tok-num">#55556a</span>;',
            '  <span class="tok-var">--signal-500</span><span class="tok-punc">:</span> <span class="tok-num">#f04e2e</span>;',
            '<span class="tok-punc">}</span>',
        ])}
        <div>
          {timeline([
              dict(time='Day 0', title='Source files', kind='start', done=True,
                   note='Every course, every collection, unminified.'),
              dict(time='Weekly', title='Private build logs', done=True,
                   note='What broke, and what it cost to fix.'),
              dict(time='Ongoing', title='A week early', current=True,
                   note='New work lands for members first.'),
          ], density='compact')}
        </div>
      </div>
    </div>

    <div class="u-mt-12">
      {sec('Questions people actually ask')}
      <div class="acc">
        <details class="collapse"><summary>Is the free tier a trial?</summary>
          <div class="collapse__body">No. Everything published stays free, with no
            countdown and no card. Membership adds things, it does not unlock
            things that were already there.</div></details>
        <details class="collapse"><summary>Can I use this commercially?</summary>
          <div class="collapse__body">Yes on every tier — the design system is MIT.
            Studio adds that in writing if your legal team needs it.</div></details>
        <details class="collapse"><summary>What happens if I cancel?</summary>
          <div class="collapse__body">You keep every file already downloaded, and
            lose access to new ones. Nothing is revoked retroactively.</div></details>
      </div>
    </div>

    <div class="u-mt-12">
      {cta('Start free. Upgrade if it <em>earns it</em>.',
           'No card for the free tier, and thirty days to change your mind on the '
           'paid ones.',
           kicker=f'{icon("take", group="creator")}Membership',
           actions='<a class="btn btn-primary btn-pill" href="./signup.html">'
                   'Create a free account →</a>'
                   '<a class="btn btn-ghost btn-pill" href="./contact.html">Ask first</a>',
           fine='Cancel in one click, from the account page.',
           pattern='pattern-glow pattern-lg')}
    </div>
  </div>'''
    return page(HERE, 'membership.html', 'Membership — Swarnil Singhai',
                'Everything public is free forever. Membership buys the source, '
                'the logs, and the next thing early.', body, NAME,
                own_css='pages.css', current='membership')


def route_welcome():
    # .hero-band — the inverse billboard, the third hero shape. A confirmation
    # is the one moment a page has earned a full-contrast band: it is saying one
    # thing, it is the only thing on the page, and there is nothing to browse.
    body = f'''
  <div class="container u-mt-6">
    <section class="hero hero-band hero-statement pattern pattern-rays pattern-lg">
      <span class="hero__eyebrow">{icon('check', group='ui')}Confirmed</span>
      <h1 class="hero__title">You're <em>in</em>.</h1>
      <p class="hero__lead">What I am building, what broke, and what I would do
        differently — sent when there is something to say. The first lands within
        the week; nothing before that.</p>
      <div class="hero__actions" style="justify-content:center">
        <a class="btn btn-primary btn-pill" href="../newsletter/index.html">Read the archive →</a>
        <a class="btn btn-ghost btn-pill" href="./home.html">Back to home</a>
      </div>
    </section>
  </div>

  <section class="container section-sm">
    {alert('Check the spam folder if the confirmation is not there in five minutes — '
           'it is the one email that gets filtered most.', tone='success',
           title='Confirmation sent', ico='check')}
  </section>

  <section class="container section-sm">
    {sec('What happens next', 'Three things, in this order, and nothing else.')}
    <div class="col-order">
      {''.join(f"""<a class="col-order__item" href="#i">
        <span class="col-order__num"><span class="col-order__dot"></span>{i + 1:02d}</span>
        <div class="col-order__body"><span class="col-order__title">{t}</span>
        <span class="col-order__note">{note}</span></div></a>"""
        for i, (t, note) in enumerate([
            ('A confirmation, already sent', 'Check the spam folder if it is not there in five minutes.'),
            ('The first one, within the week', 'Then whenever there is something worth sending.'),
            ('Nothing else, ever', 'No drip sequence, no course funnel, no "just checking in".'),
        ]))}
    </div>
  </section>

  <section class="container section-sm">
    {sec('Start here', 'The three things most people read first.')}
    <div class="grid-3">
      {''.join(f'<a class="card" href="{href}"><div class="card__body">'
               f'<span class="card__meta">{icon(ico)}{kind}</span>'
               f'<h3 class="card__title">{title}</h3>'
               f'<p class="card__excerpt">{note}</p></div></a>'
               for kind, title, note, href, ico in [
                   ('Newsletter', 'The grid update', 'Why grid-auto-rows fixes more than any tutorial mentions.', '../newsletter/post.html', 'mail'),
                   ('Course', 'CSS From Scratch', 'Tokens, layout and type — the whole system, built live.', '../course/course.html', 'course'),
                   ('Guide', 'Grid, from scratch', 'Six steps, in the order you actually reach for them.', '../guides/guide.html', 'slate'),
               ])}
    </div>
  </section>

  <div class="container section-sm">
    {cta_sponsor('Prefer to follow along elsewhere?',
        kicker=f'{icon("chat")}Also here',
        actions=links_block(LINKS))}
  </div>'''
    return page(HERE, 'welcome.html', 'You\'re subscribed — Swarnil Singhai',
                'Confirmed — the first one lands within the week.',
                body, NAME, own_css='pages.css', current='welcome')


# ── Résumé (moved from collection/resume/) ───────────────────────────────────

def route_resume():
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./home.html">Home</a> <span>/</span> <span>Résumé</span>
    </nav>

    {page_head('Swarnil Singhai',
        'Senior Product Engineer — design systems, and the sites that run on them.',
        eyebrow=f'{icon("briefcase", group="resume")}Résumé',
        actions='<a class="btn btn-primary btn-pill" href="#i">'
                + icon('download', group='resume') + 'Download PDF</a>'
                '<a class="btn btn-secondary btn-pill" href="./contact.html">Get in touch</a>',
        small=True)}

    <!-- Location, nationality, website, email, availability and the handles —
         the questions a recruiter opens a résumé to answer, above the fold
         rather than in a footer. -->
    {profile_block()}

    <div class="u-mt-8">
      {stats([('9', 'Years'), ('3', 'Companies'),
              (str(len(CERTIFICATIONS)), 'Certifications'),
              (str(len(LANGUAGES)), 'Languages')], bare=True)}
    </div>

    <div class="grid-rail u-mt-10">
      <div>
        <section id="experience">
          {sec('Experience')}
          {timeline_block(EXPERIENCE)}
        </section>

        <section class="u-mt-10">
          {sec('Education')}
          {education_block(EDUCATION)}
        </section>

        <section class="u-mt-10">
          {sec('Projects')}
          {projects_block(RESUME_PROJECTS)}
        </section>

      </div>

      <!-- The rail is every résumé widget the system can legitimately supply.
           Each is an existing component: .col-widget, .badge cluster, .progress,
           .stats-bare, .avatar, .list-group, .cta-sponsor. -->
      <aside class="col-rail">
        <div class="col-widget">
          <span class="col-widget__title">At a glance</span>
          <div class="cluster" style="gap:var(--space-3);align-items:center">
            <span class="avatar avatar-xl">SS</span>
            <div>
              <b>Swarnil Singhai</b>
              <span class="t-slate-sm" style="display:block;color:var(--fg-faint)">
                Senior Product Engineer</span>
              <span class="badge badge-live u-mt-2"><span class="dot dot-sm dot-live"></span>
                Open to work</span>
            </div>
          </div>
        </div>

        <div class="col-widget">
          <span class="col-widget__title">Skills</span>
          {skills_block(SKILLS)}
        </div>

        <div class="col-widget">
          <span class="col-widget__title">Core strengths</span>
          {''.join(f'''<div class="progress-labelled u-mb-4">
            <span class="progress__label"><span>{what}</span><span>{pct}%</span></span>
            <div class="progress progress-thin">
              <div class="progress__bar" style="--value:{pct}%"></div></div>
          </div>''' for what, pct in [('Design systems', 95), ('CSS &amp; layout', 92),
                                       ('Accessibility', 88), ('Motion', 74)])}
        </div>

        <!-- Certifications belong in the rail: they are credentials to be
             scanned, not a narrative to be read, and the seal makes them
             scannable at a glance. -->
        <div class="col-widget">
          <span class="col-widget__title">Certifications</span>
          {certifications_block(CERTIFICATIONS)}
        </div>

        <div class="col-widget">
          <span class="col-widget__title">Languages</span>
          {languages_block(LANGUAGES)}
        </div>

        <div class="col-widget">
          <span class="col-widget__title">Elsewhere</span>
          <div class="stack-sm">
            {''.join(f'<a class="btn btn-quiet btn-sm u-w-full" href="{url}" '
                     f'target="_blank" rel="noopener" style="justify-content:flex-start">'
                     f'{icon(i, group="social")}{handle}</a>'
                     for i, label, handle, url in SOCIALS)}
          </div>
        </div>

        <div class="col-widget col-widget-accent">
          <span class="col-widget__title">Available for work</span>
          <p class="t-small">Design-system work — tokens, component libraries, and
            migrating a site onto one.</p>
          <div class="stack-sm u-mt-4">
            <a class="btn btn-primary btn-sm u-w-full" href="./contact.html">Hire me →</a>
            <a class="btn btn-quiet btn-sm u-w-full" href="#i">
              {icon('download', group='resume')}Download PDF</a>
          </div>
        </div>
      </aside>
    </div>

    <!-- A horizontal timeline of the same career, for the one view a vertical
         list cannot give: shape. Folds back to vertical under 48rem and in
         print, both handled by the component. -->
    <div class="u-mt-12 no-print">
      {sec('The same nine years, as a line',
           'The horizontal axis reads as a process rather than a list — useful '
           'exactly once per page, and this is the once.')}
      {timeline([
          dict(time='2019', title='Loop &amp; Co', kind='start', done=True,
               note='First engineering hire.'),
          dict(time='2021', title='Fieldnote', done=True,
               note='Two thirds less CSS, no framework.'),
          dict(time='2023', title='Northwind Studio', current=True,
               note='Owns the system this page is built with.'),
          dict(time='Next', title='Open to work', kind='now',
               note='Design systems, and the sites that run on them.'),
      ], axis='h')}
    </div>
  </div>'''
    return page(HERE, 'resume.html', 'Résumé — Swarnil Singhai',
                'Senior Product Engineer — experience, education and skills.',
                body, NAME, own_css='pages.css', current='resume')


if __name__ == '__main__':
    made = [route_index(), route_home(), route_about(), route_contact(), route_archive(),
            route_now(), route_terms(), route_privacy(), route_welcome(),
            route_resume(), route_login(), route_signup(), route_signup_minimal(),
            route_membership()]
    print('pages: ' + ', '.join(made))
