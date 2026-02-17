"""
Day 04: Switch Case Button Selector
Same button problem but using match-case (Python's switch).
Switch is cleaner when you have multiple exact value checks.
"""

button = int(input("Enter the value of button:"))

# Using match-case to handle different button values
match button:
    case 1:
        print("Music")
    case 2:
        print("Video")
    case 3:
        print("Nothing")
    case _:
        print("Invalid Button")
