# Cadence — Landing Page

A variation of the "Template Name Here" Figma design — a sales-coaching / call-analytics
SaaS landing page. Rebuilt as a clean, responsive, self-contained static site.

## What's inside
- `index.html` — full page markup (nav, hero, problem/solution, feature grid, steps,
  testimonial, integrations, pricing, FAQ, final CTA, footer)
- `styles.css` — design tokens + all styling (Inter typeface, light theme with dark
  accent sections, indigo accent)
- `script.js` — mobile nav toggle + single-open FAQ accordion

## How it varies from the source
- Reworked product as **"Cadence"** with original copy
- Light/dark sectioning with rounded dark panels and a radial-gradient CTA
- Interactive dashboard mock in the hero (talk ratio / win rate / ramp stats + coaching card)
- "Without vs. With" comparison block in place of a plain problem statement
- 3-step "how it works" flow and a 3-tier pricing table with a featured plan

## Run it
Just open `index.html` in a browser, or serve the folder:

```bash
cd landing
python3 -m http.server 8000
# visit http://localhost:8000
```

No build step or dependencies — only Inter is loaded from Google Fonts.
