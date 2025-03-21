
import openai
import os

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set it before running this script.")

def analyze_market_trends(location, property_type):
    """Analyzes real estate trends based on location and property type."""
    prompt = f"Analyze real estate trends in {location} for {property_type} properties."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI real estate market analyst."},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    location = "New York"
    property_type = "Luxury Condos"
    trends = analyze_market_trends(location, property_type)
    print(f"🏡 AI Market Trends Analysis for {location}: {trends}")
