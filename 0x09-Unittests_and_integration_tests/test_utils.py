#!/usr/bin/env python3
""" this module builds test for utils """
from parameterized import parameterized
from unittest import mock
from utils import access_nested_map, get_json
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ this class tests access_nested_maps method from utils.py """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ this method runs tests for access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ this method runs test on method exceptions """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """ this class tests get_json method """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        with mock.patch('requests.get()') as mock_req:
            response = mock_req.get_json(test_url)
            self.assertEqual(isinstance(response, dict), True)
            self.assertEqual(response, test_payload)
            mock.return_value = response
            assert mock_req() == test_payload


if __name__ == '__main__':
    unittest.main()
