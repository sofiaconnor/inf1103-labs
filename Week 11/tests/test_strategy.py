from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from supplier import Supplier
from physical_product import PhysicalProduct
from student_discount import StudentDiscount


supplier = Supplier("S001", "ABC Supplies", "abc@example.com")

product = PhysicalProduct("P001", "Desk Lamp", 25.0, 10, 2.5, supplier)

# test BulkDiscount class
order = Order("O001", BulkDiscount(200, 20))
order.add_order_line(product, 10)
print(f"Bulk Discount Total:, ${order.calculate_total():.2f}")

# test PercentageDiscount class
order.set_discount(PercentageDiscount(10))
print(f"Percentage Discount Total:, ${order.calculate_total():.2f}")

# test StudentDiscount class
order.set_discount(StudentDiscount())
print(f"Student Discount Total:, ${order.calculate_total():.2f}")

# test shared PercentageDiscount strategy
shared_discount = PercentageDiscount(10)
order_a = Order("O002", shared_discount)
order_b = Order("O003", shared_discount)
print("Same DiscountStrategy object:", order_a._Order__discount is order_b._Order__discount)