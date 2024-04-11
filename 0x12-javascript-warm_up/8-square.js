#!/usr/bin/node

const times = process.argv[2];
if (times === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < times; i++) {
    for (let i = 0; i < times; i++) {
      process.stdout.write('x');
    }
    console.log();
  }
}
