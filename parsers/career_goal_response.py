from typing import Optional
from pydantic import BaseModel

class CareerGoalResponse(BaseModel):
    next_step: str
    message: str
    required_input: Optional[str] = None