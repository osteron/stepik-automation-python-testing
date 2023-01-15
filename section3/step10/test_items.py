"""
1. Тест в репозитории можно запустить командой pytest --language=es, тест успешно проходит.
2. Проверка работоспособности кода для разных языков. Добавьте в файл с тестом команду time.sleep(30)
сразу после открытия ссылки. Запустите тест с параметром --language=fr и визуально проверьте, что фраза
на кнопке добавления в корзину выглядит так: "Ajouter au panier".
3. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
4. В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным для
проверяемой страницы. Есть assert.
5. Название тестового метода внутри файла test_items.py соответствует задаче. Название test_something
не удовлетворяет требованиям.
"""
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestBookPage:
    # По заданию №5 название тестового метода соответствует задаче
    def test_find_the_button_for_adding_book_to_basket_with_choice_language(self, browser):
        browser.get(LINK)
        # По заданию №2 устанавливается time.sleep(30)
        time.sleep(30)
        # Поиск кнопки добавления в корзину
        # По заданию №4 добавлен assert
        assert WebDriverWait(browser, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'btn-add-to-basket'))
            )
        # По заданию №4 считаем количество элементов на странице с селектором кнопки добавления в корзину
        number = WebDriverWait(browser, 5).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, 'btn-add-to-basket'))
            )
        # Здесь по заданию №4 проверяется уникальность селектора кнопки (количество == 1 на странице)
        assert len(number) == 1, f'The selector found is not unique, number is {len(number)}'
