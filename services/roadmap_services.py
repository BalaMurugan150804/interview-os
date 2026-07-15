from prompts.roadmap_prompt import roadmap_prompt
from parsers.roadmap_response import RoadmapResponse
from services.llm_service import generate_json

def generate_roadmap(resume_analysis: dict):
    prompt = roadmap_prompt(resume_analysis)
    parsed = generate_json(prompt)
    validated = RoadmapResponse.model_validate(parsed)
    print(parsed)
    return validated