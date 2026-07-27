from common import tile, sec, END, ct

PAGES = {}

PAGES['forms'] = ('Forms overview',
    'A field is the component: label + control + hint + error, one unit that knows about itself. '
    'Every control is exactly as tall as a button, so forms and actions line up without shimming.',
    tile('<div class="field" style="max-width:24rem"><label class="label" for="fo-1">Email</label>'
         '<input class="input" id="fo-1" type="email" placeholder="you@domain.com" />'
         '<p class="hint">Where the build log lands. One send a week.</p></div>',
         '<b>.field &gt; .label + .input + .hint</b> — the unit')
    + tile('<div class="field" style="max-width:24rem"><label class="label" for="fo-2">Email</label>'
           '<input class="input" id="fo-2" type="email" value="swarnil@" aria-invalid="true" aria-describedby="fo-2e" />'
           '<p class="error-text" id="fo-2e">Add a domain after the @ to finish this address.</p></div>',
           'error state — <b>aria-invalid + aria-describedby</b> drive the styling, never a class alone')
    + ct([('.field', 'label + control + hint/error stack'),
          ('.label / .label-optional', 'the name; optional marks itself, required doesn\'t'),
          ('.hint / .error-text', 'one line under the control — never both at once'),
          ('.fieldset', 'grouped controls with a legend'),
          ('.form-row', 'side-by-side fields that stack on small screens')]))

PAGES['form-control'] = ('Form control',
    'Text inputs and textareas, in every state.',
    tile('<div class="stack-sm" style="max-width:26rem">'
         '<input class="input" type="text" placeholder="Default" />'
         '<input class="input" type="text" value="Filled value" />'
         '<input class="input" type="text" placeholder="Disabled" disabled />'
         '<input class="input" type="text" value="Read only" readonly />'
         '<textarea class="textarea" rows="3" placeholder="Textarea — grows with the field, never the page"></textarea>'
         '</div>',
         '<b>.input · .textarea</b> — default, filled, disabled, readonly')
    + tile('<div class="input-search" style="max-width:26rem"><svg class="icon" aria-hidden="true"><use href="#i-search"/></svg>'
           '<input class="input" type="search" placeholder="Search the docs…" aria-label="Search" /></div>',
           '<b>.input-search</b> — the icon rides inside the control'))

PAGES['select'] = ('Select',
    'The native element, dressed. Never a div pretending to be one.',
    tile('<div class="stack-sm" style="max-width:24rem">'
         '<select class="select" aria-label="Collection"><option>All collections</option><option>Videos</option><option>Courses</option><option>Travel</option></select>'
         '<select class="select" disabled aria-label="Disabled"><option>Disabled</option></select>'
         '</div>',
         '<b>.select</b> — chevron drawn in CSS, color-scheme aware')
    + tile('<div class="field" style="max-width:24rem"><label class="label" for="se-1">Sort by</label>'
           '<select class="select" id="se-1"><option>Newest first</option><option>Longest watch time</option><option>A → Z</option></select>'
           '<p class="hint">Sorting is remembered per collection.</p></div>',
           'inside a <b>.field</b>, like every other control'))

PAGES['checks-radios'] = ('Checks & radios',
    'Native inputs restyled — the accessibility tree never lies. The switch is a checkbox wearing motion.',
    tile('<div class="stack-sm">'
         '<label class="check"><input type="checkbox" checked /> <span>Email me new build logs</span></label>'
         '<label class="check"><input type="checkbox" /> <span>Also the newsletter</span></label>'
         '<label class="check"><input type="checkbox" disabled /> <span class="u-fg-faint">Disabled option</span></label>'
         '</div>',
         '<b>.check</b> — checkbox + label as one hit target')
    + tile('<fieldset class="fieldset u-border-0 u-p-0 u-m-0"><legend class="label u-mb-2">Watch quality</legend><div class="stack-sm">'
           '<label class="radio"><input type="radio" name="cr-q" checked /> <span>Auto (recommended)</span></label>'
           '<label class="radio"><input type="radio" name="cr-q" /> <span>1080p60 always</span></label>'
           '<label class="radio"><input type="radio" name="cr-q" /> <span>Data saver</span></label>'
           '</div></fieldset>',
           '<b>.radio</b> — grouped by a real fieldset + legend')
    + tile('<div class="stack-sm">'
           '<label class="switch"><input type="checkbox" checked /> Autoplay next lesson</label>'
           '<label class="switch"><input type="checkbox" /> Reduced-motion previews</label>'
           '</div>',
           '<b>.switch</b> — a checkbox with a thumb; state stays in the input'))

