#!/usr/bin/node

const times = parseInt(process.argv[2]);
if (isNaN(times)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < times; i++) {
    console.log('X'.repeat(times));
  }
}
