#!/bin/bash
# displays only the HTTP status code of the response, no pipes or redirection
curl -s -o /dev/null -w "%{http_code}" "$1"
