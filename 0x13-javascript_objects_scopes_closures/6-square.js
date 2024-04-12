#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) { super(size, size); }
  charPrint () {
    super.print();
  }

  charPrint (character) {
    if (character === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log(character.repeat(this.size));
      }
    }
  }
}

module.exports = Square;
