#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const counter in dict) {
  if (newDict[dict[counter]] === undefined) {
    newDict[dict[counter]] = [];
  }
  newDict[dict[counter]].push(counter);
}
console.log(newDict);
