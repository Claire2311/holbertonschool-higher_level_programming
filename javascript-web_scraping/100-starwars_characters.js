#!/usr/bin/node

const request = require('request');

request(
  'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  function (err, res, body) {
    if (err) {
      return console.log(err);
    }
    const result = JSON.parse(body);

    result.characters.forEach(function (url) {
      request(url, function (err, res, body) {
        if (err) {
          return console.log(err);
        }
        const result2 = JSON.parse(body);
        console.log(result2.name);
      });
    });
  }
);
