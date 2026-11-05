from product import Product

class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

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
        print("Donwload size:", self.__download_size, "MB")

    def get_fulfilment_info(self):
        return "This digital product is delivered digitally"