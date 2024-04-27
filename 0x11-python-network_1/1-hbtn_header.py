#!/usr/bin/python3
""" Import necessary modules from the standard library """
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)
