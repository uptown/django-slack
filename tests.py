__author__ = 'uptown'
import unittest
from django_slack.client import SlackClient

class TheTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_step1(self):
        print(SlackClient().oauth2_step1_url(client_id="3319221146.3505511246"))

if __name__ == '__main__':
    unittest.main()