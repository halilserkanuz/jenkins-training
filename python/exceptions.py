try:
    print(10/0)
except ZeroDivisionError:
    print("You can't divide by zero")

try:
    raise ValueError("This is a value error")
except Exception as e:
    print(e)