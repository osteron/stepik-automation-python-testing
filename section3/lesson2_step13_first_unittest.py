"""Первое тест на unittest"""
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Ссылка на исправную версию формы регистрации
LINK1 = 'http://suninjuly.github.io/registration1.html'
# Ссылка на версию формы регистрации с ошибкой
LINK2 = 'http://suninjuly.github.io/registration2.html'


class TestAbs(unittest.TestCase):
    browser = webdriver.Chrome()

    def test_positive_registration_form(self):
        self.browser.get(LINK1)
        first_name = self.browser.find_element(By.XPATH,
                                               '//div[@class="first_block"]//input[@class="form-control first"]')
        first_name.send_keys('Hello')

        last_name = self.browser.find_element(By.XPATH,
                                              '//div[@class="first_block"]//input[@class="form-control second"]')
        last_name.send_keys('Hello')

        email = self.browser.find_element(By.XPATH, '//div[@class="form-group third_class"]//input')
        email.send_keys('Hello')

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         f"The text does not match with '{welcome_text}'")

    def test_negative_registration_form(self):
        self.browser.get(LINK2)
        first_name = self.browser.find_element(By.XPATH,
                                               '//div[@class="first_block"]//input[@class="form-control first"]')
        first_name.send_keys('Hello')

        last_name = self.browser.find_element(By.XPATH,
                                              '//div[@class="first_block"]//input[@class="form-control second"]')
        last_name.send_keys('Hello')

        email = self.browser.find_element(By.XPATH, '//div[@class="form-group third_class"]//input')
        email.send_keys('Hello')

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         f"The text does not match with '{welcome_text}'")


if __name__ == "__main__":
    unittest.main()
