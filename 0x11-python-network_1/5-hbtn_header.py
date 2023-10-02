#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    x_req_id = req.headers.get("X-Request-Id")
    print(x_req_id)
