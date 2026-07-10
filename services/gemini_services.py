from google import genai
from dotenv import load_dotenv
from prompts.interview_prompt import interview_prompt
import json
from parsers.output_parser import InterviewResponse
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_gemini(prompt: str):
    formatted_prompt = interview_prompt(prompt)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=formatted_prompt
    )

    cleaned_response = (
        response.text
        .replace("```json", "")
        .replace("```","")
        .strip()
    )
    print(cleaned_response)
    parsed_response = json.loads(cleaned_response)
    validated_response = InterviewResponse.model_validate(parsed_response)
    return validated_response