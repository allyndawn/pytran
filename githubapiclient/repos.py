import json
import requests

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
