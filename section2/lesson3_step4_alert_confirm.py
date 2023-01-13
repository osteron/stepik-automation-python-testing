"""Принимает alert"""
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(number):
    """Функция для расчета значения по заданию"""
    return str(math.log(abs(12 * math.sin(int(number)))))


LINK = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()

try:
    browser.get(LINK)

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    value = browser.find_element(By.ID, 'input_value').text
    result = calc(value)

    input_text = browser.find_element(By.ID, 'answer')
    input_text.send_keys(result)

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
