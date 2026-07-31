#!/usr/bin/python3
"""Sends a request to a URL using urllib and prints the decoded body, or the HTTP error code on failure."""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as http_error:
        print("Error code: {}".format(http_error.code))
