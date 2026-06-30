# M1. Python and Data Science

**Week 1, Days 2 to 4.** The working language of medical AI. By the end you can load real health data, explore it, and reason about it in code you understand.

## Why Python

Python is where the healthcare AI ecosystem lives: pandas for tables, NumPy for arrays, scikit-learn for models, the FHIR and imaging libraries you will meet later. You do not need to be a software engineer. You need to be fluent enough to load data, transform it, and check your own work.

## Learning objectives

By the end of M1 you can:

- Run and structure a notebook in Google Colab.
- Use Git to version your work and read other people's repositories.
- Read and reshape tabular data with pandas: select, filter, group, join.
- Use NumPy arrays and understand vectorised thinking.
- Read library documentation well enough to learn a new tool on your own.
- Call a simple API and understand what the cloud is doing underneath.

## Notebooks and Colab

A notebook is code, output, and prose in one document. It is how data science is done and shared. In Colab you get a free Python environment in the browser with common libraries installed.

Habits that separate good notebooks from messy ones:

- One idea per cell. Run top to bottom and it should always work.
- Name things for what they are, not `df2` and `x`.
- Write a sentence of markdown before each block. Future you is a stranger.
- Restart and run all before you trust a result. Hidden state lies.

## Git, in practice

Git is how you save versions, collaborate, and never lose work. The core loop is small:

```bash
git clone <url>        # get a repository
git checkout -b my-work # make your own branch
# ... edit files ...
git add -A             # stage changes
git commit -m "what and why"  # save a version
git push               # share it
```

You will use Git to submit labs and to read the club's open notebooks. Branch for your own work, commit small and often, and write messages that say why, not just what.

## Pandas: the data workhorse

Most health data arrives as tables: one row per patient, per visit, per lab result. Pandas is how you handle them.

```python
import pandas as pd

df = pd.read_csv("admissions.csv")
df.shape                      # rows, columns
df.head()                     # look before you leap
df["age"].describe()          # quick distribution
df[df["age"] >= 65]           # filter
df.groupby("ward")["los"].mean()   # aggregate
df.merge(labs, on="visit_id", how="left")  # join tables
```

The skills that matter most in clinical data: joining tables that came from different systems, handling missing values honestly, and converting messy free text and codes into something a model can use. You will do all three in the lab.

## NumPy and vectorised thinking

Under pandas sits NumPy, arrays of numbers you operate on all at once instead of looping. Vectorised code is faster and clearer.

```python
import numpy as np
risk = 0.04 * age + 0.3 * (sbp < 90)   # whole columns at once
```

You do not need deep NumPy yet. You need to recognise when you are looping by hand and a vector operation would be cleaner.

## Reading documentation

The real skill of M1 is learning to learn. When you meet a new library:

1. Find the official docs, not a random blog.
2. Read the quickstart and run it unchanged.
3. Change one thing and predict the result before you run it.
4. Search the API reference for the exact function, read its arguments.

An AI coding assistant accelerates this, but it will confidently invent functions that do not exist. The documentation is the source of truth. Verify before you trust.

## APIs and the cloud, briefly

An API is a way for your code to ask another system for something over the network. You send a request, you get structured data back.

```python
import requests
r = requests.get("https://api.example.org/patients/123")
data = r.json()
```

The cloud is just someone else's computers you rent: storage, compute, and services you reach through APIs. In M9 you will deploy to it. For now, know that "calling an API" and "running in the cloud" are ordinary, learnable things, not magic.

## Hands-on lab

Open **Notebook 1, Python and Data Science for Health**. You will load a synthetic admissions table, clean it, join it to a labs table, and compute a simple risk indicator. No prior Python required, every step is explained.

## Common pitfalls

- Trusting a number you got after editing cells out of order. Restart and run all.
- Silently dropping rows with missing data. In medicine, missingness is often informative. Look before you drop.
- Copying an assistant's code without reading it. If you cannot explain a line, you do not own it.

## Exercise

Take the admissions table from the lab. Answer three questions in code: what is the median length of stay by ward, what fraction of patients are 65 or older, and how many patients have at least one abnormal lab. Write one markdown sentence interpreting each.

## Further reading

- pandas official documentation, the "10 minutes to pandas" guide.
- The club's Notebook 1 solutions branch, after you attempt the lab.
