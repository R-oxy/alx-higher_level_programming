#!/usr/bin/node

// Import the 'fs' module for file operations
const fs = require('fs');

// Get the file path and string to write from the command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the file using 'fs.writeFile'
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurs
    console.error(err);
  }
});
