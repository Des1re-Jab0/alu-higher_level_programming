#!/usr/bin/python3
"""Sends a request to a URL using requests; prints the body, or the error code if status is 400 or above."""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
