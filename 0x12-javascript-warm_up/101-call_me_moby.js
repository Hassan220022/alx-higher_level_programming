#!/bin/usr/node
exports.callMeMoby = function callMeMoby (x, y) {
  for (let i = 0; i < x; i++) { y(); }
};
