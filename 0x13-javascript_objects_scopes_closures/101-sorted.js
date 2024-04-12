#!/usr/bin/node

const dict = require('./101-data').dict;

const occurrences = {};

for (const userId in dict) {
  const occurrencesCount = dict[userId];
  if (occurrences[occurrencesCount]) {
    occurrences[occurrencesCount].push(userId);
  } else {
    occurrences[occurrencesCount] = [userId];
  }
}

console.log(occurrences);
