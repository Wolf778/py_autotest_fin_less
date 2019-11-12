from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main>h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    ADD_NAME_PRODUCT = (By.CSS_SELECTOR, "div.alertinner")
    ADD_PRICE_PRODUCT = (By.CSS_SELECTOR, "div > div.basket-mini.pull-right.hidden-xs")
