"""
Day 02: Fibonacci Series

Problem: Print the Fibonacci series up to n terms.
The Fibonacci series is: 0, 1, 1, 2, 3, 5, 8, 13, 21...
Each number is the sum of the previous two numbers.

Why this matters: Fibonacci is everywhere in coding interviews.
Plus, it teaches you about loops and how numbers build on each other.
Google interviewers love asking variations of this.

Approach: Classic iterative method - no recursion headaches here.

Algorithm:
1. Start with first two numbers: 0 and 1
2. For each next number, add the previous two
3. Keep going until we hit n terms

Time Complexity: O(n) - One loop through n terms
Space Complexity: O(1) - Only storing three variables
"""

# Setting up to grab user input
# How many Fibonacci numbers do you want? Let's find out.
n = int(input("Enter the number of terms: "))

# The first two numbers in Fibonacci are always 0 and 1
# Think of them as the "seed" numbers that start everything
first = 0
second = 1

print("Fibonacci Series:")

# Generate and print the Fibonacci sequence
for i in range(1, n + 1):
    # Print the current term
    print(first, end=" ")
    
    # Here's the magic: calculate the next Fibonacci number
    # It's just the sum of the previous two numbers
    next_num = first + second
    
    # Shift the numbers: second becomes first, next becomes second
    # It's like moving down a conveyor belt
    first = second
    second = next_num
