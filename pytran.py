import json
import githubapiclient.repos as repos_api

if __name__ == "__main__":
    f = open('config.json')
    config = json.load(f)
    f.close()

    from_username = config['from']['username']
    from_user_secret = config['from']['secret']
    to_username = config['to']['username']

    while(True):
        print('')
        repo_names = repos_api.get_names(from_username, from_user_secret)

        for idx, repo_name in enumerate(repo_names):
            print(idx, repo_name)

        selection = input(f'Enter number of repo to transfer from {from_username} to {to_username} (or just hit enter to abort): ')
        if not selection:
            break

        selection = int(selection)
        repo_name = repo_names[selection]
        repos_api.transfer(from_username, from_user_secret, repo_name, to_username)
        print(f'Transfer of {repo_name} initiated')
