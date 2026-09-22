def get_valid_input():
    stock_quantity = input("Enter stock quantity or 'quit': ")

    if not stock_quantity.isdigit():
        print("Error: You have entered an invalid input.")
        return None # stops the execution of a function and returns null value

    if stock_quantity == 'quit':
        return 'quit'

    return int(stock_quantity) # converts string input into an integer

inventory = 0
failed_entries = 0 

while True:
    stock_quantity = input("Enter stock quantity or 'quit': ")

    if stock_quantity == 'quit':
        break # exits the While loop and proceeds on to the final print statements

    if not stock_quantity.isdigit():
        print("Error: You have entered an invalid input.")
        failed_entries += 1
        continue

    stock_quantity = int(stock_quantity)

    inventory += stock_quantity
    print("Current inventory:", inventory)

    if inventory > 500:
        print("ALERT! Inventory exceeds limit (500 units)")
        break

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)



