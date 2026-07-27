# Frame & Signal — After Effects template

A starter After Effects project generated from this design system's tokens:
the ink/signal/craft/mint/azure/rose colour ramps, the three-typeface system
(Space Grotesk / Inter / IBM Plex Mono), and the safe-area math from
[`src/4-broadcast`](../src/4-broadcast) (thumbnail, banner, Instagram canvases).

## Why a script, not a `.aep` file

`.aep` is a proprietary binary format — it can't be hand-written outside After
Effects. The standard way to automate AE project creation is an ExtendScript
(`.jsx`) that runs *inside* AE and builds real compositions and layers, which
you then save as a normal project. That's what
[`build-design-system-template.jsx`](build-design-system-template.jsx) does.

## Setup

1. Install the three typefaces if you don't have them (all free):
   - [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) — display, weight 700
   - [Inter](https://fonts.google.com/specimen/Inter) — body, weight 400/600
   - [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono) — slate/metadata voice, weight 500
2. Open After Effects → **File → Scripts → Run Script File…**
3. Pick `build-design-system-template.jsx`.
4. Read the completion alert — it lists every comp it built and any font/effect
   it couldn't apply (fix those manually in the Character panel / Effect
   Controls, it's a couple of clicks).
5. **File → Save As** to keep the project — the script only adds to the
   current session, it never writes to disk itself.

## What it builds

| Folder | Comp | Purpose |
|---|---|---|
| 01 Style Guide | `00 — Style Guide` | Every colour ramp as swatches + type specimens (Display/Body/Slate), at broadcast scale |
| 02 Backgrounds | `BG — Grid` / `Blueprint` / `Dots` / `Scanline` / `Noise` | Tileable pattern textures built from AE's native Generate effects (Grid, Cell Pattern, Fractal Noise) — same grammar as `src/1-foundation/07-pattern.css`, just re-cut for a 1920×1080 canvas instead of CSS |
| 03 Canvases | `YouTube Thumbnail — 1280x720` | Guide layers marking the 5.5% safe inset and the right-36% subject zone from `21-thumbnail.css` |
| | `YouTube Banner — 2560x1440` | Guide layers for the full TV crop and the centred 1546×423 mobile-safe box from `25-brand.css` |
| | `Instagram Post — 1080x1080` / `Instagram Story — 1080x1920` | Safe-area guides for feed and story crops |
| 04 Examples | `Example — Title Card` | The grid background + accent rule + record dot + type, composed together, so you can see the system as a finished frame rather than isolated parts |

All guide-layer overlays (`GUIDE — …`) are marked as **AE guide layers** — they
show in the viewer but never render or export, same as the `banner-rulers`
crop lines in the CSS source.

## Notes & limits

- The five background patterns are built with AE's built-in Generate effects
  (Grid, Fractal Noise, Cell Pattern), not a pixel-for-pixel port of the CSS
  gradients — there's no AE equivalent to a CSS `repeating-linear-gradient`.
  They're tuned to read the same (hairline grid, fine noise, scattered dots)
  but nudge the Effect Controls sliders to taste.
- Text sizes are fixed points, not the CSS's fluid `clamp()` scale — picked to
  read well at 1920×1080 / broadcast canvas sizes.
- No animation yet (no lower-third, no intro sting). The design system's
  `05-motion.css` durations (120/200/320/560ms) and easings map directly to
  AE keyframe eases if you want to add one later — ask and I'll build it as a
  v2 script.
- I couldn't run this inside a live After Effects instance to verify it end
  to end — if any line throws when you run it, send me the error message and
  line number from the alert and I'll fix it immediately.
