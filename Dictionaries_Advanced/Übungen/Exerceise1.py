"""Exercise 1 — Comprehension Basics
Using a dict comprehension, create a dictionary mapping each word in this list to its length:
words = ["python", "is", "awesome", "and", "powerful"]
# Expected: {"python": 6, "is": 2, "awesome": 7, "and": 3, "powerful": 8}"""

words = ["python", "is", "awesome", "and", "powerful"]
# Expected: {"python": 6, "is": 2, "awesome": 7, "and": 3, "powerful": 8}

word_lenghts = {word: len(word) for word in words}



