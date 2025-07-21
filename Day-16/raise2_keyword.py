x = "hello"

if not type(x) is int:
    raise TypeError("x must be an integer")
else:
    print("x is an integer")