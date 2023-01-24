import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ""
    assert not user.name, "User name should be empty"


@pytest.mark.check
def test_name(user):
    assert user.name == "Dmytro"


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Latyshev"
