#!/usr/bin/node

const process = require('process');
const args = process.argv;

const fs = require('fs');
fs.readFile(args[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

// console.log("num: " + args[2]);
