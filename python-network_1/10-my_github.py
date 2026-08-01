#!/usr/bin/python3
"""Displays the id of a user authenticated via the GitHub API."""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        "https://api.github.com/user", auth=(username, password))
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print(None)
