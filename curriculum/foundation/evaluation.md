# Week 3: Evaluation & Optimization

<p class="dha-eyebrow">Foundation / Week 3</p>

<div class="dha-pill-row">
  <span class="dha-pill">กลาง</span>
  <span class="dha-pill dha-pill--green">4 ชม.</span>
  <span class="dha-pill dha-pill--coral">มี 2 ส่วน</span>
</div>

<p class="dha-lead">โมเดลที่แม่นบนข้อมูล train อาจล้มเหลวกับผู้ป่วยจริง สัปดาห์นี้เรียนการวัดผลที่ถูกต้อง การสร้าง baseline และหลักการ optimization เบื้องหลังการ train โมเดล</p>

---

## 3a: Metrics, Baselines & LLM Evaluation

### การแบ่งข้อมูล

```python
from sklearn.model_selection import train_test_split

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_valid, X_test, y_valid, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
# 70% train / 15% valid / 15% test
```

### Metric สำหรับ Classification

| Metric | เหมาะกับ | สูตรย่อ |
|---|---|---|
| **Accuracy** | คลาสสมดุล | ทำนายถูก / ทั้งหมด |
| **Precision** | ลด false positive | TP / (TP+FP) |
| **Recall (Sensitivity)** | ลด false negative สำคัญในคลินิก | TP / (TP+FN) |
| **F1** | สมดุล precision/recall | ค่าเฉลี่ยฮาร์โมนิก |
| **AUROC** | จัดอันดับความเสี่ยง | พื้นที่ใต้ ROC curve |

```{tip} ในงานคลินิก Recall มักสำคัญที่สุด
การพลาดผู้ป่วยที่ป่วยจริง (false negative) มักอันตรายกว่าการเตือนเกินจริง จึงให้ความสำคัญกับ recall/sensitivity สูง
```

### LLM-as-Judge

เมื่อประเมินผลลัพธ์ที่เป็นข้อความ (เช่นสรุปเวชระเบียน) เราใช้ LLM อีกตัวเป็น "ผู้ตัดสิน" ให้คะแนนตามเกณฑ์ที่กำหนด

---

## 3b: Gradient Descent จากศูนย์

หัวใจของการ train คือ **ค่อย ๆ ปรับพารามิเตอร์ให้ loss ลดลง**

```python
import torch

# ข้อมูลจำลอง: y = 2x + noise
x = torch.randn(100, 1)
y = 2 * x + 0.1 * torch.randn(100, 1)

w = torch.zeros(1, requires_grad=True)
lr = 0.1

for step in range(50):
    pred = x * w
    loss = ((pred - y) ** 2).mean()   # MSE
    loss.backward()                   # คำนวณ gradient
    with torch.no_grad():
        w -= lr * w.grad              # อัปเดตพารามิเตอร์
        w.grad.zero_()

print(f"w เรียนรู้ได้ ≈ {w.item():.3f} (เป้าหมาย = 2.0)")
```

---

## หลีกเลี่ยง Overfitting

<div class="dha-grid dha-grid--2">
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--coral">⚠️</div>
    <h3>สัญญาณ Overfitting</h3>
    <p>train accuracy สูง แต่ validation/test ต่ำ โมเดลจำข้อมูลแทนการเรียนรู้รูปแบบ</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--green">✅</div>
    <h3>วิธีแก้</h3>
    <p>เพิ่มข้อมูล, regularization, dropout, early stopping และ cross-validation</p>
  </div>
</div>

ถัดไป: เลือก [Specialization Track](../tracks/index.md) ของคุณ →
