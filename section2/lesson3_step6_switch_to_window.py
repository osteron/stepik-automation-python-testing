"""Переключение на новую вкладку"""
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(number):
    """Функция для расчета значения по заданию"""
    return str(math.log(abs(12 * math.sin(int(number)))))


LINK = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()

try:
    browser.get(LINK)

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

    new_window = browser.window_handles[1]  # Следующая вкладка
    browser.switch_to.window(new_window)    # Переход на следующую вкладку

    value = browser.find_element(By.ID, 'input_value').text
    result = calc(value)

    text_input = browser.find_element(By.ID, 'answer')
    text_input.send_keys(result)

    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
