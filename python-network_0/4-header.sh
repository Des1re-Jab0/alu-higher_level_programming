#!/bin/bash
# sends a GET request with a custom X-Holberton-User-Id header and displays the body
curl -s -H "X-Holberton-User-Id: 98" "$1"
