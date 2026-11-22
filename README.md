# Chioma Silas | Portfolio

A static, zero-build portfolio site for **Chioma Silas**, nursing student,
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
| `studio.html` | Studio | Three vertical video pieces, AI video and UGC capabilities, TikTok link |
| `writing.html` | Writing | Romance fiction, ghostwriting, process and work in progress |
| `contact.html` | Contact | Location, availability, email, WhatsApp, TikTok, LinkedIn |
| `404.html` | Not found | Custom error page |

## Structure

```
index.html / about.html / ...   one file per page
404.html                        custom not-found page
assets/css/styles.css           design tokens and all styles
assets/js/main.js               theme, mobile menu, scroll reveals, counters, reels
assets/img/og-cover.png         social sharing image
assets/img/studio/              poster frames for the three studio reels
assets/video/                   compressed, web-ready studio clips
sitemap.xml, robots.txt         search engine files
.github/workflows/deploy.yml    auto-deploy to GitHub Pages on push to main
```

## Editing

Each page is a complete, self-contained HTML file. The header and footer are
repeated in every page, so if you add or rename a navigation item, update the
`<nav>` block in all eight pages (and the `aria-current="page"` marker on the
page you're editing).

The design uses:

- **Fraunces** for display type and **Inter** for body text (Google Fonts).
- A warm ivory and rose palette, with a dark theme remembered per visitor.
- Soft drifting colour orbs, gentle card motion and scroll reveals, all disabled
  under `prefers-reduced-motion`.
- Responsive layout from 320px up.
- No external JavaScript libraries.

## Deploying (GitHub Pages)

Every push to `main` publishes via `.github/workflows/deploy.yml`. Set
**Settings → Pages → Source: GitHub Actions** once, then push.

Live URL: `https://comradeonboard.github.io/chioma-silas-portfolio/`

## Content notes

- A portrait supplied by Chioma is used in the hero and on `about.html`, and in
  the social preview image. It can be swapped for a studio portrait later
  without changing the layout.
- Contact details are published on `contact.html`: **chiomasilas92@gmail.com**,
  **+234 907 009 9071** (WhatsApp and phone), **TikTok @oma_automates** and
  **LinkedIn**.
- The Studio page uses three vertical clips supplied by Chioma. Originals stay
  in `media content/` and are excluded from git; compressed copies live in
  `assets/video/` with poster frames in `assets/img/studio/`.
- All claims are limited to the information Chioma supplied: nursing student,
  AI automation training, content and video, romance writing and ghostwriting,
  Oma AI and Tech, and Omas Empire.

## Standalone project

This site is its own repository and folder. It is **not** connected to, built
from, or deployed alongside any other portfolio project in this workspace.
