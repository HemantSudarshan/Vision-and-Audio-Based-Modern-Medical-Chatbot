import os
from groq import Groq
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transcribe_with_groq(stt_model, audio_filepath, groq_api_key):
    client = Groq(api_key=groq_api_key)
    try:
        with open(audio_filepath, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model=stt_model,
                file=audio_file,
                language="en"
            )
        logging.info(f"Transcription successful: {transcription.text}")
        return transcription.text
    except Exception as e:
        logging.error(f"Transcription error: {str(e)}")
        return "Failed to transcribe audio"