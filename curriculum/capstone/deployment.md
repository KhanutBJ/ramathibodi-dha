# Week 8: Deployment

<p class="dha-eyebrow">Capstone / Week 8</p>

<p class="dha-lead">โมเดลที่ดีที่สุดไม่มีค่าถ้าไม่มีใครได้ใช้ สัปดาห์สุดท้ายเราเปลี่ยน Notebook ให้กลายเป็นเว็บแอปที่คนทั่วไปใช้งานได้ และ deploy ขึ้นออนไลน์</p>

---

## จาก Notebook สู่ App

<div class="dha-timeline">
  <div class="dha-step">
    <div class="dha-step__week">01</div>
    <h4>แยก inference ออกจาก training</h4>
    <p>เก็บเฉพาะส่วนที่จำเป็นสำหรับการทำนาย โหลดโมเดลที่ train แล้ว</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">02</div>
    <h4>สร้าง UI ด้วย Gradio</h4>
    <p>เพิ่มหน้าจอให้ผู้ใช้ป้อนข้อมูลและเห็นผลลัพธ์</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">03</div>
    <h4>เขียน requirements.txt</h4>
    <p>ระบุไลบรารีที่ต้องใช้เพื่อให้รันที่ไหนก็ได้</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">04</div>
    <h4>Deploy บน Hugging Face Spaces</h4>
    <p>push โค้ดขึ้น Spaces แล้วได้ลิงก์ที่แชร์ได้ทันที</p>
  </div>
</div>

---

## ตัวอย่าง: Gradio App

```python
import gradio as gr
import joblib

model = joblib.load("risk_model.pkl")

def predict(age, bmi, glucose, bp):
    risk = model.predict_proba([[age, bmi, glucose, bp]])[0, 1]
    level = "สูง" if risk > 0.7 else "กลาง" if risk > 0.3 else "ต่ำ"
    return f"ความเสี่ยง: {risk:.1%} (ระดับ{level})"

demo = gr.Interface(
    fn=predict,
    inputs=["number", "number", "number", "number"],
    outputs="text",
    title="เครื่องมือประเมินความเสี่ยงเบาหวาน",
    description="สำหรับการศึกษาเท่านั้น ไม่ใช้แทนการวินิจฉัยของแพทย์",
)
demo.launch()
```

```{warning} เครื่องมือสาธิต ≠ เครื่องมือทางการแพทย์
ต้นแบบที่สร้างในหลักสูตรเป็นเพื่อการศึกษา การนำไปใช้กับผู้ป่วยจริงต้องผ่าน clinical validation และการกำกับดูแลตามที่เรียนใน [AI Ethics](ethics.md)
```

---

## ขั้นต่อไป

<div class="dha-cta">
  <div>
    <h3>นำเสนอผลงานของคุณ</h3>
    <p>ส่งโปรเจกต์เข้า Showcase และเปิดโอกาสต่อยอดสู่ Fellowship หรือ Venture Builder</p>
  </div>
  <a class="dha-btn dha-btn--primary" href="../../community/showcase.html">ไปที่ Showcase →</a>
</div>
