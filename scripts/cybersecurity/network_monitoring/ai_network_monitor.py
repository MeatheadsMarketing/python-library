
import openai
import os

def monitor_network_activity(network_logs):
    """
    AI-Powered Network Monitoring.
    Analyzes network traffic logs to detect anomalies or suspicious behavior.
    """
    prompt = f"Analyze the following network activity logs and detect any potential threats:\n{network_logs}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI network security analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    sample_logs = "Unusual high data transfer detected from server at 2 AM."
    alert = monitor_network_activity(sample_logs)
    print(f"🌐 AI-Detected Network Alert: {alert}")
