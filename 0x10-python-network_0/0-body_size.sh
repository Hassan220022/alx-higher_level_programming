#!/bin/bash
# This script sends a request to a specified URL and displays the size of the response body in bytes.
curl -s "$1" | wc -c
