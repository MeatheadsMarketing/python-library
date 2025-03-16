import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_contract(text):
    """Analyzes real estate contracts for key terms and clauses."""
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

# Example usage
if __name__ == "__main__":
    contract_text = "This contract states that the property at 123 Main St. will be sold for $500,000."
    clauses = analyze_contract(contract_text)
    print(f"✅ Key Contract Terms: {clauses}")
