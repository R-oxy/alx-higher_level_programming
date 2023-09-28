#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response
curl -sLX PUT -H "0.0.0.0:5000/catch_me" -d "user_id=98" "Origin: You got me!"
