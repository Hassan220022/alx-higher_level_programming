#!/bin/usr/node
exports.callMeMoby = function (x, y) {
  for (let i = 0; i < x; i++) { y(); }
};
