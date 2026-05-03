"""
CRUD Operations
Start with this dictionary:
pythoncar = {"make": "Toyota", "model": "Corolla", "year": 2020}

Add a "color" key with any value
Update the "year" to 2024
Remove "model" using .pop() and print the removed value
Print the final dictionary"""



car = {"make": "Toyota", "model": "Corolla", "year": 2020}

car["color"] = "blue"

car.update({"year": 2024})

car.pop("model")

print(car)