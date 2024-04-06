#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, res, body) {
  if (err) {
    return console.log(err);
  }

  fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) throw err;
  });
});
