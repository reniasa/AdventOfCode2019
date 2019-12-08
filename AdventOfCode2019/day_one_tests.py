import unittest
from day_one import DayOne

class Tests(unittest.TestCase):
    
    def test_fuel_calculate(self):
        day_one = DayOne();
        expected = 654
        actual = day_one.calculateAllFuel([1969])
        self.assertEqual(expected, actual)