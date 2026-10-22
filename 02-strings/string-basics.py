"""Basic string creation, formatting, and methods."""

first_name = "Ada"
language = "Python"

greeting = f"Hello, {first_name}!"
print(greeting)
print("Language:", language)
print("Uppercase:", language.upper())
print("Lowercase:", language.lower())
print("Number of characters:", len(language))
print("First character:", language[0])
print("First three characters:", language[:3])

message = "  Python is fun!  "
print("Without extra spaces:", message.strip())
print("Replace a word:", message.replace("fun", "useful"))