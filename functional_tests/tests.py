import os
from django.test import LiveServerTestCase

from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.test_host = os.environ.get('TEST_HOST')
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def test_app_exists(self):
        if self.test_host:
            self.browser.get(self.test_host)
        else:
            self.browser.get(self.live_server_url)
        self.assertIn('PyLadies', self.browser.title)
        # self.fail('Finish writing this test!')

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)
