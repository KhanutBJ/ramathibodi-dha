# What is AI, really

Before you build with AI, you need an honest mental model of what it is and what
it is not. Most confusion in medical AI, and most of the danger, comes from
people treating a statistical pattern-matcher as if it understands medicine. It
does not. Once you see clearly what these systems actually do, you make better
and safer decisions with them.

```{note}
**Level** Beginner. **Prerequisite** None.
**Time** ~2 to 3 hours. **Sessions** 2.
**Before you start** Nothing to install. Bring curiosity and a real clinical
annoyance you would like a computer to help with one day.
```

## What you will be able to do

1. Explain, without jargon, the difference between AI, machine learning, deep
   learning, and large language models.
2. Name the three ways people build with today's models, and when to use each.
3. Classify a clinical problem as classification, regression, or generation.
4. State, in one paragraph, why prediction is not understanding, and why that
   matters at the bedside.

## Sessions

| # | Session | Format | Time | You finish |
|---|---|---|---|---|
| 1 | The AI family tree | Read | ~1 hr | The four-level map, in your own words |
| 2 | Prediction vs. understanding | Read + exercise | ~1.5 hrs | Three problems, correctly classified |

## The one-sentence definition

Artificial intelligence is software that learns patterns from data and uses
those patterns to make predictions or decisions, instead of following rules a
human wrote by hand.

A traditional program is a list of instructions: if the temperature is above
38, flag a fever. An AI system is not told the rule. It is shown thousands of
examples and works out a rule of its own, one that can be far more subtle than
anything a person would write, and also far stranger.

## The family tree

Everything in "AI" nests inside something bigger:

```
Artificial Intelligence (AI)
└── Machine Learning (ML)
    └── Deep Learning (DL)
        └── Large Language Models (LLM)
```

| Level | Definition | Medical example |
|---|---|---|
| **AI** | Any system whose behaviour looks like it requires intelligence | A diagnosis-support system |
| **ML** | Learns patterns from data instead of hand-written rules | Predicting diabetes risk from lab results |
| **DL** | ML using neural networks with many layers | Reading a chest X-ray |
| **LLM** | Deep learning trained on huge amounts of text | Summarising a medical record, answering a clinical question |

You will meet all four levels in this curriculum. Classic ML on tabular data
(labs, vitals, demographics) is the quiet workhorse of clinical prediction.
Deep learning reads images, signals, and sound. LLMs read and write language and
power the assistants you build in [AI Agent](../ai-agent.md).

```{note}
"AI" in the news usually means the LLM layer. In a hospital, the ML layer,
tabular models, quietly does more real work. Do not let the hype pull you
toward a complicated tool when a simple one wins.
```

## Three ways to build

You rarely start from nothing. There are three levels of effort, and each has
its place.

| Approach | What it means | Trade-off |
|---|---|---|
| **Train from scratch** | Build and train a model entirely on your own data | Full control, but needs the most data and compute |
| **Fine-tune** | Take a pretrained model and adapt it with your own, smaller dataset | The best balance for most clinical projects |
| **Prompt / API** | Call a large existing model with instructions, no training | Fastest to start, best for prototypes and language tasks |

```{tip}
Start every project one level down from where you think you need to be. Most
clinical problems that feel like they need training from scratch can be solved,
at least as a first prototype, by prompting an existing model or fine-tuning a
small one. Prove the idea cheaply before you spend on the expensive route.
```

## Classify before you build

Every AI task is one of three shapes. Naming the shape correctly is the first
real decision in any project, because it decides which models and which metrics
apply.

- **Classification.** Predicting a category. *Is this patient high, medium, or
  low risk?*
- **Regression.** Predicting a continuous number. *What will this patient's
  blood glucose be in six months?*
- **Generation.** Producing new content. *Summarise this patient's treatment
  history in one paragraph.*

```python
# Classification: predict a category
# e.g. Is this patient high risk, medium risk, or low risk?

# Regression: predict a continuous number
# e.g. What will this patient's blood glucose be in six months?

# Generation: produce new content
# e.g. Summarise this patient's treatment history in one paragraph.
```

```{tip}
**Try this now.** Classify each of these as classification, regression, or
generation, before you read on:
1. Predicting whether a patient will be readmitted within 30 days.
2. Estimating length of stay, in days.
3. Drafting a referral letter from a doctor's notes.

(1 is classification, 2 is regression, 3 is generation. If you got all three,
you are ready for the rest of this domain.)
```

## Prediction is not understanding

This is the most important idea in the whole curriculum, so sit with it.

A model that predicts sepsis has never seen a patient, felt a fever, or read a
textbook. It has seen numbers that, in its training data, tended to come before
a sepsis label. It is matching patterns, not reasoning about biology. Three
consequences follow, and you must internalise all three:

- **It learns the data's biases.** If the training data under-tested a group,
  the model will under-predict for that group, faithfully and invisibly.
- **It fails silently outside its experience.** Show it a patient unlike
  anything in training and it still outputs a confident number. It does not
  know that it does not know.
- **Correlation is all it has.** It may key on the scanner, the ward, or the
  time of day, anything that happened to correlate with the label, not the
  disease itself.

```{warning}
A clinician who remembers that a model is a pattern-matcher, not a colleague,
will use it well. One who forgets will be misled by it. Keep this sentence
somewhere you will see it again: **the model does not know what it does not
know.**
```

## Where AI helps in medicine today

- **Perception at scale.** Reading images and signals faster than humans can,
  as a second reader.
- **Risk from many small signals.** Combining dozens of weak clues in tabular
  data into one useful number.
- **Language and admin.** Drafting notes, summarising records, routing
  messages, especially valuable for Thai-language clinical text, which is
  underserved by most global tools.

And where it does not help yet: anywhere that needs genuine reasoning about a
novel situation, or where being confidently wrong is unacceptable and cannot be
caught by a human in time.

## Common mistakes

- **Treating "AI" as one thing.** A chatbot and a sepsis risk score are built,
  evaluated, and governed completely differently. Always name the level:
  classic ML, deep learning, or LLM.
- **Reaching for the biggest model first.** Start with prompting or a small
  fine-tune. Escalate only when a simpler approach genuinely fails.
- **Confusing correlation with causation.** A model finding a pattern does not
  mean it found a cause. You will return to this in [Evaluation](evaluation.md).

## Check yourself

- [ ] I can draw the AI, ML, DL, LLM nesting diagram from memory.
- [ ] I can explain train-from-scratch, fine-tune, and prompt in one sentence each.
- [ ] I can classify a new clinical problem as classification, regression, or generation.
- [ ] I can explain, to a classmate, why prediction is not understanding.

## What you build

A one-paragraph write-up of a clinical problem from your own experience,
naming its AI family (ML, DL, or LLM), its shape (classification, regression,
generation), and one way the model could fail silently.

## Where this goes next

Now that you know what these systems are, set up your tools in
[How to do AI](how-to-ai.md), then learn the two things that decide whether a
model works: [datasets](datasets.md) and [evaluation](evaluation.md).
