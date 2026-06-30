# M0. Onboarding and the Pipeline Mindset

**Week 1, Days 1 to 2.** The first module is not about code. It is about how to think, so that everything you build afterwards has a chance of reaching a patient.

## Why this comes first

Most healthcare AI projects do not fail because the model was weak. They fail because the team solved a problem nobody had, trained on data they could not get in production, or built something no clinician could trust or use. The pipeline mindset exists to stop that.

A working clinical AI system is a chain. Every link has to hold.

```
Problem  ->  Data  ->  Model  ->  Evaluation  ->  Deployment  ->  Governance
```

If the problem is wrong, the rest is wasted. If the data you train on does not exist at the moment of care, the model cannot run. If you cannot evaluate honestly, you cannot be trusted. If you cannot deploy into a real workflow, nothing changes. If you ignore governance, you get stopped before launch. You will return to this chain in every module.

## Learning objectives

By the end of M0 you can:

- State a clinical problem as a decision a real person makes, at a real moment, with a real action attached.
- Sketch the full pipeline for a project before writing any code.
- Set up your working environment: Colab, Git, and the club workspace.
- Decide when to use no-code, when to use AI-assisted coding, and when to write code yourself.
- Name the three most common ways hospital AI projects die, and how to avoid each.

## The clinical-problem-first rule

Before any dataset or model, write one sentence in this shape:

> When **[who]** is at **[what moment]**, they have to decide **[what]**, and a better decision would lead to **[what action and outcome]**.

Example: "When a ward nurse reviews an admitted patient overnight, they have to decide who is at risk of deteriorating, and an earlier flag would lead to a faster review and fewer ICU transfers."

If you cannot fill that sentence in, you do not have a project yet. You have a topic. Topics do not ship.

## The pipeline, link by link

**Problem.** A decision, an owner, and a measure of success that a clinician agrees with. Write down what "good" looks like in numbers before you build.

**Data.** Ask the question that kills most projects early: will this exact data be available, in this exact form, at the moment the model has to run? Training on a rich research export and deploying where only three fields exist is the classic trap.

**Model.** Start with the simplest thing that could work. A rule or a logistic regression that a clinician understands often beats a deep network nobody trusts. Complexity is a cost you justify, not a default.

**Evaluation.** Honest evaluation is the whole game in medicine. You will spend a full module on it. For now: never report a number on data the model has seen, and never report only accuracy.

**Deployment.** A model in a notebook helps no one. It has to live inside a workflow, on infrastructure the hospital allows, fast enough to be useful.

**Governance.** Safety, privacy, validation, and regulation. In Thailand this means the PDPA, the Thai FDA pathway for Software as a Medical Device, and your institution's review. Designed in from the start, this is a path. Bolted on at the end, it is a wall.

## How to build: no-code, AI-assisted, or by hand

You have three gears. Choosing well saves weeks.

- **No-code and low-code** (dashboards, form builders, n8n automations). Best for workflow glue, internal tools, and fast prototypes where logic is simple and volume is modest.
- **AI-assisted coding** ("vibe coding" with an assistant). Best for moving fast on standard problems, learning a new library, and turning a clear plan into a first draft. You still have to read and test every line. The assistant is a fast junior, not an authority.
- **Hand-written code.** Best for the core logic that has to be correct, anything touching patient data, and anything you will have to defend to a regulator.

The rule: prototype in the highest gear that is honest, then drop a gear for anything that has to be safe.

## Three ways hospital AI dies, and the antidote

1. **Solving a non-problem.** Antidote: the clinical-problem-first sentence, signed off by the clinician who owns the decision.
2. **Data that does not exist in production.** Antidote: trace every input back to a real-time source before you train.
3. **No owner, no workflow.** Antidote: name the person whose day changes, and design the tool into their existing steps, not beside them.

## Your setup checklist

- [ ] Club workspace account and access code working.
- [ ] Google Colab opens and runs a cell.
- [ ] Git installed, and you can clone and commit to a practice repository.
- [ ] A markdown note where you keep your project's problem sentence and pipeline sketch.
- [ ] You have read one AMA Ed Hub overview on practical AI in health care to calibrate on tone and rigour.

## Exercise

Pick any clinical situation you have seen or can imagine. Write the problem sentence. Then sketch all six pipeline links in two lines each. Bring the data question to the front: name the exact fields and where they come from at the moment of care. You will reuse this in M3 and M4.

## Further reading

- AMA Ed Hub, practical applications for AI in health care, for the clinician's framing.
- The club's note on governance as a design material, in Insights.
