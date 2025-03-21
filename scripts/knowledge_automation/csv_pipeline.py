
import openai
import os
import csv

# Ensure API Key is Set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing. Set it before running this script.")

def convert_to_csv(data, filename="knowledge_pipeline.csv"):
    """Converts structured data into a downloadable CSV file."""
    file_path = f"/content/{filename}"
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
    
    print(f"📌 CSV Generated: {file_path}")

# Example Usage
if __name__ == "__main__":
    data = [
        ["Category", "Insight", "Action Step"],
        ["SEO Strategy", "Backlinks boost rankings", "Analyze competitor backlinks"],
        ["Content Marketing", "Long-form content performs better", "Write 2,000+ word guides"]
    ]
    convert_to_csv(data)
