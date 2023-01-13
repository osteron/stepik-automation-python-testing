"""Ожидание отображения текста на странице"""
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(number):
    """Функция для расчета значения по заданию"""
    return str(math.log(abs(12 * math.sin(int(number)))))


LINK = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Chrome()

try:
    browser.get(LINK)
    # Ожидание отображения всех элементов в течение 15 секунд
    browser.implicitly_wait(15)
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    submit_button = browser.find_element(By.ID, 'solve')
    browser.execute_script('return arguments[0].scrollIntoView(true)', submit_button)

    value = browser.find_element(By.ID, 'input_value').text
    result = calc(value)

    text_input = browser.find_element(By.ID, 'answer')
    text_input.send_keys(result)

    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
