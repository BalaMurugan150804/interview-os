import json
from google import genai
from dotenv import load_dotenv
import os
from prompts.roadmap_prompt import roadmap_prompt

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_roadmap(resume_analysis: dict):
    prompt = roadmap_prompt(resume_analysis)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    clean_text = response.text.replace("```json", "").replace("```","").strip()

    roadmap = json.loads(clean_text)

    return roadmap