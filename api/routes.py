from fastapi import APIRouter
from fastapi import UploadFile, File
from parsers.career_goal_parser import CareerGoal
from services.pdf_service import extract_text_from_pdf
from services.gemini_services import analyze_resume
from services.career_router import route_career
from parsers.company_models import CompanyRequest
from services.company_services import analyze_company
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

@router.post("/career/goal")
def choose_goal(goal: CareerGoal):

    return route_career(goal.goal)

@router.post("/company/analyse")
def company_analysis(request: CompanyRequest):
    return analyze_company(request.company_name)