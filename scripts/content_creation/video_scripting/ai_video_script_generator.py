

import openai
import os

def generate_video_script(topic, length="short"):
    """
    Generates a structured video script for a YouTube or social media video.
    """
    prompt = f"Write a {length} video script for YouTube about {topic}. Include an engaging hook, main content, and a call-to-action."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional video script writer."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    topic = "Top 5 AI Trends in 2025"
    script = generate_video_script(topic, "short")
    print(f"🎥 AI-Generated Video Script:\n\n{script}")
