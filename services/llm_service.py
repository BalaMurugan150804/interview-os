import json 
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_json(prompt: str):

    response = client.model.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    clean_text = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(clean_text)