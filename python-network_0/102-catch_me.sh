#!/bin/bash
# follows a PUT redirect chain checking user_id and Origin to find the message
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "0.0.0.0:5000/catch_me"
