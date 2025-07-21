
# Python Try-Except Basics

This document explains Python's `try`, `except`, `else`, and `finally` blocks in simple terms with examples.

---

##  What is try-except in Python?

`try-except` is used to handle errors (called exceptions) so the program doesn’t crash.

### 🔹 Syntax

```python
try:
    # Code that may cause an error
except:
    # Code to handle the error
````

---

## Example 1: Basic Error Handling

```python
try:
    print(x)  # x is not defined
except:
    print("Something went wrong")
```

Output:

```
Something went wrong
```

---

## 🔸 Example 2: Handling Specific Exceptions

```python
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
```

---

## 🔸 Example 3: Using else

```python
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
```

Output:

```
Hello
Nothing went wrong
```

---

## 🔸 Example 4: Using finally

```python
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("This always runs")
```

Output:

```
Something went wrong  
This always runs
```

---

## Real-Life Example: Division

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print("Result is:", result)
    finally:
        print("Finished calculation.")

divide(10, 2)
divide(10, 0)
```

---

##  Summary Table

| Block     | When it Runs                                |
| --------- | ------------------------------------------- |
| `try`     | First. If error happens, jumps to `except`. |
| `except`  | Runs **only** if error occurs in `try`.     |
| `else`    | Runs **only if no error** in `try`.         |
| `finally` | **Always runs** (error or not).             |

---

##  Tip

Use `except` blocks to handle known error types like:

* `ZeroDivisionError`
* `NameError`
* `TypeError`
* `FileNotFoundError`




