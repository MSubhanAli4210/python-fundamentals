"""Basic examples of lambda (small anonymous) functions."""

double = lambda number: number * 2
print("Double 5:", double(5))

numbers = [1, 4, 2, 5, 3]
squared_numbers = list(map(lambda number: number**2, numbers))
print("Squared numbers:", squared_numbers)

words = ["pear", "fig", "banana"]
words_by_length = sorted(words, key=lambda word: len(word))
print("Words sorted by length:", words_by_length)