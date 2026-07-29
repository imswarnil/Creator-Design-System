# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning follows [SemVer](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **`scripts/audit-classes.py`** — the gap between the CSS and the markup, in
  both directions: classes the markup uses that the CSS never defines (should
  always be empty; `--strict` gates CI on it) and classes the CSS defines that
  no page uses (never empty, but a whole *family* at zero is a component nobody
  knows about). Both checks are grep; the value is in running them at all.
  Wired into `npm run audit:classes` and the CI workflow.
- **Six more `shell.py` helpers, all wrapping components that shipped unused** —
  `win_browser()`, `win_code()`, `win_term()` (the window chrome from
  `12-frame.css`, whose own header says "containers that say what a thing IS
  before you read it" — a design system that ships a browser mockup and never
  shows a page in one is leaving the obvious demo on the table), plus
  `marquee()`, `alert()` and `vf()`.
- **Many more variants per page.** Home now carries the marquee, a signal
  alert, a split hero with the docs running in a browser window, a terminal and
  an editor side by side, the collections grid, a cascading stats band, the
  viewfinder over a filmstrip, the newsletter CTA and the sponsor strip. About
  gains the editor + terminal pair; contact an info alert in the rail; now a
  terminal and a warning; welcome a success alert; archive a skeleton
  loading state; the legal pages a plain-English summary alert above the prose.
  Framework classes actually shipping went from 412 to 487.

### Fixed
- **Two "reuse before adding" violations, both mine.** The guides collection
  shipped a bespoke `.guide-cover` while `.book` / `.book__cover` /
  `.book-shelf` sat unused in `12-frame.css` — already carrying a spine, a page
  edge, and a shelf that tilts every second cover, with a doc comment naming
  *the guides* as what it was built for. Guides now uses the component and gets
  a real shelf; `guides.css` is down to the one thing that genuinely was new.
  Separately, every collection hand-rolled a two-line `.row-between` footer
  while the real `.footer` — brand column, link columns, sign-off row with the
  record dot — went unused, which meant the one place a sitemap gets to be
  exhaustive was a single sentence. `shell.FOOT` is now that component, so all
  twelve collections got a real footer at once.
- **The cinematic hero is a component now** — `.hero-band-full` (full viewport,
  full bleed, pulled up under the island nav) and `.hero-band__scan` (a film
  layer holding any `.pattern-scanline`, with an optional `data-ripple` that
  `nav.js` tracks the pointer through via `--mx`/`--my`). This shape existed
  before as ~40 lines of inline style and its own `<script>` inside
  `travel/build.py`, which meant no other page could have it. Travel now calls
  `shell.cine_hero()` like everyone else, and the homepage opens with it.
  JS writes two custom properties; every visual decision stays in CSS/SVG.
- **`shell.py` grows five helpers** — `page_head()`, `stats()`, `cta()`,
  `cta_sponsor()` and `cine_hero()`, because the sections they wrap were
  defined in `src/5-sections/` and reachable by nothing. Before this,
  **the entire `33-cta.css` file — five variants — was used by zero pages**,
  as were `.stat`/`.stats-bare`/`.stats-inverse`, `.page-head`, `.pullquote`,
  `.acc`/`.collapse`, `.progress-labelled` and `.frame-ink`. All now ship.
- **Each `_pages` route gets its own components** rather than a heading and a
  paragraph: home takes the cinematic hero + stats + newsletter CTA; about the
  split hero + framed portrait + bare stats + pull-quote + sponsor strip;
  contact a page head + two-column form with response times in the rail + a
  native-`<details>` FAQ; archive a search field + collection chips + totals;
  now the one honest progress bar; the legal pages a sticky TOC rail and a
  last-updated date; welcome the inverse billboard + a three-step "what happens
  next" + a start-here grid; résumé a page head with the download in it.

### Fixed
- **Two phantom classes removed.** `.quote` was used in five collections
  (blog, course, newsletter, travel, webseries) and **defined nowhere** — it
  only looked right because those blockquotes sit inside `.content`, which
  styles `blockquote` directly. Anyone copying that markup elsewhere got
  nothing. `.spec-table` in `collection/docs/` existed only in this repo's own
  `docs/preview.css`, so the reusable docs template rendered an unstyled table
  in any project that copied it; it now uses the framework's own `.table`.
- **Seven more collections** — newsletter (calendar-styled issue cards),
  projects (GitHub-style cards, a build-log timeline, and a shared-element
  hero that shrinks into a log entry on click via `view-transition-name`),
  videos/YouTube (channel hero, upload list, chaptered single-video page and
  a "products I use" block), guides (book-cover cards with a colour-blend
  cover via `ph(..., blend=True)`, and a `.stepper` between steps), prompts,
  snippets and products-i-use. Each reuses an existing `#tag`-scoped card
  variant from `23-collection.css` rather than inventing a new one.
