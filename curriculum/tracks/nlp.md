# Track: Natural Language Processing

<p class="dha-eyebrow">Specialization / NLP</p>

<div class="dha-pill-row">
  <span class="dha-pill dha-pill--coral">กลาง-ขั้นสูง</span>
  <span class="dha-pill dha-pill--green">3 สัปดาห์</span>
</div>

<p class="dha-lead">ปลดล็อกข้อมูลในรูปข้อความ เวชระเบียน บันทึกแพทย์ และเอกสารทางคลินิก ด้วย Transformers และ LLM เพื่อเปลี่ยนข้อความให้เป็นข้อมูลเชิงลึกที่ใช้ได้</p>

---

<div class="dha-timeline">
  <div class="dha-step">
    <div class="dha-step__week">Week 4</div>
    <h4>NLP Overview & Transformers</h4>
    <p>การประยุกต์ NLP, embeddings, word representations และสถาปัตยกรรม Transformer</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">Week 5</div>
    <h4>Encoder-Only Models & Hugging Face</h4>
    <p>Fine-tune encoder-only model สำหรับ text classification, ระบบ Hugging Face (transformers, datasets, tokenizers)</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">Week 6</div>
    <h4>Large Language Models & GPT</h4>
    <p>วิธีการ train LLM, prompt engineering และ Retrieval Augmented Generation</p>
  </div>
</div>

---

## ตัวอย่าง: วิเคราะห์บันทึกทางคลินิก

```python
from transformers import pipeline

# จำแนกความรู้สึก/ความเร่งด่วนจากบันทึก
ner = pipeline("ner", model="d4data/biomedical-ner-all", aggregation_strategy="simple")
note = "ผู้ป่วยมีไข้สูง 39 องศา ปวดศีรษะ และไอแห้งมา 3 วัน"
for ent in ner(note):
    print(f"{ent['word']} → {ent['entity_group']}")
```

---

## โปรเจกต์ตัวอย่าง (Health)

<div class="dha-grid dha-grid--2">
  <div class="dha-card">
    <h3>Clinical Note Summarizer</h3>
    <p>สรุปบันทึกแพทย์ยาว ๆ ให้เป็นสรุปสั้นกระชับสำหรับการส่งต่อ</p>
  </div>
  <div class="dha-card">
    <h3>ICD Coding Assistant</h3>
    <p>แนะนำรหัส ICD-10 จากข้อความวินิจฉัยอัตโนมัติ</p>
  </div>
</div>
