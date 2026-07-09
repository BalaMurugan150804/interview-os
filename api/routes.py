from fastapi import APIRouter
from pydantic import BaseModel

from services.gemini_services import ask_gemini

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.get("/")
def home():
    return {
        "message": "Welcome to InterviewOS"
    }

@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "InterviewOS",
        "version": "1.0.0"
    }

@router.post("/ask")
def ask(request: PromptRequest):
    answer = ask_gemini(request.prompt)

    return {
        "response": answer
    }