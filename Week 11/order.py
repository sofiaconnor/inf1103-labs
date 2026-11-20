from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None: # DiscountStrategy | None means the argument can either
                                                                                         # accept DiscountStrategy or None, = None makes the argument optional
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = [] # initialises an empty list here, hence there's no need to pass in order_lines
        self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def get_order_id(self) -> str:
        return self.__order_id

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def calculate_total(self) -> float:
        total: float = 0.0

        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()

        return self.__discount.apply(total)