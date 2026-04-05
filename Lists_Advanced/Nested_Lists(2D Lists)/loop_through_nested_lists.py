"""
Docstring for Lists_Advanced.Nested_Lists(2D Lists).loop_through_nested_lists
"""

# Looping through nested lists


# Method 1: Nested for loops
matrix = [[1, 2], [3, 4], [5, 6]]
# goes through each element of the list matrix,each element itself is a list
for row in matrix:
    for item in row:# this is the inner loop, loops through [1, 2]
        print(item, end=" ") #end= here replaces the new line with a space,so items printed in a new line with spaces between them
    print()    # new line after each row

# Output: 1 2 3 4 5 6

print("==================================================")

# Method 2: With indices (USING RANGE)
# goes through each element in the matrix list,each element itself is a list
# range(3) produces: 0,1,2 and i will be the row index
for i in range(len(matrix)): # len here gives us 3 because matrix has 3 rows
    for j in range(len(matrix[i])): # len(matrix is the number of items in that row), j will be the column index,matrix[i] is the current row.
        # matrix[i][j]} - Accesses and displays the actual value at that position, [{i}][{j}] - Displays the row index i and column index j in bracket notation
        print(f"[{i}][{j}] = {matrix[i][j]}")

""" Key Differences Between Methods
Method 1:
Gets the actual values directly
Simpler if you only need values 
for row in matrix:
 Can't easily know position
 Can't modify the matrix easily

 
 Method 2:
 Gets indices (positions)
 Useful when you need positions
 (for i in range(len(matrix)):
 Knows exactly where you are [i][j]
 Can modify: matrix[i][j] = new_value    """

