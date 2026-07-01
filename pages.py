# -*- coding: utf-8 -*-
"""
Long-form page bodies for the DHA Club venture site.
Voice: plain, confident, human. No em dashes, no middle dots, no filler.
"""

# ---------------------------------------------------------------------------
# small builders
# ---------------------------------------------------------------------------
def bi(en, th):
    """Inline bilingual span. CSS shows one per active [data-lang]."""
    return f'<span class="l-en">{en}</span><span class="l-th">{th}</span>'

def ph(en, th):
    """Plain-text bilingual placeholder attributes (bi() HTML breaks attributes)."""
    e = esc_txt(en).replace('"', '&quot;'); t = esc_txt(th).replace('"', '&quot;')
    return f'placeholder="{t}" data-ph-en="{e}" data-ph-th="{t}"'

def sec(inner, cls="section"):
    return f'<section class="{cls}"><div class="container">{inner}</div></section>'

def note_hand(en, th):
    """The handwritten line above a hero's eyebrow. One per page, ties every
    page back to the same voice: a note scrawled in the margin before the
    typeset headline begins."""
    return f'<p class="annot reveal" style="margin-bottom:.6rem">{bi(en, th)}</p>'

def flow(steps, icons):
    """Horizontal 'one line' stepper diagram. steps=[(k,title,desc)], icons=[icon,...]."""
    out = '<div class="flow reveal">'
    for i, (k, title, desc) in enumerate(steps):
        out += (f'<div class="flow__step"><div class="flow__dot">{icons[i]}</div>'
                f'<div class="flow__k">{k}</div><h3>{title}</h3><p>{desc}</p></div>')
    return out + '</div>'

def course_card(num, icon, title, desc, tags, href, prefix, label):
    tag_html = "".join(f'<span class="tagx">{t}</span>' for t in tags)
    return (f'<a class="course reveal" href="{prefix}{href}">'
            f'<span class="course__num">{num}</span>'
            f'<span class="course__ic">{icon}</span>'
            f'<h3>{title}</h3><p>{desc}</p>'
            f'<div class="course__meta">{tag_html}</div>'
            f'<span class="course__go">{label} <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>'
            f'<span class="course__bar"></span></a>')

def pullquote(text, attrib=None):
    a = f'<cite class="pq__cite">{attrib}</cite>' if attrib else ""
    return (f'<section class="section pq-wrap"><div class="container">'
            f'<blockquote class="pq reveal">{text}{a}</blockquote>'
            f'</div></section>')

def journey_map(items, icons):
    """Vertical 'single line' path through the curriculum. items=[(k,title,desc)]."""
    nodes = ""
    for i, (k, title, desc) in enumerate(items):
        ic = icons[i] if i < len(icons) else ""
        nodes += (f'<div class="journey__node reveal"><span class="journey__ic">{ic}</span>'
                  f'<div class="k">{k}</div><h3>{title}</h3><p>{desc}</p></div>')
    return f'<div class="journey">{nodes}</div>'

def whynow_viz(labels):
    """Three inputs converging to one gap. labels = (a,b,c,gap)."""
    a, b, c, gap = labels
    return (f'<div class="converge reveal">'
            f'<div class="converge__in"><span class="dotline dotline--on"></span><div class="converge__lab">{a}</div></div>'
            f'<div class="converge__in"><span class="dotline dotline--on"></span><div class="converge__lab">{b}</div></div>'
            f'<div class="converge__in"><span class="dotline dotline--off"></span><div class="converge__lab converge__lab--miss">{c}</div></div>'
            f'<div class="converge__out">{gap}</div>'
            f'</div>')

def moment(img, prefix, label, ratio="ratio-21x9"):
    """Full-width photographic band, editorial style."""
    return (f'<section class="section--tight"><div class="container">'
            f'<div class="frame frame--photo reveal"><div class="ratio {ratio}">'
            f'<img src="{prefix}assets/photos/{img}" alt="{esc_txt(label)}" loading="lazy"/>'
            f'<span class="frame__tint"></span>'
            f'<span class="frame__label">{label}</span>'
            f'</div></div></div></section>')

def head(eyebrow, title, sub=None):
    s = f'<p class="lead measure mt3">{sub}</p>' if sub else ""
    return f'<div class="section-head reveal"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2>{s}</div>'

def frame(label, ratio="ratio-16x9", tone="a", img=None, prefix=""):
    # Real photography when img is given, branded gradient otherwise.
    if img:
        return (f'<div class="frame frame--photo reveal"><div class="ratio {ratio}">'
                f'<img src="{prefix}assets/photos/{img}" alt="{esc_txt(label)}" loading="lazy"/>'
                f'<span class="frame__tint"></span>'
                f'<span class="frame__label">{label}</span>'
                f'</div></div>')
    grads = {
        "a": "radial-gradient(60% 80% at 20% 10%, rgba(247,98,5,.5), transparent 60%), radial-gradient(60% 80% at 90% 90%, rgba(52,18,209,.55), transparent 60%), #0e1728",
        "b": "radial-gradient(60% 80% at 80% 10%, rgba(88,34,166,.55), transparent 60%), radial-gradient(60% 80% at 10% 90%, rgba(1,0,252,.45), transparent 60%), #0e1728",
        "c": "radial-gradient(70% 90% at 50% 0%, rgba(145,56,110,.5), transparent 60%), #0e1728",
    }
    return (f'<div class="frame reveal"><div class="ratio {ratio}" '
            f'style="background:{grads.get(tone, grads["a"])}">'
            f'<div style="position:absolute;inset:auto auto 1rem 1.2rem;font-family:var(--font-mono);'
            f'font-size:.72rem;letter-spacing:.1em;color:rgba(255,255,255,.7)">{label}</div></div></div>')

def esc_txt(s):
    import re as _re
    return _re.sub(r"<[^>]+>", "", str(s))

# ===========================================================================
# HOME
# ===========================================================================
def vision_dawn():
    """Seventh signature sketch, the homepage's vision statement. Not literal
    figures (tried, looked like clip art, cut). Instead: a workforce is many
    people, so the diagram is many thin threads, each starting from a
    different point on the ground, each on its own path, all converging into
    one bold gradient line, the way the whole site's 'one continuous line'
    idea actually works at the scale of a country. Abstract, but the meaning
    is exact: nobody rises alone, and the many become one movement without
    losing their individual starting points."""
    import math
    starts = [70, 150, 230, 310, 390]
    merge = (560, 175)
    threads = ""
    for i, sx in enumerate(starts):
        cx1 = sx + 90 + i * 6
        cy1 = 330 - i * 8
        cx2 = merge[0] - 110
        cy2 = merge[1] + 40 - i * 4
        d = f"M {sx} 360 C {cx1} {cy1}, {cx2} {cy2}, {merge[0]} {merge[1]}"
        threads += f'<path class="vd-thread" d="{d}" fill="none" style="animation-delay:{i*0.12:.2f}s"/>'
    d_main = f"M {merge[0]} {merge[1]} C 650 130, 720 90, 810 55"
    svg = f"""
<div class="flow-art reveal">
  <svg viewBox="0 0 900 400" role="img" aria-label="Many individual threads, each starting from a different point on the ground, converging into one bright line rising toward the future" preserveAspectRatio="xMidYMid meet">
    <defs>
      <filter id="sketch8" x="-8%" y="-8%" width="116%" height="116%">
        <feTurbulence type="fractalNoise" baseFrequency="0.015" numOctaves="2" seed="61" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="2.4"/>
      </filter>
      <linearGradient id="vd-grad" x1="0" y1="1" x2="1" y2="0">
        <stop offset="0" stop-color="#3412d1"/><stop offset="0.5" stop-color="#91386e"/><stop offset="1" stop-color="#fd6502"/>
      </linearGradient>
    </defs>
    <g filter="url(#sketch8)">
      <line class="vd-ground" x1="40" y1="360" x2="860" y2="360"/>
      {threads}
      <path class="vd-arc" d="{d_main}" fill="none"/>
      <circle class="vd-node vd-node--sun" cx="810" cy="55" r="15"/>
    </g>
    <circle class="vd-merge-ring" cx="{merge[0]}" cy="{merge[1]}" r="20"/>
    <text class="l-en vd-lab" x="70" y="345">Many starting points</text>
    <text class="l-th vd-lab" x="70" y="345">จุดเริ่มต้นที่ต่างกัน</text>
    <text class="l-en vd-lab" x="{merge[0]}" y="{merge[1]-32}" text-anchor="middle">One workforce</text>
    <text class="l-th vd-lab" x="{merge[0]}" y="{merge[1]-32}" text-anchor="middle">หนึ่งกำลังคน</text>
    <text class="l-en vd-lab" x="835" y="30" text-anchor="end">The future of Thai care</text>
    <text class="l-th vd-lab" x="835" y="30" text-anchor="end">อนาคตการดูแลสุขภาพไทย</text>
    <text class="fa-hand" x="120" y="215" transform="rotate(-4 120 215)">not one hero, a whole generation</text>
    <path class="fa-hand-arrow" d="M170 224 q 30 8 54 22"/>
  </svg>
  <div class="flow-art__legend">
    <span class="l-en">A workforce is not one brilliant person. It is many people, starting from different places, who choose to rise together.</span>
    <span class="l-th">กำลังคนไม่ใช่คนเก่งเพียงคนเดียว แต่คือคนจำนวนมาก ที่เริ่มจากจุดต่างกัน แล้วเลือกที่จะเติบโตไปด้วยกัน</span>
  </div>
</div>"""
    return svg

def hero_line_art():
    """The hero's signature mark: the club's actual brain mark, traced from
    its real outer-contour path data (extracted from the official brand
    file), drawn as one open gradient stroke that draws itself in once on
    load. This is the real logo's geometry, not an invented shape: the
    viewBox matches the mark's native bounding box so the path 'd' string
    is used verbatim, with no manual coordinate transform to get wrong."""
    d = ("M659.95,2445.04c-6.94,29.54-11.39,62.57-23.03,90.67-25.24,60.91-56.08-20.01-66.06-44.8-16.27-40.42-29.09-83.7-37.65-126.43"
         "-15.2-.29-28.27,8.86-42.18,14.16-66.28,25.26-159.35,39.58-213.7-17.63-3.1-3.26-11.96-16.85-13.66-17.99-5.21-3.47-27.99-9.55"
         "-36.14-12.86-142.95-58.04-245.32-195.9-127.71-337.06,150.67-180.85,541.76-203.48,719.7-54.32,78.13,65.49,103.83,156.33,50.78"
         ",247.84-1.88,3.24-9.36,12.57-9.72,15.03-.22,1.45,7.41,14.02,8.84,17.64,25.01,62.8-22.51,141.53-69.46,181.48-37.68,32.06-89.56"
         ",57.1-140,44.25Z")
    return f"""
<svg class="hero-line" viewBox="-2.5 1797.5 951.7 803.5" preserveAspectRatio="xMidYMid meet" aria-hidden="true" focusable="false">
  <defs>
    <linearGradient id="hl-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fd6502"/><stop offset="0.5" stop-color="#91386e"/><stop offset="1" stop-color="#2a1bd6"/>
    </linearGradient>
  </defs>
  <path class="hero-line__path" d="{d}" fill="none" stroke="url(#hl-grad)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

def home(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero">
  <div class="hero__glow"></div>
  {hero_line_art()}
  <div class="container">
    <span class="eyebrow reveal">Ramathibodi Digital Health &amp; AI Club</span>
    <h1 class="reveal" data-d="1"><span class="l-en">We train the people who will bring <span class="gradient-text">AI to the bedside</span>.</span><span class="l-th">เราสร้างคนที่จะนำ <span class="gradient-text">AI สู่ข้างเตียงผู้ป่วย</span></span></h1>
    <p class="lead reveal measure" data-d="2">{bi("A club, an academy, and a fellowship built inside one of Thailand's leading medical schools.", "คลับ อคาเดมี และเฟลโลว์ชิป ที่สร้างขึ้นภายในหนึ่งในโรงเรียนแพทย์ชั้นนำของไทย")}</p>
    <div class="btn-row reveal" data-d="3">
      <a class="btn btn--grad btn--lg" href="{prefix}academy.html">{bi("Explore the Academy", "สำรวจอคาเดมี")} {I['arrow']}</a>
      <a class="btn btn--ghost btn--lg" href="{prefix}fellowship.html">{bi("Apply for the Fellowship", "สมัครเฟลโลว์ชิป")}</a>
    </div>
    <div class="hero__meta">
      {ctx['stat']('<span class="gradient-text">AI + Medicine</span>', bi('One discipline, taught as one', 'สองศาสตร์ สอนเป็นหนึ่งเดียว'))}
      {ctx['stat'](bi('Idea to bedside', 'ไอเดียสู่ข้างเตียง'), bi('Build under clinical supervision', 'สร้างงานภายใต้การกำกับทางคลินิก'))}
      {ctx['stat'](bi('Open + selective', 'เปิดกว้าง + คัดสรร'), bi('Academy for all, Fellowship for few', 'อคาเดมีเพื่อทุกคน เฟลโลว์ชิปเพื่อคนที่ใช่'))}
    </div>
  </div>
</section>"""

    _partner_marks = (
        (f'{prefix}assets/partners/ramathibodi-seal.svg', 'Faculty of Medicine Ramathibodi Hospital, Mahidol University'),
        (f'{prefix}assets/partners/mind-center.svg', 'MIND Center, Ramathibodi'),
        (f'{prefix}assets/partners/gdg-bangkok.svg', 'Google Developer Group Bangkok'),
        (f'{prefix}assets/partners/botnoi-academy.svg', 'Botnoi Academy'),
    )
    _marks_html = "".join(f'<img class="logo-mark" src="{src}" alt="{alt}" loading="lazy"/>' for src, alt in _partner_marks)
    proof = sec(
        '<div class="reveal partner-strip">'
        '<span class="eyebrow center">Built inside the system, with partners who build</span>'
        f'<div class="logo-marquee"><div class="logo-marquee__track">{_marks_html}{_marks_html}</div></div>'
        '<p class="muted center" style="font-size:.82rem;margin-top:1.4rem">Aligned with MOPH Digital Health, NHSO, Thai FDA, and Thai HealthTech</p>'
        '</div>', "section section--tight")

    vision = f"""
<section class="section">
  <div class="container">
    {head(bi("The vision", "วิสัยทัศน์"), bi("A new kind of doctor, rising from the same ground.", "แพทย์แบบใหม่ ที่งอกจากรากเดิม"), bi("Not a replacement for the clinician Thailand already trusts. An evolution of them: rooted in the same care, risen with a new instrument, still carrying the culture that made the care mean something.", "ไม่ใช่การแทนที่แพทย์ที่ประเทศไทยไว้ใจอยู่แล้ว แต่คือวิวัฒนาการของพวกเขา หยั่งรากในการดูแลแบบเดิม เติบโตขึ้นด้วยเครื่องมือใหม่ และยังคงแบกวัฒนธรรมที่ทำให้การดูแลนั้นมีความหมาย"))}
    {vision_dawn()}
  </div>
</section>"""

    what = sec(
        head(bi("What we do", "สิ่งที่เราทำ"), bi("Four parts, one pipeline.", "สี่ส่วน หนึ่งเส้นทาง"),
             bi("Most programmes teach theory and stop. We carry a person all the way from first principles to a working clinical product, then help the strongest ideas become real.", "หลักสูตรส่วนใหญ่สอนทฤษฎีแล้วจบ เราพาคนคนหนึ่งไปตลอดทาง ตั้งแต่พื้นฐานจนถึงผลิตภัณฑ์ทางคลินิกที่ใช้ได้จริง แล้วช่วยให้ไอเดียที่ดีที่สุดเกิดขึ้นจริง")) +
        '<div class="grid grid-2">' +
        ctx['card']('brain', bi('Academy', 'อคาเดมี'), bi('An open curriculum in AI and digital health, from foundations to clinical deployment. Free to learn, practical from day one.', 'หลักสูตรเปิดด้าน AI และสุขภาพดิจิทัล ตั้งแต่พื้นฐานจนถึงการนำไปใช้ในคลินิก เรียนฟรี ลงมือทำได้ตั้งแต่วันแรก'), 'academy.html', bi('Start learning', 'เริ่มเรียน'), prefix, 1) +
        ctx['card']('flask', bi('Fellowship', 'เฟลโลว์ชิป'), bi('A selective, in-residence year. Fellows work on real clinical problems with Ramathibodi data, faculty, and patients.', 'หนึ่งปีแบบคัดสรรและประจำในสถานที่ เฟลโลว์ทำงานกับโจทย์คลินิกจริง ด้วยข้อมูล อาจารย์ และผู้ป่วยของรามาธิบดี'), 'fellowship.html', bi('See the Fellowship', 'ดูเฟลโลว์ชิป'), prefix, 2) +
        ctx['card']('rocket', bi('Venture Studio', 'เวนเจอร์สตูดิโอ'), bi('We help the best fellowship work become deployable products, with engineering, regulatory, and go-to-market support.', 'เราช่วยให้ผลงานเฟลโลว์ชิปที่ดีที่สุดกลายเป็นผลิตภัณฑ์ที่ใช้งานได้จริง ด้วยการสนับสนุนด้านวิศวกรรม กฎระเบียบ และการออกสู่ตลาด'), 'venture.html', bi('How it works', 'ทำงานอย่างไร'), prefix, 1) +
        ctx['card']('compass', bi('Consulting', 'ที่ปรึกษานวัตกรรม'), bi('We advise hospitals and agencies building their own AI capability, so the workforce we train has somewhere to land.', 'เราให้คำปรึกษาแก่โรงพยาบาลและหน่วยงานที่กำลังสร้างขีดความสามารถด้าน AI ของตนเอง เพื่อให้คนที่เราฝึกมีที่ไปที่แข็งแรง'), 'what-we-do.html', bi('Work with us', 'ร่วมงานกับเรา'), prefix, 2) +
        '</div>')

    band = f"""
<section class="section">
  <div class="container">
    <div class="band reveal">
      <div class="band__glow"></div>
      <div class="container" style="padding-block:clamp(3rem,6vw,5rem)">
        <div class="split">
          <div class="stack">
            <span class="eyebrow" style="color:#cbd5ef">{bi("The standard we learn from", "มาตรฐานที่เรายึดถือ")}</span>
            <h2>{bi("The craft of medical AI, taught like a craft.", "วิชาชีพ AI การแพทย์ สอนแบบวิชาชีพ")}</h2>
            <p>{bi("Accredited education such as the AMA Ed Hub course on practical applications of AI in health care shows what rigorous, clinician-facing AI training looks like. We hold to that same standard of care, then pair it with a builder's studio, so people do not just understand medical AI, they make it.", "การศึกษาที่ได้รับการรับรอง เช่น คอร์สของ AMA Ed Hub ว่าด้วยการประยุกต์ใช้ AI ในการดูแลสุขภาพ แสดงให้เห็นว่าการฝึกอบรม AI ที่เข้มงวดสำหรับแพทย์ควรเป็นอย่างไร เรายึดมาตรฐานเดียวกันนี้ แล้วเสริมด้วยสตูดิโอของผู้สร้าง เพื่อให้คนไม่ได้แค่เข้าใจ AI การแพทย์ แต่ลงมือสร้างมันขึ้นมาเอง")}</p>
            <div class="btn-row">
              <a class="btn btn--grad" href="{prefix}what-we-do.html">{bi("How we teach", "เราสอนอย่างไร")} {I['arrow']}</a>
              <a class="btn btn--ghost" href="{prefix}insights/index.html" style="color:#fff;border-color:rgba(255,255,255,.25)">{bi("Read Insights", "อ่านบทความ")}</a>
            </div>
          </div>
          <div class="grid" style="gap:1rem">
            <div style="display:flex;gap:2rem;flex-wrap:wrap">
              {ctx['stat']('<span style="color:#fff">'+bi("Governance first", "ธรรมาภิบาลมาก่อน")+'</span>', '<span style="color:#9fb0d4">'+bi("Evaluation and safety from day one", "ประเมินและปลอดภัยตั้งแต่วันแรก")+'</span>')}
            </div>
            <div style="display:flex;gap:2rem;flex-wrap:wrap">
              {ctx['stat']('<span style="color:#fff">'+bi("Real data", "ข้อมูลจริง")+'</span>', '<span style="color:#9fb0d4">'+bi("Clinical problems, supervised access", "โจทย์คลินิกจริง เข้าถึงข้อมูลแบบมีการกำกับ")+'</span>')}
            </div>
            <div style="display:flex;gap:2rem;flex-wrap:wrap">
              {ctx['stat']('<span style="color:#fff">'+bi("Real deployment", "นำไปใช้จริง")+'</span>', '<span style="color:#9fb0d4">'+bi("Ship into the workflow, measure outcomes", "ส่งเข้าสู่เวิร์กโฟลว์จริง วัดผลลัพธ์")+'</span>')}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

    insights = sec(
        head(bi("Insights", "บทความ"), bi("Thinking from the club.", "มุมมองจากคนที่ลงมือทำจริง")) +
        '<div class="grid grid-3">' +
        entry("Field note", "Governance is a design material, not a checkpoint", "Why we teach evaluation and safety as part of building, from the first commit.", prefix + "insights/governance-as-design.html", "b", "code.jpg", prefix) +
        entry("Explainer", "FHIR, in plain language", "The data standard every clinical AI builder in Thailand should know, and why.", prefix + "insights/fhir-in-plain-language.html", "a", "analytics.jpg", prefix) +
        entry("Position", "Why Thailand should train builders, not just buyers", "The case for a homegrown medical AI workforce inside the health system.", prefix + "insights/train-builders-not-buyers.html", "c", "network-people.jpg", prefix) +
        '</div>' +
        f'<div class="btn-row mt5 reveal"><a class="btn btn--ghost" href="{prefix}insights/index.html">{bi("All insights", "บทความทั้งหมด")} {I["arrow"]}</a></div>')

    cta = f"""
<section class="section">
  <div class="container center stack reveal">
    <span class="eyebrow" style="justify-content:center">{bi("Join us", "มาร่วมกับเรา")}</span>
    <h2 class="measure" style="margin-inline:auto">{bi("Two doors in. One mission.", "สองประตูเข้า หนึ่งภารกิจ")}</h2>
    <p class="lead measure" style="margin-inline:auto">{bi("Learn the craft in the Academy. Prove it in the Fellowship. Either way, you leave able to build medical AI that a hospital will actually use.", "เรียนวิชาชีพในอคาเดมี พิสูจน์ตัวเองในเฟลโลว์ชิป ไม่ว่าทางไหน คุณจะจากไปพร้อมความสามารถในการสร้าง AI ทางการแพทย์ที่โรงพยาบาลใช้ได้จริง")}</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn--grad btn--lg" href="{prefix}academy.html">{bi("Enter the Academy", "เข้าสู่อคาเดมี")} {I['arrow']}</a>
      <a class="btn btn--ghost btn--lg" href="{prefix}fellowship.html">{bi("Apply for the Fellowship", "สมัครเฟลโลว์ชิป")}</a>
    </div>
  </div>
</section>"""

    # Chapter: the problem, with a diagram
    problem = f"""
<section class="section">
  <div class="container">
    {head(bi("Why now", "ทำไมต้องตอนนี้"), bi("The models are here. The people are not.", "โมเดลมาถึงแล้ว แต่คนยังไม่มา"))}
    <div class="split">
      <div class="stack reveal">
        <p class="lead">{bi("For the first time, AI is genuinely useful in the clinic. Thailand has a national direction, the data, and the talent. The one thing missing is a generation of people who can hold a clinical problem in one hand and a model in the other.", "เป็นครั้งแรกที่ AI มีประโยชน์จริงในคลินิก ประเทศไทยมีทิศทางระดับชาติ มีข้อมูล และมีคนเก่ง สิ่งเดียวที่ขาดคือคนรุ่นใหม่ที่ถือโจทย์ทางคลินิกไว้มือหนึ่ง และถือโมเดลไว้อีกมือหนึ่ง")}</p>
        <p>{bi("That gap is not technology. It is people. Closing it is the whole reason we exist.", "ช่องว่างนั้นไม่ใช่เทคโนโลยี แต่คือคน การปิดช่องว่างนี้คือเหตุผลทั้งหมดที่เรามีอยู่")}</p>
      </div>
      <div class="stack reveal" style="justify-content:center">
        {whynow_viz((bi("Capable models", "โมเดลที่เก่งพอ"), bi("National policy", "นโยบายระดับชาติ"), bi("Trained builders", "คนที่สร้างเป็น"), bi("The gap is people.", "ช่องว่างคือคน")))}
      </div>
    </div>
  </div>
</section>"""

    # Chapter: why medical students
    whymed = f"""
