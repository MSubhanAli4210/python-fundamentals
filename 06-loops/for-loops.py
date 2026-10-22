"""Basic examples of for loops."""

for number in range(1, 6):
    print("Number:", number)

colors = ["red", "green", "blue"]
for color in colors:
    print("Color:", color)

# Use enumerate when both the position and value are needed.
for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")