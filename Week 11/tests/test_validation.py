from supplier import Supplier
from physical_product import PhysicalProduct
from order_line import OrderLine

supplier = Supplier("S001", "ABC Supplies", "abc@example.com")

# test invalid product price
try:
    product = PhysicalProduct("P001", "Laptop", -100.0, 10, 2.5, supplier)
except ValueError as error:
    print("Invalid Price:", error)

# test invalid product stock
try:
    product = PhysicalProduct("P002", "Mouse", 25.0, -5, 0.5, supplier)
except ValueError as error:
    print("Invalid Stock:", error)

# create a valid product
product = PhysicalProduct("P003", "Keyboard", 45.0, 10, 1.0, supplier)

# test invalid stock update
try:
    product.update_stock(-5)
except ValueError as error:
    print("Invalid Stock Update:", error)

# test invalid order quantity
try:
    order_line = OrderLine(product, 0)
except ValueError as error:
    print("Invalid Quantity:", error)