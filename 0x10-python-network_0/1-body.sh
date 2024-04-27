#!/bin/bash
# this script sends a GET request to a URL and displays the body of the response

URL=$1
STATUS_CODE=$(curl -s -o /dev/null -I -w "%{http_code}" $URL)

if [ $STATUS_CODE -eq 200 ]; then
    curl -s $URL
else
    echo "Invalid status code: $STATUS_CODE"
fi
