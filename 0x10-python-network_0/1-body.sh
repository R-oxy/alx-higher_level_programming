#!/bin/bash
# This script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -X GET -D - "$1" | awk 'NR==1 { if ($2 == 200) print $0 }' | awk 'END { if (NR == 0) exit 1 } 1'
