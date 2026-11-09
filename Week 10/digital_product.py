from product import Product
from supplier import Supplier

class DigitalProduct(Product):

    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def display_information(self):
        # Section 1.3: Display product information
        # product = self.to_dict()
        # print("ID:", product["id"])
        # print("Name:", product["name"])
        # print("Price: $" + format(product["price"], ".2f"))
        # print("Current Stock:", product["stock"])
        # print("Download Size:", self.__download_size, "MB")

        # Section 2.1: Method overriding using super()
        super().display_information()
        print("Download size:", self.__download_size, "MB")

    def get_fulfilment_info(self):
        return "This digital product is delivered digitally"

    def to_dict(self):
        product = super().to_dict() # retrieves the existing product details (id, name, price, stock)
        product["type"] = "digital"
        product["download_size"] = self.__download_size
        return product