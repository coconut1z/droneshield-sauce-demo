from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    firstname_input = (By.ID, "first-name")
    lastname_input = (By.ID, "last-name")
    postcode_input = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")
    checkout_confirmation_message = (By.CLASS_NAME, "complete-header")
    
    def __init__(self, driver):
        self.driver = driver
        
    def checkout(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.firstname_input).send_keys(first_name)
        self.driver.find_element(*self.lastname_input).send_keys(last_name)
        self.driver.find_element(*self.postcode_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_btn).click()
        
    def click_finish(self):
        self.driver.find_element(*self.finish_btn).click()
        
    def get_checkout_confirmation_message(self):
        return self.driver.find_element(*self.checkout_confirmation_message).text