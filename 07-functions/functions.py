"""Basic examples of defining and calling functions."""


def greet(name):
    """Print a greeting for the given name."""
    print(f"Hello, {name}!")


def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


greet("Alex")
total = add(4, 6)
print("The sum is:", total)