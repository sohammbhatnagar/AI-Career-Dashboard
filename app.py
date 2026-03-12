import streamlit as st
import re
import requests
import time
from streamlit_lottie import st_lottie
from generator import generate_document, analyze_ats 
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

st.set_page_config(page_title="AI Career Assistant", layout="wide")

# --- Helper Functions ---
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

def create_pdf(text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Translate Markdown to ReportLab tags
    formatted_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    formatted_text = re.sub(r'\b_(.*?)_\b', r'<i>\1</i>', formatted_text) 
    formatted_text = re.sub(r'^### (.*?)$', r'<font size="12"><b>\1</b></font><br/>', formatted_text, flags=re.MULTILINE)
    formatted_text = re.sub(r'^## (.*?)$', r'<font size="14"><b>\1</b></font><br/>', formatted_text, flags=re.MULTILINE)
    formatted_text = re.sub(r'^# (.*?)$', r'<font size="16"><b>\1</b></font><br/>', formatted_text, flags=re.MULTILINE)
    formatted_text = formatted_text.replace('\n', '<br />')
    
    story = [Paragraph(formatted_text, styles['Normal'])]
    doc.build(story)
    return buffer.getvalue()

# --- DARK NEUMORPHIC CSS ---
st.markdown("""
    <style>
    /* Fade-in animation */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .main .block-container {
        animation: fadeIn 0.8s ease-out;
    }

    /* Dark Neumorphic Input Boxes (Pushed In) */
    div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > div {
        background-color: #1B1F24 !important;
        border: none !important;
        border-radius: 15px !important;
        box-shadow: inset 5px 5px 10px #0d0f12, 
                    inset -5px -5px 10px #292f36 !important;
        color: #CDD9E5 !important;
    }
    
    /* Dark Neumorphic Buttons (Popped Out) */
    div.stButton > button {
        background-color: #1B1F24 !important;
        color: #CDD9E5 !important;
        border: none !important;
        border-radius: 15px !important;
        box-shadow: 5px 5px 10px #0d0f12, 
                   -5px -5px 10px #292f36 !important;
        transition: all 0.2s ease-in-out;
        font-weight: bold !important;
        margin-top: 10px;
    }
    
    /* Button Press Effect */
    div.stButton > button:active {
        box-shadow: inset 5px 5px 10px #0d0f12, 
                    inset -5px -5px 10px #292f36 !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
    }

    /* Tab Styling */
    button[data-baseweb="tab"] {
        color: #CDD9E5 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("### 🎓 Developer Profile")
    st.write("**Name:** Sohamm Bhatnagar")
    st.write("**Role:** Gen AI Intern")
    st.write("**Course:** MCA - Sem 4")
    st.write("---")
    st.markdown("""
        <div style="padding:15px; border-radius:15px; background-color:#1B1F24; 
                    box-shadow: 5px 5px 10px #0d0f12, -5px -5px 10px #292f36;">
            <p style="margin:0; font-weight:bold; color:#CDD9E5;">Connect:</p>
            <a href="#" style="text-decoration:none; color:#6366F1;">LinkedIn</a> | 
            <a href="#" style="text-decoration:none; color:#6366F1;">GitHub</a>
        </div>
    """, unsafe_allow_html=True)
    st.write("---")
    st.caption("Dark Mode | v1.5")

# --- App Header ---
st.markdown("""
    <h1 style='text-align: center; color: #CDD9E5; font-family: "Inter", sans-serif; font-weight: 800; text-shadow: 2px 2px 4px #0d0f12;'>
        🚀 AI Career Dashboard
    </h1>
    """, unsafe_allow_html=True)

# --- Load Glowing Pulse Animation ---
lottie_pulse = load_lottieurl("https://lottie.host/80860361-26c3-4d4b-9705-728b70f07297/HqP3P3P3P3.json")

tab1, tab2 = st.tabs(["📝 Generator", "📊 ATS Analyzer"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        target_role = st.text_input("Target Job")
    with col2:
        skills = st.text_input("Skills (comma separated)")
        experience = st.text_area("Experience Details")

    doc_type = st.radio("Type:", ("Cover Letter", "Resume Points"), horizontal=True)

    if st.button("Generate Document"):
        if name and target_role and skills:
            with st.status("AI is thinking...", expanded=True) as status:
                if lottie_pulse: st_lottie(lottie_pulse, height=200, key="gen_pulse")
                
                result = generate_document(name, target_role, skills, experience, doc_type)
                
                if "503" in result or "high demand" in result.lower():
                    status.update(label="Server Overload!", state="error")
                    st.error("Google's servers are busy. Please wait a few seconds and try again.")
                else:
                    status.update(label="Generation Complete!", state="complete")
                    st.success("Done!")
                    st.info(result)
                    st.download_button("📄 Download PDF", create_pdf(result), f"{name}_CareerDoc.pdf")
        else:
            st.warning("Missing required fields.")

with tab2:
    st.markdown("### ATS Compatibility Check")
    res_text = st.text_area("Your Resume Content", height=200)
    jd_text = st.text_area("Job Description", height=200)
    
    if st.button("Run ATS Scan"):
        if res_text and jd_text:
            with st.status("Analyzing Patterns...", expanded=True) as status:
                if lottie_pulse: st_lottie(lottie_pulse, height=200, key="ats_pulse")
                analysis = analyze_ats(res_text, jd_text)
                
                if "503" in analysis:
                    status.update(label="Server Busy!", state="error")
                    st.error("The ATS engine is currently experiencing high traffic.")
                else:
                    status.update(label="Scan Finished!", state="complete")
                    st.markdown(analysis)