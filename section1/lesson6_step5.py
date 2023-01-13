import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'http://suninjuly.github.io/find_link_text'
browser = webdriver.Chrome()

try:
    browser.get(LINK)

    link_text = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link_text.click()

    first_name = browser.find_element(By.TAG_NAME, 'input')
    first_name.send_keys("Dmitry")

    last_name = browser.find_element(By.NAME, 'last_name')
    last_name.send_keys("S")

    city = browser.find_element(By.CLASS_NAME, 'city')
    city.send_keys('Moscow')

    country = browser.find_element(By.ID, 'country')
    country.send_keys('Russia')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
