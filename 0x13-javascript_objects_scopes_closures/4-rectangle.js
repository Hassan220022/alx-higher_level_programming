#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    const bor3i = this.height;
    this.height = this.width;
    this.width = bor3i;
  }
}

module.exports = Rectangle;
