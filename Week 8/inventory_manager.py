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
            print("inventory.json found.")
            print("Inventory loaded successfully.\n")
            return products
    except FileNotFoundError:
        return []

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")

inventory = load_inventory()
# print(inventory)

def add_product():
    print("Add New Product")
    product_ID = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock_quantity = int(input("Stock Quantity: "))

    product = {
        "id": product_ID,
        "name": product_name,
        "price": price,
        "stock": stock_quantity
    }

    inventory.append(product)
    print("\nProduct added successfully!")

# add_product()
# print(inventory)

def update_stock():
    print("Update Stock")
    product_ID = input("Enter Product ID: ")
    print()

    for product in inventory:
        if product["id"] == product_ID:
            print("Product Found:")
            print("Name:", product["name"] )
            print("Current Stock:", product["stock"])
            
            new_stock = int(input("New Stock Quantity: "))
            product["stock"] = new_stock
            print("\nStock updated successfully!")
            break
    else:
        print("Product not found.")

# update_stock()

def search_product():
    print("Search Product")
    product_ID = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_ID:
            print("\nProduct Found")
            print("--------------------------")
            print("ID: ", product["id"] )
            print("Name: ", product["name"])
            print("Price: $" + format(product["price"], ".2f"))
            print("Stock: ", product["stock"])
            print("--------------------------")
            break
    else:
        print("\nProduct not found.")

def display_all():
    print("Current Inventory")
    print("--------------------------")

    for product in inventory:
        print("ID:",product["id"],
              "| Name:",product["name"],
              "| Price: $" + format(product["price"], ".2f"),
              "| Stock:",product["stock"])

    print("--------------------------")

# display_all()

def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file) # from Python -> to JSON

    print("Inventory saved successfully to inventory.json.")

# update_stock()

# print("Saving Inventory...")
# save_inventory()

def main():
    print("-----------MENU-----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------")

    while True:
        option = input("\nEnter option: ")
        print()

        if option == "1":
            display_all()
        elif option == "2":
            add_product()
        elif option == "3":
            update_stock()
        elif option == "4":
            search_product()
        elif option == "5":
            print("Saving inventory...")
            save_inventory()
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory()
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please try again: ") # since it is a loop, there is no need to put "Enter option again: "
                                                        # because the loop will shortly print option = input("Enter option: ")

if __name__ == '__main__':
    main()