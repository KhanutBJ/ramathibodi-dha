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

def sec(inner, cls="section"):
    return f'<section class="{cls}"><div class="container">{inner}</div></section>'

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
def home(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero">
  <div class="hero__glow"></div>
  <div class="container">
    <span class="eyebrow reveal">Ramathibodi Digital Health &amp; AI Club</span>
    <h1 class="reveal" data-d="1"><span class="l-en">We train the people who will bring <span class="gradient-text">AI to the bedside</span>.</span><span class="l-th">เราสร้างคนที่จะนำ <span class="gradient-text">AI สู่ข้างเตียงผู้ป่วย</span></span></h1>
    <p class="lead reveal measure" data-d="2">{bi("A club, an academy, and a fellowship built inside one of Thailand's leading medical schools. We turn clinicians, engineers, and scientists into builders who can take medical AI from idea to patient care, safely.", "คลับ อคาเดมี และเฟลโลว์ชิป ที่สร้างขึ้นภายในหนึ่งในโรงเรียนแพทย์ชั้นนำของไทย เราเปลี่ยนแพทย์ วิศวกร และนักวิทยาศาสตร์ ให้เป็นผู้สร้างที่นำ AI ทางการแพทย์จากไอเดียไปสู่การดูแลผู้ป่วยได้จริงอย่างปลอดภัย")}</p>
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

    proof = sec(
        '<div class="reveal" style="display:flex;flex-direction:column;gap:1.4rem">'
        '<span class="eyebrow">Built inside the system, with partners who build</span>'
        '<div class="logos">'
        '<span>Ramathibodi</span><span>Mahidol University</span>'
        '<span>Google Developer Groups on Campus</span><span>BOTNOI Academy</span>'
        '</div>'
        '<div class="logos muted" style="font-size:.85rem">'
        '<span>Aligned with</span><span>MOPH Digital Health</span><span>NHSO</span>'
        '<span>Thai FDA</span><span>NIA</span><span>Thai HealthTech</span>'
        '</div></div>', "section section--tight")

    what = sec(
        head(bi("What we do", "สิ่งที่เราทำ"), bi("Four parts, one pipeline.", "สี่ส่วน หนึ่งเส้นทาง"),
             bi("Most programmes teach theory and stop. We carry a person all the way from first principles to a working clinical product, then help the strongest ideas become real.", "หลักสูตรส่วนใหญ่สอนทฤษฎีแล้วจบ เราพาคนคนหนึ่งไปตลอดทาง ตั้งแต่พื้นฐานจนถึงผลิตภัณฑ์ทางคลินิกที่ใช้ได้จริง แล้วช่วยให้ไอเดียที่ดีที่สุดเกิดขึ้นจริง")) +
        '<div class="grid grid-2">' +
        ctx['card']('brain', bi('Academy', 'อคาเดมี'), bi('An open curriculum in AI and digital health, from foundations to clinical deployment. Free to learn, practical from day one.', 'หลักสูตรเปิดด้าน AI และสุขภาพดิจิทัล ตั้งแต่พื้นฐานจนถึงการนำไปใช้ในคลินิก เรียนฟรี ลงมือทำได้ตั้งแต่วันแรก'), 'academy.html', bi('Start learning', 'เริ่มเรียน'), prefix, 1) +
        ctx['card']('flask', bi('Fellowship', 'เฟลโลว์ชิป'), bi('A selective, in-residence year. Fellows work on real clinical problems with Ramathibodi data, faculty, and patients.', 'หนึ่งปีแบบคัดสรรและประจำในสถานที่ เฟลโลว์ทำงานกับโจทย์คลินิกจริง ด้วยข้อมูล อาจารย์ และผู้ป่วยของรามาธิบดี'), 'fellowship.html', bi('See the Fellowship', 'ดูเฟลโลว์ชิป'), prefix, 2) +
        ctx['card']('rocket', bi('Venture Studio', 'เวนเจอร์สตูดิโอ'), bi('We help the best fellowship work become deployable products, with engineering, regulatory, and go-to-market support.', 'เราช่วยให้ผลงานเฟลโลว์ชิปที่ดีที่สุดกลายเป็นผลิตภัณฑ์ที่ใช้งานได้จริง ด้วยการสนับสนุนด้านวิศวกรรม กฎระเบียบ และการออกสู่ตลาด'), 'what-we-do.html', bi('How it works', 'ทำงานอย่างไร'), prefix, 1) +
        ctx['card']('compass', bi('Consulting', 'ที่ปรึกษานวัตกรรม'), bi('We advise hospitals and agencies building their own AI capability, so the workforce we train has somewhere to land.', 'เราให้คำปรึกษาแก่โรงพยาบาลและหน่วยงานที่กำลังสร้างขีดความสามารถด้าน AI ของตนเอง เพื่อให้คนที่เราฝึกมีที่ไปที่แข็งแรง'), 'what-we-do.html', bi('Work with us', 'ร่วมงานกับเรา'), prefix, 2) +
        '</div>')

    why = f"""
<section class="section">
  <div class="container">
    {head("Why us, why now", "The gap in Thai medical AI is not models. It is people.")}
    <div class="split">
      <div class="stack reveal">
        <p class="lead">The models are here. National policy is here. What is missing is a generation of people who can hold a clinical problem in one hand and a model in the other, and ship something a hospital can trust.</p>
        <p>Thailand's digital health agenda runs through the Ministry of Public Health, the National Health Security Office, the Thai FDA's pathway for Software as a Medical Device, and the National Innovation Agency. Each of them needs the same thing: trained builders. We exist to produce them, inside a hospital, on real problems, with governance built in from the first line of code.</p>
        <a class="btn btn--ghost" href="{prefix}who-we-are.html">Read our position {I['arrow']}</a>
      </div>
      <div class="stack">
        <div class="card reveal"><div class="card--num"><span class="num">01 / Why here</span></div><h3 class="mt2">Inside the clinic</h3><p>We are part of Ramathibodi, not a bootcamp bolted onto it. Real data, real supervision, real patients.</p></div>
        <div class="card reveal" data-d="1"><div class="card--num"><span class="num">02 / Why now</span></div><h3 class="mt2">The threshold crossed</h3><p>AI has reached clinical usefulness while the country is actively writing the rules. The window to train people well is open now.</p></div>
        <div class="card reveal" data-d="2"><div class="card--num"><span class="num">03 / Why this way</span></div><h3 class="mt2">Learn by shipping</h3><p>Apprenticeship over lectures. You build, you are reviewed, you deploy. Safety and evaluation are the curriculum, not an afterthought.</p></div>
      </div>
    </div>
  </div>
</section>"""

    band = f"""
<section class="section">
  <div class="container">
    <div class="band reveal">
      <div class="band__glow"></div>
      <div class="container" style="padding-block:clamp(3rem,6vw,5rem)">
        <div class="split">
          <div class="stack">
            <span class="eyebrow" style="color:#cbd5ef">The model we learn from</span>
            <h2>The craft of medical AI, taught like a craft.</h2>
            <p>Accredited education like the AMA Ed Hub shows what rigorous, clinician-facing AI training looks like. We take that standard of care and pair it with a builder's studio, so people do not just understand medical AI, they make it.</p>
            <div class="btn-row">
              <a class="btn btn--grad" href="{prefix}what-we-do.html">How we teach {I['arrow']}</a>
              <a class="btn btn--ghost" href="{prefix}insights/index.html" style="color:#fff;border-color:rgba(255,255,255,.25)">Read Insights</a>
            </div>
          </div>
          <div class="grid" style="gap:1rem">
            <div style="display:flex;gap:2rem;flex-wrap:wrap">
              {ctx['stat']('<span style="color:#fff">Governance first</span>', '<span style="color:#9fb0d4">Evaluation and safety from day one</span>')}
            </div>
            <div style="display:flex;gap:2rem;flex-wrap:wrap">
              {ctx['stat']('<span style="color:#fff">Real data</span>', '<span style="color:#9fb0d4">Clinical problems, supervised access</span>')}
            </div>
            <div style="display:flex;gap:2rem;flex-wrap:wrap">
              {ctx['stat']('<span style="color:#fff">Real deployment</span>', '<span style="color:#9fb0d4">Ship into the workflow, measure outcomes</span>')}
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

    return (hero + proof
            + moment("hero-clinician.jpg", prefix, bi("AI at the bedside", "AI ข้างเตียงผู้ป่วย") + " / Ramathibodi")
            + what + why + band + insights + cta)

def entry(meta, title, body, href, tone="a", img=None, prefix=""):
    return (f'<a class="entry reveal" href="{href}">'
            f'{frame(meta, "ratio-4x3", tone, img, prefix)}'
            f'<div class="entry__meta">{meta}</div>'
            f'<h3>{title}</h3><p>{body}</p></a>')

# ===========================================================================
# WHO WE ARE
# ===========================================================================
def who_we_are(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:3rem">
  <div class="hero__glow"></div>
  <div class="container">
    <span class="eyebrow reveal">{bi("Who we are", "เกี่ยวกับเรา")}</span>
    <h1 class="reveal" data-d="1" style="max-width:20ch">{bi("A club with the discipline of an institution and the speed of a startup.", "คลับที่มีวินัยของสถาบัน และความเร็วของสตาร์ตอัป")}</h1>
    <p class="lead reveal measure" data-d="2">{bi("We are the Ramathibodi Digital Health and AI Club. We sit inside the Faculty of Medicine Ramathibodi Hospital, Mahidol University, and we are building the people who will modernise Thai healthcare from within.", "เราคือ Ramathibodi Digital Health and AI Club อยู่ภายในคณะแพทยศาสตร์โรงพยาบาลรามาธิบดี มหาวิทยาลัยมหิดล และเรากำลังสร้างคนที่จะพลิกโฉมระบบสุขภาพไทยจากภายใน")}</p>
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
        '<div class="rows">' +
        row("01", bi("Clinic first", "คลินิกมาก่อน"), bi("Every project starts from a real clinical question, with a clinician in the room. Technology serves care, never the other way around.", "ทุกโปรเจกต์เริ่มจากคำถามทางคลินิกจริง โดยมีแพทย์อยู่ในทีม เทคโนโลยีรับใช้การดูแลผู้ป่วย ไม่ใช่ทางกลับกัน")) +
        row("02", bi("Governance as a material", "ธรรมาภิบาลเป็นวัสดุในการสร้าง"), bi("Safety, evaluation, privacy, and regulation are part of how we build, present from the first design decision, not bolted on at the end.", "ความปลอดภัย การประเมินผล ความเป็นส่วนตัว และกฎระเบียบ เป็นส่วนหนึ่งของการสร้างตั้งแต่การตัดสินใจออกแบบครั้งแรก ไม่ใช่มาแปะทีหลัง")) +
        row("03", bi("Build to learn", "เรียนรู้ด้วยการลงมือสร้าง"), bi("We learn by shipping. Reviewed work, real deployment, measured outcomes. Lectures support the build, not the other way around.", "เราเรียนรู้ด้วยการส่งงานจริง งานที่ผ่านการรีวิว การนำไปใช้จริง และผลลัพธ์ที่วัดได้ การบรรยายสนับสนุนการสร้าง ไม่ใช่ทางกลับกัน")) +
        row("04", bi("Open where we can, selective where it counts", "เปิดกว้างเท่าที่ทำได้ คัดสรรในจุดที่สำคัญ"), bi("The Academy is open to anyone in Thailand. The Fellowship is small on purpose, so depth is possible.", "อคาเดมีเปิดให้ทุกคนในประเทศไทย เฟลโลว์ชิปตั้งใจให้เล็ก เพื่อให้เกิดความลึกได้จริง")) +
        row("05", bi("Of the system, for the system", "จากระบบ เพื่อระบบ"), bi("We design to plug into the national health agenda, so the people we train have a country ready to receive them.", "เราออกแบบให้เชื่อมกับวาระสุขภาพของชาติ เพื่อให้คนที่เราฝึกมีประเทศที่พร้อมรองรับ")) +
        '</div>')

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
      <div class="stack">
        <div class="card reveal"><h3>{bi("Universities", "มหาวิทยาลัย")}</h3><p>{bi("Deep theory, little deployment. Knowledge that rarely reaches a ward.", "ทฤษฎีลึก แต่แทบไม่ได้นำไปใช้ ความรู้ที่ไม่ค่อยไปถึงหอผู้ป่วย")}</p></div>
        <div class="card reveal" data-d="1"><h3>{bi("Startups", "สตาร์ตอัป")}</h3><p>{bi("Fast deployment, thin clinical grounding, no teaching mandate.", "นำไปใช้เร็ว แต่รากฐานทางคลินิกบาง และไม่มีพันธกิจการสอน")}</p></div>
        <div class="card reveal" data-d="2"><h3>{bi("Vendors", "ผู้ขายเทคโนโลยี")}</h3><p>{bi("Finished products, no capability left behind in the institution.", "ผลิตภัณฑ์สำเร็จรูป แต่ไม่ทิ้งขีดความสามารถไว้ในสถาบัน")}</p></div>
        <div class="card reveal" data-d="3" style="border-color:var(--accent)"><h3 class="gradient-text">{bi("The Club", "คลับของเรา")}</h3><p>{bi("Clinical depth, real deployment, and a workforce produced on the way. All three, in one place.", "ความลึกทางคลินิก การนำไปใช้จริง และกำลังคนที่เกิดขึ้นระหว่างทาง ครบทั้งสามในที่เดียว")}</p></div>
      </div>
    </div>
  </div>
</section>"""

    eco = sec(
        head(bi("Where we fit nationally", "เราอยู่ตรงไหนในระดับชาติ"), bi("Designed to plug into Thailand's health agenda.", "ออกแบบให้เสียบเข้ากับวาระสุขภาพของไทย"),
             bi("We do not work around the system. We build toward the goals the country has already set, so our graduates and tools have a place to go.", "เราไม่ได้ทำงานเลี่ยงระบบ เราสร้างไปในทิศทางเป้าหมายที่ประเทศตั้งไว้แล้ว เพื่อให้ผู้จบและเครื่องมือของเรามีที่ไป")) +
        '<div class="grid grid-3">' +
        ctx['card']('shield', 'Ministry of Public Health', 'The MOPH Digital Health agenda sets the direction for a connected, data-driven health system. We train the workforce that direction requires.', None, '', prefix) +
        ctx['card']('users', 'NHSO', 'The National Health Security Office runs universal coverage. AI that improves access and efficiency has to meet its real-world constraints.', None, '', prefix) +
        ctx['card']('doc', 'Thai FDA', 'Medical AI is regulated as Software as a Medical Device. We teach to that standard so what we build can be approved and trusted.', None, '', prefix) +
        ctx['card']('rocket', 'NIA', 'The National Innovation Agency backs the move from research to venture. Our studio is built to meet it.', None, '', prefix) +
        ctx['card']('node', 'Thai HealthTech', 'A growing ecosystem of health technology companies and associations. We supply it talent and partners.', None, '', prefix) +
        ctx['card']('pulse', 'Accredited education', 'We hold to the standard set by bodies like the AMA Ed Hub for clinician-facing AI education, adapted for Thailand.', None, '', prefix) +
        '</div>')

    partners = sec(
        head(bi("Partners", "พันธมิตร"), bi("We do not build alone.", "เราไม่ได้สร้างเพียงลำพัง"),
             bi("We work with the people who train builders and ship technology, and we align with the bodies that set Thailand's health agenda.", "เราทำงานร่วมกับผู้ที่ฝึกคนสร้างและส่งมอบเทคโนโลยี และเชื่อมกับหน่วยงานที่กำหนดวาระสุขภาพของไทย")) +
        '<div class="grid grid-2">' +
        ctx['card']('node', 'Google Developer Groups on Campus', bi('A community of student developers and the Google Cloud and AI tooling our hands-on work runs on. Our Basics and Deployment domains lean on this stack.', 'ชุมชนนักพัฒนานักศึกษา และเครื่องมือ Google Cloud และ AI ที่งานภาคปฏิบัติของเราใช้ โดเมน Basics และ Deployment ของเราพึ่งพาชุดเครื่องมือนี้'), None, '', prefix) +
        ctx['card']('users', 'BOTNOI Academy', bi('A Thai leader in AI education and voice technology. A natural partner for the speech and language parts of the curriculum, taught for Thai data.', 'ผู้นำไทยด้านการศึกษา AI และเทคโนโลยีเสียง เป็นพันธมิตรที่เหมาะกับส่วน speech และภาษาในหลักสูตร ที่สอนบนข้อมูลภาษาไทย'), None, '', prefix) +
        '</div>' +
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
    <span class="eyebrow reveal">{bi("What we do", "สิ่งที่เราทำ")}</span>
    <h1 class="reveal" data-d="1" style="max-width:18ch">{bi("One pipeline, from first principles to the patient.", "หนึ่งเส้นทาง จากพื้นฐานสู่ผู้ป่วย")}</h1>
    <p class="lead reveal measure" data-d="2">{bi("Learn the craft, prove it on real problems, turn the best of it into products, and help institutions stand up their own capability. Four parts that feed each other.", "เรียนวิชาชีพ พิสูจน์บนโจทย์จริง เปลี่ยนงานที่ดีที่สุดให้เป็นผลิตภัณฑ์ และช่วยสถาบันสร้างขีดความสามารถของตนเอง สี่ส่วนที่ป้อนกันและกัน")}</p>
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
        (bi("Venture Studio", "เวนเจอร์สตูดิโอ"), "rocket", bi("Turn work into product", "เปลี่ยนงานเป็นผลิตภัณฑ์"), "fellowship.html", bi("Build with us", "สร้างไปกับเรา"),
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
        '<div class="steps">' +
        step("Step 01", bi("Learn", "เรียน"), bi("Start in the Academy. Build the foundations and the clinical context, free and at your own pace.", "เริ่มที่อคาเดมี สร้างพื้นฐานและบริบททางคลินิก ฟรีและตามจังหวะของคุณเอง")) +
        step("Step 02", bi("Apply", "สมัคร"), bi("Bring a real problem to the Fellowship, or join a project team. Get matched with a mentor and supervised data.", "นำโจทย์จริงมาที่เฟลโลว์ชิป หรือเข้าร่วมทีมโปรเจกต์ จับคู่กับเมนเทอร์และข้อมูลที่มีการกำกับ")) +
        step("Step 03", bi("Build", "สร้าง"), bi("Ship a reviewed, evaluated tool into a real clinical workflow. Governance and safety are part of the grade.", "ส่งเครื่องมือที่ผ่านการรีวิวและประเมิน เข้าสู่เวิร์กโฟลว์คลินิกจริง ธรรมาภิบาลและความปลอดภัยเป็นส่วนหนึ่งของการวัดผล")) +
        step("Step 04", bi("Scale", "ขยายผล"), bi("If it deserves to live, the studio helps it become a product, with a regulatory and market path.", "หากมันคู่ควรที่จะอยู่ต่อ สตูดิโอช่วยให้มันกลายเป็นผลิตภัณฑ์ พร้อมเส้นทางกฎระเบียบและตลาด")) +
        '</div>')

    return hero + parts + method

def step(k, title, body):
    return (f'<div class="step reveal"><div class="step__k">{k}</div>'
            f'<div><h3>{title}</h3><p class="mt2">{body}</p></div></div>')

# ===========================================================================
# ACADEMY (public overview)
# ===========================================================================
def academy(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:3rem">
  <div class="hero__glow"></div>
  <div class="container">
    <span class="eyebrow reveal">{bi("The Academy", "อคาเดมี")}</span>
    <h1 class="reveal" data-d="1" style="max-width:19ch">{bi("The open curriculum for medical AI in Thailand.", "หลักสูตรเปิดด้าน AI การแพทย์ สำหรับประเทศไทย")}</h1>
    <p class="lead reveal measure" data-d="2">{bi("From what a model is to how it reaches a patient safely. Free to start, taught with real clinical data and real code. Open to clinicians, students, and engineers alike.", "ตั้งแต่โมเดลคืออะไร ไปจนถึงการนำไปสู่ผู้ป่วยอย่างปลอดภัย เริ่มเรียนฟรี สอนด้วยข้อมูลคลินิกจริงและโค้ดจริง เปิดสำหรับแพทย์ นักศึกษา และวิศวกรเท่าเทียมกัน")}</p>
    <div class="btn-row reveal" data-d="3">
      <a class="btn btn--grad btn--lg" href="{prefix}academy/gate.html">{bi("Enter the Academy", "เข้าสู่อคาเดมี")} {I['arrow']}</a>
      <a class="btn btn--ghost btn--lg" href="{prefix}fellowship.html">{bi("Or apply for the Fellowship", "หรือสมัครเฟลโลว์ชิป")}</a>
    </div>
    <p class="muted mt4" style="font-size:.85rem">{I['lock']} {bi("Curriculum is open to enrolled members. Ask your programme lead for the access code.", "หลักสูตรเปิดสำหรับสมาชิกที่ลงทะเบียน ขอรหัสเข้าใช้งานจากผู้ดูแลโปรแกรมของคุณ")}</p>
  </div>
</section>"""

    modules = sec(
        head(bi("The curriculum", "หลักสูตร"), bi("Six tracks, one through-line.", "หกโดเมน หนึ่งเส้นทางเชื่อมโยง"),
             bi("Each track is hands-on. You write code, read clinical data, and build something that runs. Notebooks open in the browser or in Colab.", "ทุกโดเมนเน้นลงมือทำ คุณเขียนโค้ด อ่านข้อมูลคลินิก และสร้างสิ่งที่รันได้จริง เปิด notebook ในเบราว์เซอร์หรือใน Colab")) +
        '<div class="grid grid-3">' +
        ctx['card']('brain', bi('Foundations', 'พื้นฐาน'), bi('What AI and machine learning are, how to think about them, datasets, and how to evaluate a model honestly.', 'AI และ machine learning คืออะไร คิดกับมันอย่างไร datasets และการประเมินโมเดลอย่างตรงไปตรงมา'), None, '', prefix) +
        ctx['card']('pulse', bi('Clinical AI', 'AI ทางคลินิก'), bi('Applying models to real clinical tasks: risk prediction, triage, and decision support, with the pitfalls named.', 'นำโมเดลไปใช้กับงานคลินิกจริง การทำนายความเสี่ยง การคัดกรอง และ decision support พร้อมชี้กับดักที่ต้องระวัง'), None, '', prefix) +
        ctx['card']('doc', bi('Health Data and FHIR', 'ข้อมูลสุขภาพและ FHIR'), bi('HIS, EMR, HL7 and FHIR. How health data actually moves, and how to build on it.', 'HIS, EMR, HL7 และ FHIR ข้อมูลสุขภาพเคลื่อนที่จริงอย่างไร และสร้างงานบนมันอย่างไร'), None, '', prefix) +
        ctx['card']('node', bi('Medical Imaging', 'ภาพทางการแพทย์'), bi('Computer vision for radiology and pathology, from preprocessing to a working classifier.', 'Computer vision สำหรับรังสีวิทยาและพยาธิวิทยา ตั้งแต่ preprocessing จนถึง classifier ที่ใช้ได้'), None, '', prefix) +
        ctx['card']('rocket', bi('Agents and Deep AI', 'Agents และ Deep AI'), bi('Modern deep learning and agentic systems, and where they help or harm in a clinical setting.', 'deep learning สมัยใหม่และ agentic systems และจุดที่มันช่วยหรือทำร้ายในบริบทคลินิก'), None, '', prefix) +
        ctx['card']('shield', bi('Deployment and Governance', 'Deployment และธรรมาภิบาล'), bi('Shipping safely: evaluation, monitoring, privacy, and the Software as a Medical Device pathway.', 'การส่งมอบอย่างปลอดภัย การประเมิน การติดตาม ความเป็นส่วนตัว และเส้นทาง Software as a Medical Device'), None, '', prefix) +
        '</div>')

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
    <span class="eyebrow reveal">{bi("The Fellowship", "เฟลโลว์ชิป")}</span>
    <h1 class="reveal" data-d="1" style="max-width:17ch">{bi("A year to build something that reaches a patient.", "หนึ่งปี เพื่อสร้างสิ่งที่ไปถึงผู้ป่วย")}</h1>
    <p class="lead reveal measure" data-d="2">{bi("The Fellowship is small on purpose. A handful of people, real clinical problems, supervised data, and the faculty of Ramathibodi behind them. You leave with a deployed tool and the judgement to build more.", "เฟลโลว์ชิปตั้งใจให้เล็ก คนไม่กี่คน โจทย์คลินิกจริง ข้อมูลที่มีการกำกับ และคณาจารย์รามาธิบดีหนุนหลัง คุณจากไปพร้อมเครื่องมือที่ deploy แล้ว และวิจารณญาณที่จะสร้างต่อ")}</p>
    <div class="btn-row reveal" data-d="3">
      <a class="btn btn--grad btn--lg" href="{prefix}fellowship/apply.html">{bi("Apply", "สมัคร")} {I['arrow']}</a>
      <a class="btn btn--ghost btn--lg" href="{prefix}fellowship/stories.html">{bi("Read fellow stories", "อ่านเรื่องราวเฟลโลว์")}</a>
    </div>
  </div>
</section>"""

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
        '<div class="rows">' +
        row("Clinical AI", bi("Decision support and risk", "decision support และความเสี่ยง"), bi("Models that help clinicians decide, evaluated against real outcomes and real workflows.", "โมเดลที่ช่วยแพทย์ตัดสินใจ ประเมินเทียบกับผลลัพธ์จริงและเวิร์กโฟลว์จริง")) +
        row("Imaging", bi("Vision for diagnosis", "vision เพื่อการวินิจฉัย"), bi("Radiology and pathology tools, from data pipeline to a validated, deployable model.", "เครื่องมือด้านรังสีวิทยาและพยาธิวิทยา ตั้งแต่ data pipeline จนถึงโมเดลที่ตรวจสอบและ deploy ได้")) +
        row("Health Data", bi("FHIR and interoperability", "FHIR และ interoperability"), bi("The plumbing of a modern health system, and the AI that rides on top of it.", "ระบบท่อของระบบสุขภาพสมัยใหม่ และ AI ที่ทำงานอยู่บนมัน")) +
        row("Agents", bi("Operational intelligence", "ปัญญาด้านปฏิบัติการ"), bi("Agentic systems for the administrative and operational load that slows care down.", "agentic systems สำหรับภาระงานธุรการและปฏิบัติการที่ทำให้การดูแลช้าลง")) +
        '</div>' +
        f'<div class="btn-row mt5 reveal"><a class="btn btn--ghost" href="{prefix}fellowship/apply.html">{bi("See eligibility and apply", "ดูคุณสมบัติและสมัคร")} {I["arrow"]}</a></div>')

    links = sec(
        '<div class="grid grid-3">' +
        ctx['card']('doc', bi('Publications', 'ผลงานตีพิมพ์'), bi('Papers, technical reports, and open releases from fellows and the club.', 'บทความ รายงานเทคนิค และการเผยแพร่แบบเปิดจากเฟลโลว์และคลับ'), 'fellowship/publications.html', bi('Read', 'อ่าน'), prefix) +
        ctx['card']('users', bi('Stories', 'เรื่องราว'), bi('How fellows chose their problem and what they built.', 'เฟลโลว์เลือกโจทย์อย่างไร และสร้างอะไรขึ้นมา'), 'fellowship/stories.html', bi('Read', 'อ่าน'), prefix) +
        ctx['card']('compass', bi('FAQ', 'คำถามที่พบบ่อย'), bi('Eligibility, time commitment, funding, and how selection works.', 'คุณสมบัติ เวลาที่ต้องใช้ ทุน และการคัดเลือกทำงานอย่างไร'), 'fellowship/faq.html', bi('Read', 'อ่าน'), prefix) +
        '</div>')

    return hero + quote + pillars + tracks + links

def fellowship_apply(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">Apply</span>
  <h1 class="reveal" data-d="1" style="max-width:16ch">Tell us the problem you want to solve.</h1>
  <p class="lead reveal measure" data-d="2">We select for judgement and drive more than for a perfect resume. If you can hold a clinical problem and a technical one at once, we want to read your application.</p>
</div></section>"""
    who = sec(
        head("Who should apply", "Three kinds of people, one room.") +
        '<div class="grid grid-3">' +
        ctx['card']('pulse', 'Clinicians', 'Doctors, nurses, and allied health staff who see the problems daily and want to build the fix.', None, '', prefix) +
        ctx['card']('node', 'Engineers and scientists', 'Software, data, and ML people who want their work to matter in a clinic.', None, '', prefix) +
        ctx['card']('brain', 'Students', 'Advanced students from medicine, engineering, and data science ready for real responsibility.', None, '', prefix) +
        '</div>')
    how = sec(
        head("How selection works", "Four steps, no theatre.") +
        '<div class="steps">' +
        step("01", "Apply", "Send a short application and the problem you care about. No long forms.") +
        step("02", "Conversation", "A focused conversation about your problem, your background, and fit.") +
        step("03", "Scoping", "We shape your problem into a project with a mentor and a data plan.") +
        step("04", "Cohort", "Join the cohort, get access, and start building under supervision.") +
        '</div>' +
        f'<div class="btn-row mt5 reveal"><a class="btn btn--grad btn--lg" href="{prefix}contact.html">Start your application {I["arrow"]}</a><a class="btn btn--ghost btn--lg" href="{prefix}fellowship/faq.html">Read the FAQ</a></div>')
    return hero + who + how

def fellowship_stories(prefix, ctx):
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">Stories</span>
  <h1 class="reveal" data-d="1" style="max-width:16ch">The work, in the words of the people who built it.</h1>
  <p class="lead reveal measure" data-d="2">Profiles of fellows and their projects will be published here as cohorts complete. The shape is always the same: a real problem, a hard build, a tool in use.</p>
</div></section>"""
    grid = sec(
        '<div class="grid grid-3">' +
        entry("Story", "From ward round to working model", "How a resident turned a daily frustration into a deployed risk tool. Coming soon.", prefix + "fellowship/stories.html", "a") +
        entry("Story", "Reading scans, faster and safer", "An imaging fellow's path from dataset to a validated classifier. Coming soon.", prefix + "fellowship/stories.html", "b") +
        entry("Story", "Making the data speak FHIR", "Building the interoperability layer a department had been missing. Coming soon.", prefix + "fellowship/stories.html", "c") +
        '</div>')
    return hero + grid

def fellowship_publications(prefix, ctx):
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">Publications</span>
  <h1 class="reveal" data-d="1" style="max-width:16ch">What we learn, we publish.</h1>
  <p class="lead reveal measure" data-d="2">Papers, technical reports, datasets, and open-source releases from the club and its fellows. We share methods and evidence so the whole Thai ecosystem moves faster.</p>
</div></section>"""
    rows = sec(
        '<div class="rows">' +
        row("2026", "Evaluation practices for clinical AI in Thai hospitals", "A practical framework for honest evaluation before deployment. In preparation.") +
        row("2026", "FHIR adoption patterns in Thai EMR systems", "What we found building on real hospital data. In preparation.") +
        row("Open", "DHA teaching notebooks", "The Academy's hands-on notebooks, released openly for educators.") +
        '</div>')
    return hero + rows

def fellowship_faq(prefix, ctx):
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">FAQ</span>
  <h1 class="reveal" data-d="1" style="max-width:16ch">Questions, answered plainly.</h1>
</div></section>"""
    qa = [
        ("Who can apply to the Fellowship?", "Clinicians, engineers, scientists, and advanced students based in Thailand or able to be in residence at Ramathibodi. You do not need to be from Ramathibodi to apply."),
        ("Do I need to be a strong programmer?", "You need to be able to learn fast and build. The Academy gives you the foundations. Clinicians without a coding background have a pathway in."),
        ("How long is the Fellowship?", "It runs as a cohort across roughly a year, ending in a deployed, evaluated project. Exact dates are published each intake."),
        ("Is it full time?", "It is designed for serious commitment. We work with clinical schedules where we can, but the build is real and takes real hours."),
        ("Is there funding?", "Funding and support vary by cohort and partner. Details are shared during the conversation stage so there are no surprises."),
        ("What is the difference between the Academy and the Fellowship?", "The Academy is open and teaches the craft. The Fellowship is selective and is where you prove it on a real clinical problem with data and mentorship."),
        ("Who owns what I build?", "Arrangements are set out clearly before you start, balancing your credit, patient safety, and the institution's responsibilities. Nothing is hidden."),
    ]
    items = "".join(
        f'<details class="row reveal" style="display:block"><summary style="cursor:pointer;font-family:var(--font-display);font-weight:700;font-size:var(--step-1)">{q}</summary>'
        f'<p class="mt3">{a}</p></details>' for q, a in qa)
    return hero + sec(f'<div class="rows">{items}</div>')

# ===========================================================================
# INSIGHTS + NEWS
# ===========================================================================
INSIGHT_ARTICLES = {
    "governance-as-design": ("Field note", "Governance is a design material, not a checkpoint",
        """Most teams treat governance as the gate at the end: build the model, then ask whether it is safe, private, and allowed. By then the important decisions are already made and hard to undo.

We teach the opposite. Evaluation, privacy, and the regulatory frame are materials you build with, present from the first design decision. When a fellow chooses a clinical problem, we ask how success will be measured and how failure will be caught before a single line of code is written.

This is slower at the start and far faster overall. A tool designed to be evaluated is a tool that can be trusted, approved, and deployed. A tool that bolts evaluation on at the end usually cannot."""),
    "fhir-in-plain-language": ("Explainer", "FHIR, in plain language",
        """If you want to build clinical AI in Thailand, you will meet FHIR quickly. It is the modern standard for how health data is described and exchanged, and it is the difference between a model that runs on one hospital's export and a model that travels.

FHIR breaks health information into resources: a Patient, an Observation, a Condition, a Medication. Each has a defined shape, so a blood pressure reading from one system looks like a blood pressure reading from another. That sounds dull. It is the whole game. Interoperability is what lets a tool built at Ramathibodi work elsewhere.

In the Academy you do not just read about FHIR. You parse it, build on it, and feel where real hospital data is messy in ways the spec does not warn you about."""),
    "train-builders-not-buyers": ("Position", "Why Thailand should train builders, not just buyers",
        """A country can get AI into its hospitals two ways. It can buy finished products from abroad, or it can grow people who build and run their own. Both have a place. Only one builds lasting capability.

When you buy, you get a tool and a dependency. The vendor holds the knowledge, the updates, and the leverage. When the context shifts, and in medicine it always shifts, you wait. When you build, the capability stays in the institution and compounds.

This is why we exist inside a hospital and not beside one. The national agenda, through the Ministry of Public Health, the NHSO, the Thai FDA, and the NIA, points the same way: a health system that can build for itself. That needs a workforce. Producing it is the work."""),
}

def insights_index(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">Insights</span>
  <h1 class="reveal" data-d="1" style="max-width:16ch">Thinking from inside the work.</h1>
  <p class="lead reveal measure" data-d="2">Field notes, explainers, and positions on building medical AI that a health system can trust. Written by the people doing it.</p>
</div></section>"""
    cards = ""
    tone = ["b", "a", "c"]
    for i, (slug, (meta, title, _)) in enumerate(INSIGHT_ARTICLES.items()):
        cards += entry(meta, title, "", prefix + f"insights/{slug}.html", tone[i % 3])
    feat = sec('<div class="grid grid-3">' + cards + '</div>')
    news = sec(
        head("From the newsroom", "Announcements and milestones.") +
        '<div class="rows">' +
        row("News", "The club, in public", "Launches, cohorts, partnerships, and events as they happen.") +
        '</div>' +
        f'<div class="btn-row mt4 reveal"><a class="btn btn--ghost" href="{prefix}news/index.html">All news {I["arrow"]}</a></div>')
    return hero + feat + news

def insight_article(slug):
    meta, title, body = INSIGHT_ARTICLES[slug]
    paras = "".join(f"<p>{p.strip()}</p>" for p in body.split("\n\n"))
    def fn(prefix, ctx):
        I = ctx["ICON"]
        return f"""
<section class="section">
  <div class="container">
    <div class="crumb"><a href="{prefix}insights/index.html">Insights</a> / {meta}</div>
    <div style="max-width:70ch">
      <span class="eyebrow reveal">{meta}</span>
      <h1 class="reveal mt3" data-d="1">{title}</h1>
    </div>
    {frame(title, "ratio-16x9", "b")}
    <article class="prose reveal" style="margin-top:2.5rem">{paras}</article>
    <div class="btn-row" style="margin-top:3rem"><a class="btn btn--ghost" href="{prefix}insights/index.html">{I['arrow']} All insights</a></div>
  </div>
</section>"""
    return fn

def news_index(prefix, ctx):
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">News</span>
  <h1 class="reveal" data-d="1" style="max-width:16ch">What is happening at the club.</h1>
  <p class="lead reveal measure" data-d="2">Launches, cohorts, partnerships, and events. The record of a club finding its feet in public.</p>
</div></section>"""
    items = sec(
        '<div class="rows">' +
        news_row("July 2026", "The club goes public", "The Ramathibodi Digital Health and AI Club launches its site, its Academy, and its first call for fellows.") +
        news_row("Soon", "First Academy cohort opens", "Enrolment for the open curriculum opens to clinicians, students, and engineers across Thailand.") +
        news_row("Soon", "Fellowship intake", "Applications open for the first in-residence fellowship cohort.") +
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
          <div class="field"><label>{bi("Name", "ชื่อ")}</label><input type="text" required placeholder="{bi('Your name', 'ชื่อของคุณ')}"/></div>
          <div class="field"><label>{bi("Email", "อีเมล")}</label><input type="email" required placeholder="you@hospital.org"/></div>
          <div class="field"><label>{bi("I want to", "ฉันต้องการ")}</label><input type="text" placeholder="{bi('learn / apply / partner / hire', 'เรียน / สมัคร / เป็นพันธมิตร / จ้าง')}"/></div>
          <div class="field"><label>{bi("Message", "ข้อความ")}</label><input type="text" placeholder="{bi('A sentence about what you have in mind', 'ประโยคเดียวเกี่ยวกับสิ่งที่คุณคิดไว้')}"/></div>
          <div class="gate__msg" style="color:var(--accent)"></div>
          <div class="btn-row mt3"><button class="btn btn--grad btn--lg" type="submit">{bi("Send", "ส่ง")} {I['arrow']}</button></div>
        </form>
      </div>
    </div>
  </div>
</section>"""
    return body

# ===========================================================================
# PLATFORM / MARKETPLACE
# ===========================================================================
def platform(prefix, ctx):
    I = ctx["ICON"]
    hero = f"""
<section class="hero" style="padding-bottom:2rem"><div class="hero__glow"></div><div class="container">
  <span class="eyebrow reveal">{bi("The Platform", "แพลตฟอร์ม")}</span>
  <h1 class="reveal" data-d="1" style="max-width:18ch">{bi("Where problems, data, and people find each other.", "ที่ที่โจทย์ ข้อมูล และคนมาเจอกัน")}</h1>
  <p class="lead reveal measure" data-d="2">{bi("One place to post a real clinical problem, find the dataset to work on it, benchmark your model, and match with the team or mentor who can help. This is the connective tissue of the club.", "พื้นที่เดียวสำหรับโพสต์โจทย์จริงจากคลินิก ค้นหาชุดข้อมูลเพื่อลงมือทำ วัดผลโมเดลของคุณ และจับคู่กับทีมหรือเมนเทอร์ที่ช่วยได้ นี่คือเนื้อเยื่อที่เชื่อมคลับเข้าด้วยกัน")}</p>
</div></section>"""

    tiles = sec(
        '<div class="grid grid-4">' +
        ctx['card']('doc', bi('Dataset marketplace', 'ตลาดชุดข้อมูล'), bi('Governed, de-identified datasets to learn and build on.', 'ชุดข้อมูลที่กำกับดูแลและลบตัวตนแล้ว สำหรับเรียนรู้และสร้างงาน'), None, '', prefix) +
        ctx['card']('flask', bi('Task board', 'กระดานโจทย์'), bi('Real clinical problems posted by departments, waiting for a builder.', 'โจทย์จริงจากคลินิกที่หน่วยงานโพสต์ไว้ รอคนมาลงมือทำ'), None, '', prefix) +
        ctx['card']('pulse', bi('Model leaderboard', 'ลีดเดอร์บอร์ดโมเดล'), bi('Benchmark models on shared tasks, in the open, honestly.', 'วัดผลโมเดลบนโจทย์กลางอย่างเปิดเผยและตรงไปตรงมา'), None, '', prefix) +
        ctx['card']('users', bi('Matching', 'จับคู่'), bi('Match people to teams, mentors, and problems.', 'จับคู่คนเข้ากับทีม เมนเทอร์ และโจทย์'), None, '', prefix) +
        '</div>')

    # Dataset marketplace
    datasets = f"""
<section class="section">
  <div class="container">
    {head(bi("Dataset marketplace", "ตลาดชุดข้อมูล"), bi("Data you can actually learn on.", "ข้อมูลที่คุณเรียนรู้ได้จริง"), bi("Governed and de-identified, released under clear terms and a PDPA basis. You never touch raw patient data without supervision.", "กำกับดูแลและลบตัวตนแล้ว เผยแพร่ภายใต้เงื่อนไขที่ชัดเจนและฐานทางกฎหมาย PDPA คุณจะไม่แตะข้อมูลผู้ป่วยดิบโดยไม่มีการกำกับ"))}
    <div class="rows">
      {ds_row("Thai Clinical Tabular", "Tabular", bi("De-identified labs, vitals, and outcomes for risk modelling.", "แล็บ สัญญาณชีพ และผลลัพธ์ที่ลบตัวตนแล้ว สำหรับสร้างโมเดลความเสี่ยง"), "Open")}
      {ds_row("Chest X-ray (teaching set)", "Image", bi("Curated radiographs with labels, for imaging practice.", "ภาพเอกซเรย์ทรวงอกที่คัดสรรพร้อมป้ายกำกับ สำหรับฝึกงานภาพ"), "Open")}
      {ds_row("Thai Clinical Notes (synthetic)", "Text", bi("Synthetic Thai clinical text for NLP without privacy risk.", "ข้อความคลินิกภาษาไทยสังเคราะห์ สำหรับงาน NLP โดยไม่มีความเสี่ยงด้านความเป็นส่วนตัว"), "Open")}
      {ds_row("ECG Rhythm Strips", "Signal", bi("Labelled ECG segments for signal model practice.", "สัญญาณ ECG พร้อมป้ายกำกับ สำหรับฝึกโมเดลสัญญาณ"), "On request")}
    </div>
    <p class="muted mt4 reveal" style="font-size:.88rem">{bi("Every dataset lists its source, its licence, and the lawful basis for use. Access to sensitive sets is supervised.", "ทุกชุดข้อมูลระบุแหล่งที่มา สัญญาอนุญาต และฐานทางกฎหมายในการใช้งาน การเข้าถึงข้อมูลอ่อนไหวจะมีการกำกับดูแล")}</p>
  </div>
</section>"""

    # Task board
    tasks = sec(
        head(bi("Task board", "กระดานโจทย์"), bi("Real problems, waiting for you.", "โจทย์จริง ที่รอคุณอยู่"), bi("Departments post problems worth solving. Pick one, form a team, and build it as an Academy project or a Fellowship.", "หน่วยงานโพสต์โจทย์ที่ควรแก้ เลือกสักโจทย์ ตั้งทีม แล้วสร้างเป็นโปรเจกต์ในอคาเดมีหรือเฟลโลว์ชิป")) +
        '<div class="rows">' +
        task_row("Emergency", bi("Triage support for the ED", "ระบบช่วยคัดกรองที่ห้องฉุกเฉิน"), bi("Reduce time to prioritise walk-in patients safely.", "ลดเวลาในการจัดลำดับผู้ป่วยที่เดินเข้ามาอย่างปลอดภัย")) +
        task_row("Radiology", bi("Flag urgent chest films", "ตั้งค่าสถานะฟิล์มทรวงอกเร่งด่วน"), bi("Surface likely-abnormal chest X-rays for faster reads.", "ดึงภาพเอกซเรย์ทรวงอกที่น่าจะผิดปกติขึ้นมา เพื่อการอ่านที่เร็วขึ้น")) +
        task_row("Pharmacy", bi("Thai drug interaction assistant", "ผู้ช่วยตรวจปฏิกิริยาระหว่างยาภาษาไทย"), bi("A grounded assistant to check interactions on the ward.", "ผู้ช่วยที่อ้างอิงแหล่งข้อมูล ตรวจปฏิกิริยาระหว่างยาบนหอผู้ป่วย")) +
        task_row("Outpatient", bi("Line follow-up bot", "บอทติดตามอาการผ่าน Line"), bi("Automate preparation and follow-up messages safely.", "ส่งข้อความเตรียมตัวและติดตามอาการอัตโนมัติอย่างปลอดภัย")) +
        '</div>' +
        f'<div class="btn-row mt5 reveal"><a class="btn btn--grad" href="{prefix}contact.html">{bi("Post a problem", "โพสต์โจทย์ของคุณ")} {I["arrow"]}</a><a class="btn btn--ghost" href="{prefix}academy.html">{bi("Pick one up", "รับโจทย์ไปทำ")}</a></div>')

    # Leaderboard
    lb = f"""
<section class="section">
  <div class="container">
    <div class="split">
      <div class="stack reveal">
        <span class="eyebrow">{bi("Open model leaderboard", "ลีดเดอร์บอร์ดโมเดลแบบเปิด")}</span>
        <h2>{bi("Benchmark in the open.", "วัดผลอย่างเปิดเผย")}</h2>
        <p class="lead">{bi("Shared tasks with a fixed test set and honest metrics. Submit a model, see where it stands, and read how the top entries were built. Ranking rewards calibration and fairness, not just accuracy.", "โจทย์กลางที่มีชุดทดสอบตายตัวและตัวชี้วัดที่ตรงไปตรงมา ส่งโมเดล ดูว่ายืนอยู่ตรงไหน และอ่านว่าอันดับต้นสร้างมาอย่างไร การจัดอันดับให้ค่ากับ calibration และความเป็นธรรม ไม่ใช่แค่ความแม่นยำ")}</p>
      </div>
      <div class="card reveal" style="padding:0;overflow:hidden">
        <table class="lb">
          <thead><tr><th>#</th><th>{bi("Team", "ทีม")}</th><th>{bi("Task", "โจทย์")}</th><th>AUROC</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>Ward 7</td><td>Sepsis</td><td>0.86</td></tr>
            <tr><td>2</td><td>RadLab</td><td>CXR</td><td>0.83</td></tr>
            <tr><td>3</td><td>NoteAI</td><td>Coding</td><td>0.81</td></tr>
            <tr><td>4</td><td>VitalsTeam</td><td>Deterioration</td><td>0.79</td></tr>
          </tbody>
        </table>
        <p class="muted" style="padding:.9rem 1.1rem;font-size:.78rem;border-top:1px solid var(--line)">{bi("Illustrative. Live boards open with the first cohort.", "เป็นตัวอย่าง บอร์ดจริงจะเปิดพร้อมรุ่นแรก")}</p>
      </div>
    </div>
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

    # Opportunity board
    jobs = sec(
        head(bi("Opportunity board", "กระดานโอกาส"), bi("Where the work leads.", "ปลายทางของงาน"), bi("Fellowships, research assistant roles, internships, and openings from our partners and the Thai HealthTech ecosystem.", "เฟลโลว์ชิป ผู้ช่วยวิจัย ฝึกงาน และตำแหน่งงานจากพันธมิตรและระบบนิเวศเฮลท์เทคไทย")) +
        '<div class="rows">' +
        task_row(bi("Fellowship", "เฟลโลว์ชิป"), bi("Digital Health & AI Fellow", "เฟลโลว์ด้านสุขภาพดิจิทัลและ AI"), bi("The in-residence programme. Rolling applications.", "โปรแกรมในสถานที่ รับสมัครต่อเนื่อง")) +
        task_row(bi("Research", "วิจัย"), bi("Research assistant, clinical AI", "ผู้ช่วยวิจัย AI ทางคลินิก"), bi("Support live projects with data and evaluation.", "สนับสนุนโปรเจกต์จริงด้านข้อมูลและการประเมินผล")) +
        task_row(bi("Partner", "พันธมิตร"), bi("Roles from GDG and BOTNOI", "ตำแหน่งจาก GDG และ BOTNOI"), bi("Openings shared by our partner network.", "ตำแหน่งงานจากเครือข่ายพันธมิตรของเรา")) +
        '</div>' +
        f'<div class="btn-row mt5 reveal"><a class="btn btn--ghost" href="{prefix}careers.html">{bi("See careers", "ดูตำแหน่งงาน")} {I["arrow"]}</a></div>')

    return hero + tiles + moment("network-people.jpg", prefix, bi("One community, many problems", "หนึ่งชุมชน หลายโจทย์")) + datasets + tasks + lb + matching + jobs

def ds_row(title, kind, desc, status):
    return (f'<div class="row reveal" style="grid-template-columns:1fr auto"><div>'
            f'<h3 style="font-size:var(--step-1)">{title} <span class="pill" style="margin-left:.4rem">{kind}</span></h3>'
            f'<p style="font-size:.95rem;margin-top:.3rem">{desc}</p></div>'
            f'<div class="mono muted" style="font-size:.8rem;white-space:nowrap">{status}</div></div>')

def task_row(tag, title, desc):
    return (f'<div class="row reveal"><div class="row__num">{tag}</div>'
            f'<h3 style="font-size:var(--step-1)">{title}</h3><p style="font-size:.95rem">{desc}</p></div>')

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
        <input type="password" autocomplete="off" placeholder="{bi('Enter your code', 'กรอกรหัสของคุณ')}"/></div>
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
    <span class="eyebrow reveal">Fellowship portal</span>
    <h1 class="reveal mt3" data-d="1" style="max-width:16ch">Welcome back, fellow.</h1>
    <p class="lead reveal measure" data-d="2">This is the private workspace for current fellows and mentors. Cohort resources, project tracking, and data access guides live here.</p>
    <div class="grid grid-3 mt5">
      <div class="card reveal"><h3>Cohort handbook</h3><p>Schedule, expectations, and your mentor pairing.</p></div>
      <div class="card reveal" data-d="1"><h3>Data access</h3><p>How to request and use supervised clinical data safely.</p></div>
      <div class="card reveal" data-d="2"><h3>Project board</h3><p>Track your build, reviews, and deployment milestones.</p></div>
    </div>
    <div class="btn-row mt5">
      <a class="btn btn--ghost" href="{prefix}academy/learn/index.html">Open the curriculum</a>
      <a class="btn btn--ghost" href="{prefix}fellowship.html" data-signout="fellowship">Sign out</a>
    </div>
  </div>
</section>"""

# ===========================================================================
# REGISTER
# ===========================================================================
MARKETING = [
    ("index.html", "Ramathibodi Digital Health & AI Club", "", home),
    ("who-we-are.html", "Who We Are - DHA Club", "who-we-are.html", who_we_are),
    ("what-we-do.html", "What We Do - DHA Club", "what-we-do.html", what_we_do),
    ("academy.html", "Academy - DHA Club", "academy.html", academy),
    ("platform.html", "Platform - DHA Club", "platform.html", platform),
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
for _slug in INSIGHT_ARTICLES:
    MARKETING.append((f"insights/{_slug}.html", f"{INSIGHT_ARTICLES[_slug][1]} - Insights",
                      "insights/index.html", insight_article(_slug)))
