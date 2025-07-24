
#  Python `shutil` Module – File and Folder Operations (Practice Summary)

This document summarizes practice tasks and concepts for Python's `shutil` module. It focuses on copying, moving, and deleting files and directories – essential for DevOps, automation, and cloud engineering workflows.

---

## What is `shutil`?

The `shutil` module provides high-level file operations:
- Copy files or entire directories
- Move files/folders
- Delete non-empty folders
- Preserve file metadata
- Check disk space usage

---

##  Practice Tasks Completed

### Task 1: Copy a File Using `copy2()`

```python
shutil.copy2("Day-19/shutil-copy.py", "Day-20/archive/")
```
✅ Preserves metadata like timestamps while copying.

---

###  Task 2: Move a File to Another Folder

```python
shutil.move("logs/report.log", "archive/report.log")
```
Moves the file and updates the location.

---

###  Task 3: Copy a File with Metadata (Same as Task 1)

```python
shutil.copy2("Day-19/script.py", "Day-20/script_backup.py")
```

---

###  Task 4: Rename a File (Move with New Name)

```python
shutil.move("notes.txt", "notes_backup.txt")
```
`move()` can be used to rename a file.

---

###  Task 5: Copy an Entire Directory Using `copytree()`

```python
shutil.copytree("Day-19/projects/", "Day-20/projects-backup")
```
✅ Recursively copies folder and all contents.
⚠️ Destination must not already exist.

---

###  Task 6: Delete a Non-Empty Folder

```python
if os.path.exists("project_backup"):
    shutil.rmtree("project_backup")
```
✅ Deletes the entire folder and everything inside it.

---

## Tips

- Use `shutil.copy2()` when you need to preserve metadata.
- `copytree()` requires the destination folder not to exist.
- `shutil.rmtree()` is powerful — use with caution!
- Combine with `os.path.exists()` for safety checks.

---

📝 **Created by:** Poovarasan  
📅 **Learning Date:** Day 17-18 – Working with `shutil`  
