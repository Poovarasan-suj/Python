
## 📌 What is `subprocess`?

The `subprocess` module lets you run **Linux/Windows terminal commands** from a Python script.

It’s like using Python to "talk to the terminal."

## ✨ Why Use It?

- Run shell commands (like `ls`, `pwd`, `systemctl`)
- Automate tasks like restarting services or running scripts
- Capture and use command outputs

---

## 🔧 Basic Syntax

```python
import subprocess

subprocess.run(["command", "arg1", "arg2"])
````

Example:

```python
subprocess.run(["echo", "Hello"])
```

Output:

```
Hello
```

---

## ✅ Real Command Examples

### 1. List files (like `ls`)

```python
subprocess.run(["ls"])
```

### 2. Show current folder (like `pwd`)

```python
subprocess.run(["pwd"])
```

### 3. Print a message (like `echo`)

```python
subprocess.run(["echo", "Hello from Python"])
```

---

## 🚨 Handling Errors with `check=True`

```python
subprocess.run(["ls", "wrong-folder"], check=True)
```

* ✅ If it runs OK → nothing happens.
* ❌ If the command fails → it raises a `CalledProcessError`.

###  Safer with Try-Except

```python
try:
    subprocess.run(["ls", "wrong-folder"], check=True)
except subprocess.CalledProcessError as e:
    print("❌ Command failed:", e)
```

---

##  What if the command doesn’t exist?

```python
subprocess.run(["wrong_command"], check=True)
```

This gives a `FileNotFoundError`, not `CalledProcessError`.

### Handle both:

```python
try:
    subprocess.run(["wrong_command"], check=True)
except subprocess.CalledProcessError:
    print("Command ran but failed.")
except FileNotFoundError:
    print("Command does not exist.")
```

---

##  Restarting a Service (Linux)

```python
service = input("Enter service name to restart: ")

try:
    subprocess.run(["sudo", "systemctl", "restart", service], check=True)
    print(f"{service} restarted successfully.")
except subprocess.CalledProcessError:
    print("Restart failed.")
except FileNotFoundError:
    print("Command or service not found.")
```

---

## Summary

| Concept         | Example                   | Use                   |
| --------------- | ------------------------- | --------------------- |
| Run command     | `subprocess.run(["ls"])`  | Basic shell command   |
| Show output     | `echo`, `pwd`, `ls`       | Test understanding    |
| Restart service | `systemctl restart`       | Real-world automation |
| Error handling  | `check=True` + try/except | Safer scripts         |






