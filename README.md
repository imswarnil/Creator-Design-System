<div align="center">

# Creator Design System

**Frame & Signal** — a token-first, dependency-free CSS design system
for creators building their own site.

Almost monochrome, so that one colour can mean something.

[Documentation](https://swarnil.github.io/Creator-Design-System/) ·
[Components](https://swarnil.github.io/Creator-Design-System/components.html) ·
[Showcase](https://swarnil.github.io/Creator-Design-System/showcase.html) ·
[Templates](https://swarnil.github.io/Creator-Design-System/templates.html) ·
[Sponsor](https://github.com/sponsors/swarnil)

</div>

---

## Why

Creators publish in more shapes than anyone: posts, videos, courses, series,
products, trips. Each shape pulls the design somewhere else — the video page
wants Netflix, the course page wants Udemy, the blog wants Medium. Copy all
three and the site becomes a mall.

This system settles the argument once, in tokens, and then reuses the answer
everywhere — including the YouTube thumbnails and the Instagram posts.

- **Plain CSS.** No framework, no build step required, no runtime.
- **Two-tier tokens.** Change three variables, rebrand the whole site.
- **Light & dark**, from the same variables.
- **State lives in ARIA**, so styling and the accessibility tree can't disagree.
- **The platform first** — `<details>`, `<dialog>`, the Popover API, native inputs.

## Install

```bash
npm install creator-design-system
```

```css
@import "creator-design-system";
```

Or take one layer at a time:

```css
@import "creator-design-system/foundation";   /* tokens only            */
@import "creator-design-system/elements";
@import "creator-design-system/components";
@import "creator-design-system/sections";
@import "creator-design-system/utilities";
@import "creator-design-system/broadcast";    /* YouTube / social art   */
```

### CDN — no build at all

```html
<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/creator-design-system@0/dist/creator.min.css">
```

### Download

Grab `dist/creator.css` from a [release](https://github.com/swarnil/Creator-Design-System/releases)
and link it. That is the whole installation.

## Make it yours

Never edit the source. Override tokens *after* the import — every component
reads them live, in both themes. This is the entire customization API:

```css
:root {
  --accent: #6d4aff;                          /* your signal colour */
  --font-display: 'Clash Display', sans-serif;
  --radius-card: 1.25rem;
}
```

Dark mode rides `data-theme="light|dark"` on `<html>`.

## Works with your stack

| Stack | How |
| --- | --- |
| Plain CSS | link `dist/creator.css`, done |
| SCSS | `@use` the same files; tokens are CSS custom properties, so runtime theming survives |
| Tailwind | keep the component classes and map the tokens into `theme.extend` — the `u-` prefix means zero collisions |
| Ghost / Astro / 11ty | it is just a stylesheet |

## Layers

| Layer | Holds |
| --- | --- |
| `1-foundation` | tokens: colour, type, space, elevation, motion, layout, patterns, logo, icons, shape, cutouts, frames |
| `2-elements` | single ideas: text, badge, table, indicator, syntax |
| `3-components` | things with parts and states: buttons → overlays → navbar → composites |
| `4-broadcast` | export canvases for YouTube and Instagram |
| `5-sections` | full-width bands: page header, hero, stats, CTA, footer |
| `6-utilities` | `u-`-prefixed single-purpose classes |

## Develop

```bash
npm install
npm run dev     # builds the docs and serves them at http://localhost:8080
npm run build   # dist/creator.css + dist/creator.min.css + docs
npm run lint
```

The docs are generated: edit `docs/_build/content_*.py`, then `npm run docs`.
Never edit the generated `docs/*.html` by hand.

## Contributing

Issues and pull requests are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).
Adding your site to the [Showcase](showcase/README.md) is one small file.

## Sponsor

This is free and MIT-licensed. If it saved you a weekend,
[sponsoring](https://github.com/sponsors/swarnil) keeps it maintained.

## Licence

[MIT](LICENSE) © Swarnil Singhai
