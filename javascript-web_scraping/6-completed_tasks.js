#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasks = {};

  for (const task of tasks) {
    if (task.completed) {
      if (completedTasks[task.userId] === undefined) {
        completedTasks[task.userId] = 0;
      }

      completedTasks[task.userId]++;
    }
  }

  console.log(completedTasks);
});
