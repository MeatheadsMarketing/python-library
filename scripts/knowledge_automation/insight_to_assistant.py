
import openai
import os

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set it before running this script.")

def generate_assistant_idea(category):
    """Converts an HVHE category into an AI assistant project idea."""
    prompt = f"Based on this knowledge domain, suggest a useful AI assistant idea:\n\n{category}"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    category = "SEO Strategy Development"
    assistant_idea = generate_assistant_idea(category)
    print(f"📌 AI Assistant Idea:\n{assistant_idea}")
