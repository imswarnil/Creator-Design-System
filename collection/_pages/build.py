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

CERTIFICATIONS = [
    ('Google UX Design Certificate', 'Google · Coursera', '2022'),
    ('Web Accessibility Specialist (WAS)', 'IAAP', '2023'),
    ('Advanced CSS and Sass', 'Udemy', '2021'),
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
    ('Newsletter', 'newsletter', 'Forty-one issues, and counting.', 'mail'),
    ('Projects', 'projects', 'Four repos, each with its own build log.', 'take'),
    ('Videos', 'videos', 'Sixty-two uploads, newest first.', 'live'),
    ('Guides', 'guides', 'Post series with a stepper — four and counting.', 'course'),
    ('Prompts', 'prompts', 'The exact wording, so the good version has a permalink.', 'chat'),
    ('Snippets', 'snippets', 'CSS and JS copy-pasted between projects often enough.', 'slate'),
    ('Products', 'products', 'What is actually on the desk and in the dock.', 'take'),
    ('Pages', '_pages', 'Every one-off page on the site, in one list.', 'pin'),
]

ARCHIVE = [
    ('2026', [
        ('Ship v1', 'projects/log.html', 'Jul 22'),
        ('Issue #41 — The grid lesson nobody asked for', 'newsletter/post.html', 'Jul 22'),
        ('Grid, in four rules', 'course/lesson.html', 'Jul 09'),
        ('The pitch that almost worked', 'webseries/episode.html', 'Jun 30'),
        ('Why I stopped using a CSS framework', 'blog/post.html', 'Jun 12'),
        ('The train south', 'travel/post.html', 'Mar 14'),
    ]),
    ('2025', [
        ('What a month in Lisbon actually costs', 'travel/post.html', 'Sep 03'),
        ('Kyoto in the rain is the correct Kyoto', 'travel/post.html', 'Nov 20'),
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
        dict(time=when, title=f'{title} · {company}', note=note, meta=tags,
             current=(when.endswith('Now')))
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


def certifications_block(certs):
    rows = ''.join(
        f'<div class="list-group__item"><span><b>{name}</b>'
        f'<span class="t-small u-fg-subtle" style="display:block">{issuer}</span></span>'
        f'<span class="t-slate-sm u-ms-auto" style="color:var(--fg-faint)">{year}</span></div>'
        for name, issuer, year in certs)
    return f'<div class="list-group">{rows}</div>'


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
    {stats([('132', 'Lessons', '+8 this month'), ('41', 'Newsletter issues'),
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
         'Forty-one issues of practice behind each one. No drip sequence, no '
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
    # .hero-split — the two-column variant: the case on the left, one framed
    # thing on the right. About is where a portrait belongs, and the frame
    # device (layer 1) does the chrome so the stage only reserves the ratio.
    body = f'''
  <div class="container">
    <section class="hero hero-split">
      <div>
        <span class="hero__eyebrow">{icon('take')}About</span>
        <h1 class="hero__title">I build the system, then <em>the site on it</em>.</h1>
        <p class="hero__lead">Tokens first, components second, and as little
          JavaScript as the page can get away with. Everything you are looking
          at is the receipts.</p>
        <div class="hero__actions">
          <a class="btn btn-primary btn-pill" href="./resume.html">Read the résumé →</a>
          <a class="btn btn-secondary btn-pill" href="./contact.html">Get in touch</a>
        </div>
      </div>
      <div class="hero-split__stage">
        <div class="frame frame-ink">{ph('about', tall=True)}</div>
        <div class="hero-split__caption">
          <span>Desk, Berlin</span><span>2026</span>
        </div>
      </div>
    </section>
  </div>

  <div class="container section-sm">
    {stats([('9', 'Years shipping'), (f'{len(COLLECTIONS)}', 'Collections'),
            ('37', 'KB gzipped', 'the whole system'), ('0', 'Dependencies')],
           bare=True)}
  </div>

  <div class="container section-sm">

    {summary_block('Swarnil Singhai', 'Senior Product Engineer',
        'I build design systems and the sites that run on them — tokens first, '
        'components second, and as little JavaScript as the page can get away with. '
        'This whole site is the receipts.', CONTACTS, resume_href='./resume.html')}

    <div class="u-mt-10">
      {sec('Where the time went', 'The short version is on the résumé; this is the '
           'same three jobs with the parts that mattered.')}
      {timeline_block(EXPERIENCE)}
    </div>

    <div class="u-mt-10">
      {sec('What I actually do')}
      <div class="col-checks">
        <span class="col-check"><span class="col-check__tick">{icon('check', group='ui')}</span>
          <span>Design systems — tokens, components, and the discipline to reuse them</span></span>
        <span class="col-check"><span class="col-check__tick">{icon('check', group='ui')}</span>
          <span>Accessibility as a default, not an audit bolted on at the end</span></span>
        <span class="col-check"><span class="col-check__tick">{icon('check', group='ui')}</span>
          <span>As little JavaScript as a page can get away with</span></span>
      </div>
    </div>

    <figure class="pullquote u-mt-10">
      <p class="pullquote__text">A design system is not a component library. It is
        the set of arguments you have already had, written down so you never have
        to have them again.</p>
      <figcaption class="pullquote__cite">From the introduction to the docs</figcaption>
    </figure>

    <div class="u-mt-10">
      {sec('What the desk looks like', 'The editor, and the one command that '
           'rebuilds all 138 pages.')}
      <div class="grid-2">
        {win_code('shell.py', [
            '<span class="tok-com"># the head, navbar and footer every route shares</span>',
            '<span class="tok-key">def</span> <span class="tok-fn">page</span>('
            '<span class="tok-var">out_dir</span>, <span class="tok-var">name</span>, '
            '<span class="tok-var">title</span>, <span class="tok-var">body</span>):',
            '    <span class="tok-var">doc</span> = <span class="tok-var">HEAD</span>'
            '.<span class="tok-fn">format</span>(...) + <span class="tok-var">body</span>',
            '    (<span class="tok-fn">Path</span>(<span class="tok-var">out_dir</span>) / '
            '<span class="tok-var">name</span>).<span class="tok-fn">write_text</span>('
            '<span class="tok-var">doc</span>)',
        ], tab='collection/shell.py')}
        {win_term([(True, 'npm run build'),
                   (False, '<span class="tok-com">postcss src/index.css → dist/creator.css</span>'),
                   (False, '<span class="tok-str">built 138 pages</span>'),
                   (True, '')])}
      </div>
    </div>
  </div>

  <div class="container section-sm">
    {cta_sponsor('This is free and MIT-licensed.',
        kicker=f'{icon("take")}Sponsor',
        actions='<a class="btn btn-secondary" href="https://github.com/sponsors/imswarnil" '
                'target="_blank" rel="noopener">Sponsor →</a>')}
  </div>'''
    return page(HERE, 'about.html', 'About — Swarnil Singhai',
                'Design systems, accessibility, and as little JavaScript as a page '
                'can get away with.', body, NAME, own_css='pages.css', current='about')


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
        <div class="u-mt-8">
          {sec('Or find me elsewhere')}
          {links_block(LINKS)}
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

def route_archive():
    years = ''.join(
        f'{sec(year)}<div class="col-order">' + ''.join(
            f'<a class="col-order__item" href="../{href}">'
            f'<span class="col-order__num"><span class="col-order__dot"></span></span>'
            f'<div class="col-order__body"><span class="col-order__title">{title}</span>'
            f'<div class="col-order__meta"><span>{when}</span></div></div></a>'
            for title, href, when in items) + '</div>'
        for year, items in ARCHIVE)
    body = f'''
  <div class="container section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./home.html">Home</a> <span>/</span> <span>Archive</span>
    </nav>
    {page_head('Everything, in order',
        'Every post, episode, issue and log entry, across every collection, '
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

    <div class="col-tags u-mt-6">
      <a class="col-tag" href="./archive.html" aria-current="page">Everything</a>
      {''.join(f'<a class="col-tag" href="../{slug}/index.html">{name}</a>'
               for name, slug, _, _ in COLLECTIONS[:6])}
    </div>

    <div class="u-mt-8">
      {stats([('273', 'Things published'), (f'{len(COLLECTIONS)}', 'Collections'),
              ('2019', 'Since')], bare=True)}
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
                'Every post, episode, issue and log entry, newest first.',
                body, NAME, own_css='pages.css', current='archive')


# ── Now ──────────────────────────────────────────────────────────────────────

def route_now():
    body = f'''
  <div class="container-narrow section-sm">
    <nav class="col-post__crumbs u-mb-6" aria-label="Breadcrumb">
      <a href="./home.html">Home</a> <span>/</span> <span>Now</span>
    </nav>
    <span class="t-slate-sm" style="color:var(--fg-faint)">Updated Jul 2026 ·
      what a <a href="https://nownownow.com" target="_blank" rel="noopener">now page</a> is</span>
    <h1 class="t-display-2 u-mt-3">What I'm doing now</h1>

    <!-- The one place a progress bar is honest: these are real, in-flight, and
         the number moves. .progress-labelled ships the label and value; nothing
         here is a fake loading state. -->
    <div class="u-mt-8">
      {sec('In flight')}
      {''.join(f'''<div class="progress-labelled u-mb-4">
        <span class="progress__label">{what}</span>
        <div class="progress"><div class="progress__bar" style="--value:{pct}%"></div></div>
        <span class="t-slate-sm" style="color:var(--fg-faint)">{note}</span>
      </div>''' for what, pct, note in [
          ('The pages collection', 90, 'home, about, archive, the legal pages'),
          ('Newsletter issue 42', 60, 'on grid-auto-rows: minmax(0, auto)'),
          ('npm package + Tailwind/SCSS builds', 35, 'the last roadmap item'),
      ])}
    </div>

    <div class="u-mt-8">
      {sec('What is actually running', 'The terminal, not a claim about it.')}
      {win_term([(True, 'npm run dev'),
                 (False, '<span class="tok-com">docs → http://localhost:8080</span>'),
                 (False, '<span class="tok-str">built 138 pages</span>'),
                 (True, 'git log --oneline -1'),
                 (False, '<span class="tok-num">70da94d</span> Promote the cinematic hero'),
                 (True, '')])}
    </div>

    <div class="u-mt-8">
      {alert('This page is updated by hand, roughly monthly. If the date above is '
             'stale, the work below probably shipped.', tone='warning', ico='search')}
    </div>

    <div class="content u-mt-10">
      <p>Mostly this: closing the gap between the collections that ship no CSS of
        their own and the ones that still owe the vocabulary something.</p>
      <h2>Building</h2>
      <p>The pages collection — home, about, archive, the legal pages nobody reads
        but every site needs anyway.</p>
      <h2>Writing</h2>
      <p>Issue 42 of the newsletter, on why <code>grid-auto-rows: minmax(0, auto)</code>
        fixes more layouts than any tutorial mentions.</p>
      <h2>Reading</h2>
      <p>Old CSS specs, mostly, looking for the one line that explains a behaviour
        everyone works around instead of naming.</p>
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

def route_welcome():
    # .hero-band — the inverse billboard, the third hero shape. A confirmation
    # is the one moment a page has earned a full-contrast band: it is saying one
    # thing, it is the only thing on the page, and there is nothing to browse.
    body = f'''
  <div class="container u-mt-6">
    <section class="hero hero-band hero-statement pattern pattern-rays pattern-lg">
      <span class="hero__eyebrow">{icon('check', group='ui')}Confirmed</span>
      <h1 class="hero__title">You're <em>in</em>.</h1>
      <p class="hero__lead">One email when something is worth forty-one issues of
        practice behind it. The first lands within the week — nothing before that.</p>
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
            ('The first issue, within the week', 'Then roughly fortnightly, when there is something.'),
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
                   ('Newsletter', 'The grid issue', 'Why grid-auto-rows fixes more than any tutorial mentions.', '../newsletter/post.html', 'mail'),
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
                'Confirmed — the first issue lands within the week.',
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

    <div class="u-mt-8">
      {stats([('9', 'Years'), ('3', 'Companies'), ('6', 'Certifications'),
              ('4', 'Languages')], bare=True)}
    </div>

    {summary_block('Swarnil Singhai', 'Senior Product Engineer',
        'I build design systems and the sites that run on them — tokens first, '
        'components second, and as little JavaScript as the page can get away with.',
        CONTACTS)}

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

        <section class="u-mt-10">
          {sec('Certifications')}
          {certifications_block(CERTIFICATIONS)}
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

        <div class="col-widget">
          <span class="col-widget__title">Languages</span>
          {languages_block(LANGUAGES)}
        </div>

        <div class="col-widget">
          <span class="col-widget__title">Links</span>
          {links_block(LINKS)}
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
            route_resume()]
    print('pages: ' + ', '.join(made))
