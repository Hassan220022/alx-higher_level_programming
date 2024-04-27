#!/bin/bash
# Sends a GET request and displays the response body if the HTTP status is 200
curl -s -o response_body -w '%{http_code}' "$1" | [ $(cat) -eq 200 ] && cat response_body && rm response_body
