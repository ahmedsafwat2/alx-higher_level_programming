#!/usr/bin/node

const process = require('process');
const args = process.argv;

const request = require('request');

const url = args[2];
const characterId = '18';

let count = 0;

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  data.results.forEach((film) => {
    film.characters.forEach((charchter) => {
      if (charchter.includes(characterId)) {
        count += 1;
      }
    });
  });
  console.log(count);
});
