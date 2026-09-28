def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            orders = file.readlines() # readlines reads all lines at once, and retrieves a list of strings
            return orders

    except FileNotFoundError:
        return []

def save_inventory(orders):
    with open("inventory.txt", "w") as file:
        for order in orders:
            file.write(order.strip() + "\n")

orders = load_inventory()

print("Current Orders:")
print()

for order in orders: # goes through each order one at a time
    print(order.strip()) # .strip() removes whitespace before and after the string

print()

while True:
    product_name = input("Enter Product Name (or type quit): ")

    if product_name.lower() == "quit": # .lower() converts the string to lowercase | loop breaks when user enters "quit"
        break

    quantity = input("Enter Quantity: ")

    if len(orders) == 0: # starts the 1st order at ID 1001 if there are no existing orders
        order_id = 1001
    else:
        last_order = orders[-1] # retrieves the last order from the orders list
        order_parts = last_order.split(",") # splits/cuts the last order into separate parts at specified location,
                                            # in this case, it is split at the commas ","
        order_id = int(order_parts[0]) + 1 # gets the previous order ID, converts it into an integer, and adds 1 to it

    new_order = f"{order_id},{product_name},{quantity}"

    orders.append(new_order)

    print()
    print("New Order Added:")
    print(new_order)
    print()

save_inventory(orders)

print("Order successfully saved to inventory.txt")