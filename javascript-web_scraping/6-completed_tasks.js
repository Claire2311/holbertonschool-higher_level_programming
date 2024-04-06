#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    return console.log(err);
  }

  const result = JSON.parse(body);

  const numCompletedTasks = [];
  for (i = 0; i < result.length; i++) {
    if (result[i].completed) {
      numCompletedTasks.push(result[i].userId);
    }
  }

  const final = {};
  numCompletedTasks.forEach(function (x) {
    final[x] = (final[x] || 0) + 1;
  });
  console.log(final);
});
