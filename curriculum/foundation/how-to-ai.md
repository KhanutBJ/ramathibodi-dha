# How to do AI

Before you can build anything, you need a workshop. This session sets up the
tools you will use for the rest of the curriculum and gets you running your
first AI code within the hour. Everything here is free, and none of it requires
installing software on your own machine.

```{note}
**Level** Beginner. **Prerequisite** [What is AI](what-is-ai.md) is helpful but
not required.
**Time** ~2 to 3 hours. **Sessions** 2.
**Before you start** A laptop and a Google account.
```

## What you will be able to do

1. Run Python in the browser with Google Colab, with a free GPU.
2. Install and import a library, and load a real dataset in three lines.
3. Explain what each tool in your stack is for.
4. Run your first model-adjacent code and see a real result.

## Sessions

| # | Session | Format | Time | You finish |
|---|---|---|---|---|
| 1 | The toolkit | Read | ~30 min | A one-line description of each tool |
| 2 | Colab setup and first run | Hands-on | ~2 hrs | A working notebook with GPU output |

## The toolkit

You do not need to install anything to start. This is the stack the whole
curriculum uses.

| Tool | What it is for |
|---|---|
| **Google Colab** | Runs Jupyter notebooks in the cloud, free GPU included |
| **Python 3** | The primary language of AI and ML |
| **Jupyter Notebook** | Code, explanation, and output together in one document |
| **Git and GitHub** | Version control and sharing code, covered in [Basics](../basics.md) |
| **Hugging Face** | A library of open models and datasets you can load in one line |

```{note}
Because one of our partners is the Google Developer Group on campus, this
curriculum leans on Google Cloud and Colab for hands-on work. The concepts
transfer directly to AWS, Azure, or a hospital's own infrastructure, which you
will meet in [Deployment](../deployment.md).
```

## Set up Google Colab

1. Open [colab.research.google.com](https://colab.research.google.com) with a
   Google account.
2. Create a new notebook: **File > New notebook**.
3. Turn on a GPU: **Runtime > Change runtime type > T4 GPU**.
4. Run the check below.

```python
import sys
import torch

print(f"Python: {sys.version.split()[0]}")
print(f"PyTorch: {torch.__version__}")
print(f"GPU available: {torch.cuda.is_available()}")
```

If you see `GPU available: True`, you are ready.

```{tip}
**Try this now.** Type that code into your first Colab cell and run it with
Shift+Enter. This is the smallest possible "hello world" for AI: it proves your
environment can see a GPU, which is what every deep learning notebook in this
curriculum will need.
```

## Commands you need on day one

```python
# Install an extra library into this notebook session
!pip install -q transformers datasets

# Load a dataset from Hugging Face
from datasets import load_dataset
ds = load_dataset("imdb", split="train[:100]")
print(ds[0]["text"][:200])
```

That `!pip install` line is you, the builder, adding a tool to your workshop.
The `load_dataset` line pulls real data from a shared, open library in one
call. You will use this exact pattern constantly: install, import, load, look.

```{tip}
Do the full hands-on version in
[Notebook: Intro to Clinical ML](../../notebooks/01-clinical-ml.ipynb). It
takes the setup above and trains a real, small model on clinical-style data
before you finish this session.
```

## Reading errors without panic

Your code will fail. Everyone's does, constantly. The skill is reading the
error, not fearing it.

1. Read the **last line** of the error first. It usually names the real problem.
2. Search that exact line, in quotes, before you search anything else.
3. Check for the boring causes first: a typo, a missing install, a wrong
   variable name.

```{note}
`ModuleNotFoundError` means you forgot to `!pip install` it. `KeyError` means
you asked for a column or key that is not there, usually a typo. These two
explain most of the errors you will see this month.
```

## Common mistakes

- **Skipping the GPU check.** If you train a deep learning model on CPU only by
  accident, it will look frozen. Always confirm `torch.cuda.is_available()`
  first.
- **Not restarting the runtime after a strange error.** Colab sessions can get
  into an odd state. **Runtime > Restart session** fixes more problems than it
  should, and costs nothing to try.
- **Copying code without running it line by line first.** Run each new cell as
  you write it. A five-line block that fails is much harder to debug than one
  line that just failed.

## Check yourself

- [ ] I have a Colab notebook with a GPU turned on.
- [ ] I ran the setup check and saw `GPU available: True`.
- [ ] I installed a library with `!pip install` and used it.
- [ ] I loaded a real dataset with `load_dataset` and printed a row.

## What you build

A Colab notebook, saved to your Google Drive or GitHub, that runs the setup
check and loads one open dataset. This notebook is your workshop. Every later
session in this curriculum builds inside a notebook like it.

## Where this goes next

Your tools are ready. Learn where the data itself comes from and how to prepare
it responsibly in [Datasets and habitats](datasets.md).
