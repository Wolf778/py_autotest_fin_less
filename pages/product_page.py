from .base_page import BasePage
from .locators import MainPageLocators


class Product(BasePage):
    def add_product_to_rec(self):
        add_button = self.browser.find_element(*MainPageLocators.ADD_BUTTON)
        add_button.click()

