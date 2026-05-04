"""loopin through dictionaryes"""

inventory = {"apples": 50, "bananas": 30, "orange": 45}

# loop over keys only (default behavior)
for item in inventory:
    print(item) # apples, bananas, oranges

# loop over values only
for quantity in inventory.values():
    print(quantity)  # 50. 30. 45

# loop over both - this is what will use me the most
for item, quantity in inventory.items():
    print(f"{item}: {quantity} units")

# practical: find items low on stock
low_stock = [item for item, qty in inventory.items() if qty < 40]
# bananas