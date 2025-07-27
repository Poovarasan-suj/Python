

###  `python_operators.md` — Python Operators Cheat Sheet

````markdown
# Python Operators Cheat Sheet

Operators are used to perform operations on variables and values.

---

## 1️⃣ Arithmetic Operators

| Operator | Description        | Example       | Output |
|----------|--------------------|---------------|--------|
| `+`      | Addition            | `10 + 5`      | 15     |
| `-`      | Subtraction         | `10 - 5`      | 5      |
| `*`      | Multiplication      | `10 * 5`      | 50     |
| `/`      | Division            | `10 / 5`      | 2.0    |
| `//`     | Floor Division      | `10 // 3`     | 3      |
| `%`      | Modulus (remainder)| `10 % 3`      | 1      |
| `**`     | Exponentiation      | `2 ** 3`      | 8      |

---

## 2️⃣ Comparison Operators

| Operator | Description     | Example         | Output |
|----------|-----------------|-----------------|--------|
| `==`     | Equal to         | `5 == 5`        | True   |
| `!=`     | Not equal to     | `5 != 3`        | True   |
| `>`      | Greater than     | `5 > 2`         | True   |
| `<`      | Less than        | `2 < 5`         | True   |
| `>=`     | Greater or equal | `5 >= 5`        | True   |
| `<=`     | Less or equal    | `3 <= 5`        | True   |

---

## 3️⃣ Logical Operators

| Operator | Description               | Example                  | Output |
|----------|---------------------------|--------------------------|--------|
| `and`    | True if both are true     | `x > 1 and x < 10`       | True   |
| `or`     | True if one is true       | `x > 10 or x == 5`       | True   |
| `not`    | Inverts the result        | `not(x == 5)`            | False  |

---

## 4️⃣ Assignment Operators

| Operator | Example      | Same As        |
|----------|--------------|----------------|
| `=`      | `x = 5`      | Assign         |
| `+=`     | `x += 3`     | `x = x + 3`    |
| `-=`     | `x -= 3`     | `x = x - 3`    |
| `*=`     | `x *= 3`     | `x = x * 3`    |
| `/=`     | `x /= 3`     | `x = x / 3`    |
| `//=`    | `x //= 3`    | `x = x // 3`   |
| `%=`     | `x %= 3`     | `x = x % 3`    |
| `**=`    | `x **= 3`    | `x = x ** 3`   |

---

## 5️⃣ Bitwise Operators

| Operator | Description        | Example    | Result |
|----------|--------------------|------------|--------|
| `&`      | AND                | `5 & 3`    | 1      |
| `|`      | OR                 | `5 | 3`    | 7      |
| `^`      | XOR                | `5 ^ 3`    | 6      |
| `~`      | NOT                | `~5`       | -6     |
| `<<`     | Left shift         | `5 << 1`   | 10     |
| `>>`     | Right shift        | `5 >> 1`   | 2      |

---

## 6️⃣ Membership Operators

| Operator    | Description                     | Example              | Output |
|-------------|---------------------------------|----------------------|--------|
| `in`        | True if value in sequence       | `'a' in 'apple'`     | True   |
| `not in`    | True if value not in sequence   | `'b' not in 'apple'` | True   |

---

## 7️⃣ Identity Operators

| Operator    | Description                      | Example     | Output |
|-------------|----------------------------------|-------------|--------|
| `is`        | True if both refer to same object| `x is y`    | False  |
| `is not`    | True if not same object          | `x is not y`| True   |

---

### ✅ Example Summary
```python
x = 10
y = 5

print(x + y)       # Arithmetic
print(x > y)       # Comparison
print(x == 10 and y < 10)  # Logical
x += 2             # Assignment
print(x)

print("apple" in ["apple", "banana"])  # Membership
print(x is y)       # Identity
````
