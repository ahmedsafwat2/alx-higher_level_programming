#!/usr/bin/node

const process = require('process');
const args = process.argv;

const request = require('request');

const url = args[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  // Create an object to store the count of completed tasks for each userId
  const dct = {};

  // Loop through the data and count completed tasks for each user
  data.forEach((task) => {
    if (task.completed) {
    // If the task is completed, increment the count for the userId
      if (dct[task.userId]) {
        dct[task.userId]++;
      } else {
        dct[task.userId] = 1;
      }
    }
  });

  console.log(dct);
});
