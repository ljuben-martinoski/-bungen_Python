"""
Docstring for Lists_Advanced.Advanced_ListOperations.fllatening_nestedList
"""


nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist] # taking the item from the sublist,that is in the nested list to create the flated list
print(flat)  # [1, 2, 3, 4, 5, 6]
