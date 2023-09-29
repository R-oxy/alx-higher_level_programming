#!/usr/bin/python3
"""
Send a POST request to http://0.0.0.0:5000/search_user
with the given letter.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    r = requests.post(url, data=data)
    try:
        json = r.json()
        if json:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
        else:
            print('No result')
    except valueError:
        print('Not a valid JSON')
