#!/bin/bash
# This script sends a request to a specific URL that triggers a "You got me!" response.
curl -sLX PUT "0.0.0.0:5000/catch_me" -H "Origin: HolbertonSchool" -d "user_id=98"
