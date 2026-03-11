# AI HR Interview Evaluation System

An AI-powered HR assistant that analyzes candidate details and automatically evaluates candidates using OpenAI.

This system helps HR teams quickly screen candidates by generating:

* Candidate summary
* Strengths
* Weaknesses
* AI score out of 100

---

## Features

* AI-powered candidate evaluation
* Automatic scoring system
* HR-friendly candidate summary
* FastAPI backend API
* Secure API key management using environment variables
* Regex-based score extraction

---

## Tech Stack

* Python
* FastAPI
* OpenAI API
* SQLite
* Regex
* python-dotenv

---

## Project Structure

```
AI-HR-INTERVIEW-SYSTEM
│
├── main.py
├── ai.py
├── candidates.db
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/your-username/ai-hr-interview-system.git
```

Navigate to the project:

```
cd ai-hr-interview-system
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Running the Project

Start the FastAPI server:

```
uvicorn main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Example Candidate Input

```
{
"name": "Rahul Sharma",
"qualification": "B.Tech Computer Science",
"experience_years": 3,
"last_company": "TCS",
"last_role": "Software Developer",
"expected_salary": "10 LPA",
"notice_period": "30 days"
}
```

---

## AI Output Example

```
Candidate Summary:
Rahul Sharma is a software developer with 3 years of experience.

Strengths:
- Good technical background
- Experience in corporate environment

Weaknesses:
- Limited leadership exposure

Score: 78/100
```

---

## Future Improvements

* Resume parsing
* AI interview question generation
* Candidate ranking system
* Dashboard for HR teams
* Vector database for candidate search

---

## Author

Simran Kaur

AI / Automation Developer
