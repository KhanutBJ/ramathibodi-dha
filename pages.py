# -*- coding: utf-8 -*-
"""
Long-form page bodies for the DHA Club venture site.
Voice: plain, confident, human. No em dashes, no middle dots, no filler.
"""

# ---------------------------------------------------------------------------
# small builders
# ---------------------------------------------------------------------------
def sec(inner, cls="section"):
    return f'<section class="{cls}"><div class="container">{inner}</div></section>'

def head(eyebrow, title, sub=None):
    s = f'<p class="lead measure mt3">{sub}</p>' if sub else ""
    return f'<div class="section-head reveal"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2>{s}</div>'

def frame(label, ratio="ratio-16x9", tone="a"):
    # branded abstract media frame (placeholder for real photography / footage)
    grads = {
        "a": "radial-gradient(60% 80% at 20% 10%, rgba(247,98,5,.5), transparent 60%), radial-gradient(60% 80% at 90% 90%, rgba(52,18,209,.55), transparent 60%), #0e1728",
        "b": "radial-gradient(60% 80% at 80% 10%, rgba(88,34,166,.55), transparent 60%), radial-gradient(60% 80% at 10% 90%, rgba(1,0,252,.45), transparent 60%), #0e1728",
        "c": "radial-gradient(70% 90% at 50% 0%, rgba(145,56,110,.5), transparent 60%), #0e1728",
    }
    return (f'<div class="frame reveal"><div class="ratio {ratio}" '
            f'style="background:{grads.get(tone, grads["a"])}">'
            f'<div style="position:absolute;inset:auto auto 1rem 1.2rem;font-family:var(--font-mono);'
            f'font-size:.72rem;letter-spacing:.1em;color:rgba(255,255,255,.7)">{label}</div></div></div>')

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
    <h1 class="reveal" data-d="1">We train the people who will bring <span class="gradient-text">AI to the bedside</span>.</h1>
    <p class="lead reveal measure" data-d="2">A club, an academy, and a fellowship built inside one of Thailand's leading medical schools. We turn clinicians, engineers, and scientists into builders who can take medical AI from idea to patient care, safely.</p>
    <div class="btn-row reveal" data-d="3">
      <a class="btn btn--grad btn--lg" href="{prefix}academy.html">Explore the Academy {I['arrow']}</a>
      <a class="btn btn--ghost btn--lg" href="{prefix}fellowship.html">Apply for the Fellowship</a>
    </div>
    <div class="hero__meta">
      {ctx['stat']('<span class="gradient-text">AI + Medicine</span>', 'One discipline, taught as one')}
      {ctx['stat']('Idea to bedside', 'Build under clinical supervision')}
      {ctx['stat']('Open + selective', 'Academy for all, Fellowship for few')}
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
        head("What we do", "Four parts, one pipeline.",
             "Most programmes teach theory and stop. We carry a person all the way from first principles to a working clinical product, then help the strongest ideas become real.") +
        '<div class="grid grid-2">' +
        ctx['card']('brain', 'Academy', 'An open curriculum in AI and digital health, from foundations to clinical deployment. Free to learn, practical from day one.', 'academy.html', 'Start learning', prefix, 1) +
        ctx['card']('flask', 'Fellowship', 'A selective, in-residence year. Fellows work on real clinical problems with Ramathibodi data, faculty, and patients.', 'fellowship.html', 'See the Fellowship', prefix, 2) +
        ctx['card']('rocket', 'Venture Studio', 'We help the best fellowship work become deployable products, with engineering, regulatory, and go-to-market support.', 'what-we-do.html', 'How it works', prefix, 1) +
        ctx['card']('compass', 'Consulting', 'We advise hospitals and agencies building their own AI capability, so the workforce we train has somewhere to land.', 'what-we-do.html', 'Work with us', prefix, 2) +
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
        head("Insights", "Thinking from the club.") +
        '<div class="grid grid-3">' +
        entry("Field note", "Governance is a design material, not a checkpoint", "Why we teach evaluation and safety as part of building, from the first commit.", prefix + "insights/governance-as-design.html", "b") +
        entry("Explainer", "FHIR, in plain language", "The data standard every clinical AI builder in Thailand should know, and why.", prefix + "insights/fhir-in-plain-language.html", "a") +
        entry("Position", "Why Thailand should train builders, not just buyers", "The case for a homegrown medical AI workforce inside the health system.", prefix + "insights/train-builders-not-buyers.html", "c") +
        '</div>' +
        f'<div class="btn-row mt5 reveal"><a class="btn btn--ghost" href="{prefix}insights/index.html">All insights {I["arrow"]}</a></div>')

    cta = f"""
<section class="section">
  <div class="container center stack reveal">
    <span class="eyebrow" style="justify-content:center">Join us</span>
    <h2 class="measure" style="margin-inline:auto">Two doors in. One mission.</h2>
    <p class="lead measure" style="margin-inline:auto">Learn the craft in the Academy. Prove it in the Fellowship. Either way, you leave able to build medical AI that a hospital will actually use.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn--grad btn--lg" href="{prefix}academy.html">Enter the Academy {I['arrow']}</a>
      <a class="btn btn--ghost btn--lg" href="{prefix}fellowship.html">Apply for the Fellowship</a>
    </div>
  </div>
</section>"""

    return hero + proof + '<hr class="divider"/>' + what + why + band + insights + cta

