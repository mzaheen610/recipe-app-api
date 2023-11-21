from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):

    def test_add(self):
        res = calc.add(10,50)
        self.assertEqual(res, 60)
    
    def test_subtract_numbers(self):
        """ Test subtracting numbers"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, -5)

