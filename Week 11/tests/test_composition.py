from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order

supplier = Supplier("S001", "ABC Supplies", "abc@example.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.0, 10, 2.5, supplier)

order_a = Order("O001")
order_b = Order("O002")

order_a.add_order_line(laptop, 1)
order_b.add_order_line(laptop, 2)

print("Order A Total: $", format(order_a.calculate_total(), ".2f"))
print("Order B Total: $", format(order_b.calculate_total(), ".2f"))

print("\nSame Order object:", order_a is order_b)