import os
import re
from openai import OpenAI
from dotenv import load_dotenv

# load .env variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# create OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


def evaluate_candidate(data):

    prompt = f"""
You are an HR hiring assistant.

Analyze the candidate data and provide:

1. Candidate Summary
2. Strengths
3. Weaknesses
4. Final Score out of 100

Candidate Information:

Name: {data.get("name")}
Qualification: {data.get("qualification")}
Experience: {data.get("experience_years")}
Last Company: {data.get("last_company")}
Last Role: {data.get("last_role")}
Expected Salary: {data.get("expected_salary")}
Notice Period: {data.get("notice_period")}

IMPORTANT: Always write the score like this:
Score: XX/100
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an HR hiring expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        result = response.choices[0].message.content

        # Extract score using regex
        score_match = re.search(r'(\d{1,3})/100', result)
        score = int(score_match.group(1)) if score_match else None

        return result, score

    except Exception as e:
        return f"AI evaluation failed: {str(e)}", None