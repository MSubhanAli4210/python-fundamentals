"""Basic examples of Python dictionaries."""

student = {
    "name": "Sam",
    "age": 20,
    "is_enrolled": True,
}

print("Student:", student)
print("Name:", student["name"])
print("Age:", student.get("age"))

student["course"] = "Python"
student["age"] = 21
print("Updated student:", student)

print("Dictionary keys:")
for key in student:
    print(key, "=", student[key])