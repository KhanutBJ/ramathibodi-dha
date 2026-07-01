# Clinical AI: safe enough to use on a patient

AI in a clinic is not AI in a demo. A mistake here has consequences for a real
person. This lesson teaches the principles that separate a model that impresses
in a paper from one that a hospital can actually trust: safety by design,
explainability, fairness across patient groups, and validation that goes far
beyond a single accuracy number.

```{note}
**Level** Intermediate. **Prerequisite** [Evaluation](../foundation/evaluation.md).
**Time** ~3 hours. **Sessions** 2.
**Before you start** One clinical prediction problem in mind, real or hypothetical.
```

## What you will be able to do

1. Name the four principles that define trustworthy clinical AI.
2. Walk a project through the five-stage clinical AI lifecycle.
3. Recognise data leakage in a clinical dataset before it wrecks your evaluation.
4. Explain the difference between internal and external validation, and why
   both matter.

## Sessions

| # | Session | Format | Time | You finish |
|---|---|---|---|---|
| 1 | The four principles | Read | ~1 hr | A one-paragraph safety case for your idea |
| 2 | The lifecycle, and data leakage | Read + hands-on | ~2 hrs | A leakage check on a real pipeline |

## Four principles

| Principle | What it means |
|---|---|
| **Safety first** | Design to fail safely, and keep a human in the loop for anything with clinical consequence. |
| **Explainability** | A clinician must be able to see why the model predicted what it predicted. Never a pure black box in a decision that touches care. |
| **Fairness** | Check for bias across patient groups (sex, age, ethnicity, socioeconomic status) rigorously, not as an afterthought. |
| **Validation** | Clinical validation happens before real use, always, on data the model has never seen. |

```{important}
These four are not a checklist you complete once. They are constraints you
carry through the entire lifecycle below, from the first design decision to the
last day the tool is in use.
```

## The clinical AI lifecycle

1. **Define the clinical question.** Start with a real problem, with a
   clinician in the room, not with whatever dataset happens to be available.
2. **Develop and internally validate.** Build the model and check it against
   held-out internal data, evaluating fairness alongside accuracy.
3. **External validation.** Test against data from a different source (another
   hospital, another population) to confirm the model generalises rather than
   having memorised quirks of one institution.
4. **Prospective trial.** Try it under controlled real-world use and measure
   the effect on actual patient outcomes, not just retrospective accuracy.
5. **Monitor and maintain.** Watch continuously for data drift and performance
   decay after deployment. A model that was accurate on launch day can quietly
   degrade as the population or the hospital's practices change.

```{tip}
Most student and early-career projects stop at step 2. The Fellowship exists
specifically to carry a project through steps 3 and 4, because that is where a
model earns the right to be trusted.
```

## Data leakage: the silent killer of clinical models

```{warning}
The most common failure in clinical AI projects is a feature that leaks
information from the future. Using a value that was recorded *after* the
diagnosis to predict that same diagnosis makes a model look impressively
accurate in testing and completely useless in the real world, because that
future information will not exist yet at the moment you need a prediction.
```

Classic examples: using a discharge code to predict readmission, or using a
treatment that was only given because a diagnosis was already made, to predict
that diagnosis. The fix is always the same discipline: for every feature, ask
"would I have known this at the moment I need to make the prediction." If the
answer is no, the feature does not belong in the model.

```{tip}
See a working, leakage-checked pipeline in
[Notebook: Intro to Clinical ML](../../notebooks/01-clinical-ml.ipynb).
```

## Internal vs. external validation, in practice

Internal validation (a held-out set from the same hospital) tells you the model
learned something. External validation (data from a different hospital, a
different scanner, a different population) tells you whether that something
generalises. A model that only passes internal validation may have learned to
recognise your hospital's specific equipment or documentation habits rather
than the underlying clinical pattern.

```{important}
For Thailand specifically: a model trained only on data from one hospital in
Bangkok may not generalise to a provincial hospital with different equipment,
staffing, and patient demographics. If your project has any ambition beyond a
single site, plan for external validation from the start.
```

## Common mistakes

- **Skipping straight to modelling.** The clinical question and the clinician's
  framing come first. A technically excellent model answering the wrong
  question helps no one.
- **Treating fairness as optional.** Check subgroup performance every time, not
  only when someone asks.
- **Confusing internal validation with proof.** Internal validation is a
  necessary first step, never the final answer.
- **Missing a leaked feature.** Audit every feature with the "would I have
  known this yet" question before you trust a result.

## Check yourself

- [ ] I can state the four principles of trustworthy clinical AI from memory.
- [ ] I can walk through all five lifecycle stages for my own project idea.
- [ ] I checked at least one feature in a real pipeline for leakage.
- [ ] I can explain the difference between internal and external validation.

## What you build

Take the notebook pipeline above (or your own project) and write a short audit:
one feature you checked for leakage, one subgroup you would check for fairness,
and which lifecycle stage your project has actually reached.

## Where this goes next

You now hold the safety discipline for clinical AI in general. Apply it to a
specific, high-impact modality in [Medical Imaging](medical-imaging.md), or
learn the data standard underneath all of this in [FHIR](fhir.md).
