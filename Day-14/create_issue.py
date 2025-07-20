import requests
from requests.auth import HTTPBasicAuth
import json
import os
# This script creates an issue in Jira using the Jira REST API.
url = "https://epoovarasansujith25.atlassian.net/rest/api/3/issue"

email_account = os.getenv("email") 
api_tokens = os.getenv("api_token")

auth = HTTPBasicAuth(email_account, api_tokens)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = {
    "fields": {
        "project": {
            "key": "AB"
        },
        "summary": "Creating an issue using the Jira API",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "This is a test issue created via the Jira API"
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Task"
        }
    }
}
# Make the request to create the issue

response = requests.request(
   "POST",
   url,
   json=payload,
   headers=headers,
   auth=auth
)

if response.status_code == 201:
    print("Issue created successfully.")
else:
    print(f"Failed to create issue. Status code: {response.status_code}")
    print(f"Response: {response.text}") 