#!/usr/bin/python3
"""Sends a request to a URL using urllib and displays the X-Request-Id response header."""
from urllib import request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
