"""Shared helpers for docs content modules."""


def tile(demo, spec, pad=True):
    """A demo surface with the what-this-is-called strip."""
    style = '' if pad else ' style="padding:0"'
    return (f'\t\t<div class="surface demo-tile u-mb-6"><div class="demo"{style}>\n{demo}\n'
            f'\t\t</div><p class="spec">{spec}</p></div>')


def sec(sid, title, note=''):
    """A section heading (scrollspy-friendly)."""
    n = f'\n\t\t<p class="t-subtle u-mb-6" style="max-width:var(--measure-lead)">{note}</p>' if note else ''
    return (f'\t\t<section id="{sid}"><h2 class="t-h3" style="margin:var(--space-10) 0 var(--space-4)">{title}</h2>{n}')


END = '</section>'


def ct(rows, head=('Class', 'Does')):
    """A class-reference table."""
    tr = '\n'.join(
        f'\t\t\t<tr><td><code class="t-code">{c}</code></td><td>{d}</td></tr>' for c, d in rows)
    return (f'\t\t<div class="surface demo-tile u-mb-6" style="overflow-x:auto"><table class="spec-table" style="width:100%">'
            f'<thead><tr><th>{head[0]}</th><th>{head[1]}</th></tr></thead><tbody>\n{tr}\n\t\t</tbody></table></div>')
