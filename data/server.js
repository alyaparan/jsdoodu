const express = require('express');
const formidable = require('formidable');
const fs = require('fs');
const cors = require('cors'); // Import the cors middleware
const app = express();
const port = 3001;

// Middleware to handle JSON parsing
app.use(express.json());

// Enable CORS for all origins
app.use(cors());

// Route for handling POST requests to upload JSON data
app.post('/upload', (req, res) => {
    const data = req.body;
    const filename = generateFilename(); // Function to generate filename

    // Convert data object to JSON string
    const jsonData = JSON.stringify(data, null, 2); // Pretty-print JSON

    // Save JSON data to file
    saveJSON(jsonData, filename);

    res.send('Data saved successfully.');
});

// Function to generate a filename based on date and time
const generateFilename = () => {
    const now = new Date();
    const date = now.toISOString().split('T')[0]; // Format: YYYY-MM-DD
    const time = now.toISOString().split('T')[1].split('.')[0]; // Format: HH:MM:SS
    return `data_${date}_${time}.json`;
};

// Function to save JSON data as a file
const saveJSON = (jsonData, filename) => {
    fs.writeFile(filename, jsonData, 'utf8', (err) => {
        if (err) throw err;
        console.log(`File ${filename} has been saved.`);
    });
};

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
