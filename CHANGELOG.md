# Changelog

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning follows [SemVer](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
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
