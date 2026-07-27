"""Landing page + Showcase + Templates + Sponsor.

The landing page is rendered with its own full-width template (no sidebar) —
it is marketing, not documentation. Showcase and Templates read the JSON files
contributors add to /showcase and /templates, so a merged PR is a published
entry with no extra step.
"""
import json, pathlib
from common import tile, ct

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent

PAGES = {}
LANDING = {}


def _load(folder):
    d = REPO / folder
    out = []
    if d.exists():
        for f in sorted(d.glob('*.json')):
            if f.name.startswith('_'):
                continue
            try:
                out.append(json.loads(f.read_text()))
            except json.JSONDecodeError:
                pass
    return out


# ── The animated hero illustration ──────────────────────────────────────────

MONO = 'IBM Plex Mono, monospace'

# One viewfinder, four things a creator makes. The frame and its chrome — the
# corners, the record light, the sweep — never move; only what is being framed
# changes, which is the whole argument of the system in one picture. Square,
# because the frame is not a video player: it holds a 16:9 video, a 9:16 reel,
# a page of writing and a screen of code without ever resizing itself.
HERO_SVG = f'''
<svg class="lp-illo" viewBox="0 0 600 600" role="img"
     aria-label="A viewfinder framing four things in turn: a video, a vertical reel, a page being written, and code being typed">
	<rect width="600" height="600" fill="var(--bg-sunken)"/>
	<g stroke="var(--line-default)" stroke-width="1">
		<path d="M0 150h600M0 300h600M0 450h600M150 0v600M300 0v600M450 0v600"/>
	</g>
	<g class="lp-orbit" fill="none" stroke="var(--line-strong)" stroke-width="1.5" stroke-dasharray="4 7">
		<circle cx="300" cy="300" r="216"/>
	</g>

	<!-- Scene 1 · the video -->
	<g class="lp-scene lp-scene-1">
		<rect x="110" y="193" width="380" height="214" rx="10"
		      fill="var(--bg-surface)" stroke="var(--line-default)"/>
		<circle class="lp-pulse" cx="300" cy="288" r="34" fill="var(--accent)"/>
		<path d="M291 276v24l21-12-21-12Z" fill="#fff"/>
		<rect x="130" y="374" width="340" height="4" rx="2" fill="var(--line-default)"/>
		<rect class="lp-grow" x="130" y="374" width="340" height="4" rx="2" fill="var(--accent)"/>
		<text x="130" y="398" font-family="{MONO}" font-size="11" letter-spacing="1.6"
		      fill="var(--fg-faint)">04:12 / 11:38</text>
		<text x="104" y="548" font-family="{MONO}" font-size="12" letter-spacing="2.5"
		      fill="var(--fg-subtle)">VIDEO · 16:9</text>
	</g>

	<!-- Scene 2 · the reel -->
	<g class="lp-scene lp-scene-2">
		<rect x="204" y="129" width="192" height="342" rx="14"
		      fill="var(--bg-surface)" stroke="var(--line-default)"/>
		<rect x="224" y="404" width="120" height="9" rx="4" fill="var(--line-default)"/>
		<rect class="lp-grow" x="224" y="422" width="86" height="9" rx="4" fill="var(--line-strong)"/>
		<g fill="none" stroke="var(--fg-subtle)" stroke-width="2.4" stroke-linecap="round"
		   stroke-linejoin="round" transform="translate(414 300)">
			<path class="lp-pop" d="M11 19s-9-5.6-9-11.5A4.9 4.9 0 0 1 11 4.6 4.9 4.9 0 0 1 20 7.5C20 13.4 11 19 11 19Z"
			      fill="var(--accent)" stroke="var(--accent)"/>
			<path d="M2 46a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H8l-5 4v-4H4a2 2 0 0 1-2-2v-9Z"
			      transform="translate(0 6)"/>
		</g>
		<text x="104" y="548" font-family="{MONO}" font-size="12" letter-spacing="2.5"
		      fill="var(--fg-subtle)">REEL · 9:16</text>
	</g>

	<!-- Scene 3 · the writing -->
	<g class="lp-scene lp-scene-3">
		<rect class="lp-grow" x="130" y="190" width="250" height="22" rx="5" fill="var(--fg-default)"/>
		<rect class="lp-grow lp-d1" x="130" y="240" width="340" height="10" rx="4" fill="var(--line-default)"/>
		<rect class="lp-grow lp-d2" x="130" y="266" width="312" height="10" rx="4" fill="var(--line-default)"/>
		<rect class="lp-grow lp-d3" x="130" y="292" width="336" height="10" rx="4" fill="var(--line-default)"/>
		<rect class="lp-grow lp-d4" x="130" y="318" width="180" height="10" rx="4" fill="var(--line-default)"/>
		<rect class="lp-caret" x="318" y="314" width="3" height="18" fill="var(--accent)"/>
		<text x="104" y="548" font-family="{MONO}" font-size="12" letter-spacing="2.5"
		      fill="var(--fg-subtle)">BLOG · WRITING</text>
	</g>

	<!-- Scene 4 · the code -->
	<g class="lp-scene lp-scene-4">
		<g font-family="{MONO}" font-size="15">
			<text class="lp-grow" x="130" y="212" fill="var(--fg-faint)">/* one colour means live */</text>
			<text class="lp-grow lp-d1" x="130" y="244" fill="var(--accent)">.dot-live<tspan fill="var(--fg-subtle)"> {{</tspan></text>
			<text class="lp-grow lp-d2" x="154" y="276" fill="var(--fg-muted)">background<tspan fill="var(--fg-subtle)">: </tspan><tspan fill="var(--fg-default)">var(--accent)</tspan><tspan fill="var(--fg-subtle)">;</tspan></text>
			<text class="lp-grow lp-d3" x="154" y="308" fill="var(--fg-muted)">animation<tspan fill="var(--fg-subtle)">: </tspan><tspan fill="var(--fg-default)">rec 2.4s</tspan><tspan fill="var(--fg-subtle)">;</tspan></text>
			<text class="lp-grow lp-d4" x="130" y="340" fill="var(--fg-subtle)">}}</text>
		</g>
		<rect class="lp-caret" x="146" y="326" width="3" height="18" fill="var(--accent)"/>
		<text x="104" y="548" font-family="{MONO}" font-size="12" letter-spacing="2.5"
		      fill="var(--fg-subtle)">CODE · SHIPPING</text>
	</g>

	<!-- The frame itself, over every scene -->
	<g fill="none" stroke="var(--fg-default)" stroke-width="5" stroke-linecap="round">
		<path d="M90 128V102a12 12 0 0 1 12-12h26M510 128V102a12 12 0 0 0-12-12h-26M90 472v26a12 12 0 0 0 12 12h26M510 472v26a12 12 0 0 1-12 12h-26"/>
	</g>
	<g class="lp-scan"><path d="M104 118h392" stroke="var(--accent)" stroke-width="1.5" opacity="0.55"/></g>
	<circle class="lp-rec" cx="486" cy="66" r="8" fill="var(--accent)"/>
	<text x="104" y="71" font-family="{MONO}" font-size="12" letter-spacing="2.5"
	      fill="var(--fg-faint)">TAKE 47 · 00:12:47</text>
	<g class="lp-chip" transform="translate(388 528)">
		<rect width="118" height="26" rx="13" fill="var(--bg-surface)" stroke="var(--line-default)"/>
		<circle cx="16" cy="13" r="4" fill="var(--accent)"/>
		<text x="30" y="17" font-family="{MONO}" font-size="10" letter-spacing="1.6"
		      fill="var(--fg-subtle)">--accent</text>
	</g>
</svg>'''

