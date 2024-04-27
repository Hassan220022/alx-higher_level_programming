#!/usr/bin/python3
import urllib.request

def fetch_status():
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))

if __name__ == "__main__":
    fetch_status()
