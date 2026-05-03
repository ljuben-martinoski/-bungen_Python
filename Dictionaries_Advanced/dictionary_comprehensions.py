"""
Just like list comprehensions we  can create dictionarys comprehensions in one elegant line."""


# Basic syntax: {key_expr: value_expr for item in iterable}

# regular approach

squares = {}

for n in range(1, 6):
    squares[n] = n ** 2

print(squares)

# comprehension approach - same result, one line
squares = {n: n ** 2 for n in range(1, 6)}

# with a coindition(filter)
even_squares = {n: n ** 2 for n in range(1, 11) if n % 2 == 0}
print(even_squares)

# transforming an exsisting dict(swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)