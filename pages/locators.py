from selenium.webdriver.common.by import By


class MainPageLocators():
    pass

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span a.btn-default')


class LoginPageLocators():
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_IN_BASKET_NAME = (By.CSS_SELECTOR, '.alertinner strong')
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alertinner')

class BasketPageLocators():
    PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, 'a.btn-lg')
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')