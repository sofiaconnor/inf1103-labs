import unittest

from supplier import Supplier
from inventory import Inventory
from product_factory import ProductFactory
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount
from inventory_manager import load_products


class TestWeek11(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "ABC Supplies", "abc@example.com"
        )
        self.product = ProductFactory.create(
            "physical", "P001", "Desk Lamp",
            25.0, 10, self.supplier
        )

    def test_strategy(self):
        order = Order("O001", BulkDiscount(200, 20))
        order.add_order_line(self.product, 10)

        self.assertEqual(order.calculate_total(), 230.0)

        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225.0)

        order.set_discount(StudentDiscount())
        self.assertEqual(order.calculate_total(), 237.5)

    def test_factory(self):
        self.assertEqual(
            type(self.product).__name__, "PhysicalProduct"
        )

        with self.assertRaises(ValueError):
            ProductFactory.create(
                "service", "S001", "Installation",
                30.0, 5, self.supplier
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical", "P002", "Invalid",
                -10.0, 5, self.supplier
            )

        with self.assertRaises(ValueError):
            self.product.update_stock(-5)

        order = Order("O002")

        with self.assertRaises(ValueError):
            order.add_order_line(self.product, 0)

    def test_csv_loading(self):
        inventory = Inventory()
        load_products("products.csv", inventory, self.supplier)

        self.assertIsNotNone(inventory.search_product("P001"))
        self.assertIsNotNone(inventory.search_product("D001"))
        self.assertIsNotNone(inventory.search_product("P003"))
        self.assertIsNone(inventory.search_product("P002"))

    def test_missing_file(self):
        inventory = Inventory()
        load_products("missing_products.csv", inventory, self.supplier)

        self.assertIsNone(inventory.search_product("P001"))


if __name__ == "__main__":
    unittest.main()