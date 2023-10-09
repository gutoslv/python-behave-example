from selenium.webdriver.common.by import By
from features.pages.home_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver
        )

    def load(self):
        self.driver.get(self.URL)

    def is_on_page(self):
        return self.driver.current_url == self.URL

    def enter_user(self, user):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(user)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
