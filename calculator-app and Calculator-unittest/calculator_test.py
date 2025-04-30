import unittest
from cal import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator(2, 3, "+")
        self.assertEqual(calc.calculate(), 5)
        calc = Calculator(5, 3, "+")
        self.assertEqual(calc.calculate(), 8)

    def test_subtract(self):
        calc = Calculator(2, 3, '-')
        self.assertEqual(calc.calculate(), -1)
        calc = Calculator(5, 3, '-')
        self.assertEqual(calc.calculate(), 2)

    def test_multiply(self):
        calc = Calculator(4, 3, '*')
        self.assertEqual(calc.calculate(), 12)
        calc = Calculator(5, 3, '*')
        self.assertEqual(calc.calculate(), 15)

    def test_divide(self):
        calc = Calculator(6, 3, '/')
        self.assertEqual(calc.calculate(), 2)
        calc = Calculator(9, 3, '/')
        self.assertEqual(calc.calculate(), 3)

    def test_square(self):
        calc = Calculator(2, 3, 'expo')
        self.assertEqual(calc.calculate(), 8)
        calc = Calculator(5, 3, 'expo')
        self.assertEqual(calc.calculate(), 125)

    def test_invalid_operation(self):
        calc = Calculator(2, 3, 'invalid')
        self.assertEqual(calc.calculate(), "Invalid operation, please try again")

    def test_str(self):
        calc = Calculator(2, 3, '+')
        self.assertEqual(str(calc), "2 + 3 = 5")
        calc = Calculator(2, 3, 'expo')
        self.assertEqual(str(calc), "8")

if __name__ == "__main__":
    unittest.main()