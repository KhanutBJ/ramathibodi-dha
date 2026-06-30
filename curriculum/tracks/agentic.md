# Track: Agentic AI

<p class="dha-eyebrow">Specialization / Agentic</p>

<div class="dha-pill-row">
  <span class="dha-pill dha-pill--coral">ขั้นสูง</span>
  <span class="dha-pill dha-pill--green">3 สัปดาห์</span>
</div>

<p class="dha-lead">สร้าง AI agent ที่คิด วางแผน และเรียกใช้เครื่องมือได้เอง ตั้งแต่ ReAct จากศูนย์ ไปจนถึง RAG และ tool calling, รากฐานของผู้ช่วยทางคลินิกอัจฉริยะ</p>

---

<div class="dha-timeline">
  <div class="dha-step">
    <div class="dha-step__week">Week 4</div>
    <h4>Building an Agent from Scratch</h4>
    <p>พื้นฐาน LLM, ReAct framework, Chain-of-Thought, few-shot prompting และ failure cases ที่พบบ่อย</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">Week 5</div>
    <h4>RAG & Automated Prompting</h4>
    <p>Deploy LLM ด้วย llama.cpp, สร้าง agent ด้วย LangGraph, RAG กับ vector database, prompt optimization ด้วย DSPy</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">Week 6</div>
    <h4>Programmatic Tool Calling</h4>
    <p>พัฒนา custom tool และผสาน ReAct + RAG + tool calling เป็น agent ที่ใช้งานจริง</p>
  </div>
</div>

---

## ตัวอย่าง: ReAct loop อย่างง่าย

```python
def react_agent(question, tools, llm):
    thought = llm(f"คำถาม: {question}\nคิดทีละขั้น แล้วเลือก tool ที่ต้องใช้:")
    while "FINAL" not in thought:
        action, arg = parse_action(thought)
        observation = tools[action](arg)        # เรียกใช้เครื่องมือ
        thought = llm(f"{thought}\nผลลัพธ์: {observation}\nคิดต่อ:")
    return extract_answer(thought)
```

---

## โปรเจกต์ตัวอย่าง (Health)

<div class="dha-grid dha-grid--2">
  <div class="dha-card">
    <h3>Clinical Q&A Agent</h3>
    <p>agent ที่ตอบคำถามจากแนวทางเวชปฏิบัติ ด้วย RAG บนเอกสาร guideline</p>
  </div>
  <div class="dha-card">
    <h3>Triage Assistant</h3>
    <p>ผู้ช่วยคัดกรองอาการเบื้องต้น เรียกใช้ tool คำนวณคะแนนความเสี่ยง</p>
  </div>
</div>

> 📓 ดูตัวอย่างที่ [Notebook: Intro to Clinical ML](../../notebooks/01-clinical-ml.html)
