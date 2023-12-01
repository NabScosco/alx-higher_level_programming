#!/usr/bin/python3
"""
    Takes GitHub credentials (username and password) and uses the GitHub API
    to display the user's id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get('https://api.github.com/user', auth=(username, password))

    try:
        json_data = response.json()
        print(json_data.get('id'))
    except ValueError:
        print("None")
