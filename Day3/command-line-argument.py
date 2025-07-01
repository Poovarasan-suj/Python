import sys

def add(num1, num2):
    total = num1 + num2
    return total
def sub(num1, num2):
    diff = num1 - num2
    return diff
def mul(num1, num2):
    output = num1 * num2
    return output

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
    result = add(num1, num2)
    print(result)
if operation == "sub":
    result1 = sub(num1, num2)
    print(result1)
if operation == "mul":
    result2 = mul(num1, num2)
    print(result2)

