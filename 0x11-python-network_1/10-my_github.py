#!/usr/bin/python3
"""
Get the GitHub user ID using Basic Authentication
with a personal access token.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    response = requests.get(
        "https://api.github.com/user",
        auth=(username, personal_access_token)
    )

    if response.status_code == 200:
        print(response.json()["id"])
    else:
        print("None")
