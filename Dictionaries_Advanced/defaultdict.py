"""defaultdict automaticaly crates a default value for key that dont exisits yet, eliminating a very common source of KeyError crashes."""
from collections import defaultdict

# Regular dict — this CRASHES if "math" not present
scores = {}
scores["math"].append(95) # # KeyError!

# defaultdict(list) — automatically creates [] for new keys
scores = defaultdict(list)
scores["math"].append(95) # works! crates {"math": [95]}
scores["math"].append(87)
scores["english"].append(82)
# defaultdict(<class 'list'>, {'math': [95, 87], 'english': [82]})

# Other useful defaults
word_count = defaultdict(int)  # default value ist 0
word_count["hello"] += 1      # no KeyError


catgory_items = defaultdict(set)  # Default value is set()

