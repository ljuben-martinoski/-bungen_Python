"""Counter in Action
Given this list of transactions:
Use Counter to find:

How many times each category appears
The top 2 most frequent categories"""


transactions = ["groceries", "rent", "groceries", "entertainment",
                "groceries", "rent", "utilities", "entertainment", "groceries"]
# Expected: {"Alice": ["Math", "English", "Science"], "Bob": [...], "Carol": [...]}

from collections import Counter

categories = [subject for name, subject in transactions]

category_counts = Counter(categories)

two_top = category_counts.most_common(2)

print(f"Category Counts : {dict(category_counts)}")
print(f"Top 2 Categories: {two_top}")


