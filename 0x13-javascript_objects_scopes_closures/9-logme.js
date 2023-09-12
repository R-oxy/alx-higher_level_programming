#!/usr/bin/node
// Prints and logs number of calls

let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
