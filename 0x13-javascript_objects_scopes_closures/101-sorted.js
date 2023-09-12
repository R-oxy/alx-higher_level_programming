#!/usr/bin/node
// computes a dictionary of user ids by occurrence

const { dict } = require('./101-data');

const userOccurrences = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (!userOccurrences[occurrence]) {
    userOccurrences[occurrence] = [];
  }

  userOccurrences[occurrence].push(userId);
}

console.log(userOccurrences);
