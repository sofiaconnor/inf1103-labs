from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

supplier = Supplier("S001", "ABC Supplies", "abc@example.com")

physical = PhysicalProduct("P001", "Laptop", 1200.0, 10, 2.5, supplier)
digital = DigitalProduct("P004", "Software", 49.90, 20, 250.0, supplier)

del supplier

print("Physical Product Supplier:")
physical.display_supplier_information()

print("\nDigital Product Supplier:")
digital.display_supplier_information()