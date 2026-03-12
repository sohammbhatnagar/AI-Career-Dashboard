# AI Resume & Cover Letter Generator

A modular web application built with Python and Streamlit that uses the Hugging Face Inference API (Mistral-7B) to generate tailored cover letters and resume summaries.

## Tech Stack
* **Frontend:** Streamlit
* **Backend:** Python, Requests
* **AI Model:** Mistral-7B-Instruct (via Hugging Face API)

## How to Run Locally

1. Clone this repository.
2. Install the required dependencies:
   `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add your Hugging Face API key:
   `HF_API_KEY=your_api_key_here`
4. Run the Streamlit app:
   `streamlit run app.py`