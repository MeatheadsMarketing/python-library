import os
import requests

# Retrieve GitHub Token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("❌ ERROR: GITHUB_TOKEN is not set.")

# Test authentication
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
response = requests.get("https://api.github.com/user", headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(f"✅ Connected to GitHub as: {user_data['login']}")
else:
    print(f"❌ GitHub Authentication Failed: {response.json()}")
