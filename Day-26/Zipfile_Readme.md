
# Compressing & Extracting Files Using Python's `zipfile` Module

This guide shows how to **compress** a folder into a `.zip` file and **extract** a `.zip` file using Python’s built-in `zipfile` module.

---

##  Why Use `zipfile`?
The `zipfile` module is part of Python’s standard library, so:
- **No extra installation** is required.
- Works on **Linux, Windows, and macOS**.
- Great for **automation** in DevOps, backups, and cloud uploads.

---

## Folder Structure Example

```

/home/user/Python/logs
├── app.log
├── error.log
└── debug.log

````

---

##  Compress a Folder into a `.zip`

```python
import os
import zipfile

# Folder to compress
folder_path = "/home/user/Python/logs"
# Output zip file
zip_file_path = "/home/user/Python/logs.zip"

with zipfile.ZipFile(zip_file_path, 'w') as zipf:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Add file to zip with relative path
            zipf.write(file_path, os.path.relpath(file_path, folder_path))
            print(f"Added {file_path} to zip.")
print("Zip file created successfully!")
````

---

##  Extract Files from a `.zip`

```python
import zipfile

zip_file_path = "/home/user/Python/logs.zip"
extract_to = "/home/user/Python/logs_extracted"

with zipfile.ZipFile(zip_file_path, 'r') as zipf:
    zipf.extractall(extract_to)
    print(f"Extracted to {extract_to}")
```

---

##  Use Cases

### 1. **Backups**

* Compress log files before archiving.
* Store old backups in a single compressed file.

### 2. **DevOps Automation**

* Zip build artifacts before moving between environments.
* Save space when transferring files between servers.

### 3. **Data Sharing**

* Send large project folders as a single compressed file.
* Reduce file transfer time.

### 4. **Scheduled Jobs**

* Use `cron` or task schedulers to automatically zip logs daily.

---

##  Notes

* `os.walk()` is used to traverse the folder and all subfolders.
* `os.path.relpath()` ensures the zip file keeps **relative paths** instead of full system paths.
* Always **close** the zip file or use the `with` statement.

