#!/usr/bin/python3
"""Fetches a URL and prints the body, or the HTTP error code."""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as http_error:
        print("Error code: {}".format(http_error.code))
