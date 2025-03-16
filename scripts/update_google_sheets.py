import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

# Authenticate Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/content/credentials.json", scope)
client = gspread.authorize(creds)

# Open Google Sheet
sheet = client.open("Python Library Reference").sheet1

# Read functions from CSV file
csv_file = "function_list.csv"
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    function_list = list(reader)

# Update Google Sheet with new function entries
for row in function_list[1:]:  # Skip header
    sheet.append_row(row)

print("✅ Google Sheets updated with new library functions!")
