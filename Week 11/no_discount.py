from discount_strategy import DiscountStrategy


class NoDiscount(DiscountStrategy):
    # does not require a constructor (__init__) because it simply returns the original total

    def apply(self, total: float) -> float:
        return total