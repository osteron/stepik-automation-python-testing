import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f'http://selenium1py.pythonanywhere.com/{language}/'
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')
