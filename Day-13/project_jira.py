import requests
from requests.auth import HTTPBasicAuth
import json
import os

email_account = os.getenv("mail")  #or  # The same one you use to log in to Jira UI
api_tokens = os.getenv("api_token")      # Create new one if needed
domain = "epoovarasansujith25.atlassian.net"
#project_key = "AB"

url = f"https://{domain}/rest/api/3/project"

headers = {
    "Accept": "application/json"
}

auth = HTTPBasicAuth(email_account, api_tokens)

response = requests.get(url, headers=headers, auth=auth)

print("Status Code:", response.status_code)
try:
    data = response.json()
    #print(json.dumps(data, indent=4))
    for n in data:
        print(n["name"])
    
except Exception as e:
    print("Error:", e)
    print("Raw response:", response.text)