from pages.product_page import Product
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = Product(browser, link)           # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    time.sleep(3)
    name_product = page.name_product()      # запоминаем имя продукта
    page.add_product_to_basket()            # добавляем товар в корзину
    page.solve_quiz_and_get_code()          # проверяем код сообщения
    page.assert_name(name_product)          # проверяем корректность добавленного товара
    price_product = page.price_product()    # запоминаем цену продукта
    page.assert_price(price_product)        # проверяем корректность добавленной цены товара

    time.sleep(5)






