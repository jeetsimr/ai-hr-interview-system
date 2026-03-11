from sqlalchemy import Column, Integer, String, Text
from database import Base


class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    # Personal Details
    name = Column(String)
    dob = Column(String)
    email = Column(String)
    phone = Column(String)
    location = Column(String)

    # Education
    qualification = Column(String)
    institution = Column(String)
    graduation_year = Column(String)

    # Work Experience
    experience_years = Column(String)
    last_company = Column(String)
    last_role = Column(String)
    responsibilities = Column(Text)

    # Compensation
    last_ctc = Column(String)
    last_inhand = Column(String)
    expected_salary = Column(String)
    notice_period = Column(String)

    # Career Stability
    reason_for_leaving = Column(Text)
    total_companies = Column(String)
    career_switch = Column(String)

    # Role Applied
    role_applied = Column(String)

    # Typing Test
    typing_speed = Column(String)
    typing_accuracy = Column(String)

    # Resume
    resume_link = Column(String)

    # AI Evaluation
    ai_summary = Column(Text)
    ai_score = Column(Integer)

    # Raw Interview Answers
    answers = Column(Text)