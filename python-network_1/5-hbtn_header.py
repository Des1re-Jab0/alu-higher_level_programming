#!/usr/bin/python3
"""Sends a request to a URL using requests and displays the X-Request-Id response header."""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
