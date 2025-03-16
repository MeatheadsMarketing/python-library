import os
import base64
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("❌ ERROR: GITHUB_TOKEN is not set.")

owner = "MeatheadsMarketing"
repo = "python-library"
file_path = "example_script.py"
commit_message = "Added example script via GitHub API"
local_file = "example_script.py"

with open(local_file, "rb") as file:
    content = base64.b64encode(file.read()).decode()

url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
data = {"message": commit_message, "content": content}

response = requests.put(url, json=data, headers=headers)

if response.status_code == 201:
    print(f"✅ File '{file_path}' uploaded successfully!")
else:
    print(f"❌ Failed to upload file: {response.json()}")
