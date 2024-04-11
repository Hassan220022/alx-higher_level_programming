#!/usr/bin/node

function fac (a) {
  if (isNaN(a)) return 1;

  if (a <= 1) { return 1; } else { return a * fac(a - 1); }
}
const a = parseInt(process.argv[2]);
console.log(fac(a));
