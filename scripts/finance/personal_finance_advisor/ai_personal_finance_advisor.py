import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import openai

def personal_finance_advice(financial_data):
    """Provides financial advice based on personal financial data."""
    prompt = f"Provide financial planning advice for the following financial data: {financial_data}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a financial AI providing personal finance advice."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    finance_data = {"income": 70000, "expenses": 50000, "savings_goal": 20000}
    advice = personal_finance_advice(finance_data)
    print(f"💰 AI Personal Finance Advice: {advice}")
