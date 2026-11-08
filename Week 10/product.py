from abc import ABC, abstractmethod
# abstractmethod is a decorator in Python that allows us to specify which methods the child classes MUST implement

from supplier import Supplier # always organise imports in the following order:
                              # 1. Standard Library Imports - Built-in Python modules such as abc, json
                              # 2. Third-party imports - External libraries installed separately
                              # 3. Local application impots - My own Python files, such as supplier.py

class Product(ABC):

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier # this stores a reference to an existing Supplier object (association),
                                             # instead of creating a new one

    def get_product_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print("Price: $" + format(self.__price, ".2f"))
        print("Current Stock:", self.__stock)

    def display_supplier_information(self) -> None:
        self.__supplier.display_information()

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