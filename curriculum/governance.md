# Strategy and Governance

This is the domain that separates a demo from something a hospital can use on a
patient. It is where a strategist and a regulator think. You do not need to
become a lawyer, but you do need to know the path, because a tool built without
the path in mind usually cannot walk it later. Governance is a design material,
present from the first decision, not a gate at the end.

## Why a clinician should care about regulation

If your tool influences diagnosis or treatment, it is probably a medical device
in the eyes of the law, even if it is just software. That is not a reason to stop.
It is the reason to build so that approval is possible. The teams that win are the
ones that designed for the regulator from day one.

## Thai FDA

Thailand's Food and Drug Administration regulates medical devices, and software
that meets the definition of a medical device falls under it. The key questions
the Thai FDA framework asks of any device map cleanly onto how you build:

- **What does it claim to do.** The intended use defines everything that follows.
- **What is the risk if it is wrong.** Risk class drives the evidence required.
- **What evidence supports the claim.** Validation, clinical evaluation, and
  ongoing monitoring.

You will learn how the Thai framework aligns with international norms, so a tool
built here can move beyond here.

## AI as Software as a Medical Device (SaMD)

SaMD is the international concept for software that is a medical device in its own
right, without being part of a physical instrument. The IMDRF framework, which
Thai and global regulators draw on, classifies SaMD by two axes: how serious the
condition is, and how central the software is to the clinical decision.

What this means for you:

- A triage suggestion a clinician confirms is a lower class than an autonomous
  diagnosis.
- AI that changes over time (a learning model) needs a plan for how change is
  controlled and re-validated.
- Your intended-use statement is the most important sentence in the project.
  Write it early, write it precisely, and let it constrain scope.

```{important}
Narrow your claim. "Flags possible diabetic retinopathy for ophthalmologist
review" is buildable and approvable. "Diagnoses eye disease" is neither. Scope is
a safety feature.
```

## ISO and quality systems

Standards are how you prove you build responsibly and repeatably.

- **ISO 13485.** Quality management for medical devices. How the organisation
  that makes the software is run.
- **ISO 14971.** Risk management. Identify, evaluate, and control every way the
  software could harm, across its life.
- **IEC 62304.** The software life-cycle for medical devices.
- **ISO 27001 and information security.** Protecting the data, which ties back to
  PDPA in [Digital Health](digital-health.md).

You will not certify a company in this course. You will learn what these
standards ask for, so your project's documentation, risk log, and change control
are built in from the start rather than reconstructed in a panic later.

## The regulatory and strategy path

Putting it together, the route from idea to real use looks like this:

1. **Intended use.** One precise sentence. The clinical problem and the claim.
2. **Risk classification.** How bad is a wrong answer. This sets the bar.
3. **Evidence plan.** What validation and clinical evaluation the claim needs.
4. **Quality and risk documentation.** The ISO and IEC artefacts, kept as you go.
5. **Data governance.** PDPA basis, consent, security, residency.
6. **Submission and review.** Engagement with the Thai FDA.
7. **Post-market monitoring.** Watching for drift and harm after deployment.

A strategist also reads the landscape: where the Ministry of Public Health is
pushing, where the National Health Security Office will pay, and where the
National Innovation Agency will fund the next step.

## What you build

A one-page regulatory and governance brief for your own project: the intended-use
statement, a first-pass risk classification with reasoning, the evidence you would
need, the PDPA basis, and the top five risks from a simple ISO 14971-style risk
table.

## Where this goes next

You now hold the whole craft, from idea to a tool with a path to real use. Choose
where it lands: the [Startup pathway](../pathways/startup.md) to build a product,
or the [Hospital information pathway](../pathways/hospital.md) to strengthen the
system from inside.
