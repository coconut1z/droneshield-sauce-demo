from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class InventoryItemPage(BasePage):
    add_to_cart_btn = (By.CLASS_NAME, "btn_primary")
    product_name = (By.CLASS_NAME, "inventory_details_name")
    product_price = (By.CLASS_NAME, "inventory_details_price")
    product_details = (By.CLASS_NAME, "inventory_details_desc")
    
    def __init__(self, driver):
        self.driver = driver
    
    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text
        
    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text
    
    def get_product_details(self):
        return self.driver.find_element(*self.product_details).text