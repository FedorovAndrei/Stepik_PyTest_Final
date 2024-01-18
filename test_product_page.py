import time
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(5)
    page.should_be_add_to_basket_button()
    page.adding_to_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_same_name()
    page.should_be_same_price()
