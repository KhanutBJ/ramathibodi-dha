# M2. Healthcare Data: FHIR, EMR, and the Thai Stack

**Week 1, Day 4 to Week 2, Day 1.** Health data is its own world, with its own standards, codes, and laws. This module is the map. Skip it and every later model will be built on sand.

## Why health data is different

A patient is not a row. They are a stream of events across systems that rarely agree: a hospital information system, an electronic medical record, lab machines, imaging, pharmacy, and claims. The data is sparse, irregular in time, full of codes, and governed by law. Learning to read it is half the job.

## Learning objectives

By the end of M2 you can:

- Explain HIS, EMR, EHR, and PHR and how they relate.
- Read the major clinical coding systems: ICD-10, SNOMED CT, LOINC, and the Thai TMT.
- Parse an HL7 v2 message and a FHIR resource, and explain the difference.
- Apply the PDPA to a real dataset: lawful basis, minimisation, and de-identification.
- Describe the Thai data landscape: NHSO claims, Genomics Thailand, and hospital data.
- Recognise the four data modalities and which problems each suits.

## The systems: HIS, EMR, EHR, PHR

- **HIS**, hospital information system. The operational backbone: admissions, beds, billing, orders. Built for running a hospital, not for analysis.
- **EMR**, electronic medical record. The clinical record inside one institution.
- **EHR**, electronic health record. The record meant to follow a patient across institutions.
- **PHR**, personal health record. The slice the patient owns and controls.

Most Thai clinical AI today is built on EMR and HIS exports from a single hospital. Knowing which system a field came from tells you how reliable and how timely it is.

## Coding systems

Clinical meaning is carried in codes. The four you must know:

- **ICD-10**, diagnoses. Thailand uses ICD-10 with the Thai Modification for some settings. One diagnosis, one code, used heavily in claims.
- **SNOMED CT**, a rich clinical terminology for findings, procedures, and more. More expressive than ICD-10, used for detailed records.
- **LOINC**, lab and observation codes. The same test from two machines should map to the same LOINC.
- **TMT**, Thai Medicines Terminology, the national drug vocabulary. The Thai equivalent layer for medications.

The recurring problem: the same concept appears under different codes in different systems. Mapping and harmonising codes is real, unglamorous, and essential work.

## HL7 v2 and FHIR

Two generations of the exchange standard.

**HL7 v2** is the older pipe-delimited messaging format still running in most hospitals. Dense, hard to read, everywhere.

```
PID|1||123456^^^RAMA||Somchai^Jaidee||19600115|M
```

**FHIR**, Fast Healthcare Interoperability Resources, is the modern standard. Data is broken into resources (Patient, Observation, Condition, Encounter, MedicationRequest), each with a defined shape, exchanged as JSON over a web API.

```json
{
  "resourceType": "Observation",
  "status": "final",
  "code": { "coding": [{ "system": "http://loinc.org", "code": "8867-4", "display": "Heart rate" }] },
  "subject": { "reference": "Patient/123456" },
  "valueQuantity": { "value": 92, "unit": "beats/minute" }
}
```

Why it matters: a model that reads FHIR can run at any hospital that speaks FHIR. A model that reads one hospital's custom export cannot travel. FHIR is how clinical AI scales beyond a single site. Thailand's health data exchange direction points here.

## PDPA: the law you build inside

The Personal Data Protection Act governs personal data in Thailand. Health data is sensitive personal data, with stronger protection. The working principles for a builder:

- **Lawful basis.** You need a legitimate reason to process the data: consent, or another lawful basis such as medical care or research under the right conditions.
- **Minimisation.** Use the fewest fields that answer the question. Do not hoard.
- **De-identification.** Remove or mask direct identifiers (name, national ID, full address, exact dates) before analysis where you can. Remember that combinations of fields can re-identify.
- **Purpose limitation and retention.** Use data for the stated purpose, keep it only as long as needed.

Governance is not a M10 afterthought. It starts here, the moment you touch data.

## The Thai data landscape

- **NHSO claims data.** The National Health Security Office holds nationwide claims from universal coverage. Enormous reach, coded in ICD-10 and procedure codes, powerful for population and risk work, but claims describe billing, not always clinical truth. Read it for what it is.
- **Genomics Thailand.** The national genomics initiative, building Thai genomic and phenotype data for precision medicine. Relevant as genomics enters routine care.
- **Hospital EMR and HIS.** The richest clinical detail, the hardest to access, governed by each institution. This is where most fellowship projects live.

## The four modalities

Clinical data comes in four shapes, and each suits different methods:

- **Tabular.** Labs, vitals, demographics, codes. The bread and butter of risk prediction. Modules M3 and M4.
- **Image.** Radiology, pathology, dermatology. Computer vision. Covered in the imaging track and Deep AI.
- **Signal.** ECG, EEG, waveforms, time series from monitors.
- **Sound.** Voice and audio, including speech for the chatbot and ASR work in M7.

Naming the modality early tells you which tools and which pitfalls you are about to meet.

## Hands-on lab

Open **Notebook 2, Working with FHIR and EMR Data**. You will parse FHIR resources into a tidy table, map codes across systems, and apply a de-identification step, the exact moves a clinical data pipeline makes.

## Common pitfalls

- Treating claims data as clinical ground truth. It records what was billed.
- Ignoring code mapping and quietly losing half your cohort to mismatched vocabularies.
- De-identifying names but leaving exact dates and rare combinations that re-identify.

## Exercise

Take a small set of FHIR Observation and Condition resources from the lab. Produce one tidy table, one row per patient per observation, with the LOINC or ICD-10 code resolved to a human-readable label. List which fields you would remove to meet the PDPA before sharing.

## Further reading

- HL7 FHIR official documentation, the resource list and the Patient and Observation pages.
- PDPA overview from the Thai regulator, the sensitive personal data provisions.
- The club's Insight, FHIR in plain language.
