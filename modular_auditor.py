def get_valid_input():
    stock_quantity = input("Enter stock quantity or 'quit': ")

    if stock_quantity.lower() == 'quit': # .lower() converts 'QUIT', 'Quit', or 'qUit' to 'quit'
        return 'quit'

    if not stock_quantity.isdigit(): # if the stock quantity is NOT a digit, returns None, 
                                     # this also works for negative numbers it check through every character, and the negative sign would make it invalid
        print("Error: You have entered an invalid input.")
        return None # stops the execution of a function and returns null value

    return int(stock_quantity) # converts string input into an integer

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    print("Current inventory:", new_total) # displays new_total after user enters valid stock_quantity
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

def main():
    inventory = 0
    failed_entries = 0 

    while True:
        stock_quantity = get_valid_input()

        if stock_quantity == 'quit':
            break # exits the While loop and proceeds on to the final print statements

        if stock_quantity is None:
            failed_entries += 1
            continue

        inventory = process_delivery(inventory, stock_quantity) # the arguments here will ovbe passed into the parameters (current_total, new_value)

        tax = calculate_tax(stock_quantity)
        print("Tax for this delivery:", tax)  

        if inventory > 500:
            print("ALERT! Inventory exceeds limit (500 units)")
            break

    generate_report(inventory, failed_entries)

if __name__ == "__main__": # launches main() if someone executes this script directly in the terminal
    main()


