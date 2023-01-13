"""Загрузка файла и использование библиотеки os"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

LINK = 'http://suninjuly.github.io/file_input.html'

browser = webdriver.Chrome()

try:
    browser.get(LINK)

    first_name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    choose_file = browser.find_element(By.ID, 'file')
    submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

    for element in first_name, last_name, email:
        element.send_keys('HELLO BOY OR GIRL')

    choose_file.send_keys(file_path)

    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
