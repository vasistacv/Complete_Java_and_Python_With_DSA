"""
Day 11: Pascal's Triangle
Printing Pascal's Triangle using list logic.
"""

n = int(input("Enter the number of rows: "))

for i in range(n):
    print(" " * (n - i), end="")
    
    number = 1
    for j in range(i + 1):
        print(number, end=" ")
        number = number * (i - j) // (j + 1)
    print()
