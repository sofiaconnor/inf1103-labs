from product_factory import ProductFactory
from supplier import Supplier

supplier = Supplier("S001", "ABC Supplies", "abc@example.com")

# test PhysicalProduct creation
physical_product = ProductFactory.create(
    "physical", "P001", "Desk Lamp", 25.0, 10,
    supplier, weight=2.5
)

print("Physical Product:", type(physical_product).__name__)

# test DigitalProduct creation
digital_product = ProductFactory.create(
    "digital", "D001", "Photo Editor", 49.90, 100,
    supplier, download_size=250.0
)

print("Digital Product:", type(digital_product).__name__)

# test unknown product type
try:
    ProductFactory.create(
        "service", "S001", "Installation", 30.0, 5,
        supplier
    )

except ValueError as error:
    print("Error:", error)