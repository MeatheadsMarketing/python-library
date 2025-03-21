
import openai
import os

def detect_intrusions(system_logs):
    """
    AI-Powered Intrusion Detection System.
    Analyzes system logs to detect unauthorized access attempts.
    """
    prompt = f"Analyze the following system logs and detect any potential intrusions:\n{system_logs}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI intrusion detection analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    sample_logs = "Multiple failed login attempts from an unknown user at midnight."
    alert = detect_intrusions(sample_logs)
    print(f"🚨 AI-Detected Intrusion Alert: {alert}")
