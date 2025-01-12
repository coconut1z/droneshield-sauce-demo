from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, ".error-message-container h3")
    
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def login_button_is_displayed(self):
        return self.driver.find_element(*self.login_btn).is_displayed()