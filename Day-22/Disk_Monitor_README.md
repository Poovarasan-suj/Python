
## 🔍 **Script Explanation**

```python
import shutil
import logging
```

* **`shutil`**: Used for high-level file operations. Here, you use it to get disk usage statistics.
* **`logging`**: Built-in module to write logs to a file (instead of printing to the console). Ideal for monitoring and debugging.

---

```python
usage = shutil.disk_usage('/')
```

* Retrieves disk usage statistics of the root (`/`) partition.
* Returns a named tuple: `(total, used, free)`, all in bytes.

---

```python
logging.basicConfig(
    filename='my_disk.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

* **`filename`**: Specifies the log file name: `my_disk.log`.
* **`level=logging.INFO`**: Only INFO-level messages and above will be logged.
* **`format`**: How log messages will look:

  * `%(asctime)s`: Timestamp of the log
  * `%(levelname)s`: Log level (e.g., INFO, WARNING)
  * `%(message)s`: The message you pass

---

```python
threshold = 80
used = (usage.used / usage.total) * 100
```

* **`threshold`**: Set limit at 80%.
* **`used`**: Calculates the percentage of disk used.

---

```python
if used > threshold :
    logging.info(f'Used Usage has exceeded the threshold. current Usage {used:.2f} %')
```

* If usage exceeds the threshold, it logs a warning message including the exact usage to 2 decimal places.


```python
else:
    logging.info(f'Root disk having enough space. current usage {used:.2f} %')`

* If usage is below or equal to 80%, it logs that there is enough space, with the current usage.

## ✅ **What This Script Does**

* Monitors the disk space on the root (`/`) filesystem.
* Logs a message if disk usage exceeds 80%.
* Logs current disk usage percentage either way.
* Stores logs in a file called `my_disk.log`.


## 📝 Example Log Output
2025-08-05 08:30:02,123 - INFO - Root disk having enough space. current usage 43.56 %

Or:

2025-08-05 08:31:10,789 - INFO - Used Usage has exceeded the threshold. current Usage 82.15 %



