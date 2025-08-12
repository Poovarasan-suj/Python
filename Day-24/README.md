
#  Python Script to Delete Old Log Files

This script automatically deletes files older than 7 days from a specified directory.
It's useful for managing disk space by removing outdated log files or other temporary data.

---

##  How the Script Works

```python
import os
import time
```

🔹 Import necessary modules:

* `os` → work with files & directories
* `time` → get current and file modified times

---

```python
folder_path = '/home/sujith/Python/logs'
days_to_keep = 7
now = time.time()
```

🔸 Set:

* `folder_path` → folder containing the logs
* `days_to_keep` → how many days you want to keep
* `now` → current time in seconds

---

```python
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
```

🔁 Loop through files in the folder and create full path

---

```python
    if os.path.isfile(file_path):
        file_mtime = os.path.getmtime(file_path)
```

✔️ Check if it's a file and get its last modified time

---

```python
        if (now - file_mtime) > (days_to_keep * 86400):
            os.remove(file_path)
            print(f"🗑️ Deleted: {file_path} (older than {days_to_keep} days)")
        else:
            print(f"✅ Kept: {file_path} (within {days_to_keep} days)")
```

🔹 If the file is older than `days_to_keep`, delete it
📌 86400 = number of seconds in a day

---

##  Suggested Fixes

* Print file name when deleted or kept
* Fix `else` so it only applies after age check (not for folders)

---

##  Tip to Remember

> “Check each file’s age → If older than X days → Remove it”

---

##  Automate with Cron (Linux)

You can schedule this script to run daily at 1:00 AM:

```bash
0 1 * * * /usr/bin/python3 /path/to/your_script.py
```

---

##  Sample Output

```text
 Kept: /home/sujith/Python/logs/app.log (within 7 days)
 Deleted: /home/sujith/Python/logs/old_report.log (older than 7 days)
```

