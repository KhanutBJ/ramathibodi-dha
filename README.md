# Ramathibodi Digital Health & AI Club

The website for the Ramathibodi Digital Health and AI Club: a club, an academy,
and a fellowship built inside the Faculty of Medicine Ramathibodi Hospital,
Mahidol University.

Tagline: *Pioneering the integration of AI and medicine for better healthcare.*

## What this is

A static site with two surfaces, generated from one design system:

1. **Public venture site** (Ive / Rams / Carbon aesthetic, light and dark themes):
   Home, Who We Are, What We Do, Academy, Fellowship (Apply, Stories,
   Publications, FAQ), Insights, News, Careers, Contact.
2. **Gated Academy reader**: the curriculum (`.md` and `.ipynb`) rendered behind
   a login gate, with a sidebar, breadcrumb, and prev/next.

## Build

```bash
pip install markdown pyyaml nbformat nbconvert
python build.py
```

Output is written to `_site/`. Open `_site/index.html`, or serve it:

```bash
python -m http.server 8899 --directory _site
```

## Architecture

| File | Role |
|------|------|
| `build.py` | Build engine: shared shell, gates, academy reader, markdown + notebook rendering |
| `pages.py` | All long-form marketing copy and page layouts |
| `assets/dha.css` | The design system: brand tokens, light/dark themes, components |
| `assets/dha.js` | Theme toggle, nav, scroll reveal, the client-side login gate |
| `assets/dha-logo-{light,dark}.png` | Theme-aware brand lockups |

The curriculum source lives under `curriculum/` and `notebooks/`. The reader's
order is defined by `ACADEMY_TOC` in `build.py`.

## Access gate

The Academy and Fellowship are gated client-side, which is the only option on a
static host. This is a soft gate, not real security. Codes live in `assets/dha.js`
(`ACCESS`). Replace the gate with a real auth backend before handling anything
sensitive.

Default member codes (change before launch):

- Academy: `RAMA-DHA`
- Fellowship: `RAMA-FELLOW`

## Brand

- Navy `#0e1728`, Purple `#5822a6`, Orange `#f76205`, Indigo `#3412d1`
- Display type: Montserrat (the logo wordmark). Body: Inter. Mono: IBM Plex Mono.
- Accent gradient runs orange to indigo, used sparingly.

## Writing style

No em dashes, no middle dots, no filler. Plain, confident, human prose.

---

Faculty of Medicine Ramathibodi Hospital, Mahidol University
คณะแพทยศาสตร์โรงพยาบาลรามาธิบดี มหาวิทยาลัยมหิดล
