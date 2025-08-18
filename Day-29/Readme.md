# Day-29 Task: Using Environment Variables for AWS Keys

## 📌 What I Learned Today
Today I learned how to **store AWS Access Key and Secret Key securely** using an `.env` file and load them into Python using the `python-dotenv` library.

This helps to keep sensitive information (like AWS credentials) safe and not directly visible in the code.

---

## 🛠 Steps

### 1. Install Required Library
```bash
pip install python-dotenv
```

### 2. Create `.env` File
This file will hold AWS credentials (never push this file to GitHub).

Example `.env` file:
```
Aws_Access_Key="your key"
Aws_Secret_Key="your key"
```

### 3. Python Script (`task1.py`)
```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the keys from environment
access_key = os.getenv("Aws_Access_Key")
secret_key = os.getenv("Aws_Secret_Key")

# Function to mask the keys (show only first 4 characters)
def mask_key(value):
    return value[:4] + "****" if value else None

# Print masked keys
print(f"AWS Access Key: {mask_key(access_key)}")
print(f"AWS Secret Key: {mask_key(secret_key)}")
```

### 4. Output Example
```
AWS Access Key: Jsks****
AWS Secret Key: 1223****
```

---

## 🎯 Why This is Useful in DevOps?
- We **never hardcode credentials** in code.
- By using `.env` files, credentials are separated from code → safer and reusable.
- Masking ensures credentials are not fully visible in logs or console outputs.
- This is the **first step** towards **secrets management** (important in Cloud/DevOps).

---

## 🚀 Future Use Cases
- Use `.env` to store **database passwords**, **API tokens**, and **cloud credentials**.
- Integrate with **CI/CD pipelines** where environment variables are injected securely.
- Replace `.env` with secret managers like **AWS Secrets Manager**, **HashiCorp Vault**, etc.

---

✅ This task helped me understand how to safely manage credentials as a fresher in DevOps/Cloud journey.
