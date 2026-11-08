from abc import ABC, abstractmethod
# abstractmethod is a decorator in Python that allows us to specify which methods the child classes MUST implement

class Product(ABC):

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print("Price: $" + format(self.__price, ".2f"))
        print("Current Stock:", self.__stock)

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    @abstractmethod # the @ tells Python to apply the abstractmethod decorator here
    def get_fulfilment_info(self):
        pass