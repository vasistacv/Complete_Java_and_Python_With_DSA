"""
Day 03: Even or Odd Checker

Problem: Check if a given number is even or odd.
The logic: If n % 2 == 0, it's even. Otherwise, it's odd.

Why this matters: Understanding the modulo operator is fundamental.
It shows up everywhere - from array indexing to checking divisibility.
Simple problem but the concept is super important for DSA.

The modulo operator (%) gives you the remainder after division.
Even numbers are perfectly divisible by 2, so remainder is 0.
Odd numbers leave a remainder of 1 when divided by 2.

Algorithm:
1. Read the number from user
2. Use modulo operator (%) to find remainder when divided by 2
3. If remainder is 0, it's even. Otherwise, it's odd.

Time Complexity: O(1) - Just one operation
Space Complexity: O(1) - Only storing one integer
"""

# Get the number we want to check
n = int(input("Enter a number: "))

# The modulo magic: n % 2 gives the remainder when n is divided by 2
# If remainder is 0, the number divides evenly by 2, so it's even
# If remainder is 1, it doesn't divide evenly, so it's odd
if n % 2 == 0:
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")