def entry(meta, title, body, href, tone="a"):
    return (f'<a class="entry reveal" href="{href}">'
            f'{frame(meta, "ratio-4x3", tone)}'
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
    <span class="eyebrow reveal">Who we are</span>
    <h1 class="reveal" data-d="1" style="max-width:18ch">A club with the discipline of an institution and the speed of a startup.</h1>
    <p class="lead reveal measure" data-d="2">We are the Ramathibodi Digital Health and AI Club. We sit inside the Faculty of Medicine Ramathibodi Hospital, Mahidol University, and we are building the people who will modernise Thai healthcare from within.</p>
  </div>
</section>"""

    mv = f"""
<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div class="card card--feature reveal">
        <span class="eyebrow">Mission</span>
        <h2 class="mt3" style="font-size:var(--step-2)">Produce a generation of healthcare builders.</h2>
        <p class="mt3">We train clinicians, engineers, and scientists to design, evaluate, and deploy trustworthy medical AI, and we give them real problems to prove it on. Our measure is not graduates. It is working tools in clinical use.</p>
      </div>
      <div class="card card--feature reveal" data-d="1">
        <span class="eyebrow">Vision</span>
        <h2 class="mt3" style="font-size:var(--step-2)">Every Thai institution staffed to build its own AI.</h2>
        <p class="mt3">A health system where hospitals and agencies do not wait to buy AI from elsewhere, because they have people who can build, vet, and run it responsibly. We want to be the place that workforce comes from.</p>
      </div>
    </div>
  </div>
</section>"""

    values = sec(
        head("How we work", "Five principles we do not bend on.") +
        '<div class="rows">' +
        row("01", "Clinic first", "Every project starts from a real clinical question, with a clinician in the room. Technology serves care, never the other way around.") +
        row("02", "Governance as a material", "Safety, evaluation, privacy, and regulation are part of how we build, present from the first design decision, not bolted on at the end.") +
        row("03", "Build to learn", "We learn by shipping. Reviewed work, real deployment, measured outcomes. Lectures support the build, not the other way around.") +
        row("04", "Open where we can, selective where it counts", "The Academy is open to anyone in Thailand. The Fellowship is small on purpose, so depth is possible.") +
        row("05", "Of the system, for the system", "We design to plug into the national health agenda, so the people we train have a country ready to receive them.") +
        '</div>')

    position = f"""
<section class="section">
  <div class="container">
    {head("Our position", "What no one else is offering, and why it has to be us.")}
    <div class="split">
      <div class="stack reveal">
        <p class="lead">Thailand has talent, data, and a clear national direction. What it lacks is a place that turns clinical insight into deployable AI and trains the next workforce while doing it, inside a hospital.</p>
        <p>Pure universities teach theory without deployment. Pure startups deploy without clinical depth or a teaching mission. Vendors sell finished products and leave no capability behind. We are deliberately the thing in the middle: an academic home with a builder's studio and a fellowship, accountable to patients and to the public health system at the same time.</p>
        <p>That is why this works here and not as a side project somewhere else. We have the clinical reality of Ramathibodi, the academic standing of Mahidol, and a mandate to teach. The result is a pipeline that produces both people and products the country can trust.</p>
      </div>
      <div class="stack">
        <div class="card reveal"><h3>Universities</h3><p>Deep theory, little deployment. Knowledge that rarely reaches a ward.</p></div>
        <div class="card reveal" data-d="1"><h3>Startups</h3><p>Fast deployment, thin clinical grounding, no teaching mandate.</p></div>
        <div class="card reveal" data-d="2"><h3>Vendors</h3><p>Finished products, no capability left behind in the institution.</p></div>
        <div class="card reveal" data-d="3" style="border-color:var(--accent)"><h3 class="gradient-text">The Club</h3><p>Clinical depth, real deployment, and a workforce produced on the way. All three, in one place.</p></div>
      </div>
    </div>
  </div>
</section>"""

    eco = sec(
        head("Where we fit nationally", "Designed to plug into Thailand's health agenda.",
             "We do not work around the system. We build toward the goals the country has already set, so our graduates and tools have a place to go.") +
        '<div class="grid grid-3">' +
        ctx['card']('shield', 'Ministry of Public Health', 'The MOPH Digital Health agenda sets the direction for a connected, data-driven health system. We train the workforce that direction requires.', None, '', prefix) +
        ctx['card']('users', 'NHSO', 'The National Health Security Office runs universal coverage. AI that improves access and efficiency has to meet its real-world constraints.', None, '', prefix) +
        ctx['card']('doc', 'Thai FDA', 'Medical AI is regulated as Software as a Medical Device. We teach to that standard so what we build can be approved and trusted.', None, '', prefix) +
        ctx['card']('rocket', 'NIA', 'The National Innovation Agency backs the move from research to venture. Our studio is built to meet it.', None, '', prefix) +
        ctx['card']('node', 'Thai HealthTech', 'A growing ecosystem of health technology companies and associations. We supply it talent and partners.', None, '', prefix) +
        ctx['card']('pulse', 'Accredited education', 'We hold to the standard set by bodies like the AMA Ed Hub for clinician-facing AI education, adapted for Thailand.', None, '', prefix) +
        '</div>')

    partners = sec(
        head("Partners", "We do not build alone.",
             "We work with the people who train builders and ship technology, and we align with the bodies that set Thailand's health agenda.") +
        '<div class="grid grid-2">' +
        ctx['card']('node', 'Google Developer Groups on Campus', 'A community of student developers and the Google Cloud and AI tooling our hands-on work runs on. Our Basics and Deployment domains lean on this stack.', None, '', prefix) +
        ctx['card']('users', 'BOTNOI Academy', 'A Thai leader in AI education and voice technology. A natural partner for the speech and language parts of the curriculum, taught for Thai data.', None, '', prefix) +
        '</div>' +
        '<p class="muted mt4 reveal" style="font-size:.9rem">We design to align with the Ministry of Public Health digital health agenda, the National Health Security Office, the Thai FDA pathway for Software as a Medical Device, the National Innovation Agency, and the Thai HealthTech ecosystem.</p>')

    consulting = f"""
<section class="section">
  <div class="container">
    <div class="band reveal">
      <div class="band__glow"></div>
      <div class="container" style="padding-block:clamp(3rem,6vw,5rem)">
        <div class="split">
          <div class="stack">
            <span class="eyebrow" style="color:#cbd5ef">Innovation consulting</span>
            <h2>An innovation partner for the next-generation healthcare workforce.</h2>
            <p>Beyond teaching and the fellowship, we advise hospitals, agencies, and health technology companies that are standing up their own AI capability. We design teams, governance, and training programmes, so the people we train have strong places to land and the system gains capability it keeps. This is how a club becomes infrastructure.</p>
            <div class="btn-row"><a class="btn btn--grad" href="{prefix}what-we-do.html">How we work {I['arrow']}</a><a class="btn btn--ghost" href="{prefix}contact.html" style="color:#fff;border-color:rgba(255,255,255,.25)">Work with us</a></div>
          </div>
          <div class="grid" style="gap:1rem">
            <div style="display:flex;gap:2rem;flex-wrap:wrap">{ctx['stat']('<span style="color:#fff">Capability design</span>', '<span style="color:#9fb0d4">Teams, not just tools</span>')}</div>
            <div style="display:flex;gap:2rem;flex-wrap:wrap">{ctx['stat']('<span style="color:#fff">Governance</span>', '<span style="color:#9fb0d4">Evaluation and SaMD readiness</span>')}</div>
            <div style="display:flex;gap:2rem;flex-wrap:wrap">{ctx['stat']('<span style="color:#fff">Workforce</span>', '<span style="color:#9fb0d4">Training programmes that stick</span>')}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

    team = sec(
        head("People", "Faculty, builders, and clinicians in one room.",
             "The club brings together attending physicians, machine learning engineers, data scientists, and health policy people. Profiles and the founding team are published as the club grows.") +
        f'<div class="btn-row reveal"><a class="btn btn--ghost" href="{prefix}careers.html">Join the team {I["arrow"]}</a><a class="btn btn--ghost" href="{prefix}contact.html">Partner with us</a></div>')

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
    <span class="eyebrow reveal">What we do</span>
    <h1 class="reveal" data-d="1" style="max-width:16ch">One pipeline, from first principles to the patient.</h1>
    <p class="lead reveal measure" data-d="2">Learn the craft, prove it on real problems, turn the best of it into products, and help institutions stand up their own capability. Four parts that feed each other.</p>
  </div>
</section>"""

    parts = ""
    blocks = [
        ("Academy", "brain", "Learn the craft", "academy.html", "Enter the Academy",
         "An open, practical curriculum in AI and digital health. It runs from what a model is, through clinical data standards like FHIR, medical imaging, and agentic systems, to deployment and governance. Built to be free to start and rigorous enough to matter. Anyone in Thailand can learn here.",
         ["Foundations of AI and machine learning", "Clinical data, HL7 and FHIR, EMR systems", "Medical imaging and clinical NLP", "Evaluation, safety, and deployment"]),
        ("Fellowship", "flask", "Prove it on real problems", "fellowship.html", "See the Fellowship",
         "A selective, in-residence programme for a small cohort. Fellows are placed on genuine clinical problems with Ramathibodi faculty, supervised data access, and patients in view. The output is reviewed work that ships into a real workflow.",
         ["In-residence at Ramathibodi", "Mentored by clinicians and engineers", "Supervised access to clinical data", "Ends in a deployed, evaluated project"]),
        ("Venture Studio", "rocket", "Turn work into product", "fellowship.html", "Build with us",
         "The strongest fellowship and member projects do not stop at a demo. The studio adds engineering, regulatory navigation for Software as a Medical Device, and go-to-market support, in step with the National Innovation Agency's path from research to venture.",
         ["Product engineering and reliability", "Thai FDA SaMD pathway navigation", "Clinical validation and evidence", "Routes to pilot and to market"]),
        ("Consulting", "compass", "Build capability in institutions", "contact.html", "Work with us",
         "We advise hospitals, agencies, and health technology companies setting up their own AI capability. We are an innovation partner for the next generation of the healthcare workforce, so the people we train have strong places to land.",
         ["Capability and team design", "AI governance and evaluation frameworks", "Workforce training programmes", "Project and deployment advisory"]),
    ]
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
      {frame(name + " / Ramathibodi", "ratio-4x3", ["a","b","c","a"][i])}
    </div>
  </div>
</section>"""

    method = sec(
        head("How a person moves through it", "The path is the product.") +
        '<div class="steps">' +
        step("Step 01", "Learn", "Start in the Academy. Build the foundations and the clinical context, free and at your own pace.") +
        step("Step 02", "Apply", "Bring a real problem to the Fellowship, or join a project team. Get matched with a mentor and supervised data.") +
        step("Step 03", "Build", "Ship a reviewed, evaluated tool into a real clinical workflow. Governance and safety are part of the grade.") +
        step("Step 04", "Scale", "If it deserves to live, the studio helps it become a product, with a regulatory and market path.") +
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
    <span class="eyebrow reveal">The Academy</span>
    <h1 class="reveal" data-d="1" style="max-width:17ch">The open curriculum for medical AI in Thailand.</h1>
    <p class="lead reveal measure" data-d="2">From what a model is to how it reaches a patient safely. Free to start, taught with real clinical data and real code. Open to clinicians, students, and engineers alike.</p>
    <div class="btn-row reveal" data-d="3">
      <a class="btn btn--grad btn--lg" href="{prefix}academy/gate.html">Enter the Academy {I['arrow']}</a>
      <a class="btn btn--ghost btn--lg" href="{prefix}fellowship.html">Or apply for the Fellowship</a>
    </div>
    <p class="muted mt4" style="font-size:.85rem">{I['lock']} Curriculum is open to enrolled members. Ask your programme lead for the access code.</p>
  </div>
</section>"""

    modules = sec(
        head("The curriculum", "Six tracks, one through-line.",
             "Each track is hands-on. You write code, read clinical data, and build something that runs. Notebooks open in the browser or in Colab.") +
        '<div class="grid grid-3">' +
        ctx['card']('brain', 'Foundations', 'What AI and machine learning are, how to think about them, datasets, and how to evaluate a model honestly.', None, '', prefix) +
        ctx['card']('pulse', 'Clinical AI', 'Applying models to real clinical tasks: risk prediction, triage, and decision support, with the pitfalls named.', None, '', prefix) +
        ctx['card']('doc', 'Health Data and FHIR', 'HIS, EMR, HL7 and FHIR. How health data actually moves, and how to build on it.', None, '', prefix) +
        ctx['card']('node', 'Medical Imaging', 'Computer vision for radiology and pathology, from preprocessing to a working classifier.', None, '', prefix) +
        ctx['card']('rocket', 'Agents and Deep AI', 'Modern deep learning and agentic systems, and where they help or harm in a clinical setting.', None, '', prefix) +
        ctx['card']('shield', 'Deployment and Governance', 'Shipping safely: evaluation, monitoring, privacy, and the Software as a Medical Device pathway.', None, '', prefix) +
        '</div>')

    fmt = f"""
<section class="section">
  <div class="container">
    <div class="band reveal">
      <div class="band__glow"></div>
      <div class="container" style="padding-block:clamp(3rem,6vw,5rem)">
        <span class="eyebrow" style="color:#cbd5ef">How it runs</span>
        <h2 class="mt3">Read, run, build. In that order.</h2>
        <div class="grid grid-3 mt5">
          <div><div class="stat__num" style="color:#fff">Self-paced</div><p style="color:#9fb0d4" class="mt2">Open the curriculum any time. Notebooks run in the browser or Google Colab.</p></div>
          <div><div class="stat__num" style="color:#fff">Project-based</div><p style="color:#9fb0d4" class="mt2">Every track ends in something you built and can show, not a multiple-choice quiz.</p></div>
          <div><div class="stat__num" style="color:#fff">Pathways</div><p style="color:#9fb0d4" class="mt2">Routes for clinicians and for engineers, meeting in the middle on real cases.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>"""

    cta = f"""
<section class="section">
  <div class="container center stack reveal">
    <h2 class="measure" style="margin-inline:auto">Ready to start building?</h2>
    <p class="lead measure" style="margin-inline:auto">The whole curriculum is one login away.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn--grad btn--lg" href="{prefix}academy/gate.html">Enter the Academy {I['arrow']}</a>
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
    <span class="eyebrow reveal">The Fellowship</span>
    <h1 class="reveal" data-d="1" style="max-width:15ch">A year to build something that reaches a patient.</h1>
    <p class="lead reveal measure" data-d="2">The Fellowship is small on purpose. A handful of people, real clinical problems, supervised data, and the faculty of Ramathibodi behind them. You leave with a deployed tool and the judgement to build more.</p>
    <div class="btn-row reveal" data-d="3">
      <a class="btn btn--grad btn--lg" href="{prefix}fellowship/apply.html">Apply {I['arrow']}</a>
      <a class="btn btn--ghost btn--lg" href="{prefix}fellowship/stories.html">Read fellow stories</a>
    </div>
  </div>
</section>"""

    quote = sec(
        '<blockquote class="prose reveal" style="max-width:30ch;margin-inline:auto;text-align:center;border:0;font-size:var(--step-3);padding:0">'
        '"The point is not to learn about medical AI. The point is to build it, well enough that a hospital will use it."'
        '</blockquote>', "section")

    pillars = sec(
        head("What a fellow gets", "Everything you need to do real work.") +
        '<div class="grid grid-2">' +
        ctx['card']('flask', 'A real problem', 'You are matched to a live clinical question that a department actually wants solved, not a toy dataset.', None, '', prefix) +
        ctx['card']('users', 'Mentorship', 'A clinician and an engineer in your corner, plus a cohort building alongside you.', None, '', prefix) +
        ctx['card']('shield', 'Supervised data', 'Governed access to clinical data, with privacy and evaluation handled the right way.', None, '', prefix) +
        ctx['card']('rocket', 'A route to scale', 'If your work deserves it, the venture studio helps it become a product with a regulatory path.', None, '', prefix) +
        '</div>')

    tracks = sec(
        head("Tracks", "Pick the work, not just the topic.") +
        '<div class="rows">' +
        row("Clinical AI", "Decision support and risk", "Models that help clinicians decide, evaluated against real outcomes and real workflows.") +
        row("Imaging", "Vision for diagnosis", "Radiology and pathology tools, from data pipeline to a validated, deployable model.") +
        row("Health Data", "FHIR and interoperability", "The plumbing of a modern health system, and the AI that rides on top of it.") +
        row("Agents", "Operational intelligence", "Agentic systems for the administrative and operational load that slows care down.") +
        '</div>' +
        f'<div class="btn-row mt5 reveal"><a class="btn btn--ghost" href="{prefix}fellowship/apply.html">See eligibility and apply {I["arrow"]}</a></div>')

    links = sec(
        '<div class="grid grid-3">' +
        ctx['card']('doc', 'Publications', 'Papers, technical reports, and open releases from fellows and the club.', 'fellowship/publications.html', 'Read', prefix) +
        ctx['card']('users', 'Stories', 'How fellows chose their problem and what they built.', 'fellowship/stories.html', 'Read', prefix) +
        ctx['card']('compass', 'FAQ', 'Eligibility, time commitment, funding, and how selection works.', 'fellowship/faq.html', 'Read', prefix) +
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
  <span class="eyebrow reveal">Careers</span>
  <h1 class="reveal" data-d="1" style="max-width:16ch">Help build the workforce that builds the future of care.</h1>
  <p class="lead reveal measure" data-d="2">We are assembling a small team of clinicians, engineers, scientists, and operators who want their work measured in patients helped, not slides shipped.</p>
  <div class="btn-row reveal" data-d="3"><a class="btn btn--grad btn--lg" href="{prefix}contact.html">Introduce yourself {I['arrow']}</a></div>
</div></section>"""
    roles = sec(
        head("Open directions", "We hire for trajectory. If you fit one of these, write to us.") +
        '<div class="rows">' +
        row("Faculty / Clinical", "Clinical leads and mentors", "Attending physicians who want to teach, supervise fellows, and shape real projects.") +
        row("Engineering", "ML and platform engineers", "People who can build reliable, evaluated clinical tools and the platform under them.") +
        row("Curriculum", "Educators and content leads", "Builders who can teach, turning real practice into Academy material and notebooks.") +
        row("Operations", "Programme and partnerships", "Operators who can run cohorts, manage partners, and keep the machine moving.") +
        '</div>')
    why = sec(
        head("Why join", "What you get that you cannot get elsewhere.") +
        '<div class="grid grid-3">' +
        ctx['card']('pulse', 'Real stakes', 'Work that reaches patients, inside a leading medical school, not a sandbox.', None, '', prefix) +
        ctx['card']('users', 'Rare room', 'Clinicians and engineers building together, every day, on the same problems.', None, '', prefix) +
        ctx['card']('compass', 'Build a field', 'Help define how Thailand trains its medical AI workforce, from the start.', None, '', prefix) +
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
        <span class="eyebrow">Contact</span>
        <h1 style="font-size:var(--step-4)">Let us talk.</h1>
        <p class="lead measure">Whether you want to learn, apply, partner, or hire us to build capability, this is the door. Tell us who you are and what you want to do.</p>
        <div class="rows" style="border-top:1px solid var(--line);margin-top:1rem">
          <div class="row" style="grid-template-columns:1fr"><div><div class="step__k">Apply</div><p class="mt2">Academy and Fellowship enquiries</p></div></div>
          <div class="row" style="grid-template-columns:1fr"><div><div class="step__k">Partner</div><p class="mt2">Hospitals, agencies, and health technology companies</p></div></div>
          <div class="row" style="grid-template-columns:1fr"><div><div class="step__k">Where</div><p class="mt2">{ctx['SITE']['org_en']}<br/>{ctx['SITE']['org_th']}</p></div></div>
        </div>
      </div>
      <div class="card card--feature reveal" data-d="1">
        <h3>Send a message</h3>
        <form onsubmit="event.preventDefault();this.querySelector('.gate__msg').textContent='Thank you. This is a static demo form. Wire it to your inbox or a form service before launch.';">
          <div class="field"><label>Name</label><input type="text" required placeholder="Your name"/></div>
          <div class="field"><label>Email</label><input type="email" required placeholder="you@hospital.org"/></div>
          <div class="field"><label>I want to</label><input type="text" placeholder="learn / apply / partner / hire"/></div>
          <div class="field"><label>Message</label><input type="text" placeholder="A sentence about what you have in mind"/></div>
          <div class="gate__msg" style="color:var(--accent)"></div>
          <div class="btn-row mt3"><button class="btn btn--grad btn--lg" type="submit">Send {I['arrow']}</button></div>
        </form>
      </div>
    </div>
  </div>
</section>"""
    return body

# ===========================================================================
# GATE + PORTAL
# ===========================================================================
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
    ("fellowship.html", "Fellowship - DHA Club", "fellowship.html", fellowship),
    ("fellowship/apply.html", "Apply - Fellowship", "fellowship.html", fellowship_apply),
    ("fellowship/stories.html", "Stories - Fellowship", "fellowship.html", fellowship_stories),
    ("fellowship/publications.html", "Publications - Fellowship", "fellowship.html", fellowship_publications),
    ("fellowship/faq.html", "FAQ - Fellowship", "fellowship.html", fellowship_faq),
    ("insights/index.html", "Insights - DHA Club", "insights/index.html", insights_index),
    ("news/index.html", "News - DHA Club", "insights/index.html", news_index),
    ("careers.html", "Careers - DHA Club", "careers.html", careers),
    ("contact.html", "Contact - DHA Club", "", contact),
]
for _slug in INSIGHT_ARTICLES:
    MARKETING.append((f"insights/{_slug}.html", f"{INSIGHT_ARTICLES[_slug][1]} - Insights",
                      "insights/index.html", insight_article(_slug)))