- **`collection/_pages/`** — home, about, contact, archive, now, terms,
  privacy and welcome-subscriber, plus the résumé moved in from its own
  folder. The homepage's collections grid is the one place every collection
  is listed, so the nav bar does not grow a thirteenth link.
- **`collection/docs/`** — a reusable three-column docs template
  (`/docs`, a section, a post, a component reference) for using this system
  on someone else's own project, distinct from this repo's own
  `docs/_build` generator.
- **`/css`, `/tailwind`, `/scss`** — short entry routes into the Usage
  page's per-flavour sections, so "how do I use this with X" has a real URL
  instead of a scroll position.
- Two new page-transition flavours completed from the original spec
  (`static` for Videos, reusing the keyframe that already existed unused)
  and one built new (`turn`, a page-turn for Guides), plus a shared
  `pagination()` helper in `collection/shell.py` used by every collection
  index.

### Fixed
- Every inline `<style>` block actually shipped in a live page (the docs
  landing page, the introduction's animated illustration, the icon-set
  page's dark-mode filter, and the broadcast fragment previews) moved into
  a real, linked stylesheet — `docs/preview.css` or a generated
  `broadcast-frag/*.css` file. The system's own site now follows the same
  "CSS lives in the CSS folder" rule its docs already asked everyone else to.
- The site-wide "Swarnil" logo linked to the docs site instead of the actual
  homepage — every collection now points it at `collection/_pages/home.html`.

- **The course collection** — `/course`, a track, a topic, the course page and
  the lesson player, in `collection/course/`. A course is the collection's
  *series* route (a first lesson, a last one, a progress through it) and a
  track is its *group*; getting those the wrong way round is what produces a
  course page with a grid of lessons on it.
- **Five sections for a post whose body is a video** — `.col-stage`,
  `.col-stagebar`, `.col-playlist`, `.col-transcript` and `.col-panel`, plus
  `.col-checks`, `.col-offer`, `.col-files`, `.col-keys`, `.col-note` and
  `.col-resume`. Shared rather than course-shaped, because a podcast season and
  a video series want every one of them. `.col-playlist` **is** `.curriculum`
  with a body that scrolls — a contents list should not become a different
  component the moment it moves next to a video.
- **`collection.js` grows two modules** — the panels (tabs that stack under
  their own headings until the script sets `data-tabs="ready"`) and the lesson
  player (mark complete, live module and course counts, and the `N` / `P` / `M`
  shortcuts the page advertises). Both only set attributes the stylesheet
  already understands, and both degrade to a readable page.
- **Course's own four** — `.crs-level` (three bars, because "intermediate"
  means nothing until you have seen the other two), `.crs-quiz`, `.crs-cert`
  and the syllabus scene.
- **A style per collection** — `.nav-video`, `.nav-blog`, `.nav-course-bar`,
  `.nav-shop`, `.nav-trip`, `.nav-docs-bar`. Each sets defaults only, written in
  six variables it also yields to: `--bar-bg`, `--bar-fg`, `--bar-line`,
  `--bar-radius`, `--bar-h`, `--bar-blur`.
- **`.nav-over`** — a bar that sits *over* media rather than on the page: no
  island, no plate, a gradient carrying legibility on any frame, and ink once
  the reader scrolls past the film. Paired with `.nav-over__media`.
- **The navbar builder now controls everything** — collection, position
  (including over-media), mark and link alignment, width, height, radius,
  border/shadow/blur, theme, accent, background, active-link treatment, the
  brand word and link labels, which actions the bar carries, dropdown trigger,
  burger style, mobile opening, and the progress line.
- **Navbar, final pass.** Shell behaviours (`.nav-shell-fixed`,
  `.nav-shell-auto` hide-on-scroll-down, `.nav-shell-morph` full-bleed →
  island); the hairline as a progress bar (`.nav-progress` + `--progress`);
  `.nav-bar-center`, `.nav-bar-inverse`, `.nav-bar-compact`; the record → play
  burger (`.nav-burger-rec`); hover-intent and self-sizing dropdowns
  (`.nav-menu-hover`, `.nav-menu-grow`) with a second level (`.nav-sub-menu`);
  two more ways to open on a phone (`.nav-sheet-drop`, and `.nav-panel`, where
  the island grows into the menu); action chips, a CTA slot and a newsletter
  that unfolds from its own icon (`.nav-icons`, `.nav-form`); the submenu's own
  burger and collection index on phones (`.nav-sub__more`, `.nav-sheet-index`)
  plus a way to hide the row entirely.
- **`src/nav.js`** — optional, dependency-free. Sets `data-scrolled`,
  `data-dir`, `data-open` and `data-sub`; everything visible stays in CSS.
- Links now lead the bar when there is no mark, and follow it when there is
  (`:has()`), so a bar without a logo never opens with a hole.
