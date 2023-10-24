#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the URL
request.get(url, (error, response) => {
  if (error) {
    // Print the error object if an error occurs
    console.error(error);
  } else {
    // Print the status code
    console.log(`code: ${response.statusCode}`);
  }
});
