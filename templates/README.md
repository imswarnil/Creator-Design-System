# Templates

Ready-made themes and starters built on the Creator Design System.

The system itself is MIT and always free. Templates are finished products —
content structure, routes, demo data and support — and some of them are paid.
That is what funds the time to maintain this.

## Listing a template

Each template is one JSON file in this folder, read by the docs site at build
time. Free templates are welcome; so are paid ones.

1. Copy `_example.json` to `your-template.json`.
2. Fill it in — `price` accepts `"Free"` or a string like `"$49"`.
3. Add a 1200×750 preview to `previews/`.
4. Open a pull request titled `template: your-template`.

Maintainers may decline listings that misrepresent what is included, or that
are not actually built on the system.

## Fields

| Field | Required | Notes |
| --- | --- | --- |
| `name` | yes | Template name |
| `description` | yes | One sentence |
| `price` | yes | `"Free"` or e.g. `"$49"` |
| `url` | yes | Where to get it |
| `platform` | yes | `Ghost`, `Astro`, `11ty`, `HTML`… |
| `author` | yes | Who made it |
| `preview` | no | Filename in `previews/` |
| `features` | no | Up to five short bullets |
