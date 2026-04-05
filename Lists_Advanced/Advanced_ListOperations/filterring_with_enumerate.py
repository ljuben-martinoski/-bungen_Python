"""
Docstring for Lists_Advanced.Advanced_ListOperations.filterring_with_enumerate
"""


# Filtering with enumerate
fruits = ["apple", "banana", "cherry", "date"]
long_fruits = [(i, fruit) for i, fruit in enumerate(fruits) if len(fruit) > 5] # in basicaly teling if there is a word with more than 5 letter to take it out and place it in the new list.
print(long_fruits)  # [(1, 'banana'), (2, 'cherry')]