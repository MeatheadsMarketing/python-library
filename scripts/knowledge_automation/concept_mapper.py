
import openai
import os

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set it before running this script.")

def generate_concept_map(text):
    """Creates a concept map showing how key ideas are interconnected."""
    prompt = f"Generate a structured concept map with relationships for:\n\n{text}"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    sample_content = "SEO consists of on-page optimization, backlinks, and keyword research."
    concept_map = generate_concept_map(sample_content)
    print(f"📌 Concept Map:\n{concept_map}")
