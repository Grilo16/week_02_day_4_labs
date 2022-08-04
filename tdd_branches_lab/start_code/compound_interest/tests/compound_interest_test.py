import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):
    
    # Tests
    
    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_return732_81(self):
        investment = CompoundInterest(100, 10, 20)
        self.assertEqual(732.81, investment.investment_return())

    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_return181_94(self):
        investment = CompoundInterest(100, 6, 10)
        self.assertEqual(181.94, investment.investment_return())

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_return140058_55(self):
        investment = CompoundInterest(100000, 5, 8)
        self.assertEqual(149058.55, investment.investment_return())

    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_0(self):
        investment = CompoundInterest(0, 10, 1)
        self.assertEqual(0, investment.investment_return())

    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_100(self):
        investment = CompoundInterest(100, 0, 10)
        self.assertEqual(100, investment.investment_return())

    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month
    def test_118380_16(self):
        investment = CompoundInterest(100, 5, 8)
        self.assertEqual(118380.16, investment.investment_return_w_monthly_contributions(1000))

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month
    def test_156093_99(self):
        investment = CompoundInterest(100, 5, 10)
        self.assertEqual(156093.99, investment.investment_return_w_monthly_contributions(1000))

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month
    def test_475442_59(self):
        investment = CompoundInterest(116028.86, 7.5, 8)
        self.assertEqual(475442.59, investment.investment_return_w_monthly_contributions(2006))

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month
    def test_718335_96(self):
        investment = CompoundInterest(116028.86, 9, 12)
        self.assertEqual(718335.96, investment.investment_return_w_monthly_contributions(1456))