<section class="section">
  <div class="container">
    <div class="split split--rev">
      {frame(bi("For the next generation", "เพื่อคนรุ่นใหม่"), "ratio-4x3", "a", "doctor.jpg", prefix)}
      <div class="stack reveal">
        <span class="eyebrow">{bi("Why medical students", "ทำไมต้องเป็นนักศึกษาแพทย์")}</span>
        <h2>{bi("You already see the problems. We give you the tools.", "คุณเห็นปัญหาอยู่แล้ว เราแค่ให้เครื่องมือ")}</h2>
        <p class="lead">{bi("The best medical AI does not come from engineers guessing at clinical needs. It comes from clinicians who learned to build. As a medical student in Thailand, you sit on the exact advantage the field needs.", "AI การแพทย์ที่ดีที่สุดไม่ได้มาจากวิศวกรที่เดาความต้องการทางคลินิก แต่มาจากแพทย์ที่เรียนรู้ที่จะสร้าง ในฐานะนักศึกษาแพทย์ไทย คุณมีข้อได้เปรียบที่วงการนี้ต้องการพอดี")}</p>
        <ul class="rows" style="border-top:1px solid var(--line)">
          <li class="row" style="grid-template-columns:1fr"><div><h3 style="font-size:var(--step-1)">{bi("You know what matters", "คุณรู้ว่าอะไรสำคัญ")}</h3><p>{bi("You have seen the ward, the frustration, the delay. You know which problems are worth solving.", "คุณเคยเห็นหอผู้ป่วย ความติดขัด ความล่าช้า คุณรู้ว่าโจทย์ไหนคุ้มค่าที่จะแก้")}</p></div></li>
          <li class="row" style="grid-template-columns:1fr"><div><h3 style="font-size:var(--step-1)">{bi("You start with no code, and that is fine", "เริ่มจากไม่มีพื้นโค้ดก็ได้")}</h3><p>{bi("The Academy is built for clinicians. You will build a working tool before you feel like a programmer.", "อคาเดมีสร้างมาเพื่อแพทย์ คุณจะสร้างเครื่องมือที่ใช้ได้ ก่อนที่จะรู้สึกว่าตัวเองเป็นโปรแกรมเมอร์")}</p></div></li>
          <li class="row" style="grid-template-columns:1fr"><div><h3 style="font-size:var(--step-1)">{bi("You compound early", "ยิ่งเริ่มเร็ว ยิ่งทบต้น")}</h3><p>{bi("Learn this now and you spend an entire career as the person who can build, not just prescribe.", "เรียนตอนนี้ แล้วคุณจะใช้ทั้งอาชีพเป็นคนที่สร้างได้ ไม่ใช่แค่สั่งการรักษา")}</p></div></li>
        </ul>
        <div class="btn-row"><a class="btn btn--grad" href="{prefix}academy.html">{bi("Start the Academy", "เริ่มที่อคาเดมี")} {I['arrow']}</a></div>
      </div>
    </div>
  </div>
</section>"""

    # Chapter: the path (flow diagram)
    path = sec(
        head(bi("The path", "เส้นทาง"), bi("From your first line of code to a tool a hospital trusts.", "จากโค้ดบรรทัดแรก สู่เครื่องมือที่โรงพยาบาลเชื่อใจ")) +
        flow([
            (bi("Step 01", "ขั้นที่ 01"), bi("Learn", "เรียน"), bi("Foundations and clinical context, free and at your own pace.", "พื้นฐานและบริบททางคลินิก ฟรีและตามจังหวะของคุณ")),
            (bi("Step 02", "ขั้นที่ 02"), bi("Apply", "สมัคร"), bi("Bring a real problem, get matched with a mentor and data.", "นำโจทย์จริงมา จับคู่กับเมนเทอร์และข้อมูล")),
            (bi("Step 03", "ขั้นที่ 03"), bi("Build", "สร้าง"), bi("Ship an evaluated tool into a real clinical workflow.", "ส่งเครื่องมือที่ประเมินแล้วเข้าสู่เวิร์กโฟลว์คลินิกจริง")),
            (bi("Step 04", "ขั้นที่ 04"), bi("Scale", "ขยายผล"), bi("If it deserves to live, the studio makes it a product.", "หากคู่ควรที่จะอยู่ต่อ สตูดิโอทำให้เป็นผลิตภัณฑ์")),
        ], [I["brain"], I["flask"], I["shield"], I["rocket"]]))

    # Chapter: the curriculum, as a journey map
    journey = f"""
<section class="section">
  <div class="container">
    {head(bi("The curriculum", "หลักสูตร"), bi("One line through six courses.", "หนึ่งเส้น ผ่านหกคอร์ส"), bi("Most people walk the courses in order, then choose a pathway. Every course ends in something you built.", "คนส่วนใหญ่เดินตามลำดับ แล้วเลือกเส้นทาง ทุกคอร์สจบด้วยสิ่งที่คุณสร้าง"))}
    <div class="split">
      <div class="reveal">
        {journey_map([
            (bi("Course 01", "คอร์ส 01"), bi("Basics", "พื้นฐาน"), bi("No-code, Git, APIs, the cloud.", "No-code, Git, API, คลาวด์")),
            (bi("Course 02", "คอร์ส 02"), bi("AI Agent", "AI Agent"), bi("LLMs, guardrails, RAG, agents.", "LLM, guardrails, RAG, agents")),
            (bi("Course 03", "คอร์ส 03"), bi("Deep AI", "Deep AI"), bi("Images, signals, sound, tables.", "ภาพ สัญญาณ เสียง ตาราง")),
            (bi("Course 04", "คอร์ส 04"), bi("Digital Health", "สุขภาพดิจิทัล"), bi("HIS, FHIR, ICD-10, PDPA.", "HIS, FHIR, ICD-10, PDPA")),
            (bi("Course 05", "คอร์ส 05"), bi("Deployment", "Deployment"), bi("Dashboards, prototyping, stats.", "แดชบอร์ด prototyping สถิติ")),
            (bi("Course 06", "คอร์ส 06"), bi("Strategy & Governance", "กลยุทธ์และธรรมาภิบาล"), bi("Thai FDA, SaMD, ISO.", "อย., SaMD, ISO")),
        ], [I["brain"], I["node"], I["pulse"], I["doc"], I["rocket"], I["shield"]])}
      </div>
      <div class="stack reveal" style="justify-content:center">
        <p class="lead">{bi("Then a pathway: build a startup, or strengthen a hospital from inside.", "จากนั้นเลือกเส้นทาง สร้างสตาร์ตอัป หรือเสริมความแข็งแกร่งให้โรงพยาบาลจากภายใน")}</p>
        <div class="btn-row"><a class="btn btn--grad btn--lg" href="{prefix}academy.html">{bi("See all courses", "ดูคอร์สทั้งหมด")} {I['arrow']}</a></div>
      </div>
    </div>
  </div>
</section>"""

    quote = pullquote(
        bi('The point is not to learn about medical AI. The point is to <span class="gradient-text">build it</span>, well enough that a hospital will use it.',
           'เป้าหมายไม่ใช่แค่เรียนรู้เรื่อง AI การแพทย์ แต่คือการ <span class="gradient-text">สร้างมันขึ้นมา</span> ให้ดีพอที่โรงพยาบาลจะใช้จริง'),
        bi("The Ramathibodi Digital Health &amp; AI Club", "Ramathibodi Digital Health &amp; AI Club"))

    return (hero + proof + vision
            + problem
            + moment("hero-clinician.jpg", prefix, bi("AI at the bedside", "AI ข้างเตียงผู้ป่วย") + " / Ramathibodi")
            + whymed + what + path + journey + band + quote + insights
            + ctx["community_block"](prefix) + cta)

def entry(meta, title, body, href, tone="a", img=None, prefix=""):
    return (f'<a class="entry reveal" href="{href}">'
            f'{frame(meta, "ratio-4x3", tone, img, prefix)}'
            f'<div class="entry__meta">{meta}</div>'
            f'<h3>{title}</h3><p>{body}</p></a>')

# ===========================================================================
# WHO WE ARE
# ===========================================================================
def position_chart():
    """A category-creation chart, not a card grid: two axes, four players
    plotted. The Club sits alone in the quadrant nobody else occupies. Every
    SVG <text> below holds plain text only, in l-en/l-th pairs, never a
    pre-wrapped bi() HTML string (that mistake once broke this exact kind
    of diagram)."""
    ox, oy, w, h = 70, 40, 460, 340  # plot origin (bottom-left) is (ox, oy+h)
    def plot(px, py):
        return (ox + px * w, oy + h - py * h)
    plain_labels = [
        (0.18, 0.22, "Universities", "มหาวิทยาลัย"),
        (0.78, 0.16, "Startups", "สตาร์ตอัป"),
        (0.86, 0.28, "Vendors", "ผู้ขายเทคโนโลยี"),
    ]
    dots, labels = "", ""
    for px, py, en, th in plain_labels:
        x, y = plot(px, py)
        dots += f'<circle class="pc-dot" cx="{x:.0f}" cy="{y:.0f}" r="7"/>'
        labels += (f'<text class="l-en pc-lab" x="{x+12:.0f}" y="{y+4:.0f}">{en}</text>'
                   f'<text class="l-th pc-lab" x="{x+12:.0f}" y="{y+4:.0f}">{th}</text>')
    cx, cy = plot(0.82, 0.86)
    club = (f'<circle class="pc-dot pc-dot--club" cx="{cx:.0f}" cy="{cy:.0f}" r="12"/>'
            f'<text class="l-en pc-club" x="{cx-16:.0f}" y="{cy-20:.0f}" text-anchor="end">The Club</text>'
            f'<text class="l-th pc-club" x="{cx-16:.0f}" y="{cy-20:.0f}" text-anchor="end">คลับของเรา</text>')
    svg = f"""
<div class="flow-art reveal" style="margin-top:0">
  <svg viewBox="0 0 600 430" role="img" aria-label="A chart plotting universities, startups, vendors, and the club on deployment versus capability left behind" preserveAspectRatio="xMidYMid meet">
    <defs>
      <filter id="sketch6" x="-8%" y="-8%" width="116%" height="116%">
        <feTurbulence type="fractalNoise" baseFrequency="0.017" numOctaves="2" seed="41" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="2.6"/>
      </filter>
      <radialGradient id="pc-grad" cx="50%" cy="50%" r="60%">
        <stop offset="0" stop-color="#fd6502"/><stop offset="0.55" stop-color="#91386e"/><stop offset="1" stop-color="#2a1bd6"/>
      </radialGradient>
    </defs>
    <g filter="url(#sketch6)" fill="none">
      <line class="pc-axis" x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy+h}"/>
      <line class="pc-axis" x1="{ox}" y1="{oy+h}" x2="{ox+w}" y2="{oy+h}"/>
    </g>
    <text class="l-en pc-axis-lab" x="{ox}" y="{oy-14}">Leaves lasting capability</text>
    <text class="l-th pc-axis-lab" x="{ox}" y="{oy-14}">ทิ้งขีดความสามารถไว้</text>
    <text class="l-en pc-axis-lab" x="{ox+w}" y="{oy+h+28}" text-anchor="end">Ships a real product</text>
    <text class="l-th pc-axis-lab" x="{ox+w}" y="{oy+h+28}" text-anchor="end">ส่งมอบผลิตภัณฑ์จริง</text>
    <g filter="url(#sketch6)">
      {dots}
      {club}
    </g>
    {labels}
  </svg>
  <div class="flow-art__legend">
    <span class="l-en">Everyone else trades one for the other. We plot in the corner where both are true at once.</span>
    <span class="l-th">คนอื่นแลกอย่างหนึ่งกับอีกอย่างหนึ่งเสมอ เราอยู่ในมุมที่ทั้งสองอย่างเป็นจริงพร้อมกัน</span>
  </div>
</div>"""
    return svg

def agenda_comb():
    """Sixth signature sketch: a spine and branches, distinct in shape from
    the path, trail, orbit, hub, funnel, and scatter chart already used
    elsewhere. The club is the spine on the left. Six branches reach out to
    the bodies that set the national agenda, each a short, direct connection,
    not a cluster of cards."""
    items = [
        ("Ministry of Public Health", "กระทรวงสาธารณสุข", "Sets the direction for a connected, data-driven health system", "กำหนดทิศทางระบบสุขภาพที่เชื่อมโยงและขับเคลื่อนด้วยข้อมูล"),
        ("NHSO", "สปสช.", "Runs universal coverage; AI has to meet its real-world constraints", "ดูแลหลักประกันสุขภาพถ้วนหน้า AI ต้องตอบโจทย์ข้อจำกัดจริง"),
        ("Thai FDA", "อย.", "Regulates medical AI as Software as a Medical Device", "กำกับดูแล AI ทางการแพทย์ในฐานะ Software as a Medical Device"),
        ("NIA", "NIA", "Backs the move from research to venture", "สนับสนุนการต่อยอดจากงานวิจัยสู่ธุรกิจ"),
        ("Thai HealthTech", "เฮลท์เทคไทย", "A growing ecosystem of companies and associations", "ระบบนิเวศบริษัทและสมาคมที่กำลังเติบโต"),
        ("Accredited education", "การศึกษาที่รับรอง", "The AMA Ed Hub standard, adapted for Thailand", "มาตรฐานแบบ AMA Ed Hub ปรับใช้สำหรับไทย"),
    ]
    sx, top, bottom = 66, 30, 370
    n = len(items)
    step = (bottom - top) / (n - 1)
    branches, nodes, labels = "", "", ""
    for i, (en, th, cap_en, cap_th) in enumerate(items):
        y = top + i * step
        ex = 210 + (14 if i % 2 else -6)
        branches += f'<path class="ac-branch" d="M {sx} {y:.0f} L {ex} {y:.0f}"/>'
        nodes += f'<circle class="ac-node" cx="{ex}" cy="{y:.0f}" r="6"/>'
        labels += (f'<text class="l-en ac-lab" x="{ex+16}" y="{y-4:.0f}">{en}</text>'
                   f'<text class="l-th ac-lab" x="{ex+16}" y="{y-4:.0f}">{th}</text>'
                   f'<text class="l-en ac-cap" x="{ex+16}" y="{y+14:.0f}">{cap_en}</text>'
                   f'<text class="l-th ac-cap" x="{ex+16}" y="{y+14:.0f}">{cap_th}</text>')
    svg = f"""
<div class="flow-art reveal">
  <svg viewBox="0 0 640 400" role="img" aria-label="The club as a spine, with six branches reaching the bodies that set Thailand's health agenda" preserveAspectRatio="xMidYMid meet">
    <defs>
      <filter id="sketch7" x="-8%" y="-8%" width="116%" height="116%">
        <feTurbulence type="fractalNoise" baseFrequency="0.017" numOctaves="2" seed="53" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="2.4"/>
      </filter>
      <linearGradient id="ac-grad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#fd6502"/><stop offset="0.5" stop-color="#91386e"/><stop offset="1" stop-color="#2a1bd6"/>
      </linearGradient>
    </defs>
    <g filter="url(#sketch7)">
      <line class="ac-spine" x1="{sx}" y1="{top}" x2="{sx}" y2="{bottom}"/>
      {branches}
      {nodes}
    </g>
    {labels}
    <text class="l-en ac-us" x="{sx}" y="{top-12}" text-anchor="middle">Us</text>
    <text class="l-th ac-us" x="{sx}" y="{top-12}" text-anchor="middle">เรา</text>
  </svg>
