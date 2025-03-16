import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("❌ ERROR: GITHUB_TOKEN is not set.")

repo_name = "new-repo"
description = "Automatically created via GitHub API"

url = "https://api.github.com/user/repos"
headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
data = {"name": repo_name, "description": description, "private": False}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print(f"✅ Repository '{repo_name}' created successfully!")
else:
    print(f"❌ Failed to create repository: {response.json()}")
