"""
Day 08: Number Pyramid
Printing a pyramid with numbers where each row contains the row number (1, 2 2, 3 3 3...).
"""

n = int(input("Enter the value of n:"))

for i in range(1, n + 1):
    # Spaces
    for j in range(1, n - i + 1):
        print(" ", end="")
        
    # Numbers (print i repeatedly) followed by space
    for j in range(1, i + 1):
        print(str(i) + " ", end="")
    print()
