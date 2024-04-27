#!/usr/bin/python3
"""
Python script that fetches the X-Request-Id value from the response header
of a given URL
"""
import requests
import sys


if __name__ == "__main__":
    """ Fetch and display the value of the X-Request-Id header from a URL """
    url = sys.argv[1]
    response = requests.get(url)

    request_id = response.headers.get('X-Request-Id')

    print(request_id)
