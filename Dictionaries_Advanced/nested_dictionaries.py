"""a dictionary values can be anything- including other dictionaries. This lets you model structured, real- world data."""

students = {
    "alice": {
        "age": 20,
        "grades": [88, 92, 79],
        "major": "Computer Science"
    },
    "bob": {
        "age": 22,
        "grades": [75, 81, 90],
        "major": "Mathematics"
    }
}

# accessing nested values - chain the keys
print(students["alice"]["major"]) # [alice] acc.the inner dictionary, [major]- geting and accesin a value of the key = major
print(students["bob"]["grades"][1])# [bob] acc. the dict.for bob, then the key = grades ,and then the grade that has index 1 in the same list


# Modifying nested data
students["alice"]["grades"].append(95)

# adding a new nested entry
students["carol"] = {
    "age": 21,
    "grades": [91, 87, 93],
    "major": "Physics"
}

# safe access with .get() - works on nested dicts too

print(students)