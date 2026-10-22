"""Write a short text file in this folder."""

from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")
text = "Hello from Python!\nThis file was created by write-files.py.\n"

with file_path.open("w", encoding="utf-8") as file:
    file.write(text)

print(f"Wrote text to {file_path.name}.")