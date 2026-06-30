#!/usr/bin/env python3
"""
Brain Code Camp — Carbon Design System static site builder.

Usage:
    pip install markdown pyyaml
    python build.py

Output: _site/
"""

import os, re, shutil, html, json
from pathlib import Path
import yaml

try:
    import markdown
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False
    print("⚠  markdown not installed. Run: pip install markdown")

try:
    import nbformat
    from nbconvert import HTMLExporter
    from nbconvert.preprocessors import ExecutePreprocessor
    HAS_NBCONVERT = True
except ImportError:
    HAS_NBCONVERT = False

BASE = Path(__file__).parent
OUT  = BASE / "_site"

# ── TOC ──────────────────────────────────────────────────────────────────────

def load_toc():
    with open(BASE / "_toc.yml") as f:
        return yaml.safe_load(f)

def flatten_toc(toc):
    """Return ordered list of dicts: {file, label, depth, part}."""
    pages = []

    def add(file, depth, part):
        pages.append({"file": file, "depth": depth, "part": part, "title": None})

    root = toc.get("root", "intro")
    add(root, 0, None)

    for part in toc.get("parts", []):
        cap = part.get("caption", "")
        for ch in part.get("chapters", []):
            _walk(ch, 1, cap, add)

    return pages

def _walk(node, depth, part, add_fn):
    add_fn(node["file"], depth, part)
    for sec in node.get("sections", []):
        _walk(sec, depth + 1, part, add_fn)

# ── Title extraction ─────────────────────────────────────────────────────────

def extract_title(file_path):
    """Pull the first # heading from a .md file."""
    p = BASE / (file_path + ".md")
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    p2 = BASE / (file_path + ".ipynb")
    if p2.exists():
        try:
            nb = json.loads(p2.read_text(encoding="utf-8"))
            for cell in nb.get("cells", []):
                if cell.get("cell_type") == "markdown":
                    for line in "".join(cell.get("source", [])).splitlines():
                        line = line.strip()
                        if line.startswith("# "):
                            return line[2:].strip()
        except Exception:
            pass
    return Path(file_path).stem.replace("_", " ").replace("-", " ").title()

# ── MyST → HTML preprocessing ────────────────────────────────────────────────

_dropdown_id = [0]

def myst_preprocess(text):
    """Convert common MyST/Sphinx directives to plain HTML snippets."""

    # Remove toctree blocks
    text = re.sub(r"```\{toctree\}.*?```", "", text, flags=re.DOTALL)

    # {image} path \n :opt: val
    def rep_image(m):
        path = m.group(1).strip()
        inner = m.group(2)
        alt   = (re.search(r":alt:\s*(.+)", inner) or [None, ""])[1].strip()
        width = (re.search(r":width:\s*(.+)", inner) or [None, ""])[1].strip()
        style = f"max-width:{width};" if width else "max-width:100%;"
        return (
            f'\n<figure class="cds-figure">'
            f'<img src="{path}" alt="{html.escape(alt)}" style="{style}" />'
            f'<figcaption>{html.escape(alt)}</figcaption>'
            f"</figure>\n"
        )
    text = re.sub(r"```\{image\}\s+([^\n]+)\n(.*?)```", rep_image, text, flags=re.DOTALL)

    # Admonitions: note, warning, tip, important, caution, attention, seealso
    ADMONITIONS = {
        "note":      ("ℹ", "note"),
        "warning":   ("⚠", "warning"),
        "caution":   ("⚠", "caution"),
        "attention": ("!", "attention"),
        "tip":       ("✓", "tip"),
        "important": ("★", "important"),
        "seealso":   ("→", "note"),
        "hint":      ("💡", "tip"),
        "error":     ("✕", "attention"),
        "danger":    ("✕", "attention"),
    }
    for kind, (icon, css) in ADMONITIONS.items():
        def rep_admon(m, _icon=icon, _css=css, _kind=kind):
            title_arg = m.group(1).strip() or _kind.capitalize()
            body = m.group(2).strip()
            return (
                f'\n<div class="cds-notification cds-notification--{_css}">'
                f'<div class="cds-notification__icon">{_icon}</div>'
                f'<div class="cds-notification__body">'
                f'<p class="cds-notification__title">{html.escape(title_arg)}</p>'
                f'<div class="cds-notification__content">{body}</div>'
                f"</div></div>\n"
            )
        text = re.sub(
            rf"```\{{{kind}\}}([^\n]*)\n(.*?)```",
            rep_admon, text, flags=re.DOTALL
        )

    # Toggle / dropdown → <details>
    for kind in ("toggle", "dropdown"):
        def rep_toggle(m, _kind=kind):
            _dropdown_id[0] += 1
            title = m.group(1).strip() or "Show / Hide"
            body  = m.group(2).strip()
            return (
                f'\n<details class="cds-accordion">'
                f'<summary class="cds-accordion__heading">{html.escape(title)}</summary>'
                f'<div class="cds-accordion__content">{body}</div>'
                f"</details>\n"
            )
        text = re.sub(
            rf"```\{{{kind}\}}([^\n]*)\n(.*?)```",
            rep_toggle, text, flags=re.DOTALL
        )

    # {code-block} lang  →  standard fenced block
    def rep_codeblock(m):
        lang  = m.group(1).strip()
        inner = m.group(2)
        lines = [l for l in inner.splitlines() if not l.lstrip().startswith(":")]
        return f"\n```{lang}\n" + "\n".join(lines).strip() + "\n```\n"
    text = re.sub(
        r"```\{code-block\}\s+(\w+)\n(.*?)```",
        rep_codeblock, text, flags=re.DOTALL
    )

    # {math} block
    text = re.sub(
        r"```\{math\}([^\n]*)\n(.*?)```",
        lambda m: f'\n<div class="cds-math">$${m.group(2).strip()}$$</div>\n',
        text, flags=re.DOTALL
    )

    # Remove any remaining unknown directives
    text = re.sub(r"```\{[^}]+\}[^\n]*\n.*?```", "", text, flags=re.DOTALL)

    # Fix relative image paths: assets/… → keep as-is (will be copied)
    return text

