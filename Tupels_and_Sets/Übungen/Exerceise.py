"""Exercise 4 — Set Basics and Deduplication
You have a list of student submissions (some submitted twice):
pythonsubmissions = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Diana", "Alice"]
Convert it to a set to find the unique submitters. Print:

How many unique students submitted
The unique names
"""

submissions = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Diana", "Alice"]

unique_submitters = set(submissions)


print(f"How many unique students submitted: {len(unique_submitters)}")
print(f"The unique names: {unique_submitters}")
