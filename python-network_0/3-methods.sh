#!/bin/bash
# displays all HTTP methods the server accepts for a given URL
curl -s -X OPTIONS -D - -o /dev/null "$1" | grep -i "^Allow:" | cut -d" " -f2-
