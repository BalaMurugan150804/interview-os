import json

def roadmap_prompt(resume_analysis: dict):
    schema = {
        "learning_order": [],
        "projects": [],
        "estimated_duration": "",
        "daily_plan": []
    }
    return f"""
You are an AI Career Mentor.

Based on this resume analysis, create a personilized roadmap.

Return ONLY valid JSON.

Expected format:

{json.dumps(schema, indent=4)}

Resume Analysis:
{json.dumps(resume_analysis, indent=4)}
"""