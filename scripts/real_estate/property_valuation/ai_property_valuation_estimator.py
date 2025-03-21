import openai
import os

def estimate_property_value(location, features, market_data):
    """
    AI-powered property valuation estimator based on market trends and features.
    """
    prompt = f"Estimate the value of a property located in {location} with the following features:\n{features}\n\nMarket data: {market_data}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI property valuation expert."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    valuation = estimate_property_value("San Diego, CA", "4 bed, 3 bath, ocean view", "Market prices up 5% year-over-year")
    print(f"🏡 AI Property Valuation Estimate: {valuation}")
