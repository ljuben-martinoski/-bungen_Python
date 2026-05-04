"""Exercise 2 — Filtered Comprehension
From the words dict you just created, use a comprehension to build a new dict 
containing only words with 4 or more characters."""

words = ["python", "is", "awesome", "and", "powerful"]
# Expected: {"python": 6, "is": 2, "awesome": 7, "and": 3, "powerful": 8}

word_lenghts = {word: len(word) for word in words}

words_only_4 = {word: len(word) for word in words if len(word) >= 4}
print(words_only_4)

