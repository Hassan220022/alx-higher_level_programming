#!/bin/bash
# This script sends a JSON POST request to a specified URL with data from a specified file.
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
