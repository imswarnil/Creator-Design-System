"""The Usage page — how to actually put this into a project.

Its own module because it is the page people arrive at with a real question:
"I have a site, how do I use this?" It answers that for plain CSS, Tailwind,
SCSS, your own CSS and any framework, and ends with the four things that
account for nearly every "it looks wrong".

Code blocks here are plain text. highlight.js colours them at run time from the
caption, so nothing has to be hand-tokenised and the samples stay copy-pasteable
and diffable.
"""
import html

from common import tile, sec, END, ct

PAGES = {}


def code(lang, text, note=''):
    body = html.escape(text.strip('\n'))
    fig = ('<figure class="codebox codebox-light u-m-0"><figcaption class="codebox__head">'
           f'<span class="codebox__lang">{lang}</span>'
           '<button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>'
           f'<pre class="codebox__pre"><code>{body}</code></pre></figure>')
    return tile(fig, note) if note else f'\t\t<div class="u-mb-6">{fig}</div>'


def p(text):
    return f'\t\t<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">{text}</p>'


u = ''

# ── 1 · getting it ──────────────────────────────────────────────────────────
u += sec('getting-it', 'Getting it',
         'Two ways in today, and a third once the package is published. They give you the '
         'same CSS.')
u += code('html',
          '<link rel="stylesheet"\n'
          '      href="https://cdn.jsdelivr.net/gh/imswarnil/Creator-Design-System@main'
          '/dist/creator.min.css">',
          'the CDN — no install, no build, nothing to configure. Pin '
          '<code class="t-code">@main</code> to a tag for production')
u += p('Or download <code class="t-code">dist/creator.css</code> from the '
       '<a href="https://github.com/imswarnil/Creator-Design-System" rel="noopener">'
       'repository</a> and link it. That is the whole installation — no init step, no config '
       'file, no runtime.')
u += code('bash', 'npm install creator-design-system',
          'coming with the first tagged release; the examples below use these paths')
u += p('The npm package is not published yet, so that command does not work today. Everything '
       'below is written against the package paths it will use, because they are the paths the '
       '<code class="t-code">exports</code> map in '
       '<code class="t-code">package.json</code> already declares — the CDN link above gives '
       'you the same stylesheet in the meantime.')
u += END

# ── 2 · first page ──────────────────────────────────────────────────────────
FIRST_PAGE = """
<!doctype html>
<html lang="en" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>My site</title>

  <!-- 1 - the type the system expects -->
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">

  <!-- 2 - the system -->
  <link rel="stylesheet" href="node_modules/creator-design-system/dist/creator.css">

  <!-- 3 - your overrides, always AFTER the system -->
  <style>
    :root {
      --accent: #f04e2e;
      --font-display: 'Space Grotesk', sans-serif;
    }
  </style>
</head>
<body>
  <header class="nav-shell">
    <nav class="nav-bar" aria-label="Main">
      <a class="logo logo-sm" href="/">Your name</a>
      <div class="nav-links">
        <a class="nav-link" href="/watch/" aria-current="page">Watch</a>
        <a class="nav-link" href="/learn/">Learn</a>
      </div>
      <div class="nav-actions">
        <a class="btn btn-primary btn-sm btn-pill" href="/subscribe/">Subscribe</a>
      </div>
    </nav>
  </header>

  <main class="container section">
    <h1 class="t-display-2">A page, already styled</h1>
    <p class="t-lead u-mt-5">Every class above exists. Nothing was invented.</p>

    <div class="deck deck-sm u-mt-8">
      <article class="card">
        <div class="card__body">
          <p class="card__meta">Build log - 12 min</p>
          <h2 class="card__title"><a class="card__link" href="/post/">A post</a></h2>
          <p class="card__excerpt">The card is the same object in every collection.</p>
        </div>
      </article>
    </div>
  </main>
</body>
</html>
"""

u += sec('first-page', 'Your first page',
         'A complete document — nothing omitted. Copy it into an .html file, open it, and the '
         'system is running.')
u += code('html', FIRST_PAGE,
          'no build step, no bundler, no framework: this is the whole integration')
u += p('The fonts are the only external dependency, and even they are a choice. Point '
       '<code class="t-code">--font-display</code>, <code class="t-code">--font-body</code> and '
       '<code class="t-code">--font-slate</code> at anything you like and drop the '
       '<code class="t-code">&lt;link&gt;</code>.')
u += END

