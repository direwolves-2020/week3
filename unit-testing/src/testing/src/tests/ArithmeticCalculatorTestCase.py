import datetime
import unittest
from mymodule.ArithmeticCalculator import ArithmeticCalculator


class ArithmeticCalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = ArithmeticCalculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(10, 20), 30, "10 + 20 should return 30")

    def test_subtract(self):
        result = self.calculator.subtract(20, 10)
        self.assertEqual(result, 10, "20 - 10 should return 10")

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6, "2 * 3 should return 6")

    def test_multiply_with_non_number(self):
        with self.assertRaises(TypeError):
            self.calculator("This", "string")

    @unittest.skipIf(datetime.date.today().day > 26, "Can't run after the 26th")
    def test_divide(self):
        result = self.calculator.divide(10, 4)
        self.assertEqual(result, 2.5, "Should have returned a fractional number")

    @unittest.expectedFailure
    def test_failure(self):
        self.assertEqual(1, 2, "Will fail")
