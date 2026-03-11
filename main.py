from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from database import SessionLocal, engine
import models
from interview_questions import questions
from ai import evaluate_candidate

app = FastAPI()

# -----------------------------
# ENABLE CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=engine)


# -----------------------------
# DATABASE DEPENDENCY
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# REQUEST MODEL
# -----------------------------
class CandidateRequest(BaseModel):

    name: str
    dob: str
    email: str
    phone: str
    location: str

    qualification: str
    institution: str
    graduation_year: str

    experience_years: str
    last_company: str
    last_role: str
    responsibilities: str | None = None

    last_ctc: str
    last_inhand: str | None = None
    expected_salary: str
    notice_period: str

    reason_for_leaving: str | None = None
    total_companies: str | None = None

    role_applied: str | None = None
    typing_speed: str | None = None
    typing_accuracy: str | None = None
    resume_link: str | None = None


# -----------------------------
# HOME
# -----------------------------
@app.get("/")
def home():
    return {"message": "AI HR Interview Bot Running 🚀"}


# -----------------------------
# SERVE FRONTEND PAGES
# -----------------------------
@app.get("/interview")
def interview_page():
    return FileResponse("frontend/index.html")


@app.get("/dashboard")
def dashboard_page():
    return FileResponse("frontend/dashboard.html")


# -----------------------------
# GET QUESTIONS
# -----------------------------
@app.get("/questions")
def get_questions():
    return questions


# -----------------------------
# SUBMIT INTERVIEW
# -----------------------------
@app.post("/submit_interview")
def submit_interview(data: CandidateRequest, db: Session = Depends(get_db)):

    candidate = models.Candidate(

        name=data.name,
        dob=data.dob,
        email=data.email,
        phone=data.phone,
        location=data.location,

        qualification=data.qualification,
        institution=data.institution,
        graduation_year=data.graduation_year,

        experience_years=data.experience_years,
        last_company=data.last_company,
        last_role=data.last_role,
        responsibilities=data.responsibilities,

        last_ctc=data.last_ctc,
        last_inhand=data.last_inhand,
        expected_salary=data.expected_salary,
        notice_period=data.notice_period,

        reason_for_leaving=data.reason_for_leaving,
        total_companies=data.total_companies,

        role_applied=data.role_applied,
        typing_speed=data.typing_speed,
        typing_accuracy=data.typing_accuracy,
        resume_link=data.resume_link,

        answers=str(data.dict())
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    try:
        summary, score = evaluate_candidate(data.dict())
    except Exception as e:
        summary = f"AI evaluation failed: {str(e)}"
        score = None

    candidate.ai_summary = summary
    candidate.ai_score = score

    db.commit()

    return {
        "message": "Interview submitted successfully",
        "candidate_id": candidate.id,
        "ai_score": score,
        "ai_summary": summary
    }


# -----------------------------
# GET ALL CANDIDATES
# -----------------------------
@app.get("/candidates")
def get_candidates(db: Session = Depends(get_db)):
    return db.query(models.Candidate).all()


# -----------------------------
# GET TOP 10 CANDIDATES
# -----------------------------
@app.get("/top_candidates")
def top_candidates(db: Session = Depends(get_db)):
    candidates = (
        db.query(models.Candidate)
        .order_by(models.Candidate.ai_score.desc())
        .limit(10)
        .all()
    )
    return candidates