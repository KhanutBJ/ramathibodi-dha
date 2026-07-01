# Deep AI

Language models get the attention, but a great deal of clinical AI is deep
learning on images, signals, sound, and tables. This domain teaches you to train
a model on real medical data, to know whether it actually works, and to explain
what it is doing. The last part is not optional in medicine.

```{note}
**Level** Intermediate. **Prerequisite** [Basics](basics.md), and the evaluation
ideas from [Foundations](foundation/evaluation.md).
**Time** ~12 to 14 hours over a week. **Sessions** 6.
**Before you start** Comfort running a Colab notebook. No calculus required; you
read training curves, you do not derive gradients.
```

### What you will be able to do

1. Explain a neural network's training loop and read its loss and validation curves.
2. Pick the right model family for image, signal, sound, or tabular data, and know when a gradient-boosted tree beats deep learning.
3. Spot and test for shortcut learning (scanner artefacts, burned-in labels).
4. Train one model on a real medical dataset and evaluate it on a held-out, ideally external, test set.
5. Produce an explanation a clinician can read: SHAP or Grad-CAM, plus a calibration curve.

### Sessions

| # | Session | Format | Time | You finish |
|---|---|---|---|---|
| 1 | Deep learning basics in PyTorch | Tutorial | ~2.5 hrs | A trained toy model |
| 2 | Image models and shortcuts | Read + tutorial | ~2.5 hrs | A tested image classifier |
| 3 | Signal and sound | Read + tutorial | ~2 hrs | A sequence model run |
| 4 | Tabular, and when trees win | Read + build | ~2 hrs | An XGBoost baseline |
| 5 | Explainability | Tutorial | ~2 hrs | SHAP or Grad-CAM output |
| 6 | Honest evaluation | Build | ~2 hrs | A calibration curve |

## Basic deep learning

A neural network is a stack of simple functions that learn, by example, to turn
an input into an output. You will build the mental model and the practical loop:

- **Tensors.** Data as arrays the model can process.
- **Layers and activation.** The building blocks that learn features.
- **Loss.** A number that says how wrong the model is right now.
- **Backpropagation and the optimiser.** How the model nudges itself less wrong.
- **Epochs, batches, learning rate.** The knobs of training.

You will use PyTorch, the standard for research and increasingly for production.
You do not derive the maths from scratch. You build, train, and read the curves.

```{important}
Overfitting is the disease of medical AI. A model that scores beautifully on data
it has seen and fails on a new hospital has learned the wrong thing. Validation
and external testing, taught in Foundations, are how you catch it.
```

## The four data types

Most medical problems fall into four shapes. Each has its own models and pitfalls.

### Image

Radiology, pathology, dermatology, fundus photography, ultrasound. Convolutional
networks and vision transformers classify, detect, and segment. The pitfalls are
specific: models latch onto scanner artifacts, body-position cues, and labels
burned into the image instead of the pathology. You will learn to preprocess,
augment, and test for these shortcuts.

This connects to the [Medical Imaging](health/medical-imaging.md) lesson and the
imaging notebook.

### Signal

ECG, EEG, vital-sign streams, waveforms. These are time series. You will meet
1D convolutions and recurrent and transformer models for sequences, and the real
challenge of noisy, irregularly sampled hospital signals.

### Sound

Cough, breath, heart and lung auscultation, and the voice biomarkers that hint
at neurological and respiratory disease. Audio is usually turned into a
spectrogram and treated like an image, then the same care about shortcuts
applies.

### Tabular

The most common and most underrated. Labs, vitals, demographics, and diagnoses
in rows and columns. Gradient-boosted trees (XGBoost, LightGBM) usually beat deep
learning here, and they are easier to interpret. Knowing this saves you months.

```{tip}
When someone shows you a deep model for a tabular problem, ask whether a
gradient-boosted tree was tried first. Often it wins and explains itself better.
```

## Explainability

A model a clinician cannot interrogate is a model a clinician should not trust.
Explainability is how you open the box.

- **Feature importance and SHAP.** Which inputs drove this prediction, and by how
  much. Essential for tabular clinical models.
- **Saliency and Grad-CAM.** Where in an image the model looked. A quick check
  that it looked at the lesion and not the label.
- **Calibration.** Does a predicted 70 percent risk mean 70 percent in reality.
  An uncalibrated model misleads even when its ranking is good.
- **Global versus local.** Understand the model overall, and explain a single
  patient's prediction at the bedside.

Explainability is also a regulatory and trust requirement, which you will see
again in [Governance](governance.md).

## Common mistakes

- **Reporting the number on data the model has seen.** Only a held-out, ideally
  external, test set tells the truth. Everything else is a rehearsal.
- **Reaching for deep learning on tabular data** before trying a gradient-boosted
  tree that is faster, stronger, and explains itself.
- **Ignoring calibration.** A good ranking with bad calibration still misleads a
  clinician reading a percentage.
- **Not checking where the model looked.** Grad-CAM on a few cases catches
  shortcut learning before it embarrasses you in front of a radiologist.

## Check yourself

- [ ] I trained a model and can read its loss and validation curves.
- [ ] I reported performance on a held-out or external test set, with its denominator.
- [ ] I tried a simple baseline before a complex model.
- [ ] I produced an explanation a clinician could actually read.
- [ ] I checked calibration, not just accuracy or AUROC.

## What you build

Train one model on a real medical dataset in the type that fits your interest,
image, signal, sound, or tabular. Evaluate it honestly with a held-out and ideally
external test set. Then produce an explanation a clinician can read: a SHAP
summary or a Grad-CAM overlay, plus a calibration curve.

## Where this goes next

A trained, explained model is still not a product. Take it to
[Deployment](deployment.md) to put it in front of users, and to
[Digital Health](digital-health.md) to feed it the real data standards it will
meet in a hospital.
