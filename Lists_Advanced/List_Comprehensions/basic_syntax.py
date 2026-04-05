"""
Docstring for Lists_Advanced.list_comprehensions
"""

"""
1. List Comprehensions
List comprehensions provide a concise way to create lists. 
They're more readable and often faster than traditional loops."""


# traditional way
square = [] # empty list
# go through all num,ber from 1 to 10 
for x in range(10):
    square.append(x**2) # and with this it will append the result to the empty list all numbers squared

# list comprehension way
squares = [x ** 2 for x in range(10)]  # all in one line. very efficient , consistent 
print(squares)    

