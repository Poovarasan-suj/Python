
## **Disk & CPU Monitoring — Modular Python Script**

### **📌 Overview**

This project monitors **disk usage** and **CPU usage** by creating a **separate Python utility module** (`sys_utils.py`) and importing it into another script.
It follows the **modular programming** approach, which is common in **DevOps automation**.

---

### **🛠 Why This is Useful in DevOps**

* **Code reusability** — once created, you can import these functions into any script.
* **Modular design** — keeps monitoring logic separate from other automation code.
* **Easy integration** — can be used inside alerting, logging, or cloud automation scripts.

---

### **Project Structure**

```
Day-28/
│
├── sys_utils.py        # Contains reusable functions for disk & CPU usage
└── Cpu_Disk_Usage.py   # Main script importing and using the functions
```

---

### ** sys\_utils.py**

```python
import shutil
import psutil

def get_disk_usage():
    usage = shutil.disk_usage("/")
    total_gb = usage.total / (1024 ** 3)
    used_gb = usage.used / (1024 ** 3)
    print(f"Disk is currently used {used_gb:.2f} GB out of {total_gb:.2f} GB")

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Cpu Usage: {cpu_percent} %")

if __name__ == "__main__":
    # This runs ONLY if you execute sys_utils.py directly
    get_disk_usage()
    get_cpu_usage()
```

---

### ** Cpu\_Disk\_Usage.py**

```python
from sys_utils import get_disk_usage, get_cpu_usage

print(get_disk_usage())
print(get_cpu_usage())
```

---

### ** Code Explanation**

1. **`get_disk_usage()`**

   * Uses `shutil.disk_usage("/")` to get total, used, and free space.
   * Converts from **bytes** to **GB**.
   * Prints the current disk usage.

2. **`get_cpu_usage()`**

   * Uses `psutil.cpu_percent(interval=1)` to measure CPU usage over 1 second.
   * Prints the CPU usage percentage.

3. **`if __name__ == "__main__":`**

   * This special check means:

     * If you **run sys\_utils.py directly**, it will print the usage stats.
     * If you **import sys\_utils.py** into another script, these print statements won’t run automatically — only the functions will be available to call.

4. **`Cpu_Disk_Usage.py`**

   * Imports the functions from `sys_utils.py`.
   * Calls them to display results.

---

### **🚀 How to Run**

**Option 1 — Run utility script directly**

```bash
python sys_utils.py
```

This will show **disk** and **CPU usage** immediately.

**Option 2 — Import into another script**

```bash
python Cpu_Disk_Usage.py
```

This will run the imported functions.

---

### ** Real-Time DevOps Use Cases**

* **Server health checks** in automation scripts.
* Reusing the module across multiple monitoring scripts.

