import unittest
import sqlite3
from sweet import Sweet
from db_handler import DBHandler

class TestDBHandler(unittest.TestCase):
    def setUp(self):
        self.db = DBHandler(":memory:")
        self.sweet = Sweet(1, "Ladoo", "Dry Sweet", 50.0, 10)
        self.db.insert_sweet(self.sweet)

    def test_insert_duplicate(self):
        self.assertFalse(self.db.insert_sweet(self.sweet))

    def test_delete(self):
        self.assertTrue(self.db.delete_sweet(1))
        self.assertFalse(self.db.delete_sweet(1))

    def test_update_and_get(self):
        self.db.update_sweet(1, price=60)
        sweets = self.db.get_all_sweets()
        self.assertEqual(sweets[0][3], 60)

    def test_purchase(self):
        self.db.purchase(1, 5)
        qty = self.db.get_all_sweets()[0][4]
        self.assertEqual(qty, 5)

    def test_purchase_error(self):
        with self.assertRaises(ValueError):
            self.db.purchase(1, 100)

    def test_restock(self):
        self.db.restock(1, 20)
        qty = self.db.get_all_sweets()[0][4]
        self.assertEqual(qty, 30)
