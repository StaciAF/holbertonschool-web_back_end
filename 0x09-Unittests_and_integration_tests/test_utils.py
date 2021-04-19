#!/usr/bin/env python3
""" this module builds test for utils """
from parameterized import parameterized
from typing import Dict
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
import requests
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
        with patch('requests.get') as mock_req:
            mock_req().json.return_value = test_payload
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            self.assertEqual(isinstance(response, Dict), True)
            assert mock_req.call_count == 2


class TestMemoize(unittest.TestCase):
    """ this class tests memoize decorator """
    def test_memoize(self):
        """ this method tests memoize """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as a_method:
            test_class = TestClass()
            test1 = test_class.a_property
            test2 = test_class.a_property
            self.assertEqual(test1, 42)
            self.assertEqual(test2, 42)
            a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
