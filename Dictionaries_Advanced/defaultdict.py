"""defaultdict automaticaly crates a default value for key that dont exisits yet, eliminating a very common source of KeyError crashes."""
from collections import defaultdict
from math import modf

# Regular dict — this CRASHES if "math" not present
scores = {}
scores["math"].append(95)
print(scores)