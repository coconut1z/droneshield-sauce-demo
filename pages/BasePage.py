import time
from selenium.webdriver.common.by import By


class BasePage:
    cart_count = (By.CLASS_NAME, "shopping_cart_badge")
    cart_btn = (By.CLASS_NAME, "shopping_cart_link")
    menu_btn = (By.ID, "react-burger-menu-btn")
    logout_btn = (By.ID, "logout_sidebar_link")

    def click_cart(self):
        self.driver.find_element(*self.cart_btn).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_count).text

# Using time.sleep() as a lazy way of waiting for the side bar animation to play, ideally use a explicit wait with expected conditions to reduce overall testing time
    def click_menu(self):
        self.driver.find_element(*self.menu_btn).click()
        time.sleep(1)

    def click_logout(self):
        self.driver.find_element(*self.logout_btn).click()
