from supplier import Supplier
from physical_product import PhysicalProduct
from inventory import Inventory

supplier = Supplier("S001", "ABC Supplies", "abc@example.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.0, 10, 2.5, supplier)

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(laptop)

print("Before Transfer:")
print("Inventory A:")
inventory_a.display_all()

inventory_a.remove_product("P001") # need to pass in the ID for remove_product()

inventory_b.add_product(laptop)

print("After Transfer:")
print("Inventory A:")
inventory_a.display_all()
print("Inventory B:")
inventory_b.display_all()

print("\nSame Product object:", inventory_b.find_product("P001") is laptop) # this verifies that the same
                                                                            # Product object was transferred