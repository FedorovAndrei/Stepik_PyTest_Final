from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        assert "basket" in self.browser.current_url, "Substring 'basket' is not presented"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PROCEED_TO_CHECKOUT), 'Basket is not empty'

    def should_be_text_that_basket_is_empty(self):
        languages = {"ar": "سلة التسوق فارغة", "ca": "La seva cistella està buida.", "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.", "de": "Ihr Warenkorb ist leer.", "en": "Your basket is empty.",
            "en-gb": "Your basket is empty.", "el": "Το καλάθι σας είναι άδειο.", "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä", "fr": "Votre panier est vide.", "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.", "nl": "Je winkelmand is leeg", "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.", "pt-br": "Sua cesta está vazia.", "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста", "sk": "Váš košík je prázdny", "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty."}
        actual_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        active_language = self.active_language()
        assert languages[active_language] in actual_text, "No text that basket is empty"
