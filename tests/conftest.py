import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from modules.api.clients.github import Github


class User:
    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Dmytro"
        self.second_name = "Latyshev"

    def delete(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()
    yield user
    user.delete()


@pytest.fixture
def github_api():
    yield Github()


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.close()

