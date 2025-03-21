
import openai
import os

def detect_threats(network_logs):
    """
    AI-Powered Threat Detection System.
    Analyzes network logs to detect suspicious activity.
    """
    prompt = f"Analyze the following network logs and detect any potential threats:\n{network_logs}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI threat detection analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    sample_logs = "Unauthorized access attempt detected from IP 192.168.1.100 at 3 AM."
    alert = detect_threats(sample_logs)
    print(f"🚨 AI-Detected Threat Alert: {alert}")
