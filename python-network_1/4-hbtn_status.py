#!/usr/bin/python3
"""Fetches the ALU status endpoint using requests and prints details about the response body."""
import requests


if __name__ == "__main__":
    response = requests.get("https://alu-intranet.hbtn.io/status")
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
