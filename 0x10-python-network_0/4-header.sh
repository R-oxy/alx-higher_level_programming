#!/bin/bash
# This script that takes in a URL as an argument, sends a GET request with a header variable X-School-User-Id with the value 98 to the URL, and displays the body of the response
curl -s -X GET -H "X-School-User-Id: 98" "$1"
