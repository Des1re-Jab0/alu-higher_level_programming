#!/bin/bash
# sends a GET request with a custom X-School-User-Id header and displays the body
curl -s -H "X-School-User-Id: 98" "$1"
