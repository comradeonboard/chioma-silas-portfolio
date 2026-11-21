# Chioma Silas | Portfolio

A static, zero-build portfolio site for **Chioma Silas** — medical student,
AI automation learner, content creator, romance writer and founder of
**Oma AI and Tech** and **Omas Empire**.

Plain HTML, CSS and vanilla JavaScript: no dependencies, no toolchain, no
install step.

## Preview locally

**Easiest:** open `index.html` directly in the browser (or use "Open with Live
Server" in VSCodium).

**Or serve it** (recommended, matches production paths):

```bash
python3 -m http.server 8000
# visit http://localhost:8000
```

## Pages

| File | Page | Content |
|---|---|---|
| `index.html` | Home | Hero, profile summary, key figures, four pillars, section index, contact CTA |
| `about.html` | About | Full biography, timeline, approach |
| `expertise.html` | Expertise | Six capability areas plus secondary skills |
| `ventures.html` | Ventures | Oma AI and Tech, Omas Empire, fiction, ghostwriting, YouTube automation |
| `writing.html` | Writing | Romance fiction, ghostwriting, process and work in progress |
| `contact.html` | Contact | Location, availability and contact details (pending) |
| `404.html` | Not found | Custom error page |

## Structure

```
index.html / about.html / ...   one file per page
404.html                        custom not-found page
assets/css/styles.css           design tokens and all styles
assets/js/main.js               theme, mobile menu, scroll reveals, counters
assets/img/og-cover.png         social sharing image
sitemap.xml, robots.txt         search engine files
.github/workflows/deploy.yml    auto-deploy to GitHub Pages on push to main
```

## Editing

Each page is a complete, self-contained HTML file. The header and footer are
repeated in every page, so if you add or rename a navigation item, update the
`<nav>` block in all seven pages (and the `aria-current="page"` marker on the
page you're editing).

The design uses:

- **Fraunces** for display type and **Inter** for body text (Google Fonts).
- A warm ivory and plum palette, with a dark theme remembered per visitor.
- Responsive layout from 320px up, and support for `prefers-reduced-motion`.
- No external JavaScript libraries.

## Deploying (GitHub Pages)

Every push to `main` publishes via `.github/workflows/deploy.yml`. Set
**Settings → Pages → Source: GitHub Actions** once, then push.

Live URL: `https://comradeonboard.github.io/chioma-silas-portfolio/`

## Content notes

- No photographs were supplied, so the hero uses a typographic "focus panel"
  instead of an image. A portrait can be added later without changing the
  layout.
- Contact details (email, WhatsApp, social handles) are **not yet published**.
  See `TODO-CONTENT.md` before sharing the site widely.
- All claims are limited to the information Chioma supplied: medical student,
  AI automation training, content and video, romance writing and ghostwriting,
  Oma AI and Tech, and Omas Empire.
