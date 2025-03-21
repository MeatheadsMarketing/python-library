

import openai
import os

def generate_blog_post(topic, keywords):
    """
    Generates an AI-powered blog post using OpenAI.
    """
    prompt = f"Write a detailed and engaging blog post about {topic} including these keywords: {', '.join(keywords)}."
    
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional blog writer."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    topic = "The Future of AI in Content Marketing"
    keywords = ["AI blogging", "SEO", "content automation"]
    
    blog_post = generate_blog_post(topic, keywords)
    print(f"📝 AI-Generated Blog Post:\n\n{blog_post}")
