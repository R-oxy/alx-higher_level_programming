#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import urlopen, Request


if __name__ == "__main__":
    req = Request('https://intranet.hbtn.io/status')
    with urlopen(req) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        print('Body response:')
        print('\t- type: {}'.format(type(content)))
        print('\t- content: {}'.format(content))
        print('\t- utf8 content: {}'.format(utf8_content))
