import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    
    def test_addition(self):
        self.assertEqual(self.calc.add(10,5),15)
        self.assertEqual(self.calc.add(-10,5),-5)
        self.assertEqual(self.calc.add(-10,-5),-15)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,5),5)
        self.assertEqual(self.calc.subtract(-10,-5),-5)
        self.assertEqual(self.calc.subtract(-10,5),-15)
        self.assertEqual(self.calc.subtract(10,10),0)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10,5),50)
        self.assertEqual(self.calc.multiply(10,-5),-50)
        self.assertEqual(self.calc.multiply(-10,-5),50)
        self.assertEqual(self.calc.multiply(10,2.5),25)
        
    def test_division(self):
        self.assertEqual(self.calc.divide(10,5),2)
        self.assertEqual(self.calc.divide(-10,5),-2)
        self.assertEqual(self.calc.divide(-10,-5),2)
        self.assertEqual(self.calc.divide(5,2),2.5)
        self.assertEqual(self.calc.divide(5,-2),-2.5)
        self.assertIsNone(self.calc.divide(10,0))
        self.assertIsNone(self.calc.divide(0,0))
            
if __name__ == "__main__":
    unittest.main()