import time
from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'http://suninjuly.github.io/registration1.html'

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
    first_name.send_keys('Hello')

    last_name = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
    last_name.send_keys('Hello')

    email = browser.find_element(By.XPATH, '//div[@class="form-group third_class"]//input')
    email.send_keys('Hello')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
