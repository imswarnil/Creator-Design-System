## What changed

<!-- One or two sentences. What does this add, fix or remove? -->

## Why

<!-- The problem it solves. Link the issue if there is one: Fixes #123 -->

## Checklist

- [ ] Every value is a `var()` off an existing ladder (no raw hex, no magic numbers)
- [ ] State uses ARIA (`aria-current` / `aria-pressed` / `[data-done]`), not an `.active` class
- [ ] Checked in **light and dark**
- [ ] Motion degrades under `prefers-reduced-motion`
- [ ] Documented on the docs site (`docs/_build/content_*.py` + a line in `NAV`)
- [ ] `npm run lint` passes

## Screenshots

<!-- Anything visual: one light, one dark. -->
