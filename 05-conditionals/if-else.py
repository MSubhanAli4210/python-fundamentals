"""Basic examples of conditional statements."""

temperature = 22

if temperature > 30:
    print("It is hot outside.")
elif temperature >= 20:
    print("The weather is comfortable.")
else:
    print("It is cold outside.")

number = 7
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")