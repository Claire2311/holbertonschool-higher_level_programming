#!/usr/bin/python3
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the function max integer"""
    def test_max_integer(self):
        """all the tests"""
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

        # Test with a list of mixed positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a list containing only one integer
        self.assertEqual(max_integer([5]), 5)

        # Test with a list containing duplicate maximum integers
        self.assertEqual(max_integer([3, 5, 8, 5, 3]), 8)

        # Test with a list containing float numbers
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 4.2, 5.0]), 5.0)

        # Test with an unsorted list
        self.assertEqual(max_integer([3, 1, 4, 2, 5]), 5)
