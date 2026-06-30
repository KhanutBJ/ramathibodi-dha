# Open Model Board

<p class="dha-eyebrow">Platform / Leaderboard</p>

<p class="dha-lead">กระดานเปิดที่จัดอันดับโมเดล AI ด้านสุขภาพบน benchmark ทางคลินิกของไทย โปร่งใส ทำซ้ำได้ และเปิดให้ทุกคนส่งโมเดลเข้าแข่งขัน เพื่อยกระดับมาตรฐานวงการร่วมกัน</p>

---

## Leaderboard: Diabetes Risk Prediction

| อันดับ | โมเดล | ทีม | AUROC | F1 | สถานะ |
|---|---|---|---|---|---|
| 🥇 1 | GradientBoost-TH | Rama-DS | 0.892 | 0.81 | ✅ verified |
| 🥈 2 | DeepTabular-v2 | Fellow-A | 0.885 | 0.79 | ✅ verified |
| 🥉 3 | RandomForest-base | Community | 0.871 | 0.77 | ✅ verified |
| 4 | LogReg-baseline | DHA staff | 0.842 | 0.74 | 📌 baseline |

---

## Leaderboard: Chest X-ray Screening

| อันดับ | โมเดล | ทีม | AUROC | Sensitivity | สถานะ |
|---|---|---|---|---|---|
| 🥇 1 | ViT-Med-TH | Vision-Lab | 0.941 | 0.92 | ✅ verified |
| 🥈 2 | ConvNeXt-FT | Fellow-B | 0.933 | 0.90 | ✅ verified |
| 🥉 3 | ResNet50-base | Community | 0.910 | 0.88 | ✅ verified |

---

## หลักการของ Open Model Board

<div class="dha-grid dha-grid--3">
  <div class="dha-card">
    <div class="dha-card__icon">🔬</div>
    <h3>Reproducible</h3>
    <p>ทุกผลลัพธ์ต้องส่งโค้ดและขั้นตอนที่ทำซ้ำได้ ไม่ใช่แค่ตัวเลข</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--green">⚖️</div>
    <h3>Fair Evaluation</h3>
    <p>ประเมินบน test set ลับเดียวกัน พร้อมรายงาน fairness ข้ามกลุ่ม</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--coral">🌍</div>
    <h3>Open</h3>
    <p>เปิดให้ทุกคนส่งโมเดล และเผยแพร่ baseline ให้เริ่มต้นได้ทันที</p>
  </div>
</div>

---

## วิธีส่งโมเดล

<div class="dha-timeline">
  <div class="dha-step">
    <div class="dha-step__week">01</div>
    <h4>เลือก benchmark</h4>
    <p>เลือกโจทย์จาก Marketplace ที่มี leaderboard เปิดอยู่</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">02</div>
    <h4>train และ package</h4>
    <p>เตรียมโค้ด inference + requirements ให้ทำซ้ำได้</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">03</div>
    <h4>ส่งเข้าระบบ</h4>
    <p>ระบบรันบน test set ลับและคำนวณคะแนนอัตโนมัติ</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">04</div>
    <h4>ขึ้นกระดาน</h4>
    <p>ผลที่ verified แล้วจะปรากฏบน leaderboard สาธารณะ</p>
  </div>
</div>

> 💡 โมเดลที่ติดอันดับต้น ๆ มีโอกาสได้รับเชิญเข้า [Fellowship](../fellowship/overview.md) และ [Venture Builder](../venture/overview.md)
