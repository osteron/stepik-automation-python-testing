"""Тестовое задание"""
import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(number):
    """Функция для расчета значения по заданию"""
    return str(math.log(abs(12 * math.sin(int(number)))))


LINK = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()

try:
    browser.get(LINK)

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    RESULT = calc(x)

    text_input = browser.find_element(By.ID, 'answer')
    text_input.send_keys(RESULT)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
finally:
    sleep(30)
    browser.quit()
