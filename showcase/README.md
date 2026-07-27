# Showcase

Sites built with the Creator Design System. Adding yours is one file and a
pull request — no build step, no code review of your site, just a check that
the link works and the entry is filled in honestly.

## Add yours

1. Copy `_example.json` to `your-site-name.json` in this folder.
2. Fill it in.
3. Drop a 1200×750 screenshot into `screenshots/` with the same base name
   (`your-site-name.png` or `.jpg`, under 300 KB — please compress it).
4. Open a pull request titled `showcase: your-site-name`.

The docs site reads every JSON file in this folder at build time, so your
entry appears on the [Showcase page](https://swarnil.github.io/Creator-Design-System/showcase.html)
as soon as the PR is merged.

## The fields

| Field | Required | Notes |
| --- | --- | --- |
| `name` | yes | The site's name |
| `url` | yes | Must be live and public |
| `author` | yes | Your name or handle |
| `authorUrl` | no | Where to find you |
| `description` | yes | One sentence, ≤ 120 characters |
| `tags` | no | Up to four, e.g. `["ghost", "portfolio", "courses"]` |
| `screenshot` | no | Filename in `screenshots/`; a pattern tile is used if absent |
| `accent` | no | Your `--accent` value, so the card can show your palette |

## House rules

- The site must be **live** and actually use the system.
- One entry per site.
- Keep the description factual — this is a gallery, not an ad.
- Entries whose links die get removed; open a PR to restore yours.
