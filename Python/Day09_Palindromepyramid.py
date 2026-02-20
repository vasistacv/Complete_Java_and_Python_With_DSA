"""
Day 09: Palindrome Pyramid
Printing numbers in a triangular shape that read the same from both sides.
Logic: Spaces -> Decreasing numbers -> Increasing numbers.
"""

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    # Printing leading spaces for center alignment
    print(" " * (n - i), end="")
    
    # First half: Numbers decreasing from i down to 1
    for j in range(i, 0, -1):
        print(j, end="")
        
    # Second half: Numbers increasing from 2 up to i
    for j in range(2, i + 1):
        print(j, end="")
    
    # Move to the next line after each row
    print()
