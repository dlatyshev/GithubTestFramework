import requests
import pytest


@pytest.mark.http
def test_first_request():
    response = requests.get("https://api.github.com/zen")
    print(response.text)


@pytest.mark.http
def test_second_request():
    response = requests.get("https://api.github.com/users/dlatyshev")
    print(response.text)