</div>"""
    return svg

def who_we_are(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:3rem">
  <div class="hero__glow"></div>
  <div class="container">
    <div class="split">
      <div>
        {note_hand("built inside a hospital", "สร้างขึ้นในโรงพยาบาล")}
        <span class="eyebrow reveal">{bi("Who we are", "เกี่ยวกับเรา")}</span>
        <h1 class="reveal" data-d="1" style="max-width:14ch;margin-top:var(--s3)">{bi("The discipline of an institution, the speed of a startup.", "วินัยของสถาบัน ความเร็วของสตาร์ตอัป")}</h1>
        <p class="lead reveal measure mt4" data-d="2">{bi("We sit inside Ramathibodi, and we build the people who will modernise Thai healthcare from within.", "เราอยู่ภายในรามาธิบดี และสร้างคนที่จะพลิกโฉมระบบสุขภาพไทยจากภายใน")}</p>
      </div>
      {nested_system()}
    </div>
  </div>
</section>"""

    mv = f"""
<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div class="card card--feature reveal">
        <span class="eyebrow">{bi("Mission", "พันธกิจ")}</span>
        <h2 class="mt3" style="font-size:var(--step-2)">{bi("Produce a generation of healthcare builders.", "สร้างคนรุ่นใหม่ที่เป็นผู้สร้างในวงการสุขภาพ")}</h2>
        <p class="mt3">{bi("We train clinicians, engineers, and scientists to design, evaluate, and deploy trustworthy medical AI, and we give them real problems to prove it on. Our measure is not graduates. It is working tools in clinical use.", "เราฝึกแพทย์ วิศวกร และนักวิทยาศาสตร์ ให้ออกแบบ ประเมิน และนำ AI ทางการแพทย์ที่น่าเชื่อถือไปใช้จริง พร้อมโจทย์จริงให้พิสูจน์ฝีมือ ตัวชี้วัดของเราไม่ใช่จำนวนผู้จบหลักสูตร แต่คือเครื่องมือที่ใช้งานจริงในคลินิก")}</p>
      </div>
      <div class="card card--feature reveal" data-d="1">
        <span class="eyebrow">{bi("Vision", "วิสัยทัศน์")}</span>
        <h2 class="mt3" style="font-size:var(--step-2)">{bi("Every Thai institution staffed to build its own AI.", "ทุกสถาบันของไทยมีคนที่สร้าง AI ของตัวเองได้")}</h2>
        <p class="mt3">{bi("A health system where hospitals and agencies do not wait to buy AI from elsewhere, because they have people who can build, vet, and run it responsibly. We want to be the place that workforce comes from.", "ระบบสุขภาพที่โรงพยาบาลและหน่วยงานไม่ต้องรอซื้อ AI จากที่อื่น เพราะมีคนที่สร้าง ตรวจสอบ และดูแลมันได้อย่างรับผิดชอบ เราอยากเป็นที่มาของกำลังคนเหล่านั้น")}</p>
      </div>
    </div>
  </div>
</section>"""

    values = sec(
        head(bi("How we work", "วิธีการทำงานของเรา"), bi("Five principles we do not bend on.", "ห้าหลักการที่เราไม่ยอมประนีประนอม")) +
        flow([
            (bi("01", "01"), bi("Clinic first", "คลินิกมาก่อน"), bi("A clinician is in the room. Technology serves care, never the reverse.", "มีแพทย์อยู่ในห้อง เทคโนโลยีรับใช้การดูแล ไม่ใช่ทางกลับกัน")),
            (bi("02", "02"), bi("Governance as a material", "ธรรมาภิบาลคือวัสดุ"), bi("Safety and privacy are present from the first design decision.", "ความปลอดภัยและความเป็นส่วนตัว มีตั้งแต่การตัดสินใจแรก")),
            (bi("03", "03"), bi("Build to learn", "เรียนรู้ด้วยการสร้าง"), bi("Reviewed work, real deployment, measured outcomes.", "งานที่รีวิวแล้ว นำไปใช้จริง วัดผลได้")),
            (bi("04", "04"), bi("Open, then selective", "เปิดกว้าง แล้วคัดสรร"), bi("The Academy is open to all. The Fellowship stays small on purpose.", "อคาเดมีเปิดให้ทุกคน เฟลโลว์ชิปตั้งใจให้เล็ก")),
            (bi("05", "05"), bi("Of the system, for the system", "จากระบบ เพื่อระบบ"), bi("Built to plug into the national health agenda.", "ออกแบบให้เชื่อมกับวาระสุขภาพของชาติ")),
        ], [I["pulse"], I["shield"], I["flask"], I["users"], I["node"]]))

    position = f"""
<section class="section">
  <div class="container">
    {head(bi("Our position", "จุดยืนของเรา"), bi("What no one else is offering, and why it has to be us.", "สิ่งที่ไม่มีใครให้ได้ และทำไมต้องเป็นเรา"))}
    <div class="split">
      <div class="stack reveal">
        <p class="lead">{bi("Thailand has talent, data, and a clear national direction. What it lacks is a place that turns clinical insight into deployable AI and trains the next workforce while doing it, inside a hospital.", "ประเทศไทยมีคนเก่ง มีข้อมูล และมีทิศทางระดับชาติที่ชัดเจน สิ่งที่ยังขาดคือที่ที่เปลี่ยนความเข้าใจทางคลินิกให้เป็น AI ที่ใช้ได้จริง และฝึกกำลังคนรุ่นต่อไปไปพร้อมกัน โดยทำอยู่ภายในโรงพยาบาล")}</p>
        <p>{bi("Pure universities teach theory without deployment. Pure startups deploy without clinical depth or a teaching mission. Vendors sell finished products and leave no capability behind. We are deliberately the thing in the middle: an academic home with a builder's studio and a fellowship, accountable to patients and to the public health system at the same time.", "มหาวิทยาลัยล้วนๆ สอนทฤษฎีแต่ไม่ได้นำไปใช้จริง สตาร์ตอัปล้วนๆ นำไปใช้แต่ขาดความลึกทางคลินิกและพันธกิจการสอน ผู้ขายขายผลิตภัณฑ์สำเร็จรูปแต่ไม่ทิ้งขีดความสามารถไว้ให้ เราตั้งใจอยู่ตรงกลาง เป็นบ้านทางวิชาการที่มีทั้งสตูดิโอของผู้สร้างและเฟลโลว์ชิป รับผิดชอบต่อผู้ป่วยและต่อระบบสุขภาพสาธารณะไปพร้อมกัน")}</p>
        <p>{bi("That is why this works here and not as a side project somewhere else. We have the clinical reality of Ramathibodi, the academic standing of Mahidol, and a mandate to teach. The result is a pipeline that produces both people and products the country can trust.", "นี่คือเหตุผลที่สิ่งนี้เกิดขึ้นได้ที่นี่ ไม่ใช่โปรเจกต์เสริมที่อื่น เรามีความจริงทางคลินิกของรามาธิบดี สถานะทางวิชาการของมหิดล และหน้าที่ในการสอน ผลลัพธ์คือเส้นทางที่ผลิตทั้งคนและผลิตภัณฑ์ที่ประเทศไว้วางใจได้")}</p>
      </div>
      {position_chart()}
    </div>
  </div>
</section>"""

    eco = sec(
        head(bi("Where we fit nationally", "เราอยู่ตรงไหนในระดับชาติ"), bi("Designed to plug into Thailand's health agenda.", "ออกแบบให้เสียบเข้ากับวาระสุขภาพของไทย"),
             bi("We do not work around the system. We build toward the goals the country has already set, so our graduates and tools have a place to go.", "เราไม่ได้ทำงานเลี่ยงระบบ เราสร้างไปในทิศทางเป้าหมายที่ประเทศตั้งไว้แล้ว เพื่อให้ผู้จบและเครื่องมือของเรามีที่ไป")) +
        agenda_comb())

    partners = sec(
        head(bi("Partners", "พันธมิตร"), bi("We do not build alone.", "เราไม่ได้สร้างเพียงลำพัง"),
             bi("We work with the people who train builders and ship technology.", "เราทำงานร่วมกับผู้ที่ฝึกคนสร้างและส่งมอบเทคโนโลยี")) +
        f"""<div class="partner-row reveal">
          <a class="partner-mark" href="{prefix}contact.html">
            <img src="{prefix}assets/partners/gdg-bangkok.svg" alt="Google Developer Groups on Campus, Bangkok"/>
            <span class="partner-mark__cap">{bi('Google Cloud and AI tooling for our hands-on work', 'เครื่องมือ Google Cloud และ AI สำหรับงานภาคปฏิบัติ')}</span>
          </a>
          <a class="partner-mark" href="{prefix}contact.html">
            <img src="{prefix}assets/partners/botnoi-academy.svg" alt="BOTNOI Academy"/>
            <span class="partner-mark__cap">{bi('Thai speech and language for the curriculum', 'เสียงและภาษาไทยสำหรับหลักสูตร')}</span>
          </a>
        </div>""" +
        '<p class="muted mt4 reveal" style="font-size:.9rem">' + bi("We design to align with the Ministry of Public Health digital health agenda, the National Health Security Office, the Thai FDA pathway for Software as a Medical Device, the National Innovation Agency, and the Thai HealthTech ecosystem.", "เราออกแบบให้สอดคล้องกับวาระสุขภาพดิจิทัลของกระทรวงสาธารณสุข สำนักงานหลักประกันสุขภาพแห่งชาติ (NHSO) แนวทาง Software as a Medical Device ของ อย. สำนักงานนวัตกรรมแห่งชาติ (NIA) และระบบนิเวศ HealthTech ไทย") + '</p>')

    consulting = f"""
<section class="section">
  <div class="container">
    <div class="band reveal">
      <div class="band__glow"></div>
      <div class="container" style="padding-block:clamp(3rem,6vw,5rem)">
        <div class="split">
          <div class="stack">
            <span class="eyebrow" style="color:#cbd5ef">{bi("Innovation consulting", "ที่ปรึกษานวัตกรรม")}</span>
            <h2>{bi("An innovation partner for the next-generation healthcare workforce.", "พันธมิตรด้านนวัตกรรม เพื่อกำลังคนสุขภาพรุ่นใหม่")}</h2>
            <p>{bi("Beyond teaching and the fellowship, we advise hospitals, agencies, and health technology companies that are standing up their own AI capability. We design teams, governance, and training programmes, so the people we train have strong places to land and the system gains capability it keeps. This is how a club becomes infrastructure.", "นอกเหนือจากการสอนและเฟลโลว์ชิป เราให้คำปรึกษาแก่โรงพยาบาล หน่วยงาน และบริษัทเทคโนโลยีสุขภาพ ที่กำลังสร้างขีดความสามารถด้าน AI ของตนเอง เราออกแบบทีม ธรรมาภิบาล และโปรแกรมฝึกอบรม เพื่อให้คนที่เราฝึกมีที่ไปที่แข็งแรง และระบบได้ขีดความสามารถที่คงอยู่ นี่คือวิธีที่คลับกลายเป็นโครงสร้างพื้นฐาน")}</p>
            <div class="btn-row"><a class="btn btn--grad" href="{prefix}what-we-do.html">{bi("How we work", "วิธีการทำงาน")} {I['arrow']}</a><a class="btn btn--ghost" href="{prefix}contact.html" style="color:#fff;border-color:rgba(255,255,255,.25)">{bi("Work with us", "ร่วมงานกับเรา")}</a></div>
          </div>
          <div class="grid" style="gap:1rem">
            <div style="display:flex;gap:2rem;flex-wrap:wrap">{ctx['stat']('<span style="color:#fff">'+bi('Capability design','ออกแบบขีดความสามารถ')+'</span>', '<span style="color:#9fb0d4">'+bi('Teams, not just tools','ทีม ไม่ใช่แค่เครื่องมือ')+'</span>')}</div>
            <div style="display:flex;gap:2rem;flex-wrap:wrap">{ctx['stat']('<span style="color:#fff">'+bi('Governance','ธรรมาภิบาล')+'</span>', '<span style="color:#9fb0d4">'+bi('Evaluation and SaMD readiness','การประเมินและความพร้อม SaMD')+'</span>')}</div>
            <div style="display:flex;gap:2rem;flex-wrap:wrap">{ctx['stat']('<span style="color:#fff">'+bi('Workforce','กำลังคน')+'</span>', '<span style="color:#9fb0d4">'+bi('Training programmes that stick','โปรแกรมฝึกที่ได้ผลจริง')+'</span>')}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

    team = sec(
        head(bi("People", "ทีมงาน"), bi("Faculty, builders, and clinicians in one room.", "อาจารย์ ผู้สร้าง และแพทย์ ในห้องเดียวกัน"),
             bi("The club brings together attending physicians, machine learning engineers, data scientists, and health policy people. Profiles and the founding team are published as the club grows.", "คลับรวมแพทย์ประจำ วิศวกร machine learning นักวิทยาศาสตร์ข้อมูล และคนด้านนโยบายสุขภาพไว้ด้วยกัน โปรไฟล์และทีมผู้ก่อตั้งจะเผยแพร่เมื่อคลับเติบโตขึ้น")) +
        f'<div class="btn-row reveal"><a class="btn btn--ghost" href="{prefix}careers.html">{bi("Join the team", "ร่วมทีม")} {I["arrow"]}</a><a class="btn btn--ghost" href="{prefix}contact.html">{bi("Partner with us", "เป็นพันธมิตร")}</a></div>')

    return hero + mv + values + position + eco + partners + consulting + team

def row(num, title, body):
    return (f'<div class="row reveal"><div class="row__num">{num}</div>'
            f'<h3>{title}</h3><p>{body}</p></div>')

# ===========================================================================
# WHAT WE DO
# ===========================================================================
def what_we_do(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:3rem">
  <div class="hero__glow"></div>
  <div class="container">
    {note_hand("one path, four parts", "หนึ่งเส้นทาง สี่ส่วน")}
    <span class="eyebrow reveal">{bi("What we do", "สิ่งที่เราทำ")}</span>
    <h1 class="reveal" data-d="1" style="max-width:18ch">{bi("One pipeline, from first principles to the patient.", "หนึ่งเส้นทาง จากพื้นฐานสู่ผู้ป่วย")}</h1>
    <p class="lead reveal measure" data-d="2">{bi("Learn. Prove it. Build the product. Four parts, one pipeline.", "เรียนรู้ พิสูจน์ฝีมือ สร้างผลิตภัณฑ์ สี่ส่วน หนึ่งเส้นทาง")}</p>
  </div>
</section>"""

    parts = ""
    blocks = [
        (bi("Academy", "อคาเดมี"), "brain", bi("Learn the craft", "เรียนวิชาชีพ"), "academy.html", bi("Enter the Academy", "เข้าสู่อคาเดมี"),
         bi("An open, practical curriculum in AI and digital health. It runs from what a model is, through clinical data standards like FHIR, medical imaging, and agentic systems, to deployment and governance. Built to be free to start and rigorous enough to matter. Anyone in Thailand can learn here.",
            "หลักสูตรเปิดที่เน้นภาคปฏิบัติ ด้าน AI และสุขภาพดิจิทัล ตั้งแต่โมเดลคืออะไร ผ่านมาตรฐานข้อมูลคลินิกอย่าง FHIR, medical imaging และ agentic systems ไปจนถึง deployment และธรรมาภิบาล ออกแบบให้เริ่มเรียนได้ฟรีและเข้มข้นพอที่จะมีความหมาย ทุกคนในไทยเรียนได้"),
         [bi("Foundations of AI and machine learning", "พื้นฐาน AI และ machine learning"), bi("Clinical data, HL7 and FHIR, EMR systems", "ข้อมูลคลินิก HL7 และ FHIR ระบบ EMR"), bi("Medical imaging and clinical NLP", "Medical imaging และ clinical NLP"), bi("Evaluation, safety, and deployment", "การประเมิน ความปลอดภัย และ deployment")]),
        (bi("Fellowship", "เฟลโลว์ชิป"), "flask", bi("Prove it on real problems", "พิสูจน์บนโจทย์จริง"), "fellowship.html", bi("See the Fellowship", "ดูเฟลโลว์ชิป"),
         bi("A selective, in-residence programme for a small cohort. Fellows are placed on genuine clinical problems with Ramathibodi faculty, supervised data access, and patients in view. The output is reviewed work that ships into a real workflow.",
            "โปรแกรมแบบคัดสรรและประจำในสถานที่ สำหรับกลุ่มเล็ก เฟลโลว์ได้ทำงานกับโจทย์คลินิกจริง ร่วมกับอาจารย์รามาธิบดี เข้าถึงข้อมูลแบบมีการกำกับ และมีผู้ป่วยอยู่ในสายตา ผลลัพธ์คืองานที่ผ่านการรีวิวและนำไปใช้ในเวิร์กโฟลว์จริง"),
         [bi("In-residence at Ramathibodi", "ประจำที่รามาธิบดี"), bi("Mentored by clinicians and engineers", "มีเมนเทอร์เป็นแพทย์และวิศวกร"), bi("Supervised access to clinical data", "เข้าถึงข้อมูลคลินิกแบบมีการกำกับ"), bi("Ends in a deployed, evaluated project", "จบด้วยโปรเจกต์ที่ deploy และประเมินแล้ว")]),
        (bi("Venture Studio", "เวนเจอร์สตูดิโอ"), "rocket", bi("Turn work into product", "เปลี่ยนงานเป็นผลิตภัณฑ์"), "venture.html", bi("Build with us", "สร้างไปกับเรา"),
         bi("The strongest fellowship and member projects do not stop at a demo. The studio adds engineering, regulatory navigation for Software as a Medical Device, and go-to-market support, in step with the National Innovation Agency's path from research to venture.",
            "โปรเจกต์เฟลโลว์ชิปและสมาชิกที่แข็งแกร่งที่สุดไม่หยุดแค่ demo สตูดิโอเสริมด้านวิศวกรรม การนำทางกฎระเบียบสำหรับ Software as a Medical Device และการออกสู่ตลาด สอดคล้องกับเส้นทางจากงานวิจัยสู่เวนเจอร์ของ NIA"),
         [bi("Product engineering and reliability", "วิศวกรรมผลิตภัณฑ์และความน่าเชื่อถือ"), bi("Thai FDA SaMD pathway navigation", "นำทางเส้นทาง SaMD ของ อย."), bi("Clinical validation and evidence", "การตรวจสอบทางคลินิกและหลักฐาน"), bi("Routes to pilot and to market", "เส้นทางสู่การนำร่องและสู่ตลาด")]),
        (bi("Consulting", "ที่ปรึกษานวัตกรรม"), "compass", bi("Build capability in institutions", "สร้างขีดความสามารถในสถาบัน"), "contact.html", bi("Work with us", "ร่วมงานกับเรา"),
         bi("We advise hospitals, agencies, and health technology companies setting up their own AI capability. We are an innovation partner for the next generation of the healthcare workforce, so the people we train have strong places to land.",
            "เราให้คำปรึกษาแก่โรงพยาบาล หน่วยงาน และบริษัทเทคโนโลยีสุขภาพ ที่กำลังสร้างขีดความสามารถ AI ของตนเอง เราเป็นพันธมิตรนวัตกรรมเพื่อกำลังคนสุขภาพรุ่นใหม่ เพื่อให้คนที่เราฝึกมีที่ไปที่แข็งแรง"),
         [bi("Capability and team design", "ออกแบบขีดความสามารถและทีม"), bi("AI governance and evaluation frameworks", "กรอบธรรมาภิบาลและการประเมิน AI"), bi("Workforce training programmes", "โปรแกรมฝึกกำลังคน"), bi("Project and deployment advisory", "ที่ปรึกษาโปรเจกต์และการ deploy")]),
    ]
    photos = ["woman-work.jpg", "doctor.jpg", "analytics.jpg", "meeting.jpg"]
    for i, (name, icon, kicker, href, cta, body, bullets) in enumerate(blocks):
        rev = "split--rev" if i % 2 else ""
        bl = "".join(f'<li class="pill">{b}</li>' for b in bullets)
        parts += f"""
<section class="section">
  <div class="container">
    <div class="split {rev}">
      <div class="stack reveal">
        <span class="eyebrow">{kicker}</span>
        <h2>{name}</h2>
        <p class="lead">{body}</p>
        <ul class="pill-row" style="margin-top:.5rem">{bl}</ul>
        <div class="btn-row"><a class="btn btn--grad" href="{prefix}{href}">{cta} {I['arrow']}</a></div>
      </div>
      {frame(name, "ratio-4x3", "a", photos[i], prefix)}
    </div>
  </div>
</section>"""

    method = sec(
        head(bi("How a person moves through it", "คนคนหนึ่งเดินผ่านมันอย่างไร"), bi("The path is the product.", "เส้นทางคือผลิตภัณฑ์")) +
        flow([
            (bi("Step 01", "ขั้นที่ 01"), bi("Learn", "เรียน"), bi("Start in the Academy. Build the foundations and the clinical context, free and at your own pace.", "เริ่มที่อคาเดมี สร้างพื้นฐานและบริบททางคลินิก ฟรีและตามจังหวะของคุณเอง")),
            (bi("Step 02", "ขั้นที่ 02"), bi("Apply", "สมัคร"), bi("Bring a real problem to the Fellowship, or join a project team. Get matched with a mentor and data.", "นำโจทย์จริงมาที่เฟลโลว์ชิป หรือเข้าร่วมทีม จับคู่กับเมนเทอร์และข้อมูล")),
            (bi("Step 03", "ขั้นที่ 03"), bi("Build", "สร้าง"), bi("Ship a reviewed, evaluated tool into a real clinical workflow. Governance is part of the grade.", "ส่งเครื่องมือที่ผ่านการรีวิวและประเมินเข้าสู่เวิร์กโฟลว์คลินิกจริง ธรรมาภิบาลเป็นส่วนหนึ่งของการวัดผล")),
            (bi("Step 04", "ขั้นที่ 04"), bi("Scale", "ขยายผล"), bi("If it deserves to live, the studio helps it become a product, with a regulatory and market path.", "หากมันคู่ควรที่จะอยู่ต่อ สตูดิโอช่วยให้กลายเป็นผลิตภัณฑ์ พร้อมเส้นทางกฎระเบียบและตลาด")),
        ], [I["brain"], I["flask"], I["shield"], I["rocket"]]))

    return hero + parts + hospital_flow(prefix) + method

def hospital_flow(prefix):
    """Signature hand-sketch, animated hospital-workflow art. Ink on paper,
    editorial captions, a patient token that flows the journey, AI nodes that
    pulse where an agent helps. Bilingual via l-en / l-th (CSS display rules)."""
    def box(x):
        return f'<rect class="fa-box" x="{x-64}" y="96" width="128" height="72" rx="12"/>'
    def ai_shape(x):
        return (f'<line class="fa-link" x1="{x}" y1="168" x2="{x}" y2="250"/>'
                f'<circle class="fa-node" cx="{x}" cy="168" r="4.5"/>'
                f'<rect class="fa-ai" x="{x-92}" y="250" width="184" height="76" rx="14"/>')
    def st_text(x, en, th):
        return (f'<text class="l-en fa-st" x="{x}" y="150" text-anchor="middle">{en}</text>'
                f'<text class="l-th fa-st" x="{x}" y="150" text-anchor="middle">{th}</text>')
    def ai_text(x, en, th):
        return (f'<circle class="fa-pulse" cx="{x-72}" cy="270" r="7"/>'
                f'<text class="fa-tag" x="{x-72}" y="274" text-anchor="middle">AI</text>'
                f'<text class="l-en fa-cap" x="{x+6}" y="268" text-anchor="middle">{en[0]}</text>'
                f'<text class="l-en fa-cap" x="{x+6}" y="286" text-anchor="middle">{en[1]}</text>'
                f'<text class="l-th fa-cap" x="{x+6}" y="268" text-anchor="middle">{th[0]}</text>'
                f'<text class="l-th fa-cap" x="{x+6}" y="286" text-anchor="middle">{th[1]}</text>')
    xs = [110, 320, 530, 740, 950]
    stations = [
        ("Arrival", "มาถึง"), ("Triage", "คัดกรอง"), ("Diagnosis", "วินิจฉัย"),
        ("Treatment", "รักษา"), ("Follow-up", "ติดตาม"),
    ]
    ai_notes = {
        1: (["Triage bot flags", "the urgent first"], ["บอทคัดกรองชู", "เคสด่วนขึ้นก่อน"]),
        2: (["Imaging AI", "pre-reads films"], ["AI ภาพช่วย", "อ่านฟิล์มก่อน"]),
        3: (["Assistant checks", "drug interactions"], ["ผู้ช่วยตรวจ", "ปฏิกิริยาระหว่างยา"]),
        4: (["A Line bot follows", "up safely"], ["บอท Line ติดตาม", "อาการปลอดภัย"]),
    }
    boxes = "".join(box(x) for x in xs)
    ai_shapes = "".join(ai_shape(xs[i]) for i in ai_notes)
    labels = "".join(st_text(x, en, th) for x, (en, th) in zip(xs, stations))
    ai_texts = "".join(ai_text(xs[i], en, th) for i, (en, th) in ai_notes.items())
    # main journey path through the station centres, hand-wobbled by the filter
    path = f"M {xs[0]} 132 C 210 118, 220 146, {xs[1]} 132 S 430 118, {xs[2]} 132 S 640 146, {xs[3]} 132 S 850 118, {xs[4]} 132"
    svg = f"""
<div class="flow-art reveal">
  <svg viewBox="0 0 1060 360" role="img" aria-label="How AI improves the hospital workflow" preserveAspectRatio="xMidYMid meet">
    <defs>
      <filter id="sketch" x="-6%" y="-6%" width="112%" height="112%">
        <feTurbulence type="fractalNoise" baseFrequency="0.014" numOctaves="2" seed="7" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="3.4"/>
      </filter>
      <linearGradient id="fa-grad" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0" stop-color="#fd6502"/><stop offset="0.5" stop-color="#91386e"/><stop offset="1" stop-color="#2a1bd6"/>
      </linearGradient>
    </defs>
    <g filter="url(#sketch)">
      <path class="fa-path" d="{path}"/>
      {boxes}
      {ai_shapes}
      <path id="fa-motion" d="{path}" fill="none" stroke="none"/>
      <circle class="fa-token" r="7"><animateMotion dur="7s" repeatCount="indefinite" rotate="auto"><mpath href="#fa-motion"/></animateMotion></circle>
    </g>
    {labels}
    {ai_texts}
    <text class="fa-hand" x="118" y="64" transform="rotate(-4 118 64)">one line, one patient</text>
    <path class="fa-hand-arrow" d="M150 74 q 6 22 -18 44"/>
    <text class="fa-hand" x="612" y="356" transform="rotate(-2.5 612 356)">a clinician still decides</text>
    <path class="fa-hand-arrow" d="M742 344 q -30 6 -70 8"/>
  </svg>
  <div class="flow-art__legend">
    <span class="l-en">A patient’s journey, drawn by hand. The dot is the patient. Where it glows, an agent is quietly doing the heavy lifting.</span>
    <span class="l-th">เส้นทางของผู้ป่วย วาดด้วยมือ จุดเรืองแสงคือผู้ป่วย ตรงที่มันเรืองแสง มีเอเจนต์กำลังช่วยแบกงานหนักอยู่เงียบ ๆ</span>
  </div>
</div>"""
    return (f'<section class="section"><div class="container">'
            f'{head(bi("Where AI helps", "AI ช่วยตรงไหน"), bi("The same journey, with less friction.", "เส้นทางเดิม แต่สะดุดน้อยลง"), bi("This is not automation for its own sake. At each step, an agent removes a delay, a risk, or a chore, and a clinician keeps the decision. Watch the patient move.", "นี่ไม่ใช่ระบบอัตโนมัติเพื่อความเท่ ในแต่ละขั้น เอเจนต์ช่วยลดความล่าช้า ความเสี่ยง หรืองานน่าเบื่อ โดยที่แพทย์ยังเป็นผู้ตัดสินใจ ลองดูผู้ป่วยเคลื่อนไป"))}'
            f'{svg}</div></section>')

def step(k, title, body):
    return (f'<div class="step reveal"><div class="step__k">{k}</div>'
            f'<div><h3>{title}</h3><p class="mt2">{body}</p></div></div>')

def nested_system():
    """Who We Are motif: the club, inside Ramathibodi, inside the Thai health
    system. Concentric hand-drawn rings, one gradient at the centre. Minimal,
    Rams-clean, drawn by our own hand."""
    return """
<div class="motif reveal">
  <svg viewBox="0 0 400 420" role="img" aria-label="The club, inside Ramathibodi, inside the Thai health system">
    <defs>
      <filter id="sk-nest" x="-8%" y="-8%" width="116%" height="116%">
        <feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="2" seed="4" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="3.6"/>
      </filter>
      <linearGradient id="nest-grad" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#fd6502"/><stop offset="1" stop-color="#2a1bd6"/>
      </linearGradient>
    </defs>
    <g filter="url(#sk-nest)" fill="none">
      <circle class="nest-ring nest-ring--o" cx="200" cy="220" r="182"/>
      <circle class="nest-ring nest-ring--m" cx="200" cy="220" r="120"/>
      <circle class="nest-ring--i" cx="200" cy="220" r="60" stroke="url(#nest-grad)" stroke-width="3" fill="none"/>
      <circle cx="200" cy="220" r="7" fill="url(#nest-grad)" stroke="none"/>
    </g>
    <text class="l-en nest-label" x="200" y="62" text-anchor="middle">Thai health system</text>
    <text class="l-th nest-label" x="200" y="62" text-anchor="middle">ระบบสุขภาพไทย</text>
    <text class="nest-label" x="200" y="124" text-anchor="middle">Ramathibodi</text>
    <text class="l-en nest-hand" x="200" y="258" text-anchor="middle">the club</text>
    <text class="l-th nest-hand" x="200" y="258" text-anchor="middle">ชมรม</text>
  </svg>
</div>"""

# ===========================================================================
# ACADEMY (public overview)
# ===========================================================================
def learning_trail(prefix):
    """Second signature sketch: a hand-drawn switchback trail through the six
    domains, distinct in shape from the hospital-flow diagram (that one is a
    smooth clinical path, this one is a hiking map). Narrates the climb."""
    pts = [(90, 230), (280, 130), (470, 250), (660, 110), (850, 230), (1000, 150)]
    names = [
        ("Basics", "พื้นฐาน"), ("AI Agent", "AI Agent"), ("Deep AI", "Deep AI"),
        ("Digital Health", "สุขภาพดิจิทัล"), ("Deployment", "Deployment"), ("Capstone", "Capstone"),
    ]
    def waypoint(i, x, y, en, th):
        yoff = -34 if y < 180 else 46
        return (f'<circle class="lt-node" cx="{x}" cy="{y}" r="9"/>'
                f'<text class="lt-num" x="{x}" y="{y+4}" text-anchor="middle">{i+1}</text>'
                f'<text class="l-en lt-lab" x="{x}" y="{y+yoff}" text-anchor="middle">{en}</text>'
                f'<text class="l-th lt-lab" x="{x}" y="{y+yoff}" text-anchor="middle">{th}</text>')
    waypoints = "".join(waypoint(i, x, y, en, th) for i, ((x, y), (en, th)) in enumerate(zip(pts, names)))
    d = (f"M {pts[0][0]} {pts[0][1]} "
         + " ".join(f"Q {(pts[i][0]+pts[i+1][0])//2} {pts[i][1] if i%2==0 else pts[i+1][1]}, {pts[i+1][0]} {pts[i+1][1]}"
                    for i in range(len(pts)-1)))
    svg = f"""
<div class="flow-art reveal">
  <svg viewBox="0 0 1060 320" role="img" aria-label="The Academy learning trail" preserveAspectRatio="xMidYMid meet">
    <defs>
      <filter id="sketch2" x="-6%" y="-6%" width="112%" height="112%">
        <feTurbulence type="fractalNoise" baseFrequency="0.016" numOctaves="2" seed="11" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="3.8"/>
      </filter>
      <linearGradient id="lt-grad" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0" stop-color="#2a1bd6"/><stop offset="0.5" stop-color="#91386e"/><stop offset="1" stop-color="#fd6502"/>
      </linearGradient>
    </defs>
    <g filter="url(#sketch2)">
      <path class="lt-path" d="{d}"/>
      {waypoints}
      <path id="lt-motion" d="{d}" fill="none" stroke="none"/>
      <circle class="lt-token" r="7"><animateMotion dur="9s" repeatCount="indefinite" rotate="auto"><mpath href="#lt-motion"/></animateMotion></circle>
    </g>
    <text class="fa-hand" x="70" y="70" transform="rotate(-4 70 70)">everyone starts here</text>
    <path class="fa-hand-arrow" d="M108 78 q 4 24 -12 44"/>
    <text class="fa-hand" x="880" y="90" transform="rotate(3 880 90)">one real thing, shipped</text>
    <path class="fa-hand-arrow" d="M950 100 q 20 20 30 44"/>
  </svg>
  <div class="flow-art__legend">
    <span class="l-en">The same trail, whoever you are. Six waypoints, one climb, drawn as you would sketch it on the back of an envelope.</span>
    <span class="l-th">เส้นทางเดียวกัน ไม่ว่าคุณจะเป็นใคร หกจุดพัก หนึ่งการไต่ระดับ วาดเหมือนร่างไว้หลังซองจดหมาย</span>
  </div>
</div>"""
    return (f'<section class="section"><div class="container">'
            f'{head(bi("The trail", "เส้นทาง"), bi("Six waypoints, one climb.", "หกจุดพัก หนึ่งการไต่ระดับ"), bi("This is not six separate courses. It is one trail. Each waypoint changes what you can see from the next.", "นี่ไม่ใช่หกคอร์สที่แยกกัน แต่เป็นเส้นทางเดียว แต่ละจุดพักเปลี่ยนมุมมองที่คุณเห็นจากจุดถัดไป"))}'
            f'{svg}</div></section>')

