# Digital Health

ความรู้ด้านระบบข้อมูลสุขภาพ มาตรฐาน และกฎหมายที่นักพัฒนา Digital Health ต้องเข้าใจ

---

## 1. ระบบสารสนเทศโรงพยาบาล (HIS)

Health Information System คือโครงสร้างพื้นฐานของข้อมูลในโรงพยาบาล

**สิ่งที่จะเรียน:**
- สถาปัตยกรรมของ HIS: OPD, IPD, Lab, Pharmacy, Radiology
- การไหลของข้อมูลผู้ป่วยตั้งแต่ลงทะเบียนจนถึงจำหน่าย
- ระบบ HIS ที่ใช้ในไทย: HOSxP, HIS Raman, JHCIS
- การเชื่อมต่อระหว่างระบบ
- ความท้าทาย: ข้อมูลกระจัดกระจาย ไม่มีมาตรฐาน

---

## 2. EMR และ PHR

**Electronic Medical Record (EMR)** — เวชระเบียนอิเล็กทรอนิกส์ที่จัดการโดยโรงพยาบาล

**Personal Health Record (PHR)** — ข้อมูลสุขภาพที่ผู้ป่วยเป็นเจ้าของและจัดการเอง

**สิ่งที่จะเรียน:**
- โครงสร้างข้อมูล EMR: Demographics, Diagnoses, Medications, Labs
- การ De-identification: ลบข้อมูลส่วนตัวออกเพื่องานวิจัย
- PHR Platforms: HealthKit (Apple), Google Health
- การเชื่อม EMR กับ AI: NLP สำหรับ Clinical Notes
- การแปลง Unstructured Text เป็น Structured Data

---

## 3. ICD-10 และการเข้ารหัสโรค

มาตรฐานการเข้ารหัสโรคสากล — พื้นฐานของข้อมูลทางการแพทย์ทั่วโลก

**สิ่งที่จะเรียน:**
- โครงสร้าง ICD-10: Chapters, Blocks, Categories
- ICD-10 ไทย: การปรับใช้ในบริบทไทย
- ICD-11: มาตรฐานใหม่และการเตรียมรับมือ
- Auto-coding: ใช้ NLP เข้ารหัส ICD จาก Clinical Note
- SNOMED CT: Ontology ทางการแพทย์ขั้นสูง

---

## 4. HL7 / FHIR

มาตรฐานการแลกเปลี่ยนข้อมูลสุขภาพระหว่างระบบ

**สิ่งที่จะเรียน:**

### HL7 v2
- Message Format: ADT, ORM, ORU
- Segment และ Field Structure
- การอ่านและแปลง HL7 v2 ด้วย Python

### FHIR (Fast Healthcare Interoperability Resources)
- Resources หลัก: Patient, Observation, Condition, MedicationRequest
- RESTful API: GET /Patient/{id}
- SMART on FHIR: Authorization สำหรับ Health Apps
- Thai FHIR Profile: การปรับ FHIR ให้เข้ากับบริบทไทย
- การใช้งาน HAPI FHIR Server

```{note} ทำไม FHIR ถึงสำคัญ
FHIR กำลังกลายเป็นมาตรฐานหลักในการแลกเปลี่ยนข้อมูลสุขภาพทั่วโลก รวมถึงไทย การเข้าใจ FHIR ช่วยให้พัฒนา App ที่เชื่อมกับระบบโรงพยาบาลได้
```

---

## 5. PDPA และความปลอดภัยข้อมูล

พระราชบัญญัติคุ้มครองข้อมูลส่วนบุคคล (PDPA) กับข้อมูลสุขภาพ

**สิ่งที่จะเรียน:**
- PDPA: สิทธิ์ของเจ้าของข้อมูล หน้าที่ของผู้ควบคุมข้อมูล
- Sensitive Personal Data: ข้อมูลสุขภาพถือเป็นข้อมูลอ่อนไหว
- Consent Management: การขอและจัดการความยินยอม
- Data Minimization และ Purpose Limitation
- De-identification vs Anonymization
- การนำข้อมูลออกนอกประเทศ

---

## 6. Genomics Thailand

โครงการจีโนมิกส์ไทยแลนด์ — ฐานข้อมูลจีโนมประชากรไทย 50,000 ราย

**สิ่งที่จะเรียน:**
- Genomics พื้นฐาน: DNA → Gene → Variant → Phenotype
- NGS Data: FASTQ, VCF, BAM
- Genomics Thailand Platform: การเข้าถึงข้อมูล
- Pharmacogenomics: ยาที่เหมาะกับ Genotype
- Population Genetics ของคนไทย

---

## 7. NHSO Claims Data

ข้อมูลเรียกร้องค่ารักษาพยาบาลจากสำนักงานหลักประกันสุขภาพแห่งชาติ

**สิ่งที่จะเรียน:**
- โครงสร้างข้อมูล 43 แฟ้ม
- การวิเคราะห์รูปแบบการใช้บริการสาธารณสุข
- Disease Burden Analysis
- Cost Analysis สำหรับนโยบาย
- การเชื่อมข้อมูล Claims กับข้อมูลคลินิก
