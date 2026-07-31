#!/bin/bash
# sends a GET request, follows any redirects, and displays the body only if the final status is 200
[ "$(curl -s -L -o /tmp/1-body_output -w "%{http_code}" "$1")" = "200" ] && cat /tmp/1-body_output
