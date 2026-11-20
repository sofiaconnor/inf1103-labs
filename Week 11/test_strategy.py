from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from supplier import Supplier
from physical_product import PhysicalProduct


supplier = Supplier("S001", "ABC Supplies", "abc@example.com")

product = PhysicalProduct(
    "P001", "Desk Lamp", 25.0, 10, 2.5, supplier
)

order = Order("O001", BulkDiscount(200, 20))
order.add_order_line(product, 10)

print("Bulk Discount Total:", order.calculate_total())

order.set_discount(PercentageDiscount(10))

print("Percentage Discount Total:", order.calculate_total())