#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function load (character) {
  return new Promise((resolve, reject) => {
    request(character, function (error, response, body) {
      if (error) {
        reject(error);
      }

      resolve(JSON.parse(body).name);
    });
  });
}

request(url, async function (error, response, body) {
  if (error) {
    throw error;
  }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    try {
      const name = await load(character);
      console.log(name);
    } catch (error) {
      console.log(error);
    }
  }
});
