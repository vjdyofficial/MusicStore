// Replace with your GitHub raw CSV file link
const url = 'https://github.com/vjdyofficial/MusicStore/blob/main/servertabs.csv?raw=true';
import fetch from 'node-fetch'; // Ensure you install node-fetch using npm
import Papa from 'papaparse'; // Ensure you install papaparse using npm

fetchCSVData(url);

async function fetchCSVData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const csvText = await response.text();
        const parsedData = Papa.parse(csvText, { header: true, skipEmptyLines: true });
        console.log(parsedData.data); // Logs an array of objects if `header: true`
        return parsedData.data;
    } catch (error) {
        console.error('Error fetching CSV data:', error);
    }
}