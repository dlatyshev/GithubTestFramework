import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from modules.ui.page_objects.sign_in_page import SignInPage


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    sign_in_page = SignInPage(driver)
    sign_in_page.navigate()
    
    driver.get("https://www.github.com/login")

    login_field = driver.find_element(By.ID, "login_field")
    login_field.send_keys("invaliduser@gmails.com")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("invalid password")

    sign_in_button = driver.find_element(By.NAME, "commit")
    sign_in_button.click()

    flash_error = driver.find_element(By.CSS_SELECTOR, "div[role=alert]")
    assert flash_error.is_displayed() and flash_error.text == "Incorrect username or password."
    assert driver.title == "Sign in to GitHub · GitHub"

    driver.close()
