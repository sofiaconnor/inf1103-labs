from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
from inventory import Inventory

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

supplier = Supplier("S001", "ABC Supplies", "abc@example.com")

laptop = PhysicalProduct("P001", "Laptop", 1200.0, 10, 2.5, supplier)
software = DigitalProduct("P004", "Antivirus Software", 49.99, 100, 250, supplier)

print("Physical Product:")
show_product_details(laptop)

print("\nDigital Product:")
show_product_details(software)

print("\nTesting Inventory:")

inventory = Inventory()

inventory.add_product(laptop)
inventory.add_product(software)

inventory.display_all()