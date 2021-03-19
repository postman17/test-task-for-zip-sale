import requests
from datetime import datetime, timezone


class GithubConnector:
    def __init__(self, token, username):
        self.headers = {
            'Authorization': f'token {token}',
        }
        self.username = username

    def get_rate_limit_reset_time(self):
        response = requests.get('https://api.github.com/users/octocat')
        reset_time = datetime.fromtimestamp(int(response.headers.get('X-RateLimit-Reset', 0)), timezone.utc)
        return reset_time - datetime.now(timezone.utc)

    def get_repos(self):
        response = requests.get(f'https://api.github.com/users/{self.username}/repos', headers=self.headers)
        return response.json()

    def get_pull_requests(self, repos_name):
        response = requests.get(
            f'https://api.github.com/repos/{self.username}/{repos_name}/pulls',
            headers=self.headers,
        )
        return response.json()

    def get_pull_requests_comments(self, repos_name, pull_request_number):
        response = requests.get(
            f'https://api.github.com/repos/{self.username}/{repos_name}/pulls/{pull_request_number}/comments',
            headers=self.headers,
        )
        return response.json()
