"""Read text from the sample file in this folder."""

from pathlib import Path

file_path = Path(__file__).with_name("sample.txt")

if file_path.exists():
    with file_path.open("r", encoding="utf-8") as file:
        contents = file.read()
    print(contents)
else:
    print("sample.txt was not found. Run write-files.py first.")