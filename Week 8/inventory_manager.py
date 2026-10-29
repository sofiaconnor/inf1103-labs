import json
from product import Product
from inventory import Inventory

# inventory = [
#     {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15}, # need to rmb to add a comma after each dict item
#     {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
#     {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
# ]

def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            products = json.load(file)

            for product in products:
                new_product = Product(
                    product["id"],
                    product["name"],
                    product["price"],
                    product["stock"]
                )
                inventory.add_product(new_product)

            print("inventory.json found.")
            print("Inventory loaded successfully.\n")

    except FileNotFoundError:
        print("inventory.json not found. Starting with an empty inventory.\n")

    return inventory

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

    product = Product(product_ID, product_name, price, stock_quantity)

    inventory.add_product(product)
    print("\nProduct added successfully!")

def update_stock():
    print("Update Stock")
    product_ID = input("Enter Product ID: ")
    print()

    product = inventory.search_product(product_ID)

    if product is not None:
        print("Product Found:")
        product.display_information()

        new_stock = int(input("New Stock Quantity: "))
        product.update_stock(new_stock)

        print("\nStock updated successfully!")
    else:
        print("Product not found.")

def search_product():
    print("Search Product")
    product_ID = input("Enter Product ID: ")

    product = inventory.search_product(product_ID)

    if product is not None:
        print("\nProduct Found")
        print("--------------------------")
        product.display_information()
        print("--------------------------")
    else:
        print("\nProduct not found.")

def save_inventory():
    products = inventory.get_all_products()

    with open("inventory.json", "w") as file:
        json.dump(products, file)

    print("Inventory saved successfully to inventory.json.")

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
            inventory.display_all()
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