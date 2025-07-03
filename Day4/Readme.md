
### What is an Environment Variable?

An **environment variable** is a value (like a setting) stored outside your Python program.
It is used to hold information such as usernames, passwords, and database links.

---

### Why Use It?

* To keep secret information (like API keys) safe
* To avoid writing the same value inside the code
* To make your program work in different systems without changing the code

---
### How to Use Environment Variables in Python

We use the `os` module to access environment variables:

```python
import os

# Get the value of a variable named USER
user = os.getenv("USER")
print("Current user:", user)
```

---

### 🛠️ How to Set an Environment Variable (Temporarily)

#### 🔸On Linux or Mac (in terminal):

```bash
export MY_VAR="HelloPython"
python env_variables.py
```

### Set Variable Inside Python (for practice only)

```python
import os

os.environ["MY_VAR"] = "TestValue"
print(os.environ["MY_VAR"])
```

⚠️ This only works inside that script and is not stored in the system.





-


