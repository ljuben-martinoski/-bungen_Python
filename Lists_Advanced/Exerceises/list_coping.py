"""
Docstring for Lists_Advanced.Exerceises.list_coping
"""

"""# Fix these bugs:
# a) 
original = [1, 2, 3]
copy = original
copy.append(4)
# Why does original also have 4? Fix it!

# b)
matrix = [[1, 2], [3, 4]]
copy_matrix = matrix.copy()
copy_matrix[0][0] = 99
# Why did the original change? Fix it!
# """

original = [1, 2, 3]
copy = original.copy()
copy.append(4)
print(copy)
print(original)

import copy # importing the mopdul copy

matrix = [[1, 2], [3, 4]]
copy_matrix = copy.deepcopy(matrix) # creating the new list copy_matrix withn the deepcopy funktion
copy_matrix[0][0] = 99 
print(matrix)
print(original)

