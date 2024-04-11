#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[2] - '0' !== Number) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.floor(process.argv[2]));
}
