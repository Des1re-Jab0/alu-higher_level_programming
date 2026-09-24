#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movies = JSON.parse(body).results;
  let count = 0;

  for (const movie of movies) {
    for (const character of movie.characters) {
      const characterUrl = character.replace(/\/$/, '');

      if (characterUrl.endsWith('/18')) {
        count++;
        break;
      }
    }
  }

  console.log(count);
});
