# Capstone: from notebook to shipped app

The best model in the world is worth nothing if nobody can use it. This final
session turns your notebook into a working app that a real person, not just
you, can open and try. This is the smallest, fastest version of the deployment
craft you learned in full in [Deployment](../deployment.md), sized for a
capstone project rather than a production hospital system.

```{note}
**Level** All levels. **Prerequisite** [AI Ethics](ethics.md), and a trained
model or working notebook.
**Time** ~1 week, self-paced. **Sessions** 1.
**Before you start** A saved model file and a completed Responsible AI Checklist.
```

## What you will be able to do

1. Separate inference from training so your app only carries what it needs to run.
2. Build a usable interface with Gradio in under an hour.
3. Package your app so it runs the same way anywhere.
4. Ship it somewhere a real person can open a link and try it.

## From notebook to app, in four steps

1. **Separate inference from training.** Keep only what is needed to make a
   prediction: load the already-trained model, do not retrain it every time
   someone opens the app.
2. **Build a UI with Gradio.** Add a simple screen where a user enters
   information and sees a result.
3. **Write a requirements.txt.** List every library your app needs, so it runs
   the same way anywhere, not just on your machine.
4. **Deploy.** Push your code to a hosting platform like Hugging Face Spaces
   and get a link you can actually share.

## A working example

```python
import gradio as gr
import joblib

model = joblib.load("risk_model.pkl")

def predict(age, bmi, glucose, bp):
    risk = model.predict_proba([[age, bmi, glucose, bp]])[0, 1]
    level = "high" if risk > 0.7 else "medium" if risk > 0.3 else "low"
    return f"Risk: {risk:.1%} ({level})"

demo = gr.Interface(
    fn=predict,
    inputs=["number", "number", "number", "number"],
    outputs="text",
    title="Diabetes risk estimator",
    description="For educational use only. Not a substitute for clinical diagnosis.",
)
demo.launch()
```

Notice what this app does not do: it does not claim to diagnose anything, and
it says so directly in the interface. That line is not decoration. It is the
scope discipline from [Governance](../governance.md), applied to a student
project.

```{warning}
**A demo tool is not a medical tool.** Prototypes built in this curriculum are
for education. Using anything like this on a real patient requires clinical
validation and the regulatory path covered in [AI Ethics](ethics.md) and in
full in [Strategy and Governance](../governance.md). Say so, clearly, in your
own app's description, the way the example above does.
```

## Common mistakes

- **Shipping the training code with the app.** Your deployed app should load a
  saved model, not retrain from scratch every time it starts.
- **Forgetting the requirements file.** An app that only runs on your laptop
  is not deployed, it is just running.
- **Skipping the disclaimer.** Every educational prototype should state
  plainly, in the interface itself, that it is not a clinical tool.
- **Treating "it works on my machine" as done.** Test the deployed link, not
  just the local notebook, before you call it finished.

## Check yourself

- [ ] My app loads a saved model rather than retraining on launch.
- [ ] I have a working, shareable link to my deployed app.
- [ ] My interface states clearly that it is for education, not clinical use.
- [ ] I can explain, in one sentence, what my app does and does not claim to do.

## What you build

A deployed, shareable app for your capstone project: a Gradio interface backed
by your trained model, with a clear non-clinical disclaimer, live at a link you
can send to anyone.

## Present your work

Share your finished project with your cohort and the club's community
channels. The strongest capstones become the seed of a
[Fellowship](../../fellowship.html) project, or, if there is real product
potential, move toward the [Venture Studio](../../venture.html).

## Where this goes next

You have completed the full Academy curriculum: from
[Basics](../basics.md) through [Strategy and Governance](../governance.md) to a
shipped, working project. Choose your
[pathway](../../pathways/startup.md), or apply what you built as the seed of a
Fellowship project.
