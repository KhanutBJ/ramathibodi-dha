# FHIR and HL7: the common language of health data

Before you can build AI for a hospital, you need to understand how health data
actually moves between systems. FHIR (Fast Healthcare Interoperability
Resources) is the modern standard that lets a HIS, a lab system, and an AI tool
built by three different vendors all describe a patient the same way.

```{note}
**Level** Intermediate. **Prerequisite** [Digital Health](../digital-health.md).
**Time** ~3 hours. **Sessions** 2.
**Before you start** Basic comfort with JSON.
```

## What you will be able to do

1. Explain why health data standards exist and what problem they solve.
2. Read and construct a basic FHIR resource.
3. Call a public FHIR server and parse the response into a usable table.
4. Name the other standards (HL7 v2, DICOM, ICD) and what each is for.

## Sessions

| # | Session | Format | Time | You finish |
|---|---|---|---|---|
| 1 | Why standards, and FHIR resources | Read | ~1 hr | A hand-written Patient resource |
| 2 | Calling a FHIR API | Hands-on | ~2 hrs | A table of patients pulled from a live server |

## Why a standard at all

A single hospital might run a HIS, a LIS (laboratory), a RIS (radiology), and
an EMR, each from a different vendor, each with its own internal format.
Without a shared language, data gets trapped in silos: the lab system knows a
result, but the EMR cannot read it without custom, fragile integration work for
every single pair of systems. FHIR solves this by defining standard
**resources**, so any system that speaks FHIR can understand data from any
other.

| Standard | Role |
|---|---|
| **HL7 v2** | The older standard, still everywhere, used for message-based exchange between systems |
| **FHIR** | The modern standard: resources exposed as a REST API, in readable JSON |
| **DICOM** | The standard specifically for medical images, covered in [Medical Imaging](medical-imaging.md) |
| **SNOMED CT / ICD** | Standard coding systems for diagnoses, covered further in [Digital Health](../digital-health.md) |

## The shape of a FHIR resource

```json
{
  "resourceType": "Patient",
  "id": "example-001",
  "name": [{ "family": "Jaidee", "given": ["Somying"] }],
  "gender": "female",
  "birthDate": "1985-03-12",
  "address": [{ "city": "Bangkok", "country": "TH" }]
}
```

Every resource has a fixed shape: a `resourceType`, an `id`, and a defined set
of fields for that type. The resources you will meet constantly:

- **Patient.** Demographic information.
- **Observation.** A measured result, a blood pressure reading, a lab value.
- **Condition.** A diagnosis.
- **MedicationRequest.** A prescription.
- **Encounter.** A visit or admission.

```{tip}
Because the shape is fixed, a tool built to read `Observation` resources from
one hospital's FHIR server can read them from any other hospital's FHIR server
with no changes. That portability is the entire point, and it is what lets a
tool you build at Ramathibodi travel elsewhere.
```

## Calling a FHIR API

```python
import requests

base = "https://hapi.fhir.org/baseR4"
resp = requests.get(f"{base}/Patient", params={"_count": 5})
bundle = resp.json()

for entry in bundle.get("entry", []):
    p = entry["resource"]
    name = p.get("name", [{}])[0]
    print(name.get("family", "-"), p.get("gender", "-"))
```

A FHIR response is a `Bundle`, a container holding a list of `entry` items,
each wrapping one resource. Parsing FHIR is mostly this pattern: unwrap the
bundle, loop the entries, pull the fields you need from each resource.

```{tip}
`hapi.fhir.org` is a free, public FHIR test server built exactly for practice
like this. You can query and even write test data to it without ever touching
real patient information. Run the code above right now, before you read
further.
```

## Where real hospital data gets messy

The specification is clean. Real data is not. You will meet fields left empty
in ways the spec allows but did not warn you about, dates recorded in
inconsistent formats, and the same clinical concept coded slightly differently
across departments. Reading FHIR from a real Thai hospital system, as opposed
to a clean public demo server, is where you learn the difference between
"the standard says" and "the hospital actually does."

```{important}
Interoperability is not a solved problem just because a hospital "uses FHIR."
Adopting the standard and using it consistently, correctly, and completely are
three different levels of maturity, and most real systems sit somewhere in the
middle. Build defensively: check for missing fields, do not assume every
resource is complete.
```

## Common mistakes

- **Assuming FHIR data is clean because the standard is well-specified.** The
  standard defines the shape, not the completeness or consistency of what a
  real system puts inside that shape.
- **Hard-coding a resource's fields without checking for missing ones.** Use
  `.get()` with defaults, as in the examples above, not direct dictionary
  access that will crash on the first incomplete record.
- **Confusing HL7 v2 and FHIR.** Many real Thai hospital systems still speak
  HL7 v2 internally, with FHIR as a newer layer on top. Know which one you are
  actually working with.

## Check yourself

- [ ] I can explain, to someone non-technical, why a data standard matters.
- [ ] I can write a basic Patient resource in JSON from memory.
- [ ] I called a live FHIR server and turned the response into a table.
- [ ] I can name HL7 v2, FHIR, DICOM, and ICD and what each is for.

## What you build

Work through [Notebook: FHIR Data Exploration](../../notebooks/02-fhir-data.ipynb)
to pull real (public, safe) FHIR data and turn it into a feature table a model
could use, following the pattern from
[Datasets and habitats](../foundation/datasets.md).

## Where this goes next

You now understand the plumbing health data runs on. Return to
[Digital Health](../digital-health.md) for the wider system it sits inside, or
continue to [Deployment](../deployment.md) to build something that reads and
writes this data in production.
