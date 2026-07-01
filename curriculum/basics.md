# Basics

Before you build anything clever, you need a workshop that does not scare you.
This domain gets you from nothing to a working setup, and to the small set of
skills every later domain assumes. None of it is hard. It is just unfamiliar,
and once it stops being unfamiliar you stop being afraid of the blank screen.

You do not need a computer science degree. Plenty of strong builders here are
doctors and nurses who started with no code at all.

```{note}
**Level** Beginner, no code required to start.
**Time** About 8 to 10 hours, spread over a week.
**Before you start** A laptop, a Google account, and one real annoyance from
your own work that you would like to fix.
```

## What you will be able to do

By the end of this module you will be able to:

1. Set up a working environment and a GitHub account without help.
2. Ship a small tool with no-code or an AI coding assistant, and not be afraid of it.
3. Save and version your work with Git, and read someone else's repository.
4. Call an API, including an AI model, and understand the response.
5. Explain, in plain words, what "the cloud" is and why where data lives is a
   clinical decision in Thailand, not only a technical one.

Keep that list. At the end you will check yourself against it.

## Sessions

Five short sessions. Each has a Read part, a hands-on part, and one thing you
finish. Do them in order.

| # | Session | Format | Time | You finish |
|---|---|---|---|---|
| 1 | Vibe coding and no-code | Read + build | ~2 hrs | A tiny working tool |
| 2 | Git and GitHub | Read + hands-on | ~1.5 hrs | A repo with a README |
| 3 | Reading docs and libraries | Read | ~1 hr | A doc you can navigate |
| 4 | APIs | Read + hands-on | ~2 hrs | One real API call |
| 5 | Cloud, and where data lives | Read | ~1.5 hrs | The safe-data habit |

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
**Try this now.** Open an AI coding assistant and ask it for a single-page
medication timing calculator: a drug, a dose interval, a first-dose time, and it
prints the next three doses. Do not aim for good. Aim for finished. You will
learn more from one finished tiny thing than from reading this whole page.
```

```{warning}
Never paste real patient data into a public AI tool while you are practising.
Use made-up names and numbers. We treat data properly in Digital Health and
Governance, but the safe habit starts here, on day one.
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
repository is as important as learning to write one. When you land on a new repo,
read three files first: the `README`, the folder names, and the most recently
changed file. That tells you what it is, how it is organised, and what someone
was working on last.

```{tip}
**Try this.** Make a GitHub account. Create one repository called `my-first-tool`.
Put the calculator you built above into it with a one-paragraph README. That
repository is the first line of your portfolio, and the Fellowship reads
portfolios.
```

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

Understand five things and you can connect almost anything to anything:

- **Request.** What you send: a URL, a method (get or post), and sometimes a body.
- **Response.** What comes back, with a status code. `200` is fine, `401` means
  your token is wrong, `429` means you are calling too fast.
- **JSON.** The structured text most APIs speak. Nested keys and lists, nothing more.
- **Authentication.** A token that proves who you are. Treat it like a password.
- **Rate limits.** How often you may call before you are told to wait.

```{tip}
**Try this.** Get a free API key for an AI model and send it one message from the
code above, adapted to that model. When you see a real JSON answer print in your
terminal, you have crossed the line from user to builder.
```

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
a technical one. Thai patient data carries obligations under the PDPA, and some
data cannot leave the hospital or the country. We come back to this in Digital
Health and in Governance, where PDPA and data residency set hard limits. For
now, learn the cloud on synthetic or open data only.
```

## Common mistakes

The ones we see every cohort, so you can skip them:

- **Aiming too big.** A tool that does one thing and is finished beats an
  ambitious thing that is never done. Shrink the scope until you can finish.
- **Not committing often.** Commit when something works, with a clear message.
  Your future self, debugging at midnight, will thank you.
- **Trusting the assistant blindly.** AI writes plausible code that is sometimes
  wrong. Read it, run it, and test it on an example you understand.
- **Practising on real data.** Do not. Use synthetic data until Governance says
  otherwise, and it will say otherwise only with the right basis in place.

## Check yourself

You are done with Basics when you can honestly say yes to each:

- [ ] I have a GitHub account and one repository with a README.
- [ ] I shipped one tiny tool that fixes a real annoyance from my work.
- [ ] I can make a commit and push it without looking up the commands each time.
- [ ] I called an API and can explain the response I got back.
- [ ] I can say why, in a Thai hospital, where data lives is not only a technical
      choice.

If any box is empty, that is your next hour of work. Do not move on around it.

## What you build

By the end of Basics you will have set up Git and GitHub, called an AI API, and
shipped one tiny no-code or vibe-coded tool that solves a real annoyance from
your own work. Put it in a repository with a README. That is your first artefact,
and every later domain adds to it.

## Resources

- **GitHub** and the GitHub Docs "Hello World" guide, for Git and repositories.
- **Google Colab**, for running Python in your browser with no setup.
- The **quickstart** page of any library before its full reference.
- Your AI coding assistant of choice, read critically, never pasted with real data.

## Where this goes next

Basics feeds everything. With a workshop you are not afraid of, move on to
[AI Agent](ai-agent.md) to build something that thinks, or to
[Digital Health](digital-health.md) to learn the data you will build on.
