"""
Docstring for Lists_Advanced.List_Comprehensions.with_conditions
"""

"""1. List Comprehensions
List comprehensions provide a concise way to create lists. #
They're more readable and often faster than traditional loops."""

# With Conditions (Filtering):

# get only even numbers from 0-19

evens = [x for x in range(20) if x % 2 == 0] # all in one sentence
print(evens)  # print all even number in the range 1-20


# convert to uppercase only if length > 3 +
words = ["hi", "hello", "hey", "goodbye"]
long_words = [word.upper() for word in words if len(word) > 3] # here will convert all the words who are longer that 3 letters in  word with big letters

