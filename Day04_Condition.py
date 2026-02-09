"""
Day 04: Button Selector
Simple if-else ladder to handle different button inputs.
Good practice for understanding multiple conditions.
"""

button = int(input("Enter the value of button:"))

# Check which button was pressed and respond accordingly
if button == 1:
    print("Music")
elif button == 2:
    print("Video")
elif button == 3:
    print("Nothing")
else:
    print("Invalid Button")
