"""
Docstring for Lists.removing_items
"""


foods = ["pizza", "burger", "salad", "pasta", "Griled steak"]

# with the .remove() method
foods.remove("pizza")
print(foods)

# we can also remove a item from the list with the pop() method

# we use .pop() remove by index(returns the item)
foods.pop()
print(foods)

foods.pop(0) # removes the last item
print(foods)



