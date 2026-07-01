#!/usr/bin/env python3
"""
Ramathibodi Digital Health & AI Club - static site builder.

Builds two surfaces from one design system:
  1. The public venture site (home, who we are, what we do, insights, news,
     careers, contact, fellowship, academy overview).
  2. The gated Academy reader (curriculum .md / .ipynb behind a login gate).

Usage:
    pip install markdown pyyaml nbformat nbconvert
    python build.py
Output: _site/
"""

import os, re, shutil, html, json, datetime, hashlib
from pathlib import Path

# Cache-busting: /assets/* is served immutable for a year (vercel.json), so a
# changed file must get a new URL or browsers keep the stale copy. Hash content.
def _asset_hash(name):
    try:
        return hashlib.md5(open(os.path.join("assets", name), "rb").read()).hexdigest()[:8]
    except Exception:
        return None
ASSET_VER = {n: _asset_hash(n) for n in
             ("dha.css", "dha.js", "favicon.png", "dha-logo-light.png", "dha-logo-dark.png")}
def av(name):
    v = ASSET_VER.get(name)
    return f"assets/{name}?v={v}" if v else f"assets/{name}"

try:
    import markdown
    HAS_MD = True
except ImportError:
    HAS_MD = False
    print("!  markdown not installed: pip install markdown")

try:
    import nbformat
    from nbconvert import HTMLExporter
    HAS_NB = True
except ImportError:
    HAS_NB = False

BASE = Path(__file__).parent
OUT = BASE / "_site"
YEAR = datetime.date.today().year

SITE = {
    "name": "Ramathibodi Digital Health & AI Club",
    "short": "DHA Club",
    "tagline": "Pioneering the integration of AI and medicine for better healthcare.",
    "org_th": "คณะแพทยศาสตร์โรงพยาบาลรามาธิบดี มหาวิทยาลัยมหิดล",
    "org_en": "Faculty of Medicine Ramathibodi Hospital, Mahidol University",
}

NAV = [
    ("Who We Are", "เกี่ยวกับเรา", "who-we-are.html"),
    ("What We Do", "สิ่งที่เราทำ", "what-we-do.html"),
    ("Academy", "อคาเดมี", "academy.html"),
    ("Platform", "แพลตฟอร์ม", "platform.html"),
    ("Tools", "เครื่องมือ", "tools.html"),
    ("Fellowship", "เฟลโลว์ชิป", "fellowship.html"),
    ("Insights", "บทความ", "insights/index.html"),
]

