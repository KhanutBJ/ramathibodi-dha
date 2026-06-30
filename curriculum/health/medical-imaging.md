# Medical Imaging: AI กับภาพถ่ายทางการแพทย์

<p class="dha-eyebrow">Digital Health / Imaging</p>

<p class="dha-lead">ภาพถ่ายทางการแพทย์, X-ray, CT, MRI, พยาธิวิทยา เป็นหนึ่งในพื้นที่ที่ AI สร้างผลกระทบได้มากที่สุด โมดูลนี้สอนการทำงานกับข้อมูล DICOM และสร้างโมเดล deep learning สำหรับภาพ</p>

---

## รูปแบบข้อมูล DICOM

ภาพทางการแพทย์ไม่ใช่ไฟล์ JPG ทั่วไป แต่เป็น **DICOM** ที่ฝังข้อมูล metadata ทางคลินิกไว้ด้วย

```python
import pydicom

ds = pydicom.dcmread("chest_ct.dcm")
print("Modality:", ds.Modality)          # CT, MR, CR, ...
print("Body part:", ds.get("BodyPartExamined", "-"))
print("Pixel shape:", ds.pixel_array.shape)

# แปลงเป็น array สำหรับ deep learning
import numpy as np
img = ds.pixel_array.astype(np.float32)
img = (img - img.min()) / (img.max() - img.min())   # normalize
```

---

## งานหลักใน Medical Imaging

| งาน | คำอธิบาย | ตัวอย่าง |
|---|---|---|
| **Classification** | จำแนกว่าภาพมีความผิดปกติหรือไม่ | ปอดอักเสบจาก X-ray |
| **Detection** | ระบุตำแหน่งความผิดปกติ | ก้อนเนื้อใน CT |
| **Segmentation** | วาดขอบเขตอวัยวะ/รอยโรค | แบ่งเขตเนื้องอกใน MRI |
| **Registration** | จัดภาพหลายช่วงเวลาให้ตรงกัน | เปรียบเทียบก่อน/หลังรักษา |

---

## ข้อควรระวังเฉพาะทางภาพการแพทย์

<div class="dha-grid dha-grid--2">
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--coral">⚠️</div>
    <h3>Class Imbalance</h3>
    <p>โรคหายากมีตัวอย่างน้อยมาก ต้องใช้เทคนิคจัดการข้อมูลไม่สมดุล</p>
  </div>
  <div class="dha-card">
    <div class="dha-card__icon dha-card__icon--violet">🏷️</div>
    <h3>Annotation Cost</h3>
    <p>การ label ต้องใช้รังสีแพทย์ ใช้เวลาและงบสูง พิจารณา semi-supervised</p>
  </div>
</div>

```{tip} Transfer Learning ช่วยได้มาก
ข้อมูลภาพการแพทย์มักมีจำกัด การเริ่มจากโมเดลที่ pretrain มาแล้ว (เช่น ImageNet หรือ RadImageNet) แล้ว fine-tune มักได้ผลดีกว่าการ train จากศูนย์
```

> 📓 ฝึกสร้าง classifier ภาพการแพทย์ที่ [Notebook: Medical Image Classification](../../notebooks/03-medical-imaging.html)
