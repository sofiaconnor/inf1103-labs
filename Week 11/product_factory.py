from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock: int, supplier: Supplier, weight: float = 0.0,
               download_size: float = 0.0) -> Product:
            # 0.0 is used for both weight and download_size as a default value, where Python automatically uses 0.0 if I don't provide an argument
        
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock, weight, supplier)

        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock, download_size, supplier)

        else:
            raise ValueError(f"Unknown product type: {product_type}")