# This function calculates the nth Fibonacci number
# It takes an integer n as input
# If n is less than or equal to 0, it returns "Invalid input"
# If n is 1, it returns 0
# If n is 2, it returns 1
# For n greater than 2, it calculates the Fibonacci number using a loop
# and returns the result
def gasoline(n: int):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Unit tests for the gasoline function
import unittest

class TestGasoline(unittest.TestCase):

    def test_invalid_input(self):
        self.assertEqual(gasoline(0), "Invalid input")
        self.assertEqual(gasoline(-5), "Invalid input")

    def test_first_fibonacci_number(self):
        self.assertEqual(gasoline(1), 0)

    def test_second_fibonacci_number(self):
        self.assertEqual(gasoline(2), 1)

    def test_third_fibonacci_number(self):
        self.assertEqual(gasoline(3), 1)

    def test_fifth_fibonacci_number(self):
        self.assertEqual(gasoline(5), 3)

    def test_tenth_fibonacci_number(self):
        self.assertEqual(gasoline(10), 34)

    def test_large_input(self):
        self.assertEqual(gasoline(30), 832040)

if __name__ == '__main__':
    unittest.main()
