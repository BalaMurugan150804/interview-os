import json

def resume_prompt(resume_text: str):
    schema = {
        "score": 0,
        "strengths": [],
        "weak_skills": [],
        "recommendation": ""
        
    }

    return f"""
You are an expert ATS Resume Reviewer.

Analyze the resume.

Return ONLY valid JSON.

Expected format:

{json.dumps(schema, indent=4)}

Resume:

{resume_text}
"""