ICON = lambda p: (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
                  f'stroke-linecap="round" stroke-linejoin="round" class="lp-feat__icon">{p}</svg>')

FEATURES = [
    ('<path d="M12 3 20 7.5v9L12 21 4 16.5v-9L12 3Z"/><path d="M12 12v9M12 12 4 7.5M12 12l8-4.5"/>',
     'Token-first', 'Every value is a variable off a ladder. Change three and the whole site rebrands — site, player, thumbnails.'),
    ('<circle cx="12" cy="12" r="3" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="8" stroke-dasharray="3 4"/>',
     'One rationed accent', 'Near-monochrome ink so a single colour can mean <em>live</em>. Attention is budgeted, not sprayed.'),
    ('<rect x="3.5" y="4.5" width="17" height="13" rx="2"/><path d="M3.5 8.5h17M12 17.5V20M8 20h8"/>',
     'The platform first', '&lt;details&gt;, &lt;dialog&gt;, the Popover API and native inputs. Keyboard and focus come free.'),
    ('<path d="M4 12h4l2-5 3 10 2-5h5"/>',
     'Honest motion', 'Under 200ms for feedback, one property at a time, and every animation off under reduced-motion.'),
    ('<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5Z"/>',
     'Light and dark', 'Both themes from the same variables. Ink and paper flip; the record-red is the one hue that stays.'),
    ('<rect x="3.5" y="5.5" width="17" height="13" rx="2"/><path d="m3.5 15 4.5-4 4 3.5 3-2.5 5.5 4.5"/><circle cx="9" cy="9.5" r="1.3"/>',
     'Site and channel', 'The same tokens export to YouTube thumbnails, banners and Instagram posts. One brand, not two.'),
]


