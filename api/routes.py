from fastapi import APIRouter

router = APIRouter()

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