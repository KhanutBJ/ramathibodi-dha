# Week 7: AI Ethics

<p class="dha-eyebrow">Capstone / Week 7</p>

<p class="dha-lead">เทคโนโลยีที่ทรงพลังมาพร้อมความรับผิดชอบ ในงานสุขภาพ การตัดสินใจของ AI ส่งผลต่อชีวิตคนโดยตรง สัปดาห์นี้เราเรียนรู้การพัฒนา AI อย่างมีจริยธรรมและรับผิดชอบ</p>

---

## ประเด็นจริยธรรมหลัก

<div class="dha-grid dha-grid--2">
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--coral">⚖️</div>
    <h3>Bias & Fairness</h3>
    <p>อคติในข้อมูลและโมเดลอาจขยายความเหลื่อมล้ำทางสุขภาพ ต้องตรวจสอบข้ามกลุ่มประชากร</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--violet">🔐</div>
    <h3>Privacy & Consent</h3>
    <p>ข้อมูลผู้ป่วยต้องได้รับความยินยอมและคุ้มครองตาม PDPA และมาตรฐานสากล</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--green">📜</div>
    <h3>Copyright & Data Rights</h3>
    <p>เคารพลิขสิทธิ์ข้อมูลที่ใช้ train โดยเฉพาะข้อมูลที่ generate จาก AI</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--amber">🎯</div>
    <h3>Accountability</h3>
    <p>ใครรับผิดชอบเมื่อ AI ผิดพลาด? ต้องมีความชัดเจนก่อนใช้งานจริง</p>
  </div>
</div>

---

## กรอบการประเมินความเสี่ยง

| ระดับความเสี่ยง | ลักษณะ | มาตรการ |
|---|---|---|
| **ต่ำ** | เครื่องมือสนับสนุน ไม่ตัดสินแทนคน | review ตามปกติ |
| **กลาง** | ช่วยตัดสินใจทางคลินิก | human-in-the-loop บังคับ |
| **สูง** | กระทบการวินิจฉัย/รักษาโดยตรง | clinical trial + กำกับดูแล |

---

## หลักปฏิบัติสำหรับผู้สร้าง

```{important} Responsible AI Checklist
- [ ] ตรวจสอบอคติในข้อมูลและผลลัพธ์ข้ามกลุ่มผู้ป่วย
- [ ] ได้รับความยินยอมและทำ de-identification แล้ว
- [ ] โมเดลอธิบายได้ (explainable) ในระดับที่แพทย์เข้าใจ
- [ ] มีแผนเฝ้าระวังหลัง deploy
- [ ] ระบุผู้รับผิดชอบและขั้นตอนเมื่อเกิดข้อผิดพลาด
```

> เชื่อมโยงกับ [Governance & Strategy](../../pathways/hospital.md) สำหรับมุมมองเชิงนโยบาย
