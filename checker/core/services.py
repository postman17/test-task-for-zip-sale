from django.conf import settings
from utils.github_connector import GithubConnector


def build_data_to_list(username):
    """Build github data to python dict."""
    client = GithubConnector(settings.GITHUB_OAUTH_TOKEN, username)
    repos = client.get_repos()
    data = []
    if not isinstance(repos, list):
        reset_time = client.get_rate_limit_reset_time()
        raise Exception(f'Rate limit exceed on {reset_time} hours')

    for repository in repos:
        rep_data = {
            'name': repository.get('name'),
            'link': f'https://github.com/{username}/{repository.get("name")}',
            'stars': repository.get('stargazers_count')
        }
        pull_requests = client.get_pull_requests(repository.get("name"))
        rep_data['merged_pull_requests'] = [
            {
                'url': item['html_url'],
                'num_of_comments': len(client.get_pull_requests_comments(repository.get('name'), item['number']))
            } for item in list(filter(lambda x: x['user'].get('login') == username and x['merged_at'], pull_requests))
        ]
        rep_data['unmerged_pull_requests'] = [
            {
                'url': item['html_url'],
                'num_of_comments': len(client.get_pull_requests_comments(repository.get('name'), item['number']))
            } for item in list(
                filter(lambda x: x['user'].get('login') == username and not x['merged_at'], pull_requests)
            )
        ]
        data.append(rep_data)

    return data
