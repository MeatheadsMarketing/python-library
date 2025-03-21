
import openai
import os

def predict_mortgage_eligibility(income, credit_score, down_payment):
    """Predicts mortgage eligibility based on financial details."""
    prompt = f"Determine mortgage eligibility for an individual with ${income} income, {credit_score} credit score, and ${down_payment} down payment."
    
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI mortgage approval expert."},
            {"role": "user", "content": prompt},
        ]
    )
    
    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    eligibility = predict_mortgage_eligibility(80000, 720, 20000)
    print(f"💰 AI Mortgage Eligibility Prediction: {eligibility}")
