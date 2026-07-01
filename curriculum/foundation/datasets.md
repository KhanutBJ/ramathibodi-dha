# Datasets and habitats

A model is only as good as the data it learns from. This session teaches you
where health data actually lives, how to source it responsibly, and the
pipeline every dataset passes through before it is safe to train on: collect,
clean, label, split. This is unglamorous work and it is most of what separates
a real project from a toy demo.

```{note}
**Level** Beginner to intermediate. **Prerequisite** [How to do AI](how-to-ai.md).
**Time** ~3 hours. **Sessions** 2.
**Before you start** Your Colab notebook from the last session.
```

## What you will be able to do

1. Name three kinds of data sources and when each is appropriate.
2. Load and inspect a dataset for shape, missing values, and obvious problems.
3. Walk a dataset through collect, clean, label, and split.
4. State the PDPA-driven rules for handling anything that looks like patient
   data, even in practice.

## Sessions

| # | Session | Format | Time | You finish |
|---|---|---|---|---|
| 1 | Where data comes from | Read | ~1 hr | A list of sources for your own project idea |
| 2 | Loading, cleaning, and the ethics of it | Hands-on | ~2 hrs | A cleaned, split dataset |

## Where data comes from

| Source | What it is | Watch for |
|---|---|---|
| **Open repositories** | Hugging Face Datasets, Kaggle, PhysioNet, MIMIC for de-identified clinical data | Licence terms, and whether it represents a Thai population at all |
| **Institutional data** | Your own hospital's HIS, EMR, or lab systems | Requires supervised access and a PDPA basis, never used casually |
| **Synthetic data** | Data generated to resemble real patients without being any real patient | The safest way to practise before you have real access |

```{tip}
For every exercise in this curriculum before the Fellowship, use open or
synthetic data. Real patient data is a privilege with real obligations attached,
covered fully in [Digital Health](../digital-health.md) and
[Governance](../governance.md). Build the habit of asking "should I even have
this" before you ask "what can I build with this."
```

## Load and look

The first thing you do with any new dataset is look at it honestly, before you
touch it.

```python
from datasets import load_dataset
import pandas as pd

ds = load_dataset("scikit-learn/diabetes", split="train")
df = ds.to_pandas()

print(df.shape)          # how many rows, how many columns
print(df.describe())     # ranges, means, obvious outliers
print(df.isnull().sum()) # where the gaps are
```

Three numbers to check before you do anything else: how many rows, how many are
missing, and whether the ranges make clinical sense. A blood pressure column
with a maximum of 900 is not high blood pressure. It is a data entry error, and
if you do not catch it, your model will "learn" it as normal.

```{warning}
Missing data is rarely random in a clinical setting. A lab value is missing
because a test was not ordered, often because the patient looked well enough
that the test seemed unnecessary. That is information, not noise. Filling it in
carelessly can quietly teach your model the opposite of the truth.
```

## The four-step pipeline

Every dataset, real or open, goes through the same sequence before it is ready
to train on.

1. **Collect.** Gather data from sources you are actually permitted to use.
2. **Clean.** Handle missing values, outliers, and inconsistencies.
3. **Label.** Annotate the data, ideally with clinical expert input, since a
   wrong label teaches a wrong lesson with total confidence.
4. **Split.** Divide into train, validation, and test sets so you can evaluate
   honestly later, a step you will use constantly starting in
   [Evaluation](evaluation.md).

```{important}
Do the split before you do anything else to the data, including cleaning
decisions that involve looking at outcomes. If information from your test set
leaks into how you clean or engineer features for training, your evaluation
will lie to you, confidently, later.
```

## Privacy and ethics, from day one

```{warning}
**Health data is sensitive personal data.** Under Thailand's PDPA, and under any
serious medical ethics standard, patient data always requires:
- **De-identification** before it is used for anything beyond direct care.
- **A lawful basis and, usually, informed consent.**
- **Boundaries.** Data does not leave the systems that are permitted to hold it.

None of this is optional, and none of it is someone else's job. If you are the
one touching the data, it is your job.
```

```{tip}
Practise everything in this domain on the FHIR sample data in
[Notebook: FHIR Data Exploration](../../notebooks/02-fhir-data.ipynb). It is
built to be safe to use while you build the habit of handling health data
correctly.
```

## Common mistakes

- **Skipping the look before the clean.** You cannot clean what you have not
  inspected. Always run `.shape`, `.describe()`, and `.isnull().sum()` first.
- **Filling missing values without asking why they are missing.** In clinical
  data this can hide the exact signal you are trying to model.
- **Splitting after feature engineering that used the whole dataset.** This
  leaks test information into training, a mistake called data leakage that
  makes your evaluation numbers meaningless.
- **Treating "open dataset" as "ethically clear."** Check the licence and the
  population it represents every time.

## Check yourself

- [ ] I can name three sources of data and one risk for each.
- [ ] I inspected a dataset's shape, ranges, and missing values before using it.
- [ ] I can explain why a missing lab value might be meaningful, not random.
- [ ] I split my data before doing any cleaning that could see the outcome.
- [ ] I can state the PDPA basics: de-identify, consent, boundaries.

## What you build

Take one open dataset (the diabetes example above, or your own choice), run it
through collect, clean, label, split, and write two sentences on one thing you
found that would have misled a careless model.

## Where this goes next

You have data you can trust. Now learn to trust your model's performance on it,
honestly, in [Evaluation and optimisation](evaluation.md).