# ── 3 · layers ──────────────────────────────────────────────────────────────
LAYERS = """
/* everything, in one line */
@import "creator-design-system";

/* or floor by floor - later layers need the earlier ones */
@import "creator-design-system/foundation";   /* tokens only                */
@import "creator-design-system/elements";     /* + text, badge, table, code */
@import "creator-design-system/components";   /* + buttons ... navbar       */
@import "creator-design-system/sections";     /* + hero, stats, CTA, footer */
@import "creator-design-system/utilities";    /* + u- helpers               */

/* not included by default: it ships to YouTube and Instagram, not a website */
@import "creator-design-system/broadcast";
"""

u += sec('layers', 'Taking less than all of it',
         'Import a layer directly when you do not want the whole system. Each layer needs only '
         'the ones below it, so you can stop at any floor.')
u += code('css', LAYERS,
          'foundation alone is already usable — it is where every decision lives')
u += END

# ── 4 · the token contract ──────────────────────────────────────────────────
TOKENS = """
@import "creator-design-system";

:root {
  --accent:        #6d4aff;                    /* your signal colour */
  --font-display:  'Clash Display', sans-serif;
  --radius-card:   1.25rem;
}
"""

u += sec('tokens', 'Customising — the token contract',
         'Never edit the source. Override tokens after the import; every component reads them '
         'live, in both themes. This is the entire customisation API.')
u += code('css', TOKENS,
          'three lines rebrands the site, the buttons, the cards and the thumbnails')
u += p('Tokens come in two tiers, and that distinction is the whole reason one override reaches '
       'everything. <b>Primitives</b> are the ladders — <code class="t-code">--ink-500</code>, '
       '<code class="t-code">--signal-500</code>, <code class="t-code">--space-4</code>. '
       '<b>Semantic tokens</b> name a job — <code class="t-code">--fg-muted</code>, '
       '<code class="t-code">--accent</code>, <code class="t-code">--line-default</code> — and '
       'point at a primitive. Components read the semantic tier only, so re-pointing one '
       'semantic token changes every component that meant that thing.')
u += ct([
    ('--accent', 'the one rationed colour: buttons, active states, the record light'),
    ('--bg-canvas · --bg-surface · --bg-sunken', 'the three background depths'),
    ('--fg-default · --fg-muted · --fg-subtle · --fg-faint', 'the text ladder, strongest first'),
    ('--line-subtle · --line-default · --line-strong', 'the three hairline weights'),
    ('--font-display · --font-body · --font-slate', 'headings · reading · labels and code'),
    ('--space-1 … --space-16', 'the spacing ladder — nothing invents a gap outside it'),
    ('--radius-sm … --radius-pill', 'the corner ladder, plus <code class="t-code">--radius-card</code>'),
    ('--dur-1 … --dur-5 · --ease-out', 'motion: durations and curves'),
], head=('Token', 'What it decides'))
u += p('The full list lives on <a href="./f-color.html">Color</a>, '
       '<a href="./f-type.html">Typography</a> and <a href="./f-space.html">Spacing</a> — or in '
       'one read at <a href="./llms-full.txt">llms-full.txt</a>.')
u += END

# ── 5 · dark mode ───────────────────────────────────────────────────────────
THEME_JS = """
// Follow the OS, remember a choice, and set it before first paint so the page
// never flashes the wrong theme.
(function () {
  var saved = localStorage.getItem('theme');
  var dark = saved ? saved === 'dark'
                   : matchMedia('(prefers-color-scheme: dark)').matches;
  document.documentElement.dataset.theme = dark ? 'dark' : 'light';
})();
"""

u += sec('dark', 'Light and dark',
         'Both themes come from the same variables. Nothing is duplicated, and no component '
         'knows which theme it is in.')
u += code('html', '<html data-theme="dark">', 'the switch — that is all the system needs')
u += code('js', THEME_JS, 'inline in &lt;head&gt;, above the stylesheet link')
u += END

# ── 6 · tailwind ────────────────────────────────────────────────────────────
TW4 = """
/* app.css - Tailwind 4 */
@import "tailwindcss";
@import "creator-design-system";        /* after Tailwind, always */

/* Hand the tokens to Tailwind so bg-accent, text-muted and friends exist.
   `inline` is the important word: it tells Tailwind these values reference
   other custom properties, which keeps modifiers like bg-accent/50 working. */
@theme inline {
  --color-accent:  var(--accent);
  --color-canvas:  var(--bg-canvas);
  --color-surface: var(--bg-surface);
  --color-ink:     var(--fg-default);
  --color-muted:   var(--fg-muted);
  --radius-card:   var(--radius-card);
}
"""

