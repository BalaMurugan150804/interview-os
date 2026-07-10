import json

def interview_prompt(question: str):

    schema = {
        "answer": "Your explanation here"
    }

    return f"""
You are a Senior GenAI Engineer.

Answer the user's question.

Return ONLY valid JSON.

Expected JSON format:
{json.dumps(schema, indent=4)}

Question:

{question}
"""