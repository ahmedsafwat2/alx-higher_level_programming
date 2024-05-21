#!/usr/bin/node

const process = require('process');
const args = process.argv;

const request = require('request');

request(args[2], function (err, response) {
  if (err) {
    console.error(err);
  }
  console.log('code: ' + response.statusCode); // Print the response status code if a response was received
});
