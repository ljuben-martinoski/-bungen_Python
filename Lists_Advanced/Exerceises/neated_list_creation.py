"""
Docstring for Lists_Advanced.Exerceises.neated_list_creation
"""

# Create these using comprehensions:
# a) A 4x4 grid filled with zeros
# b) A 3x3 identity matrix [[1,0,0], [0,1,0], [0,0,1]]
# c) A 5x5 multiplication table
# d) A chess board pattern of "B" and "W" (8x8)


# a) A 4x4 grid filled with zeros
grid_4x4 = [[0 for col in range(4)] for row in range (4)]
print(grid_4x4)

print("========================================================================")

# b) 

iden_matrix = [[1 if row == col else 0 for col in range (3)] for row in range(3)]  
print(iden_matrix) 


# c)
tabele = [[row * col for col in range(1, 6)] for row in range(1, 6)]
print(tabele)

#d)
chess_board = [["B" if (row + col) % 2 == 0 else "W" for col in range (8)] for row in range(8)]
print(chess_board)
