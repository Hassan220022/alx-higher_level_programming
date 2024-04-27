#!/usr/bin/python3
""" Import necessary libraries """
import sys
import urllib.request


if __name__ == "__main__":
    # Extract URL from the command line argument
    url = sys.argv[1]
    
    """ Send a request to the specified URL and handle HTTP errors """
    try:
        # Attempt to open the URL and read the response
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
