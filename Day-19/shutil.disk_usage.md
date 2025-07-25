
# Python `shutil` Module – Disk Usage and File Operations

This document summarizes how to use Python's `shutil` module to work with files, directories, and check disk usage — especially useful in DevOps and cloud engineering.

---

## What is `shutil.disk_usage()`?

```python
import shutil
usage = shutil.disk_usage("/")
```

This function checks **disk space on the root filesystem (`/`)** and returns:

- `usage.total` → Total disk space in bytes
- `usage.used` → Used space in bytes
- `usage.free` → Free space in bytes

---

## Example: Converting Bytes to GB

```python
total_gb = usage.total // (1024**3)
used_gb = usage.used // (1024**3)
free_gb = usage.free // (1024**3)
```

This gives readable output:

```
📦 Total: 16 GB
💾 Used: 3 GB
🟩 Free: 12 GB
```

---

## Why This Output Differs From `df -Th`

You may notice small differences when comparing with the Linux command:

```bash
df -Th
```

### Reasons for Difference:

| Factor                | `shutil.disk_usage()`           | `df -Th` (Linux Command)        |
|-----------------------|----------------------------------|---------------------------------|
| Path checked          | Only `/`                         | All mounted filesystems         |
| Reserved space        | Not shown                        | OS may reserve 5% of space      |
| Rounding base         | 1024 (GiB)                       | May use 1000 (GB)               |
| Filesystem overhead   | Not included                     | Included                        |

So if you see:
- Python: 16 GB
- df -Th: 17 GB

 That is normal and expected.

---

##  Bonus: Show Disk Usage as Percent

```python
percent_used = (usage.used / usage.total) * 100
print(f"Disk Usage: {percent_used:.2f}%")
```

---

##  Use Cases

- Monitor server storage before running backups or logs
- Alerting or cleaning up if disk is almost full
- Automatically managing disk quotas in DevOps scripts

---

 **Author:** Poovarasan  
**Learning Day:** Day 19 – `shutil.disk_usage()` and comparison with `df -Th`
