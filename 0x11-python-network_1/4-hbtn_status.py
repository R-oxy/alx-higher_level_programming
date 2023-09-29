#!/usr/bin/python3
"""
Fetches the response from a given URL
using the requests library and displays it.
"""

import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    print("Body response:")
    print("\t- type: {_type}".format(_type=type(req.text)))
    print("\t- content: {_content}".format(_content=req.text))
