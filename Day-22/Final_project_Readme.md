
# 📧 Sending Email Alerts Using Python's smtplib

This project demonstrates how to send automated email alerts using Python's built-in `smtplib` module — a useful skill for DevOps tasks such as disk usage alerts, error notifications, and monitoring scripts.

---

## What is `smtplib`?

Python's `smtplib` module allows your program to send emails using the **Simple Mail Transfer Protocol (SMTP)**.

This is commonly used in:
- Automated alerting (e.g., disk full)
- Scheduled email reports
- System failure notifications

---
## Prerequisites

- Python 3.x installed
- Access to a **Gmail account**
- A **Gmail App Password** (for secure login)

---

## How to Get Gmail App Password

1. Enable **2-Step Verification** on your Google Account.
2. Go to [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Generate an **App Password** for "Mail".
4. Use this App Password in your script **instead of your normal Gmail password**.

---

##  Required Libraries

| Library      | Purpose                              |
|--------------|--------------------------------------|
| `shutil`     | Get disk usage stats                 |
| `smtplib`    | Send emails over SMTP                |
| `logging`    | Write warnings/errors to a log file  |

All are built-in in Python, so no need to install them manually.

---

##  Script: Disk Usage Alert with Email Notification

```python
import shutil              # For checking disk usage
import smtplib             # For sending emails
import logging             # For logging warnings/errors

# Configure logging
logging.basicConfig(
    filename='disk_usage.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email settings
sender_email = 'your_email@gmail.com'
receiver_email = 'receiver_email@example.com'
password = 'your_gmail_app_password'  # Use App Password here

# Define the email message with disk usage details
message = f"""Subject:  Warning - Disk Usage Alert

Hello,

This is an automated alert from your disk monitoring system.

 Disk usage has exceeded the threshold.
Please take necessary action.

Best regards,
Disk Monitoring System

Note: This is an automated message. Do not reply.
"""

# Define threshold and check current usage
threshold = 80  # in percentage
usage = shutil.disk_usage('/')  # Get disk usage for root directory

# Calculate usage in percent
current_usage = usage.used / usage.total * 100

# If usage exceeds threshold, send email
if current_usage > threshold:
    try:
        # Establish connection to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # 587 is the TLS port
        server.starttls()                             # Start TLS encryption
        server.login(sender_email, password)          # Login to Gmail account
        server.sendmail(sender_email, receiver_email, message)  # Send email
        server.quit()                                 # Close the SMTP connection

        # Log the warning
        logging.warning(f"Disk usage is above {threshold}%: {current_usage:.2f}%")

    except Exception as e:
        # Log any error that occurs during the email sending
        logging.error(f"Failed to send email alert: {e}")
else:
    print(f" Disk usage is normal: {current_usage:.2f}%")
````

---

##  Code Explanation

| Line                     | Explanation                                  |
| ------------------------ | -------------------------------------------- |
| `shutil.disk_usage('/')` | Checks disk usage of root directory          |
| `current_usage = ...`    | Calculates disk usage in percent             |
| `threshold = 80`         | Set your alert limit (can be 20%, 50%, etc.) |
| `smtplib.SMTP(...)`      | Connects to Gmail’s SMTP server              |
| `server.starttls()`      | Starts a secure encrypted connection         |
| `server.login(...)`      | Authenticates using Gmail + App Password     |
| `server.sendmail(...)`   | Sends the email alert                        |
| `logging.warning(...)`   | Writes alert info to a log file              |
| `try...except`           | Catches and logs errors during email send    |

---

##  Sample Output

When usage exceeds the threshold:

```
2025-08-05 08:15:34,217 - WARNING - Disk usage is above 80%: 85.23%
```

When usage is normal:

 Disk usage is normal: 42.56%
```

## 🙌 Author

**Poovarasan E** – Python for DevOps Learner
This project is part of my automation journey. Feel free to fork, improve, and use it in your own DevOps setups!
