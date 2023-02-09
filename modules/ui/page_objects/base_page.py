from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


SECONDS = int


class BasePage:
    BASE_TIMEOUT: SECONDS = 5

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__base_wait = WebDriverWait(self.__driver, BasePage.BASE_TIMEOUT)

    def navigate(self, url):
        self.__driver.get(url)

    @property
    def page_title(self):
        return self.__driver.title

    def _find(self, locator, condition=ec.presence_of_element_located, timeout: SECONDS = 0):
        wait = self.__select_wait(timeout)
        return wait.until(condition(locator))
    
    def __select_wait(self, timeout) -> WebDriverWait:
        if not timeout:
            return self.__base_wait
        else:
            return WebDriverWait(self.__driver, timeout)

