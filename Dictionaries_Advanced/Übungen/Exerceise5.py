"""Exercise 5 — defaultdict Grouping
You have a list of (student, subject) tuples. Use defaultdict(list) to build a 
dictionary where each student maps to a list of their subject"""

from collections import defaultdict


enrollments = [
    ("Alice", "Math"), ("Bob", "Science"), ("Alice", "English"),
    ("Carol", "Math"), ("Bob", "Math"), ("Alice", "Science")
]
# Expected: {"Alice": ["Math", "English", "Science"], "Bob": [...], "Carol": [...]}

student_map = defaultdict(list)

for student, subject in enrollments:
    student_map[student].append(subject)

print(dict(student_map))