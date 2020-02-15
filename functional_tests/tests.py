import os
import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def test_django_installed(self):
        self.browser.get('http://testHost')
        self.assertIn('Django', self.browser.title)

if __name__ == "__main__":
    unittest.main(warnings='ignore')
