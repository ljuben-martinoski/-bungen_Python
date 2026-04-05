"""
Docstring for Lists_Advanced.List_copyingVSReferencing.CRUCIAL_TO_UNDERSTAND_TO AVOIDbugs
"""

# WRONG: This creates a reference, not a copy
list1 = [1, 2, 3]
list2 = list1  # list2 points to the SAME list as list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - OOPS! list1 changed too!


# RIGHT: Create a shallow copy
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1) # list unchanged - [1, 2, 3]
print(list2) # new list with appended number 4


######THEREE ways to copy a list:
# copy1 = original.copy()  # with the copy method
# copy2 = original[:]  # with the slice notation meanning from the begfinign to the end
# copy3 = list(original) # and with the list funktion 


