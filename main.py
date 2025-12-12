import streamlit as st
import dotenv
import langchain
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import dotenv
import subprocess
import sys
import zipfile
from dotenv import load_dotenv
from pypdf import PdfReader


load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEM")

st.set_page_config(page_title="AI Portfolio Generator", page_icon="📄")
st.title("AI Portfolio Website from Resume")
st.write("Upload your resume (PDF). The app will generate a simple portfolio website using Gemini.")

#  PDF

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

#  File Upload

uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

resume_text = ""

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Resume Text (for checking)")
    st.text_area(" verify if needed", resume_text, height=200)

# Main Button 

if st.button("Generate Portfolio Website"):

    if resume_text.strip() == "":
        st.error("Please upload  resume ")
        st.stop()

    #  Prompt Generator

    with st.spinner("Step 1/2: Creating website prompt from resume..."):

        system_prompt_1 = """
You are a prompt-engineering assistant. Read the user's resume and generate a detailed prompt
that another LLM can use to create a personal portfolio website.

From the resume, include:
- Full name
- Skills
- Projects
- Education
- Experience
- Achievements
- Color/theme/style preferences (guess logically based on the role)

Write it as clear instructions for a website generator model.
Do not invent crazy things, stay close to the resume.
"""

        messages_1 = [
            ("system", system_prompt_1),
            ("user", resume_text)
        ]

        model_1 = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.5
        )

        website_prompt = model_1.invoke(messages_1).content

        st.subheader("LLM #1 Output (Website Prompt)")
        st.write(website_prompt)

    #  Website Generator 

    with st.spinner("Step 2/2: Generating HTML, CSS and JavaScript..."):

        system_prompt_2 = """
You generate complete website files. Output HTML, CSS, and JavaScript code only.
No explanation text.

Follow this exact format:

--html--
[html code]
--html--

--css--
[css code]
--css--

--javascript--
[javascript code]
--javascript--

Do NOT add any explanation.
Do NOT add comments outside the code.
Use only these three sections in this order.
"""

        messages_2 = [
            ("system", system_prompt_2),
            ("user", website_prompt)
        ]

        model_2 = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.8
        )

        response = model_2.invoke(messages_2).content

    try:
        html_code = response.split("--html--")[1].strip()
        css_code = response.split("--css--")[1].strip()
        js_code = response.split("--javascript--")[1].strip()
    except Exception as e:
        st.error("Could not split the model output into HTML/CSS/JS sections.")
        st.code(response)
        st.stop()

    

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_code)

    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css_code)

    with open("script.js", "w", encoding="utf-8") as f:
        f.write(js_code)

    st.success("Website files created: index.html, style.css, script.js")

    

    zip_filename = "website.zip"
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        zipf.write("index.html")
        zipf.write("style.css")
        zipf.write("script.js")

    with open(zip_filename, "rb") as f:
        st.download_button(
            "Download Website as ZIP",
            f,
            file_name="portfolio_website.zip",
            mime="application/zip"
        )

    st.info("To view the portfolio, unzip the file and open index.html in your browser.")