def _install_block():
    def blk(lang, lines):
        body = ''.join(f'<span class="ln">{l}</span>' for l in lines)
        return (f'<figure class="codebox u-m-0"><figcaption class="codebox__head">'
                f'<span class="codebox__lang">{lang}</span>'
                f'<button class="codebox__copy" type="button" data-copy>Copy</button></figcaption>'
                f'<pre class="codebox__pre"><code>{body}</code></pre></figure>')
    return (
        '<div class="lp-install">'
        '<div class="tabs" role="tablist" aria-label="Install">'
        '<button class="tab" role="tab" aria-selected="true" data-install-tab="npm">npm</button>'
        '<button class="tab" role="tab" aria-selected="false" data-install-tab="cdn">CDN</button>'
        '<button class="tab" role="tab" aria-selected="false" data-install-tab="css">Download</button>'
        '</div>'
        f'<div data-install-panel="npm">{blk("bash", ["npm install creator-design-system"])}'
        f'{blk("css", ["<span class=\'tok-key\'>@import</span> <span class=\'tok-str\'>&quot;creator-design-system&quot;</span>;"])}</div>'
        f'<div data-install-panel="cdn" hidden>{blk("html", ["&lt;<span class=\'tok-key\'>link</span> rel=<span class=\'tok-str\'>&quot;stylesheet&quot;</span>", "      href=<span class=\'tok-str\'>&quot;https://cdn.jsdelivr.net/npm/creator-design-system@0/dist/creator.min.css&quot;</span>&gt;"])}</div>'
        f'<div data-install-panel="css" hidden>{blk("bash", ["curl -O https://unpkg.com/creator-design-system/dist/creator.css", "<span class=\'tok-com\'># link it. that is the whole installation.</span>"])}</div>'
        '</div>')


