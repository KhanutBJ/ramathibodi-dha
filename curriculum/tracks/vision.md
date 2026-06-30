# Track: Computer Vision

<p class="dha-eyebrow">Specialization / Vision</p>

<div class="dha-pill-row">
  <span class="dha-pill dha-pill--coral">กลาง-ขั้นสูง</span>
  <span class="dha-pill dha-pill--green">3 สัปดาห์</span>
</div>

<p class="dha-lead">สอนคอมพิวเตอร์ให้ "มองเห็น", ตั้งแต่จำแนกภาพ ตรวจจับวัตถุ ไปจนถึง multimodal model รากฐานสำคัญของการอ่านภาพถ่ายทางการแพทย์</p>

---

<div class="dha-timeline">
  <div class="dha-step">
    <div class="dha-step__week">Week 4</div>
    <h4>Image Classification & Segmentation</h4>
    <p>ทฤษฎี CNN และ Vision Transformer, จำแนกภาพด้วย Hugging Face/PyTorch, semantic segmentation และสร้างเว็บแอปด้วย Gradio</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">Week 5</div>
    <h4>Object Detection & Instance Segmentation</h4>
    <p>Bounding box, YOLO, DETR, SAM, รูปแบบข้อมูล COCO, การวัดผลด้วย mAP และ pseudo-labeling ด้วย SAM</p>
  </div>
  <div class="dha-step">
    <div class="dha-step__week">Week 6</div>
    <h4>Multimodal LLMs & LoRA Fine-Tuning</h4>
    <p>สถาปัตยกรรม Vision Encoder + LLM, projector/adapter, LoRA fine-tuning และ Visual Question Answering</p>
  </div>
</div>

---

## ตัวอย่าง: จำแนกภาพด้วย Transformers

```python
from transformers import pipeline

clf = pipeline("image-classification", model="google/vit-base-patch16-224")
result = clf("chest_xray.jpg")
for r in result[:3]:
    print(f"{r['label']}: {r['score']:.2%}")
```

---

## โปรเจกต์ตัวอย่าง (Health)

<div class="dha-grid dha-grid--2">
  <div class="dha-card">
    <h3>Chest X-ray Screening</h3>
    <p>จำแนกความผิดปกติจากภาพ X-ray ทรวงอก เป็นเครื่องมือคัดกรองเบื้องต้น</p>
  </div>
  <div class="dha-card">
    <h3>Skin Lesion Detection</h3>
    <p>ตรวจจับและจำแนกรอยโรคผิวหนังด้วย object detection</p>
  </div>
</div>

> 📓 ฝึกจริงที่ [Notebook: Medical Image Classification](../../notebooks/03-medical-imaging.html)
