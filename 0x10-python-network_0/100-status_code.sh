#!/bin/bash
# This script sends a request to a URL and displays the HTTP status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
