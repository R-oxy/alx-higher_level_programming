#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Define the API URL based on the Movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to fetch character name by URL
const getCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
};

// Main function to fetch movie details and then fetch each character name
const main = async () => {
  request(apiUrl, async (error, response, body) => {
    if (error) {
      console.error('error:', error);
    } else {
      const film = JSON.parse(body);
      const characters = film.characters;

      for (const url of characters) {
        const name = await getCharacterName(url);
        console.log(name);
      }
    }
  });
};

main();
