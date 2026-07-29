#!/usr/bin/env python3
"""One-time extractor: split the legacy overview pages into HTML fragments that
build.py assembles into individual docs pages. Run from _build/:
    python3 extract.py
Writes fragments/<page>/<section-id>.html (+ _style.css where a page had an
inline <style>). Safe to re-run while the legacy pages still exist; after they
are deleted the fragments are the source of truth.
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
PREVIEW = HERE.parent.parent
FRAG = HERE / 'fragments'

SOURCES = {
    'index.html': 'foundation',
    'elements.html': 'elements',
    'components.html': 'components',
    'youtube.html': 'youtube',
    'social.html': 'social',
}


def sections(html):
    """Yield (id, inner_html) for every TOP-level <section id=…>, balanced."""
    for m in re.finditer(r'<section id="([a-z0-9-]+)"[^>]*>', html):
        sid, depth, i = m.group(1), 1, m.end()
        while depth:
            nxt = re.search(r'<section\b|</section>', html[i:])
            if not nxt:
                break
            depth += 1 if nxt.group(0) != '</section>' else -1
            i += nxt.end()
        yield sid, html[m.end():i - len('</section>')]


def main():
    for fname, folder in SOURCES.items():
        src = PREVIEW / fname
        if not src.exists():
            print('skip (gone):', fname)
            continue
        html = src.read_text()
        out = FRAG / folder
        out.mkdir(parents=True, exist_ok=True)

        style = re.search(r'<style>(.*?)</style>', html, re.S)
        if style:
            (out / '_style.css').write_text(style.group(1).strip() + '\n')

        n = 0
        for sid, inner in sections(html):
            (out / f'{sid}.html').write_text(inner.strip() + '\n')
            n += 1
        print(f'{fname}: {n} fragments -> fragments/{folder}/')

    # Split the foundation motion mega-section into its sub-layers.
    motion = FRAG / 'foundation' / 'motion.html'
    if motion.exists():
        parts = re.split(r'(?=<h3 class="t-h2")', motion.read_text())
        names = ['motion-basics']
        for p in parts[1:]:
            t = re.search(r'>([^<]+)</h3>', p)
            slug = re.sub(r'[^a-z0-9]+', '-', t.group(1).lower()).strip('-') if t else 'x'
            names.append(slug)
        for name, part in zip(names, parts):
            (FRAG / 'foundation' / f'{name}.html').write_text(part.strip() + '\n')
        print('motion split ->', ', '.join(names))


if __name__ == '__main__':
    main()
