# Basics

Before you build anything clever, you need a workshop that does not scare you.
This domain gets you from nothing to a working setup, and to the small set of
skills every later domain assumes. None of it is hard. It is just unfamiliar,
and once it stops being unfamiliar you stop being afraid of the blank screen.

You do not need a computer science degree. Plenty of strong builders here are
doctors and nurses who started with no code at all.

## Vibe coding and no-code

The fastest way to feel what software can do is to make some without writing
much. Modern tools let you describe what you want in plain language and get a
working app back.

- **No-code builders** like Glide, Bubble, and Google AppSheet turn a spreadsheet
  into an app. Good for a quick clinic tool, a registry, a simple form.
- **Vibe coding** with an AI assistant (Claude, Cursor, GitHub Copilot, Google
  AI Studio) lets you build real software by conversation. You still need to
  read what it produces, but you can start today.

The point is not to avoid code forever. It is to remove the fear, ship something
small, and learn what to ask for next.

```{tip}
Your first project should be useful and tiny. A medication timing calculator, a
ward handover form, a simple triage checklist. Finish one small thing.
```

## Git

Git is how you save your work properly and how you work with other people
without overwriting each other. Think of it as a lab notebook for code that
remembers every version.

You need four ideas, no more, to start:

1. **Repository.** A project folder that Git is watching.
2. **Commit.** A saved snapshot with a message describing what changed.
3. **Push and pull.** Send your commits to GitHub, get other people's down.
4. **Branch.** A safe copy where you try something without breaking the main version.

```bash
git clone https://github.com/your-org/your-project.git
git checkout -b my-feature
git add .
git commit -m "Add triage form"
git push origin my-feature
```

GitHub is where the world's medical AI is built in the open. Learning to read a
repository is as important as learning to write one.

## Reading libraries and documentation

A library is code other people wrote so you do not have to. You will use many:
pandas for tables, scikit-learn for models, FastAPI for web services. The skill
that matters is not memorising them. It is reading their documentation quickly.

How to read docs without drowning:

- Start with the quickstart, not the full reference.
- Run the first example before you read the second paragraph.
- Search the error message, then the docs, then ask.

```{note}
Half of real engineering is reading. Good builders are fast readers of other
people's code and docs, not people who have memorised everything.
```

## APIs

An API is a way for one program to ask another program for something. When your
app calls an AI model, looks up a drug interaction, or reads a patient record
from the hospital system, it is calling an API.

The shape is almost always the same: you send a request to a URL with some data,
you get a structured answer back, usually as JSON.

```python
import requests

r = requests.get(
    "https://api.example-health.org/patient/123/observations",
    headers={"Authorization": "Bearer YOUR_TOKEN"},
)
data = r.json()
print(data["observations"][0])
```

Understand requests, responses, JSON, authentication tokens, and rate limits and
you can connect almost anything to anything.

## Cloud

The cloud is just someone else's computer that you rent by the minute. You use
it so you do not have to keep your laptop running, and so others can reach your
tool.

What to know at this stage:

- **Compute.** A virtual machine or a container that runs your code.
- **Storage.** A bucket where files and data live.
- **Managed services.** Databases, model endpoints, and pipelines you do not
  have to run yourself.

The big three are Google Cloud, AWS, and Azure. Because one of our partners is
the Google Developer Group on campus, the Academy leans on Google Cloud and
Colab for hands-on work, but the ideas transfer everywhere.

```{important}
In healthcare, where your data lives is a clinical and legal decision, not just
a technical one. We come back to this in Digital Health and in Governance, where
PDPA and data residency set hard limits.
```

## What you build

By the end of Basics you will have set up Git and GitHub, called an AI API, and
shipped one tiny no-code or vibe-coded tool that solves a real annoyance from
your own work.

## Where this goes next

Basics feeds everything. With a workshop you are not afraid of, move on to
[AI Agent](ai-agent.md) to build something that thinks, or to
[Digital Health](digital-health.md) to learn the data you will build on.
