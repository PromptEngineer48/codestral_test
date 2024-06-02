# app4.py
def summer(a, b):
    return a + b

# test_app4.py
import unittest
from app4 import summer

class TestSummerFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(summer(5, 3), 8)

    def test_negative_numbers(self):
        self.assertEqual(summer(-5, -3), -8)

    def test_mixed_numbers(self):
        self.assertEqual(summer(5, -3), 2)

    def test_zero_numbers(self):
        self.assertEqual(summer(0, 0), 0)

    def test_large_numbers(self):
        self.assertEqual(summer(1000000, 2000000), 3000000)

# Run the tests
if __name__ == '__main__':
    unittest.main()
