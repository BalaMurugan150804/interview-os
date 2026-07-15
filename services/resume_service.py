import json
from google import genai
from dotenv import load_dotenv
from prompts.interview_prompt import interview_prompt
from prompts.resume_prompt import resume_prompt
from services.llm_service import generate_json
from parsers.resume_parser import ResumeAnalysis
from parsers.output_parser import InterviewResponse
from google.genai.errors import ServerError
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

def analyze_resume(resume_text: str):
    try:
      formatted_prompt = resume_prompt(resume_text)
      parsed = generate_json(formatted_prompt)
      validated = ResumeAnalysis.model_validate(parsed)
      return validated

    except ServerError:
       raise Exception(
          "Gemini is temporarily unavailable. Please try again in a few moments"
       )    

