#!/usr/bin/node

const request = require("request");

request
  .get("https://swapi-api.hbtn.io/api/films/" + process.argv[2])
  .on("response", function (response) {
    console.log(response.title);
  });
