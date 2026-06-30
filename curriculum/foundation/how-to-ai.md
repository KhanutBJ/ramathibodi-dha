# Week 0: How to AI

<p class="dha-eyebrow">Foundation / Week 0</p>

<div class="dha-pill-row">
  <span class="dha-pill">เริ่มต้น</span>
  <span class="dha-pill dha-pill--green">2-3 ชม.</span>
  <span class="dha-pill dha-pill--navy">ไม่ต้องมีพื้นฐาน</span>
</div>

<p class="dha-lead">ก่อนเริ่มเรียน AI เราต้องเตรียมเครื่องมือให้พร้อม สัปดาห์นี้คุณจะตั้งค่าสภาพแวดล้อมที่ใช้ตลอดหลักสูตร และเขียนโค้ด AI บรรทัดแรก</p>

---

## เครื่องมือที่เราใช้

| เครื่องมือ | ใช้ทำอะไร |
|---|---|
| **Google Colab** | รัน Notebook บนคลาวด์ฟรี มี GPU ให้ใช้ |
| **Python 3** | ภาษาหลักของ AI/ML |
| **Jupyter Notebook** | เขียนโค้ด + ข้อความ + ผลลัพธ์ในที่เดียว |
| **Git & GitHub** | จัดการเวอร์ชันและแบ่งปันโค้ด |
| **Hugging Face** | คลังโมเดลและชุดข้อมูลสำเร็จรูป |

---

## ตั้งค่า Google Colab

1. เปิด [colab.research.google.com](https://colab.research.google.com) ด้วยบัญชี Google
2. สร้าง Notebook ใหม่: **File → New notebook**
3. เปิด GPU: **Runtime → Change runtime type → T4 GPU**
4. ทดสอบด้วยโค้ดด้านล่าง

```python
import sys
import torch

print(f"Python: {sys.version.split()[0]}")
print(f"PyTorch: {torch.__version__}")
print(f"GPU พร้อมใช้งาน: {torch.cuda.is_available()}")
```

ถ้าเห็น `GPU พร้อมใช้งาน: True` แสดงว่าพร้อมแล้ว 🎉

---

## คำสั่ง Python ที่ต้องรู้

```python
# ติดตั้งไลบรารีเพิ่มเติม
!pip install -q transformers datasets

# โหลดข้อมูลจาก Hugging Face
from datasets import load_dataset
ds = load_dataset("imdb", split="train[:100]")
print(ds[0]["text"][:200])
```

> 📓 ทำแบบฝึกหัดเต็มได้ที่ [Notebook: Intro to Clinical ML](../../notebooks/01-clinical-ml.html)

---

## เช็คลิสต์ก่อนไปต่อ

- [ ] เปิด Colab และรันโค้ดทดสอบได้
- [ ] เข้าใจการติดตั้งไลบรารีด้วย `!pip install`
- [ ] มีบัญชี GitHub และ Hugging Face
- [ ] โหลดชุดข้อมูลตัวอย่างได้สำเร็จ

ถัดไป: [What is AI?](what-is-ai.md) →
