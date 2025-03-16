import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_real_estate_listing(property_details):
    """Generates real estate listings using AI."""
    prompt = f"Generate a real estate listing description for: {property_details}"
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Example usage
if __name__ == "__main__":
    listing = generate_real_estate_listing("3-bed, 2-bath modern home with pool in Los Angeles")
    print(f"✅ AI-Generated Listing: {listing}")
