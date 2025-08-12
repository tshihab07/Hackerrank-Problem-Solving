import math

AB = int(input().strip())
BC = int(input().strip())

# Calculate the angle MBC
angle = math.degrees(math.atan2(AB, BC))

# Round to nearest integer and print in ASCII-friendly form
print(f"{round(angle)}{chr(176)}")
