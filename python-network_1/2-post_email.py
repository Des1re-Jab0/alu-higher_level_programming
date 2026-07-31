#!/usr/bin/python3
"""Sends a POST request with an email parameter using urllib and prints the decoded body."""
from urllib import request, parse
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    data = parse.urlencode({"email": email}).encode("utf-8")
    with request.urlopen(sys.argv[1], data=data) as response:
        print(response.read().decode("utf-8"))
