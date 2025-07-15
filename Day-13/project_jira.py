import requests
from requests.auth import HTTPBasicAuth
import json

email = "email account"     # The same one you use to log in to Jira UI
api_token = "API token key"         # Create new one if needed
domain = "* .atlassian.net"
project_key = "SCRUM"

url = f"https://{domain}/rest/api/3/project/{project_key}"

headers = {
    "Accept": "application/json"
}

auth = HTTPBasicAuth(email, api_token)

response = requests.get(url, headers=headers, auth=auth)

print("Status Code:", response.status_code)
try:
    data = response.json()
    #print(json.dumps(data, indent=4))
    print(data["key"])
except Exception as e:
    print("Error:", e)
    print("Raw response:", response.text)