# ── Markdown → HTML ──────────────────────────────────────────────────────────

MD_EXTS = [
    "fenced_code", "tables", "attr_list", "def_list",
    "footnotes", "toc", "nl2br", "sane_lists",
]

def md_to_html(text):
    if not HAS_MARKDOWN:
        return f"<pre>{html.escape(text)}</pre>"
    preprocessed = myst_preprocess(text)
    return markdown.markdown(preprocessed, extensions=MD_EXTS)

# ── Notebook → HTML ──────────────────────────────────────────────────────────

def nb_to_html(nb_path, file_rel):
    """Convert ipynb → HTML body content."""
    if not HAS_NBCONVERT:
        stem = Path(file_rel).stem
        colab_url = (
            "https://colab.research.google.com/github/"
            f"braincodecamp/brainCodeCamp2026/blob/main/{file_rel}.ipynb"
        )
        return (
            f'<div class="cds-notification cds-notification--note">'
            f'<div class="cds-notification__icon">📓</div>'
            f'<div class="cds-notification__body">'
            f'<p class="cds-notification__title">Jupyter Notebook</p>'
            f'<div class="cds-notification__content">'
            f"<p>This page is a Jupyter Notebook. "
            f"Install <code>nbconvert</code> and rebuild to render it locally:</p>"
            f"<pre><code>pip install nbconvert\npython build.py</code></pre>"
            f'<p><a class="cds-btn cds-btn--primary" href="{colab_url}" '
            f'target="_blank" rel="noopener">Open in Google Colab ↗</a></p>'
            f"</div></div></div>"
        )

    try:
        nb = nbformat.read(str(nb_path), as_version=4)
        exp = HTMLExporter()
        exp.template_name = "basic"
        body, _ = exp.from_notebook_node(nb)
        # strip outer HTML boilerplate from nbconvert
        body = re.sub(r"^.*?<body[^>]*>", "", body, flags=re.DOTALL)
        body = re.sub(r"</body>.*$", "", body, flags=re.DOTALL)
        return body
    except Exception as e:
        return f'<div class="cds-notification cds-notification--warning"><div class="cds-notification__icon">⚠</div><div class="cds-notification__body"><p class="cds-notification__title">Notebook render error</p><div class="cds-notification__content"><p>{html.escape(str(e))}</p></div></div></div>'

# ── Navigation HTML ──────────────────────────────────────────────────────────

def build_nav_html(toc, titles, current_file, root_prefix):
    """Return the <li>…</li> blocks for the side nav."""
    lines = []

    root = toc.get("root", "intro")
    root_title = titles.get(root, "Home")
    root_href  = root_prefix + root + ".html"
    active     = " active" if current_file == root else ""
    lines.append(
        f'<li class="cds-side-nav__item">'
        f'<a class="cds-side-nav__link{active}" href="{root_href}">{html.escape(root_title)}</a>'
        f"</li>"
    )

    for part in toc.get("parts", []):
        cap = part.get("caption", "")
        lines.append(f'<li class="cds-side-nav__category">{html.escape(cap)}</li>')
        for ch in part.get("chapters", []):
            lines.extend(_nav_chapter(ch, titles, current_file, root_prefix, depth=0))

    return "\n".join(lines)

