
![1](https://github.com/user-attachments/assets/ad49f752-478a-4a2f-a22d-1e89f85dc80b)


Here’s your well-formatted version with improvements for clarity, structure, and professionalism. You can copy and paste it directly!  

```markdown
# Vision and Audio-Based Modern Medical Chatbot

Welcome to the *Vision and Audio-Based Modern Medical Chatbot*, an innovative AI-powered tool designed to simulate medical consultations. Speak your symptoms, upload an image, and receive a **fictional** diagnosis in both text and audio form. **Note: This is for educational purposes only and not real medical advice.**

---

## 🚀 Features
- **Audio Transcription**: Converts spoken symptoms into text using Groq’s Whisper model.  
- **Image Analysis**: Uses Groq’s LLaMA Vision model to analyze uploaded images.  
- **Voice Response**: Generates realistic audio diagnoses via ElevenLabs.  
- **Interactive UI**: Built with Gradio for a smooth web-based experience.  

---

## 🛠 Installation Guide

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/HemantSudarshan/Vision-and-Audio-Based-Modern-Medical-Chatbot.git
cd Vision-and-Audio-Based-Modern-Medical-Chatbot
```

### 2️⃣ Set Up a Virtual Environment  
#### Linux/Mac:  
```bash
python -m venv venv
source venv/bin/activate
```
#### Windows:  
```powershell
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables  
#### Linux/Mac:  
```bash
export GROQ_API_KEY="your-groq-key"
export ELEVENLABS_API_KEY="your-elevenlabs-key"
```
#### Windows (PowerShell):  
```powershell
$env:GROQ_API_KEY="your-groq-key"
$env:ELEVENLABS_API_KEY="your-elevenlabs-key"
```

### 5️⃣ Run the Application  
```bash
python gradio_app.py
```
Then open `http://localhost:7860` in your browser.

---

## 📋 Requirements
The necessary dependencies are listed in `requirements.txt`:  
```
groq==0.4.0
gradio==4.19
elevenlabs==0.3.0
```

---

## 🎯 Usage Guide
1. **Speak**: Use your microphone to describe symptoms.  
2. **Upload**: Optionally, add an image (e.g., a rash photo).  
3. **Diagnose**: Click *"Get Diagnosis"* to receive a simulated response (text & voice).  

---

## 📂 Project Structure
- **`gradio_app.py`** → Manages the Gradio interface and app logic.  
- **`voice_of_the_patient.py`** → Handles audio transcription with Groq.  
- **`voice_of_the_doctor.py`** → Converts text to speech using ElevenLabs.  
- **`brain_of_the_doctor.py`** → Uses Groq’s Vision AI to analyze images.  

---

## 🏆 Skills Demonstrated
- **Python programming**  
- **AI Integration** (speech-to-text, vision AI, text-to-speech)  
- **Web app development with Gradio**  
- **API Handling** (Groq, ElevenLabs)  
- **File Handling & Logging**  

---

## ℹ️ About  
Created by **Hemant Sudarshan** on **March 2, 2025**, as a hands-on project to explore multimodal AI in a medical context.  
⚠️ **Disclaimer:** This tool is for learning purposes **only** and should not be used for real medical decisions. Always consult a certified professional for health concerns.  

---

## 🤝 Contributing  
Want to improve this project? Feel free to:  
✔️ Fork the repo  
✔️ Submit issues  
✔️ Send pull requests  

Suggestions for improving the UI, adding features, or refining AI responses are always welcome! 🚀  
```