def build_landing():
    show = _load('showcase')[:3]
    tpl = _load('templates')[:2]

    cards = ''.join(
        f'<div class="lp-feat"><span class="lp-feat__ico">{ICON(p)}</span>'
        f'<h3 class="t-h4">{t}</h3><p class="t-small u-fg-subtle u-mt-2">{d}</p></div>'
        for p, t, d in FEATURES)

    showcards = ''.join(
        f'<a class="card" href="{s["url"]}" rel="noopener" target="_blank">'
        f'<span class="card__media pattern pattern-grid pattern-media"></span>'
        f'<span class="card__body"><span class="card__meta">{s.get("author","")}</span>'
        f'<span class="card__title">{s["name"]}</span>'
        f'<span class="card__excerpt">{s.get("description","")}</span></span></a>'
        for s in show) or '<p class="t-small u-fg-faint">No entries yet — be the first.</p>'

    tplcards = ''.join(
        f'<a class="card card-row" href="{t["url"]}" rel="noopener" target="_blank">'
        f'<span class="card__body"><span class="card__meta">{t.get("platform","")} · '
        f'<b>{t.get("price","")}</b></span>'
        f'<span class="card__title">{t["name"]}</span>'
        f'<span class="card__excerpt">{t.get("description","")}</span></span></a>'
        for t in tpl) or '<p class="t-small u-fg-faint">No templates listed yet.</p>'

    return f'''
<header class="lp-nav">
	<div class="container lp-nav__in">
		<a class="cds-mark cds-mark-live" href="./index.html">
			<span class="cds-mark__word">creat<i class="cds-mark__o" aria-hidden="true"></i><span class="u-sr-only">o</span>r</span>
			<span class="cds-mark__sub">design system</span>
		</a>
		<nav class="cluster-sm">
			<a class="nav-link" href="./introduction.html">Docs</a>
			<a class="nav-link" href="./components.html">Components</a>
			<a class="nav-link" href="./showcase.html">Showcase</a>
			<a class="nav-link" href="./templates.html">Templates</a>
		</nav>
		<div class="cluster-sm">
			<button class="nav-burger nav-burger-aperture cds-bar__burger" type="button"
			        aria-expanded="false" aria-controls="cds-menu" data-dialog="cds-menu" data-menu-burger>
				<span class="nav-burger__box"><span class="nav-burger__bars"></span></span>
				<span class="u-sr-only">Menu</span>
			</button>
			<button class="doc-btn" id="themeToggle" type="button" aria-pressed="false">
				<span class="dot dot-sm" aria-hidden="true"></span><span id="themeLabel">Light</span>
			</button>
			<a class="btn btn-secondary btn-sm" href="https://github.com/imswarnil/Creator-Design-System"
			   rel="noopener" target="_blank">
				<svg class="icon btn__icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7C6.73 19.91 6.14 18 6.14 18a2.7 2.7 0 0 0-1.13-1.49c-.92-.63.07-.62.07-.62a2.14 2.14 0 0 1 1.56 1.05 2.17 2.17 0 0 0 2.96.85 2.18 2.18 0 0 1 .65-1.37c-2.23-.25-4.57-1.11-4.57-4.95a3.88 3.88 0 0 1 1.03-2.69 3.6 3.6 0 0 1 .1-2.65s.84-.27 2.75 1.03a9.47 9.47 0 0 1 5 0c1.91-1.3 2.75-1.03 2.75-1.03a3.6 3.6 0 0 1 .1 2.65 3.87 3.87 0 0 1 1.03 2.69c0 3.85-2.34 4.7-4.57 4.95a2.43 2.43 0 0 1 .69 1.88v2.79c0 .27.18.58.69.48A10 10 0 0 0 12 2Z"/></svg>
				GitHub <span class="badge" data-gh-stars>★</span>
			</a>
		</div>
	</div>
</header>
<dialog class="nav-sheet" id="cds-menu">
	<div class="nav-sheet__in">
		<span class="nav-sheet__scan" aria-hidden="true"></span>
		<div class="nav-sheet__head">
			<span class="cds-mark"><span class="cds-mark__word">creat<i class="cds-mark__o" aria-hidden="true"></i><span class="u-sr-only">o</span>r</span></span>
			<button class="btn-close" type="button" data-dialog-close aria-label="Close menu"></button>
		</div>
		<nav class="nav-sheet__links" aria-label="Site">
			<a class="nav-sheet__link" style="--i:0" href="./introduction.html">Docs</a>
			<a class="nav-sheet__link" style="--i:1" href="./components.html">Components</a>
			<a class="nav-sheet__link" style="--i:2" href="./showcase.html">Showcase</a>
			<a class="nav-sheet__link" style="--i:3" href="./templates.html">Templates</a>
			<a class="nav-sheet__link" style="--i:4" href="./sponsor.html">Sponsor</a>
		</nav>
		<div class="nav-sheet__foot">
			<span class="t-slate-sm" style="color:var(--fg-faint)"><span class="dot dot-sm dot-live"></span> still rolling</span>
			<a class="btn btn-primary btn-sm btn-pill" href="https://github.com/imswarnil/Creator-Design-System" rel="noopener">GitHub</a>
		</div>
	</div>
</dialog>

<main id="main">
	<section class="container lp-hero pattern pattern-grid pattern-lg fade-corners">
		<div class="lp-hero__copy">
			<span class="eyebrow"><span class="dot dot-sm dot-live"></span> MIT · v0.1 · dependency-free CSS</span>
			<h1 class="lp-hero__title">The design system for people who <em>make things</em>.</h1>
			<p class="t-lead u-mt-5">
				Videos, courses, build logs, trips — every shape a creator publishes,
				decided once in tokens and reused everywhere. Almost monochrome, so
				one colour can mean <em class="t-accent">live</em>.
			</p>
			<div class="cluster u-mt-8">
				<a class="btn btn-primary btn-lg" href="./introduction.html">Read the docs</a>
				<a class="btn btn-secondary btn-lg" href="./components.html">Browse components</a>
			</div>
			<p class="t-slate-sm u-mt-5" style="color:var(--fg-faint)">
				No framework · no runtime · no build step required
			</p>
		</div>
		<div class="lp-hero__art">{HERO_SVG}</div>
	</section>

	<section class="container section">
		<div class="sec-head-row">
			<div><span class="sec-head-row__kicker">Why it exists</span>
			<h2 class="sec-head-row__title">Opinions, so you can stop having them</h2></div>
		</div>
		<div class="lp-feats">{cards}</div>
	</section>

	<section class="container section">
		<div class="grid-2" style="gap:var(--space-10);align-items:center">
			<div>
				<span class="sec-head-row__kicker">Install</span>
				<h2 class="sec-head-row__title u-mb-4">Three lines, any stack</h2>
				<p class="u-fg-subtle" style="max-width:var(--measure-ui)">
					It is a stylesheet. Use it with plain CSS, SCSS, Tailwind, Ghost,
					Astro or a single HTML file — then override three variables and
					it is yours.
				</p>
				<a class="t-link fx-shift u-inline-block u-mt-4" href="./install.html">
					Full install guide <span class="fx-shift__icon">→</span></a>
			</div>
			{_install_block()}
		</div>
	</section>

	<section class="container section">
		<div class="sec-head-row">
			<div><span class="sec-head-row__kicker">Built with it</span>
			<h2 class="sec-head-row__title">Showcase</h2></div>
			<a class="sec-head-row__more fx-shift" href="./showcase.html">All sites <span class="fx-shift__icon">→</span></a>
		</div>
		<div class="deck-c">{showcards}</div>
	</section>

	<section class="container section">
		<div class="sec-head-row">
			<div><span class="sec-head-row__kicker">Start from a finished thing</span>
			<h2 class="sec-head-row__title">Templates</h2></div>
			<a class="sec-head-row__more fx-shift" href="./templates.html">All templates <span class="fx-shift__icon">→</span></a>
		</div>
		<div class="stack">{tplcards}</div>
	</section>

	<section class="container section">
		<div class="cta pattern pattern-grid" data-surface="inverse">
			<span class="cta__kicker">Open source</span>
			<h2 class="cta__title">Free forever. <em>Sponsored</em> keeps it maintained.</h2>
			<p class="cta__body">
				MIT-licensed and built in public. If it saved you a weekend, sponsorship
				pays for the next component — and templates fund the rest.
			</p>
			<div class="cta__actions">
				<a class="btn btn-primary btn-lg" href="https://github.com/sponsors/imswarnil" rel="noopener" target="_blank">Sponsor the project</a>
				<a class="btn btn-secondary btn-lg" href="https://github.com/imswarnil/Creator-Design-System" rel="noopener" target="_blank">Star on GitHub</a>
			</div>
			<p class="cta__fine">Or contribute — issues and pull requests are genuinely welcome.</p>
		</div>
	</section>

	<footer class="container footer">
		<div class="footer__grid">
			<div class="footer__brand">
				<span class="cds-mark"><span class="cds-mark__word">creat<i class="cds-mark__o" aria-hidden="true"></i><span class="u-sr-only">o</span>r</span></span>
				<p class="footer__tag">Frame &amp; Signal — a token-first design system for creators building their site.</p>
			</div>
			<div><h2 class="footer__head">Docs</h2><div class="footer__links">
				<a href="./introduction.html">Introduction</a><a href="./principles.html">Principles</a>
				<a href="./install.html">Install</a><a href="./components.html">Components</a></div></div>
			<div><h2 class="footer__head">Project</h2><div class="footer__links">
				<a href="https://github.com/imswarnil/Creator-Design-System" rel="noopener">GitHub</a>
				<a href="https://github.com/imswarnil/Creator-Design-System/blob/main/CONTRIBUTING.md" rel="noopener">Contributing</a>
				<a href="https://github.com/imswarnil/Creator-Design-System/releases" rel="noopener">Releases</a></div></div>
			<div><h2 class="footer__head">More</h2><div class="footer__links">
				<a href="./showcase.html">Showcase</a><a href="./templates.html">Templates</a>
				<a href="https://github.com/sponsors/imswarnil" rel="noopener">Sponsor</a></div></div>
		</div>
		<div class="footer__signoff">
			<span>MIT © 2026 Swarnil Singhai</span>
			<span class="footer__rec"><span class="dot dot-sm dot-live"></span> still rolling</span>
		</div>
	</footer>
</main>
'''


