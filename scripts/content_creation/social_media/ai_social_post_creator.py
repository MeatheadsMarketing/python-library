
import openai
import os

def generate_social_post(platform, topic, hashtags):
    """
    Generates a social media post optimized for a specific platform.
    """
    prompt = f"Write a high-engagement social media post for {platform} about {topic}, using the hashtags {', '.join(hashtags)}."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert social media content strategist."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    platform = "Twitter"
    topic = "AI-Powered Marketing"
    hashtags = ["#AI", "#Marketing", "#FutureTech"]
    
    post = generate_social_post(platform, topic, hashtags)
    print(f"📢 AI-Generated Social Media Post:\n\n{post}")
