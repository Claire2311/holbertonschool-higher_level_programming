#!/usr/bin/node
const request = require("request");

request(process.env.url, function (error, response, body) {
  console.error("error:", error);
  console.log("statusCode:", response && response.statusCode);
  return body;
});
