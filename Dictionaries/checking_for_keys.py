"""Checking for keys"""


person = {"name": "obojo", "age": 30, "city": "Skopje"}

# use 'in' - checks keys by default

print("name" in person)
print("email" in person)
print("obojo" in person)


# check values
print("obojo" in person.values())  # True
