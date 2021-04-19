#!/usr/bin/env python3
""" this module tests the client module """
from client import GitHubOrgClient
from parameterized import parameterized
from unittest.mock import patch
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ this class test client methods """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_param, mock_json):
        """ this method tests return value for client method """
        test_org = GitHubOrgClient(org_param)
        git_url = "https://api.github.com/orgs/" + org_param
        self.assertEqual(test_org.org, {'key': 'value'})
        mock_json.assert_called_once_with(git_url)
