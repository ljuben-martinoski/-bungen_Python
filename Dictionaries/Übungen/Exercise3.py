"""
 Looping Practice
Given this dictionary:
pythonscores = {"Alice": 88, "Bob": 72, "Carol": 95, "David": 61, "Eve": 79}
Write a loop that prints each student and their grade, AND marks them as "Pass" or "Fail" (passing score is 70+). Format it like:
Alice: 88 — Pass
Bob: 72 — Pass
David: 61 — Fail"""

scores = {"Alice": 88, "Bob": 72, "Carol": 95, "David": 61, "Eve": 79}  

# Corrected version
for key, value in scores.items():
    status = "Pass" if value >= 70 else "Fail"
    print(f"{key}: {value} — {status}")
