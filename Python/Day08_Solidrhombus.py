"""
Day 08: Solid Rhombus
Printing a rhombus shape (slanted rectangle) using stars and spaces.
"""

n = int(input("Enter the value of n:"))

for i in range(1, n + 1):
    # Spaces
    for j in range(1, n - i + 1):
        print(" ", end="")
        
    # Stars
    for j in range(1, n + 1):
        print("*", end="")
    print()
