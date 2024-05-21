#!/usr/bin/node

const process = require('process');
const args = process.argv;

const fs = require('fs');
fs.writeFile(args[2], args[3], err => {
  if (err) {
    console.error(err);
  }
});

// console.log("num: " + args[2]);
