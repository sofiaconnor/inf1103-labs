from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped): # Product is the parent, PhysicalProduct is the child
                                              # inherits from one parent class (Product)
                                              # implements the CanBeShipped interface-style ABC

    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier) -> None: # weight is our new attribute!
                                                                                                                         # when a PhysicalProduct is created, it is given a Supplier onject
                                                                                                                         # along with its other details
        super().__init__(product_id, name, price, stock, supplier) # super() points back to the parent class,
                                                                   # need to specify which attributes are needed for the child class
                                                                   # the child then passes the supplier to its parent (Product), which stores it in self.__supplier

        self.__weight: float = weight # double underscores stores weight as a private attribute

    def display_information(self) -> None:
        # Section 1.2: Display product information
        # product = self.to_dict()
        # print("ID:", product["id"])
        # print("Name:", product["name"])
        # print("Price: $" + format(product["price"], ".2f"))
        # print("Current Stock:", product["stock"])
        # print("Weight:", self.__weight, "kg")

        # Section 2.1: Method overriding using super()
        super().display_information()
        print("Weight:", self.__weight, "kg") # prints the previously stored value for weight

    def get_fulfilment_info(self) -> str:
        return "This physical product requires physical shipping" # cannot use return print() because print() displays the message but returns None
                                                         # this way, the method returns the actual string

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 5 # $5 per kg, returns the calculated shipping cost

    def to_dict(self) -> dict:
        product = super().to_dict() # retrieves the existing product details (id, name, price, stock)
        product["type"] = "physical"
        product["weight"] = self.__weight
        return product