def _nav_chapter(node, titles, current_file, root_prefix, depth):
    file     = node["file"]
    title    = titles.get(file, Path(file).stem.replace("_", " ").title())
    href     = root_prefix + file + ".html"
    sections = node.get("sections", [])
    active   = " active" if current_file == file else ""

    lines = []

    if sections:
        # Parent with children
        open_cls = " open" if _contains_active(node, current_file) else ""
        indent   = "  " * depth
        lines.append(
            f'<li class="cds-side-nav__item{open_cls}">'
            f'<a class="cds-side-nav__link{active}" href="{href}" data-toggle="1">'
            f'{html.escape(title)}'
            f'<svg class="cds-side-nav__chevron" width="12" height="12" viewBox="0 0 12 12" fill="currentColor">'
            f'<path d="M4.5 1.5L9 6l-4.5 4.5-.9-.9L7.2 6 3.6 2.4z"/>'
            f"</svg>"
            f"</a>"
            f'<ul class="cds-side-nav__sub">'
        )
        for sec in sections:
            lines.extend(_nav_chapter(sec, titles, current_file, root_prefix, depth + 1))
        lines.append("</ul></li>")
    else:
        lines.append(
            f'<li class="cds-side-nav__item">'
            f'<a class="cds-side-nav__link{active}" href="{href}">{html.escape(title)}</a>'
            f"</li>"
        )

    return lines

def _contains_active(node, current_file):
    if node["file"] == current_file:
        return True
    for sec in node.get("sections", []):
        if _contains_active(sec, current_file):
            return True
    return False

# ── Breadcrumb ───────────────────────────────────────────────────────────────

def make_breadcrumb(file, titles, toc, root_prefix):
    root   = toc.get("root", "intro")
    crumbs = []
    crumbs.append(
        f'<a href="{root_prefix}{root}.html">{html.escape(titles.get(root, "Home"))}</a>'
        f'<span class="cds-breadcrumb__separator">/</span>'
    )
    # find part caption
    for part in toc.get("parts", []):
        for ch in part.get("chapters", []):
            if _contains_active(ch, file):
                crumbs.append(
                    f'<span>{html.escape(part.get("caption", ""))}</span>'
                    f'<span class="cds-breadcrumb__separator">/</span>'
                )
                break
    title = titles.get(file, Path(file).stem.replace("_", " ").title())
    crumbs.append(f'<span class="cds-breadcrumb__current">{html.escape(title)}</span>')
    return "\n".join(crumbs)

# ── Prev / Next ───────────────────────────────────────────────────────────────

def make_prev_next(file, flat_pages, titles, root_prefix):
    files = [p["file"] for p in flat_pages]
    try:
        idx = files.index(file)
    except ValueError:
        return ""
    parts = []
    if idx > 0:
        prev_f  = files[idx - 1]
        prev_t  = html.escape(titles.get(prev_f, prev_f))
        prev_hr = root_prefix + prev_f + ".html"
        parts.append(
            f'<a class="cds-page-nav__link cds-page-nav__link--prev" href="{prev_hr}">'
            f'<span class="cds-page-nav__label">← Previous</span>'
            f'<span class="cds-page-nav__title">{prev_t}</span>'
            f"</a>"
        )
    if idx < len(files) - 1:
        next_f  = files[idx + 1]
        next_t  = html.escape(titles.get(next_f, next_f))
        next_hr = root_prefix + next_f + ".html"
        parts.append(
            f'<a class="cds-page-nav__link cds-page-nav__link--next" href="{next_hr}">'
            f'<span class="cds-page-nav__label">Next →</span>'
            f'<span class="cds-page-nav__title">{next_t}</span>'
            f"</a>"
        )
    return "\n".join(parts)

# ── Page template ─────────────────────────────────────────────────────────────

