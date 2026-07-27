# Working in this repository

Instructions for AI coding agents. Humans: this is a condensed version of
[CONTRIBUTING.md](CONTRIBUTING.md) and the file headers in `src/`.

Creator Design System ("Frame & Signal") is a token-first, dependency-free CSS
design system for creators. Plain CSS custom properties and classes — no
framework, no runtime, no build step required to *use* it.

## Commands

```bash
npm install
npm run dev     # build the docs, serve at http://localhost:8080
npm run build   # dist/creator.css + dist/creator.min.css + docs
npm run docs    # regenerate docs/*.html only
npm run lint    # stylelint over src/**/*.css — must pass, it is clean
npm run size    # gzipped size of the minified bundle
```

`python3 media/build.py` redraws the README specimen SVGs from token values.

## Rules that will bite you

1. **Never hand-edit `docs/*.html`.** Every one of the 128 pages is generated.
   Edit `docs/_build/content_*.py`, then run `npm run docs`. CI fails the build
   if committed HTML differs from a fresh generation.
2. **Never edit `src/` to customise the system.** Overriding a token *after*
   the import is the entire customisation API. If a change cannot be expressed
   as a token, that is a design question, not a patch.
3. **`docs/src`, `docs/icons` and `docs/dist` are gitignored mirrors** that the
   build regenerates. GitHub Pages therefore cannot serve `docs/` off a branch —
   deployment must stay on the Actions workflow that builds first.
4. **Import order matters.** A layer may only depend on lower-numbered layers.
5. **No AI attribution in commits.** No `Co-Authored-By`, no "Generated with"
   line, no AI listed as contributor. This is published as the owner's own work.

## Layout

| Path | What it is |
| --- | --- |
| `src/1-foundation` … `src/6-utilities` | the system; hand-authored CSS |
| `src/highlight.js`, `src/nav.js` | optional, dependency-free, additive |
| `dist/` | generated bundles, committed so the CDN has them |
| `docs/_build/*.py` | the docs generator — **the source of the docs** |
| `docs/*.html` | generated output, committed so Pages can serve it |
| `docs/preview.css`, `docs/preview.js` | docs chrome only, ships to nobody |
| `media/build.py` | generates the README specimen SVGs from tokens |

## House rules of the CSS

- **Active state is a dot or a 2px rule — never a filled pill.**
- **State lives in ARIA**: style `[aria-current]`, `[aria-expanded]`,
  `[data-*]`. Never invent an `.active` class that can disagree with the
  accessibility tree.
- **The platform first**: `<details>`, `<dialog>`, the Popover API, native
  inputs. Keyboard and Escape should come free rather than be rebuilt.
- **Motion is honest**: under 200ms for feedback, one property at a time, and
  everything off under `prefers-reduced-motion`. The finished state is the
  resting state — nothing may be unreachable if an animation never runs.
- **Two-tier tokens**: primitives (`--ink-500`, `--signal-500`) are referenced
  by semantic tokens (`--fg-muted`, `--accent`). Components read the semantic
  tier only, which is why one override rebrands everything.
- **One accent, rationed.** The system is almost monochrome so that a single
  colour can carry meaning. Adding a second hue is a change to the argument of
  the system, not a tweak.

## JavaScript

`src/nav.js` and `src/highlight.js` are optional. Both only ever set attributes
the stylesheet already understands (`data-scrolled`, `data-dir`, `data-open`),
so CSS stays the single description of how anything looks. Without them the
system degrades to sticky bars, click-only dropdowns and uncoloured code —
nothing breaks. Keep it that way.

## When editing CSS

- Match the surrounding density: a rule whose body is one or two declarations
  stays on one line. `.stylelintrc.json` encodes this.
- Comment *why*, not what. The file headers explain the argument of each layer;
  keep that voice.
- Run `npm run lint` before finishing. It passes at zero errors today.
