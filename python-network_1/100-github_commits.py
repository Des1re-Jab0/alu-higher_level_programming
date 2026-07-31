#!/usr/bin/python3
"""Lists the 10 most recent commits of a GitHub repository, newest first, using the GitHub API."""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author))
