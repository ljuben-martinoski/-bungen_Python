"""Exercise 4 — Key/Value Checks
Using the scores dictionary from Exercise 3:

Check if "Alice" is in the dictionary (check keys)
Check if 100 is in the scores (check values)
Check if "Zara" is in the dictionary, and if not, print "Student not found"
Print the total number of students"""

scores = {"Alice": 88, "Bob": 72, "Carol": 95, "David": 61, "Eve": 79}

print("Alice" in scores)
print(100 in scores.values())
if "Zara" in scores:
    pass
else:
    print("Student not found")

print(len(scores))