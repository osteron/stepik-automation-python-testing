"""Тестовое задание"""
import time

from _decimal import Decimal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

LINK = 'http://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()

try:
    browser.get(LINK)
    number_one = browser.find_element(By.ID, 'num1').text
    number_two = browser.find_element(By.ID, 'num2').text
    # symbol = browser.find_element(By.ID, '//span[@id="num1"]/following-sibling::span')
    RESULT = Decimal(number_one) + Decimal(number_two)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(RESULT))
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