# ----------------------------------------------------------------------------
# Icons (Carbon-style line icons)
# ----------------------------------------------------------------------------
ICON = {
    "arrow": '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 8h10M9 4l4 4-4 4"/></svg>',
    "brain": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-1 5.8A3 3 0 0 0 9 18a2 2 0 0 0 3 0 2 2 0 0 0 3 0 3 3 0 0 0 4-5.2A3 3 0 0 0 18 7a3 3 0 0 0-3-3 2.5 2.5 0 0 0-3 0 2.5 2.5 0 0 0-3 0Z"/><path d="M12 6v12"/></svg>',
    "flask": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/><path d="M7.5 15h9"/></svg>',
    "rocket": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 15c-1 2-1 4-1 4s2 0 4-1m6-13a9 9 0 0 1 3 7c0 3-2 5-2 5l-4 1-3-3 1-4s2-6 2-6Z"/><circle cx="14" cy="9" r="1.3"/></svg>',
    "compass": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
    "node": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="5" cy="12" r="2.4"/><circle cx="19" cy="6" r="2.4"/><circle cx="19" cy="18" r="2.4"/><path d="M7.2 11l9.6-4M7.2 13l9.6 4"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 13h6M9 17h6"/></svg>',
    "pulse": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 12h4l2-5 4 10 2-5h6"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0M16 5a3 3 0 0 1 0 6M15 20a6 6 0 0 0-1.5-4"/></svg>',
    "moon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" width="18" height="18"><path d="M20 14a8 8 0 1 1-10-10 7 7 0 0 0 10 10Z"/></svg>',
    "sun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" width="18" height="18"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5L19 19M19 5l-1.5 1.5M6.5 17.5L5 19"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" width="22" height="22"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
    "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
    "x": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.9 2H22l-7.1 8.1L23 22h-6.6l-5.2-6.8L5.3 22H2.2l7.6-8.7L1.5 2h6.8l4.7 6.2zm-1.1 18h1.8L7.3 3.9H5.4z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5A2.5 2.5 0 1 1 5 8.5a2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05C20.4 8.65 22 10.7 22 14.1V21h-4v-6.1c0-1.45-.03-3.3-2-3.3s-2.3 1.57-2.3 3.2V21H9z"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.2c-1.2 0-1.6.75-1.6 1.5V12h2.7l-.43 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>',
    "github": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-3.16 19.5c.5.1.68-.22.68-.48v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.45-1.16-1.1-1.47-1.1-1.47-.9-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.9 1.52 2.34 1.08 2.9.83.1-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.26-.45-1.28.1-2.66 0 0 .84-.27 2.75 1.02a9.5 9.5 0 0 1 5 0c1.9-1.29 2.74-1.02 2.74-1.02.55 1.38.2 2.4.1 2.66.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.68-4.57 4.93.36.31.68.92.68 1.85v2.74c0 .27.18.59.69.48A10 10 0 0 0 12 2z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 12s0-3.4-.43-5a2.5 2.5 0 0 0-1.77-1.77C19.2 4.8 12 4.8 12 4.8s-7.2 0-8.8.43A2.5 2.5 0 0 0 1.43 7C1 8.6 1 12 1 12s0 3.4.43 5a2.5 2.5 0 0 0 1.77 1.77C4.8 19.2 12 19.2 12 19.2s7.2 0 8.8-.43A2.5 2.5 0 0 0 22.57 17c.43-1.6.43-5 .43-5zM9.8 15.3V8.7l5.7 3.3z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.85.07 1.17.05 1.8.25 2.23.42.56.22.96.48 1.38.9.42.42.68.82.9 1.38.17.42.37 1.06.42 2.23.06 1.27.07 1.65.07 4.85s0 3.58-.07 4.85c-.05 1.17-.25 1.8-.42 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.17-1.06.37-2.23.42-1.27.06-1.65.07-4.85.07s-3.58 0-4.85-.07c-1.17-.05-1.8-.25-2.23-.42a3.7 3.7 0 0 1-1.38-.9 3.7 3.7 0 0 1-.9-1.38c-.17-.42-.37-1.06-.42-2.23C2.21 15.58 2.2 15.2 2.2 12s0-3.58.07-4.85c.05-1.17.25-1.8.42-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.17 1.06-.37 2.23-.42C8.42 2.21 8.8 2.2 12 2.2zm0 1.8c-3.15 0-3.5.01-4.74.07-.9.04-1.38.19-1.7.32-.43.16-.74.36-1.06.68-.32.32-.52.63-.68 1.06-.13.32-.28.8-.32 1.7C3.44 8.94 3.43 9.3 3.43 12s.01 3.06.07 4.29c.04.9.19 1.38.32 1.7.16.43.36.74.68 1.06.32.32.63.52 1.06.68.32.13.8.28 1.7.32 1.24.06 1.59.07 4.74.07s3.5-.01 4.74-.07c.9-.04 1.38-.19 1.7-.32.43-.16.74-.36 1.06-.68.32-.32.52-.63.68-1.06.13-.32.28-.8.32-1.7.06-1.23.07-1.59.07-4.29s-.01-3.06-.07-4.29c-.04-.9-.19-1.38-.32-1.7a2.85 2.85 0 0 0-.68-1.06 2.85 2.85 0 0 0-1.06-.68c-.32-.13-.8-.28-1.7-.32C15.5 4.01 15.15 4 12 4zm0 3.06A4.94 4.94 0 1 1 12 16.94 4.94 4.94 0 0 1 12 7.06zm0 8.15A3.21 3.21 0 1 0 12 8.79a3.21 3.21 0 0 0 0 6.42zm6.29-8.35a1.15 1.15 0 1 1-2.3 0 1.15 1.15 0 0 1 2.3 0z"/></svg>',
    "discord": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.3 4.9A19.8 19.8 0 0 0 15.4 3.4a.07.07 0 0 0-.08.04c-.2.38-.44.87-.6 1.25a18.3 18.3 0 0 0-5.44 0c-.17-.39-.4-.87-.62-1.25a.08.08 0 0 0-.08-.04A19.7 19.7 0 0 0 3.7 4.9a.07.07 0 0 0-.03.03C.53 9.6-.32 14.16.1 18.66a.08.08 0 0 0 .03.06 19.9 19.9 0 0 0 6 3.03.08.08 0 0 0 .09-.03c.46-.63.87-1.3 1.23-2a.08.08 0 0 0-.04-.11c-.66-.25-1.28-.55-1.88-.9a.08.08 0 0 1-.01-.13l.37-.29a.07.07 0 0 1 .08-.01 14.2 14.2 0 0 0 12.06 0 .07.07 0 0 1 .08.01l.37.29a.08.08 0 0 1-.01.13c-.6.35-1.23.65-1.89.9a.08.08 0 0 0-.04.11c.37.7.78 1.36 1.23 2a.08.08 0 0 0 .09.03 19.8 19.8 0 0 0 6-3.03.08.08 0 0 0 .04-.06c.5-5.2-.84-9.72-3.55-13.73a.06.06 0 0 0-.03-.03zM8.02 15.9c-1.18 0-2.16-1.08-2.16-2.42s.96-2.42 2.16-2.42c1.21 0 2.18 1.1 2.16 2.42 0 1.34-.96 2.42-2.16 2.42zm7.97 0c-1.18 0-2.16-1.08-2.16-2.42s.96-2.42 2.16-2.42c1.21 0 2.18 1.1 2.16 2.42 0 1.34-.95 2.42-2.16 2.42z"/></svg>',
    "line": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 5.64 2 10.13c0 4.02 3.55 7.39 8.35 8.03.32.07.77.21.88.49.1.25.06.64.03.9l-.14.85c-.04.25-.2.99.87.54 1.07-.45 5.75-3.39 7.85-5.8C21.28 13.5 22 11.9 22 10.13 22 5.64 17.52 2 12 2zM8.28 12.7a.2.2 0 0 1-.19.19H5.3a.2.2 0 0 1-.19-.19V8.42c0-.1.09-.19.19-.19h.7c.1 0 .19.09.19.19v3.39h1.9c.1 0 .19.09.19.19v.71zm1.72 0a.2.2 0 0 1-.19.19h-.7a.2.2 0 0 1-.19-.19V8.42c0-.1.09-.19.19-.19h.7c.1 0 .19.09.19.19v4.28zm4.75 0a.19.19 0 0 1-.19.19h-.7a.19.19 0 0 1-.15-.08l-1.96-2.65v2.54a.2.2 0 0 1-.19.19h-.7a.2.2 0 0 1-.19-.19V8.42c0-.1.09-.19.19-.19h.72l.05.02.03.03 1.96 2.65V8.42c0-.1.09-.19.19-.19h.7c.1 0 .19.09.19.19v4.28zm3.81-3.57a.2.2 0 0 1-.19.19h-1.9v.73h1.9c.1 0 .19.09.19.19v.71a.2.2 0 0 1-.19.19h-1.9v.73h1.9c.1 0 .19.09.19.19v.71a.2.2 0 0 1-.19.19h-2.79a.2.2 0 0 1-.19-.19V8.42c0-.1.09-.19.19-.19h2.79c.1 0 .19.09.19.19v.71z"/></svg>',
}

