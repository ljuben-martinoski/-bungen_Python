"""
Docstring for Lists_Advanced.Advanced_ListOperations.listOlist_toColumns
"""

# List of lists to columns
matrix = [[1, 2, 3], [4, 5, 6]]  # nested List
column_0 = [row[0] for row in matrix] # creating only on column of the existing list matrix
print(column_0)   # [1, 4]


