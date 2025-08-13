## **Day-26: Print Hostname, Date, and Logged-in User**

### ** Objective**

Learn how to:

* Get the **hostname** of the current machine.
* Fetch the **current date** and **time**.
* Retrieve the **username** of the logged-in user.
* Format the output in a clean and readable way.

---

### ** Concepts Learned**

#### 1. **`socket.gethostname()`**

* **Purpose**: Get the system's hostname.
* **Example**:

```python
import socket
hostname = socket.gethostname()
print(hostname)  # e.g., MyLaptop
```

* **Use Case**: Useful in scripts where the machine identity is important, like in system monitoring.

---

#### 2. **`datetime` Module**

* **Purpose**: Work with dates and times in Python.
* **Two ways to get the date**:

  **(a) Only Date**

```python
import datetime
today = datetime.date.today()
print(today)  # YYYY-MM-DD
```

**(b) Date + Time**

```python
now = datetime.datetime.now()
print(now)  # Full date-time object
```

* **Formatting Dates & Times** with `.strftime()`:

```python
print(now.strftime("%Y-%m-%d"))  # Date in YYYY-MM-DD
print(now.strftime("%H:%M:%S"))  # Time in HH:MM:SS
```

**Common Format Codes**:

| Code | Meaning         | Example |
| ---- | --------------- | ------- |
| `%Y` | Year (4-digit)  | 2025    |
| `%m` | Month (2-digit) | 08      |
| `%d` | Day (2-digit)   | 13      |
| `%H` | Hour (24-hour)  | 14      |
| `%M` | Minute          | 05      |
| `%S` | Second          | 45      |

---

#### 3. **`getpass.getuser()`**

* **Purpose**: Get the current logged-in username.
* **Example**:

```python
import getpass
user = getpass.getuser()
print(user)  # e.g., root
```

---

### ** Final Code**

```python
import socket
import datetime
import getpass

# Get hostname
hostname = socket.gethostname()

# Get current date & time
now = datetime.datetime.now()

# Get logged-in user
user = getpass.getuser()

# Print formatted output
print(f"Server: {hostname} | Date: {now.strftime('%Y-%m-%d')} | Time: {now.strftime('%H:%M:%S')} | User: {user}")
```

---

### ** Output Example**

```
Server: MyLaptop | Date: 2025-08-13 | Time: 14:05:45 | User: poovarasan
```

---

### ** Key Takeaways**

* `socket` → System/network info (like hostname).
* `datetime` → Date & time manipulation.
* `strftime()` → Custom formatting for date/time.
* `getpass` → Retrieve username securely.

