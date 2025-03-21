
import openai
import os

def optimize_airbnb_price(location, season, amenities):
    """Suggests optimal Airbnb rental pricing."""
    prompt = f"Suggest an optimal short-term rental price for an Airbnb in {location} during {season}, considering {amenities} amenities."
    
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI short-term rental pricing expert."},
            {"role": "user", "content": prompt},
        ]
    )
    
    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    price = optimize_airbnb_price("Miami Beach", "Summer", "Pool, Ocean View")
    print(f"🏖️ AI-Optimized Airbnb Price: {price}")