TW3 = """
// tailwind.config.js - Tailwind 3
module.exports = {
  theme: {
    extend: {
      colors: {
        accent:  'var(--accent)',
        canvas:  'var(--bg-canvas)',
        surface: 'var(--bg-surface)',
        ink:     'var(--fg-default)',
        muted:   'var(--fg-muted)',
      },
      borderRadius: { card: 'var(--radius-card)' },
    },
  },
  // Optional: this system brings its own reset, so you may not want two.
  corePlugins: { preflight: false },
};
"""

TW_USE = """
<article class="card mt-8 lg:mt-12">
  <div class="card__body">
    <h2 class="card__title">Component from the system</h2>
    <p class="text-muted">Spacing and layout from Tailwind</p>
  </div>
</article>

<!-- change --accent once and both of these follow -->
<button class="btn btn-primary">System button</button>
<span class="bg-accent text-white px-3 py-1 rounded-full">Tailwind chip</span>
"""

u += sec('tailwind', 'With Tailwind',
         'The two do different jobs and compose well: Tailwind gives you utilities, this gives '
         'you decided components. The u- prefix means there are no class collisions.')
u += p('<b>Order matters more than anything else here.</b> Both ship a reset — Tailwind calls '
       'its one Preflight — and the last one loaded wins. Import Tailwind first, so this '
       'system’s reset and components sit on top of it.')
u += code('css', TW4, 'Tailwind 4 — one import each, then map the tokens')
u += code('js', TW3, 'Tailwind 3 — the same idea, in the config file')
u += p('Now both vocabularies work on one element, and they agree by construction, because '
       'they are reading the same variable:')
u += code('html', TW_USE,
          'no collisions — every helper here is <b>u-</b> prefixed and every component is a noun')
u += ct([
    ('Use the system for', 'components with parts and states — cards, navbar, forms, buttons, '
                           'sections. The things where the decisions matter.'),
    ('Use Tailwind for', 'one-off layout on a page: grid, flex, margins, responsive tweaks.'),
    ('Do not', 'rebuild a card out of utilities. That is how two pages stop matching.'),
], head=('Which one', 'For what'))
u += p('If you would rather not load two resets at all: import '
       '<code class="t-code">creator-design-system/foundation</code> and skip '
       '<code class="t-code">00-reset.css</code>, or turn Preflight off as above. Either is '
       'fine. Loading both in the wrong order is not.')
u += END

# ── 7 · scss ────────────────────────────────────────────────────────────────
SCSS = """
// main.scss
@use "creator-design-system/dist/creator.css";

.promo {
  // SCSS variables are compile-time; the tokens are not, and that is the point
  padding: var(--space-6);
  border-radius: var(--radius-card);
  background: var(--bg-sunken);
}
"""

u += sec('scss', 'With SCSS', 'Nothing special is required, and one thing is worth knowing.')
u += code('scss', SCSS,
          'the tokens stay custom properties, so runtime theming survives compilation')
u += p('Resist copying tokens into SCSS variables. A SCSS variable is resolved when you build; '
       'a custom property is resolved when the page runs. Only the second can flip to dark mode, '
       'or be re-pointed by a reader setting, without a rebuild.')
u += END

# ── 8 · your own CSS ────────────────────────────────────────────────────────
OWN = """
@import "creator-design-system";

/* Your component. Written in the system's tokens, so it inherits the theme,
   dark mode, the motion rules and any future rebrand - for free, forever. */
.testimonial {
  display: grid;
  gap: var(--space-4);
  padding: var(--space-6);
  background: var(--bg-surface);
  border: var(--border-hair) solid var(--line-default);
  border-radius: var(--radius-card);
  box-shadow: var(--shadow-1);
}

.testimonial__quote {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  line-height: var(--leading-snug);
  color: var(--fg-default);
  text-wrap: balance;
}

.testimonial__who {
  font-family: var(--font-slate);
  font-size: var(--text-2xs);
  letter-spacing: var(--tracking-slate);
  text-transform: uppercase;
  color: var(--fg-faint);
}

/* State goes in ARIA, not in a class the accessibility tree cannot see. */
.testimonial[aria-current] { border-color: var(--accent); }
"""

