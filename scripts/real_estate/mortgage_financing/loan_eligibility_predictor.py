def check_loan_eligibility(credit_score, income, debt):
    """Determines mortgage loan eligibility based on credit score and debt-to-income ratio."""
    if credit_score > 700 and (income / debt) > 3:
        return "Eligible for Loan"
    return "Not Eligible"

# Example usage
if __name__ == "__main__":
    status = check_loan_eligibility(720, 5000, 1200)
    print(f"✅ Loan Eligibility Status: {status}")
