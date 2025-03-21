import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import openai

def predict_loan_default(borrower_info):
    """Predicts loan default probability based on borrower details."""
    prompt = f"Predict the default probability for the following borrower: {borrower_info}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a financial AI predicting loan default probabilities."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    borrower = {"loan_amount": 200000, "income": 60000, "credit_score": 680}
    default_risk = predict_loan_default(borrower)
    print(f"🏦 Loan Default Prediction: {default_risk}")
