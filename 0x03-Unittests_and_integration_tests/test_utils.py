#!/usr/bin/env python3
""" Parameterize a unit test modeule """

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap Test Class """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected_result):
        """ tests access nested map """
        results = access_nested_map(nested_map, path)
        self.assertEqual(results, expected_result)
