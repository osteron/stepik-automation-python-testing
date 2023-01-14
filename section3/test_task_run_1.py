"""pytest -v -m "smoke and not beta_users" test_task_run_1.py"""
import pytest


@pytest.fixture
def browser():
    pass


class TestMainPage1:
    # Номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # Номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket:
    # Номер 3
    @pytest.mark.skip(reason='not implemented yet')
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # Номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True


@pytest.mark.skip
class TestBookPage:
    # Номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # Номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True


@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True
