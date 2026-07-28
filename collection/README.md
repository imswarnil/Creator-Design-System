# Collections

A collection is a kind of thing a creator publishes — travel, courses, a video
series, a shop. Each one gets a folder here holding the routes it needs, the
sections those routes are built from, and one stylesheet of components written
entirely in the system's tokens.

The point of doing it this way: a collection is not a new design. It is the same
tokens, the same cards, the same type scale, arranged for a different subject.
If a collection needs a colour or a spacing the system does not have, that is a
question about the system, not a licence to invent one here.

```
collection/
  README.md          ← this file: the shared contract
  collection.css     ← the col- vocabulary: every section, defined once
  collection.js      ← the linked filters — the only thing CSS cannot do
  shell.py           ← the head, navbar and footer every route shares

  _default/          ← the starting point. cp -r it and rename
    build.py         ← five routes with no subject in them
    *.html

  travel/            ← the first collection
    travel.css       ← only what travel needs: globe, flight line, palm
    build.py
    *.html           ← index, region, country, trip, post, components

  blog/              ← the second
    build.py         ← no CSS of its own — which is the test
    *.html           ← index, post

  course/            ← the third
    course.css       ← the syllabus scene, the level meter, the quiz, the cert
    build.py
    *.html           ← index, track, topic, course, lesson, components
```

**Blog ships no stylesheet, deliberately.** If a second collection cannot be
built out of the shared vocabulary, then the vocabulary was really just the
first collection wearing a general-sounding prefix. Travel keeps 44 lines,
because a globe and a palm genuinely do belong to travel.

**Course was the one that grew the vocabulary.** Its post route has a video in
it rather than prose, and five sections were missing for that — the stage, the
stage bar, the playlist, the transcript and the panels. They are shared rather
than course-shaped because a podcast season and a video series want every one
of them. What stayed in `course.css` is the four things nothing else wants: the
syllabus scene, the difficulty meter, the knowledge check and the certificate.

Starting a new one:

```bash
cp -r collection/_default collection/podcast
python3 collection/podcast/build.py
```

Then change the lists at the top of its `build.py`. Nothing below that line
refers to the subject.

## The five routes every collection has

Every collection answers the same five questions, so every collection has the
same five routes. The names change; the shape does not.

| Route | Question it answers | Travel | Course |
| --- | --- | --- | --- |
| **index** | what is here? | `/travel` | `/course` |
| **group** | what is here, of this kind? | `/travel/asia` | `/course/layout` |
| **place** | what is here, about this one thing? | `/travel/japan` | `/course/topic/grid` |
| **series** | what is here, in order? | `/travel/india-2026` | `/course/css-from-scratch` |
| **post** | the thing itself | `/travel/getting-a-visa` | `/course/…/grid-in-four-rules` |

A **series** is the one worth being careful about. It is an ordered set of posts
that were made as one body of work — a trip, a course, a season. A **group** is
an unordered set that share an attribute — a region, a subject, a tag. They look
similar and behave differently: a series has a first and a last and a progress
through it; a group has neither.

Course is the clearest case of it. **A course is a series** — first lesson, last
lesson, a percentage through it. **A track is a group** — it has no first course
and nothing to be halfway through. Getting those two the wrong way round is what
produces a course page with a grid of lessons on it.

## Sections

The vocabulary a route is assembled from. Every section is a block you can drop
into any route of any collection — that is what makes them worth having.

Add to this table as sections are built. A section is only "done" when it works
in both themes, at every width, and with no JavaScript unless it is listed as
needing it.

| Section | Class | Used on | Needs JS | Status |
| --- | --- | --- | --- | --- |
| Collection hero | `.col-hero` | index | no | ✅ travel |
| Search + call to action | `.col-search` | index, group | no | ✅ travel |
| Meta strip | `.col-meta` | index, group, series | no | ✅ travel |
| Group cards | `.col-groups` | index | no | ✅ travel |
| Place cards | `.col-places` | index, group | no | ✅ travel |
| Spot chips | `.col-spots` | index, group, place | no | ✅ travel |
| Linked filters | `.col-filters` | index, group | **yes** | ✅ travel |
| Facet sidebar | `.col-facets` | index, group | **yes** | ✅ travel |
| Series card | `.col-series` | index, place | no | ✅ travel |
| Featured | `.col-featured` | index | no | ✅ travel |
| Post list | `.col-posts` | everywhere | no | ✅ travel |
| Ordered series | `.col-order` | series | no | ✅ travel |
| Post header | `.col-post__head` | post | no | ✅ travel |
| Post body + rail | `.col-post` | post | no | ✅ travel |
| Next in series | `.col-next` | post, series | no | ✅ travel |
| Rail + widget | `.col-rail`, `.col-widget` | post | no | ✅ blog |
| Author | `.col-author` | post | no | ✅ blog |
| Numbered list | `.col-mini` | widgets | no | ✅ blog |
| Tags | `.col-tags`, `.col-tag` | post, index | no | ✅ blog |
| Contents | `.col-toc` | post | scrollspy only | ✅ blog |
| Reading progress | `.col-progress` | post | **yes** | ✅ blog |
| Player stage | `.col-stage` | post | no | ✅ course |
| Stage bar | `.col-stagebar` | post | no | ✅ course |
| Playlist | `.col-playlist` | post | no | ✅ course |
| Transcript | `.col-transcript` | post | no | ✅ course |
| Panels | `.col-panel` | post | **yes** | ✅ course |
| Outcomes | `.col-checks` | series, place | no | ✅ course |
| Offer | `.col-offer` | series | no | ✅ course |
| Files | `.col-files` | post, series | no | ✅ course |
| Shortcuts | `.col-keys` | post | no | ✅ course |
| Note composer | `.col-note` | post | no | ✅ course |
| Resume | `.col-resume` | index | no | ✅ course |
| Map | `.col-map` | index, group | — | planned |
| Gallery | `.col-gallery` | place, post | — | planned |
| Cost / stats table | `.col-figures` | place, series | — | planned |

## Rules

1. **Tokens only.** Every value in a collection stylesheet is a `var(--…)`. No
   hex, no px outside a border hairline. A collection that hard-codes a colour
   cannot be rebranded and has quietly left the system.
2. **Prefix once.** Sections are `col-`; a collection's own extras are prefixed
   with the collection (`trv-`). If something turns out to be useful to a second
   collection, it graduates from `trv-` to `col-`.
3. **Reuse before adding.** A place card is a `.card`. A post row is a
   `.c` collection card. If a section is 90% an existing component, it *is* that
   component with a modifier.
4. **JavaScript is additive.** The filters degrade to showing everything. A
   route must be readable and navigable with the script blocked.
5. **State in ARIA.** Filters use `aria-pressed`; the current item uses
   `aria-current`. Never an `.active` class.
