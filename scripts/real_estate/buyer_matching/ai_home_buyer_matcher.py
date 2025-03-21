import openai
import os

def match_home_buyer(buyer_preferences, available_properties):
    """
    AI-powered home buyer preference matcher.
    """
    prompt = f"Match the buyer preferences:\n{buyer_preferences}\n\nAvailable properties:\n{available_properties}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI real estate expert helping buyers find ideal properties."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    preferences = "Looking for a 2-bed condo near downtown, budget $400,000"
    listings = "1) 2-bed condo, $380K, near downtown\n2) 2-bed townhome, $420K, 10 min from downtown"
    match = match_home_buyer(preferences, listings)
    print(f"🔍 AI Home Buyer Match: {match}")
