import os
from dotenv import load_dotenv
from google import genai

# Securely load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_document(name, target_role, skills, experience, doc_type):
    """Handles prompt engineering and API communication."""
    
    if not GEMINI_API_KEY:
        return "Error: Gemini API key not found. Please check your .env file."

    client = genai.Client(api_key=GEMINI_API_KEY)

    # --- Prompt Engineering ---
    if doc_type == "Cover Letter":
        prompt = f"""You are an expert career coach. Keep it concise, professional, and impactful. Do not include placeholder addresses.
        
Write a professional, engaging cover letter for {name} applying for the role of {target_role}. 
The candidate has the following skills: {skills}. 
Their experience includes: {experience}."""
    else:
        prompt = f"""You are an expert resume writer. Format clearly with bullet points.
        
Write a powerful professional summary and 3-4 impactful achievement bullet points for {name}, who is applying for a {target_role} position. 
Skills to highlight: {skills}. 
Experience base: {experience}."""

    # --- API Call ---
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text.strip()
            
    except Exception as e:
        return f"API Error: {e}"


def analyze_ats(resume_text, job_description):
    """Compares a resume against a job description for ATS optimization."""
    
    if not GEMINI_API_KEY:
        return "Error: Gemini API key not found. Please check your .env file."

    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""You are an advanced Applicant Tracking System (ATS). Analyze the following resume against the provided job description.
    
    Format your response exactly like this:
    **Match Score:** [Insert Percentage]%
    
    **Missing Keywords:**
    * [List 3-5 crucial skills/keywords present in the JD but missing in the resume]
    
    **Actionable Advice:**
    * [Give 2 short tips to improve the resume for this specific role]
    
    Job Description:
    {job_description}
    
    Resume:
    {resume_text}"""

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text.strip()
    except Exception as e:
        return f"API Error: {e}"