LANDING['index'] = ('Creator Design System — Frame & Signal', build_landing)


# ── Showcase ────────────────────────────────────────────────────────────────

def _showcase():
    items = _load('showcase')
    body = (
        '<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
        'Sites built with the system. Adding yours is one JSON file and a pull '
        'request — the page is generated from '
        '<code class="t-code">/showcase/*.json</code>, so a merged PR is a '
        'published entry.</p>'
        '<div class="cluster u-mb-8">'
        '<a class="btn btn-primary" href="https://github.com/imswarnil/Creator-Design-System/tree/main/showcase" rel="noopener">Add your site</a>'
        '<a class="btn btn-quiet" href="https://github.com/imswarnil/Creator-Design-System/blob/main/showcase/README.md" rel="noopener">How it works</a>'
        '</div>')
    if not items:
        body += ('<div class="empty"><span class="eyebrow">Empty</span>'
                 '<p class="empty__title">No sites listed yet</p>'
                 '<p class="empty__body">Yours could be the first.</p></div>')
    else:
        cards = ''
        for s in items:
            tags = ''.join(f'<span class="badge">{t}</span>' for t in s.get('tags', [])[:4])
            accent = f' style="--accent:{s["accent"]}"' if s.get('accent') else ''
            media = (f'<img src="../showcase/screenshots/{s["screenshot"]}" alt="{s["name"]}" '
                     f'class="u-object-cover u-w-full u-h-full" loading="lazy" />'
                     if s.get('screenshot') else
                     '<span class="pattern pattern-grid u-absolute u-inset-0"></span>')
            cards += (f'<article class="card"{accent}>'
                      f'<span class="card__media u-relative u-overflow-hidden u-ratio-video">{media}</span>'
                      f'<div class="card__body"><p class="card__meta">'
                      f'<span class="dot dot-sm"></span> {s.get("author","")}</p>'
                      f'<h2 class="card__title"><a class="card__link" href="{s["url"]}" rel="noopener" target="_blank">{s["name"]}</a></h2>'
                      f'<p class="card__excerpt">{s.get("description","")}</p>'
                      f'<div class="cluster-sm u-mt-3">{tags}</div></div></article>')
        body += f'<div class="deck-c">{cards}</div>'
    return body


