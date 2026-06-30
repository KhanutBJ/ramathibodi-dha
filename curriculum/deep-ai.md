# Deep AI

การนำ Deep Learning มาใช้กับข้อมูลทางการแพทย์ประเภทต่าง ๆ — ภาพ สัญญาณ เสียง และข้อมูลตาราง

---

## 1. Deep Learning พื้นฐาน

ทำความเข้าใจหลักการและสถาปัตยกรรมหลักของ Neural Network

**สิ่งที่จะเรียน:**
- Neural Network: Perceptron → MLP → Deep Network
- Backpropagation และ Gradient Descent
- Activation Functions: ReLU, Sigmoid, Softmax
- Loss Functions: Cross-Entropy, MSE, Focal Loss
- Regularization: Dropout, BatchNorm, Weight Decay
- Framework: PyTorch (หลัก), TensorFlow (ภาพรวม)
- Training Loop: ข้อมูล → Forward → Loss → Backward → Update

---

## 2. Explainability (XAI)

การอธิบายผลการตัดสินใจของ AI — สำคัญมากในบริบทการแพทย์เพื่อความน่าเชื่อถือและการยอมรับจากแพทย์

**สิ่งที่จะเรียน:**
- SHAP (SHapley Additive exPlanations)
- LIME (Local Interpretable Model-agnostic Explanations)
- Grad-CAM: Visualization สำหรับ CNN
- Attention Visualization สำหรับ Transformer
- Counterfactual Explanations
- การนำเสนอ XAI ต่อแพทย์และผู้ป่วย

```{important} ทำไม XAI ถึงสำคัญ
AI ที่วินิจฉัยโรคแต่ "ไม่รู้ว่าทำไม" ยากที่แพทย์จะไว้วางใจ XAI ช่วยให้เห็นว่า Model ตัดสินใจจากส่วนไหนของข้อมูล
```

---

## 3. ข้อมูลภาพ (Image)

Deep Learning สำหรับภาพทางการแพทย์ — ประยุกต์ใช้กับ X-ray, CT, MRI, Pathology

**สิ่งที่จะเรียน:**

### CNN และ Vision Transformer
- CNN: Conv2D, Pooling, ResNet, EfficientNet
- Vision Transformer (ViT): Self-Attention บนภาพ
- Pre-trained Models: Transfer Learning จาก ImageNet

### งานหลัก
- **Image Classification**: โรคหรือไม่โรค
- **Object Detection**: ตำแหน่งของรอยโรค (YOLO, DETR)
- **Segmentation**: แบ่งส่วน Organ หรือเนื้องอก (U-Net, SAM)
- **Generative**: Data Augmentation ด้วย Diffusion Model

### ข้อมูลเฉพาะทาง
- DICOM: รูปแบบไฟล์ภาพทางการแพทย์มาตรฐาน
- Whole Slide Image (WSI): ภาพ Pathology ขนาดใหญ่
- Fundus Photography: ภาพจอประสาทตา

---

## 4. ข้อมูลสัญญาณ (Signal)

Deep Learning สำหรับสัญญาณชีวภาพ เช่น ECG, EEG, PPG

**สิ่งที่จะเรียน:**
- 1D CNN และ RNN/LSTM สำหรับ Time Series
- Transformer สำหรับสัญญาณ: PatchTST, TimesNet
- ECG Analysis: การตรวจจับ Arrhythmia
- EEG Analysis: Brain-Computer Interface
- Feature Engineering: FFT, Wavelet, STFT
- Wearable Data: Apple Watch, Garmin, Fitbit

---

## 5. ข้อมูลเสียง (Sound)

Deep Learning สำหรับเสียงในงานสาธารณสุข

**สิ่งที่จะเรียน:**
- Audio Preprocessing: Mel Spectrogram, MFCC
- Sound Classification: เสียงไอ เสียงหัวใจ เสียงปอด
- Medical ASR: Whisper Fine-tuning ภาษาไทย
- Voice Activity Detection
- กรณีศึกษา: วินิจฉัยโรคปอดจากเสียงไอ

---

## 6. ข้อมูลตาราง (Tabular)

Deep Learning และ ML สำหรับข้อมูลผู้ป่วยในรูปแบบตาราง

**สิ่งที่จะเรียน:**
- TabNet, FT-Transformer, SAINT
- Gradient Boosting: XGBoost, LightGBM, CatBoost
- การจัดการ Missing Data ในเวชระเบียน
- Survival Analysis: Time-to-Event Prediction
- Imbalanced Classification: SMOTE, Focal Loss
- Feature Engineering จาก Clinical Data

```{tip} เลือก Model ให้เหมาะกับข้อมูล
ข้อมูลตารางในโรงพยาบาลมักมี Missing Value สูง Gradient Boosting มักทำงานได้ดีกว่า Deep Learning ในหลายกรณี ทดสอบทั้งสองก่อนตัดสินใจ
```
