#!/bin/bash
# sends a GET request with a custom X-HolbertonSchool-User-Id header and displays the body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
