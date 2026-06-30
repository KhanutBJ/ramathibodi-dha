# M5. Rule Engines and Gap Detection

**Week 2, Day 4 to 5.** Not every problem needs machine learning. Often the safest, most explainable, most deployable tool is a well-built set of rules. This module teaches you when to reach for rules, and how to build them well.

## The case for rules

A rule engine encodes clinical logic explicitly: if these conditions hold, raise this flag. Rules are transparent, auditable, easy to approve, and easy for clinicians to trust because they can read them. For care-gap detection, guideline checks, and safety alerts, a rule engine is frequently the right answer, and sometimes the only answer a hospital will accept.

The mature view: rules and models are partners, not rivals. Rules catch the known and the must-never-miss. Models catch the subtle and the statistical. Many real systems are a layer of rules with a model inside.

## Learning objectives

By the end of M5 you can:

- Decide between a rule engine, a model, or a hybrid for a given problem.
- Express clinical guidelines as clear, testable rules.
- Build a care-gap detector: find patients who should have had something and did not.
- Measure a rule set the same way you measure a model, and tune it.
- Keep rules maintainable as guidelines change.

## Rules or model: how to choose

Reach for **rules** when:

- The logic is known and written down (a guideline, a protocol, a safety limit).
- Every decision must be explainable and auditable.
- You cannot get enough labelled data to train.
- A miss is catastrophic and the rule is unambiguous.

Reach for a **model** when the pattern is statistical, subtle, and hidden in many weak signals, as in M4. Reach for a **hybrid** when you want a model's reach with a rule's guardrails.

## Encoding guidelines as rules

A clinical guideline becomes a set of conditions and actions.

```python
def diabetes_care_gaps(patient):
    gaps = []
    if patient["has_diabetes"]:
        if patient["months_since_hba1c"] is None or patient["months_since_hba1c"] > 6:
            gaps.append("HbA1c overdue")
        if not patient["had_eye_exam_12m"]:
            gaps.append("Annual eye exam missing")
        if patient["ldl"] is not None and patient["ldl"] > 100 and not patient["on_statin"]:
            gaps.append("LDL above target, not on statin")
    return gaps
```

Good rules are named, single-purpose, and traceable to a source guideline. Bad rules are tangled nests of nested conditions nobody can audit. Keep each rule readable on its own.

## Gap detection

Care-gap detection finds patients who, by guideline, should have received a test, a follow-up, or a treatment, and did not. It is high value and low risk because it suggests, it does not diagnose. The pattern:

1. Define the eligible population (who the guideline applies to).
2. Define the expected action and its time window.
3. Find the eligible patients with no record of the action.
4. Surface them to the right clinician, with the reason.

This is where many hospitals get their first real, trusted win from data, and it builds the credibility that later models need.

## Measuring and tuning rules

Rules are evaluated like any classifier. Run them against a labelled set and read precision and recall. A rule that flags everyone has perfect recall and zero usefulness. Tune the thresholds and the eligibility to balance catching real gaps against alarm fatigue. Track how many flags clinicians act on, the only metric that proves value.

## Maintainability

Guidelines change. A rule engine that nobody can safely update becomes a liability. Keep rules in one place, version them with Git, write a test for each rule with example patients, and record which guideline and which version each rule came from. When the guideline updates, you change one rule and the tests tell you what broke.

## Hands-on lab

Build a small care-gap detector for a chronic-disease cohort from synthetic data. Encode three guideline rules, run them, measure precision and recall against labels, and tune one threshold to cut false alarms.

## Common pitfalls

- Rules so tangled that no clinician will audit them. Keep each rule simple and named.
- No tests, so an update silently breaks a safety check.
- Flagging so much that clinicians ignore the system. Alarm fatigue kills adoption.

## Exercise

Pick a guideline you know (diabetes, hypertension, or antibiotic stewardship). Write three care-gap rules as named functions, each with two example patients as tests. State the eligible population and the time window for each.

## Further reading

- Clinical practice guidelines relevant to your cohort, as the source of truth for rules.
- The club's note on hybrid rule-plus-model systems.
