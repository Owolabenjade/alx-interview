#!/usr/bin/node

const request = require('request');

// Get movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Star Wars API base URL
const baseUrl = 'https://swapi-api.alx-tools.com/api';

// Function to make HTTP requests with promises
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`HTTP ${response.statusCode}: ${body}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

// Main function to fetch and display characters
async function getMovieCharacters(movieId) {
  try {
    // Fetch movie data
    const movieUrl = `${baseUrl}/films/${movieId}/`;
    const movieData = await makeRequest(movieUrl);
    
    // Get character URLs from the movie data
    const characterUrls = movieData.characters;
    
    // Fetch all character data in the same order
    for (const characterUrl of characterUrls) {
      const characterData = await makeRequest(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

// Execute the main function
getMovieCharacters(movieId);