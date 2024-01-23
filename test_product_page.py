import time, pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.authorised
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.page = ProductPage(browser, link)
        self.page.open()
        time.sleep(3)
        email = str(time.time()) + "@fakemail.org"
        password = 'fdJ-fslF-34K'
        self.page.go_to_login_page()
        time.sleep(3)
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        time.sleep(3)
        self.page = ProductPage(browser, link)
        self.page.open()
        time.sleep(3)
        self.page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        self.page.should_be_add_to_basket_button()
        self.page.adding_to_basket()
        time.sleep(2)
        self.page.should_be_success_message()
        self.page.should_be_same_name()
        self.page.should_be_same_price()

    def test_user_cant_see_success_message(self, browser):
        self.page.should_be_add_to_basket_button()
        self.page.should_not_be_success_message()


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
    page.should_be_success_message()
    page.should_be_same_name()
    page.should_be_same_price()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket()
    basket_page.should_be_text_that_basket_is_empty()

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