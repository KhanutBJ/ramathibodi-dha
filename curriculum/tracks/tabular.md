# Track: Tabular Data

<p class="dha-eyebrow">Specialization / Tabular</p>

<div class="dha-pill-row">
  <span class="dha-pill">กลาง</span>
  <span class="dha-pill dha-pill--green">3 สัปดาห์</span>
</div>

<p class="dha-lead">ข้อมูลส่วนใหญ่ในโรงพยาบาลอยู่ในรูปตาราง ผลแล็บ สัญญาณชีพ ทะเบียนผู้ป่วย track นี้สอนการทำนาย จำแนก และจัดกลุ่มจากข้อมูลตารางที่ตีความได้</p>

---

<div class="dha-timeline">
  <div class="dha-step">
    <div class="dha-step__week">Week 4</div>
    <h4>Correlation & Regression</h4>
    <p>ทำนายตัวแปรตัวเลข การวิเคราะห์ correlation, regression และ time series</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">Week 5</div>
    <h4>Classification</h4>
    <p>ทำนายหมวดหมู่ เช่น การ readmit, การเกิดภาวะแทรกซ้อน และการประเมินผลโมเดล</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">Week 6</div>
    <h4>Similarity, Recommendation & Clustering</h4>
    <p>การจับคู่ความคล้าย ระบบแนะนำ และการแบ่งกลุ่มผู้ป่วย (patient segmentation)</p>
  </div>
</div>

---

## ตัวอย่าง: ทำนายความเสี่ยงด้วย scikit-learn

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

proba = model.predict_proba(X_test)[:, 1]
print(f"AUROC: {roc_auc_score(y_test, proba):.3f}")

# ความสำคัญของแต่ละ feature, ตีความทางคลินิกได้
for name, imp in sorted(zip(feature_names, model.feature_importances_), key=lambda x: -x[1])[:5]:
    print(f"{name}: {imp:.3f}")
```

---

## โปรเจกต์ตัวอย่าง (Health)

<div class="dha-grid dha-grid--2">
  <div class="dha-card">
    <h3>30-Day Readmission</h3>
    <p>ทำนายโอกาส readmit ภายใน 30 วันจากข้อมูลการรักษา</p>
  </div>
  <div class="dha-card">
    <h3>Patient Risk Stratification</h3>
    <p>แบ่งกลุ่มผู้ป่วยตามระดับความเสี่ยงเพื่อจัดสรรการดูแล</p>
  </div>
</div>

> 📓 ฝึกจริงที่ [Notebook: Intro to Clinical ML](../../notebooks/01-clinical-ml.html)
