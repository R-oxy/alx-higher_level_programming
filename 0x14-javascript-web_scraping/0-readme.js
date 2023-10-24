#!/usr/bin/node

// Import the 'fs' module for file operations
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the file using 'fs.readFile'
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurs
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
