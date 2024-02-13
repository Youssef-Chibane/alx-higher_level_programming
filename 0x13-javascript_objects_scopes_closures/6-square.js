#!/usr/bin/node
const Square_ = require('./5-square');

module.exports = class Square extends Square_ {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
