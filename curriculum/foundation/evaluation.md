# Evaluation and optimisation

A model that scores beautifully on the data it trained on can fail completely
on the next real patient. This session is the one that keeps you honest: how to
measure a model correctly, what actually happens during training, and how to
spot the single most common disease in medical AI projects, overfitting.

```{note}
**Level** Intermediate. **Prerequisite** [Datasets and habitats](datasets.md).
**Time** ~4 hours. **Sessions** 2.
**Before you start** A cleaned, split dataset from the last session.
```

## What you will be able to do

1. Split data into train, validation, and test sets correctly, and explain why
   each exists.
2. Choose the right metric for a clinical classification task, and explain why
   recall often matters most.
3. Explain, from first principles, what gradient descent is doing during
   training.
4. Recognise overfitting and name at least three ways to reduce it.

## Sessions

| # | Session | Format | Time | You finish |
|---|---|---|---|---|
| 1 | Splits, metrics, and honest evaluation | Read + hands-on | ~2 hrs | A metrics table for a real model |
| 2 | How training actually works, and overfitting | Read + hands-on | ~2 hrs | Gradient descent from scratch |

## Splitting data properly

```python
from sklearn.model_selection import train_test_split

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_valid, X_test, y_valid, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
# 70% train / 15% validation / 15% test
```

Three sets, three jobs:

- **Train.** What the model learns from.
- **Validation.** What you use to tune choices while building, so you are not
  peeking at the real test.
- **Test.** Touched once, at the end, to report honest performance. If you tune
  anything based on the test set, it stops being a test set.

## Choosing the right metric

Accuracy is the metric everyone reaches for first, and it is often the wrong
one in medicine.

| Metric | Best for | Rough formula |
|---|---|---|
| **Accuracy** | Balanced classes only | Correct predictions / all predictions |
| **Precision** | Minimising false positives | TP / (TP + FP) |
| **Recall (sensitivity)** | Minimising false negatives, often critical clinically | TP / (TP + FN) |
| **F1** | A balance of precision and recall | Harmonic mean of the two |
| **AUROC** | Ranking risk across all thresholds | Area under the ROC curve |

```{tip}
In clinical work, recall is often the metric that matters most. Missing a
patient who is actually sick (a false negative) is usually more dangerous than
raising a false alarm (a false positive). Decide, before you train, which
error your problem can tolerate less, and pick your metric accordingly.
```

## Evaluating language output: LLM-as-judge

When a model's output is text, a summary, a translated note, a drafted reply,
you cannot compute accuracy in the usual sense. A common approach is
**LLM-as-judge**: use a second, usually stronger, language model to score the
output against a rubric you define (completeness, faithfulness to the source,
clarity). This is not a replacement for clinician review of anything with
clinical consequence, but it is a useful, scalable first filter while iterating.

## What training actually does: gradient descent from scratch

The heart of training a model is: adjust the parameters a little, check if the
error got smaller, repeat.

```python
import torch

# Simulated data: y = 2x + noise
x = torch.randn(100, 1)
y = 2 * x + 0.1 * torch.randn(100, 1)

w = torch.zeros(1, requires_grad=True)
lr = 0.1

for step in range(50):
    pred = x * w
    loss = ((pred - y) ** 2).mean()   # mean squared error
    loss.backward()                   # compute the gradient
    with torch.no_grad():
        w -= lr * w.grad              # update the parameter
        w.grad.zero_()

print(f"Learned w ≈ {w.item():.3f} (target = 2.0)")
```

Run this and watch `w` converge toward 2.0. That is the entire idea behind
training a neural network with a billion parameters instead of one: the same
loop, at scale. Nothing more mystical is happening underneath.

## Overfitting: the disease of medical AI

| Signal | What it looks like |
|---|---|
| **The symptom** | Training accuracy is high, but validation or test accuracy is low. The model memorised the training examples instead of learning the underlying pattern. |
| **The fix** | More data, regularisation, dropout, early stopping, and cross-validation. |

```{important}
A model that scores beautifully on data it has seen and fails on a new hospital
has learned the wrong thing. This is the single most common way a promising
medical AI project quietly fails. Every model you build from here on gets
checked against this before you trust it.
```

## Common mistakes

- **Tuning against the test set.** The moment you adjust anything based on test
  performance, it becomes a second validation set, and you no longer have an
  honest final number.
- **Reporting accuracy alone.** Always report the metric that matches the
  clinical cost of being wrong, and report more than one number.
- **Declaring victory on training performance.** Only validation and test
  performance tell you anything about a new patient.
- **Ignoring the gap between train and validation scores.** A large gap is
  overfitting, even if both numbers look acceptable in isolation.

## Check yourself

- [ ] I can explain what each of train, validation, and test is for.
- [ ] I chose a metric based on the clinical cost of being wrong, not by default.
- [ ] I can explain gradient descent in plain language to someone non-technical.
- [ ] I can recognise overfitting from a train/validation gap and name two fixes.

## What you build

Train the small linear model above, then take one dataset from the previous
session and report train, validation, and test performance on the metric you
judge most appropriate, with one sentence justifying your choice.

## Where this goes next

You now hold the whole foundation: what these models are, how to build with
them, where data comes from, and how to evaluate honestly. Move into
[AI Agent](../ai-agent.md) to build something that acts, or
[Deep AI](../deep-ai.md) to work with images, signals, and sound.
