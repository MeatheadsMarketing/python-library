import openai
import os

def calculate_rental_roi(property_price, monthly_rent, expenses):
    """
    AI-powered rental property ROI calculator.
    """
    prompt = f"Calculate the ROI for a rental property:\nPrice: ${property_price}\nMonthly Rent: ${monthly_rent}\nExpenses: ${expenses}/month"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI expert in rental property investments."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    roi = calculate_rental_roi(250000, 2000, 500)
    print(f"🏠 AI Rental ROI Estimate: {roi}")
