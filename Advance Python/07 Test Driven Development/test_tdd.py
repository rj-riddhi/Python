import unittest 
from tdd import Calculator 

class TestCalculator(unittest.TestCase): 

    # def test_add(self): 
    #     calc = Calculator() 
    #     result = calc.add(2, 3) 
    #     assert result == 5
    def setUp(self): 
        self.calc = Calculator()  # Initialize Calculator once for all tests 

    def test_add(self): 
        self.assertEqual(self.calc.add(2, 3), 5) 

    def test_subtract(self): 
        self.assertEqual(self.calc.subtract(5, 3), 2) 

    def test_multiply(self): 
        self.assertEqual(self.calc.multiply(2, 3), 6) 

    def test_divide(self): 

        self.assertEqual(self.calc.divide(6, 3), 2) 
        with self.assertRaises(ZeroDivisionError):  # Test division by zero 
            self.calc.divide(6, 0)