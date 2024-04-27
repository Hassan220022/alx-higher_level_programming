#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display your user ID.
"""
import requests
import sys


if __name__ == '__main__':

    username = sys.argv[1]
    token = sys.argv[2]

    url = f'https://api.github.com/user'

    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        user_id = response.json().get('id')
        print(user_id)
    else:
        print(None)
