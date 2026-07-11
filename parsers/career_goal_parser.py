from pydantic import BaseModel
from typing import Literal

class CareerGoal(BaseModel):
    goal: Literal["company", "learning"]