# ----------------------------------------------------------------------------
# Community channels. Paste real URLs here to activate a channel.
# Leave url as "" (empty) to render a "soon" chip instead of a dead link.
# ----------------------------------------------------------------------------
COMMUNITY = [
    ("line",      "LINE",      "",  ("LINE OpenChat", "LINE OpenChat")),
    ("facebook",  "Facebook",  "",  ("Facebook", "เฟซบุ๊ก")),
    ("instagram", "Instagram", "",  ("Instagram", "อินสตาแกรม")),
    ("discord",   "Discord",   "",  ("Discord", "ดิสคอร์ด")),
    ("linkedin",  "LinkedIn",  "",  ("LinkedIn", "ลิงก์ดอิน")),
    ("github",    "GitHub",    "",  ("GitHub", "กิตฮับ")),
    ("youtube",   "YouTube",   "",  ("YouTube", "ยูทูบ")),
]

# ----------------------------------------------------------------------------
# Shell
# ----------------------------------------------------------------------------
def esc(s): return html.escape(s, quote=True)

def bi(en, th):
    """Inline bilingual span. CSS shows one per active [data-lang]."""
    return f'<span class="l-en">{en}</span><span class="l-th">{th}</span>'

def ph(en, th):
    """Plain-text bilingual placeholder attributes. bi() HTML cannot go inside
    an attribute, so we emit data-ph-* and let dha.js swap on language."""
    return f'placeholder="{esc(th)}" data-ph-en="{esc(en)}" data-ph-th="{esc(th)}"'

def nav_links(prefix, active):
    out = []
    for en, th, href in NAV:
        cls = "nav__link is-active" if active == href else "nav__link"
        out.append(f'<a class="{cls}" href="{prefix}{href}">{bi(en, th)}</a>')
    return "\n".join(out)

def mobile_links(prefix):
    return "\n".join(f'<a href="{prefix}{href}">{bi(en, th)}</a>' for en, th, href in NAV)

