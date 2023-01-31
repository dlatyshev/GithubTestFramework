import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    response_body = github_api.get_user('windowsxpenterescape')
    assert response_body['message'] == 'Not Found'


@pytest.mark.api
def test_repo_search(github_api):
    response_body = github_api.search_repo("PythonPlaywright")
    assert response_body['total_count'] > 0
    assert "PythonPlaywright" in [item['name']
                                  for item in response_body['items']]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    response_body = github_api.search_repo("NonExistingRepoXXX")
    assert response_body['total_count'] == 0


@pytest.mark.api
def test_repo_search_with_single_character(github_api):
    response_body = github_api.search_repo("x")
    assert response_body['total_count'] > 0
