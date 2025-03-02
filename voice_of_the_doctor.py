import os
import elevenlabs
from elevenlabs.client import ElevenLabs
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def text_to_speech_with_elevenlabs(input_text, output_filepath, elevenlabs_api_key=None):
    if elevenlabs_api_key is None:
        elevenlabs_api_key = os.environ.get("ELEVENLABS_API_KEY")
        logging.info(f"ELEVENLABS_API_KEY loaded from env: {'True' if elevenlabs_api_key else 'False'}")
        if elevenlabs_api_key:
            logging.info(f"First few characters of ELEVENLABS_API_KEY: {elevenlabs_api_key[:5]}...")

    logging.info(f"Starting ElevenLabs conversion with text: '{input_text[:50]}...'")
    if not elevenlabs_api_key:
        logging.error("No ElevenLabs API key provided")
        raise Exception("No ElevenLabs API key provided")
    try:
        client = ElevenLabs(api_key=elevenlabs_api_key)
        audio = client.generate(
            text=input_text,
            voice="Aria",
            output_format="mp3_22050_32",
            model="eleven_turbo_v2"
        )
        elevenlabs.save(audio, output_filepath)
        logging.info(f"ElevenLabs audio saved to {output_filepath}")
        if os.path.exists(output_filepath):
            logging.info(f"Confirmed {output_filepath} exists with size {os.path.getsize(output_filepath)} bytes")
        else:
            logging.error(f"{output_filepath} was not created")
        return output_filepath
    except Exception as e:
        logging.error(f"Error in ElevenLabs: {str(e)}")
        raise

if __name__ == "__main__":
    logging.info("Script started")
    test_text = "Hi this is AI with Hemant, testing ElevenLabs autoplay!"
    test_output = "elevenlabs_testing_autoplay.mp3"
   