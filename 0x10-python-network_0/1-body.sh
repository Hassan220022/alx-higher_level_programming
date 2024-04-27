#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response only if the status code is 200
response=$(curl -s -o response_body -w "%{http_code}" "$1")
if [ "$response" -eq 200 ]; then
    cat response_body
fi
rm response_body
