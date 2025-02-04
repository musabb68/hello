import sys

try:
    x = int(input("X: "))
    y = int(input("y: "))
except ValueError:
    print("invalid input")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("cannot be diveded by Zero")
    sys.exit(1)


