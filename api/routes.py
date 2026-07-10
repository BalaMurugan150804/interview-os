from fastapi import APIRouter
from fastapi import UploadFile, File
from services.pdf_service import extract_text_from_pdf
from services.gemini_services import analyze_resume
import shutil
import uuid
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
    return answer

@router.post("/resume/upload")
def upload_resume(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        return {
            "error": "Only PDF files are allowed."
        }
    
    unique_filename = f"{uuid.uuid4()}.pdf"
    file_path = f"uploads/{unique_filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(file_path)

    analysis = analyze_resume(text)
    return analysis