PAGES['showcase'] = ('Showcase',
    'Sites built with the Creator Design System — and how to add yours in one pull request.',
    _showcase())


# ── Templates ───────────────────────────────────────────────────────────────

def _templates():
    items = _load('templates')
    body = (
        '<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
        'The system is MIT and always free. Templates are finished products — '
        'content structure, routes, demo data and support — and buying one funds '
        'the time to maintain the system itself.</p>')
    if not items:
        body += ('<div class="empty"><span class="eyebrow">Empty</span>'
                 '<p class="empty__title">No templates listed yet</p></div>')
    else:
        rows = ''
        for t in items:
            feats = ''.join(f'<li>{f}</li>' for f in t.get('features', [])[:5])
            rows += (
                f'<article class="surface u-p-6 u-mb-4">'
                f'<div class="row-between u-mb-3" style="align-items:flex-start;gap:var(--space-4)">'
                f'<div><span class="eyebrow">{t.get("platform","")} · {t.get("author","")}</span>'
                f'<h2 class="t-h3 u-mt-2">{t["name"]}</h2></div>'
                f'<span class="badge badge-signal">{t.get("price","")}</span></div>'
                f'<p class="u-fg-subtle">{t.get("description","")}</p>'
                + (f'<ul class="t-small u-fg-subtle u-mt-4" style="padding-left:1.1rem;display:grid;gap:4px">{feats}</ul>' if feats else '')
                + f'<div class="cluster u-mt-5"><a class="btn btn-primary" href="{t["url"]}" rel="noopener" target="_blank">Get this template</a></div>'
                f'</article>')
        body += rows
    body += (
        '<h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">List your template</h2>'
        '<p class="u-fg-subtle u-mb-4" style="max-width:var(--measure-lead)">'
        'Built something on the system? Free or paid, add a JSON file to '
        '<code class="t-code">/templates</code> and open a pull request.</p>'
        '<a class="btn btn-secondary" href="https://github.com/imswarnil/Creator-Design-System/blob/main/templates/README.md" rel="noopener">How to list</a>')
    return body


