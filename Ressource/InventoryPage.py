from robot.libraries.BuiltIn import BuiltIn

class InventoryPage:
    """This class represents the inventory page of a web application."""

    # Locators
    PAGE_TITLE          = "//span[@class='title']"
    PRODUCT_NAMES       = "css=.inventory_item_name"
    PRODUCT_PRICES      = "css=.inventory_item_price"
    PRODUCT_DESCRIPTIONS = "css=.inventory_item_desc"
    CART_ICON           = "id=shopping_cart_container"
    ADD_TO_CART_BIKE    = "add-to-cart-sauce-labs-bike-light"

    def __init__(self):
        # ← manquait !
        self.selenium = BuiltIn().get_library_instance('SeleniumLibrary')

    def verify_inventory_page(self):
        """Verifies we are on the inventory/products page."""
        self.selenium.element_should_contain(self.PAGE_TITLE, "Products")

    def get_product_names(self):
        """Retrieves product names."""
        return self.selenium.get_text(self.PRODUCT_NAMES)

    def get_product_prices(self):
        """Retrieves product prices."""
        return self.selenium.get_text(self.PRODUCT_PRICES)

    def get_product_descriptions(self):
        """Retrieves product descriptions."""
        return self.selenium.get_text(self.PRODUCT_DESCRIPTIONS)

    def get_bike_light_info(self):
        """Retrieves and displays price and description of Sauce Labs Bike Light."""
        price = self.selenium.get_text(
            "xpath=//div[text()='Sauce Labs Bike Light']"
            "/ancestor::div[@class='inventory_item']"
            "//div[@class='inventory_item_price']"
        )
        description = self.selenium.get_text(
            "xpath=//div[text()='Sauce Labs Bike Light']"
            "/ancestor::div[@class='inventory_item']"
            "//div[@class='inventory_item_desc']"
        )
        print(f"\n Product : Sauce Labs Bike Light")
        print(f" Price   : {price}")
        print(f" Desc    : {description}")
        return price, description

    def add_bike_light_to_cart(self):
        """Adds Sauce Labs Bike Light to the cart."""
        self.selenium.click_button(self.ADD_TO_CART_BIKE)

    def view_cart(self):
        """Navigates to the shopping cart page."""
        self.selenium.click_element(self.CART_ICON)