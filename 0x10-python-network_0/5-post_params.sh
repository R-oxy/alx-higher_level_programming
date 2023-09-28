#!/bin/bash
# This Bash script sends a POST request to a specified URL with parameters and displays the response body.
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
