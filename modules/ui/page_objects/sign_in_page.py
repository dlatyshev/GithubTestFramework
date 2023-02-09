from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://www.github.com/login"
    USERNAME_FIELD = By.ID, "login_field"
    PASSWORD_FIELD = By.ID, "password"
    SUBMIT_BUTTON = By.NAME, "commit"
    FLASH_ERROR = By.CSS_SELECTOR, "div[role=alert]"

    def navigate(self):
        super().navigate(SignInPage.URL)

    def log_in(self, username, password):
        self.navigate()
        self._find(SignInPage.USERNAME_FIELD).send_keys(username)
        self._find(SignInPage.PASSWORD_FIELD).send_keys(password)
        self._find(SignInPage.SUBMIT_BUTTON).click()

    def get_flash_error_message_text(self):
        return self._find(SignInPage.FLASH_ERROR).text