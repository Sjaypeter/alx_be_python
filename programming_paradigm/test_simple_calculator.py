import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    
    def test_addition(self):
        self.assertEqual(SimpleCalculator.add(10,5),5)
        self.assertEqual(SimpleCalculator.add(-10,5),-5)
        self.assertEqual(SimpleCalculator.add(-10,-5),-15)
        
    def test_subtraction(self):
        self.assertEqual(SimpleCalculator.subtract(10,5),5)
        self.assertEqual(SimpleCalculator.subtract(-10,-5),-15)
        self.assertEqual(SimpleCalculator.subtract(-10,5),-5)
        self.assertEqual(SimpleCalculator.subtract(10,10),0)
    
    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(10,5),50)
        self.assertEqual(SimpleCalculator.multiply(10,-5),-50)
        self.assertEqual(SimpleCalculator.multiply(-10,-5),50)
        self.assertEqual(SimpleCalculator.multiply(10,2.5),25)
        
    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(10,5),2)
        self.assertEqual(SimpleCalculator.divide(-10,5),-2)
        self.assertEqual(SimpleCalculator.divide(-10,-5),2)
        self.assertEqual(SimpleCalculator.divide(5,2),2.5)
        self.assertEqual(SimpleCalculator.divide(5,-2),-2.5)
        with self.assertRaises(ValueError):
            SimpleCalculator.divide(10,0)
            
    