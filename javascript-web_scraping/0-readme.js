#!/usr/bin/node
const request = require("request");

const url = process.env;

request(url, function (error, response, body) {
  console.error("error:", error);
  console.log("statusCode:", response && response.statusCode);
  return body;
});
