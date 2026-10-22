"""Basic examples of handling common exceptions."""

text_number = "42"

try:
    number = int(text_number)
    result = 100 / number
except ValueError:
    print("The text must contain a valid whole number.")
except ZeroDivisionError:
    print("A number cannot be divided by zero.")
else:
    print("The result is:", result)
finally:
    print("This block always runs.")