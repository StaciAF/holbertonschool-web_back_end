#!/usr/bin/env python3
""" this module tests the client module """
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """ this class test client methods """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_param, mock_json):
        """ this method tests return value for client method """
        test_org = GithubOrgClient(org_param)
        git_url = "https://api.github.com/orgs/" + org_param
        self.assertEqual(test_org.org, {'key': 'value'})
        mock_json.assert_called_once_with(git_url)

    def test_public_repos_url(self):
        """ this method unit-tests _public_repos_url """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': 'something.com'}
            client = GithubOrgClient("brand_new")
            self.assertEqual(client._public_repos_url, "something.com")
