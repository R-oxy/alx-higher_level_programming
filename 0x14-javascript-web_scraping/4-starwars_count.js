#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeId = 18;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    for (const film of films) {
      for (const character of film.characters) {
        if (character.endsWith(`/${wedgeId}/`)) {
          count++;
          break;
        }
      }
    }

    console.log(count);
  }
});
