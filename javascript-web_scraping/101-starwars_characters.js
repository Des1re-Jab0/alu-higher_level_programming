#!/usr/bin/node

const request = require('request');

const movieUrl =
  'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;
  let index = 0;

  const getCharacter = () => {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.log(characterError);
        return;
      }

      const character = JSON.parse(characterBody);
      console.log(character.name);

      index++;
      getCharacter();
    });
  };

  getCharacter();
});
