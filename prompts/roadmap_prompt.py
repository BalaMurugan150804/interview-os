import json

def roadmap_prompt(resume_analysis: dict):
    schema = {
        "learning_order": [
            {
                "module_name": "",
                "estimated_time_weeks": 0
            }
        ],
        "projects": [
            {
                "project_name": "",
                "difficulty": "",
                "estimated_time_weeks": 0
            }
        ],
        "estimated_duration": "",
        "daily_plan": [
            {
                "time_slot": "",
                "task": ""
            }
        ]
    }
    return f"""
You are an AI Career Mentor.

Based on this resume analysis, create a personilized roadmap.
Rules:

- Do not rename keys.
- Do not add extra keys.
- Do not remove keys.
- learning_order must contain LearningModule objects.
- projects must contain ProjectItem objects.
- daily_plan must contain DailyPlanSlot objects.
- Return ONLY JSON.

Expected format:

{json.dumps(schema, indent=4)}

Resume Analysis:
{json.dumps(resume_analysis, indent=4)}
"""