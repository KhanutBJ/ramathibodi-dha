# FHIR & HL7, ภาษากลางของข้อมูลสุขภาพ

<p class="dha-eyebrow">Digital Health / Interoperability</p>

<p class="dha-lead">ก่อนจะสร้าง AI ทางการแพทย์ ต้องเข้าใจว่าข้อมูลสุขภาพไหลเวียนอย่างไร FHIR (Fast Healthcare Interoperability Resources) คือมาตรฐานสมัยใหม่ที่ทำให้ทุกระบบ "คุยกันรู้เรื่อง"</p>

---

## ทำไมต้องมีมาตรฐาน?

โรงพยาบาลหนึ่งแห่งอาจมีระบบ HIS, LIS, RIS, EMR ที่ต่างผู้ผลิต หากไม่มีภาษากลาง ข้อมูลจะติดอยู่เป็น silo, FHIR แก้ปัญหานี้ด้วยการนิยาม "resource" มาตรฐาน

| มาตรฐาน | บทบาท |
|---|---|
| **HL7 v2** | มาตรฐานเก่าแก่ ใช้แลกเปลี่ยน message ระหว่างระบบ |
| **FHIR** | มาตรฐานยุคใหม่ เป็น REST API + JSON อ่านง่าย |
| **DICOM** | มาตรฐานสำหรับภาพถ่ายทางการแพทย์ |
| **SNOMED CT / ICD** | ระบบรหัสมาตรฐานสำหรับการวินิจฉัย |

---

## โครงสร้าง FHIR Resource

```json
{
  "resourceType": "Patient",
  "id": "example-001",
  "name": [{ "family": "ใจดี", "given": ["สมหญิง"] }],
  "gender": "female",
  "birthDate": "1985-03-12",
  "address": [{ "city": "กรุงเทพมหานคร", "country": "TH" }]
}
```

Resource ที่พบบ่อย: `Patient`, `Observation` (ผลตรวจ), `Condition` (การวินิจฉัย), `MedicationRequest`, `Encounter` (การเข้ารับบริการ)

---

## เรียก FHIR API ด้วย Python

```python
import requests

base = "https://hapi.fhir.org/baseR4"
resp = requests.get(f"{base}/Patient", params={"_count": 5})
bundle = resp.json()

for entry in bundle.get("entry", []):
    p = entry["resource"]
    name = p.get("name", [{}])[0]
    print(name.get("family", "-"), p.get("gender", "-"))
```

```{tip} ลองเล่นได้ฟรี
มี public FHIR test server เช่น `hapi.fhir.org` ให้ทดลองโดยไม่ต้องใช้ข้อมูลผู้ป่วยจริง
```

> 📓 ฝึกดึงและแปลงข้อมูล FHIR เป็นตารางที่ [Notebook: FHIR Data Exploration](../../notebooks/02-fhir-data.html)