PAGES['range'] = ('Range',
    'One slider, the accent fills to the thumb. Set --value inline (or from JS) for the filled track.',
    tile('<div class="stack" style="max-width:26rem">'
         '<label class="label" for="rg-1">Playback position</label>'
         '<input class="range" id="rg-1" type="range" min="0" max="100" value="35" style="--value:35%" '
         'oninput="this.style.setProperty(\'--value\', this.value + \'%\')" />'
         '<div class="row-between t-slate-sm"><span>00:00</span><span>14:22</span></div>'
         '</div>',
         '<b>.range</b> — accent-filled track, ringed thumb')
    + tile('<input class="range" type="range" value="60" style="--value:60%;max-width:26rem" disabled />',
           'disabled — half opacity, cursor says so'))

PAGES['input-group'] = ('Input group',
    'A control with something welded to its edge: a prefix, a suffix, a button.',
    tile('<div class="stack-sm" style="max-width:28rem">'
         '<div class="input-group"><span class="input-group__text">https://</span><input class="input" type="text" value="swarnil.com" aria-label="URL" /></div>'
         '<div class="input-group"><input class="input" type="email" placeholder="you@domain.com" aria-label="Email" /><button class="btn btn-primary" type="button">Subscribe</button></div>'
         '<div class="input-group"><span class="input-group__text">€</span><input class="input" type="number" value="49" aria-label="Price" /><span class="input-group__text">/ mo</span></div>'
         '</div>',
         '<b>.input-group</b> — controls fuse, inner radii drop, one border'))

PAGES['floating-labels'] = ('Floating labels',
    'The label rests where the value will be, then retreats to a slate caption on focus or fill. '
    'The placeholder must be a single space — :placeholder-shown does the driving.',
    tile('<div class="stack-sm" style="max-width:26rem">'
         '<label class="float-field"><input class="input" type="email" placeholder=" " /><span class="float-field__label">Email address</span></label>'
         '<label class="float-field"><input class="input" type="text" placeholder=" " value="Swarnil Singhai" /><span class="float-field__label">Name</span></label>'
         '<label class="float-field"><textarea class="textarea" rows="3" placeholder=" "></textarea><span class="float-field__label">Message</span></label>'
         '</div>',
         '<b>.float-field &gt; .input + .float-field__label</b> — empty, filled, textarea'))

PAGES['form-layout'] = ('Form layout',
    'Rows that pair, fieldsets that group, and the one-line subscribe. Forms compose from the same '
    'gap ladder as everything else.',
    tile('<form class="stack" style="max-width:34rem" onsubmit="return false">'
         '<div class="form-row">'
         '<div class="field"><label class="label" for="fl-1">First name</label><input class="input" id="fl-1" type="text" /></div>'
         '<div class="field"><label class="label" for="fl-2">Last name</label><input class="input" id="fl-2" type="text" /></div>'
         '</div>'
         '<div class="field"><label class="label" for="fl-3">Email</label><input class="input" id="fl-3" type="email" placeholder="you@domain.com" /></div>'
         '<div class="field"><label class="label" for="fl-4">Topic</label><select class="select" id="fl-4"><option>Sponsorship</option><option>Collab</option><option>Just saying hi</option></select></div>'
         '<label class="check"><input type="checkbox" checked /> <span>Reply by email, not a call</span></label>'
         '<div class="cluster-sm"><button class="btn btn-primary" type="submit">Send it</button><button class="btn btn-quiet" type="reset">Clear</button></div>'
         '</form>',
         '<b>.form-row</b> pairs fields · actions cluster at the end, primary first'))
