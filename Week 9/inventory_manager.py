import json
from product import Product
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# inventory = [
#     {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15}, # need to rmb to add a comma after each dict item
#     {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
#     {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
# ]

def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            products = json.load(file) # json.load() loads the json structure into python

            for product in products:
                if product["type"] == "physical":
                    new_product = PhysicalProduct(
                        product["id"],
                        product["name"],
                        product["price"],
                        product["stock"],
                        product["weight"]
                    )

                elif product["type"] == "digital":
                    new_product = DigitalProduct(
                        product["id"],
                        product["name"],
                        product["price"],
                        product["stock"],
                        product["download_size"]
                    )

                else:
                    continue

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

def add_product():
    print("Add New Product")
    product_ID = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock_quantity = int(input("Stock Quantity: "))


    product = Product(
        product_ID,
        product_name,
        price,
        stock_quantity
    )

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

        new_stock = int(input("\nNew Stock Quantity: "))
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

def display_all():
    inventory.display_all()

def save_inventory():
    products = inventory.get_all_products()

    with open("inventory.json", "w") as file:
        json.dump(products, file, indent = 4) # from Python -> to JSON

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
            print("Product not found: ") 
            # Since it is a loop, there is no need to put "Enter option again: "
            # This is because the loop will shortly print option = input("Enter option: ")


# PhysicalProduct testing
laptop = PhysicalProduct("P001", "Laptop", 1200, 15, 2.5)
laptop.display_information()
print(laptop.get_fulfilment_info()) # Section 3.2: Test physical product fulfilment
print("Shipping Cost: $" + format(laptop.calculate_shipping_cost(), ".2f"))

# DigitalProduct testing
software = DigitalProduct("P004", "Antivirus Software", 49.99, 100, 250)
software.display_information()
print(software.get_fulfilment_info()) # Section 3.2: Test digital product fulfilment

# Section 3.3: Test direct instantiation of the Product class while its abstract method remains unimplemented
# product = Product("P003", "Random Product", 20, 10) # raises a TypeError git add inventory_manager.pybecause Product is abstract

if __name__ == '__main__':
    main()