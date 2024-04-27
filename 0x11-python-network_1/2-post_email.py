#!/usr/bin/python3
""" Import necessary libraries """
import sys
import urllib.request
import urllib.parse


def send_post_request(url, email):
    """ Prepare data and send a POST request to the specified URL """
    # Encode the email data to be sent with POST
    data = urllib.parse.urlencode({'email': email}).encode()
    
    # Create a request object with the URL and data
    req = urllib.request.Request(url, data=data)
    
    # Open the URL and send the POST request
    with urllib.request.urlopen(req) as response:
        # Read and decode the response
        response_body = response.read().decode('utf-8')
        print(response_body)


if __name__ == "__main__":
    # Extract URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Call the function to send POST request
    send_post_request(url, email)
