def calculate_roi(purchase_price, rental_income, expenses):
    """Calculates Return on Investment (ROI) for rental properties."""
    annual_cash_flow = (rental_income - expenses) * 12
    roi = (annual_cash_flow / purchase_price) * 100
    return roi

# Example usage
if __name__ == "__main__":
    roi = calculate_roi(300000, 2000, 500)
    print(f"✅ Estimated ROI: {roi:.2f}%")
