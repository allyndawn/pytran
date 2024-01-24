import json
import requests

# https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-repositories
def get_names(username, secret):
    r = requests.get(
        url=f'https://api.github.com/search/repositories?q=user:{username}',
        headers={
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
            'Authorization': f'Bearer {secret}'
        }
    )

    search_results = r.json()

    names = []
    for item in search_results['items']:
        names.append(item['name'])

    return names

# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#transfer-a-repository
def transfer(from_username, from_user_secret, repository_name, to_username):
    r = requests.post(
        url=f'https://api.github.com/repos/{from_username}/{repository_name}/transfer',
        headers={
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
            'Authorization': f'Bearer {from_user_secret}'
        },
        json={
            'new_owner': to_username
        }
    )
