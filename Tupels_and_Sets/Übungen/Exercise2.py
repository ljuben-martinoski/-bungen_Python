"""
Exercise 2 — Tuple Unpacking
You're given this tuple representing a product:"""

product = ("Laptop", 999.99, 15)  # (name, price, quantity)

"""
Unpack it into three variables name, price, quantity. Then print:
Product: Laptop
Price: €999.99
In Stock: 15 units"""

x, y, z = product

print("Product: ", x)
print("Price: ", y)
print("In Stock: ", z, " units")



