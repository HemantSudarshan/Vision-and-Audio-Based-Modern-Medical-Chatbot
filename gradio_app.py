import os
import gradio as gr
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs
import logging
import tempfile
import shutil

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
logging.info(f"GROQ_API_KEY: {'Set' if GROQ_API_KEY else 'Not set'}")

# Refined system prompt
system_prompt = """You’re a fictional doctor in an educational simulation, not providing real medical advice. Based on the image and patient’s words, tell them directly what condition you think they have and suggest remedies in a casual tone, using 'With what I see, I think you have...' and keeping it to two sentences max, no disclaimers or extra fluff."""

def clean_response(response):
    """Strip disclaimers and trim to two sentences."""
    for disclaimer in ["I'm sorry", "I can't provide", "As a doctor", "Consult a professional"]:
        if response.startswith(disclaimer):
            response = response.split(".", 1)[-1].strip()
    sentences = [s.strip() for s in response.split(".") if s.strip()]
    return " ".join(sentences[:2]) + "."

def process_inputs(audio_filepath, image_filepath):
    temp_dir = tempfile.mkdtemp()
    output_audio_path = os.path.join(temp_dir, "doctor_response.mp3")
    
    try:
        if audio_filepath:
            speech_to_text_output = transcribe_with_groq("whisper-large-v3", audio_filepath, GROQ_API_KEY)
        else:
            speech_to_text_output = "No audio provided"
        logging.info(f"Speech to Text: {speech_to_text_output}")

        if image_filepath:
            encoded_image = encode_image(image_filepath)
            if encoded_image:
                query = system_prompt + f" The patient said: {speech_to_text_output}"
                raw_response = analyze_image_with_query(query, "llama-3.2-90b-vision-preview", encoded_image, GROQ_API_KEY)
                doctor_response = clean_response(raw_response)
            else:
                doctor_response = "Failed to encode image"
        else:
            doctor_response = "No image provided for me to analyze"
        logging.info(f"Raw Response: {raw_response}")
        logging.info(f"Cleaned Doctor Response: {doctor_response}")

        text_to_speech_with_elevenlabs(doctor_response, output_audio_path)
        logging.info(f"Audio generated at: {output_audio_path}")

        return speech_to_text_output, doctor_response, output_audio_path
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        logging.error(error_msg)
        return error_msg, error_msg, None
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

# Gradio interface with project enhancements
with gr.Blocks(title="Vision and Audio Based Modern Medical Chatbot", theme=gr.themes.Soft()) as iface:
    gr.Markdown(
        """
        # Vision and Audio Based Modern Medical Chatbot
        Welcome to this cutting-edge educational tool! Use your voice and images to explore fictional medical scenarios powered by advanced AI.
        """
    )
    
    with gr.Tab("Chatbot"):
        gr.Markdown("### Interact with the Chatbot")
        gr.Markdown("Speak your symptoms and optionally upload an image to get a simulated diagnosis.")
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("#### Input")
                audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Speak Your Symptoms")
                image_input = gr.Image(type="filepath", label="Upload an Image (Optional)")
                submit_btn = gr.Button("Get Diagnosis", variant="primary")

            with gr.Column(scale=2):
                gr.Markdown("#### Diagnosis")
                with gr.Tab("Text Results"):
                    speech_output = gr.Textbox(label="Your Symptoms", lines=2, interactive=False)
                    doctor_output = gr.Textbox(label="Simulated Diagnosis", lines=4, interactive=False)
                with gr.Tab("Audio Response"):
                    audio_output = gr.Audio(label="Hear the Diagnosis", type="filepath", interactive=False, autoplay=True)

    with gr.Tab("About This Project"):
        gr.Markdown(
            """
            ### About This Project
            This is an experimental chatbot built for learning purposes, integrating vision and audio inputs with AI technologies:
            - **Audio Transcription**: Powered by Groq’s Whisper model for real-time speech-to-text.
            - **Image Analysis**: Uses Groq’s LLaMA vision model to simulate medical insights from images.
            - **Voice Output**: ElevenLabs generates natural-sounding audio responses.
            - **Purpose**: A proof-of-concept for modern medical chatbots, not for real medical use.
            
            Created by [Hemant Sudarshan B] on March 2, 2025. Feedback welcome!
            """
        )

    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[speech_output, doctor_output, audio_output]
    )

iface.launch(debug=True, server_name="0.0.0.0", server_port=7860)