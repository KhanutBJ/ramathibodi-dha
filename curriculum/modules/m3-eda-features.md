# M3. Exploratory Data Analysis and Feature Engineering

**Week 2, Day 1 to 2.** Before any model, you look. EDA is how you understand the data, find the traps, and turn raw records into features a model can learn from.

## Why this decides everything

The quality of a clinical model is set long before training, in how well you understood the data and how you built the features. A weak model on good features beats a strong model on bad ones. This module is where careful builders pull ahead.

## Learning objectives

By the end of M3 you can:

- Profile a clinical dataset: distributions, missingness, outliers, and leakage.
- Visualise data to find problems a summary table hides.
- Engineer features from vitals, labs, codes, and time.
- Handle missing data honestly, with the clinical meaning in mind.
- Detect and prevent data leakage, the silent killer of medical models.

## Exploratory data analysis

EDA is structured looking. For any new dataset, work through:

- **Shape and types.** How many rows, how many patients, what is each column.
- **Distributions.** Histogram every numeric field. Clinical data is full of impossible values: a heart rate of 0, an age of 200, a placeholder of 999.
- **Missingness.** What fraction is missing per field, and is it missing at random. In medicine a missing lab often means the clinician did not order it, which is itself a signal.
- **Relationships.** How features relate to each other and to the outcome.
- **Time.** When did each event happen relative to the moment of prediction.

```python
df.describe()
df.isna().mean().sort_values(ascending=False)   # missingness per column
df["heart_rate"].hist(bins=50)                   # find impossible values
df.groupby("outcome")["age"].median()            # signal check
```

## Visualise to see what tables hide

A summary statistic can be identical for very different data. Plot before you conclude. Histograms reveal placeholders and bimodal mixes. Scatter plots reveal nonlinearities. A simple plot of a feature against the outcome rate, by bucket, tells you whether the feature carries signal at all.

## Feature engineering for clinical data

Raw fields are rarely the best inputs. Common, high-value transforms:

- **Vitals to flags.** Systolic below 90 becomes an "is hypotensive" feature that a clinician recognises.
- **Labs to trends.** Not just the latest creatinine, but the change from baseline.
- **Codes to groups.** Roll dozens of ICD-10 codes into clinically meaningful categories.
- **Time features.** Hours since admission, time since last abnormal result, time of day.
- **Counts.** Number of prior admissions, number of abnormal labs in 24 hours.

Good features encode clinical knowledge. This is where a clinician on the team is worth more than another GPU.

## Missing data, the honest way

Three honest options, in rough order of preference for clinical work:

1. **Encode missingness explicitly.** Add an "was this measured" flag. Often the most informative move.
2. **Impute with care.** Fill with a sensible value (median, carry-forward for vitals) and record that you did.
3. **Drop**, only when missingness is rare and truly random.

Never drop silently. Never impute in a way that leaks the answer.

## Data leakage: the silent killer

Leakage is when information that would not be available at prediction time sneaks into training, giving a model that looks brilliant in the notebook and fails in the ward. Classic medical examples:

- A "discharge diagnosis" used to predict something known only at admission.
- A treatment that is only given after the outcome is suspected.
- Scaling or imputing using statistics computed over the whole dataset, including the test set.

The discipline: for every feature, ask "would this value exist, for this patient, at the exact moment the model runs." If not, it leaks. Fit all transforms on training data only, then apply to validation and test.

## Hands-on lab

Continue in **Notebook 1 and Notebook 3**. You will profile a synthetic vitals and labs dataset, build a feature set for a deterioration model, and run a leakage check that catches a planted trap.

## Common pitfalls

- Computing the mean over the full dataset to impute, then "discovering" great test performance. That is leakage.
- Throwing away missingness that was actually a strong predictor.
- Engineering hundreds of features and never checking which carry signal.

## Exercise

From the lab data, build five features for predicting deterioration, at least one of each: a vital flag, a lab trend, a time feature, and a count. For each, write one sentence on why it should carry clinical signal, and confirm none of them leak.

## Further reading

- scikit-learn user guide on preprocessing and pipelines, to keep transforms leak-free.
- The club's Notebook 3 feature engineering walkthrough.