- JSON-LD on every docs page: `SiteNavigationElement` for the site menu and a
  `BreadcrumbList` for the current page.
- **Syntax highlighter** (`src/highlight.js`) — the system's own, dependency-free.
  Five languages (html · css · js · json · bash) emitting the token roles the
  CSS already ships. `data-play` settles a block in with one short fade on
  first view, and is skipped under `prefers-reduced-motion`.
- Token roles for markup and CSS: `.tok-tag`, `.tok-attr`, `.tok-prop`,
  `.tok-sel`, `.tok-var`, `.tok-punc`, in both themes.

### Removed
- **The submenu row.** `.nav-stack`, `.nav-sub`, `.nav-context*`, the mobile
  collection index (`.nav-sheet-index`) and the row's hide/show mechanism are
  gone. The navbar is one row again; what a collection needs to say, it says in
  its own style rather than in a second bar underneath.
- **The ten `nav-v-*` / `nav-s-*` shape variants.** A bar's shape is decided
  once in the design; where it goes when the reader scrolls is the decision
  worth a variant. Four positions remain — island, fixed, island-on-scroll,
  fixed-on-scroll — and the skins that were pretending to be variants are the
  things they always were: `.nav-bar-center`, `.nav-bar-inverse`,
  `.nav-bar-compact`, `.nav-shell-flush`, `.nav-shell-full`, `.nav-ghost`.
  `.nav-v-stacked` and `.nav-v-bordered` are gone outright.

### Changed
- **Navbar — context is now a submenu row, not a replacement bar.** The site
  menu stays and the contextual chrome appears beneath it inside
  `.nav-stack`, so the way out never disappears. Reverses the old house rule
  ("contextual bars replace the site bar, never stack on top of it").
- **Navbar — one design instead of eight skins.** `.nav-course`, `.nav-guide`,
  `.nav-lesson`, `.nav-episode`, `.nav-video`, `.nav-trip`, `.nav-docs` and
  `.nav-shop` are removed in favour of knobs on `.nav-sub`: `data-tone`
  (paper · ink · accent), `data-density`, `data-mark`, `--value` and
  `--pos-prefix`. A course and a trip differ in their words, not their CSS.
  New slot classes: `.nav-context__back`, `__kind`, `__actions`.
- Navbar docs gained a live playground: set every knob, watch the row change,
  copy the markup it prints.
- **Docs layout** — the site bar now runs the full width, the per-page contents
  moved out of the left sidebar into a sticky right rail beside the content,
  and a sponsor card sits under it. The left sidebar is pages only.
- Docs code views print formatted, highlighted, paste-ready markup, and a tile
  that is already a code block no longer offers a Preview/Code toggle that
  would switch between two identical views.
- The navbar playground gained the main row: logo, social icons, newsletter,
  CTA, burger and the progress line.
- **Landing hero** is square and cycles through what the frame holds — a 16:9
  video, a 9:16 reel, a page being written, a screen of code. The viewfinder
  chrome never moves; only the subject does.
- The project's own pages (showcase · templates · sponsor) left the docs
  sidebar; they are reached from the site bar.

### Fixed
- **`hidden` means hidden.** The browser's rule for the attribute lives in the
  UA sheet, so every component that set a display — `.btn`, `.card` — silently
  beat it, and `<button class="btn" hidden>` stayed on screen. One line in
  `00-reset.css`, and the one place `!important` is right: the attribute is an
  assertion about the document, not a style. Visible symptom: the collections'
  "Clear filters" button showed with nothing filtered.
- Docs `@import`s inside `src/*/index.css` are stamped with the build version
  when mirrored into `docs/`. Only the parent stylesheet carried `?v=`, so
  browsers served stale layer files behind a freshly-versioned index and a
  rebuild appeared to do nothing.

## [0.1.0] — 2026-07-27

First public skeleton.

### Added
- **Foundation** — colour (ink · paper · mist · line · silver + the record-red),
  typography, spacing & radius, elevation, motion, layout, patterns, logo,
  icons, shape, cutouts, frames, accessibility.
- **Elements** — text, badge, table, indicator, syntax highlighting with copy.
- **Components** — buttons, forms, cards, collection cards, navigation,
  feedback, media, composites (syllabus · episode panel · build log ·
  itinerary), disclosure, overlays, long-form content, editorial, navbar.
- **Sections** — page header, hero, stats, CTA, footer.
- **Utilities** — `u-`-prefixed helpers off every token ladder.
- **Broadcast** — YouTube and Instagram export canvases.
- **Icons** — 27 SVGs in four groups, `currentColor` throughout.
- Generated documentation site with search, a components explorer,
  showcase and templates pages.

[Unreleased]: https://github.com/imswarnil/Creator-Design-System/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/imswarnil/Creator-Design-System/releases/tag/v0.1.0
