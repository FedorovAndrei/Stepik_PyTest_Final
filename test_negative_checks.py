import time, pytest
from .pages.product_page import ProductPage

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(5)
    page.should_be_add_to_basket_button()
    page.adding_to_basket()
    time.sleep(2)
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(5)
    page.should_be_add_to_basket_button()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(5)
    page.should_be_add_to_basket_button()
    page.adding_to_basket()
    time.sleep(2)
    page.should_disappear()