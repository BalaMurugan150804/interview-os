from pydantic import BaseModel

class InterviewResponse(BaseModel):
    answer: str