import unittest
from src.fizzbuzz import fizzbuzz

class testFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizz = 3
        self.buzz = 5
        self.fizz_buzz = 15
        self.number = 7
        
        
    def test_returns_fizz_for_3(self):
        self.assertEqual("fizz", fizzbuzz(3))
        
    def test_returns_buzz_for_5(self):
        self.assertEqual("buzz", fizzbuzz(5))
        
    def test_returns_fizz_for_15(self):
        self.assertEqual("fizzbuzz", fizzbuzz(15))
        
    def test_returns_7_for_7(self):
        self.assertEqual("7", fizzbuzz(7))
        