# Contributing

Thanks for being here. This system has strong opinions, and they exist so the
whole thing stays coherent — a contribution that respects them is much easier
to merge than a clever one that doesn't.

## The rules a change must keep

1. **Tokens before templates.** Every value is a `var()` off a ladder. No raw
   hex, no magic pixel numbers. If a component needs a value that isn't on a
   ladder, fix the ladder.
2. **State lives in ARIA.** Active, selected, pressed, current, done — use
   `aria-current`, `aria-selected`, `aria-pressed`, `[data-done]`. Never an
   `.active` class.
3. **The platform first.** `<details>`, `<dialog>`, the Popover API and native
   inputs before any JavaScript.
4. **Motion is honest.** Interaction feedback under 200ms, one property, and
   everything degrades under `prefers-reduced-motion`.
5. **Both themes.** Anything you add must be checked in light *and* dark.
6. **The rules of one.** One signal dot per surface, one accent word per
   headline, one inverse band per view, one ask per page.

## Getting set up

```bash
git clone https://github.com/imswarnil/Creator-Design-System
cd Creator-Design-System
npm install
npm run dev          # docs at http://localhost:8080
```

## Adding or changing a component

1. Put the CSS in the right layer — `src/3-components/` for anything with
   variants or states, `src/2-elements/` for a single idea with neither.
2. Add its `@import` to that layer's `index.css`.
3. **Document it.** A component that isn't on the docs site doesn't exist.
   Add a page in `docs/_build/content_*.py` and a line in `NAV` in
   `docs/_build/build.py`, then run `npm run docs`.
4. Show **every** variant and state, each with its class names in the spec
   strip beneath it.
5. `npm run lint` and check the page in both themes.

Never edit `docs/*.html` — those files are generated.

## Commit messages

Plain and specific: `nav: add aperture burger variant`,
`fix: grid-rail-left stacked when used alone`.

## Pull requests

Say what changed and why, and include a screenshot in both themes for anything
visual. Small PRs get reviewed faster than large ones.

## Reporting bugs

Open an issue with the browser, the theme (light/dark), the markup you used,
and what you expected. A link to a reduced test case is worth a thousand words.

## Adding your site to the Showcase

See [showcase/README.md](showcase/README.md) — it's one JSON file and a PR.
