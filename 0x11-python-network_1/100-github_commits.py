#!/usr/bin/python3
"""
Fetches and prints the 10 most recent
commits from a GitHub repository.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)
    else:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        url = "https://api.github.com/repos/{}/{}/commits".format(
            owner_name, repo_name)

        try:
            r = requests.get(url)
            commits = r.json()

            for commit in commits[:10]:
                sha = commit.get("sha")
                author = commit.get("commit").get("author").get("name")
                print("{}: {}".format(sha, author))
        except requests.exceptions.RequestException as e:
            print("Error: {}".format(e))
