
import openai
import os

def respond_to_incidents(incident_logs):
    """
    AI-Powered Incident Response.
    Analyzes security incidents and provides a step-by-step response plan.
    """
    prompt = f"Analyze the following security incidents and provide a response plan:\n{incident_logs}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI security incident response expert."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    incident_logs = "Server breach detected on March 20th, 2025. Unauthorized file access recorded."
    response_plan = respond_to_incidents(incident_logs)
    print(f"📌 AI Incident Response Plan: {response_plan}")
