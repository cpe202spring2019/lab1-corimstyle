import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_eq(self):
        loc1 = Location("yeet", 69, 420)
        loc2 = Location("yeet", 420, 69)
        self.assertNotEqual(loc1, loc2)
        loc3 = Location("yeet", 69, 420)
        loc4 = loc2
        self.assertEqual(loc1, loc3)
        self.assertEqual(loc2, loc4)


if __name__ == "__main__":
    unittest.main()
