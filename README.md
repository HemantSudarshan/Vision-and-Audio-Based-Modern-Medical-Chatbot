
![1](https://github.com/user-attachments/assets/ad49f752-478a-4a2f-a22d-1e89f85dc80b)

```markdown
# Vision and Audio Based Modern Medical Chatbot



Welcome to the *Vision and Audio Based Modern Medical Chatbot*, an innovative educational tool that simulates medical consultations using cutting-edge AI technologies. Speak your symptoms, upload an image, and receive a fictional diagnosis in both text and audio form—all for learning purposes, not real medical advice.

## Features
- **Audio Transcription**: Converts spoken symptoms into text using Groq’s Whisper model.
- **Image Analysis**: Analyzes uploaded images with Groq’s LLaMA vision model to simulate medical insights.
- **Voice Response**: Generates natural-sounding audio diagnoses via ElevenLabs.
- **Interactive UI**: Built with Gradio for a user-friendly, web-based experience.

## Demo
![Demo GIF](demo.gif)  
*(Add a GIF or screenshot here by recording your app in action and uploading it to this repo)*

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/VisionAudioMedicalChatbot.git
   cd VisionAudioMedicalChatbot
   ```
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Environment Variables**:
   ```bash
   export GROQ_API_KEY="your-grok-key"
   export ELEVENLABS_API_KEY="your-elevenlabs-key"
   ```
   On Windows:
   ```powershell
   $env:GROQ_API_KEY="your-grok-key"
   $env:ELEVENLABS_API_KEY="your-elevenlabs-key"
   ```
5. **Run the App**:
   ```bash
   python gradio_app.py
   ```
   Open `http://localhost:7860` in your browser.

## Requirements
See `requirements.txt`:
```
groq==0.4.0
gradio==4.19
elevenlabs==0.3.0
```

## Usage
- **Speak**: Record your symptoms using the microphone.
- **Upload**: Optionally add an image (e.g., a rash photo).
- **Diagnose**: Click "Get Diagnosis" to see and hear a simulated response.

## Project Structure
- `gradio_app.py`: Main Gradio interface and logic.
- `voice_of_the_patient.py`: Audio transcription with Groq.
- `voice_of_the_doctor.py`: Text-to-speech with ElevenLabs.
- `brain_of_the_doctor.py`: Image analysis with Groq.

## Skills Demonstrated
- Python programming
- AI integration (speech-to-text, vision, text-to-speech)
- Web app development with Gradio
- API usage (Groq, ElevenLabs)
- File handling and logging

## About
Created by Hemant Sudarshan on March 2, 2025, as a learning project to explore multimodal AI in a medical context. This is not intended for real medical use—consult a professional for actual health concerns.

## Contributing
Feel free to fork, submit issues, or send pull requests! Suggestions for improving the UI, adding features, or refining the AI responses are welcome.



