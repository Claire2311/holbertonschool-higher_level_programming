#!/usr/bin/node

const request = require('request');

request(
  'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  function (err, res, body) {
    const result = JSON.parse(body);
    console.log(result.title);
  }
);
