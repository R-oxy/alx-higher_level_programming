#!/usr/bin/node
// Class Rectangle that defines a rectangle

class Rectangle {
  constructor(w, h) {
      if ((w = parseInt(w)) > 0 && (h = parseInt(h)) > 0) {
	  this.width = w;
	  this.height = h;
      }
  }
}

module.exports = Rectangle;
