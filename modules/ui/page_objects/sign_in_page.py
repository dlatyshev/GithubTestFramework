from ui.page_objects.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver


class SignInPage(BasePage):
    URL = "https://www.github.com/login"
    
    def navigate(self):
        self._driver.get(SignInPage.URL)

    