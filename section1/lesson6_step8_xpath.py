import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.TAG_NAME, 'input')
    first_name.send_keys("Dmitry")

    last_name = browser.find_element(By.NAME, 'last_name')
    last_name.send_keys("S")

    city = browser.find_element(By.CLASS_NAME, 'city')
    city.send_keys('Moscow')

    country = browser.find_element(By.ID, 'country')
    country.send_keys('Russia')

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
