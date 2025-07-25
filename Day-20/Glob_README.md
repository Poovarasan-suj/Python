# 🌐 Python `glob` Module – Pattern Matching for Files

##  What is `glob`?

The `glob` module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell.

> Example: You want to get all `.txt` or `.log` files from a folder.

---

## 🧠 Basic Usage

```python
import glob

# Get all .txt files in a folder
files = glob.glob("/home/sujith/Python/logs/*.txt")

for file in files:
    print("Found:", file)


 Author: Poovarasan
 Learning Day: Day 20 – Working with glob for file searching and filtering