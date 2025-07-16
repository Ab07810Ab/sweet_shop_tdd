import unittest
from sweet import Sweet

class TestSweet(unittest.TestCase):
    def test_repr(self):
        s = Sweet(1, "Ladoo", "Dry Sweet", 50, 20)
        self.assertIn("Ladoo", str(s))
