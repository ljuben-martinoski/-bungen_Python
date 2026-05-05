"""
Assignment: Inventory Management System
Build a program that manages a store's inventory using nested dictionaries. The system should support:
Data Structure — each product should store:

price (float)
quantity (int)
category (string)

Required features:

Display all inventory in a formatted table
Add a new product
Update a product's price or quantity
Remove a product
Search by category (show all products in a given category)
Generate a summary report showing:

Total inventory value (price × quantity summed)
Count of products per category (great use for Counter!)
The most expensive product
Products with quantity below a threshold (low-stock alert)



Start with at least 5 products pre-loaded so you have data to work with immedia"""

from collections import Counter

inventory = {
    "Laptop": {"price": 1200.0, "quantity": 5, "category": "Electronics"},
    "Coffee Maker": {"price": 85.0, "quantity": 12, "category": "Appliances"},
    "Desk Chair": {"price": 150.0, "quantity": 8, "category": "Furniture"},
    "Monitor": {"price": 300.0, "quantity": 2, "category": "Electronics"},
    "Notebook": {"price": 5.0, "quantity": 50, "category": "Stationery"}
}

def display_inventory(inventory):
    print("Inventory: ")
    for product, details in inventory.items():
        print(f"{product}: {details['quantity']} units, Price: ${details['price']}, Category: {details['category']}")

def add_product(inventory):
    product = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    quantity = int(input("Enter the product quantity: "))
    category = input("Enter the product category: ")
    inventory[product] = {"price": price, "quantity": quantity, "category": category}

def update_product(inventory):
    product = input("Enter the product name to update: ")
    if product in inventory:
        price = float(input("Enter the new price: "))
        quantity = int(input("Enter the new quantity: "))  
        inventory[product]["price"] = price
        inventory[product]["quantity"] = quantity
    else:
        print(f"Product '{product}' not found in inventory.")

def remove_product(inventory):
    product = input("Enter the product name to remove: ")
    if product in inventory:
        del inventory[product]
        print(f"Product '{product}' removed from inventory.")
    else:
        print(f"Product '{product}' not found in inventory.")


