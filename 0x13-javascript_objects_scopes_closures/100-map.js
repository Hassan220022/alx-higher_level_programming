#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
newList = list.map((x, index) => x * index);
console.log(newList);
