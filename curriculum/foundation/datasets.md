# Week 2: Datasets & Habitats

<p class="dha-eyebrow">Foundation / Week 2</p>

<div class="dha-pill-row">
  <span class="dha-pill">เริ่มต้น-กลาง</span>
  <span class="dha-pill dha-pill--green">3 ชม.</span>
</div>

<p class="dha-lead">โมเดลดีแค่ไหนขึ้นอยู่กับข้อมูลที่ป้อนให้ สัปดาห์นี้เรียนรู้ว่าจะหา ทำความสะอาด และเตรียมชุดข้อมูลสุขภาพอย่างไรให้พร้อมใช้ พร้อมประเด็นจริยธรรมและลิขสิทธิ์</p>

---

## แหล่งข้อมูล

<div class="dha-grid dha-grid--3">
  <div class="dha-card">
    <div class="dha-card__icon">🌐</div>
    <h3>Open Repositories</h3>
    <p>Hugging Face Datasets, Kaggle, PhysioNet, MIMIC สำหรับข้อมูลทางการแพทย์</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--green">🕸️</div>
    <h3>Web Scraping</h3>
    <p>เก็บข้อมูลจากเว็บอย่างมีจริยธรรม เคารพ robots.txt และลิขสิทธิ์</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--coral">🧪</div>
    <h3>Synthetic Data</h3>
    <p>สร้างข้อมูลสังเคราะห์เพื่อปกป้องความเป็นส่วนตัวของผู้ป่วย</p>
  </div>
</div>

---

## โหลดและสำรวจข้อมูล

```python
from datasets import load_dataset
import pandas as pd

# โหลดชุดข้อมูล
ds = load_dataset("scikit-learn/diabetes", split="train")
df = ds.to_pandas()

# สำรวจเบื้องต้น
print(df.shape)
print(df.describe())
print(df.isnull().sum())   # ตรวจค่าว่าง
```

---

## ขั้นตอนการเตรียมข้อมูล

<div class="dha-timeline">
  <div class="dha-step">
    <div class="dha-step__week">01</div>
    <h4>Collect</h4>
    <p>รวบรวมข้อมูลจากแหล่งที่เชื่อถือได้และได้รับอนุญาต</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">02</div>
    <h4>Clean</h4>
    <p>จัดการค่าว่าง ค่าผิดปกติ และความไม่สอดคล้อง</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">03</div>
    <h4>Label</h4>
    <p>กำกับป้ายข้อมูล (annotation) ด้วยผู้เชี่ยวชาญทางคลินิก</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">04</div>
    <h4>Split</h4>
    <p>แบ่ง train / validation / test เพื่อประเมินอย่างเป็นธรรม</p>
  </div>
</div>

---

## จริยธรรมและความเป็นส่วนตัว

```{warning} ข้อมูลสุขภาพคือข้อมูลอ่อนไหว
ข้อมูลผู้ป่วยอยู่ภายใต้ PDPA และมาตรฐานความปลอดภัยทางการแพทย์เสมอ:
- ทำ de-identification ก่อนนำมาใช้
- ขอความยินยอม (consent) ที่ถูกต้อง
- ไม่นำข้อมูลออกนอกระบบที่ได้รับอนุญาต
```

> 📓 ฝึกจริงกับข้อมูล FHIR ที่ [Notebook: FHIR Data Exploration](../../notebooks/02-fhir-data.html)

ถัดไป: [Evaluation & Optimization](evaluation.md) →
