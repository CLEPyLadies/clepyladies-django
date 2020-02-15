import os
import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.test_host = os.environ.get('TEST_HOST')
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def test_django_installed(self):
        if self.test_host:
            self.browser.get(self.test_host)
        else:
            self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)

if __name__ == "__main__":
    unittest.main(warnings='ignore')
