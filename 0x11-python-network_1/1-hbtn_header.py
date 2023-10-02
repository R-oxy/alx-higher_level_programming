#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id header
from a given URL's HTTP response.
"""

from urllib import request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    with request.urlopen(req) as response:
        x_req_id = response.getheader('X-Request-Id')
        print(x_req_id)
