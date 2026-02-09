# DormDispatch  
**AI-Powered Content–Platform Matching & Scheduling Tool for Student Creators**

---

## 📌 Problem Statement

Talented student creators — educators, artists, writers, and performers — often struggle not because of lack of skill, but due to **poor content distribution decisions and inconsistent posting**.

They face:
- Overwhelming number of platforms (YouTube, Instagram, Pinterest, Medium, etc.)
- Lack of clarity on which platform suits their content best
- Irregular posting caused by exams, assignments, and academic workload
- Decisions based on intuition rather than data

This results in low reach, burnout, and abandoned creative efforts.

---

## 💡 Our Solution: DormDispatch

**DormDispatch** is an **AI-driven support system for content–platform matching and scheduling assistant**, designed specifically for **student creators**.

It helps users:

* Discover the most suitable platforms for their content
* Generate realistic posting schedules aligned with academic constraints
* Make data-informed distribution decisions instead of guesswork

The focus is **not on content generation**, but on **distribution intelligence**.

---

## 🎯 Target Users

* College students creating educational content
* Student artists (music, art, dance, design)
* Exam toppers / tutors sharing learning resources
* Creators managing content alongside academics

---

## ✨ Key Features

* AI-based platform discovery based on content type and creator goals
* Academic-aware scheduling recommendations
* Platform-specific optimization suggestions
* Structured, explainable AI output (JSON)
* Lightweight, scalable backend design

---

## 🧠 Why AI Is Necessary

Content distribution involves:

* Multiple platforms with evolving algorithms
* Different content formats and posting times
* Highly personalized constraints (time, goals, academic load)

These factors are **non-linear and dynamic**, making rule-based systems insufficient.

AI enables:

* Context-aware reasoning
* Personalization at scale
* Adaptability across platforms and creator profiles

Evaluating these factors jointly and generating personalized, explainable recommendations requires AI-driven reasoning rather than static heuristics.

---

## 🏗️ System Architecture (High Level)

```
User Input (Content + Constraints)
        ↓
FastAPI Backend
        ↓
AI Reasoning Layer
(Amazon Bedrock – designed)
(Bedrock-aligned Mock – prototype)
        ↓
Structured Recommendations (JSON)
```

---

## 🤖 Amazon Bedrock Usage (Important Note)

The system is **designed for Amazon Bedrock** as the AI inference layer.

### ⚠️ Prototype Constraint

Due to billing authorization requirements on new AWS accounts (credit/debit card dependency), **live Bedrock API calls could not be enabled**.

### ✅ Fallback Strategy Used

* A **Bedrock-aligned mock service** is implemented
* Prompt structure and response schema match the intended Bedrock design
* The system can be switched to live Bedrock by replacing the mock layer

This approach ensures:

* Architectural correctness
* Honest constraint handling
* Functional working prototype

---

## 🚀 Working Prototype

A FastAPI backend exposes an `/analyze` endpoint that:

* Accepts creator context as input
* Returns platform recommendations and scheduling strategy

### Run Locally

```bash
pip install fastapi uvicorn
uvicorn backend.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

Use the Swagger UI to test the `/analyze` endpoint.

---

## 📂 Repository Structure

```
AIFB/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   └── mock_bedrock.py
├── requirements.md
├── design.md
└── README.md
```

---

## 🛠️ Technologies Used

* **Backend:** Python, FastAPI
* **AI Layer:** Amazon Bedrock (designed), Bedrock-aligned mock
* **Documentation & Dev Assistance: Kiro, Amazon Q**
* **Version Control:** GitHub
* **Testing:** Swagger UI

---

## 🌍 Impact & Relevance (AI for Bharat)

* Empowers student creators across India
* Reduces dependency on costly creator agencies
* Supports sustainable side-hustles and passion projects
* Aligns with accessibility and skill-first innovation

---

## 🔮 Future Scope

* Replace mock layer with live Amazon Bedrock inference
* Add calendar integration (exam schedules)
* Multi-language support for regional creators
* Engagement feedback loop for adaptive scheduling

---

## 👤 Team

**Application Name:** DormDispatch  
**Team Lead:** Arkaprabha Chakraborty
