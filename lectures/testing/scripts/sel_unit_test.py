from selenium import webdriver
from selenium.webdriver.common import keys

import unittest

URL = "https://www.google.com.ua/"


class TestURL(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    def setUp(self) -> None:
        self.driver.get(URL)

    def test_open_url(self):
        input_line = self.driver.find_element_by_class_name("gLFyf")
        input_line.click()
        print("input_line", input_line)
        input_line.send_keys("Python")
        input_line.send_keys(keys.Keys.ENTER)
