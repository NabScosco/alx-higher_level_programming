#!/usr/bin/python3
"""
    Fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content_type = type(response.text)

    print("Body response:")
    print(f"\t- type: {content_type}")
    print(f"\t- content: {response.text}")
