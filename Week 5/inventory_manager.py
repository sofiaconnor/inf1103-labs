import json

# inventory = [
#     {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15}, # need to rmb to add a comma after each dict item
#     {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
#     {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
# ]

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            products = json.load(file) # json.load() loads the json structure into python
            return products
    except FileNotFoundError:
        return []

inventory = load_inventory()
# print(inventory)

def add_product():
    pass

def update_stock():
    pass

def search_product():
    pass

def display_all():
    pass