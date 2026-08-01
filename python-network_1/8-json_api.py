#!/usr/bin/python3
"""Searches for a user by letter via the search_user endpoint."""
import requests
import sys


if __name__ == "__main__":
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    response = requests.post(
        "http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        json_body = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not json_body:
            print("No result")
        else:
            print("[{}] {}".format(
                json_body.get("id"), json_body.get("name")))
