"""
counter is a spezialized dictionary that counts occurrences.It saves you from writting counting logic yourself."""

from collections import Counter

# count characters in a string
text = "mississipi"
letters_counts = Counter(text)
# Counter({'s': 4, 'i': 4, 'p': 2, 'm': 1})

votes = ["Alice", "Bob", "Alice", "Carol", "Alice", "Bob"]
tally = Counter(votes)
# Counter({'Alice': 3, 'Bob': 2, 'Carol': 1})

# Most common items
print(tally.most_common(2))   # [('Alice', 3), ('Bob', 2)]

# It behaves like a regular dict
print(tally["Alice"])         # 3
print(tally["Dave"])          # 0  (no KeyError — returns 0 for missing keys!)





