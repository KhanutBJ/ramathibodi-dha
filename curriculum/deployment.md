# Deployment

A model in a notebook helps no one. Deployment is the craft of putting your work
in front of real users, in a form they can use, and then measuring whether it
actually helped. Most clinical AI dies here, not because the model was bad, but
because it never reached a workflow. This domain is how yours does not.

## Dashboards and visualisation

The first way most clinical AI reaches people is a dashboard. A good dashboard
answers a clinical question at a glance and earns trust by being honest about
uncertainty.

- **Tools.** Streamlit and Gradio for fast Python apps, Plotly and Altair for
  charts, Power BI or Looker Studio for operational reporting.
- **Principles.** One question per view. Show the denominator. Show uncertainty.
  Never a number without context.

```python
import streamlit as st
st.metric("Predicted 30-day readmission risk", "18%", help="Calibrated, n=1,204")
st.caption("Model v0.3 / external test AUROC 0.79 / for clinician review only")
```

## Web prototyping

To get feedback you need something people can click. You will learn to stand up a
working prototype fast: a front end people can use, a small API behind it, and a
model endpoint it calls.

- **Front end.** A simple page, or a Streamlit and Gradio app, or a no-code tool.
- **API.** FastAPI is the standard for serving a Python model.
- **The loop.** Ship a rough version, watch a real clinician use it, fix the
  thing that confused them, repeat.

```python
from fastapi import FastAPI
app = FastAPI()

@app.post("/predict")
def predict(features: dict):
    risk = model.predict_proba([to_vector(features)])[0][1]
    return {"risk": round(float(risk), 3), "model": "v0.3"}
```

## Cloud and on-premise

Where your tool runs is a clinical and legal decision as much as a technical one.

- **Cloud.** Fast to start, scales easily. Cloud Run, managed endpoints, and
  serverless functions. Watch data residency and PDPA.
- **On-premise.** Inside the hospital network, behind its firewall. Often
  required for the most sensitive data. Harder to run, sometimes the only option.
- **Hybrid.** Train in the cloud on de-identified data, serve on-premise.

You will learn containers (Docker) so the same tool runs the same way in both
places, and the basics of monitoring so you know when a deployed model drifts.

## Statistics that hold up

Deployment is where bad statistics get people hurt, so this domain insists on the
numbers being honest.

- **The right metric.** AUROC, sensitivity, specificity, PPV and NPV, and why
  prevalence makes PPV move. Calibration, not just discrimination.
- **Uncertainty.** Confidence intervals on every headline number.
- **Comparison.** Against the current standard of care, not against nothing.
- **Subgroups.** Does it work as well for women, for the elderly, for the poor.
  A model that helps on average and harms a subgroup is not good enough.
- **Prospective evaluation.** Retrospective performance is a promise. Prospective
  performance is the truth. The strongest projects end with a prospective look.

```{important}
The question is never just "is the model accurate." It is "does using this tool
change a decision, and does that change help the patient." Design the evaluation
to answer that.
```

## What you build

Take your trained model and ship it: a Streamlit or Gradio app backed by a FastAPI
endpoint in a Docker container, deployed to Cloud Run, with an honest results
panel showing the metric, its confidence interval, and the population it was
tested on.

## Where this goes next

A deployed, evaluated tool is ready for the hardest questions, which live in
[Strategy and Governance](governance.md): may you use it, and how do you get it
approved. From there, choose a [pathway](../pathways/startup.md).
