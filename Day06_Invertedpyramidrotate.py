"""
Day 06: Inverted Half Pyramid (Rotated 180 deg)
Printing a triangle of stars aligned to the right.
"""

n = int(input("Enter the value of n:"))

for i in range(1, n + 1):
    # Print spaces
    for j in range(1, n - i + 1):
        print(" ", end="")
    # Print stars
    for j in range(1, i + 1):
        print("*", end="")
    print()
