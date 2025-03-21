
import openai
import os

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set it before running this script.")

def extract_high_value_headers(text):
    """Extracts 10 ultra-valuable category headers from a course/module."""
    prompt = f"Extract 10 strategic, high-value headers from this content:\n\n{text}"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)  # Set API key properly
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    sample_text = "This is a course about digital marketing covering SEO, PPC, email marketing, and analytics."
    headers = extract_high_value_headers(sample_text)
    print(f"📌 HVHE Headers Extracted:\n{headers}")
