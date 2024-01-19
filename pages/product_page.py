from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def adding_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button for adding the product to basket is not presented"

    def should_be_same_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_in_basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME).text
        assert product_name == product_in_basket_name, 'The wrong product name in the basket'

    def should_be_same_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total_basket_price = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_PRICE).text
        assert product_price == total_basket_price, 'The wrong total price in the basket'

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message does not disappear"
