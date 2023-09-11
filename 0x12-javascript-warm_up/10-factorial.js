#!/usr/bin/node

function computeFactorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
}

const arg = parseInt(process.argv[2]);
const factorial = computeFactorial(arg);

console.log(factorial);
