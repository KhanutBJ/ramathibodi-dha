# Being a steward, after the launch is over

Every other lesson has prepared a tool to go live. This one is about what
happens for the years after that: who keeps watching, how bias gets audited
on an ongoing basis rather than once, and how an institution decides when a
model has quietly stopped being safe to trust. Stewardship is a distinct
competency from building or launching, and it is usually nobody's job unless
someone deliberately makes it theirs.

```{note}
**Level** Intermediate to advanced. **Prerequisite** [AI Ethics](../capstone/ethics.md).
**Time** ~2.5 hours. **Sessions** 1.
**Before you start** A deployed or soon-to-deploy tool to imagine stewarding.
```

## What you will be able to do

1. Explain why launch-day safety checks are not enough on their own.
2. Design a monitoring plan that would actually catch a model quietly failing.
3. Describe what an AI governance committee does and why one is needed.
4. Recognise the signs that a model should be retrained or retired.

## Why launch day is not the finish line

A model validated at launch was tested against the population and practices
of that moment. Populations shift, documentation habits change, a new patient
group starts arriving, and a hospital's own workflow evolves around the tool
in ways that change what data it sees. A model that was safe in January can be
quietly wrong by the following year, with nothing about its interface telling
anyone that happened. This is called drift, and stewardship exists to catch it.

```{warning}
The most dangerous failure mode is not a model that is obviously broken. It is
one that keeps producing confident, plausible-looking answers while its real
accuracy has silently degraded. Nothing about a wrong number looks different
from a right one, unless someone is watching for it.
```

## A monitoring plan that would actually work

"We will monitor it" is not a plan. A real one answers four questions in
advance:

1. **What signal would reveal a problem** (a performance metric on a rolling
   sample, a shift in the input data's distribution, a rise in overrides by
   clinicians).
2. **Who looks at that signal, and how often.** Weekly, monthly, on a
   dashboard someone actually opens.
3. **What threshold triggers action**, decided before the data exists, not
   argued about in the moment.
4. **What the action is**: retrain, restrict use, or pull the tool entirely.

```{tip}
Build the monitoring plan at the same time as the model, using the honest
statistics discipline from [Deployment](../deployment.md): the same
confidence intervals and subgroup breakdowns you reported at launch are what
you re-check on a schedule afterward.
```

## The governance committee, and why it is not bureaucracy

An AI governance committee is the standing group that owns the questions no
single builder or department should answer alone: which tools are approved
for use, what the monitoring plan requires, and what happens when something
goes wrong. It typically includes a clinician, a technical lead, someone
representing patient interests, and someone who understands the regulatory
picture from [Governance](../governance.md). Its job is not to slow things
down. It is to make sure the questions in this lesson have a named owner
instead of drifting to nobody.

```{important}
An institution with many AI tools and no governance committee is trusting
each individual builder's judgement, indefinitely, with no one checking that
judgement against the others. That does not scale past the first tool or two.
```

## Bias auditing as a practice, not a checkpoint

The fairness check in [Evaluation](../foundation/evaluation.md) and
[AI Ethics](../capstone/ethics.md) happens once, before launch. Stewardship
repeats it on a schedule, because a model's fairness can shift even when its
overall accuracy looks stable: a subgroup that was well represented at launch
can shrink or change, quietly reintroducing the exact bias the launch audit
cleared.

## When to retrain, restrict, or retire

- **Retrain** when performance has drifted but the underlying task and
  population are still a good fit for the tool.
- **Restrict** scope when the tool still works well for its original case but
  is being used, or drifting, beyond it.
- **Retire** when the cost of continued monitoring and correction exceeds the
  value the tool still provides, or when a better option has emerged. Retiring
  a tool responsibly, with a plan for what replaces it, is a steward's
  decision as much as launching one was.

## Common mistakes

- **Treating the launch validation as permanent.** It was true once, for a
  population and moment that has already started to change.
- **Monitoring accuracy but not fairness.** Both drift, and separately.
- **No named committee or owner**, so degradation is nobody's job to notice.
- **Being unwilling to retire a tool** that has been surpassed or has drifted
  past a safe threshold, out of sunk-cost attachment to the original build.

## Check yourself

- [ ] I can explain why a validated model can still fail a year later.
- [ ] I have a monitoring plan naming the signal, the owner, the threshold, and the action.
- [ ] I can describe what a governance committee owns that no single builder should decide alone.
- [ ] I can name the signs that would make me retrain, restrict, or retire a tool.

## What you build

A one-page stewardship plan for a deployed or soon-to-deploy tool: the
monitoring signal and schedule, the threshold that triggers action, and who
is named as the owner.

## Where this goes next

You now hold the complete arc: build, evaluate, deploy, govern, decide
strategically, and steward for the long run. From here, choose your
[pathway](../../pathways/startup.md), or take this discipline into your
[capstone](../capstone/index.md).
