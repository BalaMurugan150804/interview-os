from pydantic import BaseModel
from typing import List

class LearningModule(BaseModel):
    module_name: str
    estimated_time_weeks: int

class RoadmapProject(BaseModel):
    project_name: str
    difficulty: str
    estimated_time_weeks: int

class DailyPlanSlot(BaseModel):
    time_slot: str
    task: str

class RoadmapResponse(BaseModel):
    learning_order: list[LearningModule]
    projects: list[RoadmapProject]
    estimated_duration: str
    daily_plan: list[DailyPlanSlot]