# Digital Health

A model is only as good as the data it runs on, and in a hospital that data has a
shape, a standard, and a law around it. This domain teaches you the systems a
Thai hospital actually runs, the standards that move data between them, and the
rules that govern how you may use it. This is the part most pure AI courses skip,
and it is the part that decides whether your tool can ever be used.

```{note}
**Level** Intermediate. **Prerequisite** [Basics](basics.md).
**Time** ~10 to 12 hours over a week. **Sessions** 6.
**Before you start** No hospital-IT background needed. If you have ever been
frustrated by a hospital system as a clinician, that frustration is your syllabus.
```

### What you will be able to do

1. Describe how a Thai HIS, EMR, and PHR store and expose data, and what that means for a model.
2. Read ICD-10 coded data and explain why codes are chosen for billing, not truth.
3. Parse and build on FHIR resources, and feel where real data is messier than the spec.
4. State the PDPA basis for every field you use, and de-identify responsibly.
5. Use NHSO claims and Genomics Thailand data for what they are good at, and distrust them where they lie.

### Sessions

| # | Session | Format | Time | You finish |
|---|---|---|---|---|
| 1 | HIS, EMR, and PHR | Read | ~1.5 hrs | A map of your hospital's data |
| 2 | ICD-10 and clinical coding | Read + build | ~1.5 hrs | A coded-data read |
| 3 | HL7 and FHIR | Read + tutorial | ~2.5 hrs | A parsed FHIR bundle |
| 4 | PDPA and data protection | Read | ~1.5 hrs | A PDPA basis note |
| 5 | Genomics Thailand and NHSO claims | Read | ~1.5 hrs | A source-limits memo |
| 6 | Build a small data pipeline | Build | ~2.5 hrs | A feature table with a basis |

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

## Common mistakes

- **Building on a one-off export** that no one can reproduce, instead of the way
  the HIS actually exposes data.
- **Treating ICD codes as ground truth.** They record what was billed. The note
  holds the reality.
- **Leaving PDPA to the end.** A model trained on data you had no right to use is
  a liability, not an asset. The basis comes first.
- **Assuming FHIR is clean.** Real bundles have missing fields, local quirks, and
  Thai free text. Plan for the mess.

## Check yourself

- [ ] I can name the HIS, EMR, and PHR my hospital uses and how they expose data.
- [ ] I can read a FHIR bundle and pull a value out of it.
- [ ] Every field in my feature table has a written PDPA basis.
- [ ] I can explain what NHSO claims data is good for and where it misleads.
- [ ] I de-identified before I did anything else with patient data.

## What you build

Take a real (or realistic synthetic) FHIR bundle and an ICD-10 coded extract, and
build a small pipeline that loads it, cleans it, and produces a feature table a
model can use, with a written note on the PDPA basis for every field you kept.

## Where this goes next

With real data and the law that governs it, you can train models that matter in
[Deep AI](deep-ai.md), and you can argue for their use responsibly in
[Strategy and Governance](governance.md).