PAGES['templates'] = ('Templates',
    'Ready-made themes and starters built on the system — free and paid.',
    _templates())


# ── Sponsor ─────────────────────────────────────────────────────────────────

PAGES['sponsor'] = ('Sponsor',
    'The system is free and MIT-licensed. Sponsorship is what keeps it maintained.',
    '<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
    'Creator Design System is free, MIT-licensed, and built in public. It has no '
    'company behind it — just the time of the people who work on it. If it saved '
    'you a weekend, here is how to keep it going.</p>'
    + '<div class="grid-3 u-mb-8">'
      '<div class="surface u-p-5"><span class="eyebrow">One-off</span>'
      '<h3 class="t-h4 u-mt-2">Buy a coffee</h3>'
      '<p class="t-small u-fg-subtle u-mt-2">A single thank-you. No tiers, no invoice.</p>'
      '<a class="btn btn-secondary btn-sm u-mt-4" href="https://github.com/sponsors/imswarnil" rel="noopener">Sponsor once</a></div>'
      '<div class="surface u-p-5" style="border-color:var(--line-accent)"><span class="eyebrow t-accent">Monthly</span>'
      '<h3 class="t-h4 u-mt-2">Keep it maintained</h3>'
      '<p class="t-small u-fg-subtle u-mt-2">Recurring support pays for the next component, and for answering issues.</p>'
      '<a class="btn btn-primary btn-sm u-mt-4" href="https://github.com/sponsors/imswarnil" rel="noopener">Sponsor monthly</a></div>'
      '<div class="surface u-p-5"><span class="eyebrow">Free</span>'
      '<h3 class="t-h4 u-mt-2">Contribute instead</h3>'
      '<p class="t-small u-fg-subtle u-mt-2">Time is worth more than money here. Fix a bug, document a gap, add your site.</p>'
      '<a class="btn btn-secondary btn-sm u-mt-4" href="https://github.com/imswarnil/Creator-Design-System/blob/main/CONTRIBUTING.md" rel="noopener">Contributing guide</a></div>'
      '</div>'
    + ct([
        ('Where it goes', 'maintenance time: issues, browser bugs, new components, documentation'),
        ('What it does not buy', 'influence over the roadmap — the principles page decides that'),
        ('Templates', 'buying a <a class="t-link" href="./templates.html">template</a> funds the system too, and you get a finished product'),
        ('Sponsors', 'listed here and in the README once the programme is live'),
      ], head=('Question', 'Answer')))
