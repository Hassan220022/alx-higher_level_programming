#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) { super(size, size); }

  charPrint (character) {
    if (character === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(character.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
