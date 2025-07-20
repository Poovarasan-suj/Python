import requests
from requests.auth import HTTPBasicAuth
import os

from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    data = request.json
    print("📥 Received webhook:")
    print(data)

    if data.get("action") == "created" and "comment" in data:
        comment_body = data["comment"]["body"]
        print("💬 Comment body:", comment_body)

        if comment_body.startswith("/jira"):
            issue_text = comment_body[len("/jira"):].strip()
            print("🚀 Creating Jira issue with:", issue_text)

            # 🔐 Jira credentials from environment variables
            email_account = os.getenv("email") 
            api_token = os.getenv("api_token") 
            project_key = "AB"  # Your Jira project key

            # Jira API endpoint
            url = f"https://{domain}/rest/api/3/issue"

            # Jira payload
            payload = {
                "fields": {
                    "project": {"key": project_key},
                    "summary": issue_text,
                    "description": {
                        "type": "doc",
                        "version": 1,
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [
                                    {"type": "text", "text": issue_text}
                                ]
                            }
                        ]
                    },
                    "issuetype": {"name": "Task"}
                }
            }

            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }

            auth = HTTPBasicAuth(email_account, api_token)

            response = requests.post(url, headers=headers, json=payload, auth=auth)

            if response.status_code == 201:
                print("✅ Jira issue created successfully.")
            else:
                print("❌ Failed to create Jira issue.")
                print("Status:", response.status_code)
                print("Response:", response.text)

    return "Webhook received", 200
if __name__ == "__main__":
    app.run(port=5000)
# To run the server, use the command: python webhooks_server.py
# Ensure Flask is installed in your environment: pip install Flask