import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/content/credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Execution Performance").sheet1

# Read and update visualization data
execution_data = sheet.get_all_values()
chart_data = [[row[0], float(row[1].replace(" seconds", ""))] for row in execution_data if "Execution Time" in row[0]]

# Create Google Sheets chart (example: Bar Chart)
chart_code = """
{
  "chart": {
    "type": "bar"
  },
  "data": {
    "labels": %s,
    "datasets": [{
      "label": "Execution Time (seconds)",
      "data": %s
    }]
  }
}
""" % (str([x[0] for x in chart_data]), str([x[1] for x in chart_data]))

sheet.update_cell(1, 6, chart_code)  # Store chart JSON in cell F1
print("✅ Google Sheets updated with performance visualization!")
