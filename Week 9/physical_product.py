from product import Product

class PhysicalProduct(Product): # Product is the parent, PhysicalProduct is the child

    def __init__(self, product_id, name, price, stock, weight): # weight is our new attribute!
        super().__init__(product_id, name, price, stock) # super() points back to the parent class,
                                                         # need to specify which attributes are needed for the child class
        self.__weight = weight # double underscores stores weight as a private attribute

    def display_information(self):
        super().display_information()
        print("Weight:", self.__weight, "kg") # prints the previously stored value for weight