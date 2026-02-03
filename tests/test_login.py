import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Test Data
VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"
LOCKED_USER = "locked_out_user"
INVALID_PASS = "wrong_pass"


def test_valid_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.load()
    login_page.login(VALID_USER, VALID_PASS)

    assert inventory_page.get_title() == "Products"
    assert inventory_page.is_cart_visible()


def test_invalid_login(page):
    login_page = LoginPage(page)

    login_page.load()
    login_page.login(VALID_USER, INVALID_PASS)

    error = login_page.get_error_message()
    assert "Username and password do not match" in error


def test_locked_out_user(page):
    login_page = LoginPage(page)

    login_page.load()
    login_page.login(LOCKED_USER, VALID_PASS)

    error = login_page.get_error_message()
    assert "Sorry, this user has been locked out" in error