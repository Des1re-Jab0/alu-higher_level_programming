#!/bin/bash
# sends a GET request and displays the body only when the status code is 200
[ "$(curl -s -o /tmp/1-body_output -w "%{http_code}" "$1")" = "200" ] && cat /tmp/1-body_output
