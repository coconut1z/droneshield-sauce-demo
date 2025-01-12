from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InventoryPage(BasePage):
    add_to_cart_btn = (By.CLASS_NAME, "btn_primary")
    products = (By.CLASS_NAME, "inventory_item")
    product_name = (By.CLASS_NAME, "inventory_item_name")
    product_price = (By.CLASS_NAME, "inventory_item_price")
    product_sort = (By.CLASS_NAME, "product_sort_container")
    title = (By.CLASS_NAME, "title")
    
    def __init__(self, driver):
        self.driver = driver
    
    def add_product_to_cart(self, name):
        products = self.driver.find_elements(*self.products)
        for product in products:
            product_name = product.find_element(*self.product_name)
            if product_name.text == name:
                product.find_element(*self.add_to_cart_btn).click()
                break
        
    def get_title(self):
        return self.driver.find_element(*self.title).text
    
    def click_product(self, name):
        products = self.driver.find_elements(*self.products)
        for product in products:
            product_name = product.find_element(*self.product_name)
            if product_name.text == name:
                product_name.click()
                break    
        
# While not how a person would normally interact with this type of element, it does simplify the page inspection process since the dropdown automatically disappears on clicks
    def sort_by(self, option):
        self.driver.find_element(*self.product_sort).click()
        self.driver.find_element(*self.product_sort).send_keys(option)
        self.driver.find_element(*self.product_sort).send_keys(Keys.RETURN)
    
# If sorting by price, we first get all the values, remove the '$' then compare it to a list sorted by Python
    def is_sorted_ascending(self, option):
        if option == "Price":
            prices = self.driver.find_elements(*self.product_price)
            prices_cleaned = [float(char.replace('$', '')) for char in (element.text for element in prices)]
            return prices_cleaned == sorted(prices_cleaned)            
        elif option == "Name":
            names = self.driver.find_elements(*self.product_name)
            names_text = [element.text for element in names]
            return names_text == sorted(names_text)
        
# This has Optional to help identify what type of parameter is to be based and type hinting for our expected return type
    def is_sorted_descending(self, option: str) -> bool:
        if option == "Price":
            prices = self.driver.find_elements(*self.product_price)
            prices_cleaned = [float(char.replace('$', '')) for char in (element.text for element in prices)]
            return prices_cleaned == sorted(prices_cleaned, reverse=True)            
        elif option == "Name":
            names = self.driver.find_elements(*self.product_name)
            names_text = [element.text for element in names]
            return names_text == sorted(names_text, reverse=True)