#!/usr/bin/python3
""" Import necessary libraries """
import sys
import urllib.request
import urllib.parse


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    new_value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(new_value).encode()
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        val = response.read().decode('utf8')
    print(val)
