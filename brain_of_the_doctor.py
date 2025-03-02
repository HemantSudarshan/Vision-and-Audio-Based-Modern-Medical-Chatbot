import os
from groq import Groq
import base64
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode('utf-8')
        logging.info(f"Image encoded successfully: {image_path}")
        return encoded
    except Exception as e:
        logging.error(f"Image encoding error: {str(e)}")
        return None

def analyze_image_with_query(query, model, encoded_image, groq_api_key):
    client = Groq(api_key=groq_api_key)
    try:
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
                ],
            }
        ]
        logging.info(f"Sending query to model: {query[:100]}...")
        logging.info(f"Image data length: {len(encoded_image)} bytes")
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model
        )
        response = chat_completion.choices[0].message.content
        logging.info(f"Full model response: {response}")
        return response
    except Exception as e:
        logging.error(f"Image analysis error: {str(e)}")
        return "Failed to analyze image"