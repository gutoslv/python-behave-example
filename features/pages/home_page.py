from selenium import webdriver


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

    def end(self):
        self.driver.quit()
