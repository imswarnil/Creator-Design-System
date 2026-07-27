"""One page that links to every page — the whole system at a glance."""
from common import ct

PAGES = {}


def build(NAV, FRAGPAGES):
    """Built from the same NAV the sidebar uses, so it can never fall behind."""
    total = sum(len(items) for _, items in NAV)
    out = [
        f'<p class="u-fg-subtle u-mb-6" style="max-width:var(--measure-lead)">'
        f'Every page in the system — <b>{total}</b> of them, in the order the sidebar '
        f'uses. This page is generated from the same navigation tree, so it can never '
        f'fall out of date. Handy for scanning what exists, and for handing someone a '
        f'single link.</p>'
        '<div class="cluster u-mb-8">'
        '<a class="btn btn-primary btn-sm" href="./components.html">Components explorer</a>'
        '<a class="btn btn-secondary btn-sm" href="./introduction.html">Introduction</a>'
        '<a class="btn btn-quiet btn-sm" href="./index.html">Landing page</a>'
        '</div>']

    for group, items in NAV:
        links = ''.join(
            f'<a class="list-group__item" href="./{slug}.html">'
            f'<span class="u-weight-medium">{label}</span>'
            f'<code class="t-code u-ms-auto t-small">{slug}</code></a>'
            for slug, label in items)
        out.append(
            f'<h2 class="t-h3" style="margin:var(--space-8) 0 var(--space-3)">{group} '
            f'<span class="badge">{len(items)}</span></h2>'
            f'<div class="list-group u-mb-4">{links}</div>')

    out.append(ct([
        ('Landing', '<code class="t-code">index.html</code> — the marketing page'),
        ('Docs home', '<code class="t-code">introduction.html</code>'),
        ('Search', 'press <kbd class="kbd">/</kbd> on any page'),
        ('Preview ⇄ Code', 'the toggle on every demo prints its own markup'),
        ('Source', '<code class="t-code">/src</code> · icons in <code class="t-code">/icons</code> · bundles in <code class="t-code">/dist</code>'),
    ], head=('Shortcut', 'Where')))
    return '\n'.join(out)
