#!/usr/bin/env python3
""" Parameterize a unit test modeule """

import unittest
import unittest.mock
from utils import access_nested_map, get_json
import requests
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap Test Class """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ tests nested map """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test exceptions """
        with self.assertRaises(KeyError) as keyerr:
            access_nested_map(nested_map, path)
        self.assertEqual(str(keyerr.exception), "'{}'".format(path[-1]))


class TestGetJson(unittest.TestCase):
    """ TestGetJson, a subclass of unittest.TestCase """
    @unittest.mock.patch("requests.get")
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Tests with get_json """
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)
        mock_response.json.assert_called_once()
