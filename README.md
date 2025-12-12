🎨 AI Portfolio Generator

Generate a complete personal portfolio website (HTML + CSS + JS) from a PDF Resume using Google Gemini + LangChain + Streamlit.

📌 Overview

This project is an AI-powered portfolio website generator.
A user uploads their resume in PDF format, and the system:

Extracts text from the resume using pypdf

Sends the extracted information to LLM #1 → generates a structured website prompt

Sends that prompt to LLM #2 → generates full website code (HTML, CSS, JavaScript)

Saves the files and provides them as a downloadable ZIP

Allows the user to open and view their generated portfolio locally

Everything is built using Streamlit for UI and Google Gemini (via LangChain) for AI.

✨ Features

📄 Upload and parse PDF resumes

🤖 Two-LLM pipeline for better accuracy

🎯 Extracts key resume details (skills, projects, education, experience, etc.)

🎨 Automatically generates a clean, styled portfolio website

📁 Outputs index.html, style.css, script.js

📦 One-click ZIP download

🔒 .env support to hide API keys

🧩 Beginner-friendly Streamlit interface

🧠 How the AI Pipeline Works
1️⃣ Resume Text Extraction (pypdf)

Reads PDF → extracts text → sends to LLM 1.

2️⃣ LLM #1 — Prompt Generator

Converts raw resume text into structured instructions for website creation.
Includes:

Full Name

Skills

Projects

Experience

Education

Achievements

Suggested theme/style

3️⃣ LLM #2 — Website Generator

Uses the final prompt to generate website files in this exact format:

--html--
[HTML CODE]
--html--

--css--
[CSS CODE]
--css--

--javascript--
[JS CODE]
--javascript--

4️⃣ ZIP Creation

All files saved → combined → given to user as website.zip.

📁 Project Structure
AI-Portfolio-Generator/
│
├── main.py              # Main Streamlit application
├── req.txt              # Python dependencies
├── index.html           # Generated website file
├── style.css            # Generated CSS stylesheet
├── script.js            # Generated JavaScript file
├── website.zip          # Auto-generated downloadable ZIP
├── .env                 # Stores API Key (not uploaded)
└── .gitignore           # Hides sensitive files

🔧 Tech Stack
Frontend

Streamlit (UI)

Backend

Python

LangChain

Google Gemini (Generative AI)

PDF Processing

pypdf (PdfReader)

Deployment Options

Streamlit Cloud

Local execution

GitHub Pages (for static website only)

🚀 Setup Instructions
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/AI-Portfolio-Generator.git
cd AI-Portfolio-Generator

2. Create & Activate Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate

3. Install Required Packages
pip install -r req.txt

4. Add Your Gemini API Key

Create a .env file:

GEM=YOUR_API_KEY_HERE

5. Run the App
streamlit run main.py

📌 How to Use

Open the Streamlit app

Upload your resume.pdf

Review extracted text

Click Generate Portfolio Website

Download the website.zip

Extract and open index.html in your browser

Your portfolio is ready! 🎉

🛠 Future Enhancements

Add multi-page website generation

Add live preview in Streamlit

Support DOCX resumes

Add themes (dark mode, professional, modern, creative)

👤 Developed By: Sangem Shiva Ram

For educational purposes — Agentic AI Project

📬 Contact

If needed:
Email:shivaram1348@gmail.com