u += sec('own-css', 'With your own CSS',
         'The system is meant to be built on. There is a right way to add to it, and it is the '
         'same way the system adds to itself.')
u += code('css', OWN,
          'a new component that behaves like a native one, because it reads the same variables')
u += ct([
    ('Do', 'write new components in tokens — <code class="t-code">var(--space-4)</code>, never '
           '<code class="t-code">16px</code>'),
    ('Do', 'follow the naming: <code class="t-code">.block</code>, '
           '<code class="t-code">.block__part</code>, <code class="t-code">.block-variant</code>'),
    ('Do', 'style from ARIA — <code class="t-code">[aria-current]</code>, '
           '<code class="t-code">[aria-expanded]</code>, <code class="t-code">[data-*]</code>'),
    ('Don’t', 'edit anything inside <code class="t-code">src/</code> — the next update '
              'overwrites it'),
    ('Don’t', 'add a second accent hue; the palette is closed so one colour can mean something'),
    ('Don’t', 'invent an <code class="t-code">.active</code> class. It can disagree with the '
              'accessibility tree, and then the two of them tell different people different '
              'things'),
], head=('', 'Extending the system'))
u += END

# ── 9 · frameworks ──────────────────────────────────────────────────────────
u += sec('frameworks', 'In a framework', 'It is a stylesheet, so it goes where stylesheets go.')
u += ct([
    ('React · Next · Vue', 'import the CSS once at the app root, then use '
                           '<code class="t-code">className="card"</code> as normal. No provider, '
                           'no theme object, no runtime'),
    ('Astro · 11ty · Hugo', 'link it in the base layout'),
    ('Ghost', 'link it in <code class="t-code">default.hbs</code> — the collection cards were '
              'designed against <code class="t-code">routes.yaml</code>'),
    ('Svelte', 'import in the root component, or link it in '
               '<code class="t-code">app.html</code>'),
], head=('Stack', 'How'))
u += p('The two optional scripts — <code class="t-code">nav.js</code> and '
       '<code class="t-code">highlight.js</code> — are plain, framework-free and additive. '
       'Without them you get sticky bars, click-only dropdowns and uncoloured code. Nothing '
       'breaks.')
u += END

# ── 10 · reading the names ──────────────────────────────────────────────────
u += sec('names', 'Reading the class names',
         'The shape of a name tells you what kind of thing it is, so you can guess correctly.')
u += ct([
    ('.card', 'a component — a noun, on its own'),
    ('.card__title', 'a part of it — two underscores'),
    ('.card-inverse', 'a variant of it — one hyphen'),
    ('.btn-primary · .btn-sm', 'intent and size on the same component'),
    ('.u-mt-6 · .u-fg-subtle', 'a utility — always <code class="t-code">u-</code> prefixed, '
                               'always one job'),
    ('.t-display-1 · .t-lead', 'a type role, not a size'),
    ('[aria-current] · [aria-expanded]', 'state — an attribute, never a class'),
], head=('Shape', 'Means'))
u += END

# ── 11 · when it goes wrong ─────────────────────────────────────────────────
u += sec('wrong', 'When it looks wrong', 'Five things account for nearly all of it.')
u += ct([
    ('Everything is unstyled', 'the class does not exist. Check it against '
                               '<a href="./llms-full.txt">llms-full.txt</a> — nothing in this '
                               'system is invented, so a name either is or is not real'),
    ('Overrides do nothing', 'they are above the import. Tokens must be set <em>after</em> the '
                             'system loads'),
    ('The type looks wrong', 'the fonts are not loaded. Add the '
                             '<code class="t-code">&lt;link&gt;</code>, or re-point '
                             '<code class="t-code">--font-*</code> at what you do have'),
    ('Tailwind flattened it', 'Preflight loaded last. Import Tailwind first, or turn Preflight '
                              'off'),
    ('Dark mode does nothing', '<code class="t-code">data-theme</code> is missing from '
                               '<code class="t-code">&lt;html&gt;</code> — it does not go on '
                               '<code class="t-code">&lt;body&gt;</code>'),
], head=('Symptom', 'Almost always'))
u += END


PAGES['usage'] = ('Usage — CSS · SCSS · Tailwind',
    'How to actually use this: a complete first page, the token contract, and how it composes '
    'with Tailwind, SCSS, your own CSS and any framework — plus what to check when it looks '
    'wrong.',
    u)