def fellowship_orbit(prefix):
    """Third signature sketch: one year as a single orbit, four waypoints
    around it, one gradient mark at the centre where the year's work lands
    on a patient. Distinct shape from the trail (hiking map) and the
    hospital-flow (clinical path): this one is a closed loop, a year that
    returns to the same place changed."""
    cx, cy, r = 260, 175, 128
    import math
    stops = [
        (0, "Match", "จับคู่"),
        (1, "Build", "สร้าง"),
        (2, "Evaluate", "ประเมิน"),
        (3, "Ship", "ส่งมอบ"),
    ]
    def pt(i):
        a = -math.pi/2 + i * (math.pi/2)
        return (cx + r*math.cos(a), cy + r*math.sin(a))
    nodes = ""
    for i, en, th in stops:
        x, y = pt(i)
        anchor = "middle"
        yoff = -22 if y < cy else 34
        xoff = 0
        if abs(x - cx) > 40:
            anchor = "start" if x > cx else "end"
            xoff = 16 if x > cx else -16
            yoff = 5
        nodes += (f'<circle class="fo-node" cx="{x:.0f}" cy="{y:.0f}" r="8"/>'
                  f'<text class="l-en fo-lab" x="{x+xoff:.0f}" y="{y+yoff:.0f}" text-anchor="{anchor}">{en}</text>'
                  f'<text class="l-th fo-lab" x="{x+xoff:.0f}" y="{y+yoff:.0f}" text-anchor="{anchor}">{th}</text>')
    svg = f"""
<div class="flow-art reveal">
  <svg viewBox="0 0 520 360" role="img" aria-label="The Fellowship year, as one orbit" preserveAspectRatio="xMidYMid meet">
    <defs>
      <filter id="sketch3" x="-8%" y="-8%" width="116%" height="116%">
        <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="19" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="3.2"/>
      </filter>
      <radialGradient id="fo-grad" cx="50%" cy="50%" r="60%">
        <stop offset="0" stop-color="#fd6502"/><stop offset="0.55" stop-color="#91386e"/><stop offset="1" stop-color="#2a1bd6"/>
      </radialGradient>
    </defs>
    <g filter="url(#sketch3)" fill="none">
      <circle class="fo-orbit" cx="{cx}" cy="{cy}" r="{r}"/>
      {nodes}
    </g>
    <circle cx="{cx}" cy="{cy}" r="15" fill="url(#fo-grad)"/>
    <text class="fa-hand" x="{cx-46}" y="{cy+56}" transform="rotate(-3 {cx-46} {cy+56})">one patient, one year</text>
    <path class="fa-hand-arrow" d="M{cx-10} {cy+40} q -14 -10 -18 -22"/>
  </svg>
  <div class="flow-art__legend">
    <span class="l-en">A year is not a line. It is a loop you complete once, closely watched, and it changes where you land.</span>
    <span class="l-th">หนึ่งปีไม่ใช่เส้นตรง แต่เป็นวงที่คุณเดินให้ครบหนึ่งรอบ ภายใต้การดูแลอย่างใกล้ชิด และมันเปลี่ยนจุดที่คุณจะไปถึง</span>
  </div>
</div>"""
    return (f'<section class="section"><div class="container">'
            f'{head(bi("The year", "หนึ่งปี"), bi("One loop, four waypoints.", "หนึ่งวงจร สี่จุดพัก"))}'
            f'{svg}</div></section>')

def competency_spine():
    """The four-pillar competency spine: Fluency, Builder, Strategist,
    Steward. A clean typographic panel, not a hand-sketch, because this is
    information architecture, not narrative. Each row's accent bar samples
    one stop of the brand gradient, so four rows read as one family rather
    than four arbitrary colours."""
    pillars = [
        ("#3412d1", "I", bi("Fluency", "ความเข้าใจพื้นฐาน"), bi("Read, question, and evaluate the AI tools a graduate meets at work.", "อ่าน ตั้งคำถาม และประเมินเครื่องมือ AI ที่บัณฑิตจะเจอในการทำงาน")),
        ("#7a2ba8", "II", bi("Builder", "ผู้สร้าง"), bi("Design, train, and evaluate a model, then ship it into a real workflow.", "ออกแบบ ฝึกโมเดล ประเมินผล แล้วนำไปใช้จริงในเวิร์กโฟลว์")),
        ("#b0507a", "III", bi("Strategist", "นักกลยุทธ์"), bi("Decide build, buy, or wait, and manage the change an institution needs.", "ตัดสินใจสร้าง ซื้อ หรือรอ และบริหารการเปลี่ยนแปลงที่สถาบันต้องการ")),
        ("#fd6502", "IV", bi("Steward", "ผู้ดูแลระยะยาว"), bi("Watch over a tool for years: monitor drift, audit bias, know when to retire it.", "ดูแลเครื่องมือในระยะยาว เฝ้าระวังความคลาดเคลื่อน ตรวจสอบอคติ และรู้ว่าเมื่อไรควรเลิกใช้")),
    ]
    rows = "".join(
        f'<div class="spine-row" style="border-left-color:{color}">'
        f'<span class="spine-row__num" style="color:{color}">{num}</span>'
        f'<div class="spine-row__body"><h3>{title}</h3><p>{desc}</p></div>'
        f'</div>'
        for color, num, title, desc in pillars)
    return f"""
<section class="section section--tight">
  <div class="container">
    <span class="eyebrow reveal">{bi("The four-pillar competency spine", "แกนกลางสี่เสาหลักของทักษะ")}</span>
    <h2 class="reveal mt3">{bi("Everyone climbs the same spine.", "ทุกคนไต่บันไดเดียวกัน")}</h2>
    <p class="lead reveal mt3 measure">{bi("The six courses teach the craft. This is the judgement the craft is for: from reading a tool honestly, to building one, to deciding where it belongs, to watching over it for years.", "หกคอร์สสอนวิชาชีพ นี่คือวิจารณญาณที่วิชาชีพนั้นมีไว้เพื่อ ตั้งแต่อ่านเครื่องมืออย่างตรงไปตรงมา ไปจนถึงสร้างมันขึ้นมา ตัดสินใจว่ามันควรอยู่ตรงไหน และดูแลมันในระยะยาว")}</p>
    <div class="spine reveal mt5">{rows}</div>
  </div>
</section>"""

