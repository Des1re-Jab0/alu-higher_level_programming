#!/usr/bin/python3
"""Sends a POST request with an email using requests."""
import requests
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    response = requests.post(sys.argv[1], data={"email": email})
    print(response.text)
