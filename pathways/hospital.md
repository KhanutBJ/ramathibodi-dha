# Hospital information pathway

For people who want to strengthen the health system from the inside. Not every
good idea should become a startup. Some of the most valuable work is making one
hospital's data flow, governing it well, and fitting AI into a real clinical
workflow so it is used and trusted. This pathway is for the builders who will run
medical informatics inside institutions.

## The problem inside the walls

A hospital is a pile of systems that do not talk to each other: an HIS, a LIS for
the lab, a PACS for imaging, a pharmacy system, a dozen spreadsheets. The patient
is scattered across all of them. Before AI can help, the data has to be findable,
joined, and trustworthy. That work is the foundation, and it is rarely glamorous
and always essential.

## Interoperability in practice

This is where [HL7 and FHIR](../curriculum/digital-health.md) stop being theory.
You will learn to:

- Map data out of the HIS and into FHIR resources.
- Stand up or connect to a FHIR server as the common layer.
- Reconcile identities across systems so one patient is one patient.
- Keep an eye on data quality, because a model on dirty data is worse than no model.

## Governance and the clinical workflow

A tool that is technically correct but does not fit how clinicians work will not
be used. The informatics builder designs for the workflow:

- Where in the round, the clinic, or the order set does the tool appear.
- What the clinician sees, and how little friction it adds.
- The [human-in-the-loop](../curriculum/ai-agent.md) checkpoint and the audit trail.
- Change control, monitoring, and the PDPA basis, owned and maintained over time.

```{important}
Adoption is a clinical change-management problem, not a software problem. The best
tool fails if it adds clicks to a busy ward. Design with the people who will use
it, from the first sketch.
```

## Working with the national system

Inside the system you connect upward too: to the Ministry of Public Health's
digital health direction, to NHSO data and reimbursement, and to national
standards. A hospital that builds to these standards plugs into the country
instead of working around it.

## What you leave with

A working interoperability layer for a real clinical problem, an AI tool that
sits inside the workflow and is actually used, and the governance and monitoring
to keep it safe after you move on.
