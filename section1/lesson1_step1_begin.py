import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды увидим новое открытие окна браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы успеть увидеть, что происходит в браузере
time.sleep(5)

# метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)

# метод find_element позволяет найти нужный элемент на сайте, указать путь к нему
# метод принимает в качестве аргументов способ поиска и значение, по которому необходимо искать
# ищем поле ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, '.textarea')

# напишем текст ответа в найденное поле
textarea.send_keys('get()')
time.sleep(5)

# найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, '.submit-submission')

# скажем драйверу, что нужно нажать на кнопку
submit_button.click()
time.sleep(5)

# после выполненных действий необходимо не забыть закрыть окно браузера
driver.quit()
