#!/usr/bin/node

const process = require('process');
const args = process.argv;

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
