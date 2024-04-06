#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const result = JSON.parse(body);

  let numChar = 0;

  let i = 0;

  for (i; i < result.results.length; i++) {
    let j = 0;
    for (j; j < result.results[i].characters.length; j++) {
      if (result.results[i].characters[j].includes(18)) {
        numChar += 1;
      }
    }
  }
  console.log(numChar);
});
