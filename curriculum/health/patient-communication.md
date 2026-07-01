# Talking to patients about AI, and who is liable

Every domain so far has taught you to build. This one teaches you what to say
and what you are responsible for once the tool is in the room with a patient.
This is the part of medical AI education that a technical course usually
skips, and the part a working clinician cannot skip: how do you explain an
AI-assisted decision to a patient, and if the AI is wrong, who answers for it.

```{note}
**Level** All levels. **Prerequisite** [Clinical AI](clinical-ai.md).
**Time** ~2 hours. **Sessions** 1.
**Before you start** Nothing technical. Bring a willingness to imagine the
conversation, not just the code.
```

## What you will be able to do

1. Explain, in plain language a patient can follow, that an AI tool contributed
   to their care.
2. Identify what informed consent should cover when AI is involved.
3. State the current, honest answer to "who is liable if the AI is wrong."
4. Recognise when a patient's discomfort with AI is a communication problem
   versus a genuine safety concern.

## Why this belongs in a technical curriculum

A model with excellent AUROC is not finished. It becomes real medicine only in
the moment a clinician uses it with a patient in the room. Every other domain
in this curriculum prepares the tool. This one prepares the conversation, and
it matters just as much: a patient who does not trust or understand an
AI-assisted recommendation may reasonably refuse it, no matter how accurate the
model is.

## Explaining AI-assisted care in plain language

Patients do not need to understand gradient descent. They need three things,
stated simply:

- **What the tool did.** "A computer program looked at your scan and flagged
  an area for me to look at more closely."
- **What it did not do.** "It does not make the diagnosis. I reviewed the flag
  and made the decision myself."
- **Why that is safe.** "This is the same kind of second check a specialist
  colleague might give, just faster."

```{tip}
Practise saying this out loud, not just reading it. "This tool helped me
review your case faster. I am the one who is deciding, and I am doubly careful
because of what it flagged." If that sentence feels awkward to say, the
project is not ready for patients yet, regardless of its metrics.
```

```{warning}
Never let "the AI said so" become the explanation. It is not an answer, and it
quietly transfers a decision that must stay with the clinician onto a tool that
cannot be held accountable. Say what the clinician decided and why, with the
AI framed as one input among several.
```

## What informed consent should cover

When an AI tool meaningfully shapes a decision, patients have a right to know.
A working standard, adapted for a Thai clinical setting:

1. **That a tool was used**, named plainly, not buried in fine print.
2. **What it does and does not decide.** Support, not autonomy, in almost every
   case you will build in this curriculum.
3. **What happens to their data**, tying directly back to the PDPA basis you
   learned in [Digital Health](../digital-health.md).
4. **That they can ask questions or decline**, and what the alternative is if
   they do.

```{important}
Consent is not a form signed once at admission. For a new or unfamiliar tool,
it is a conversation, however brief, at the point the tool is actually used.
The form protects the institution. The conversation protects the patient's
understanding, and only one of those is the actual point.
```

## Who is liable, honestly

This question does not yet have one clean, settled answer anywhere in the
world, and anyone who tells you otherwise is oversimplifying. What is true
today, and worth carrying into every project you build:

- **The clinician who acts on a recommendation is generally still
  accountable** for the decision, in the same way they would be for advice
  from a colleague or a lab result they chose to act on.
- **A tool used outside its stated intended use** (the scope discipline from
  [Governance](../governance.md)) shifts risk sharply toward whoever deployed
  it that way.
- **Documentation matters enormously.** Recording that a tool was used, what
  it output, and what the clinician independently decided is now part of
  defensible clinical practice, not paperwork for its own sake.
- **This is precisely why scope, human-in-the-loop, and the SaMD risk
  classification from Governance exist.** They are not bureaucratic hurdles.
  They are what keeps the liability picture answerable at all.

```{note}
As a general pattern, and not legal advice: the less autonomous the tool (an
assistant a clinician reviews, versus a system that decides), the clearer the
liability picture stays. This is one more reason the strongest capstones and
Fellowship projects keep a human decisively in the loop.
```

## When discomfort is a safety signal, not just a communication gap

Sometimes a patient's hesitation about an AI-assisted tool is really about
trust or unfamiliarity, and a clear explanation resolves it. Sometimes it is
telling you something real: that the tool has not been explained well enough
to be used responsibly, or that it should not have been used in that case at
all. Do not treat every objection as something to talk a patient out of. Ask
whether the objection is pointing at a real gap in your project's readiness.

## Common mistakes

- **Treating explanation as optional** because the tool is accurate. Accuracy
  and trust are different problems, and you need both.
- **Hiding behind the tool's authority** ("the AI recommended it") instead of
  owning the clinical decision.
- **A consent form with no conversation.** The signature is not the point.
- **Assuming liability disappears because a tool was involved.** It does not.
  It usually stays with the clinician, more clearly when scope was respected.

## Check yourself

- [ ] I can explain an AI-assisted decision to a patient in three plain sentences.
- [ ] I can list what informed consent should cover when AI is used.
- [ ] I can state, honestly, where liability usually sits and why scope matters to it.
- [ ] I can tell the difference between a patient's discomfort that needs
      better explanation and one that is flagging a real problem with the tool.

## What you build

Write the exact words you would say to a patient to introduce your own
capstone or Fellowship project in their care, in under thirty seconds, plus
one sentence on who remains accountable for the decision it supports.

## Where this goes next

You now hold the full picture: how to build a clinical AI tool, how to
evaluate it honestly, how to govern and deploy it responsibly, and how to
bring it into a real conversation with a real patient. Return to
[Clinical AI](clinical-ai.md) for the technical safety discipline, or move on
to your [capstone](../capstone/index.md).
