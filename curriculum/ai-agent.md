# AI Agent

การสร้างและนำ AI Agent มาใช้ในงานด้านสุขภาพ — ตั้งแต่การใช้งาน LLM ขั้นพื้นฐานไปจนถึงระบบ Agent ที่ทำงานอัตโนมัติ

---

## 1. LLM พื้นฐาน (LLM Basics)

ทำความเข้าใจการทำงานของ Large Language Model ก่อนนำไปใช้งานจริง

**สิ่งที่จะเรียน:**
- Transformer Architecture ภาพรวม
- Tokenization และ Context Window
- Prompt Engineering: Zero-shot, Few-shot, Chain-of-Thought
- การเลือกใช้ Model: GPT-4o, Claude, Gemini, LLaMA, Typhoon
- API Calling และการจัดการ Response

---

## 2. Hallucination และ Guardrails

ปัญหาที่ต้องเข้าใจก่อนนำ AI ไปใช้ในระบบสาธารณสุข

**สิ่งที่จะเรียน:**
- ประเภทของ Hallucination: Factual, Logical, Citation
- วิธีตรวจสอบและลด Hallucination
- Guardrails: NeMo Guardrails, Llama Guard
- Constitutional AI และ Safety Alignment
- การทดสอบ LLM ในบริบทการแพทย์

```{warning} สำคัญมาก
LLM ที่ไม่มี Guardrails เหมาะสมอาจให้ข้อมูลทางการแพทย์ที่ผิดพลาด ซึ่งเป็นอันตรายต่อผู้ป่วย ต้องมีกระบวนการตรวจสอบโดยผู้เชี่ยวชาญเสมอ
```

---

## 3. RAG (Retrieval-Augmented Generation)

การเชื่อม LLM กับฐานความรู้ทางการแพทย์เพื่อให้คำตอบที่แม่นยำและอ้างอิงได้

**สิ่งที่จะเรียน:**
- RAG Architecture: Retriever + Generator
- Vector Database: Chroma, Pinecone, Weaviate
- Embedding Models: text-embedding-3, BGE-M3
- Chunking Strategies สำหรับเอกสารทางการแพทย์
- Reranking และ Hybrid Search
- การสร้าง Medical Q&A Bot ด้วย RAG

---

## 4. Context / Loop Engineering

การออกแบบระบบ AI ที่ทำงานอัตโนมัติในหลายขั้นตอน

**สิ่งที่จะเรียน:**
- Agentic Workflow: Plan → Act → Observe → Reflect
- Tool Use / Function Calling
- Memory: Short-term, Long-term, Episodic
- Multi-Agent Systems
- LangChain / LangGraph พื้นฐาน
- Claude MCP (Model Context Protocol)

---

## 5. TTS / STT (ASR)

การแปลงเสียงพูดเป็นข้อความและข้อความเป็นเสียง — สำหรับระบบบันทึกเวชระเบียน AI

**สิ่งที่จะเรียน:**
- Speech-to-Text: Whisper, Conformer
- Text-to-Speech: XTTS, Fish Speech
- ASR ภาษาไทย: NECTEC, AI for Thai
- Medical Transcription: บันทึกเวชระเบียนด้วยเสียง
- Speaker Diarization: แยกเสียงแพทย์และผู้ป่วย

---

## 6. Line Agent

การสร้าง Chatbot บน Line สำหรับงานสาธารณสุข — แพลตฟอร์มที่คนไทยใช้มากที่สุด

**สิ่งที่จะเรียน:**
- Line Messaging API
- Line Bot พื้นฐาน: Webhook, Reply, Push
- การเชื่อม LLM กับ Line Bot
- Line LIFF: Mini App บน Line
- กรณีศึกษา: Bot นัดหมาย, ติดตามอาการ, ให้ข้อมูลยา

---

## 7. n8n / OpenClaw (Workflow Automation)

สร้างระบบอัตโนมัติโดยไม่ต้องเขียนโค้ดมาก

**สิ่งที่จะเรียน:**
- n8n: Workflow อัตโนมัติแบบ Visual
- การเชื่อมต่อ API, Database, Email, Line
- Trigger-based Automation สำหรับงานโรงพยาบาล
- Error Handling และ Monitoring

---

## 8. Cloud Run

การ Deploy AI Agent บน Cloud อย่างมีประสิทธิภาพ

**สิ่งที่จะเรียน:**
- Docker: Container พื้นฐาน
- Google Cloud Run: Serverless Container
- CI/CD: GitHub Actions
- Scaling และ Cost Optimization

---

## 9. Human in the Loop

การออกแบบระบบ AI ที่มีแพทย์หรือผู้เชี่ยวชาญ Validate ผลลัพธ์

**สิ่งที่จะเรียน:**
- การออกแบบ Workflow ที่ AI ช่วยตัดสินใจ ไม่ใช่ตัดสินใจแทน
- Active Learning: ให้ผู้เชี่ยวชาญ Label ข้อมูลที่ไม่แน่ใจ
- HITL Interface Design
- Audit Trail และ Accountability
- กรณีศึกษา: AI วินิจฉัยภาพถ่าย X-ray พร้อม Radiologist Review
