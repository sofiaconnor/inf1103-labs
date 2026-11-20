from inventory import Inventory
from supplier import Supplier
from inventory_manager import load_products

inventory = Inventory()
supplier = Supplier("S001", "ABC Supplies", "abc@example.com")

load_products("products.csv", inventory, supplier)