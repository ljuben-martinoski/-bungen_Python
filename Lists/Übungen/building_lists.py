"""
Docstring for Lists.Übungen.building_lists
"""


# Create 3 separate lists:
#   - fruits (3 items)
#   - vegetables (3 items)  
#   - proteins (3 items)
# Combine them into one shopping list
# Print the total number of items
# Print each item with its position (1. apple, 2. banana, etc.)


def shoping_list():

    fruits = ["orange", "banana", "appel"]
    vegetables = ["cucamber", "tomaten", "Brokoli"]
    proteins = ["Chicken", "eggs", "Milk"]

    shoping_list = []
    shoping_list = fruits + vegetables + proteins
    for i in range(len(shoping_list)):#
        print()
    print(f"In the todays shoping list we have : {len(shoping_list)} number of items")
    print()

shoping_list()    









