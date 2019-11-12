from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class Product(BasePage):
    def name_product(self):
        return self.browser.find_element(*MainPageLocators.NAME_PRODUCT).text

    def price_product(self):
        return self.browser.find_element(*MainPageLocators.PRICE_PRODUCT).text

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*MainPageLocators.ADD_BUTTON)
        add_button.click()

    def assert_name(self, name_product):
        add_name_product = self.browser.find_element(*MainPageLocators.ADD_NAME_PRODUCT).text
        assert name_product in add_name_product, "Имя продукта в корзине не совпадает с добавленным"

    def assert_price(self, price_product):
        add_price_product = self.browser.find_element(*MainPageLocators.ADD_PRICE_PRODUCT).text
        assert price_product in add_price_product, f"Цена продукта в корзине не совпадает с добавленным {price_product}, {add_price_product}"
