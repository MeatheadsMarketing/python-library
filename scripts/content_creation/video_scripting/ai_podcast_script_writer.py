

import openai
import os

def generate_podcast_script(topic, duration="10 minutes"):
    """Generates a structured podcast script."""
    prompt = f"Write a {duration} podcast script on {topic}, including an introduction, key discussion points, and a conclusion."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a professional podcast script writer."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    topic = "The Rise of AI in Podcasting"
    script = generate_podcast_script(topic, "15 minutes")
    print(f"🎙️ AI-Generated Podcast Script:\n\n{script}")
