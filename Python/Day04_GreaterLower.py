"""
Day 04: Compare Two Numbers
Basic comparison to check which number is greater or if they're equal.
"""

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))

if a == b:
    print("Both are equal")
elif a > b:
    print("a is greater than b")
else:
    print("b is greater than a")
