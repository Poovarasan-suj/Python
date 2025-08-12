
# Automate User Creation with Python (Single User Version)

## 📌 Overview

This Python script automates the process of **adding a single Linux user**, setting a password, and assigning the user to a specific group.
It’s handy for quickly provisioning accounts without manually running multiple Linux commands.

---

## 🚀 Features

* Creates a user if they don’t already exist.
* Sets the password automatically.
* Adds the user to a given group.
* Avoids duplicate creation by checking user existence.

---

## 🖥️ Code Workflow

1. **Check if the user exists** using:

   ```python
   subprocess.run(["id", username])
   ```
2. **Create the user** with:

   ```python
   subprocess.run(["sudo", "useradd", username])
   ```
3. **Set the password** using:

   ```python
   subprocess.run(["sudo", "chpasswd"], input=f"{username}:{password}")
   ```
4. **Add to group** using:

   ```python
   subprocess.run(["sudo", "usermod", "-aG", group, username])
   ```

---

## 📂 Script Example

```python
import subprocess

username = "demo2"
password = "test1234"
group = "sudo"

# Check if user exists
if subprocess.run(["id", username], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
    subprocess.run(["sudo", "useradd", username], check=True)
    subprocess.run(["sudo", "chpasswd"], input=f"{username}:{password}", text=True, check=True)
    subprocess.run(["sudo", "usermod", "-aG", group, username], check=True)
    print(f"✅ {username} created with password and added to group '{group}'.")
else:
    print(f"⚠️ User {username} already exists.")
```

---

## ⚙️ Usage

Run the script with `sudo` privileges:

```bash
sudo python3 create_user.py
```

---

## 📝 Notes

* `stdout=subprocess.DEVNULL` and `stderr=subprocess.DEVNULL` hide command outputs for a cleaner script output.
* The script uses `returncode` to decide whether the user exists (`0` = exists, non-zero = does not exist).
* **Security caution:** The password is stored in plain text — not recommended for production.

---

## 📌 Requirements

* Linux system with `sudo` privileges.
* Python 3.x installed.
* User running the script must have permission to create new users.

