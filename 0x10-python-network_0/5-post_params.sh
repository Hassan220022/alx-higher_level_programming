#!/bin/bash
# Sends a POST request with email and subject variables and displays the response body.
curl -s "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
