# Digital Health

A model is only as good as the data it runs on, and in a hospital that data has a
shape, a standard, and a law around it. This domain teaches you the systems a
Thai hospital actually runs, the standards that move data between them, and the
rules that govern how you may use it. This is the part most pure AI courses skip,
and it is the part that decides whether your tool can ever be used.

## Health information system (HIS)

The HIS is the hospital's operational backbone: registration, orders, results,
billing, pharmacy. In Thailand you will meet systems like HOSxP, SSB, and a range
of in-house builds. Knowing how the HIS stores and exposes data is the difference
between a model that runs on a one-off export and a model that runs in the ward.

## EMR and PHR

- **EMR (electronic medical record).** The clinical record inside the hospital:
  notes, results, medications, problems. This is your richest source of signal
  and your hardest data to use well, because notes are free text and Thai.
- **PHR (personal health record).** The record the patient holds and controls,
  increasingly through national apps. The PHR is where patient-facing AI and
  consent meet.

## ICD-10 and clinical coding

ICD-10 is the international code for diagnoses, and in Thailand it drives
reimbursement and statistics. Procedures use ICD-9-CM and drugs use national
standards. You will learn to read coded data, to understand its biases (codes are
chosen for billing, not for truth), and to map between codes and the messy
reality of the note.

## HL7 and FHIR

This is the most important technical standard in the domain. HL7 version 2 is the
old messaging format still everywhere in hospitals. **FHIR** is the modern
standard, and it is what you build on.

FHIR describes health data as resources with a defined shape: a Patient, an
Observation, a Condition, a MedicationRequest. Because the shape is fixed, a tool
built at Ramathibodi can run at another hospital. That portability is the whole
point.

```json
{
  "resourceType": "Observation",
  "status": "final",
  "code": { "text": "Systolic blood pressure" },
  "subject": { "reference": "Patient/123" },
  "valueQuantity": { "value": 138, "unit": "mmHg" }
}
```

You will parse FHIR, build on it, and feel where real hospital data is messier
than the spec promises. This connects to the [FHIR lesson](health/fhir.md) and
the FHIR notebook.

## PDPA and data protection

Thailand's Personal Data Protection Act is the law that governs health data. It
is not a footnote. It shapes what you may collect, how you must store it, who may
see it, and what consent you need.

What every builder must internalise:

- Health data is sensitive personal data with the highest protection.
- You need a lawful basis and, usually, informed consent.
- Minimise: collect only what the task needs.
- De-identify wherever possible, and know that de-identification is hard.
- Data residency and access controls are design requirements, not afterthoughts.

```{warning}
A brilliant model trained on data you had no right to use is worthless and a
liability. Governance and consent come first, always. We return to this in
[Strategy and Governance](governance.md).
```

## Genomics Thailand

Genomics Thailand is the national population genomics initiative, building a Thai
reference for precision medicine. For an AI builder it is both a frontier and a
responsibility: genomic data is the most identifying data there is, and Thai
populations are underrepresented in global references. Working here means
rigorous consent, secure compute, and an eye on equity.

## NHSO claims data

The National Health Security Office holds claims data for the universal coverage
scheme: a vast, population-scale record of diagnoses, procedures, and costs.
Claims data is powerful for population health, risk, and policy, and treacherous
if you forget what it is. It records what was billed, not what was true, and it
misses what happens outside the scheme. You will learn to use it for what it is
good at and to distrust it where it lies.

## What you build

Take a real (or realistic synthetic) FHIR bundle and an ICD-10 coded extract, and
build a small pipeline that loads it, cleans it, and produces a feature table a
model can use, with a written note on the PDPA basis for every field you kept.

## Where this goes next

With real data and the law that governs it, you can train models that matter in
[Deep AI](deep-ai.md), and you can argue for their use responsibly in
[Strategy and Governance](governance.md).
