#!/usr/bin/node

const process = require('process');
const args = process.argv;

const request = require('request');
const fs = require('fs');

const url = args[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  fs.writeFile(args[3], body, err => {
    if (err) {
      console.error(err);
    }
  });
});
