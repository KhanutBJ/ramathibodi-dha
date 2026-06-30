# Clinical AI: AI ที่ปลอดภัยพอจะใช้กับผู้ป่วย

<p class="dha-eyebrow">Digital Health / Clinical AI</p>

<p class="dha-lead">AI ในคลินิกต่างจาก AI ทั่วไป ความผิดพลาดมีผลต่อชีวิตคน โมดูลนี้สอนหลักการสร้าง AI ทางการแพทย์ที่ปลอดภัย น่าเชื่อถือ ตรวจสอบได้ และทำงานร่วมกับบุคลากรได้จริง</p>

---

## หลักการสำคัญ

<div class="dha-grid dha-grid--2">
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--green">🛡️</div>
    <h3>Safety First</h3>
    <p>ออกแบบให้พลาดในทางที่ปลอดภัย (fail-safe) และมี human-in-the-loop เสมอ</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--violet">🔍</div>
    <h3>Explainability</h3>
    <p>แพทย์ต้องเข้าใจว่าทำไมโมเดลถึงทำนายเช่นนั้น ไม่ใช่กล่องดำ</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--coral">⚖️</div>
    <h3>Fairness</h3>
    <p>ตรวจสอบอคติข้ามกลุ่มผู้ป่วย (เพศ อายุ เชื้อชาติ) อย่างเข้มงวด</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--amber">📋</div>
    <h3>Validation</h3>
    <p>ทดสอบทางคลินิก (clinical validation) ก่อนใช้งานจริงเสมอ</p>
  </div>
</div>

---

## วงจรชีวิตของ Clinical AI

<div class="dha-timeline">
  <div class="dha-step">
    <div class="dha-step__week">01</div>
    <h4>Define clinical question</h4>
    <p>เริ่มจากโจทย์คลินิกจริงร่วมกับแพทย์ ไม่ใช่เริ่มจากข้อมูล</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">02</div>
    <h4>Develop & internal validate</h4>
    <p>สร้างโมเดลและตรวจสอบบนข้อมูลภายใน พร้อมประเมิน fairness</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">03</div>
    <h4>External validation</h4>
    <p>ทดสอบกับข้อมูลจากแหล่งอื่นเพื่อยืนยันว่า generalize ได้</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">04</div>
    <h4>Prospective trial</h4>
    <p>ทดลองใช้จริงแบบมีการควบคุม วัดผลกระทบต่อ outcome ผู้ป่วย</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">05</div>
    <h4>Monitor & maintain</h4>
    <p>เฝ้าระวัง data drift และ performance หลัง deploy อย่างต่อเนื่อง</p>
  </div>
</div>

---

```{warning} ระวัง Data Leakage
ปัญหาที่พบบ่อยในงานคลินิกคือ feature ที่ "รั่ว" ข้อมูลอนาคต เช่น ใช้ค่าที่บันทึกหลังการวินิจฉัยมาทำนายการวินิจฉัย ทำให้โมเดลดูแม่นเกินจริงแต่ใช้งานไม่ได้
```

> 📓 ดูตัวอย่าง pipeline ที่ [Notebook: Intro to Clinical ML](../../notebooks/01-clinical-ml.html)