PAGE_TMPL = """\
<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{page_title} — Brain Code Camp</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="{root}assets/carbon.css"/>
  <link rel="stylesheet" href="{root}assets/dha-overrides.css"/>
</head>
<body>

<header class="cds-header" role="banner">
  <button class="cds-header__menu-btn" id="nav-toggle" aria-label="Toggle navigation" aria-expanded="true">
    <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
      <rect x="2" y="4"  width="16" height="2"/>
      <rect x="2" y="9"  width="16" height="2"/>
      <rect x="2" y="14" width="16" height="2"/>
    </svg>
  </button>
  <a class="cds-header__name" href="{root}index.html">
    <img src="{root}assets/dha-logo.svg" alt="" class="cds-header__logo" style="height:36px;width:auto;"/>
  </a>
  <div class="cds-header__search" role="search">
    <svg width="16" height="16" viewBox="0 0 32 32" fill="currentColor" aria-hidden="true">
      <path d="M29 27.586l-7.552-7.552A11.018 11.018 0 1 0 19.83 21.63L27.586 29zM13 22a9 9 0 1 1 9-9 9.01 9.01 0 0 1-9 9z"/>
    </svg>
    Search
  </div>
</header>

<div class="cds-header__overlay" id="nav-overlay"></div>

<div class="cds-shell">
  <nav class="cds-side-nav" id="side-nav" aria-label="Side navigation">
    <ul class="cds-side-nav__items">
{nav_html}
    </ul>
  </nav>

  <main class="cds-content" id="main-content" role="main">
    <div class="cds-content__inner">
      <nav class="cds-breadcrumb" aria-label="Breadcrumb">
{breadcrumb}
      </nav>
      <article class="cds-article">
{content}
      </article>
      <nav class="cds-page-nav" aria-label="Page navigation">
{prev_next}
      </nav>
    </div>
  </main>
</div>

<footer class="cds-footer" role="contentinfo">
  คณะแพทยศาสตร์โรงพยาบาลรามาธิบดี มหาวิทยาลัยมหิดล &nbsp;·&nbsp; Ramathibodi Digital Health Academy
</footer>

<script src="{root}assets/carbon-nav.js"></script>
</body>
</html>
"""

# ── Build ─────────────────────────────────────────────────────────────────────

def build():
    toc        = load_toc()
    flat_pages = flatten_toc(toc)

    # Collect titles
    titles = {}
    for p in flat_pages:
        titles[p["file"]] = extract_title(p["file"])

    # Clean output
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # Copy assets
    src_assets = BASE / "assets"
    if src_assets.exists():
        shutil.copytree(src_assets, OUT / "assets")

    # Copy any notebook-related images (from _images or assets subfolders)
    for pattern in ("_images",):
        src = BASE / pattern
        if src.exists():
            shutil.copytree(src, OUT / pattern)

    ok = fail = 0

    for page in flat_pages:
        file = page["file"]   # e.g. "GeneralInfo/schedule"
        depth = len(Path(file).parts) - 1
        root_prefix = "../" * depth if depth > 0 else ""

        # Determine source
        md_src = BASE / (file + ".md")
        nb_src = BASE / (file + ".ipynb")

        if md_src.exists():
            raw_md  = md_src.read_text(encoding="utf-8")
            content = md_to_html(raw_md)
        elif nb_src.exists():
            content = nb_to_html(nb_src, file)
        else:
            content = f"<p>Source file not found: <code>{file}</code></p>"
            fail += 1

        # Build nav (root-relative always, then fix prefix)
        nav_html   = build_nav_html(toc, titles, file, root_prefix)
        breadcrumb = make_breadcrumb(file, titles, toc, root_prefix)
        prev_next  = make_prev_next(file, flat_pages, titles, root_prefix)
        page_title = titles.get(file, "Brain Code Camp")

        html_out = PAGE_TMPL.format(
            page_title=html.escape(page_title),
            root=root_prefix,
            nav_html=nav_html,
            breadcrumb=breadcrumb,
            content=content,
            prev_next=prev_next,
        )

        # Write file
        out_path = OUT / (file + ".html")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html_out, encoding="utf-8")
        ok += 1

    # index.html → redirect to root page
    root_file = toc.get("root", "intro")
    (OUT / "index.html").write_text(
        f'<!DOCTYPE html><html><head><meta charset="utf-8"/>'
        f'<meta http-equiv="refresh" content="0;url={root_file}.html"/>'
        f'<title>Brain Code Camp</title></head>'
        f'<body><a href="{root_file}.html">Brain Code Camp</a></body></html>',
        encoding="utf-8",
    )

    print(f"\n✓  Built {ok} pages → _site/")
    if fail:
        print(f"   {fail} source files missing (placeholders rendered)")
    print(f"   Open: _site/index.html\n")

if __name__ == "__main__":
    build()
