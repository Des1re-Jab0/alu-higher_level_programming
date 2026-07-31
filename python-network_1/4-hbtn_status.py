#!/usr/bin/python3
"""Fetches the hbtn status endpoint using requests."""
import requests


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
