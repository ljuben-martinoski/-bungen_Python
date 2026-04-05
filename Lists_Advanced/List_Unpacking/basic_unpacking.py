"""
Docstring for Lists_Advanced.List_Unpacking.basic_unpacking
"""

"""4. List Unpacking
Extract multiple values from a list into separate variable
"""

# Basic unpacking
fruits = ["apple", "banana", "cherry"]
first, second, third = fruits
print(first)
print(second)

# Using * to capture remaining items
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)


# Swapping values(using unpacking)
a, b = 10, 20
a, b = b, a # Swap!
print(a, b) # 20 10

# Unpacking in loops 
pairs = [(1, 2), (3, 4), (5, 6)] # this is a list of tuples 
for x, y in pairs:
    print(f"x={x}, y={y}") # the two values in the f-faktore string,