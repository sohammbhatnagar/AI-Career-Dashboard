# 🚀 AI Career Dashboard & ATS Optimizer

A cutting-edge, professional career assistant built with **Generative AI** and **Neumorphic UI** principles. This tool automates the creation of tailored career documents and provides deep analysis of resume compatibility with modern Applicant Tracking Systems (ATS).

---

## 🌟 Key Features

* **📝 AI Document Generator:** Leverages **Google Gemini 2.5 Flash** to synthesize role-specific cover letters and resume summaries based on unique user skills and experience.
* **📊 ATS Pattern Analyzer:** Uses advanced prompt engineering to compare resumes against job descriptions, identifying keyword gaps and providing a match percentage.
* **🎨 Neumorphic Dark UI:** A custom-engineered "Soft UI" interface designed with eye-soothing deep slate tones and tactile 3D elements to reduce user fatigue.
* **📄 Professional PDF Export:** Integrated **ReportLab** engine that translates AI-generated Markdown into structured, high-quality PDF documents.
* **✨ Smooth UX:** Features **Lottie** vector animations and CSS-driven entrance effects for a premium "SaaS" feel.

---

## 🛠️ Technical Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.14+ |
| **LLM Provider** | Google Gemini 2.5 Flash |
| **Frontend Framework** | Streamlit |
| **PDF Generation** | ReportLab |
| **Styling** | Custom CSS & Neumorphism |
| **Animations** | Streamlit-Lottie (JSON) |
| **Environment Mgmt** | Python-Dotenv |

---

## 📂 Project Structure

```text
AI-career-dashboard/
├── app.py               # Main Frontend & UI Logic
├── generator.py         # AI Prompt Engineering & API Integration
├── requirements.txt     # Python Dependency List
├── .env                 # API Keys (Protected/Ignored)
├── .gitignore           # Git Security Rules
├── .streamlit/
│   └── config.toml      # Custom Theme Configuration
└── README.md            # Project Documentation