#!/usr/bin/node

const data = require('./100-data');

console.log(data.list);

const newList = data.list.map((value, index) => value * index);

console.log(newList);
