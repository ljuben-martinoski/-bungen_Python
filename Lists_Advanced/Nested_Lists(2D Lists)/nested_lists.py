"""
Docstring for Lists_Advanced.Nested_Lists(2D Lists).nested_lists
"""

# Creating a 2D List (3x3 grid)

grid = [
    [1, 2, 3],  #indexing 0
    [4, 5, 6],  # indexing 1
    [7, 8, 9]   # indexing 2
]

# Accessing elements: grid[row][column]
print(grid[0][0])
print(grid[1][2])
print(grid[2][1])

# Modifying elements
grid[1][1] = 99
print(grid[1]) # result 4, 99, 6



