#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  fs.writeFile(process.argv[3], body, 'utf-8', (writeError) => {
    if (writeError) {
      console.log(writeError);
    }
  });
});
