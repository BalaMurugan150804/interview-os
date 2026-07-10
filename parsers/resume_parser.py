from pydantic import BaseModel

class ResumeAnalysis(BaseModel):
    score: int
    strengths: list[str]
    weak_skills: list[str]
    recommendation: str