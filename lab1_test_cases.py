import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([69, 420, 123]), 420)  # testing it finds max
        self.assertNotEqual(max_list_iter([123, 23, 4]), 23)  # testing it doesn't return not max
        self.assertEqual(max_list_iter([123, 2, 123]), 123)  # test for multiple maxes
        self.assertEqual(max_list_iter([]), None)  # test for empty list

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])  # testing it reverses properly
        with self.assertRaises(ValueError):  # check if it raises properly
            reverse_rec(None)
        self.assertEqual(reverse_rec([]), [])  # test for empty list

    def test_bin_search(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)  # check if it searches an entire list



if __name__ == "__main__":
    unittest.main()
