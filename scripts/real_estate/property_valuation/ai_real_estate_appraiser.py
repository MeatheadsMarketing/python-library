
import openai
import os

def estimate_property_value(location, square_feet, bedrooms, bathrooms):
    """Estimates the value of a property based on key attributes."""
    prompt = f"Estimate the value of a property in {location} with {square_feet} sqft, {bedrooms} beds, {bathrooms} baths."
    
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI real estate valuation expert."},
            {"role": "user", "content": prompt},
        ]
    )
    
    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    value = estimate_property_value("Los Angeles", 2000, 3, 2)
    print(f"🏠 AI-Estimated Property Value: {value}")
