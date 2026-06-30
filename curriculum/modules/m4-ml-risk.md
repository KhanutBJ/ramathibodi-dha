# M4. Machine Learning and Risk Prediction

**Week 2, Day 2 to 4.** The first real model. You will train a risk predictor, evaluate it the way medicine demands, and learn why the simplest model that works is usually the right one.

## The shape of the problem

A huge share of useful clinical AI is risk prediction: given what we know now, how likely is this outcome. Will this patient deteriorate, be readmitted, develop sepsis, miss an appointment. These are supervised learning problems on tabular data, and they are where most fellowship projects begin.

## Learning objectives

By the end of M4 you can:

- Frame a clinical question as a supervised learning task with a clear label and time window.
- Train baseline models: logistic regression and a gradient-boosted tree.
- Evaluate with the metrics medicine actually uses, not just accuracy.
- Read a calibration curve and explain why calibration matters at the bedside.
- Choose an operating threshold from the cost of false positives and false negatives.

## Frame before you fit

Three decisions define the task, and getting them wrong invalidates everything downstream:

- **The label.** What exactly are you predicting, and how is it defined in the data? "Deterioration" must become a concrete, checkable event.
- **The prediction time.** At what moment does the model run, and only data before that moment is allowed. This is your defence against leakage from M3.
- **The cohort.** Who is included and excluded, and does that match where the model will be used.

Write these down and have a clinician confirm them before training.

## Baselines first

Start simple, always.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
proba = model.predict_proba(X_valid)[:, 1]
```

**Logistic regression** is interpretable, fast, and a strong baseline. Each feature gets a weight a clinician can inspect. **Gradient-boosted trees** (such as XGBoost or scikit-learn's `HistGradientBoostingClassifier`) often win on tabular data and handle interactions and missingness well. Train both. If the complex model does not clearly beat the simple one, ship the simple one.

## Evaluation, the part medicine cares about

Accuracy is almost useless here. If 3 percent of patients deteriorate, a model that says "no one will" is 97 percent accurate and worthless. Use:

- **ROC AUC.** Ranking ability across thresholds. Good for comparing models, weak when classes are very imbalanced.
- **PR AUC** and precision and recall. More honest when the positive class is rare, which in medicine it usually is.
- **Sensitivity and specificity.** The clinical language. Sensitivity is how many true cases you catch, specificity is how many healthy patients you do not alarm.
- **Calibration.** Do the predicted probabilities mean what they say. When the model says 20 percent, do 20 percent of those patients actually have the event.

```python
from sklearn.metrics import roc_auc_score, average_precision_score
roc = roc_auc_score(y_valid, proba)
pr  = average_precision_score(y_valid, proba)
```

## Why calibration matters at the bedside

A clinician acts on the probability, not the rank. If a model is well calibrated, "30 percent risk" supports a real decision. If it is miscalibrated, the same number misleads. Plot a calibration curve. If it is off, calibrate (Platt scaling or isotonic). In medicine, a well-calibrated simpler model often beats a sharper but overconfident one.

## Choosing a threshold

A probability becomes an action only at a threshold. That choice is clinical, not statistical. Ask: what does a false positive cost (an unnecessary review, alarm fatigue) and what does a false negative cost (a missed deterioration). Set the threshold where the trade matches the clinical reality, and report sensitivity and specificity at that point. One model can have many right thresholds for different wards.

## Validation that survives contact with reality

- **Hold out by patient and by time.** Never let the same patient appear in train and test. Where you can, test on a later time period than you trained on, because hospitals drift.
- **Cross-validate** for stability, grouped by patient.
- **Report a confidence interval**, not a single number. Bootstrapping is enough.

## Hands-on lab

Open **Notebook 3, Risk Prediction on Tabular Clinical Data**. You will train logistic regression and a gradient-boosted tree on a synthetic deterioration dataset, compare ROC and PR curves, inspect calibration, and choose a threshold from a cost argument.

## Common pitfalls

- Reporting accuracy on imbalanced data and calling it good.
- A test set with leakage or with patients also in training. Brilliant numbers, useless model.
- Shipping the complex model when the simple one was as good and far easier to trust and deploy.

## Exercise

On the lab data, beat the logistic-regression baseline with a gradient-boosted tree, judged on PR AUC, or show honestly that you cannot. Then pick an operating threshold for a busy ward and justify it in two sentences using the cost of each error type.

## Further reading

- scikit-learn user guide, model evaluation and calibration.
- A clinical prediction model reporting guide (such as TRIPOD) for how to present results responsibly.
