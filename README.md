# ui-design-assets

A design repository for UI/UX projects, design systems, components, and visual assets.

## Firehorse Agent — marketing page

A cleaned-up build of the Firehorse Agent page from the Figma file
[Apr 1 – Dec 1](https://www.figma.com/design/hRXgqWi8j5q0IEaHKGFvVm/Apr-1---Dec-1?node-id=1225-242)
(page `1225:242`, which holds both the current site capture `1225:243` and the
target frame `1225:468`).

Brief: same copy, same style, cleaned up. So the brand language is unchanged —
navy `#14295b`, rust `#a33b2e`, tan `#e0cc9f`, IBM Plex Serif for headings and
IBM Plex Sans for everything else, and the alternating tinted card rhythm. Every
string on the page is the copy from the Figma frame.

### Files

| Path | What it is |
| --- | --- |
| `index.html` | The page. All artwork is inline SVG. |
| `assets/styles.css` | Page styles. |
| `assets/fonts.css` | IBM Plex Sans + Serif (latin), embedded as data URIs. |
| `build.py` | Inlines the CSS into a single self-contained file. |
| `dist/index.html` | Build output — one file, no external requests. |

Open `index.html` directly, or run `python3 build.py` to regenerate `dist/`.
Add `--fragment` to also emit a scaffolding-free `dist/fragment.html`.

There is no build toolchain and no dependencies — it is HTML and CSS.

### What changed

**Typography.** The original mixed font families mid-page: "Firehorse
Alethiometer" and every footer heading were set in Inter while the other four
card headings used IBM Plex Serif. All headings are IBM Plex Serif now. The
eight ad-hoc sizes (40/32/32/22/18/17/15/14) became one fluid scale.

**Card geometry.** The five feature cards were 955 and 960px wide, 426/489/417/
317/351px tall, with text columns hard-set to 412/415/470/548px — which is why
the paragraphs broke raggedly at different measures. They are now one component
with one padding value and a single `46ch` measure.

**Artwork.** The five illustrations were bitmaps at five unrelated sizes
(238×354 down to 164×174), so stroke weights and visual presence differed card
to card. They are redrawn as inline SVG on a shared 200-unit-tall canvas with a
common stroke width, so they finally read as one set — and they stay sharp at
any resolution.

**The rust heading rule** was a stray absolutely-positioned border on a box
wider than the heading it marked. It is now a border on the heading itself.

**The forms visual** was a 1472×720 flat bitmap with "Unstructured data from
insurance paperwork" baked into the pixels — unselectable, unsearchable, and
soft on retina displays. The caption is live text and the paperwork is vector.

**Hero background.** A fixed 1512px graph-paper bitmap that clipped mid-square.
Drawn in CSS it tiles at any width, and is masked so it fades out rather than
being chopped off.

**Footer.** Five columns hard-positioned at 0 / 234 / 450.89 / 667.79 / 884.69,
with two empty paragraph nodes padding out the contact column. Now a grid.

**Responsive.** The original was a fixed 1512px canvas. This reflows to mobile;
stacked cards always lead with their text so the reading order stays
predictable.

**Accessibility.** Semantic landmarks and headings, a skip link, visible focus
rings, `prefers-reduced-motion` support, and labelled artwork. The attribution
line was `#999` on white (2.9:1 — fails WCAG AA); it is now 5.8:1. Every
text/background pairing on the page passes AA.

**Navigation.** The logo and all five links were crammed against the left edge.
Logo left, nav right, genuinely sticky, with hover and current-page states —
the original signalled "current" only through a `#14295b` vs `#3e4c67` shift
that is nearly invisible.

### Known gap

The horse mark in the header and footer is a **placeholder** drawn to match the
original's line weight and proportions. The real logo lives in the Figma file as
a bitmap on `www.figma.com`, which this environment's network policy blocks, so
it could not be extracted. Drop the real asset into the `<symbol id="fh-logo">`
in `index.html` to swap it — both the navy header copy and the white footer copy
render from that one symbol via `currentColor`.
