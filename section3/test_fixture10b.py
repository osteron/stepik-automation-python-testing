"""pytest -rX -v test_fixture10b.py
Здесь мы добавили символ X в параметр -r, чтобы получить подробную информацию по XPASS-тестам"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for tests..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()


class TestMainPage1:

    def test_guest_should_see_login_link(self, browser):
        browser.get(LINK)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_on_the_main_page(self, browser):
        browser.get(LINK)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')

    @pytest.mark.xfail(reason='fixing this bug right now')
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(LINK)
        browser.find_element(By.CSS_SELECTOR, 'input.btn.btn-default')
