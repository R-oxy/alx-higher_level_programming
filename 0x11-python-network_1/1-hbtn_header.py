#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id header
from a given URL's HTTP response.
"""

import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
