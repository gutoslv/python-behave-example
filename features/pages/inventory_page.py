from selenium.webdriver.common.by import By
from features.pages.home_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver
        )

    def load(self):
        self.driver.get(self.URL)

    def is_on_page(self):
        return self.driver.current_url == self.URL

    def get_product_names(self):
        return [product.text for product in self.driver.find_elements(By.CSS_SELECTOR, "div.inventory_item_name")]

    def get_product_images_source(self):
        return [product.get_attribute("src") for product in self.driver.find_elements(By.CSS_SELECTOR, "img"
                                                                                                       ".inventory_item_img")]