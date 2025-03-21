import openai
import os

def analyze_real_estate_investment(property_details, market_trends):
    """
    AI-powered investment analysis based on property details and market trends.
    """
    prompt = f"Analyze the investment potential of the following property:\n{property_details}\n\nMarket trends: {market_trends}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI expert in real estate investment analysis."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    property_details = "3-bed, 2-bath house in Miami, FL with waterfront views"
    market_trends = "Property values in Miami are rising by 7% annually."
    analysis = analyze_real_estate_investment(property_details, market_trends)
    print(f"🏡 AI Investment Analysis:\n{analysis}")
