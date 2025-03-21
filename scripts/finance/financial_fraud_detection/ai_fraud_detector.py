import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import openai
import pandas as pd

def detect_fraudulent_activity(transaction_data):
    """Analyzes financial transactions for fraudulent activity."""
    prompt = f"Analyze the following transaction data and detect potential fraudulent patterns: {transaction_data}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a financial analyst detecting fraudulent activities in transactions."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    transactions = [{"amount": 5000, "location": "NY", "frequency": "5x daily"}]
    fraud_alert = detect_fraudulent_activity(transactions)
    print(f"🚨 Fraud Detection Report: {fraud_alert}")
