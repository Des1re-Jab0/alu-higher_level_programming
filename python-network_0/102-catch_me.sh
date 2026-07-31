#!/bin/bash
# follows the redirect chain on /catch_me until the server returns "You got me!"
curl -s -L "0.0.0.0:5000/catch_me"
