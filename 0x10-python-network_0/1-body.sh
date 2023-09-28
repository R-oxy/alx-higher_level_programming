#!/bin/bash
# This script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" -X GET -D ./header -o ./output && { grep -q "200 OK" ./header && cat ./output; } || echo ""
