const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const DATA_FILE = path.join(__dirname, 'appointments.json');

// Load existing data or create an empty array
let appointments = [];
if (fs.existsSync(DATA_FILE)) {
    appointments = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
}

const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url);
    
    // Handle API endpoints
    if (req.method === 'GET' && req.url === '/appointments') {
        res.writeHead(200, { 
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        });
        res.end(JSON.stringify(appointments));
    } 
    else if (req.method === 'POST' && req.url === '/book') {
        let body = '';

        req.on('data', chunk => { body += chunk.toString(); });
        req.on('end', () => {
            const data = JSON.parse(body);
            appointments.push(data);

            // Save to file
            fs.writeFileSync(DATA_FILE, JSON.stringify(appointments, null, 2));

            // Add CORS headers
            res.writeHead(201, { 
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            });
            res.end(JSON.stringify({ message: 'Appointment booked!', data }));
        });
    }
    // Add CORS preflight handler
    else if (req.method === 'OPTIONS') {
        res.writeHead(204, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        });
        res.end();
    }
    // Serve static files
    else {
        let filePath = path.join(__dirname, '../frontend', parsedUrl.pathname === '/' ? 'index.html' : parsedUrl.pathname);
        
        const extname = path.extname(filePath);
        let contentType = 'text/html';
        
        switch (extname) {
            case '.js':
                contentType = 'text/javascript';
                break;
            case '.css':
                contentType = 'text/css';
                break;
            case '.png':
                contentType = 'image/png';
                break;
        }
        
        fs.readFile(filePath, (error, content) => {
            if (error) {
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('File not found');
            } else {
                res.writeHead(200, { 'Content-Type': contentType });
                res.end(content);
            }
        });
    }
});

server.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});