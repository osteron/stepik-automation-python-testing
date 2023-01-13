"""Scroll it!"""
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(number):
    """Функция для расчета значения по заданию"""
    return str(math.log(abs(12 * math.sin(int(number)))))


LINK = 'http://suninjuly.github.io/execute_script.html'

browser = webdriver.Chrome()

try:
    browser.get(LINK)

    x_element = browser.find_element(By.ID, 'input_value').text
    RESULT = calc(x_element)
    text_input = browser.find_element(By.ID, 'answer')
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    radiobutton = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

    browser.execute_script('window.scrollBy(0, 100);')
    # browser.execute_script('return arguments[0].scrollIntoView(true)', submit_button)
    text_input.send_keys(RESULT)

    for element in checkbox, radiobutton, submit_button:
        element.click()

finally:
    time.sleep(30)
    browser.quit()
