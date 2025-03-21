import openai
import os

def analyze_commercial_lease(lease_terms, market_rates):
    """
    AI-powered commercial lease analyzer.
    """
    prompt = f"Analyze the following commercial lease terms:\n{lease_terms}\n\nCompare with market rates: {market_rates}"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI lease agreement expert analyzing commercial lease terms."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    lease = "5-year lease, $25/sqft, annual increase 3%"
    market = "Market rates range from $23-$27/sqft with similar annual increases."
    analysis = analyze_commercial_lease(lease, market)
    print(f"📜 AI Lease Analysis: {analysis}")
