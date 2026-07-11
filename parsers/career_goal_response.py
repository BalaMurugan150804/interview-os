from pydantic import BaseModel

class CareerGoalResponse(BaseModel):
    next_step: str
    message: str