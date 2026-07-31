#!/usr/bin/python3
"""Fetches the ALU status endpoint using urllib and prints details about the response body."""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alu-intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
