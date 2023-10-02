#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id header
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_req_id = response.getheader('X-Request-Id')
        print(x_req_id)
