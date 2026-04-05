

#  Shallow vs Deep Copy (for nested lists):

# shallow copy problem with nested lists

original = [[1, 2], [3, 4]]
shallow = original.copy() # using the copy method
shallow[0][0] = 99 # replacing the row and the col 0 with the value 99 
print(original)  # [[99, 2], [3, 4]] - OOPS! Inner list changed!

# Rule of thumb:

# Shallow copy → OK for simple lists like [1, 2, 3]
# Deep copy → Required for nested lists like [[1, 2], [3, 4]] 

# A shallow copy creates a new object, but it does NOT fully copy the nested objects inside it.
# Instead, it copies references to those inner objects.
# - Changing nested data affects both copies.
# - Fast, but not fully independent.

"""
Deep Copy
A deep copy creates a new object and recursively copies everything inside it.
All nested objects are duplicated.
- Changing nested data does NOT affect the original.
- Slower, but fully independent.
"""

# DEEP COPY 
import copy # copy module , Generic (shallow and deep) copying operations.

original = [[1, 2], [3, 4]] # nested list
deep = copy.deepcopy(original) # making a new list with the copyed valuse of the original
deep[0][0] = 99
print(original) #   [[1, 2], [3, 4]] - original unchanged
print(deep)   #   [[99, 2], [3, 4]]

