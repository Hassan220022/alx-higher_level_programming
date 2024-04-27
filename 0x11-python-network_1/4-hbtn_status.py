#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    """ Fetch and display the body of the response from a URL """
    response = requests.get('https://alx-intranet.hbtn.io/status')

    content = response.text

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
