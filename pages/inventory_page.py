from pages.base_page import BasePage


class InventoryPage(BasePage):
    # Selectors
    PAGE_TITLE = ".title"
    SHOPPING_CART = ".shopping_cart_link"

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def is_cart_visible(self):
        return self.get_element(self.SHOPPING_CART).is_visible()