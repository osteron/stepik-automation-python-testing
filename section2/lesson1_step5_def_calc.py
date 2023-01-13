"""Тестовое задание"""
import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(number):
    """Функция для расчета значения по заданию"""
    return str(math.log(abs(12 * math.sin(int(number)))))


LINK = 'https://suninjuly.github.io/math.html'

browser = webdriver.Chrome()

try:
    browser.get(LINK)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    RESULT = calc(x)

    text_input = browser.find_element(By.ID, 'answer')
    text_input.send_keys(RESULT)

    checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
finally:
    sleep(30)
    browser.quit()
