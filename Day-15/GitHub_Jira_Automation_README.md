#  GitHub + Jira Automation Project

**Author:** Poovarasan  
**Date:** 2025-07-20

---

##  Overview

This project automates the creation of Jira issues whenever someone comments `/jira <message>` in a GitHub issue or pull request.

It uses:
- Flask (Python) for a webhook listener
- Ngrok to expose the local server
- GitHub webhooks to receive events
- Jira REST API to create tickets

---

## Features Implemented

| Feature | Status |
|--------|--------|
| Flask server for GitHub webhooks | ✅ Done |
| Ngrok tunnel to make local server public | ✅ Done |
| GitHub webhook integration | ✅ Done |
| Parse `/jira` comment from GitHub | ✅ Done |
| Automatically create Jira issue | ✅ Done |

---

## Technologies Used

- Python 3
- Flask
- Ngrok
- GitHub Webhooks
- Jira REST API
- requests module

---
## How It Works

### Step-by-Step Flow

1. **User comments** on GitHub:
   ```
   /jira The login button is not working
   ```

2. GitHub sends a webhook payload → received by Flask server.

3. Flask extracts the comment text and checks if it starts with `/jira`.

4. If it does, the server extracts the text and sends it to Jira REST API.

5. Jira creates the issue in the project automatically.

---

## Project Structure

```
jira-github-webhook/
├── project.py              # Main Flask server that handles webhooks and creates Jira issues
├── .env (optional)         # Stores secrets securely (email, token)
├── README.md               # This file
```

---

##  project.py - Final Working Code

```python
import requests
from requests.auth import HTTPBasicAuth
import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    data = request.json
    print(" Received webhook:")
    print(data)

    if data.get("action") == "created" and "comment" in data:
        comment_body = data["comment"]["body"]
        print(" Comment body:", comment_body)

        if comment_body.startswith("/jira"):
            issue_text = comment_body[len("/jira"):].strip()
            print("Creating Jira issue with:", issue_text)

            email_account = "mail_acoount"
            api_token = "YOUR_API_TOKEN"
            domain = "epoovarasansujith25.atlassian.net"
            project_key = "AB"

            url = f"https://epoovarasansujith25.atlassian.net/rest/api/3/issue"

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
                print(" Jira issue created successfully.")
            else:
                print("Failed to create Jira issue.")
                print("Status:", response.status_code)
                print("Response:", response.text)

    return "Webhook received", 200

if __name__ == "__main__":
    app.run(port=5000)
```

---

##  Common Errors & Fixes

| Problem | Solution |
|--------|----------|
| `401 Unauthorized` | Wrong API token or missing Jira permission |
| `405 Method Not Allowed` | Missing `methods=["POST"]` in Flask |
| Env variables not working | Hardcode email/token or use `.env` + `python-dotenv` |
| Webhook not triggering | Check GitHub webhook settings and Ngrok is live |

---

##  Tips to Remember

- Keep Jira API token safe. Don’t push it to GitHub.
- Reuse Ngrok only for development.
- Use `.env` files for storing secrets in production.
- Always test by commenting `/jira something` in GitHub.

---

##  Conclusion

You're now equipped to:
- Build GitHub automation
- Integrate REST APIs
- Create custom dev workflows

Next steps?
- Add support for other issue types
- Add comment back to GitHub when issue is created
- Log Jira issue key

---

## 🏁 End of README
