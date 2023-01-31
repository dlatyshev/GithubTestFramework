import requests


class Github:

    BASE_URL = "https://api.github.com"
    GET_USER_ENDPOINT = "/users/{username}"
    SEARCH_REPO_ENDPOINT = "/search/repositories"

    def get_user(self, username):
        response = requests.get(
            Github.BASE_URL + Github.GET_USER_ENDPOINT.format(username=username))
        body = response.json()
        return body

    def search_repo(self, name):
        response = requests.get(
            Github.BASE_URL + Github.SEARCH_REPO_ENDPOINT, params={'q': name})
        body = response.json()
        return body
