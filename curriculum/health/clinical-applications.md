# Clinical applications of AI

Where does AI actually touch care today. This lesson surveys the real,
in-practice applications, grounded in the kind of practical, clinician-facing
material taught by accredited education such as the AMA Ed Hub course
*Practical Applications for AI in Health Care*. The aim is judgement: knowing
where AI helps now, where it is hype, and where the risk sits.

A note on language. The field increasingly says **augmented intelligence** rather
than artificial intelligence, to keep the emphasis on supporting the clinician
rather than replacing them. That framing is not just politeness. It is the safest
way to deploy.

## Diagnostics and imaging

The most mature area. AI reads radiographs, CT, retinal photographs, pathology
slides, and skin lesions, usually to flag findings for a clinician rather than to
decide alone.

- Strong where the task is narrow and the data is standardised.
- Weak when the model meets a scanner, a population, or a disease it never saw.
- Almost always deployed as a second reader or a triage flag, with a clinician
  signing off.

## Clinical decision support

Risk scores, early-warning systems for deterioration, sepsis alerts, readmission
risk. These ride on tabular EMR data and live or die on calibration and on
whether the alert changes a decision without drowning staff in noise.

```{warning}
Alert fatigue is a real harm. A model that is right but cries wolf will be
switched off, and switching it off can be the rational choice. Evaluate the
workflow, not just the AUROC.
```

## Documentation and the administrative load

Often the highest-value, lowest-risk place to start. Ambient transcription that
drafts a note from a consultation, summarisation of long records, coding support,
and inbox triage. This is where language models and [speech](../ai-agent.md) earn
their place, and where a Thai-language solution is badly needed and underserved.

## Patient-facing AI

Triage chat, appointment and preparation guidance, medication reminders, and
follow-up, often delivered on Line in the Thai context. The rule is firm: these
inform and route, they do not diagnose, and a clinician owns anything with
clinical consequence.

## Operations and population health

Bed and theatre scheduling, demand forecasting, and population risk
stratification on claims data. Less visible than a diagnosis, often more
impactful across a whole system.

## The honest summary

- AI is real and useful today, mostly as an assistant that a clinician oversees.
- The safest, fastest wins are in documentation and operations, not autonomous
  diagnosis.
- Every application carries the same duties: evaluate it properly, watch for
  subgroup harm, keep a human accountable, and govern the data.

## Reflect

Pick one application above that exists in your own department. Write three
sentences: what it would do, who signs off, and how you would know if it helped.
That is the seed of a real project.
