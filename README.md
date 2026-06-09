# ui-design-assets

A design repository for UI/UX projects, design systems, components, and visual assets.

## Ciridae — Marketing Website

A single-page marketing site for **Ciridae**, which builds AI operating systems
for real-economy businesses.

### Design

UI guidelines (color, typography, layout) are mapped from the Figma reference
[Ciridae | Jack](https://www.figma.com/design/Uxmn9Kc2MFgfBqKvap3hI9/Ciridae-%7C-Jack?node-id=82-7120):

| Token        | Value / Mapping                                                   |
| ------------ | ---------------------------------------------------------------- |
| Background   | Deep navy-black `#070a12`                                         |
| Accent       | `#ff5600` (Figma brand / progress orange)                        |
| Display font | Light editorial serif — *IvoryLL* → **Spectral**                 |
| Body font    | Grotesque sans — *MediumLL* → **Inter**                          |
| Label font   | Mono, uppercase, wide tracking — *AeonikFono* → **JetBrains Mono** |

### Stack

Plain, dependency-free static site — no build step required.

- `index.html` — full page markup (navbar → hero → footer)
- `styles.css` — design tokens + all component styling
- `script.js` — sticky nav, mobile menu, scroll reveal, FAQ accordion, card glow

### Run locally

Open `index.html` directly, or serve the folder:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

### Sections

Navbar · Hero · Trust strip · Problem · Solution · What We Do · Who It's For ·
How It Works · Outcomes · Case studies · Testimonials · AI Index · Security ·
Comparison · FAQ · Final CTA · Footer
