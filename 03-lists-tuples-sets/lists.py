"""Basic examples of lists, tuples, and sets."""

# Lists are ordered and can be changed.
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
fruits[0] = "pear"
print("List:", fruits)
print("First fruit:", fruits[0])
print("Number of fruits:", len(fruits))

# Tuples are ordered and cannot be changed after creation.
coordinates = (10, 20)
print("Tuple:", coordinates)
print("X coordinate:", coordinates[0])

# Sets contain unique values.
unique_numbers = {1, 2, 2, 3}
unique_numbers.add(4)
print("Set:", unique_numbers)
print("Is 2 in the set?", 2 in unique_numbers)