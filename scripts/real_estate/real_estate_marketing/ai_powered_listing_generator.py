import openai
import os

# Retrieve API Key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_real_estate_listing(property_details):
    """Generates real estate listings using OpenAI's latest API format."""
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": f"Generate a real estate listing description for: {property_details}"}]
    )
    
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    listing = generate_real_estate_listing("3-bed, 2-bath modern home with pool in Los Angeles")
    print(f"✅ AI-Generated Listing: {listing}")
