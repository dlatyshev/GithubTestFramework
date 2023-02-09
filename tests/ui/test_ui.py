import pytest

from modules.ui.page_objects.sign_in_page import SignInPage


@pytest.mark.ui
def test_check_incorrect_username(driver):
    sign_in_page = SignInPage(driver)
    sign_in_page.log_in("invaliduser@gmails.com", "password")
    assert sign_in_page.page_title == "Sign in to GitHub · GitHub"
    assert sign_in_page.get_flash_error_message_text() == "Incorrect username or password."
