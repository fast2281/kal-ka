import unittest
from main import вычислить  # Импортируем функцию из основного файла (например calculator.py)

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertAlmostEqual(вычислить("2+3"), 5)

    def test_subtraction(self):
        self.assertAlmostEqual(вычислить("10-4"), 6)

    def test_multiplication(self):
        self.assertAlmostEqual(вычислить("3*7"), 21)

    def test_division(self):
        self.assertAlmostEqual(вычислить("20/5"), 4)

    def test_division_by_zero(self):
        self.assertIsNone(вычислить("5/0"))

    def test_power(self):
        self.assertAlmostEqual(вычислить("2^3"), 8)

    def test_parentheses(self):
        self.assertAlmostEqual(вычислить("(2+3)*4"), 20)

    def test_nested_parentheses(self):
        self.assertAlmostEqual(вычислить("((1+2)*(3+4))"), 21)

    def test_float_numbers(self):
        self.assertAlmostEqual(вычислить("1.5+2.3"), 3.8)

    def test_operator_precedence(self):
        self.assertAlmostEqual(вычислить("2+3*4"), 14)

    def test_complex_expression(self):
        self.assertAlmostEqual(вычислить("3+(4*5)-(6/2)^2"), 11)

if __name__ == "__main__":
    unittest.main()
