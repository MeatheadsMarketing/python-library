
import openai
import os

def check_contract_compliance(contract_text):
    """Analyzes a real estate contract for legal compliance issues."""
    prompt = f"Check the following real estate contract for legal compliance:\n\n{contract_text}"
    
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI real estate contract analyst."},
            {"role": "user", "content": prompt},
        ]
    )
    
    return response.choices[0].message.content.strip()

# Example Usage
if __name__ == "__main__":
    contract = "This agreement is made between Buyer and Seller for the sale of property located at 123 Main St."
    compliance_check = check_contract_compliance(contract)
    print(f"📜 AI Contract Compliance Review: {compliance_check}")
