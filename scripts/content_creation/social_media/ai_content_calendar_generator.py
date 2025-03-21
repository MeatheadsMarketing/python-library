

import openai
import os

def generate_content_calendar(topic, duration="30 days"):
    """Generates a structured content calendar for a given duration."""
    prompt = f"Create a content calendar for {topic} for the next {duration}. Include blog posts, videos, and social media content ideas."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an expert content strategist."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    topic = "Digital Marketing Trends"
    calendar = generate_content_calendar(topic, "60 days")
    print(f"📅 AI-Generated Content Calendar:\n\n{calendar}")
