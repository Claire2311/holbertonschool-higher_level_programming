#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/', function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  const result = JSON.parse(body);

  let numChar = 0;

  for (i = 0; i < result.results.length; i++) {
    for (j = 0; j < result.results[i].characters.length; j++) {
      if (
        result.results[i].characters[j] ===
        'https://swapi-api.hbtn.io/api/people/18/'
      ) {
        numChar += 1;
      }
    }
  }
  console.log(numChar);
});
