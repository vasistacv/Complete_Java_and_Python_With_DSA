"""
Day 05: Inverted Half Pyramid
Printing a triangle of stars upside down.
"""

n = int(input("Enter the value of n: "))

# Outer loop goes downwards from n to 1
# range(start, stop, step) -> range(n, 0, -1) stops before 0 (at 1)
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
