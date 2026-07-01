# Medical imaging: AI and clinical images

X-rays, CT, MRI, and pathology slides are one of the areas where AI has made
the most real difference. This lesson teaches you to work with the actual
format medical images come in, DICOM, and the deep learning tasks built on top
of it, plus the pitfalls that are specific to imaging and nowhere else.

```{note}
**Level** Intermediate. **Prerequisite** [Deep AI](../deep-ai.md).
**Time** ~4 hours. **Sessions** 2.
**Before you start** Basic familiarity with numpy arrays.
```

## What you will be able to do

1. Read a DICOM file in Python and extract its pixel data and metadata.
2. Name the four core medical imaging tasks and give a clinical example of each.
3. Identify class imbalance and annotation cost as risks specific to imaging
   projects.
4. Explain why transfer learning is usually the right starting point for
   medical imaging.

## Sessions

| # | Session | Format | Time | You finish |
|---|---|---|---|---|
| 1 | DICOM and the four imaging tasks | Read + hands-on | ~2 hrs | A DICOM file read and normalised |
| 2 | Pitfalls and transfer learning | Read | ~2 hrs | A plan using a pretrained model |

## DICOM: not just a picture

A medical image is not a plain JPEG. It is **DICOM** (Digital Imaging and
Communications in Medicine), a format that carries clinical metadata alongside
the pixels: the modality, the body part, the acquisition settings, and often
patient information that must be handled under the same PDPA rules covered in
[Digital Health](../digital-health.md).

```python
import pydicom

ds = pydicom.dcmread("chest_ct.dcm")
print("Modality:", ds.Modality)                          # CT, MR, CR, ...
print("Body part:", ds.get("BodyPartExamined", "-"))
print("Pixel shape:", ds.pixel_array.shape)

# Convert to an array ready for deep learning
import numpy as np
img = ds.pixel_array.astype(np.float32)
img = (img - img.min()) / (img.max() - img.min())   # normalise to 0-1
```

```{warning}
DICOM headers can carry patient name, ID, and date of birth embedded directly
in the file's metadata, separate from the pixel data itself. Before any image
leaves a supervised environment, that metadata must be stripped as part of
de-identification, not just the visible parts of the image.
```

## The four core tasks

| Task | Description | Example |
|---|---|---|
| **Classification** | Decide whether an image shows an abnormality | Pneumonia from a chest X-ray |
| **Detection** | Locate where an abnormality is | A nodule in a CT scan |
| **Segmentation** | Draw the exact boundary of an organ or lesion | Outlining a tumour in an MRI |
| **Registration** | Align images from different times or modalities | Comparing before and after treatment |

Each is a genuinely different modelling problem with different architectures
and different evaluation metrics. Classification gives you a label,
segmentation gives you a pixel-level mask, and confusing the two when scoping a
project is a common early mistake.

## Pitfalls specific to imaging

| Risk | Why it happens | What helps |
|---|---|---|
| **Class imbalance** | Rare diseases have very few positive examples | Weighted loss functions, oversampling, careful metric choice (not plain accuracy) |
| **Annotation cost** | Labelling requires a radiologist's time, which is expensive and scarce | Semi-supervised learning, active learning, starting with a smaller expert-labelled set |
| **Shortcut learning** | Models can latch onto scanner artefacts, text burned into the image, or positioning cues instead of the actual pathology | Multi-site data, saliency checks (see [Deep AI](../deep-ai.md) on explainability) |

```{important}
A chest X-ray classifier that performs suspiciously well can sometimes be
reading the hospital name printed in the corner of images from a site that
happens to see sicker patients, not the lung findings themselves. Always ask
what else in the image could explain the model's performance before you trust
it.
```

## Transfer learning: your default starting point

```{tip}
Medical imaging datasets are almost always small relative to what deep
learning normally wants. Starting from a model pretrained on a large dataset
(ImageNet, or a medical-specific one like RadImageNet) and fine-tuning it on
your smaller, specific dataset usually beats training from scratch, often by a
wide margin. Default to transfer learning unless you have a specific reason not
to.
```

## Common mistakes

- **Treating DICOM like a JPEG.** You lose clinically important metadata and
  risk mishandling embedded patient information.
- **Confusing classification with segmentation when scoping a project.** Decide
  which task you actually need before you pick an architecture.
- **Training from scratch on a small dataset** when a pretrained model would
  have done better with a fraction of the data and compute.
- **Not checking for shortcut learning.** A suspiciously good result deserves
  suspicion, not celebration.

## Check yourself

- [ ] I can read a DICOM file and extract both metadata and pixel data.
- [ ] I can describe classification, detection, segmentation, and registration
      with a distinct clinical example for each.
- [ ] I can name one technique for class imbalance and one for annotation cost.
- [ ] I can explain, in one sentence, why transfer learning usually wins for
      medical imaging.

## What you build

Work through [Notebook: Medical Image Classification](../../notebooks/03-medical-imaging.ipynb)
to build a real image classifier starting from a pretrained model, and note one
shortcut the model could plausibly be taking instead of learning the real
pathology.

## Where this goes next

You now have one deep, applied modality. Return to
[Digital Health](../digital-health.md) for the data standards that carry
imaging studies through a hospital, or continue to
[Deployment](../deployment.md) to put a trained classifier in front of users.
