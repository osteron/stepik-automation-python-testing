"""
Открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
Авторизоваться со своими логином и паролем
Дождаться того, что поп-апа с авторизацией больше нет
"""
import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

email = ''
password = ''


@pytest.mark.parametrize('number',
                         ['236895', '236896', '236897', '236898',
                          '236899', '236903', '236904', '236905'])
class TestStepikPage:
    @pytest.mark.smoke
    def test_authorize_with_valid_email_and_password_and_send_solving(self, browser, number):
        browser.implicitly_wait(5)
        link = f'https://stepik.org/lesson/{number}/step/1'
        browser.get(link)

        login_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#ember33'))
        )
        login_button.click()

        email_input = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="login"]'))
        )
        email_input.send_keys(email)

        password_input = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="password"]'))
        )
        password_input.send_keys(password)

        submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))
        )
        submit_button.click()

        WebDriverWait(browser, 10).until_not(
            EC.presence_of_element_located((By.CLASS_NAME, 'modal-dialog-inner'))
        )

        answer_input = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea:required'))
        )
        answer_input.send_keys(str(math.log(int(time.time()))))

        answer_submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))
        )
        answer_submit_button.click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'attempt-message_correct'))
        )

        correct = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
        ).text

        assert correct == 'Correct!', f'Текст в опциональном фидбеке "{correct}" не совпадает с "Correct!"'
