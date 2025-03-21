

import openai
import os

def generate_email(subject, audience, goal):
    """
    Generates a marketing email based on audience and campaign goals.
    """
    prompt = f"Write a persuasive email with the subject '{subject}', targeting {audience}, with the goal of {goal}."

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional email marketing specialist."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    subject = "Exclusive AI Marketing Strategies for 2025!"
    audience = "Digital Marketers & Entrepreneurs"
    goal = "Boost email engagement and conversions"
    
    email_content = generate_email(subject, audience, goal)
    print(f"📧 AI-Generated Email:\n\n{email_content}")
