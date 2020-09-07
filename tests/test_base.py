import unittest


class BaseTest(unittest.TestCase):
    def test_flask_health(self):
        import requests
        url = 'http://127.0.0.1:5000/'
        resp = requests.get(url)
        self.assertIsNotNone(resp)
