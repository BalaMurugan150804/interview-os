from fastapi import FastAPI

app = FastAPI(
    title="InterviewOS",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to InterviewOS"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "InterviewOS",
        "version": "1.0.0"
    }