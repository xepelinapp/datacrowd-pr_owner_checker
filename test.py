import requests

def get_pull_request_user(owner, repo, pull_request_number, access_token):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_request_number}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        pull_request_data = response.json()
        user_login = pull_request_data.get('user', {}).get('login')
        return user_login
    else:
        print(f"Failed to fetch pull request details. Status code: {response.status_code}")
        return None

# Example usage:
owner = 'xepelin'
repo = 'datacrowd-pr_owner_checker'
pull_request_number = 1  # Replace with your pull request number
access_token = 'CUSTOM_GA_TOKEN'

user_login = get_pull_request_user(owner, repo, pull_request_number, access_token)
if user_login:
    print(f"The user of pull request #{pull_request_number} is: {user_login}")
else:
    print("Failed to fetch user information.")
