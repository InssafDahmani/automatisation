from robot.libraries.BuiltIn import BuiltIn

class CartPage:
    """This class represents the cart page of a web application."""

    # Locators
    PAGE_TITLE    = "//span[@class='title']"
    CART_ITEMS    = "css=.cart_item"
    ITEM_NAME     = "css=.inventory_item_name"
    REMOVE_BUTTON = "xpath=//button[text()='Remove']"
    CONTINUE_BTN  = "id=continue-shopping"
    CHECKOUT_BTN  = "id=checkout"

    def __init__(self):
        self.selenium = BuiltIn().get_library_instance('SeleniumLibrary')

    def verify_cart_page(self):
        """Verifies we are on the cart page."""
        self.selenium.element_should_contain(self.PAGE_TITLE, "Your Cart")

    def verify_product_in_cart(self, product_name):       # ← AJOUTÉ
        """Verifies that the product IS in the cart."""
        self.selenium.page_should_contain(product_name)

    def click_remove(self):                                # ← AJOUTÉ
        """Clicks the Remove button."""
        self.selenium.click_button(self.REMOVE_BUTTON)

    def verify_product_not_in_cart(self, product_name):
        """Verifies product is no longer in cart."""
        self.selenium.page_should_not_contain(product_name)

    def is_product_in_cart(self, product_name):
        """Checks if a specific product is in the cart."""
        items = self.selenium.get_text(self.ITEM_NAME)
        return product_name in items

    def remove_product(self, product_name):
        """Removes a product from the cart."""
        self.selenium.click_button(
            f"xpath=//div[text()='{product_name}']/following-sibling::button[text()='Remove']"
        )

    def get_cart_items(self):
        """Returns all items in the cart."""
        return self.selenium.find_elements(self.CART_ITEMS)

    def get_cart_count(self):
        """Returns the number of items in the cart."""
        return len(self.get_cart_items())

    def is_cart_empty(self):
        """Checks if the cart is empty."""
        return self.get_cart_count() == 0