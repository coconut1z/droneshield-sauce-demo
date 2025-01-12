import pytest
from selenium import webdriver
from pages.CartPage import CartPage
from pages.LoginPage import LoginPage
from pages.CheckoutPage import CheckoutPage
from pages.InventoryPage import InventoryPage
from pages.InventoryItemPage import InventoryItemPage


@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_successful_login(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = InventoryPage(setup_driver)
    assert "Products" in products_page.get_title()
    

def test_unsuccessful_login(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.login("standard_user", "apple_sauce")
    assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message()


def test_logout(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = InventoryPage(setup_driver)
    products_page.click_menu()
    products_page.click_logout()
    assert login_page.login_button_is_displayed()


def test_product_sorting_price_ascending(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = InventoryPage(setup_driver)
    products_page.sort_by("Price (low to high)")
    assert products_page.is_sorted_ascending("Price")


def test_product_sorting_name_descending(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = InventoryPage(setup_driver)
    products_page.sort_by("Name (Z to A)")
    assert products_page.is_sorted_descending("Name")


def test_product_details(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = InventoryPage(setup_driver)
    products_page.click_product("Sauce Labs Fleece Jacket")

    product_page = InventoryItemPage(setup_driver)
    assert "Sauce Labs Fleece Jacket" in product_page.get_product_name()
    assert "$49.99" in product_page.get_product_price()


def test_add_to_cart(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = InventoryPage(setup_driver)
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.click_cart()

    cart_page = CartPage(setup_driver)
    assert cart_page.is_in_cart("Sauce Labs Backpack")


def test_remove_from_cart(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = InventoryPage(setup_driver)
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.click_cart()

    cart_page = CartPage(setup_driver)
    cart_page.remove_from_cart("Sauce Labs Backpack")
    assert cart_page.cart_is_empty()


def test_checkout(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = InventoryPage(setup_driver)
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bike Light")
    products_page.click_cart()

    cart_page = CartPage(setup_driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(setup_driver)
    checkout_page.checkout("First", "Last", "1234")
    checkout_page.click_finish()
    assert "Thank you for your order!" in checkout_page.get_checkout_confirmation_message()