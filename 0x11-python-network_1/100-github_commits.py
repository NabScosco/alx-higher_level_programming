#!/usr/bin/python3
"""
    List 10 commits (from the most recent to oldest) of the repository “rails”
    by the user “rails”.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    response = requests.get(url)

    try:
        commits = response.json()[:10]

        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit', {}).get('author', {}).get('name')
            print(f'{sha}: {author_name}')

    except ValueError:
        print("Not a valid JSON")
