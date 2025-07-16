import unittest
from sweet import Sweet
from sweet_shop import SweetShop

class TestSweetShop(unittest.TestCase):
    def setUp(self):
        self.shop = SweetShop()
        self.sweet1 = Sweet(1, "Kaju Katli", "Dry Sweet", 80, 10)
        self.sweet2 = Sweet(2, "Gulab Jamun", "Bengali Sweet", 60, 15)
        self.shop.add_sweet(self.sweet1)
        self.shop.add_sweet(self.sweet2)

    def test_add_duplicate(self):
        self.assertFalse(self.shop.add_sweet(self.sweet1))

    def test_search(self):
        res = self.shop.search_by_category("Bengali Sweet")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].name, "Gulab Jamun")

    def test_purchase_error(self):
        with self.assertRaises(ValueError):
            self.shop.purchase(2, 100)
