import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import openai

def assess_credit_risk(applicant_data):
    """Assesses an applicant's credit risk based on financial data."""
    prompt = f"Evaluate the credit risk for the following applicant: {applicant_data}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a financial AI evaluating credit risk."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    applicant = {"income": 50000, "debt": 10000, "credit_score": 720}
    risk_assessment = assess_credit_risk(applicant)
    print(f"📉 AI Credit Risk Assessment: {risk_assessment}")
