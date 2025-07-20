
### Jira Project Listing Script

**Author:** Poovarasan
**Date:** 2025-07-20

## Description

This Python script connects to your Jira Cloud instance using the **Jira REST API v3** and **Basic Authentication** to list all available projects for your account.

---

## Features

* Uses environment variables to securely load Jira login credentials
* Makes a GET request to `/rest/api/3/project`
* Parses and prints the names of all available Jira projects

---

##  Requirements

* Python 3.x
* Modules:

  * `requests`
  * `os`
  * `requests.auth`

Install `requests` if not already installed:

```bash
pip install requests
```

---

## 🔐 Environment Variables

Set the following environment variables before running:

```bash
export mail="your-email@example.com"
export api_token="your-api-token"
```

> Generate your API token at:
> [https://id.atlassian.com/manage/api-tokens](https://id.atlassian.com/manage/api-tokens)

---

## Script Code

```python
import requests
from requests.auth import HTTPBasicAuth
import json
import os

email_account = os.getenv("mail")
api_tokens = os.getenv("api_token")
domain = "epoovarasansujith25.atlassian.net"

url = f"https://{domain}/rest/api/3/project"

headers = {
    "Accept": "application/json"
}

auth = HTTPBasicAuth(email_account, api_tokens)

response = requests.get(url, headers=headers, auth=auth)

print("Status Code:", response.status_code)
try:
    data = response.json()
    for n in data:
        print(n["name"])
except Exception as e:
    print("Error:", e)
    print("Raw response:", response.text)
```



## Example Output

```
Status Code: 200
Project Alpha
DevOps Team
Cloud Migration

## Common Errors & Fixes

| Error                 | Reason                | Fix                                  |
| --------------------- | --------------------- | ------------------------------------ |
| `401 Unauthorized`    | Wrong email or token  | Double-check credentials             |
| `[]` (Empty response) | No access to projects | Ensure user is added to Jira project |
| KeyError              | JSON format mismatch  | Print raw response for debugging     |


