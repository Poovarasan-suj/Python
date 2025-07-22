
# 📝 Python Logging - Beginner's Guide

Python’s `logging` module lets you record events from your program — useful for debugging, error tracking, and understanding what your program is doing.

---

## Why Use Logging Instead of print()?

| print()                        | logging                         |
|-------------------------------|----------------------------------|
| Just prints messages           | Logs info, warnings, errors     |
| No control over message level | Can filter by message importance |
| Doesn't write to file         | Can log to files automatically   |

---

##  Logging Levels

| Level       | Use When...                             |
|-------------|------------------------------------------|
| `DEBUG`     | For very detailed internal info 🛠️       |
| `INFO`      | General updates or steps done ℹ️         |
| `WARNING`   | Something seems off, but it's not broken ⚠️ |
| `ERROR`     | Something went wrong ❌                   |
| `CRITICAL`  | Serious issue; app might crash 🔥         |

---

## 🧪 Basic Logging Example

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("Something went wrong!")
```

🖥️ Output:
```
INFO:root:This is an info message
WARNING:root:This is a warning
ERROR:root:Something went wrong!
```

---

##  Logging to a File

```python
import logging

logging.basicConfig(
    filename='my_log_file.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("This message will go into a file.")
```

📂 After running, `my_log_file.log` will contain:
```
2025-07-22 08:00:00,000 - INFO - This message will go into a file.
```

---

##  Common Mistakes

```python
#  Wrong (using logging.debug instead of logging.DEBUG)
level=logging.debug  # This is a function, not a constant!

# Correct
level=logging.DEBUG
```

---
## Logging in a Function with Try/Except

```python
import logging

logging.basicConfig(level=logging.INFO)

def divide(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero is not allowed.")
        return None

divide(10, 2)  # OK
divide(10, 0)  # Logs error
```

---

##  Log All Levels Example

```python
import logging

logging.basicConfig(
    filename='test.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("Debugging details")
logging.info("Information")
logging.warning("Warning message")
logging.error("An error occurred")
logging.critical("Critical issue!")
```

---

##  Summary

- Use `logging` to monitor your code.
- Choose the correct **log level**.
- Save logs to a **file** if needed.
- Avoid using `print()` in real applications.


