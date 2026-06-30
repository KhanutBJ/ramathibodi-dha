# Week 1: What is AI?

<p class="dha-eyebrow">Foundation / Week 1</p>

<div class="dha-pill-row">
  <span class="dha-pill">เริ่มต้น</span>
  <span class="dha-pill dha-pill--green">3 ชม.</span>
</div>

<p class="dha-lead">คำว่า "AI" ถูกใช้กว้างมากจนสับสน สัปดาห์นี้เราจะแยกแยะให้ชัดว่า AI, Machine Learning, Deep Learning และ LLM ต่างกันอย่างไร และเลือกใช้ให้เหมาะกับโจทย์สุขภาพ</p>

---

## ลำดับชั้นของแนวคิด

```
Artificial Intelligence (AI)
└── Machine Learning (ML)
    └── Deep Learning (DL)
        └── Large Language Models (LLM)
```

| ระดับ | นิยาม | ตัวอย่างทางการแพทย์ |
|---|---|---|
| **AI** | ระบบที่ทำงานต้องใช้ "ความฉลาด" | ระบบช่วยวินิจฉัย |
| **ML** | เรียนรู้รูปแบบจากข้อมูล โดยไม่เขียน rule เอง | ทำนายความเสี่ยงเบาหวานจากผลแล็บ |
| **DL** | ML ที่ใช้ neural network หลายชั้น | อ่านฟิล์ม X-ray |
| **LLM** | DL ที่เข้าใจและสร้างภาษา | สรุปเวชระเบียน ตอบคำถามทางคลินิก |

---

## สามแนวทางการพัฒนา AI ยุคปัจจุบัน

<div class="dha-grid dha-grid--3">
  <div class="dha-card">
    <div class="dha-card__icon">🏗️</div>
    <h3>Train from scratch</h3>
    <p>สร้างและฝึกโมเดลเองทั้งหมด ควบคุมได้สูงสุด แต่ใช้ข้อมูลและทรัพยากรมาก</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--green">🔧</div>
    <h3>Fine-tune</h3>
    <p>นำโมเดลสำเร็จรูปมาปรับด้วยข้อมูลเฉพาะทาง สมดุลที่ดีที่สุดสำหรับงานคลินิก</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--coral">💬</div>
    <h3>Prompt / API</h3>
    <p>เรียกใช้โมเดลขนาดใหญ่ผ่าน prompt, เริ่มเร็วที่สุด เหมาะกับ prototype</p>
  </div>
</div>

---

## ตัวอย่าง: จำแนกประเภทปัญหา

```python
# ปัญหาแบบ Classification, ทำนายหมวดหมู่
# เช่น: ผู้ป่วยรายนี้มีความเสี่ยงสูง/กลาง/ต่ำ?

# ปัญหาแบบ Regression, ทำนายตัวเลขต่อเนื่อง
# เช่น: ค่าน้ำตาลในเลือดอีก 6 เดือนจะเป็นเท่าไร?

# ปัญหาแบบ Generation, สร้างเนื้อหาใหม่
# เช่น: สรุปประวัติการรักษาของผู้ป่วยเป็นย่อหน้า
```

```{note} แบบฝึกหัด
ลองจำแนกว่าโจทย์ต่อไปนี้เป็น Classification, Regression หรือ Generation:
1. ทำนายว่าผู้ป่วยจะ readmit ภายใน 30 วันหรือไม่
2. ประเมินระยะเวลานอนโรงพยาบาล (จำนวนวัน)
3. ร่างจดหมายส่งต่อผู้ป่วยจากบันทึกแพทย์
```

---

## สรุป

- AI เป็นร่มใหญ่ ML/DL/LLM เป็นเครื่องมือย่อยที่ต่างกัน
- เลือกแนวทาง (scratch / fine-tune / prompt) ตามข้อมูลและทรัพยากรที่มี
- การจำแนกประเภทโจทย์ให้ถูกคือก้าวแรกที่สำคัญที่สุด

ถัดไป: [Datasets & Habitats](datasets.md) →
