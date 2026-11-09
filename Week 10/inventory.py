from product import Product

class Inventory:

    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product) # removes the Product from Inventory without deleting the Product object itself
                return
        
    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def find_product(self, product_id: str) -> Product | None:
        return self.search_product(product_id)

    def display_all(self) -> None:
        print("Current Inventory")
        print("--------------------------")

        for product in self.__products:
            product.display_information()
            print("--------------------------")

    def get_all_products(self) -> list[dict]: # list[dict] because this method returns a list containing dictionaries
        products = []

        for product in self.__products:
            products.append(product.to_dict())

        return products