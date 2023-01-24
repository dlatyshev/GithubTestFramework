import pytest


def test_remove_name(user):
    user.name = ""
    assert user.name == ""


@pytest.mark.smoke
def test_user_name(user):
    assert user.name == "Dmytro"


@pytest.mark.smoke
def test_user_second_name(user):
    assert user.second_name == "Latyshev"


@pytest.mark.math
def test_check_math():
    assert 7 * 7 == 49
    assert 7 / 7 == 1
    assert 7 % 7 == 0
    assert 7 ** 2 == 49
