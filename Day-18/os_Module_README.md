
#  Python `os` Module – Files & Directories (Beginner Guide)

The `os` module in Python allows you to interact with the operating system. It helps with file management, directories, and paths.

---

##  Commonly Used `os` Functions

| Function                     | Description                              |
|------------------------------|------------------------------------------|
| `os.getcwd()`               | Get current working directory            |
| `os.chdir(path)`            | Change current directory                 |
| `os.listdir(path)`          | List all files/folders in a directory    |
| `os.mkdir(path)`            | Create a new directory                   |
| `os.makedirs(path)`         | Create nested directories (parents)      |
| `os.rmdir(path)`            | Remove an empty directory                |
| `os.remove(path)`           | Delete a file                            |
| `os.rename(old, new)`       | Rename file or folder                    |
| `os.path.exists(path)`      | Check if a file/folder exists            |
| `os.path.isfile(path)`      | Check if a path is a file                |
| `os.path.isdir(path)`       | Check if a path is a directory           |

---

## What I Practiced Today

###  1. Print Current Directory
```python
import os
print("Current Directory:", os.getcwd())
```

---

###  2. Create and Delete a Folder
```python
os.mkdir("test_dir")                # Create
os.rmdir("test_dir")               # Remove (must be empty)
```

---

###  3. List Files in Directory
```python
print(os.listdir())               # Lists current directory content
```

---

###  4. Check if File or Folder Exists
```python
if os.path.exists("main.py"):
    print("main.py exists")
```

---

###  5. Check if Path is File or Directory
```python
file = "data.txt"

if os.path.isfile(file):
    print("It's a file")
elif os.path.isdir(file):
    print("It's a directory")
```

---

###  6. Create Folder If Not Exists
```python
if not os.path.exists("logs"):
    os.mkdir("logs")
```

---

###  7. Rename Folder
```python
os.rename("old_name", "new_name")
```

---

### Tips
- Always check `os.path.exists()` before removing or renaming.
- Use `os.makedirs()` to create nested directories.
- Use `os.listdir(path)` to explore specific folders.


📝 **Created by:** Poovarasan  
📅 **Learning Date:** Day 17 – Working with Files & Directories  



