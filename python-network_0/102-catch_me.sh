#!/bin/bash
# sends a PUT request and follows the redirect until the server returns "You got me!"
curl -s -L -X PUT "0.0.0.0:5000/catch_me"
