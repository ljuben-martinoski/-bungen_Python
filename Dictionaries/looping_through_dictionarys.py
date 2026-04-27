"""Looping through dictionarys"""

person = {"name": "obojo", "age": 30, "city": "Skopje"}

# loop through keys (default behavior)
for key in person:
    print(key)

# loop through values
for value in person.values():
    print(value)


# loop through key values
for key in person.items():
    print(f"{key}: {value}")


