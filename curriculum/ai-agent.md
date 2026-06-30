# AI Agent

This is where most people feel the ground shift. Large language models can read,
write, reason over documents, talk, and take actions. An agent is an LLM given
tools, memory, and a goal. In a hospital that can mean drafting a discharge
summary, answering a patient on Line, or triaging a referral inbox.

It can also mean confidently inventing a drug dose. The whole craft is getting
the power without the harm. That is what this domain teaches.

## LLM basics

A large language model predicts the next token given everything before it. From
that one trick comes summarising, translating, extracting, and answering. You do
not need the maths to use one well, but you do need the mental model:

- The model has no memory between calls unless you give it one.
- Everything it knows about your task lives in the **context** you send.
- It does not know what it does not know. It will guess fluently.

Key controls you will use every day:

- **Prompt.** The instruction and the context you provide.
- **System prompt.** The standing role and rules.
- **Temperature.** How random the output is. Low for clinical work.
- **Tokens.** The unit of text, and the unit of cost and limits.

## Hallucination

A hallucination is a confident, wrong answer. In casual use it is annoying. In
medicine it is dangerous. You must assume the model can be wrong and design so
that a wrong answer is caught.

Where hallucinations come from:

- The answer was not in the context, so the model guessed.
- The question was ambiguous, so the model picked a reading.
- The model was pushed to always answer, so it never said "I do not know."

You reduce hallucination with grounding (give the model the source), with
permission to abstain, and with verification (check the answer against the
source before showing it).

```{warning}
Never put an ungrounded LLM between a patient and a decision. Every clinical
output needs a source it can be checked against and a human who signs off.
```

## Guardrails

Guardrails are the rules and checks that sit around the model so it behaves. They
are not optional in healthcare.

- **Input guardrails.** Strip or flag protected information, block out-of-scope requests.
- **Output guardrails.** Check format, check for unsupported claims, refuse when uncertain.
- **Scope limits.** The assistant answers logistics, not diagnosis, unless a clinician is in the loop.
- **Logging.** Every interaction is recorded so it can be audited and improved.

## RAG: retrieval augmented generation

RAG is how you make a model answer from your documents instead of from its
training. You retrieve the relevant passages from your own knowledge base, put
them in the context, and ask the model to answer using only those passages.

The pipeline:

1. Split your documents (guidelines, formularies, SOPs) into chunks.
2. Turn each chunk into an embedding and store it in a vector database.
3. At question time, embed the question, find the closest chunks, and pass them in.
4. Ask the model to answer from those chunks and cite them.

```python
# sketch of a RAG step
chunks = vector_db.search(embed(question), k=5)
answer = llm.complete(
    system="Answer only from the provided sources. If unsure, say so.",
    context=chunks,
    question=question,
)
```

RAG is the single most useful pattern for clinical assistants, because it keeps
the answer tied to a source you control and can update.

## Context and loop engineering

Getting good results is less about clever prompts and more about managing what
goes into the context and how the model loops over a task.

- **Context engineering.** Decide what the model sees: the right documents, the
  right examples, the patient summary and nothing it should not have.
- **Loop engineering.** Many tasks are not one call. The agent plans, calls a
  tool, reads the result, and decides the next step. You design that loop, set a
  stopping condition, and keep a human checkpoint where it matters.

## Speech: TTS and STT (ASR)

Voice is how medicine actually runs. Two capabilities matter:

- **STT / ASR (speech to text).** Transcribe a consultation or a ward round.
  Thai and code-switched Thai-English are the real challenge. You will evaluate
  models on Thai medical speech, not just English benchmarks.
- **TTS (text to speech).** Read instructions back to a patient, useful for
  accessibility and for low-literacy settings.

A transcription assistant that produces a structured note from a Thai
consultation is one of the highest-value things a fellow can build.

## Building real agents: Line, n8n, Cloud Run, OpenClaw

Thailand runs on Line, so that is where a patient-facing agent often lives.

- **Line agent.** Use the Line Messaging API to put an assistant where patients
  and staff already are. Appointment reminders, triage intake, follow-up.
- **n8n.** A visual automation tool. Wire together triggers, the model, a
  database, and Line without writing a full backend. Excellent for prototypes
  and for real internal workflows.
- **OpenClaw and agent frameworks.** Orchestration for multi-step agents that
  call tools and keep state.
- **Cloud Run.** Google Cloud's way to run your service in a container that
  scales to zero when idle. Cheap, simple, production-grade. A good first
  deployment target for a Line webhook or an API.

```{tip}
A realistic first agent: a Line bot, backed by an n8n flow, running on Cloud Run,
that answers appointment and preparation questions from your department's own FAQ
using RAG. Useful, shippable, and safe because it never diagnoses.
```

## Human in the loop

The most important design choice in clinical AI is where the human sits. Human in
the loop means a person reviews or approves before an action with clinical
consequence happens. The model drafts, the clinician decides.

Design the checkpoint deliberately: what the human sees, how fast they can
approve or reject, and how their corrections feed back to improve the system.

## Basic ML, in this context

Not everything needs an LLM. A lot of clinical prediction is better served by a
simple, interpretable model on tabular data. You will learn when to reach for
classic machine learning instead of a language model, and how to combine them:
an LLM to read the note, a calibrated model to make the prediction.

This connects directly to [Deep AI](deep-ai.md), where you train these models
properly.

## What you build

A supervised assistant that does one real job end to end: grounded in your own
documents with RAG, wrapped in guardrails, reachable on Line, deployed on Cloud
Run, with a human checkpoint before anything that touches care.

## Where this goes next

Take the assistant into [Deployment](deployment.md) to measure whether it helps,
and into [Strategy and Governance](governance.md) to understand what it would
take to use it for real.
