from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    checkout_btn = (By.ID, "checkout")
    cart_items = (By.CLASS_NAME, "cart_item")
    product_name = (By.CLASS_NAME, "inventory_item_name")
    remove_button = (By.CLASS_NAME, "cart_button")

    def __init__(self, driver):
        self.driver = driver

#   Uses loops through a list of items in the cart so even if the cart is empty it won't error out if there are no items to begin with
    def is_in_cart(self, name):
        cart_items = self.driver.find_elements(*self.cart_items)
        for item in cart_items:
            product_name = item.find_element(*self.product_name)
            if product_name.text == name:
                return True
        return False

    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()

    def remove_from_cart(self, name):
        cart_items = self.driver.find_elements(*self.cart_items)
        for item in cart_items:
            product_name = item.find_element(*self.product_name)
            if product_name.text == name:
                item.find_element(*self.remove_button).click()
                
    def cart_is_empty(self):
        cart_items = self.driver.find_elements(*self.cart_items)
        return len(cart_items) == 0