#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    const printCharacters = async () => {
      for (const url of characters) {
        await new Promise((resolve, reject) => {
          request(url, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              const character = JSON.parse(body);
              console.log(character.name);
              resolve();
            }
          });
        });
      }
    };

    printCharacters();
  }
});
