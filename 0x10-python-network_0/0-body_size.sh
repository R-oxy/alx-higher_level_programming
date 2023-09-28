#!/bin/bash
# This script sends a GET request to a URL and displays the size of the response body in bytes
curl -sI "$1" | grep -i "Content-Length:" | cut -d " " -f 2
