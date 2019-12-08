import unittest
from Day_Two.day_two import DayTwo

class Tests(unittest.TestCase):
    
    def test_intcode_add(self):
        day_two = DayTwo();
        input_list = [1,0,0,0,99]
        expected_list = [2,0,0,0,99]

        actual = day_two.run_intcode(input_list)
        self.assertEqual(expected_list, actual)

    def test_intcode_multiply(self):
        day_two = DayTwo();
        input_list = [2,3,0,3,99]
        expected_list = [2,3,0,6,99]

        actual = day_two.run_intcode(input_list)
        self.assertEqual(expected_list, actual)
        
   