def academy(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:3rem">
  <div class="hero__glow"></div>
  <div class="container">
    {note_hand("read, run, build", "อ่าน ลงมือทำ สร้าง")}
    <span class="eyebrow reveal">{bi("The Academy", "อคาเดมี")}</span>
    <h1 class="reveal" data-d="1" style="max-width:19ch">{bi("The open curriculum for medical AI in Thailand.", "หลักสูตรเปิดด้าน AI การแพทย์ สำหรับประเทศไทย")}</h1>
    <p class="lead reveal measure" data-d="2">{bi("From what a model is, to a patient it safely reaches. Free to start.", "ตั้งแต่โมเดลคืออะไร ถึงผู้ป่วยที่มันไปถึงอย่างปลอดภัย เริ่มเรียนฟรี")}</p>
    <div class="btn-row reveal" data-d="3">
      <a class="btn btn--grad btn--lg" href="{prefix}academy/gate.html">{bi("Enter the Academy", "เข้าสู่อคาเดมี")} {I['arrow']}</a>
      <a class="btn btn--ghost btn--lg" href="{prefix}fellowship.html">{bi("Or apply for the Fellowship", "หรือสมัครเฟลโลว์ชิป")}</a>
    </div>
    <p class="muted mt4" style="font-size:.85rem">{I['lock']} {bi("Curriculum is open to enrolled members. Ask your programme lead for the access code.", "หลักสูตรเปิดสำหรับสมาชิกที่ลงทะเบียน ขอรหัสเข้าใช้งานจากผู้ดูแลโปรแกรมของคุณ")}</p>
  </div>
</section>"""

    lv_all = bi("All levels", "ทุกระดับ")
    lv_int = bi("Intermediate", "ระดับกลาง")
    hands = bi("Hands-on", "ลงมือทำ")
    openc = bi("Open course", "เปิดคอร์ส")
    courses = [
        ("01", I["brain"], bi("Basics", "พื้นฐาน"), bi("No-code and vibe coding, Git, documentation, APIs, and the cloud. Start from zero, lose the fear of the blank screen.", "No-code และ vibe coding, Git, เอกสาร, API และคลาวด์ เริ่มจากศูนย์ ทิ้งความกลัวหน้าจอเปล่า"), [lv_all, hands], "academy/learn/curriculum__basics.html"),
        ("02", I["node"], bi("AI Agent", "AI Agent"), bi("LLMs, hallucination, guardrails, RAG, speech, and real agents on Line, n8n, and Cloud Run.", "LLM, hallucination, guardrails, RAG, speech และ agent จริงบน Line, n8n และ Cloud Run"), [lv_int, hands], "academy/learn/curriculum__ai-agent.html"),
        ("03", I["pulse"], bi("Deep AI", "Deep AI"), bi("Deep learning for images, signals, sound, and tables, plus explainability that a clinician can read.", "Deep learning สำหรับภาพ สัญญาณ เสียง และตาราง พร้อม explainability ที่แพทย์อ่านเข้าใจ"), [lv_int, hands], "academy/learn/curriculum__deep-ai.html"),
        ("04", I["doc"], bi("Digital Health", "สุขภาพดิจิทัล"), bi("HIS, EMR and PHR, ICD-10, HL7 and FHIR, PDPA, Genomics Thailand, and NHSO claims data.", "HIS, EMR และ PHR, ICD-10, HL7 และ FHIR, PDPA, Genomics Thailand และข้อมูลเคลม NHSO"), [lv_all, hands], "academy/learn/curriculum__digital-health.html"),
        ("05", I["rocket"], bi("Deployment", "Deployment"), bi("Dashboards, web prototyping, cloud and on-premise, and statistics that hold up in front of clinicians.", "แดชบอร์ด web prototyping คลาวด์และ on-premise และสถิติที่เชื่อถือได้ต่อหน้าแพทย์"), [lv_int, hands], "academy/learn/curriculum__deployment.html"),
        ("06", I["shield"], bi("Strategy & Governance", "กลยุทธ์และธรรมาภิบาล"), bi("Thai FDA, AI as Software as a Medical Device, ISO, and the regulatory path from prototype to approval.", "อย. AI ในฐานะ Software as a Medical Device, ISO และเส้นทางกฎระเบียบจากต้นแบบสู่การอนุมัติ"), [lv_all], "academy/learn/curriculum__governance.html"),
    ]
    cat = "".join(course_card(n, ic, t, d, tg, h, prefix, openc) for n, ic, t, d, tg, h in courses)
    modules = sec(
        head(bi("The curriculum", "หลักสูตร"), bi("Six courses, one through-line.", "หกคอร์ส หนึ่งเส้นทางเชื่อมโยง"),
             bi("Each course is hands-on. You write code, read clinical data, and build something that runs. Notebooks open in the browser or in Colab.", "ทุกคอร์สเน้นลงมือทำ คุณเขียนโค้ด อ่านข้อมูลคลินิก และสร้างสิ่งที่รันได้จริง เปิด notebook ในเบราว์เซอร์หรือใน Colab")) +
        f'<div class="catalog">{cat}</div>') + learning_trail(prefix) + competency_spine()

    fmt = f"""
<section class="section">
  <div class="container">
    <div class="band reveal">
      <div class="band__glow"></div>
      <div class="container" style="padding-block:clamp(3rem,6vw,5rem)">
        <span class="eyebrow" style="color:#cbd5ef">{bi("How it runs", "หลักสูตรทำงานอย่างไร")}</span>
        <h2 class="mt3">{bi("Read, run, build. In that order.", "อ่าน รัน สร้าง ตามลำดับนั้น")}</h2>
        <div class="grid grid-3 mt5">
          <div><div class="stat__num" style="color:#fff">{bi("Self-paced", "เรียนตามจังหวะตัวเอง")}</div><p style="color:#9fb0d4" class="mt2">{bi("Open the curriculum any time. Notebooks run in the browser or Google Colab.", "เปิดหลักสูตรได้ทุกเวลา notebook รันในเบราว์เซอร์หรือ Google Colab")}</p></div>
          <div><div class="stat__num" style="color:#fff">{bi("Project-based", "เน้นโปรเจกต์")}</div><p style="color:#9fb0d4" class="mt2">{bi("Every track ends in something you built and can show, not a multiple-choice quiz.", "ทุกโดเมนจบด้วยสิ่งที่คุณสร้างและโชว์ได้ ไม่ใช่ข้อสอบปรนัย")}</p></div>
          <div><div class="stat__num" style="color:#fff">{bi("Pathways", "เส้นทาง")}</div><p style="color:#9fb0d4" class="mt2">{bi("Routes for clinicians and for engineers, meeting in the middle on real cases.", "เส้นทางสำหรับแพทย์และวิศวกร มาบรรจบกันตรงกลางบนเคสจริง")}</p></div>
        </div>
      </div>
    </div>
  </div>
</section>"""

    cta = f"""
<section class="section">
  <div class="container center stack reveal">
    <h2 class="measure" style="margin-inline:auto">{bi("Ready to start building?", "พร้อมเริ่มสร้างหรือยัง")}</h2>
    <p class="lead measure" style="margin-inline:auto">{bi("The whole curriculum is one login away.", "หลักสูตรทั้งหมดอยู่ห่างแค่การเข้าสู่ระบบครั้งเดียว")}</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn--grad btn--lg" href="{prefix}academy/gate.html">{bi("Enter the Academy", "เข้าสู่อคาเดมี")} {I['arrow']}</a>
    </div>
  </div>
</section>"""
    return hero + modules + fmt + cta

# ===========================================================================
# FELLOWSHIP (Steve Jobs Archive inspired: quiet, generous, story-led)
# ===========================================================================
def fellowship(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem">
  <div class="hero__glow"></div>
  <div class="container">
    {note_hand("a year, in residence", "หนึ่งปี ประจำในสถานที่")}
    <span class="eyebrow reveal">{bi("The Fellowship", "เฟลโลว์ชิป")}</span>
    <h1 class="reveal" data-d="1" style="max-width:17ch">{bi("A year to build something that reaches a patient.", "หนึ่งปี เพื่อสร้างสิ่งที่ไปถึงผู้ป่วย")}</h1>
    <p class="lead reveal measure" data-d="2">{bi("Small on purpose. Real problems, real data, Ramathibodi behind you.", "ตั้งใจให้เล็ก โจทย์จริง ข้อมูลจริง มีรามาธิบดีหนุนหลัง")}</p>
    <div class="btn-row reveal" data-d="3">
      <a class="btn btn--grad btn--lg" href="{prefix}fellowship/apply.html">{bi("Apply", "สมัคร")} {I['arrow']}</a>
      <a class="btn btn--ghost btn--lg" href="{prefix}fellowship/stories.html">{bi("Read fellow stories", "อ่านเรื่องราวเฟลโลว์")}</a>
    </div>
  </div>
</section>"""

    orbit = fellowship_orbit(prefix)

    quote = sec(
        '<blockquote class="prose reveal" style="max-width:34ch;margin-inline:auto;text-align:center;border:0;font-size:var(--step-3);padding:0">'
        + bi('"The point is not to learn about medical AI. The point is to build it, well enough that a hospital will use it."',
             '"เป้าหมายไม่ใช่แค่เรียนรู้เรื่อง AI การแพทย์ แต่คือการสร้างมัน ให้ดีพอที่โรงพยาบาลจะใช้จริง"')
        + '</blockquote>', "section")

    pillars = sec(
        head(bi("What a fellow gets", "เฟลโลว์ได้อะไร"), bi("Everything you need to do real work.", "ทุกอย่างที่คุณต้องมีเพื่อทำงานจริง")) +
        '<div class="grid grid-2">' +
        ctx['card']('flask', bi('A real problem', 'โจทย์จริง'), bi('You are matched to a live clinical question that a department actually wants solved, not a toy dataset.', 'คุณถูกจับคู่กับคำถามคลินิกจริงที่หน่วยงานอยากแก้จริง ไม่ใช่ dataset ของเล่น'), None, '', prefix) +
        ctx['card']('users', bi('Mentorship', 'การเป็นเมนเทอร์'), bi('A clinician and an engineer in your corner, plus a cohort building alongside you.', 'แพทย์และวิศวกรอยู่ข้างคุณ พร้อมเพื่อนร่วมรุ่นที่สร้างไปด้วยกัน'), None, '', prefix) +
        ctx['card']('shield', bi('Supervised data', 'ข้อมูลที่มีการกำกับ'), bi('Governed access to clinical data, with privacy and evaluation handled the right way.', 'การเข้าถึงข้อมูลคลินิกที่มีการกำกับ พร้อมจัดการความเป็นส่วนตัวและการประเมินอย่างถูกวิธี'), None, '', prefix) +
        ctx['card']('rocket', bi('A route to scale', 'เส้นทางสู่การขยายผล'), bi('If your work deserves it, the venture studio helps it become a product with a regulatory path.', 'หากงานของคุณคู่ควร เวนเจอร์สตูดิโอช่วยให้มันเป็นผลิตภัณฑ์พร้อมเส้นทางกฎระเบียบ'), None, '', prefix) +
        '</div>')

    tracks = sec(
        head(bi("Tracks", "แทร็ก"), bi("Pick the work, not just the topic.", "เลือกที่งาน ไม่ใช่แค่หัวข้อ")) +
        '<div class="grid grid-2">' +
        task_card('pulse', "Clinical AI", bi("Decision support and risk", "decision support และความเสี่ยง"), bi("Models that help clinicians decide, evaluated against real outcomes and real workflows.", "โมเดลที่ช่วยแพทย์ตัดสินใจ ประเมินเทียบกับผลลัพธ์จริงและเวิร์กโฟลว์จริง"), ctx, 1) +
        task_card('doc', "Imaging", bi("Vision for diagnosis", "vision เพื่อการวินิจฉัย"), bi("Radiology and pathology tools, from data pipeline to a validated, deployable model.", "เครื่องมือด้านรังสีวิทยาและพยาธิวิทยา ตั้งแต่ data pipeline จนถึงโมเดลที่ตรวจสอบและ deploy ได้"), ctx, 2) +
        task_card('node', "Health Data", bi("FHIR and interoperability", "FHIR และ interoperability"), bi("The plumbing of a modern health system, and the AI that rides on top of it.", "ระบบท่อของระบบสุขภาพสมัยใหม่ และ AI ที่ทำงานอยู่บนมัน"), ctx, 1) +
        task_card('flask', "Agents", bi("Operational intelligence", "ปัญญาด้านปฏิบัติการ"), bi("Agentic systems for the administrative and operational load that slows care down.", "agentic systems สำหรับภาระงานธุรการและปฏิบัติการที่ทำให้การดูแลช้าลง"), ctx, 2) +
        '</div>' +
        f'<div class="btn-row mt5 reveal"><a class="btn btn--ghost" href="{prefix}fellowship/apply.html">{bi("See eligibility and apply", "ดูคุณสมบัติและสมัคร")} {I["arrow"]}</a></div>')

    links = sec(
        '<div class="grid grid-3">' +
        ctx['card']('doc', bi('Publications', 'ผลงานตีพิมพ์'), bi('Papers, technical reports, and open releases from fellows and the club.', 'บทความ รายงานเทคนิค และการเผยแพร่แบบเปิดจากเฟลโลว์และคลับ'), 'fellowship/publications.html', bi('Read', 'อ่าน'), prefix) +
        ctx['card']('users', bi('Stories', 'เรื่องราว'), bi('How fellows chose their problem and what they built.', 'เฟลโลว์เลือกโจทย์อย่างไร และสร้างอะไรขึ้นมา'), 'fellowship/stories.html', bi('Read', 'อ่าน'), prefix) +
        ctx['card']('compass', bi('FAQ', 'คำถามที่พบบ่อย'), bi('Eligibility, time commitment, funding, and how selection works.', 'คุณสมบัติ เวลาที่ต้องใช้ ทุน และการคัดเลือกทำงานอย่างไร'), 'fellowship/faq.html', bi('Read', 'อ่าน'), prefix) +
        '</div>')

    return hero + orbit + quote + pillars + tracks + links

def fellowship_apply(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">{bi("Apply", "สมัคร")}</span>
  <h1 class="reveal" data-d="1" style="max-width:18ch">{bi("Tell us the problem you want to solve.", "บอกเราว่าคุณอยากแก้โจทย์อะไร")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("We select for judgement and drive more than for a perfect resume. If you can hold a clinical problem and a technical one at once, we want to read your application.", "เราคัดเลือกจากวิจารณญาณและความมุ่งมั่น มากกว่าเรซูเม่ที่สมบูรณ์แบบ ถ้าคุณถือโจทย์คลินิกไว้มือหนึ่งและโจทย์เทคนิคไว้อีกมือหนึ่งได้ เราอยากอ่านใบสมัครของคุณ")}</p>
</div></section>"""
    who = sec(
        head(bi("Who should apply", "ใครควรสมัคร"), bi("Three kinds of people, one room.", "สามแบบคน หนึ่งห้อง")) +
        '<div class="grid grid-3">' +
        ctx['card']('pulse', bi('Clinicians', 'บุคลากรทางการแพทย์'), bi('Doctors, nurses, and allied health staff who see the problems daily and want to build the fix.', 'แพทย์ พยาบาล และบุคลากรสายสุขภาพที่เห็นปัญหาทุกวัน และอยากลงมือสร้างทางแก้'), None, '', prefix) +
        ctx['card']('node', bi('Engineers and scientists', 'วิศวกรและนักวิทยาศาสตร์'), bi('Software, data, and ML people who want their work to matter in a clinic.', 'คนสายซอฟต์แวร์ ข้อมูล และ ML ที่อยากให้งานของตัวเองมีความหมายในคลินิก'), None, '', prefix) +
        ctx['card']('brain', bi('Students', 'นักศึกษา'), bi('Advanced students from medicine, engineering, and data science ready for real responsibility.', 'นักศึกษาชั้นสูงจากแพทยศาสตร์ วิศวกรรม และวิทยาศาสตร์ข้อมูล ที่พร้อมรับผิดชอบงานจริง'), None, '', prefix) +
        '</div>')
    how = sec(
        head(bi("How selection works", "การคัดเลือกทำงานอย่างไร"), bi("Four steps, no theatre.", "สี่ขั้นตอน ไม่มีพิธีรีตอง")) +
        '<div class="steps">' +
        step("01", bi("Apply", "สมัคร"), bi("Send a short application and the problem you care about. No long forms.", "ส่งใบสมัครสั้น ๆ พร้อมโจทย์ที่คุณสนใจ ไม่มีแบบฟอร์มยาวเยิ่นเย้อ")) +
        step("02", bi("Conversation", "พูดคุย"), bi("A focused conversation about your problem, your background, and fit.", "บทสนทนาที่เจาะจงเรื่องโจทย์ของคุณ ประสบการณ์ และความเหมาะสม")) +
        step("03", bi("Scoping", "กำหนดขอบเขต"), bi("We shape your problem into a project with a mentor and a data plan.", "เราช่วยปั้นโจทย์ของคุณให้เป็นโปรเจกต์ พร้อมเมนเทอร์และแผนข้อมูล")) +
        step("04", bi("Cohort", "เข้ารุ่น"), bi("Join the cohort, get access, and start building under supervision.", "เข้าร่วมรุ่น ได้รับสิทธิ์เข้าถึง แล้วเริ่มสร้างภายใต้การกำกับดูแล")) +
        '</div>' +
        f'<div class="btn-row mt5 reveal"><a class="btn btn--grad btn--lg" href="{prefix}contact.html">{bi("Start your application", "เริ่มสมัคร")} {I["arrow"]}</a><a class="btn btn--ghost btn--lg" href="{prefix}fellowship/faq.html">{bi("Read the FAQ", "อ่านคำถามที่พบบ่อย")}</a></div>')
    return hero + who + how

def fellowship_stories(prefix, ctx):
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">{bi("Stories", "เรื่องราว")}</span>
  <h1 class="reveal" data-d="1" style="max-width:18ch">{bi("The work, in the words of the people who built it.", "ผลงาน เล่าโดยคนที่สร้างมันขึ้นมา")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("Profiles of fellows and their projects will be published here as cohorts complete. The shape is always the same: a real problem, a hard build, a tool in use.", "โปรไฟล์ของเฟลโลว์และโปรเจกต์จะเผยแพร่ที่นี่เมื่อแต่ละรุ่นจบการศึกษา รูปแบบเดิมเสมอ โจทย์จริง การสร้างที่ยาก และเครื่องมือที่ใช้งานจริง")}</p>
</div></section>"""
    grid = sec(
        '<div class="grid grid-3">' +
        entry(bi("Story", "เรื่องราว"), bi("From ward round to working model", "จากรอบหอผู้ป่วยสู่โมเดลที่ใช้งานได้"), bi("How a resident turned a daily frustration into a deployed risk tool. Coming soon.", "แพทย์ประจำบ้านคนหนึ่งเปลี่ยนความหงุดหงิดในทุกวันให้เป็นเครื่องมือประเมินความเสี่ยงที่ deploy จริง เร็ว ๆ นี้"), prefix + "fellowship/stories.html", "a") +
        entry(bi("Story", "เรื่องราว"), bi("Reading scans, faster and safer", "อ่านภาพสแกน เร็วขึ้นและปลอดภัยขึ้น"), bi("An imaging fellow's path from dataset to a validated classifier. Coming soon.", "เส้นทางของเฟลโลว์สายภาพจากชุดข้อมูลสู่ classifier ที่ผ่านการตรวจสอบ เร็ว ๆ นี้"), prefix + "fellowship/stories.html", "b") +
        entry(bi("Story", "เรื่องราว"), bi("Making the data speak FHIR", "ทำให้ข้อมูลพูดภาษา FHIR"), bi("Building the interoperability layer a department had been missing. Coming soon.", "สร้างชั้น interoperability ที่แผนกหนึ่งขาดหายไปนาน เร็ว ๆ นี้"), prefix + "fellowship/stories.html", "c") +
        '</div>')
    return hero + grid

def fellowship_publications(prefix, ctx):
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">{bi("Publications", "ผลงานตีพิมพ์")}</span>
  <h1 class="reveal" data-d="1" style="max-width:18ch">{bi("What we learn, we publish.", "สิ่งที่เราเรียนรู้ เราเผยแพร่")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("Papers, technical reports, datasets, and open-source releases from the club and its fellows. We share methods and evidence so the whole Thai ecosystem moves faster.", "บทความ รายงานเทคนิค ชุดข้อมูล และซอฟต์แวร์โอเพนซอร์สจากชมรมและเฟลโลว์ เราแบ่งปันวิธีการและหลักฐาน เพื่อให้ระบบนิเวศไทยทั้งหมดก้าวไปเร็วขึ้น")}</p>
</div></section>"""
    rows = sec(
        '<div class="rows">' +
        row("2026", bi("Evaluation practices for clinical AI in Thai hospitals", "แนวปฏิบัติการประเมิน AI ทางคลินิกในโรงพยาบาลไทย"), bi("A practical framework for honest evaluation before deployment. In preparation.", "กรอบการทำงานเชิงปฏิบัติสำหรับการประเมินอย่างตรงไปตรงมาก่อนนำไปใช้จริง กำลังจัดทำ")) +
        row("2026", bi("FHIR adoption patterns in Thai EMR systems", "รูปแบบการใช้ FHIR ในระบบ EMR ของไทย"), bi("What we found building on real hospital data. In preparation.", "สิ่งที่เราพบจากการสร้างงานบนข้อมูลโรงพยาบาลจริง กำลังจัดทำ")) +
        row("Open", bi("DHA teaching notebooks", "Notebook การสอนของ DHA"), bi("The Academy's hands-on notebooks, released openly for educators.", "Notebook ภาคปฏิบัติของอคาเดมี เผยแพร่แบบเปิดสำหรับผู้สอน")) +
        '</div>')
    return hero + rows

def fellowship_faq(prefix, ctx):
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">{bi("FAQ", "คำถามที่พบบ่อย")}</span>
  <h1 class="reveal" data-d="1" style="max-width:16ch">{bi("Questions, answered plainly.", "คำถาม ตอบตรง ๆ")}</h1>
</div></section>"""
    qa = [
        (bi("Who can apply to the Fellowship?", "ใครสมัครเฟลโลว์ชิปได้บ้าง"), bi("Clinicians, engineers, scientists, and advanced students based in Thailand or able to be in residence at Ramathibodi. You do not need to be from Ramathibodi to apply.", "บุคลากรทางการแพทย์ วิศวกร นักวิทยาศาสตร์ และนักศึกษาชั้นสูงที่อยู่ในไทยหรือสามารถประจำที่รามาธิบดีได้ คุณไม่จำเป็นต้องมาจากรามาธิบดีเพื่อสมัคร")),
        (bi("Do I need to be a strong programmer?", "ต้องเขียนโปรแกรมเก่งไหม"), bi("You need to be able to learn fast and build. The Academy gives you the foundations. Clinicians without a coding background have a pathway in.", "คุณแค่ต้องเรียนรู้เร็วและลงมือสร้างได้ อคาเดมีให้พื้นฐานกับคุณ บุคลากรทางการแพทย์ที่ไม่มีพื้นโค้ดก็มีเส้นทางเข้ามาได้")),
        (bi("How long is the Fellowship?", "เฟลโลว์ชิปใช้เวลานานแค่ไหน"), bi("It runs as a cohort across roughly a year, ending in a deployed, evaluated project. Exact dates are published each intake.", "รันเป็นรุ่น ระยะเวลาประมาณหนึ่งปี จบด้วยโปรเจกต์ที่ deploy และประเมินแล้ว วันที่แน่นอนประกาศในแต่ละรอบรับสมัคร")),
        (bi("Is it full time?", "ต้องทำเต็มเวลาไหม"), bi("It is designed for serious commitment. We work with clinical schedules where we can, but the build is real and takes real hours.", "ออกแบบมาให้ต้องทุ่มเทจริงจัง เราปรับให้เข้ากับตารางคลินิกเท่าที่ทำได้ แต่งานสร้างเป็นเรื่องจริงที่ต้องใช้เวลาจริง")),
        (bi("Is there funding?", "มีทุนสนับสนุนไหม"), bi("Funding and support vary by cohort and partner. Details are shared during the conversation stage so there are no surprises.", "ทุนและการสนับสนุนแตกต่างกันไปตามรุ่นและพันธมิตร รายละเอียดจะแจ้งในขั้นตอนพูดคุย เพื่อไม่ให้มีเรื่องเซอร์ไพรส์")),
        (bi("What is the difference between the Academy and the Fellowship?", "อคาเดมีกับเฟลโลว์ชิปต่างกันอย่างไร"), bi("The Academy is open and teaches the craft. The Fellowship is selective and is where you prove it on a real clinical problem with data and mentorship.", "อคาเดมีเปิดกว้างและสอนวิชาชีพ เฟลโลว์ชิปคัดสรรและเป็นที่ที่คุณพิสูจน์ฝีมือบนโจทย์คลินิกจริง พร้อมข้อมูลและเมนเทอร์")),
        (bi("Who owns what I build?", "ใครเป็นเจ้าของสิ่งที่ฉันสร้าง"), bi("Arrangements are set out clearly before you start, balancing your credit, patient safety, and the institution's responsibilities. Nothing is hidden.", "ข้อตกลงถูกกำหนดไว้ชัดเจนก่อนเริ่ม โดยสมดุลระหว่างเครดิตของคุณ ความปลอดภัยของผู้ป่วย และความรับผิดชอบของสถาบัน ไม่มีอะไรถูกซ่อนไว้")),
    ]
    items = "".join(
        f'<details class="row reveal" style="display:block"><summary style="cursor:pointer;font-family:var(--font-display);font-weight:700;font-size:var(--step-1)">{q}</summary>'
        f'<p class="mt3">{a}</p></details>' for q, a in qa)
    return hero + sec(f'<div class="rows">{items}</div>')

# ===========================================================================
# INSIGHTS + NEWS
# ===========================================================================
INSIGHT_ARTICLES = {
    "governance-as-design": {
        "meta": bi("Field note", "บันทึกภาคสนาม"),
        "title": bi("Governance is a design material, not a checkpoint", "ธรรมาภิบาลคือวัสดุในการออกแบบ ไม่ใช่ด่านตรวจ"),
        "body_en": [
            "Most teams treat governance as the gate at the end: build the model, then ask whether it is safe, private, and allowed. By then the important decisions are already made and hard to undo.",
            "We teach the opposite. Evaluation, privacy, and the regulatory frame are materials you build with, present from the first design decision. When a fellow chooses a clinical problem, we ask how success will be measured and how failure will be caught before a single line of code is written.",
            "This is slower at the start and far faster overall. A tool designed to be evaluated is a tool that can be trusted, approved, and deployed. A tool that bolts evaluation on at the end usually cannot.",
        ],
        "body_th": [
            "ทีมส่วนใหญ่มองธรรมาภิบาลเป็นด่านสุดท้าย สร้างโมเดลก่อน แล้วค่อยถามว่ามันปลอดภัย เป็นส่วนตัว และได้รับอนุญาตหรือไม่ ถึงตอนนั้นการตัดสินใจสำคัญได้เกิดขึ้นแล้วและแก้ยาก",
            "เราสอนตรงกันข้าม การประเมินผล ความเป็นส่วนตัว และกรอบกฎระเบียบ เป็นวัสดุที่คุณใช้สร้างงาน อยู่ตั้งแต่การตัดสินใจออกแบบครั้งแรก เมื่อเฟลโลว์เลือกโจทย์คลินิก เราถามว่าจะวัดความสำเร็จอย่างไรและจะจับความล้มเหลวได้อย่างไร ก่อนที่จะเขียนโค้ดบรรทัดแรกด้วยซ้ำ",
            "วิธีนี้ช้ากว่าในช่วงเริ่มต้น แต่เร็วกว่ามากในภาพรวม เครื่องมือที่ออกแบบมาให้ประเมินได้ คือเครื่องมือที่ไว้ใจได้ อนุมัติได้ และนำไปใช้จริงได้ เครื่องมือที่แปะการประเมินไว้ท้ายสุดมักทำแบบนั้นไม่ได้",
        ],
    },
    "fhir-in-plain-language": {
        "meta": bi("Explainer", "อธิบายให้เข้าใจ"),
        "title": bi("FHIR, in plain language", "FHIR อธิบายแบบเข้าใจง่าย"),
        "body_en": [
            "If you want to build clinical AI in Thailand, you will meet FHIR quickly. It is the modern standard for how health data is described and exchanged, and it is the difference between a model that runs on one hospital's export and a model that travels.",
            "FHIR breaks health information into resources: a Patient, an Observation, a Condition, a Medication. Each has a defined shape, so a blood pressure reading from one system looks like a blood pressure reading from another. That sounds dull. It is the whole game. Interoperability is what lets a tool built at Ramathibodi work elsewhere.",
            "In the Academy you do not just read about FHIR. You parse it, build on it, and feel where real hospital data is messy in ways the spec does not warn you about.",
        ],
        "body_th": [
            "ถ้าคุณอยากสร้าง AI ทางคลินิกในไทย คุณจะเจอ FHIR อย่างรวดเร็ว มันคือมาตรฐานสมัยใหม่สำหรับการอธิบายและแลกเปลี่ยนข้อมูลสุขภาพ และเป็นตัวตัดสินว่าโมเดลของคุณจะรันได้แค่กับข้อมูลส่งออกของโรงพยาบาลเดียว หรือเดินทางไปที่อื่นได้ด้วย",
            "FHIR แบ่งข้อมูลสุขภาพออกเป็น resource ต่าง ๆ เช่น Patient, Observation, Condition, Medication แต่ละอย่างมีโครงสร้างที่กำหนดไว้ชัดเจน ค่าความดันโลหิตจากระบบหนึ่งจึงมีหน้าตาเหมือนค่าความดันโลหิตจากอีกระบบหนึ่ง ฟังดูน่าเบื่อ แต่นี่คือหัวใจทั้งหมด interoperability คือสิ่งที่ทำให้เครื่องมือที่สร้างที่รามาธิบดีไปทำงานที่อื่นได้",
            "ในอคาเดมี คุณไม่ได้แค่อ่านเรื่อง FHIR แต่คุณ parse มัน สร้างงานบนมัน และสัมผัสได้ว่าข้อมูลโรงพยาบาลจริงยุ่งเหยิงตรงไหนบ้างที่สเปกไม่ได้เตือนไว้",
        ],
    },
    "train-builders-not-buyers": {
        "meta": bi("Position", "จุดยืน"),
        "title": bi("Why Thailand should train builders, not just buyers", "ทำไมไทยควรฝึกคนที่สร้างเป็น ไม่ใช่แค่คนที่ซื้อเป็น"),
        "body_en": [
            "A country can get AI into its hospitals two ways. It can buy finished products from abroad, or it can grow people who build and run their own. Both have a place. Only one builds lasting capability.",
            "When you buy, you get a tool and a dependency. The vendor holds the knowledge, the updates, and the leverage. When the context shifts, and in medicine it always shifts, you wait. When you build, the capability stays in the institution and compounds.",
            "This is why we exist inside a hospital and not beside one. The national agenda, through the Ministry of Public Health, the NHSO, the Thai FDA, and the NIA, points the same way: a health system that can build for itself. That needs a workforce. Producing it is the work.",
        ],
        "body_th": [
            "ประเทศหนึ่งมีสองทางที่จะนำ AI เข้าสู่โรงพยาบาลของตน ซื้อผลิตภัณฑ์สำเร็จรูปจากต่างประเทศ หรือบ่มเพาะคนที่สร้างและดูแลของตัวเองได้ ทั้งสองทางมีที่ทางของมัน แต่มีเพียงทางเดียวที่สร้างขีดความสามารถที่ยั่งยืน",
            "เมื่อคุณซื้อ คุณได้เครื่องมือมาพร้อมกับการพึ่งพา ผู้ขายถือความรู้ การอัปเดต และอำนาจต่อรองไว้ทั้งหมด เมื่อบริบทเปลี่ยน และในทางการแพทย์มันเปลี่ยนเสมอ คุณต้องรอ เมื่อคุณสร้างเอง ขีดความสามารถนั้นอยู่ในสถาบันและเติบโตทบต้นไปเรื่อย ๆ",
            "นี่คือเหตุผลที่เราอยู่ภายในโรงพยาบาล ไม่ใช่อยู่ข้าง ๆ วาระระดับชาติ ไม่ว่าจะเป็นกระทรวงสาธารณสุข NHSO อย. หรือ NIA ต่างชี้ไปทางเดียวกัน ระบบสุขภาพที่สร้างเพื่อตัวเองได้ ต้องการกำลังคน การผลิตกำลังคนนั้นคืองานของเรา",
        ],
    },
}

def insights_index(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">{bi("Insights", "บทความ")}</span>
  <h1 class="reveal" data-d="1" style="max-width:18ch">{bi("Thinking from inside the work.", "ความคิดจากคนที่ลงมือทำ")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("Field notes, explainers, and positions on building medical AI that a health system can trust. Written by the people doing it.", "บันทึกภาคสนาม บทอธิบาย และจุดยืน ว่าด้วยการสร้าง AI การแพทย์ที่ระบบสุขภาพไว้ใจได้ เขียนโดยคนที่ลงมือทำจริง")}</p>
</div></section>"""
    cards = ""
    tone = ["b", "a", "c"]
    for i, (slug, art) in enumerate(INSIGHT_ARTICLES.items()):
        cards += entry(art["meta"], art["title"], "", prefix + f"insights/{slug}.html", tone[i % 3])
    feat = sec('<div class="grid grid-3">' + cards + '</div>')
    news = sec(
        head(bi("From the newsroom", "จากห้องข่าว"), bi("Announcements and milestones.", "ประกาศและก้าวสำคัญ")) +
        '<div class="rows">' +
        row(bi("News", "ข่าว"), bi("The club, in public", "ชมรม สู่สาธารณะ"), bi("Launches, cohorts, partnerships, and events as they happen.", "การเปิดตัว รุ่นเรียน พันธมิตร และกิจกรรม ตามเวลาจริง")) +
        '</div>' +
        f'<div class="btn-row mt4 reveal"><a class="btn btn--ghost" href="{prefix}news/index.html">{bi("All news", "ข่าวทั้งหมด")} {I["arrow"]}</a></div>')
    return hero + feat + news

def insight_article(slug):
    art = INSIGHT_ARTICLES[slug]
    meta, title = art["meta"], art["title"]
    paras = "".join(
        f'<p><span class="l-en">{en.strip()}</span><span class="l-th">{th.strip()}</span></p>'
        for en, th in zip(art["body_en"], art["body_th"]))
    def fn(prefix, ctx):
        I = ctx["ICON"]
        return f"""
<section class="section">
  <div class="container">
    <div class="crumb"><a href="{prefix}insights/index.html">{bi("Insights", "บทความ")}</a> / {meta}</div>
    <div style="max-width:70ch">
      <span class="eyebrow reveal">{meta}</span>
      <h1 class="reveal mt3" data-d="1">{title}</h1>
    </div>
    {frame(title, "ratio-16x9", "b")}
    <article class="prose reveal" style="margin-top:2.5rem">{paras}</article>
    <div class="btn-row" style="margin-top:3rem"><a class="btn btn--ghost" href="{prefix}insights/index.html">{I['arrow']} {bi("All insights", "บทความทั้งหมด")}</a></div>
  </div>
</section>"""
    return fn

def news_index(prefix, ctx):
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">{bi("News", "ข่าวสาร")}</span>
  <h1 class="reveal" data-d="1" style="max-width:16ch">{bi("What is happening at the club.", "ความเคลื่อนไหวของชมรม")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("Launches, cohorts, partnerships, and events. The record of a club finding its feet in public.", "การเปิดตัว รุ่นเรียน พันธมิตร และกิจกรรม บันทึกการเติบโตของชมรมสู่สาธารณะ")}</p>
</div></section>"""
    items = sec(
        '<div class="rows">' +
        news_row("July 2026", bi("The club goes public", "ชมรมเปิดตัวสู่สาธารณะ"), bi("The Ramathibodi Digital Health and AI Club launches its site, its Academy, and its first call for fellows.", "Ramathibodi Digital Health and AI Club เปิดตัวเว็บไซต์ อคาเดมี และประกาศรับสมัครเฟลโลว์รุ่นแรก")) +
        news_row(bi("Soon", "เร็ว ๆ นี้"), bi("First Academy cohort opens", "เปิดรับรุ่นแรกของอคาเดมี"), bi("Enrolment for the open curriculum opens to clinicians, students, and engineers across Thailand.", "เปิดลงทะเบียนหลักสูตรเปิด สำหรับบุคลากรทางการแพทย์ นักศึกษา และวิศวกรทั่วประเทศไทย")) +
        news_row(bi("Soon", "เร็ว ๆ นี้"), bi("Fellowship intake", "เปิดรับเฟลโลว์ชิป"), bi("Applications open for the first in-residence fellowship cohort.", "เปิดรับสมัครเฟลโลว์ชิปรุ่นแรกแบบประจำในสถานที่")) +
        '</div>')
    return hero + items

def news_row(date, title, body):
    return (f'<div class="row reveal"><div class="row__num">{date}</div>'
            f'<h3>{title}</h3><p>{body}</p></div>')

# ===========================================================================
# CAREERS
# ===========================================================================
def careers(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">{bi("Careers", "ร่วมงานกับเรา")}</span>
  <h1 class="reveal" data-d="1" style="max-width:18ch">{bi("Help build the workforce that builds the future of care.", "มาร่วมสร้างกำลังคนที่จะสร้างอนาคตของการดูแลสุขภาพ")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("We are assembling a small team of clinicians, engineers, scientists, and operators who want their work measured in patients helped, not slides shipped.", "เรากำลังรวมทีมเล็กๆ ของแพทย์ วิศวกร นักวิทยาศาสตร์ และคนปฏิบัติการ ที่อยากให้งานของตนวัดด้วยจำนวนผู้ป่วยที่ได้รับการช่วยเหลือ ไม่ใช่จำนวนสไลด์ที่ส่ง")}</p>
  <div class="btn-row reveal" data-d="3"><a class="btn btn--grad btn--lg" href="{prefix}contact.html">{bi("Introduce yourself", "แนะนำตัวกับเรา")} {I['arrow']}</a></div>
</div></section>"""
    roles = sec(
        head(bi("Open directions", "ทิศทางที่เปิดรับ"), bi("We hire for trajectory. If you fit one of these, write to us.", "เรารับคนที่มีแนวโน้มเติบโต หากคุณเข้ากับข้อใดข้อหนึ่ง เขียนมาหาเรา")) +
        '<div class="rows">' +
        row(bi("Faculty / Clinical", "อาจารย์ / คลินิก"), bi("Clinical leads and mentors", "หัวหน้าคลินิกและเมนเทอร์"), bi("Attending physicians who want to teach, supervise fellows, and shape real projects.", "แพทย์ประจำที่อยากสอน กำกับเฟลโลว์ และกำหนดทิศทางโปรเจกต์จริง")) +
        row(bi("Engineering", "วิศวกรรม"), bi("ML and platform engineers", "วิศวกร ML และแพลตฟอร์ม"), bi("People who can build reliable, evaluated clinical tools and the platform under them.", "คนที่สร้างเครื่องมือคลินิกที่เชื่อถือได้และผ่านการประเมิน พร้อมแพลตฟอร์มที่รองรับ")) +
        row(bi("Curriculum", "หลักสูตร"), bi("Educators and content leads", "นักการศึกษาและหัวหน้าเนื้อหา"), bi("Builders who can teach, turning real practice into Academy material and notebooks.", "ผู้สร้างที่สอนได้ เปลี่ยนการปฏิบัติจริงให้เป็นเนื้อหาอคาเดมีและ notebook")) +
        row(bi("Operations", "ปฏิบัติการ"), bi("Programme and partnerships", "โปรแกรมและพันธมิตร"), bi("Operators who can run cohorts, manage partners, and keep the machine moving.", "คนปฏิบัติการที่ดูแลรุ่น จัดการพันธมิตร และทำให้ทุกอย่างเดินหน้า")) +
        '</div>')
    why = sec(
        head(bi("Why join", "ทำไมต้องมาร่วม"), bi("What you get that you cannot get elsewhere.", "สิ่งที่คุณได้ที่หาจากที่อื่นไม่ได้")) +
        '<div class="grid grid-3">' +
        ctx['card']('pulse', bi('Real stakes', 'เดิมพันจริง'), bi('Work that reaches patients, inside a leading medical school, not a sandbox.', 'งานที่ไปถึงผู้ป่วย ภายในโรงเรียนแพทย์ชั้นนำ ไม่ใช่แค่ sandbox'), None, '', prefix) +
        ctx['card']('users', bi('Rare room', 'ห้องที่หายาก'), bi('Clinicians and engineers building together, every day, on the same problems.', 'แพทย์และวิศวกรสร้างงานด้วยกันทุกวัน บนโจทย์เดียวกัน'), None, '', prefix) +
        ctx['card']('compass', bi('Build a field', 'สร้างวงการ'), bi('Help define how Thailand trains its medical AI workforce, from the start.', 'ร่วมกำหนดว่าประเทศไทยจะฝึกกำลังคน AI การแพทย์อย่างไร ตั้งแต่เริ่มต้น'), None, '', prefix) +
        '</div>')
    return hero + roles + why

# ===========================================================================
# CONTACT
# ===========================================================================
def contact(prefix, ctx):
    I = ctx["ICON"]
    body = f"""
<section class="section">
  <div class="container">
    <div class="split">
      <div class="stack reveal">
        <span class="eyebrow">{bi("Contact", "ติดต่อ")}</span>
        <h1 style="font-size:var(--step-4)">{bi("Let us talk.", "มาคุยกัน")}</h1>
        <p class="lead measure">{bi("Whether you want to learn, apply, partner, or hire us to build capability, this is the door. Tell us who you are and what you want to do.", "ไม่ว่าคุณอยากเรียน สมัคร เป็นพันธมิตร หรือจ้างเราสร้างขีดความสามารถ นี่คือประตู บอกเราว่าคุณเป็นใครและอยากทำอะไร")}</p>
        <div class="rows" style="border-top:1px solid var(--line);margin-top:1rem">
          <div class="row" style="grid-template-columns:1fr"><div><div class="step__k">{bi("Apply", "สมัคร")}</div><p class="mt2">{bi("Academy and Fellowship enquiries", "สอบถามอคาเดมีและเฟลโลว์ชิป")}</p></div></div>
          <div class="row" style="grid-template-columns:1fr"><div><div class="step__k">{bi("Partner", "พันธมิตร")}</div><p class="mt2">{bi("Hospitals, agencies, and health technology companies", "โรงพยาบาล หน่วยงาน และบริษัทเทคโนโลยีสุขภาพ")}</p></div></div>
          <div class="row" style="grid-template-columns:1fr"><div><div class="step__k">{bi("Where", "ที่ตั้ง")}</div><p class="mt2">{ctx['SITE']['org_en']}<br/>{ctx['SITE']['org_th']}</p></div></div>
        </div>
      </div>
      <div class="card card--feature reveal" data-d="1">
        <h3>{bi("Send a message", "ส่งข้อความ")}</h3>
        <form onsubmit="event.preventDefault();this.querySelector('.gate__msg').textContent=(document.documentElement.getAttribute('data-lang')==='th'?'ขอบคุณครับ นี่คือฟอร์มสาธิต เชื่อมต่ออีเมลหรือบริการฟอร์มก่อนเปิดใช้จริง':'Thank you. This is a static demo form. Wire it to your inbox or a form service before launch.');">
          <div class="field"><label>{bi("Name", "ชื่อ")}</label><input type="text" required {ph('Your name', 'ชื่อของคุณ')}/></div>
          <div class="field"><label>{bi("Email", "อีเมล")}</label><input type="email" required placeholder="you@hospital.org"/></div>
          <div class="field"><label>{bi("I want to", "ฉันต้องการ")}</label><input type="text" {ph('learn / apply / partner / hire', 'เรียน / สมัคร / เป็นพันธมิตร / จ้าง')}/></div>
          <div class="field"><label>{bi("Message", "ข้อความ")}</label><input type="text" {ph('A sentence about what you have in mind', 'ประโยคเดียวเกี่ยวกับสิ่งที่คุณคิดไว้')}/></div>
          <div class="gate__msg" style="color:var(--accent)"></div>
          <div class="btn-row mt3"><button class="btn btn--grad btn--lg" type="submit">{bi("Send", "ส่ง")} {I['arrow']}</button></div>
        </form>
      </div>
    </div>
  </div>
</section>"""
    return body

def platform_ecosystem(prefix):
    """Fourth signature sketch: the platform as a hub and spoke, distinct in
    shape from the clinical path (hospital-flow), the hiking trail (Academy),
    and the closed loop (Fellowship orbit). A builder at the centre, six
    stations around it, each a two-way street: you draw from it, you feed it
    back."""
    import math
    cx, cy, r = 300, 200, 148
    stations = [
        ("Datasets", "ชุดข้อมูล", "Learn from real, governed data", "เรียนรู้จากข้อมูลจริงที่กำกับดูแล"),
        ("Task board", "กระดานโจทย์", "Pick up a real clinical problem", "รับโจทย์คลินิกจริงไปทำ"),
        ("Showcase", "โชว์เคส", "Show what you built, honestly scored", "แสดงผลงาน วัดผลตรงไปตรงมา"),
        ("Matching", "จับคู่", "Find a mentor, a team, a partner", "หาเมนเทอร์ ทีม หรือพันธมิตร"),
        ("Job board", "กระดานงาน", "Turn a project into a role", "เปลี่ยนโปรเจกต์เป็นตำแหน่งงาน"),
        ("Academy & Fellowship", "อคาเดมีและเฟลโลว์ชิป", "Where the skill to use all this comes from", "ที่มาของทักษะที่ใช้สิ่งเหล่านี้"),
    ]
    def pt(i, n):
        a = -math.pi/2 + i * (2*math.pi/n)
        return (cx + r*math.cos(a), cy + r*math.sin(a))
    nodes, spokes = "", ""
    n = len(stations)
    for i, (lab_en, lab_th, cap_en, cap_th) in enumerate(stations):
        x, y = pt(i, n)
        anchor = "middle"
        xoff, yoff = 0, (-30 if y < cy - 20 else (46 if y > cy + 20 else 0))
        if abs(y - cy) <= 20:
            anchor = "start" if x > cx else "end"
            xoff = 18 if x > cx else -18
        lx, ly, cyoff = x + xoff, y + yoff, y + yoff + 16
        spokes += f'<line class="pe-spoke" x1="{cx:.0f}" y1="{cy:.0f}" x2="{x:.0f}" y2="{y:.0f}"/>'
        nodes += (f'<circle class="pe-node" cx="{x:.0f}" cy="{y:.0f}" r="10"/>'
                  f'<text class="l-en pe-lab" x="{lx:.0f}" y="{ly:.0f}" text-anchor="{anchor}">{lab_en}</text>'
                  f'<text class="l-th pe-lab" x="{lx:.0f}" y="{ly:.0f}" text-anchor="{anchor}">{lab_th}</text>'
                  f'<text class="l-en pe-cap" x="{lx:.0f}" y="{cyoff:.0f}" text-anchor="{anchor}">{cap_en}</text>'
                  f'<text class="l-th pe-cap" x="{lx:.0f}" y="{cyoff:.0f}" text-anchor="{anchor}">{cap_th}</text>')
    svg = f"""
<div class="flow-art reveal">
  <svg viewBox="0 0 600 400" role="img" aria-label="The Platform, as a hub with six stations" preserveAspectRatio="xMidYMid meet">
    <defs>
      <filter id="sketch4" x="-8%" y="-8%" width="116%" height="116%">
        <feTurbulence type="fractalNoise" baseFrequency="0.015" numOctaves="2" seed="23" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="3.3"/>
      </filter>
      <radialGradient id="pe-grad" cx="50%" cy="50%" r="60%">
        <stop offset="0" stop-color="#fd6502"/><stop offset="0.55" stop-color="#91386e"/><stop offset="1" stop-color="#2a1bd6"/>
      </radialGradient>
    </defs>
    <g filter="url(#sketch4)" fill="none">
      {spokes}
    </g>
    <g filter="url(#sketch4)">
      {nodes}
    </g>
    <circle cx="{cx}" cy="{cy}" r="17" fill="url(#pe-grad)"/>
    <text class="pe-center l-en" x="{cx}" y="{cy+4}" text-anchor="middle">You</text>
    <text class="pe-center l-th" x="{cx}" y="{cy+4}" text-anchor="middle">คุณ</text>
    <text class="fa-hand" x="30" y="40" transform="rotate(-3 30 40)">one builder, six doors</text>
    <path class="fa-hand-arrow" d="M70 50 q 10 20 -4 40"/>
  </svg>
  <div class="flow-art__legend">
    <span class="l-en">Not six separate products. Six doors into the same platform, and you can walk through more than one at a time.</span>
    <span class="l-th">ไม่ใช่หกผลิตภัณฑ์ที่แยกกัน แต่เป็นหกประตูสู่แพลตฟอร์มเดียวกัน และคุณเดินผ่านได้มากกว่าหนึ่งประตูพร้อมกัน</span>
  </div>
</div>"""
    return (f'<section class="section"><div class="container">'
            f'{head(bi("The ecosystem", "ระบบนิเวศ"), bi("One platform, six stations, one builder in the middle.", "หนึ่งแพลตฟอร์ม หกสถานี หนึ่งผู้สร้างตรงกลาง"), bi("Data feeds problems. Problems become projects. Projects find mentors, teams, and jobs. It is one loop you move through more than once.", "ข้อมูลป้อนโจทย์ โจทย์กลายเป็นโปรเจกต์ โปรเจกต์พาไปเจอเมนเทอร์ ทีม และงาน มันคือวงเดียวที่คุณเดินผ่านได้มากกว่าหนึ่งรอบ"))}'
            f'{svg}</div></section>')

def public_datasets(prefix):
    rows = [
        ("Open", bi("NIH ChestX-ray14", "NIH ChestX-ray14"), bi("112,000 chest X-rays with disease labels, from the NIH Clinical Center. No registration needed.", "ภาพเอกซเรย์ทรวงอก 112,000 ภาพพร้อมป้ายกำกับโรค จาก NIH Clinical Center ไม่ต้องลงทะเบียน")),
        ("Open", bi("CheXpert", "CheXpert"), bi("224,000 chest radiographs from Stanford, free with a short registration.", "ภาพรังสีทรวงอก 224,000 ภาพจาก Stanford ใช้ฟรีเพียงลงทะเบียนสั้น ๆ")),
        ("Credentialed", bi("MIMIC-IV", "MIMIC-IV"), bi("De-identified ICU records from Beth Israel Deaconess. Requires PhysioNet credentialing and a short ethics course, worth doing once.", "เวชระเบียน ICU ที่ลบตัวตนแล้ว จาก Beth Israel Deaconess ต้องผ่านการรับรองจาก PhysioNet และคอร์สจริยธรรมสั้น ๆ คุ้มค่าที่จะทำครั้งหนึ่ง")),
        ("Credentialed", bi("eICU Collaborative Research Database", "eICU Collaborative Research Database"), bi("Multi-centre ICU data from over 200 US hospitals, same PhysioNet credentialing as MIMIC.", "ข้อมูล ICU จากกว่า 200 โรงพยาบาลในสหรัฐฯ ใช้การรับรองแบบเดียวกับ MIMIC")),
        ("Open", bi("PhysioNet Challenge datasets", "PhysioNet Challenge datasets"), bi("ECG and other waveform datasets released for open research challenges.", "ชุดข้อมูล ECG และสัญญาณอื่น ๆ ที่เปิดเผยสำหรับการแข่งขันวิจัยแบบเปิด")),
        ("Aggregate", bi("Ministry of Public Health open data (data.go.th)", "ข้อมูลเปิดกระทรวงสาธารณสุข (data.go.th)"), bi("Thailand's own open government health statistics: disease surveillance, facility data, and more, at the population level.", "สถิติสุขภาพเปิดของรัฐบาลไทยเอง ทั้งการเฝ้าระวังโรค ข้อมูลสถานพยาบาล และอื่น ๆ ในระดับประชากร")),
        ("Open", bi("Thai language corpora (VISTEC-AIResearch)", "คลังข้อมูลภาษาไทย (VISTEC-AIResearch)"), bi("Open Thai text corpora used to train Thai language models, a starting point for Thai clinical NLP work.", "คลังข้อความภาษาไทยแบบเปิดที่ใช้ฝึกโมเดลภาษาไทย จุดเริ่มต้นสำหรับงาน NLP คลินิกภาษาไทย")),
    ]
    trs = "".join(
        f'<tr><td><span class="pill" style="font-size:.72rem">{status}</span></td><td><strong>{name}</strong></td><td>{desc}</td></tr>'
        for status, name, desc in rows)
    return f"""
<section class="section">
  <div class="container">
    {head(bi("Public datasets to start on today", "ชุดข้อมูลสาธารณะที่เริ่มได้วันนี้"), bi("You do not need to wait for access to begin.", "ไม่ต้องรอสิทธิ์เข้าถึงก็เริ่มได้"), bi("Real, widely used datasets the global and Thai research community already works on. Some are open immediately, some need a short, free credentialing step. None require you to touch a real patient's record before you are ready.", "ชุดข้อมูลจริงที่ชุมชนวิจัยทั้งไทยและทั่วโลกใช้กันอยู่แล้ว บางชุดเปิดใช้ได้ทันที บางชุดต้องผ่านขั้นตอนรับรองสั้น ๆ ฟรี ไม่มีชุดไหนที่ต้องแตะเวชระเบียนผู้ป่วยจริงก่อนที่คุณจะพร้อม"))}
    <div class="card reveal" style="padding:0;overflow-x:auto">
      <table class="lb" style="min-width:640px">
        <thead><tr><th>{bi("Access", "การเข้าถึง")}</th><th>{bi("Dataset", "ชุดข้อมูล")}</th><th>{bi("What it is", "คืออะไร")}</th></tr></thead>
        <tbody>{trs}</tbody>
      </table>
    </div>
    <p class="muted mt4 reveal" style="font-size:.85rem">{bi("This list sits alongside the club's own governed, Thai clinical datasets above. Start on the open ones in the Academy, move to credentialed access as your project grows.", "รายการนี้อยู่ควบคู่กับชุดข้อมูลคลินิกไทยของชมรมเองด้านบน เริ่มจากชุดข้อมูลเปิดในอคาเดมี แล้วขยับไปสู่การเข้าถึงแบบมีการรับรองเมื่อโปรเจกต์ของคุณโตขึ้น")}</p>
  </div>
</section>"""

# ===========================================================================
# PLATFORM / MARKETPLACE
# ===========================================================================
def platform(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  {note_hand("where work finds people", "ที่ที่งานเจอคน")}
  <span class="eyebrow reveal">{bi("The Platform", "แพลตฟอร์ม")}</span>
  <h1 class="reveal" data-d="1" style="max-width:18ch">{bi("Where problems, data, and people find each other.", "ที่ที่โจทย์ ข้อมูล และคนมาเจอกัน")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("Problems, data, and people, in one place. The connective tissue of the club.", "โจทย์ ข้อมูล และคน อยู่ในที่เดียว นี่คือเนื้อเยื่อที่เชื่อมคลับเข้าด้วยกัน")}</p>
</div></section>"""

    tiles = sec(
        '<div class="grid grid-4">' +
        ctx['card']('doc', bi('Dataset marketplace', 'ตลาดชุดข้อมูล'), bi('Governed, de-identified datasets to learn and build on.', 'ชุดข้อมูลที่กำกับดูแลและลบตัวตนแล้ว สำหรับเรียนรู้และสร้างงาน'), None, '', prefix) +
        ctx['card']('flask', bi('Task board', 'กระดานโจทย์'), bi('Real clinical problems posted by departments, waiting for a builder.', 'โจทย์จริงจากคลินิกที่หน่วยงานโพสต์ไว้ รอคนมาลงมือทำ'), None, '', prefix) +
        ctx['card']('pulse', bi('Work showcase', 'โชว์เคสผลงาน'), bi('Display your model or project. Let the right people find and contact you.', 'แสดงโมเดลหรือโปรเจกต์ของคุณ ให้คนที่ใช่เจอและติดต่อคุณ'), None, '', prefix) +
        ctx['card']('users', bi('Matching', 'จับคู่'), bi('Match people to teams, mentors, and problems.', 'จับคู่คนเข้ากับทีม เมนเทอร์ และโจทย์'), None, '', prefix) +
        '</div>')

    # Dataset marketplace (data.gov.sg-inspired: coloured icon chip + stat card grid)
    datasets = f"""
<section class="section">
  <div class="container">
    {head(bi("Dataset marketplace", "ตลาดชุดข้อมูล"), bi("Data you can actually learn on.", "ข้อมูลที่คุณเรียนรู้ได้จริง"), bi("Governed and de-identified. You never touch raw patient data without supervision.", "กำกับดูแลและลบตัวตนแล้ว คุณจะไม่แตะข้อมูลผู้ป่วยดิบโดยไม่มีการกำกับ"))}
    <div class="ds-panel reveal">
      <div class="ds-grid">
        {ds_card("teal", I["doc"], "Thai Clinical Tabular", "Tabular", "Open", "12 fields / n=4,200", prefix)}
        {ds_card("coral", I["pulse"], "Chest X-ray teaching set", "Image", "Open", "9,100 films", prefix)}
        {ds_card("purple", I["brain"], "Thai Clinical Notes", "Text / synthetic", "Open", "12k notes", prefix)}
        {ds_card("blue", I["pulse"], "ECG Rhythm Strips", "Signal", "On request", "3,400 strips", prefix)}
      </div>
    </div>
    <p class="muted mt4 reveal" style="font-size:.88rem">{bi("Every dataset lists its source, its licence, and the lawful basis for use. Access to sensitive sets is supervised.", "ทุกชุดข้อมูลระบุแหล่งที่มา สัญญาอนุญาต และฐานทางกฎหมายในการใช้งาน การเข้าถึงข้อมูลอ่อนไหวจะมีการกำกับดูแล")}</p>
  </div>
</section>"""

    # Task board
    tasks = sec(
        head(bi("Task board", "กระดานโจทย์"), bi("Real problems, waiting for you.", "โจทย์จริง ที่รอคุณอยู่"), bi("Departments post problems worth solving. Pick one, form a team, and build it as an Academy project or a Fellowship.", "หน่วยงานโพสต์โจทย์ที่ควรแก้ เลือกสักโจทย์ ตั้งทีม แล้วสร้างเป็นโปรเจกต์ในอคาเดมีหรือเฟลโลว์ชิป")) +
        '<div class="grid grid-2">' +
        task_card('pulse', bi("Emergency", "ฉุกเฉิน"), bi("Triage support for the ED", "ระบบช่วยคัดกรองที่ห้องฉุกเฉิน"), bi("Reduce time to prioritise walk-in patients safely.", "ลดเวลาในการจัดลำดับผู้ป่วยที่เดินเข้ามาอย่างปลอดภัย"), ctx, 1) +
        task_card('doc', bi("Radiology", "รังสีวิทยา"), bi("Flag urgent chest films", "ตั้งค่าสถานะฟิล์มทรวงอกเร่งด่วน"), bi("Surface likely-abnormal chest X-rays for faster reads.", "ดึงภาพเอกซเรย์ทรวงอกที่น่าจะผิดปกติขึ้นมา เพื่อการอ่านที่เร็วขึ้น"), ctx, 2) +
        task_card('flask', bi("Pharmacy", "เภสัชกรรม"), bi("Thai drug interaction assistant", "ผู้ช่วยตรวจปฏิกิริยาระหว่างยาภาษาไทย"), bi("A grounded assistant to check interactions on the ward.", "ผู้ช่วยที่อ้างอิงแหล่งข้อมูล ตรวจปฏิกิริยาระหว่างยาบนหอผู้ป่วย"), ctx, 1) +
        task_card('node', bi("Outpatient", "ผู้ป่วยนอก"), bi("Line follow-up bot", "บอทติดตามอาการผ่าน Line"), bi("Automate preparation and follow-up messages safely.", "ส่งข้อความเตรียมตัวและติดตามอาการอัตโนมัติอย่างปลอดภัย"), ctx, 2) +
        '</div>' +
        f'<div class="btn-row mt5 reveal"><a class="btn btn--grad" href="{prefix}contact.html">{bi("Post a problem", "โพสต์โจทย์ของคุณ")} {I["arrow"]}</a><a class="btn btn--ghost" href="{prefix}academy.html">{bi("Pick one up", "รับโจทย์ไปทำ")}</a></div>')

    # Showcase marketplace (display work, let interested people reach out)
    lb = f"""
<section class="section">
  <div class="container">
    {head(bi("Work showcase", "โชว์เคสผลงาน"), bi("Display your work. Let the right people find you.", "แสดงผลงาน ให้คนที่ใช่มาเจอคุณ"), bi("A marketplace for what members build. Post your model or project with honest metrics, and hospitals, partners, and mentors can reach out. Metrics are shown with their denominator, because trust is the point.", "ตลาดสำหรับสิ่งที่สมาชิกสร้าง โพสต์โมเดลหรือโปรเจกต์พร้อมตัวเลขที่ตรงไปตรงมา แล้วโรงพยาบาล พันธมิตร และเมนเทอร์ติดต่อเข้ามาได้ ตัวเลขแสดงพร้อมตัวหารเสมอ เพราะความเชื่อใจคือหัวใจ"))}
    <div class="grid grid-3">
      {show_card(I, bi("Sepsis early warning", "ระบบเตือนภาวะติดเชื้อในกระแสเลือด"), "Ward 7", "AUROC 0.86", bi("n=4,200 admissions", "n=4,200 การรับตัว"), bi("Deployed pilot", "นำร่องแล้ว"), prefix)}
      {show_card(I, bi("Chest X-ray triage", "คัดกรองภาพเอกซเรย์ทรวงอก"), "RadLab", "AUROC 0.83", bi("n=9,100 films", "n=9,100 ฟิล์ม"), bi("Seeking partner", "หาพันธมิตร"), prefix)}
      {show_card(I, bi("Thai clinical coding", "การให้รหัสเวชระเบียนภาษาไทย"), "NoteAI", "F1 0.81", bi("n=12k notes", "n=12k เวชระเบียน"), bi("Open to hire", "พร้อมรับงาน"), prefix)}
    </div>
    <p class="muted mt4 reveal" style="font-size:.82rem">{bi("Illustrative entries. The live showcase opens with the first cohort. A private leaderboard still ranks shared tasks by calibration and fairness for members.", "ผลงานตัวอย่าง โชว์เคสจริงจะเปิดพร้อมรุ่นแรก ยังมีลีดเดอร์บอร์ดภายในที่จัดอันดับโจทย์กลางด้วย calibration และความเป็นธรรมสำหรับสมาชิก")}</p>
    <div class="btn-row mt5 reveal"><a class="btn btn--grad" href="{prefix}contact.html">{bi("Show your work", "แสดงผลงานของคุณ")} {I["arrow"]}</a></div>
  </div>
</section>"""

    # Matching
    matching = f"""
<section class="section">
  <div class="container">
    <div class="band reveal"><div class="band__glow"></div>
      <div class="container" style="padding-block:clamp(3rem,6vw,5rem)">
        <span class="eyebrow" style="color:#cbd5ef">{bi("Partner and team matching", "จับคู่ทีมและพันธมิตร")}</span>
        <h2 class="mt3">{bi("The right people around the right problem.", "คนที่ใช่ รอบโจทย์ที่ใช่")}</h2>
        <div class="grid grid-3 mt5">
          <div><div class="stat__num" style="color:#fff">{bi("Mentor match", "จับคู่เมนเทอร์")}</div><p style="color:#9fb0d4" class="mt2">{bi("Pair with a clinician and an engineer who fit your problem.", "จับคู่กับแพทย์และวิศวกรที่เหมาะกับโจทย์ของคุณ")}</p></div>
          <div><div class="stat__num" style="color:#fff">{bi("Team match", "จับคู่ทีม")}</div><p style="color:#9fb0d4" class="mt2">{bi("Find teammates with the skills yours is missing.", "หาเพื่อนร่วมทีมที่มีทักษะที่ทีมคุณยังขาด")}</p></div>
          <div><div class="stat__num" style="color:#fff">{bi("Partner match", "จับคู่พันธมิตร")}</div><p style="color:#9fb0d4" class="mt2">{bi("Connect a hospital or company to a team that can build.", "เชื่อมโรงพยาบาลหรือบริษัทเข้ากับทีมที่สร้างได้จริง")}</p></div>
        </div>
        <div class="btn-row" style="margin-top:2rem"><a class="btn btn--grad" href="{prefix}contact.html">{bi("Get matched", "ขอจับคู่")} {I['arrow']}</a></div>
      </div>
    </div>
  </div>
</section>"""

    # Job board (canvas / kanban)
    jobs = f"""
<section class="section"><div class="container">
  {head(bi("Job board", "กระดานงาน"), bi("Post a role. Find the people who build.", "ประกาศงาน หาคนที่ลงมือสร้าง"), bi("A recruiting board for the club and its partners. Post a fellowship, a research assistant role, an internship, or a job, and reach members who can actually build. Browse the lanes below.", "กระดานรับสมัครสำหรับชมรมและพันธมิตร ประกาศเฟลโลว์ชิป ผู้ช่วยวิจัย ฝึกงาน หรือตำแหน่งงาน แล้วเข้าถึงสมาชิกที่สร้างได้จริง เลื่อนดูตามเลนด้านล่าง"))}
  <div class="board reveal" role="list" aria-label="Job board">
    {board_lane(I, "grad", bi("Fellowship", "เฟลโลว์ชิป"), 2, [
        board_card("open", bi("Digital Health & AI Fellow", "เฟลโลว์สุขภาพดิจิทัลและ AI"), bi("The in-residence programme. Build one real system to the bedside.", "โปรแกรมในสถานที่ สร้างระบบจริงหนึ่งชิ้นให้ถึงข้างเตียง"), bi("Rolling", "รับต่อเนื่อง"), bi("12 months", "12 เดือน"), prefix + "fellowship/apply.html"),
        board_card("open", bi("Clinician Fellow (part-time)", "เฟลโลว์แพทย์ (พาร์ทไทม์)"), bi("For practising clinicians who want to build alongside their service.", "สำหรับแพทย์ที่ยังทำงานคลินิกและอยากสร้างงานควบคู่กัน"), bi("Rolling", "รับต่อเนื่อง"), bi("Flexible", "ยืดหยุ่น"), prefix + "fellowship/apply.html"),
    ])}
    {board_lane(I, "orange", bi("Research", "วิจัย"), 2, [
        board_card("open", bi("Research assistant, clinical AI", "ผู้ช่วยวิจัย AI ทางคลินิก"), bi("Support live projects with data curation and honest evaluation.", "สนับสนุนโปรเจกต์จริงด้านการจัดการข้อมูลและการประเมินผลอย่างตรงไปตรงมา"), bi("Open", "เปิดรับ"), bi("Ramathibodi", "รามาธิบดี"), prefix + "careers.html"),
        board_card("soon", bi("Data engineer, FHIR pipelines", "วิศวกรข้อมูล FHIR"), bi("Build the de-identified data pipelines the platform runs on.", "สร้างไปป์ไลน์ข้อมูลที่ลบตัวตนแล้วซึ่งเป็นฐานของแพลตฟอร์ม"), bi("Soon", "เร็ว ๆ นี้"), bi("Ramathibodi", "รามาธิบดี"), prefix + "careers.html"),
    ])}
    {board_lane(I, "indigo", bi("Internship", "ฝึกงาน"), 1, [
        board_card("open", bi("Student builder internship", "ฝึกงานนักศึกษาผู้สร้าง"), bi("A term inside a real project team, from problem to prototype.", "หนึ่งเทอมในทีมโปรเจกต์จริง ตั้งแต่โจทย์จนถึงต้นแบบ"), bi("Cohort", "ตามรุ่น"), bi("3 months", "3 เดือน"), prefix + "academy.html"),
    ])}
    {board_lane(I, "purple", bi("Partner roles", "ตำแหน่งจากพันธมิตร"), 2, [
        board_card("partner", bi("Roles from GDG & BOTNOI", "ตำแหน่งจาก GDG และ BOTNOI"), bi("Engineering and product openings shared by our partner network.", "ตำแหน่งวิศวกรรมและโปรดักต์จากเครือข่ายพันธมิตรของเรา"), bi("Partner", "พันธมิตร"), bi("Thai HealthTech", "เฮลท์เทคไทย"), prefix + "careers.html"),
        board_card("partner", bi("Hospital innovation roles", "ตำแหน่งนวัตกรรมโรงพยาบาล"), bi("Openings from hospitals standing up their own AI teams.", "ตำแหน่งจากโรงพยาบาลที่กำลังตั้งทีม AI ของตนเอง"), bi("Partner", "พันธมิตร"), bi("Network", "เครือข่าย"), prefix + "careers.html"),
    ])}
  </div>
  <p class="muted mt4 reveal" style="font-size:.82rem">{bi("Illustrative board. Live postings open with the first cohort. Partners can list a role from Contact.", "บอร์ดตัวอย่าง ตำแหน่งจริงจะเปิดพร้อมรุ่นแรก พันธมิตรลงประกาศได้จากหน้าติดต่อ")}</p>
  <div class="btn-row mt5 reveal"><a class="btn btn--grad" href="{prefix}contact.html">{bi("List a role", "ลงประกาศตำแหน่ง")} {I["arrow"]}</a><a class="btn btn--ghost" href="{prefix}careers.html">{bi("See careers", "ดูตำแหน่งงาน")} {I["arrow"]}</a></div>
</div></section>"""

    # Tools strip
    engine = sec(
        head(bi("What powers it", "สิ่งที่ขับเคลื่อน"), bi("A toolkit underneath.", "ชุดเครื่องมือที่อยู่เบื้องหลัง")) +
        '<div class="grid grid-2">' +
        ctx['card']('flask', bi('Tools', 'เครื่องมือ'), bi('De-identification, a grounded Thai guideline assistant, model report cards, and the Learning Navigator.', 'เครื่องมือลบตัวตน ผู้ช่วยแนวเวชปฏิบัติไทยแบบอ้างอิง รายงานผลโมเดล และเนวิเกเตอร์การเรียนรู้'), "tools.html", bi("Open the toolkit", "เปิดชุดเครื่องมือ"), prefix) +
        ctx['card']('shield', bi('Governed data', 'ข้อมูลที่กำกับดูแล'), bi('Every dataset ships with its source, licence, and a lawful basis under the PDPA.', 'ทุกชุดข้อมูลมาพร้อมแหล่งที่มา สัญญาอนุญาต และฐานทางกฎหมายตาม PDPA'), None, '', prefix) +
        '</div>')

    return (hero + tiles + platform_ecosystem(prefix)
            + moment("network-people.jpg", prefix, bi("One community, many problems", "หนึ่งชุมชน หลายโจทย์"))
            + datasets + public_datasets(prefix) + tasks + lb + matching + engine + jobs)

def ds_card(tone, icon, title, kind, status, stat, prefix=""):
    """data.gov.sg-style dataset card: coloured icon chip, bold title, mono stat line."""
    return (f'<a class="ds-card ds-card--{tone}" href="{prefix}contact.html">'
            f'<span class="ds-card__ic">{icon}</span>'
            f'<span class="ds-card__title">{title}</span>'
            f'<span class="ds-card__stat">{kind} / {status} / {stat}</span></a>')

def task_card(icon, dept, title, desc, ctx, d=0):
    dd = f' data-d="{d}"' if d else ""
    return f"""<div class="card reveal"{dd}>
  <div class="card__icon">{ctx['ICON'][icon]}</div>
  <span class="pill" style="margin-bottom:.7rem">{dept}</span>
  <h3>{title}</h3><p>{desc}</p>
</div>"""

def task_row(tag, title, desc):
    return (f'<div class="row reveal"><div class="row__num">{tag}</div>'
            f'<h3 style="font-size:var(--step-1)">{title}</h3><p style="font-size:.95rem">{desc}</p></div>')

def board_card(state, title, desc, badge, meta, href):
    """A sticky-note style card on the opportunity canvas. state in {open,soon,partner}."""
    dot = {"open": bi("Open", "เปิดรับ"), "soon": bi("Soon", "เร็ว ๆ นี้"), "partner": bi("Partner", "พันธมิตร")}.get(state, badge)
    go = ("" if state == "soon" else
          f'<span class="bcard__go">{bi("View", "ดู")} <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>')
    tag = f'<a class="bcard" href="{href}">' if state != "soon" else '<div class="bcard bcard--soon">'
    end = '</a>' if state != "soon" else '</div>'
    return (f'{tag}<div class="bcard__top"><span class="bcard__state bcard__state--{state}">{dot}</span>'
            f'<span class="bcard__meta">{meta}</span></div>'
            f'<h4 class="bcard__title">{title}</h4><p class="bcard__desc">{desc}</p>'
            f'<div class="bcard__foot"><span class="bcard__badge">{badge}</span>{go}</div>{end}')

def show_card(I, title, author, metric, denom, status, prefix):
    """A showcase-marketplace card: a member's work, with a way to reach them."""
    return (f'<div class="show reveal"><div class="show__top">'
            f'<span class="show__status">{status}</span><span class="show__metric">{metric}</span></div>'
            f'<h3 class="show__title">{title}</h3>'
            f'<div class="show__by">{bi("by", "โดย")} <strong>{author}</strong> / {denom}</div>'
            f'<a class="show__contact" href="{prefix}contact.html">{bi("Get in touch", "ติดต่อ")} {I["arrow"]}</a></div>')

def board_lane(I, tone, title, count, cards):
    n = f'<span class="lane__count">{count}</span>'
    return (f'<div class="lane lane--{tone}" role="listitem">'
            f'<div class="lane__head"><span class="lane__dot lane__dot--{tone}"></span>'
            f'<span class="lane__title">{title}</span>{n}</div>'
            f'<div class="lane__cards">{"".join(cards)}</div></div>')

# ===========================================================================
# GATE + PORTAL
# ===========================================================================
def signin(prefix, ctx):
    I = ctx["ICON"]
    roles = [
        ("student", I["brain"], bi("Ramathibodi Student", "นักศึกษารามาธิบดี"),
         bi("Learn the full Academy curriculum.", "เรียนหลักสูตรอคาเดมีทั้งหมด")),
        ("faculty", I["users"], bi("Ramathibodi Faculty", "อาจารย์และบุคลากรรามาธิบดี"),
         bi("Teach, mentor, and post problems.", "สอน เป็นเมนเทอร์ และโพสต์โจทย์")),
        ("fellow", I["flask"], bi("Fellow", "เฟลโลว์"),
         bi("Enter the Fellowship portal.", "เข้าสู่พอร์ทัลเฟลโลว์ชิป")),
        ("partner", I["node"], bi("Partner", "พันธมิตร"),
         bi("Hospitals, agencies, and companies.", "โรงพยาบาล หน่วยงาน และบริษัท")),
        ("admin", I["shield"], bi("Admin", "ผู้ดูแลระบบ"),
         bi("Manage the club and the platform.", "ดูแลคลับและแพลตฟอร์ม")),
    ]
    cards = ""
    for rid, icon, label, desc in roles:
        cards += (f'<button type="button" class="role" data-role="{rid}">'
                  f'<span class="role__ic">{icon}</span>'
                  f'<span class="role__t">{label}</span>'
                  f'<span class="role__d">{desc}</span></button>')
    return f"""
<section class="gate" data-signin>
  <div class="gate__card" style="max-width:560px">
    <span class="eyebrow">{bi("Sign in", "เข้าสู่ระบบ")}</span>
    <h2 class="mt2">{bi("Welcome. Who are you?", "ยินดีต้อนรับ คุณคือใคร")}</h2>
    <p class="muted mt2" style="font-size:.92rem">{bi("Choose your role, then enter your access code.", "เลือกบทบาทของคุณ แล้วกรอกรหัสเข้าใช้งาน")}</p>
    <div class="role-grid mt3">{cards}</div>
    <form class="signin-form" style="margin-top:1.2rem;display:none">
      <div class="field"><label>{bi("Access code", "รหัสเข้าใช้งาน")}</label>
        <input type="password" autocomplete="off" {ph('Enter your code', 'กรอกรหัสของคุณ')}/></div>
      <div class="gate__msg"></div>
      <div class="btn-row mt3"><button class="btn btn--grad btn--lg" type="submit" style="width:100%;justify-content:center">{bi("Enter", "เข้าสู่ระบบ")}</button></div>
    </form>
    <p class="gate__hint mt3">{bi("Codes are issued by your programme lead. Do not have one?", "รหัสออกให้โดยผู้ดูแลโปรแกรมของคุณ ยังไม่มีรหัส?")} <a href="{prefix}contact.html" style="color:var(--accent)">{bi("Contact us", "ติดต่อเรา")}</a>.</p>
  </div>
</section>"""

def admin_page(prefix, ctx):
    return f"""
<section class="section">
  <div class="container" data-guard="admin" data-guard-gate="signin.html">
    <span class="eyebrow reveal">{bi("Admin", "ผู้ดูแลระบบ")}</span>
    <h1 class="reveal mt3" data-d="1" style="max-width:16ch">{bi("Club control room.", "ห้องควบคุมคลับ")}</h1>
    <p class="lead reveal measure" data-d="2">{bi("A private overview for club administrators. Members, cohorts, datasets, and the task board live here once the Supabase backend is connected.", "ภาพรวมส่วนตัวสำหรับผู้ดูแลคลับ สมาชิก รุ่น ชุดข้อมูล และกระดานโจทย์จะอยู่ที่นี่เมื่อเชื่อมต่อระบบหลังบ้าน Supabase แล้ว")}</p>
    <div class="grid grid-3 mt5">
      <div class="card reveal"><h3>{bi("Members", "สมาชิก")}</h3><p>{bi("Students, faculty, fellows, and partners.", "นักศึกษา อาจารย์ เฟลโลว์ และพันธมิตร")}</p></div>
      <div class="card reveal" data-d="1"><h3>{bi("Cohorts", "รุ่น")}</h3><p>{bi("Academy and Fellowship intakes.", "การรับเข้าอคาเดมีและเฟลโลว์ชิป")}</p></div>
      <div class="card reveal" data-d="2"><h3>{bi("Platform", "แพลตฟอร์ม")}</h3><p>{bi("Datasets, tasks, and matching.", "ชุดข้อมูล โจทย์ และการจับคู่")}</p></div>
    </div>
    <div class="btn-row mt5"><a class="btn btn--ghost" href="{prefix}index.html" data-signout="admin">{bi("Sign out", "ออกจากระบบ")}</a></div>
  </div>
</section>"""

def legal_page(title_en, title_th, lead_en, lead_th, sections):
    def fn(prefix, ctx):
        secs = ""
        for (h_en, h_th), (b_en, b_th) in sections:
            secs += f'<h2 class="mt5">{bi(h_en, h_th)}</h2><p class="mt2">{bi(b_en, b_th)}</p>'
        return f"""
<section class="section">
  <div class="container">
    <div style="max-width:70ch">
      <span class="eyebrow reveal">{bi(title_en, title_th)}</span>
      <h1 class="reveal mt3" data-d="1">{bi(title_en, title_th)}</h1>
      <p class="lead reveal mt3">{bi(lead_en, lead_th)}</p>
      <div class="prose reveal mt4">{secs}</div>
    </div>
  </div>
</section>"""
    return fn

conduct_page = legal_page(
    "Code of Conduct", "จรรยาบรรณ",
    "We are a community of clinicians, engineers, and students. We treat each other, and patient data, with respect.",
    "เราคือชุมชนของแพทย์ วิศวกร และนักศึกษา เราปฏิบัติต่อกันและต่อข้อมูลผู้ป่วยด้วยความเคารพ",
    [
        (("Respect", "ความเคารพ"), ("Be kind, be direct, assume good faith. Harassment or discrimination of any kind is not tolerated.", "มีน้ำใจ ตรงไปตรงมา และเชื่อในเจตนาดีของกันและกัน เราไม่ยอมรับการคุกคามหรือการเลือกปฏิบัติทุกรูปแบบ")),
        (("Patient first", "ผู้ป่วยมาก่อน"), ("Everything we build serves patient care. Safety and dignity come before novelty.", "ทุกสิ่งที่เราสร้างมีไว้เพื่อการดูแลผู้ป่วย ความปลอดภัยและศักดิ์ศรีมาก่อนความแปลกใหม่")),
        (("Data with care", "ดูแลข้อมูล"), ("Handle clinical data lawfully and minimally, under supervision, always with a PDPA basis.", "จัดการข้อมูลคลินิกอย่างถูกกฎหมายและเท่าที่จำเป็น ภายใต้การกำกับ และมีฐานตาม PDPA เสมอ")),
        (("Report", "แจ้งเหตุ"), ("If something is wrong, tell a programme lead. We will listen.", "หากมีสิ่งใดผิดปกติ แจ้งผู้ดูแลโปรแกรม เราพร้อมรับฟัง")),
    ])

privacy_page = legal_page(
    "Privacy (PDPA)", "ความเป็นส่วนตัว (PDPA)",
    "How we handle personal data, in line with Thailand's Personal Data Protection Act.",
    "เราจัดการข้อมูลส่วนบุคคลอย่างไร ตามพระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคลของไทย",
    [
        (("What we collect", "เราเก็บอะไร"), ("Only what a task needs: your contact details when you enrol or apply, and site analytics. We do not collect patient data through this website.", "เฉพาะสิ่งที่จำเป็นต่องาน ได้แก่ ข้อมูลติดต่อเมื่อคุณสมัคร และสถิติการใช้งานเว็บไซต์ เราไม่เก็บข้อมูลผู้ป่วยผ่านเว็บไซต์นี้")),
        (("Your rights", "สิทธิของคุณ"), ("Under PDPA you may access, correct, or ask us to delete your personal data. Contact us to exercise these rights.", "ภายใต้ PDPA คุณมีสิทธิเข้าถึง แก้ไข หรือขอให้ลบข้อมูลส่วนบุคคลของคุณ ติดต่อเราเพื่อใช้สิทธิเหล่านี้")),
        (("Clinical data", "ข้อมูลคลินิก"), ("Clinical and research data are governed separately, under supervised access and a specific lawful basis, never through this public site.", "ข้อมูลคลินิกและการวิจัยถูกกำกับแยกต่างหาก ภายใต้การเข้าถึงที่มีการกำกับและฐานทางกฎหมายเฉพาะ ไม่ผ่านเว็บไซต์สาธารณะนี้")),
    ])

def gate_body(prefix, scope, target, eyebrow, headline, hint):
    return f"""
<section class="gate" data-gate="{scope}" data-gate-target="{target}">
  <div class="gate__card reveal">
    <span class="eyebrow">{eyebrow}</span>
    <h2 class="mt2">{headline}</h2>
    <form>
      <div class="field"><label>Access code</label><input type="password" autocomplete="off" placeholder="Enter your member code" autofocus/></div>
      <div class="gate__msg"></div>
      <div class="btn-row mt3"><button class="btn btn--grad btn--lg" type="submit" style="width:100%;justify-content:center">Enter</button></div>
    </form>
    <p class="gate__hint">{hint}</p>
    <p class="gate__hint"><a href="{prefix}index.html" style="color:var(--accent)">Back to the public site</a></p>
  </div>
</section>"""

def portal_body(prefix):
    return f"""
<section class="section">
  <div class="container">
    <span class="eyebrow reveal">{bi("Fellowship portal", "พอร์ทัลเฟลโลว์ชิป")}</span>
    <h1 class="reveal mt3" data-d="1" style="max-width:18ch">{bi("Welcome back, fellow.", "ยินดีต้อนรับกลับมา เฟลโลว์")}</h1>
    <p class="lead reveal measure" data-d="2">{bi("This is the private workspace for current fellows and mentors. Cohort resources, project tracking, and data access guides live here.", "นี่คือพื้นที่ทำงานส่วนตัวสำหรับเฟลโลว์และเมนเทอร์ปัจจุบัน ทรัพยากรของรุ่น การติดตามโปรเจกต์ และคู่มือการเข้าถึงข้อมูล อยู่ที่นี่")}</p>
    <div class="grid grid-3 mt5">
      <div class="card reveal"><h3>{bi("Cohort handbook", "คู่มือประจำรุ่น")}</h3><p>{bi("Schedule, expectations, and your mentor pairing.", "ตารางเวลา ความคาดหวัง และการจับคู่เมนเทอร์ของคุณ")}</p></div>
      <div class="card reveal" data-d="1"><h3>{bi("Data access", "การเข้าถึงข้อมูล")}</h3><p>{bi("How to request and use supervised clinical data safely.", "วิธีขอและใช้ข้อมูลคลินิกที่มีการกำกับดูแลอย่างปลอดภัย")}</p></div>
      <div class="card reveal" data-d="2"><h3>{bi("Project board", "กระดานโปรเจกต์")}</h3><p>{bi("Track your build, reviews, and deployment milestones.", "ติดตามการสร้าง การรีวิว และก้าวสำคัญของการนำไปใช้จริง")}</p></div>
    </div>
    <div class="btn-row mt5">
      <a class="btn btn--ghost" href="{prefix}academy/learn/index.html">{bi("Open the curriculum", "เปิดหลักสูตร")}</a>
      <a class="btn btn--ghost" href="{prefix}fellowship.html" data-signout="fellowship">{bi("Sign out", "ออกจากระบบ")}</a>
    </div>
  </div>
</section>"""

# ===========================================================================
# REGISTER
# ===========================================================================
# ===========================================================================
# VENTURE STUDIO
# ===========================================================================
def venture(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div>
  {hero_line_art()}
  <div class="container">
  {note_hand("past the demo", "ให้ไกลกว่าเดโม")}
  <span class="eyebrow reveal">{bi("Venture Studio", "เวนเจอร์สตูดิโอ")}</span>
  <h1 class="reveal" data-d="1" style="max-width:17ch">{bi("The best work should not stop at a demo.", "งานที่ดีที่สุดไม่ควรหยุดแค่เดโม")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("Proof becomes product: engineering, regulation, evidence, market.", "จากพิสูจน์แล้วสู่ผลิตภัณฑ์ วิศวกรรม กฎระเบียบ หลักฐาน และตลาด")}</p>
</div></section>"""

    what = f"""
<section class="section">
  <div class="container">
    <div class="band reveal">
      <div class="band__glow"></div>
      <div class="container" style="padding-block:clamp(3rem,6vw,5rem)">
        <span class="eyebrow" style="color:#cbd5ef">{bi("What the studio adds", "สิ่งที่สตูดิโอเสริม")}</span>
        <h2 class="mt3" style="color:#fff">{bi("Four things a demo is missing.", "สี่สิ่งที่เดโมยังขาด")}</h2>
        <div class="grid grid-2 mt5">
          <div class="card reveal" style="background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.14)"><div class="card__icon">{I['rocket']}</div><h3 style="color:#fff">{bi("Product engineering", "วิศวกรรมผลิตภัณฑ์")}</h3><p style="color:#aeb9d0">{bi("Reliability, monitoring, and the unglamorous work that makes a prototype safe to run every day.", "ความน่าเชื่อถือ การเฝ้าติดตาม และงานเบื้องหลังที่ทำให้ต้นแบบปลอดภัยพอจะใช้ได้ทุกวัน")}</p></div>
          <div class="card reveal" data-d="1" style="background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.14)"><div class="card__icon">{I['shield']}</div><h3 style="color:#fff">{bi("Regulatory navigation", "การนำทางกฎระเบียบ")}</h3><p style="color:#aeb9d0">{bi("The Thai FDA pathway for AI as Software as a Medical Device, mapped and walked with you.", "เส้นทาง อย. สำหรับ AI ในฐานะ Software as a Medical Device ที่วางแผนและเดินไปด้วยกัน")}</p></div>
          <div class="card reveal" data-d="2" style="background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.14)"><div class="card__icon">{I['pulse']}</div><h3 style="color:#fff">{bi("Clinical evidence", "หลักฐานทางคลินิก")}</h3><p style="color:#aeb9d0">{bi("Study design and validation so the claims hold up to review, not just a good demo day.", "การออกแบบงานวิจัยและการตรวจสอบ เพื่อให้ข้อกล่าวอ้างผ่านการตรวจทาน ไม่ใช่แค่วันเดโมที่ดูดี")}</p></div>
          <div class="card reveal" data-d="3" style="background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.14)"><div class="card__icon">{I['compass']}</div><h3 style="color:#fff">{bi("Route to market", "เส้นทางสู่ตลาด")}</h3><p style="color:#aeb9d0">{bi("Pilots, procurement, and the move from research to venture through the Thai HealthTech ecosystem.", "การนำร่อง การจัดซื้อ และการเปลี่ยนจากงานวิจัยสู่เวนเจอร์ผ่านระบบนิเวศเฮลท์เทคไทย")}</p></div>
        </div>
      </div>
    </div>
  </div>
</section>"""

    path = sec(
        head(bi("From research to venture", "จากงานวิจัยสู่เวนเจอร์"), bi("A path, not a leap.", "เส้นทาง ไม่ใช่การกระโดด")) +
        flow([
            (bi("01", "01"), bi("Proven project", "โปรเจกต์ที่พิสูจน์แล้ว"), bi("A tool that already helped in a real workflow, with evidence.", "เครื่องมือที่ช่วยได้จริงในเวิร์กโฟลว์ พร้อมหลักฐาน")),
            (bi("02", "02"), bi("Hardening", "ทำให้แข็งแรง"), bi("Engineering, security, and a regulatory plan.", "วิศวกรรม ความปลอดภัย และแผนกฎระเบียบ")),
            (bi("03", "03"), bi("Pilot", "นำร่อง"), bi("A supervised deployment with clinical validation.", "การนำไปใช้แบบมีการกำกับ พร้อมการตรวจสอบทางคลินิก")),
            (bi("04", "04"), bi("Venture", "เวนเจอร์"), bi("Spin-out or adoption, with NIA and ecosystem support.", "แยกตัวเป็นบริษัทหรือถูกนำไปใช้ พร้อมการสนับสนุนจาก NIA และระบบนิเวศ")),
        ], [I["flask"], I["shield"], I["pulse"], I["rocket"]]))

    portfolio = sec(
        head(bi("Portfolio", "พอร์ตโฟลิโอ"), bi("What comes out of it.", "สิ่งที่ออกมาจากมัน"), bi("Illustrative examples of the kind of product the studio exists to build.", "ตัวอย่างประเภทของผลิตภัณฑ์ที่สตูดิโอมีไว้เพื่อสร้าง")) +
        '<div class="grid grid-3">' +
        task_card('doc', bi("Radiology", "รังสีวิทยา"), bi("Chest X-ray triage, adopted by a department", "คัดกรองเอกซเรย์ทรวงอก ที่หน่วยงานรับไปใช้"), bi("From teaching set to a supervised pilot on the ward.", "จากชุดสอนสู่การนำร่องแบบมีการกำกับบนหอผู้ป่วย"), ctx, 1) +
        task_card('flask', bi("Pharmacy", "เภสัชกรรม"), bi("Thai drug-interaction assistant", "ผู้ช่วยตรวจปฏิกิริยาระหว่างยาภาษาไทย"), bi("A grounded assistant with a clear evidence base.", "ผู้ช่วยที่อ้างอิงแหล่งข้อมูล บนฐานหลักฐานที่ชัดเจน"), ctx, 2) +
        task_card('node', bi("Outpatient", "ผู้ป่วยนอก"), bi("Line follow-up product", "ผลิตภัณฑ์ติดตามอาการผ่าน Line"), bi("From a bot to a maintained service with governance.", "จากบอทสู่บริการที่ดูแลต่อเนื่องพร้อมธรรมาภิบาล"), ctx, 3) +
        '</div>' +
        f'<p class="muted mt4 reveal" style="font-size:.82rem">{bi("Illustrative. Real portfolio entries publish as pilots mature.", "เป็นตัวอย่าง พอร์ตจริงจะเผยแพร่เมื่อการนำร่องเติบโต")}</p>')

    cta = sec(
        f'<div class="band reveal"><div class="band__glow"></div><div class="container" style="padding-block:clamp(3rem,6vw,5rem)">'
        f'<h2 style="color:#fff;max-width:20ch">{bi("Have work that deserves to live?", "มีงานที่คู่ควรจะอยู่ต่อไหม?")}</h2>'
        f'<div class="btn-row" style="margin-top:2rem"><a class="btn btn--grad" href="{prefix}contact.html">{bi("Talk to the studio", "คุยกับสตูดิโอ")} {I["arrow"]}</a>'
        f'<a class="btn btn--ghost btn--on-dark" href="{prefix}fellowship.html">{bi("Start in the Fellowship", "เริ่มที่เฟลโลว์ชิป")}</a></div>'
        f'</div></div>')

    return hero + what + path + portfolio + cta

# ===========================================================================
# TEAM
# ===========================================================================
def _person(initials, name, role_en, role_th, bio_en, bio_th, tag_en, tag_th):
    return (f'<div class="person reveal"><div class="person__avatar">{initials}</div>'
            f'<div class="person__name">{name}</div>'
            f'<div class="person__role">{bi(role_en, role_th)}</div>'
            f'<p class="person__bio">{bi(bio_en, bio_th)}</p>'
            f'<span class="person__tag">{bi(tag_en, tag_th)}</span></div>')

def team(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  {note_hand("who is in the room", "ใครอยู่ในห้องนี้")}
  <span class="eyebrow reveal">{bi("The team", "ทีมงาน")}</span>
  <h1 class="reveal" data-d="1" style="max-width:16ch">{bi("The people behind the line.", "คนเบื้องหลังเส้นสายเดียวนั้น")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("People who decided Thailand should build its own medical AI.", "คนที่เชื่อว่าประเทศไทยควรสร้าง AI การแพทย์ของตนเอง")}</p>
</div></section>"""

    lead = sec(
        head(bi("Leadership", "ทีมนำ"), bi("Faculty and founders.", "อาจารย์และผู้ก่อตั้ง")) +
        '<div class="team-grid">' +
        _person("RA", bi("Faculty Lead", "หัวหน้าฝ่ายวิชาการ"), "Faculty advisor", "ที่ปรึกษาคณาจารย์",
                "Physician and academic sponsor within the Faculty of Medicine, connecting the club to real clinical need.",
                "แพทย์และผู้สนับสนุนเชิงวิชาการในคณะแพทยศาสตร์ เชื่อมชมรมเข้ากับความต้องการจริงในคลินิก", "Ramathibodi", "รามาธิบดี") +
        _person("PL", bi("Programme Lead", "หัวหน้าโครงการ"), "Curriculum & operations", "หลักสูตรและปฏิบัติการ",
                "Runs the Academy and Fellowship, from cohort design to the projects that ship.",
                "ดูแลอคาเดมีและเฟลโลว์ชิป ตั้งแต่การออกแบบรุ่นจนถึงโปรเจกต์ที่ส่งจริง", "Core team", "ทีมหลัก") +
        _person("EL", bi("Engineering Lead", "หัวหน้าวิศวกรรม"), "Platform & tooling", "แพลตฟอร์มและเครื่องมือ",
                "Builds the data pipelines, the reader, and the tools members use to ship safely.",
                "สร้างไปป์ไลน์ข้อมูล ระบบอ่าน และเครื่องมือที่สมาชิกใช้ส่งงานอย่างปลอดภัย", "Core team", "ทีมหลัก") +
        '</div>')

    crew = sec(
        head(bi("Core team", "ทีมหลัก"), bi("The builders.", "ผู้ลงมือสร้าง")) +
        '<div class="team-grid">' +
        _person("CL", bi("Clinical Lead", "หัวหน้าคลินิก"), "Clinical validation", "การตรวจสอบทางคลินิก",
                "Keeps every project honest against how care actually happens on the ward.",
                "รักษาให้ทุกโปรเจกต์ตรงกับการดูแลผู้ป่วยจริงบนหอผู้ป่วย", "Clinician", "แพทย์") +
        _person("DL", bi("Data Lead", "หัวหน้าข้อมูล"), "Data governance", "ธรรมาภิบาลข้อมูล",
                "Owns de-identification, PDPA basis, and the terms every dataset ships under.",
                "ดูแลการลบตัวตน ฐาน PDPA และเงื่อนไขการเผยแพร่ของทุกชุดข้อมูล", "Governance", "ธรรมาภิบาล") +
        _person("CM", bi("Community Lead", "หัวหน้าชุมชน"), "Members & partners", "สมาชิกและพันธมิตร",
                "Grows the community across Line, Discord, and the partner network.",
                "ขยายชุมชนผ่าน Line, Discord และเครือข่ายพันธมิตร", "Community", "ชุมชน") +
        _person("ST", bi("Student Leads", "ผู้นำนักศึกษา"), "Cohort representatives", "ตัวแทนรุ่น",
                "Students who run study groups, hack nights, and keep the club a club.",
                "นักศึกษาที่จัดกลุ่มติว แฮกไนต์ และทำให้ชมรมเป็นชมรมจริง ๆ", "Students", "นักศึกษา") +
        '</div>' +
        f'<p class="muted mt5 reveal" style="font-size:.82rem">{bi("Placeholder roster. Real names, photos, and bios go live before launch.", "รายชื่อตัวอย่าง ชื่อจริง รูปภาพ และประวัติจะขึ้นก่อนเปิดตัว")}</p>')

    join = sec(
        f'<div class="band reveal"><div class="band__glow"></div><div class="container" style="padding-block:clamp(3rem,6vw,5rem)">'
        f'<span class="eyebrow" style="color:#cbd5ef">{bi("Join us", "ร่วมกับเรา")}</span>'
        f'<h2 class="mt3" style="color:#fff;max-width:18ch">{bi("We are looking for people who build.", "เรากำลังมองหาคนที่ลงมือสร้าง")}</h2>'
        f'<div class="btn-row" style="margin-top:2rem"><a class="btn btn--grad" href="{prefix}careers.html">{bi("See open roles", "ดูตำแหน่งที่เปิดรับ")} {I["arrow"]}</a>'
        f'<a class="btn btn--ghost btn--on-dark" href="{prefix}contact.html">{bi("Say hello", "ทักทายเรา")}</a></div>'
        f'</div></div>')

    return hero + lead + crew + ctx["community_block"](prefix) + join

# ===========================================================================
# ANNUAL REPORT
# ===========================================================================
def _metric(num, label_en, label_th):
    return f'<div class="metric reveal"><div class="metric__num">{num}</div><div class="metric__label">{bi(label_en, label_th)}</div></div>'

def annual_report(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  {note_hand("the denominator shown", "แสดงตัวหารเสมอ")}
  <span class="eyebrow reveal">{bi("Annual report 2026", "รายงานประจำปี 2569")}</span>
  <h1 class="reveal" data-d="1" style="max-width:17ch">{bi("A year, measured in patients helped.", "หนึ่งปี วัดด้วยจำนวนผู้ป่วยที่ได้รับการช่วยเหลือ")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("What we set out to do, what we built, and what we learned. Written plainly, with the denominators shown.", "สิ่งที่เราตั้งใจทำ สิ่งที่เราสร้าง และสิ่งที่เราได้เรียนรู้ เขียนอย่างตรงไปตรงมา พร้อมแสดงตัวหารให้เห็น")}</p>
</div></section>"""

    metrics = sec(
        head(bi("The year in numbers", "หนึ่งปีในตัวเลข"), bi("Illustrative figures.", "ตัวเลขตัวอย่าง")) +
        '<div class="report-metrics">' +
        _metric("6", "Courses shipped", "คอร์สที่เปิดสอน") +
        _metric("120+", "Members trained", "สมาชิกที่ได้รับการอบรม") +
        _metric("14", "Projects to prototype", "โปรเจกต์ที่ถึงต้นแบบ") +
        _metric("9", "Partner organisations", "องค์กรพันธมิตร") +
        '</div>' +
        f'<p class="report-note reveal">{bi("Figures are illustrative placeholders for the design. Real, audited numbers replace them at year end.", "ตัวเลขเป็นตัวอย่างสำหรับการออกแบบ ตัวเลขจริงที่ตรวจสอบแล้วจะแทนที่เมื่อสิ้นปี")}</p>')

    letter = sec(
        head(bi("From the team", "จากทีมงาน"), bi("What this year was about.", "ปีนี้คือเรื่องของอะไร")) +
        f'<div class="measure reveal" style="font-size:1.05rem;color:var(--ink-soft);line-height:1.75">'
        f'<p>{bi("We started with a simple discomfort: hospitals were buying AI they could not inspect, and students were learning about AI they never got to build. So we made a club that does the opposite. Members do not study medical AI from a distance. They build it, evaluate it honestly, and carry it toward the bedside.", "เราเริ่มจากความอึดอัดง่าย ๆ โรงพยาบาลกำลังซื้อ AI ที่ตรวจสอบไม่ได้ และนักศึกษากำลังเรียนเรื่อง AI ที่ไม่เคยได้ลงมือสร้าง เราจึงสร้างชมรมที่ทำตรงกันข้าม สมาชิกไม่ได้เรียน AI การแพทย์จากระยะไกล แต่ลงมือสร้าง ประเมินอย่างตรงไปตรงมา และนำมันไปสู่ข้างเตียงผู้ป่วย")}</p>'
        f'<p class="mt4">{bi("This report is short on purpose. It shows what we built, the projects that reached a real ward, and the ones that failed and taught us why. Honesty is a design material here too.", "รายงานนี้สั้นโดยตั้งใจ มันแสดงสิ่งที่เราสร้าง โปรเจกต์ที่ไปถึงหอผู้ป่วยจริง และโปรเจกต์ที่ล้มเหลวและสอนเราว่าทำไม ความซื่อตรงคือวัสดุในการออกแบบที่นี่เช่นกัน")}</p>'
        f'</div>')

    highlights = sec(
        head(bi("Highlights", "ไฮไลต์"), bi("Three things worth remembering.", "สามสิ่งที่ควรจดจำ")) +
        '<div class="rows">' +
        task_row(bi("Academy", "อคาเดมี"), bi("Six-course curriculum, taught end to end", "หลักสูตรหกคอร์ส สอนครบเส้นทาง"), bi("From what AI is, to a system a hospital can run.", "ตั้งแต่ AI คืออะไร จนถึงระบบที่โรงพยาบาลใช้ได้จริง")) +
        task_row(bi("Platform", "แพลตฟอร์ม"), bi("Governed datasets and an open leaderboard", "ชุดข้อมูลที่กำกับดูแลและลีดเดอร์บอร์ดแบบเปิด"), bi("Members benchmark in the open, rewarding calibration and fairness.", "สมาชิกวัดผลอย่างเปิดเผย ให้ค่ากับ calibration และความเป็นธรรม")) +
        task_row(bi("Fellowship", "เฟลโลว์ชิป"), bi("First fellows carried projects to the ward", "เฟลโลว์รุ่นแรกนำโปรเจกต์สู่หอผู้ป่วย"), bi("Real systems, evaluated against real care.", "ระบบจริง ประเมินกับการดูแลผู้ป่วยจริง")) +
        '</div>')

    cta = sec(
        f'<div class="band reveal"><div class="band__glow"></div><div class="container" style="padding-block:clamp(3rem,6vw,5rem)">'
        f'<h2 style="color:#fff;max-width:20ch">{bi("Read the work, then come build the next chapter.", "อ่านผลงาน แล้วมาสร้างบทต่อไปด้วยกัน")}</h2>'
        f'<div class="btn-row" style="margin-top:2rem"><a class="btn btn--grad" href="{prefix}academy.html">{bi("Explore the Academy", "สำรวจอคาเดมี")} {I["arrow"]}</a>'
        f'<a class="btn btn--ghost btn--on-dark" href="{prefix}fellowship.html">{bi("The Fellowship", "เฟลโลว์ชิป")}</a></div>'
        f'</div></div>')

    return hero + metrics + letter + highlights + cta

# ===========================================================================
# TOOLS
# ===========================================================================
def _tool(icon, state_en, state_th, build, title, desc, for_en, for_th):
    cls = "tool__state tool__state--build" if build else "tool__state"
    return (f'<div class="tool reveal"><div class="tool__head"><span class="tool__ic">{icon}</span>'
            f'<span class="{cls}">{bi(state_en, state_th)}</span></div>'
            f'<h3>{title}</h3><p>{desc}</p>'
            f'<div class="tool__for">{bi(for_en, for_th)}</div></div>')

def tools_funnel(prefix):
    """Fifth signature sketch: the toolkit as a funnel, distinct in shape from
    the path, the trail, the orbit, and the hub. Wide and messy at the top
    (raw Thai clinical reality), narrow and trustworthy at the bottom (what a
    student or faculty member actually gets to use)."""
    bands = [
        (60, 520, 70, "Raw reality", "ความจริงดิบ", "Messy Thai notes, no labels, no structure", "โน้ตภาษาไทยที่ยุ่งเหยิง ไม่มีป้ายกำกับ ไม่มีโครงสร้าง"),
        (140, 440, 150, "De-identify & ground", "ลบตัวตนและอ้างอิง", "PDPA-safe text, answers tied to real guidelines", "ข้อความปลอดภัยตาม PDPA คำตอบอ้างอิงแนวปฏิบัติจริง"),
        (220, 360, 230, "Evaluate honestly", "ประเมินอย่างตรงไปตรงมา", "A report card with the denominator shown", "รายงานผลที่แสดงตัวหารเสมอ"),
        (280, 320, 310, "Routed to you", "ส่งตรงถึงคุณ", "The Learning Navigator hands you the next step", "เนวิเกเตอร์การเรียนรู้ยื่นก้าวถัดไปให้คุณ"),
    ]
    trapezoids = ""
    for i in range(len(bands) - 1):
        x1a, x1b, y1, *_ = bands[i]
        x2a, x2b, y2, *_ = bands[i + 1]
        trapezoids += f'<path class="tf-band" d="M {x1a} {y1} L {x1b} {y1} L {x2b} {y2} L {x2a} {y2} Z"/>'
    labels = ""
    for xa, xb, y, lab_en, lab_th, cap_en, cap_th in bands:
        cx = (xa + xb) / 2
        labels += (f'<text class="l-en tf-lab" x="{cx}" y="{y-10}" text-anchor="middle">{lab_en}</text>'
                   f'<text class="l-th tf-lab" x="{cx}" y="{y-10}" text-anchor="middle">{lab_th}</text>'
                   f'<text class="l-en tf-cap" x="{cx}" y="{y+16}" text-anchor="middle">{cap_en}</text>'
                   f'<text class="l-th tf-cap" x="{cx}" y="{y+16}" text-anchor="middle">{cap_th}</text>')
    svg = f"""
<div class="flow-art reveal">
  <svg viewBox="0 0 600 380" role="img" aria-label="The toolkit, as a funnel from raw text to a routed answer" preserveAspectRatio="xMidYMid meet">
    <defs>
      <filter id="sketch5" x="-8%" y="-8%" width="116%" height="116%">
        <feTurbulence type="fractalNoise" baseFrequency="0.016" numOctaves="2" seed="31" result="n"/>
        <feDisplacementMap in="SourceGraphic" in2="n" scale="3"/>
      </filter>
      <linearGradient id="tf-grad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#fd6502"/><stop offset="0.5" stop-color="#91386e"/><stop offset="1" stop-color="#2a1bd6"/>
      </linearGradient>
    </defs>
    <g filter="url(#sketch5)" fill="url(#tf-grad)" fill-opacity="0.10" stroke="url(#tf-grad)" stroke-width="1.6">
      {trapezoids}
    </g>
    {labels}
    <text class="fa-hand" x="360" y="60" transform="rotate(3 360 60)">this is the whole job</text>
    <path class="fa-hand-arrow" d="M400 68 q 16 18 8 40"/>
  </svg>
  <div class="flow-art__legend">
    <span class="l-en">Every tool below does one part of this narrowing: from messy reality to one trustworthy, routed answer.</span>
    <span class="l-th">เครื่องมือแต่ละชิ้นด้านล่างทำหน้าที่หนึ่งช่วงของการค่อย ๆ กลั่นนี้ จากความจริงที่ยุ่งเหยิง สู่คำตอบเดียวที่เชื่อถือได้และส่งตรงถึงคุณ</span>
  </div>
</div>"""
    return (f'<section class="section"><div class="container">'
            f'{head(bi("How the toolkit works", "ชุดเครื่องมือทำงานอย่างไร"), bi("Narrowing from raw text to one routed answer.", "ค่อย ๆ กลั่นจากข้อความดิบ สู่คำตอบเดียวที่ส่งตรงถึงคุณ"))}'
            f'{svg}</div></section>')

def tools(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  {note_hand("small, sharp instruments", "เครื่องมือเล็กแต่คม")}
  <span class="eyebrow reveal">{bi("Tools", "เครื่องมือ")}</span>
  <h1 class="reveal" data-d="1" style="max-width:15ch">{bi("Tools we build so the work gets easier.", "เครื่องมือที่เราสร้าง เพื่อให้งานง่ายขึ้น")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("Small instruments. Real chores removed. Built Thai-first.", "เครื่องมือเล็กแต่คม ตัดงานน่าเบื่อออกไป สร้างแบบไทยเป็นหลัก")}</p>
</div></section>"""

    grid = sec(
        head(bi("The toolkit", "ชุดเครื่องมือ"), bi("Value you can use today.", "คุณค่าที่ใช้ได้จริง")) +
        '<div class="tool-grid">' +
        _tool(I["compass"], "Flagship", "เรือธง", True,
              bi("Learning Navigator", "เนวิเกเตอร์การเรียนรู้"),
              bi("The proprietary one. Tell it where you are, a first-year resident, a faculty statistician, a nurse who codes, and it maps the shortest path from your skills to where Thailand’s hospitals actually need people. It reads live workforce demand and the club’s own project outcomes, then hands you a route: which courses, which real project, which mentor. Your learning stops being a guess.", "ตัวเด็ดที่เป็นกรรมสิทธิ์ บอกมันว่าคุณอยู่ตรงไหน แพทย์ประจำบ้านปีหนึ่ง อาจารย์สายสถิติ หรือพยาบาลที่เขียนโค้ดได้ แล้วมันจะวางเส้นทางที่สั้นที่สุดจากทักษะของคุณไปยังจุดที่โรงพยาบาลไทยต้องการคนจริง ๆ มันอ่านความต้องการกำลังคนแบบเรียลไทม์และผลลัพธ์โปรเจกต์ของชมรมเอง แล้วยื่นเส้นทางให้คุณ คอร์สไหน โปรเจกต์จริงชิ้นไหน เมนเทอร์คนไหน การเรียนของคุณจะเลิกเป็นการเดา"),
              "For: students, residents, faculty", "สำหรับ: นักศึกษา แพทย์ประจำบ้าน อาจารย์") +
        _tool(I["shield"], "In build", "กำลังสร้าง", True,
              bi("Thai clinical-text de-identifier", "เครื่องมือลบตัวตนจากข้อความคลินิกภาษาไทย"),
              bi("Paste Thai clinical notes and get PDPA-safe, de-identified text back. Names, hospital numbers, dates, and places removed with a reviewable audit trail. Drop-in for any project on the platform.", "วางข้อความคลินิกภาษาไทย แล้วได้ข้อความที่ลบตัวตนและปลอดภัยตาม PDPA กลับมา ลบชื่อ เลขโรงพยาบาล วันที่ และสถานที่ พร้อมร่องรอยให้ตรวจสอบได้ ใช้ได้ทันทีกับทุกโปรเจกต์บนแพลตฟอร์ม"),
              "For: anyone touching patient text", "สำหรับ: ทุกคนที่ทำงานกับข้อความผู้ป่วย") +
        _tool(I["doc"], "In build", "กำลังสร้าง", True,
              bi("Grounded Thai guideline assistant", "ผู้ช่วยแนวเวชปฏิบัติภาษาไทยแบบอ้างอิง"),
              bi("Ask a clinical question and get an answer grounded in Thai clinical practice guidelines and Ramathibodi protocols, with a citation for every claim. Retrieval-augmented, so it shows its sources instead of guessing.", "ถามคำถามทางคลินิกแล้วได้คำตอบที่อ้างอิงแนวเวชปฏิบัติไทยและโปรโตคอลรามาธิบดี พร้อมการอ้างอิงในทุกข้อความ ใช้ RAG จึงแสดงแหล่งที่มาแทนการเดา"),
              "For: students, ward teams", "สำหรับ: นักศึกษา ทีมหอผู้ป่วย") +
        _tool(I["pulse"], "In build", "กำลังสร้าง", True,
              bi("Model report card generator", "เครื่องมือสร้างรายงานผลโมเดล"),
              bi("Give it a model and a test set, get back an honest report card: the denominator, confidence intervals, calibration, and performance broken down by subgroup. It writes the STARD-AI style report so you cannot hide the population a model was tested on.", "ใส่โมเดลและชุดทดสอบ ได้รายงานที่ตรงไปตรงมากลับมา ทั้งตัวหาร ช่วงความเชื่อมั่น calibration และผลแยกตามกลุ่มย่อย เขียนรายงานสไตล์ STARD-AI ให้ คุณจึงซ่อนประชากรที่ใช้ทดสอบโมเดลไม่ได้"),
              "For: builders, reviewers", "สำหรับ: ผู้สร้าง ผู้ตรวจทาน") +
        _tool(I["flask"], "Planned", "วางแผนไว้", False,
              bi("FHIR & synthetic-data sandbox", "แซนด์บ็อกซ์ FHIR และข้อมูลสังเคราะห์"),
              bi("A safe teaching playground: realistic synthetic patients in FHIR, with no privacy risk. Explore records, practise queries, and prototype a pipeline before you ever touch real data.", "สนามฝึกที่ปลอดภัย ผู้ป่วยสังเคราะห์ที่สมจริงในรูปแบบ FHIR โดยไม่มีความเสี่ยงด้านความเป็นส่วนตัว สำรวจเวชระเบียน ฝึกเขียนคำสั่ง และสร้างต้นแบบไปป์ไลน์ก่อนแตะข้อมูลจริง"),
              "For: teaching, onboarding", "สำหรับ: การสอน การเริ่มต้น") +
        _tool(I["compass"], "Planned", "วางแผนไว้", False,
              bi("Study-design & sample-size assistant", "ผู้ช่วยออกแบบงานวิจัยและคำนวณขนาดตัวอย่าง"),
              bi("For faculty writing a paper: a guided assistant for study design, sample-size calculation, and a STARD-AI / TRIPOD-AI reporting checklist, so the methods hold up to review.", "สำหรับอาจารย์ที่เขียนงานวิจัย ผู้ช่วยแบบมีคำแนะนำสำหรับการออกแบบงานวิจัย การคำนวณขนาดตัวอย่าง และเช็กลิสต์การรายงาน STARD-AI / TRIPOD-AI เพื่อให้ระเบียบวิธีผ่านการตรวจทาน"),
              "For: faculty, researchers", "สำหรับ: อาจารย์ นักวิจัย") +
        '</div>' +
        f'<p class="muted mt5 reveal" style="font-size:.82rem">{bi("These are the club’s own tools, built and governed in-house. Access opens to members first.", "นี่คือเครื่องมือของชมรมเอง สร้างและกำกับดูแลภายใน เปิดให้สมาชิกก่อน")}</p>')

    cta = sec(
        f'<div class="band reveal"><div class="band__glow"></div><div class="container" style="padding-block:clamp(3rem,6vw,5rem)">'
        f'<h2 style="color:#fff;max-width:20ch">{bi("Want early access, or a tool we have not built yet?", "อยากได้สิทธิ์ใช้ก่อน หรือเครื่องมือที่เรายังไม่ได้สร้าง?")}</h2>'
        f'<div class="btn-row" style="margin-top:2rem"><a class="btn btn--grad" href="{prefix}contact.html">{bi("Request access", "ขอสิทธิ์เข้าใช้")} {I["arrow"]}</a>'
        f'<a class="btn btn--ghost btn--on-dark" href="{prefix}platform.html">{bi("See the Platform", "ดูแพลตฟอร์ม")}</a></div>'
        f'</div></div>')

    return hero + tools_funnel(prefix) + grid + cta

# ===========================================================================
# SCIENCE OF SCIENCE
# ===========================================================================
MARKETING = [
    ("index.html", "Ramathibodi Digital Health & AI Club", "", home),
    ("who-we-are.html", "Who We Are - DHA Club", "who-we-are.html", who_we_are),
    ("team.html", "Team - DHA Club", "who-we-are.html", team),
    ("annual-report.html", "Annual Report 2026 - DHA Club", "who-we-are.html", annual_report),
    ("venture.html", "Venture Studio - DHA Club", "what-we-do.html", venture),
    ("what-we-do.html", "What We Do - DHA Club", "what-we-do.html", what_we_do),
    ("academy.html", "Academy - DHA Club", "academy.html", academy),
    ("platform.html", "Platform - DHA Club", "platform.html", platform),
    ("tools.html", "Tools - DHA Club", "tools.html", tools),
    ("fellowship.html", "Fellowship - DHA Club", "fellowship.html", fellowship),
    ("fellowship/apply.html", "Apply - Fellowship", "fellowship.html", fellowship_apply),
    ("fellowship/stories.html", "Stories - Fellowship", "fellowship.html", fellowship_stories),
    ("fellowship/publications.html", "Publications - Fellowship", "fellowship.html", fellowship_publications),
    ("fellowship/faq.html", "FAQ - Fellowship", "fellowship.html", fellowship_faq),
    ("insights/index.html", "Insights - DHA Club", "insights/index.html", insights_index),
    ("news/index.html", "News - DHA Club", "insights/index.html", news_index),
    ("careers.html", "Careers - DHA Club", "careers.html", careers),
    ("contact.html", "Contact - DHA Club", "", contact),
    ("signin.html", "Sign in - DHA Club", "", signin),
    ("admin.html", "Admin - DHA Club", "", admin_page),
    ("about/conduct.html", "Code of Conduct - DHA Club", "", conduct_page),
    ("about/privacy.html", "Privacy - DHA Club", "", privacy_page),
]
_INSIGHT_PLAIN_TITLES = {
    "governance-as-design": "Governance is a design material, not a checkpoint",
    "fhir-in-plain-language": "FHIR, in plain language",
    "train-builders-not-buyers": "Why Thailand should train builders, not just buyers",
}
for _slug in INSIGHT_ARTICLES:
    MARKETING.append((f"insights/{_slug}.html", f"{_INSIGHT_PLAIN_TITLES[_slug]} - Insights",
                      "insights/index.html", insight_article(_slug)))