def shell(title, body, prefix="", active="", desc=None, body_attr=""):
    desc = desc or SITE["tagline"]
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}"/>
<link rel="icon" href="{prefix}{av('favicon.png')}"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,400;1,9..144,500&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Caveat:wght@500;600;700&family=Montserrat:ital,wght@0,600;0,700;0,800;1,700&family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+Thai:wght@400;500;600;700&family=Noto+Serif+Thai:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="{prefix}{av('dha.css')}"/>
<script>(function(){{try{{var t=localStorage.getItem('dha-theme')||((window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light');document.documentElement.setAttribute('data-theme',t);var l=localStorage.getItem('dha-lang')||'th';document.documentElement.setAttribute('data-lang',l);document.documentElement.setAttribute('lang',l);}}catch(e){{}}}})();</script>
</head>
<body{(' ' + body_attr) if body_attr else ''}>
<header class="nav">
  <div class="nav__inner">
    <a class="nav__logo" href="{prefix}index.html" aria-label="{esc(SITE['name'])}">
      <img class="light-only" src="{prefix}{av('dha-logo-light.png')}" alt="{esc(SITE['name'])}"/>
      <img class="dark-only" src="{prefix}{av('dha-logo-dark.png')}" alt="{esc(SITE['name'])}"/>
    </a>
    <nav class="nav__links" aria-label="Primary">
      {nav_links(prefix, active)}
    </nav>
    <div class="nav__actions">
      <button class="lang-toggle" data-lang-toggle aria-label="Switch language">
        <span class="l-en">TH</span><span class="l-th">EN</span>
      </button>
      <button class="theme-toggle" data-theme-toggle aria-label="Toggle colour theme">
        <span class="sun">{ICON['sun']}</span><span class="moon">{ICON['moon']}</span>
      </button>
      <a class="nav__signin" href="{prefix}signin.html">{bi('Sign in', 'เข้าสู่ระบบ')}</a>
      <a class="btn btn--primary" href="{prefix}contact.html" style="padding:.6rem 1.1rem">{bi('Contact', 'ติดต่อ')}</a>
      <button class="nav__burger" data-burger aria-label="Open menu">{ICON['menu']}</button>
    </div>
  </div>
</header>
<div class="mobile-menu">
  {mobile_links(prefix)}
  <a href="{prefix}signin.html">{bi('Sign in', 'เข้าสู่ระบบ')}</a>
  <a href="{prefix}contact.html">{bi('Contact', 'ติดต่อเรา')}</a>
</div>
<main id="top">
{body}
</main>
{footer(prefix)}
<script src="{prefix}{av('dha.js')}"></script>
</body>
</html>"""

def footer(prefix):
    cols = [
        (("Main Menu", "เมนูหลัก"), [
            (("Who We Are", "เกี่ยวกับเรา"), "who-we-are.html"),
            (("What We Do", "สิ่งที่เราทำ"), "what-we-do.html"),
            (("Academy", "อคาเดมี"), "academy.html"),
            (("Platform", "แพลตฟอร์ม"), "platform.html"),
            (("Tools", "เครื่องมือ"), "tools.html"),
            (("Fellowship", "เฟลโลว์ชิป"), "fellowship.html"),
            (("Venture Studio", "เวนเจอร์สตูดิโอ"), "venture.html"),
            (("Sign in", "เข้าสู่ระบบ"), "signin.html"),
        ]),
        (("Resources", "แหล่งข้อมูล"), [
            (("Insights", "บทความ"), "insights/index.html"),
            (("News", "ข่าวสาร"), "news/index.html"),
            (("Team", "ทีมงาน"), "team.html"),
            (("Annual Report", "รายงานประจำปี"), "annual-report.html"),
            (("Publications", "ผลงานตีพิมพ์"), "fellowship/publications.html"),
            (("Stories", "เรื่องราว"), "fellowship/stories.html"),
            (("FAQ", "คำถามที่พบบ่อย"), "fellowship/faq.html"),
        ]),
        (("Connect", "ติดต่อและร่วมงาน"), [
            (("Contact", "ติดต่อเรา"), "contact.html"),
            (("Careers", "ร่วมงานกับเรา"), "careers.html"),
            (("Partner with us", "เป็นพันธมิตร"), "contact.html"),
            (("Code of Conduct", "จรรยาบรรณ"), "about/conduct.html"),
            (("Privacy (PDPA)", "ความเป็นส่วนตัว PDPA"), "about/privacy.html"),
        ]),
    ]
    col_html = ""
    for (h_en, h_th), links in cols:
        items = "".join(f'<li><a href="{prefix}{href}">{bi(l_en, l_th)}</a></li>' for (l_en, l_th), href in links)
        col_html += f'<div><h4>{bi(h_en, h_th)}</h4><ul>{items}</ul></div>'

    socials = "".join(
        (f'<a class="social" href="{url}" target="_blank" rel="noopener" aria-label="{name}">{ICON[ic]}</a>'
         if url else
         f'<span class="social social--soon" role="img" aria-label="{name} (coming soon)" title="{name} coming soon">{ICON[ic]}</span>')
        for ic, name, url, _lab in COMMUNITY)

    newsletter = f"""
      <div class="footer__news">
        <h4>{bi("Stay up to date", "ติดตามข่าวสาร")}</h4>
        <form class="news-form" onsubmit="event.preventDefault();this.querySelector('.news-msg').textContent=(document.documentElement.getAttribute('data-lang')==='th'?'ขอบคุณครับ ระบบสาธิต เชื่อมต่ออีเมลจริงก่อนเปิดใช้':'Thanks. Demo form, wire it to a real list before launch.');">
          <input type="email" required {ph('Your email', 'อีเมลของคุณ')} aria-label="Email"/>
          <button class="btn btn--grad" type="submit">{bi("Subscribe", "สมัคร")}</button>
        </form>
        <div class="news-msg muted" style="font-size:.8rem;min-height:1em;margin-top:.5rem"></div>
        <div class="socials">{socials}</div>
      </div>"""

    return f"""<footer class="footer">
  <div class="container">
    <div class="footer__grid footer__grid--rich">
      <div class="footer__brand">
        <img class="light-only" src="{prefix}{av('dha-logo-light.png')}" alt="{esc(SITE['name'])}"/>
        <img class="dark-only" src="{prefix}{av('dha-logo-dark.png')}" alt="{esc(SITE['name'])}" style="display:none"/>
        <p>{bi('The Ramathibodi Digital Health and AI Club trains the next generation of Thailand&#39;s medical AI builders, inside the Faculty of Medicine Ramathibodi Hospital, Mahidol University.', 'ชมรมสุขภาพดิจิทัลและปัญญาประดิษฐ์รามาธิบดี บ่มเพาะคนรุ่นใหม่ผู้สร้าง AI ทางการแพทย์ของไทย ภายใต้คณะแพทยศาสตร์โรงพยาบาลรามาธิบดี มหาวิทยาลัยมหิดล')}</p>
        <p class="sig" style="margin-top:var(--s3)">{bi('Made by hand, in Bangkok.', 'สร้างด้วยมือ ในกรุงเทพฯ')}</p>
      </div>
      {col_html}
      {newsletter}
    </div>
    <div class="footer__bottom">
      <span>© {YEAR} {esc(SITE['name'])}</span>
      <span>{bi("Built in Bangkok for Thailand&#39;s health system.", "สร้างในกรุงเทพ เพื่อระบบสุขภาพของไทย")}</span>
    </div>
  </div>
</footer>"""

# ----------------------------------------------------------------------------
# Section helpers
# ----------------------------------------------------------------------------
def card(icon, title, body, link=None, link_label="Learn more", prefix="", d=0):
    lk = f'<a class="card__link" href="{prefix}{link}">{link_label} {ICON["arrow"]}</a>' if link else ""
    dd = f' data-d="{d}"' if d else ""
    return f"""<div class="card reveal"{dd}>
  <div class="card__icon">{ICON.get(icon, ICON['node'])}</div>
  <h3>{title}</h3><p>{body}</p>{lk}
</div>"""

def stat(num, label):
    return f'<div class="reveal"><div class="stat__num">{num}</div><div class="stat__label">{label}</div></div>'

def community_block(prefix="", eyebrow=None, title=None, sub=None):
    """A 'Join the community' band with channel cards, driven by COMMUNITY."""
    eyebrow = eyebrow or bi("Community", "ชุมชน")
    title = title or bi("Join the club.", "เข้าร่วมชมรม")
    sub = sub or bi(
        "We build in the open and we learn together. Come in through whichever door is yours.",
        "เราสร้างงานอย่างเปิดเผยและเรียนรู้ไปด้วยกัน เข้ามาทางประตูไหนก็ได้ที่ใช่สำหรับคุณ")
    cards = ""
    for ic, name, url, (l_en, l_th) in COMMUNITY:
        label = bi(l_en, l_th)
        if url:
            cta = f'<span class="chan__go">{bi("Join", "เข้าร่วม")} {ICON["arrow"]}</span>'
            cards += (f'<a class="chan reveal" href="{url}" target="_blank" rel="noopener">'
                      f'<span class="chan__ic chan__ic--{ic}">{ICON[ic]}</span>'
                      f'<span class="chan__name">{label}</span>{cta}</a>')
        else:
            cta = f'<span class="chan__go chan__go--soon">{bi("Coming soon", "เร็ว ๆ นี้")}</span>'
            cards += (f'<div class="chan chan--soon reveal">'
                      f'<span class="chan__ic chan__ic--{ic}">{ICON[ic]}</span>'
                      f'<span class="chan__name">{label}</span>{cta}</div>')
    return f"""
<section class="section"><div class="container">
  <div class="section-head reveal"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2><p class="lead measure mt3">{sub}</p></div>
  <div class="chan-grid">{cards}</div>
</div></section>"""

# ----------------------------------------------------------------------------
# Markdown / MyST -> HTML  (kept from prior build)
# ----------------------------------------------------------------------------
def myst(text):
    text = re.sub(r"```\{toctree\}.*?```", "", text, flags=re.DOTALL)
    def rep_image(m):
        path = m.group(1).strip()
        inner = m.group(2)
        alt = (re.search(r":alt:\s*(.+)", inner) or [None, ""])[1].strip()
        width = (re.search(r":width:\s*(.+)", inner) or [None, ""])[1].strip()
        style = f"max-width:{width};" if width else "max-width:100%;"
        return f'\n<figure><img src="{path}" alt="{esc(alt)}" style="{style}"/><figcaption>{esc(alt)}</figcaption></figure>\n'
    text = re.sub(r"```\{image\}\s+([^\n]+)\n(.*?)```", rep_image, text, flags=re.DOTALL)
    ADM = {"note": "note", "warning": "warning", "tip": "tip", "important": "important",
           "caution": "warning", "seealso": "note", "hint": "tip"}
    for kind, css in ADM.items():
        def rep(m, _css=css, _k=kind):
            t = m.group(1).strip() or _k.capitalize()
            return f'\n<div class="callout callout--{_css}"><strong>{esc(t)}</strong><div>{m.group(2).strip()}</div></div>\n'
        text = re.sub(rf"```\{{{kind}\}}([^\n]*)\n(.*?)```", rep, text, flags=re.DOTALL)
    for kind in ("toggle", "dropdown"):
        def rept(m):
            return f'\n<details class="callout"><summary>{esc(m.group(1).strip() or "Show")}</summary><div>{m.group(2).strip()}</div></details>\n'
        text = re.sub(rf"```\{{{kind}\}}([^\n]*)\n(.*?)```", rept, text, flags=re.DOTALL)
    def repcb(m):
        lines = [l for l in m.group(2).splitlines() if not l.lstrip().startswith(":")]
        return f"\n```{m.group(1).strip()}\n" + "\n".join(lines).strip() + "\n```\n"
    text = re.sub(r"```\{code-block\}\s+(\w+)\n(.*?)```", repcb, text, flags=re.DOTALL)
    text = re.sub(r"```\{[^}]+\}[^\n]*\n.*?```", "", text, flags=re.DOTALL)
    text = text.replace("](", "](")  # noop keep links
    return text

MD_EXTS = ["fenced_code", "tables", "attr_list", "def_list", "footnotes", "toc", "sane_lists"]
def md_html(text):
    if not HAS_MD:
        return f"<pre>{esc(text)}</pre>"
    return markdown.markdown(myst(text), extensions=MD_EXTS)

def nb_html(nb_path):
    """Render an .ipynb directly to styled HTML. No nbconvert dependency."""
    try:
        nb = json.loads(Path(nb_path).read_text(encoding="utf-8"))
    except Exception as e:
        return f'<div class="callout callout--warning"><strong>Notebook error</strong><div>{esc(str(e))}</div></div>'

    def src(cell):
        s = cell.get("source", [])
        return "".join(s) if isinstance(s, list) else s

    parts = []
    for cell in nb.get("cells", []):
        kind = cell.get("cell_type")
        if kind == "markdown":
            parts.append(md_html(src(cell)))
        elif kind == "code":
            code = src(cell)
            if code.strip():
                parts.append(
                    '<div class="nb-cell"><div class="nb-in">'
                    f'<pre><code>{esc(code)}</code></pre></div>'
                )
            else:
                parts.append('<div class="nb-cell">')
            for out in cell.get("outputs", []):
                parts.append(render_output(out))
            parts.append("</div>")
    return "\n".join(parts)

def render_output(out):
    ot = out.get("output_type")
    if ot == "stream":
        text = "".join(out.get("text", []))
        return f'<pre class="nb-out">{esc(text)}</pre>' if text.strip() else ""
    if ot in ("execute_result", "display_data"):
        data = out.get("data", {})
        if "image/png" in data:
            b64 = data["image/png"]
            if isinstance(b64, list):
                b64 = "".join(b64)
            return f'<div class="nb-out nb-out--img"><img src="data:image/png;base64,{b64.strip()}" alt="output"/></div>'
        if "text/html" in data:
            html_out = data["text/html"]
            return "".join(html_out) if isinstance(html_out, list) else html_out
        if "text/plain" in data:
            text = "".join(data["text/plain"])
            return f'<pre class="nb-out">{esc(text)}</pre>'
    if ot == "error":
        tb = esc("\n".join(out.get("traceback", [])))
        tb = re.sub(r"\x1b\[[0-9;]*m", "", tb)  # strip ANSI colour codes
        return f'<pre class="nb-out nb-out--err">{tb}</pre>'
    return ""

def first_h1(path):
    if path.suffix == ".md" and path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("# "):
                return line.strip()[2:].strip()
    if path.suffix == ".ipynb" and path.exists():
        try:
            nb = json.loads(path.read_text(encoding="utf-8"))
            for c in nb.get("cells", []):
                if c.get("cell_type") == "markdown":
                    for line in "".join(c.get("source", [])).splitlines():
                        if line.strip().startswith("# "):
                            return line.strip()[2:].strip()
        except Exception:
            pass
    return path.stem.replace("-", " ").replace("_", " ").title()

# ----------------------------------------------------------------------------
# Page bodies are defined in pages.py-style functions imported below
# ----------------------------------------------------------------------------
import pages  # noqa: E402  (separate module holds the long-form copy)

def write(rel, content):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(BASE / "assets", OUT / "assets")

    ctx = {"ICON": ICON, "SITE": SITE, "card": card, "stat": stat, "esc": esc, "ICONS": ICON,
           "community_block": community_block, "COMMUNITY": COMMUNITY}

    # ---- Public marketing pages ----
    marketing = pages.MARKETING  # list of (rel, title, active, body_fn)
    for rel, title, active, fn in marketing:
        prefix = "../" * (len(Path(rel).parts) - 1)
        body = fn(prefix, ctx)
        write(rel, shell(title, body, prefix=prefix, active=active))

    # ---- Gates ----
    write("academy/gate.html", shell(
        "Enter the Academy", pages.gate_body("../", "academy", "learn/index.html",
        "Academy access", "The Academy curriculum is open to enrolled members.",
        "Ask your programme lead for the member access code."),
        prefix="../", active="academy.html"))
    write("fellowship/gate.html", shell(
        "Fellowship portal", pages.gate_body("../", "fellowship", "portal/index.html",
        "Fellowship portal", "The Fellowship portal is reserved for current fellows and mentors.",
        "Use the access code from your fellowship onboarding."),
        prefix="../", active="fellowship.html"))

    # ---- Academy reader (gated) ----
    build_academy_reader()

    # ---- Fellowship portal stub (gated) ----
    write("fellowship/portal/index.html", shell(
        "Fellowship portal", pages.portal_body("../../"),
        prefix="../../", active="fellowship.html",
        body_attr='data-guard="fellowship" data-guard-gate="../gate.html"'))

    print(f"\n  Built site -> _site/   ({count_pages()} html pages)")
    print("  Open: _site/index.html\n")

def count_pages():
    return sum(1 for _ in OUT.rglob("*.html"))

# ---- Academy curriculum reader -------------------------------------------
ACADEMY_TOC = [
    ("Start here", [
        ("intro", "intro.md"),
        ("curriculum/overview", "curriculum/overview.md"),
    ]),
    ("1 / Basics", [
        ("curriculum/basics", "curriculum/basics.md"),
        ("curriculum/foundation/what-is-ai", "curriculum/foundation/what-is-ai.md"),
        ("curriculum/foundation/how-to-ai", "curriculum/foundation/how-to-ai.md"),
        ("curriculum/foundation/datasets", "curriculum/foundation/datasets.md"),
        ("curriculum/foundation/evaluation", "curriculum/foundation/evaluation.md"),
    ]),
    ("2 / AI Agent", [
        ("curriculum/ai-agent", "curriculum/ai-agent.md"),
        ("notebooks/04-clinical-rag", "notebooks/04-clinical-rag.ipynb"),
    ]),
    ("3 / Deep AI", [
        ("curriculum/deep-ai", "curriculum/deep-ai.md"),
        ("curriculum/health/medical-imaging", "curriculum/health/medical-imaging.md"),
        ("notebooks/03-medical-imaging", "notebooks/03-medical-imaging.ipynb"),
        ("notebooks/01-clinical-ml", "notebooks/01-clinical-ml.ipynb"),
    ]),
    ("4 / Digital Health", [
        ("curriculum/digital-health", "curriculum/digital-health.md"),
        ("curriculum/health/clinical-ai", "curriculum/health/clinical-ai.md"),
        ("curriculum/health/clinical-applications", "curriculum/health/clinical-applications.md"),
        ("curriculum/health/fhir", "curriculum/health/fhir.md"),
        ("notebooks/02-fhir-data", "notebooks/02-fhir-data.ipynb"),
    ]),
    ("5 / Deployment", [
        ("curriculum/deployment", "curriculum/deployment.md"),
    ]),
    ("6 / Strategy & Governance", [
        ("curriculum/governance", "curriculum/governance.md"),
    ]),
    ("Pathways", [
        ("pathways/startup", "pathways/startup.md"),
        ("pathways/hospital", "pathways/hospital.md"),
    ]),
    ("Capstone", [
        ("curriculum/capstone/index", "curriculum/capstone/index.md"),
        ("curriculum/capstone/deployment", "curriculum/capstone/deployment.md"),
        ("curriculum/capstone/ethics", "curriculum/capstone/ethics.md"),
    ]),
]

def build_academy_reader():
    # flatten, keep only existing sources
    flat = []
    for cap, items in ACADEMY_TOC:
        for slug, src in items:
            if (BASE / src).exists():
                flat.append((cap, slug, src))
    titles = {slug: first_h1(BASE / src) for cap, slug, src in flat}

    # academy landing inside reader -> redirect to first
    if not flat:
        return
    first_slug = flat[0][1]
    write("academy/learn/index.html",
          f'<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" '
          f'content="0;url={first_slug.replace("/","__")}.html"><a href="{first_slug.replace("/","__")}.html">Enter</a>')

    order = [slug for _, slug, _ in flat]
    known = {slug for _, slug, _ in flat}

    def rewrite_links(html_text, src_path):
        import posixpath
        base_dir = posixpath.dirname(src_path)  # e.g. "curriculum"

        def strip_ext(t):
            for e in (".md", ".ipynb", ".html"):
                if t.endswith(e):
                    return t[:-len(e)]
            return t

        def repl(m):
            href = m.group(1)
            if href.startswith(("http://", "https://", "#", "mailto:")):
                return m.group(0)
            target = posixpath.normpath(posixpath.join(base_dir, href))
            slug2 = strip_ext(target)
            if slug2 in known:
                return 'href="' + slug2.replace("/", "__") + '.html"'
            # unresolved internal link (orphan reference): fall back to overview
            if "curriculum/overview" in known:
                return 'href="curriculum__overview.html"'
            return 'href="index.html"'
        return re.sub(r'href="([^"]+\.(?:md|ipynb|html))"', repl, html_text)

    for i, (cap, slug, src) in enumerate(flat):
        sp = BASE / src
        if sp.suffix == ".md":
            content = md_html(sp.read_text(encoding="utf-8"))
        else:
            content = nb_html(sp)
        content = rewrite_links(content, src)
        # fix relative asset/image links: point to academy root
        content = content.replace('src="assets/', 'src="../../assets/')
        content = content.replace('href="assets/', 'href="../../assets/')

        nav = academy_nav(slug, titles)
        prev_next = academy_prevnext(order, titles, i)
        flat_name = slug.replace("/", "__") + ".html"
        body = f"""
<div class="container" style="padding-block:1.5rem 0">
  <div class="crumb"><a href="../../academy.html">Academy</a> / <a href="index.html">Curriculum</a> / {esc(titles.get(slug, slug))}</div>
</div>
<div class="container">
  <div class="docs">
    <aside class="docs__nav">{nav}</aside>
    <div class="docs__main">
      <article class="prose">{content}</article>
      <nav class="page-nav">{prev_next}</nav>
    </div>
  </div>
</div>"""
        write(f"academy/learn/{flat_name}",
              shell(titles.get(slug, "Academy"), body, prefix="../../", active="academy.html",
                    body_attr='data-guard="academy" data-guard-gate="../gate.html"'))

def academy_nav(active_slug, titles):
    out = []
    for cap, items in ACADEMY_TOC:
        existing = [(s, src) for s, src in items if (BASE / src).exists()]
        if not existing:
            continue
        out.append(f'<div class="cap">{cap}</div>')
        for s, src in existing:
            cls = "is-active" if s == active_slug else ""
            fn = s.replace("/", "__") + ".html"
            out.append(f'<a class="{cls}" href="{fn}">{esc(titles.get(s, s))}</a>')
    return "\n".join(out)

def academy_prevnext(order, titles, i):
    parts = []
    if i > 0:
        s = order[i - 1]; fn = s.replace("/", "__") + ".html"
        parts.append(f'<a href="{fn}"><div class="k">Previous</div><div class="t">{esc(titles.get(s, s))}</div></a>')
    else:
        parts.append("<span></span>")
    if i < len(order) - 1:
        s = order[i + 1]; fn = s.replace("/", "__") + ".html"
        parts.append(f'<a class="next" href="{fn}"><div class="k">Next</div><div class="t">{esc(titles.get(s, s))}</div></a>')
    return "\n".join(parts)

if __name__ == "__main__":
    build()
