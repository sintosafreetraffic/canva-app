const express = require('express');
const cors = require('cors');

const app = express();
const PORT = 8080;

// ✅ CORS Configuration - Allow Canva's domain
const allowedOrigins = [
    'https://app-aaggg38zc5q.canva-apps.com',  // Canva App Origin
    'http://localhost:8080'  // Local development
];

app.use(cors({
    origin: allowedOrigins,
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    allowedHeaders: ['Content-Type', 'Authorization'],
    credentials: true
}));

app.get('/', (req, res) => {
    res.json({ message: "✅ CORS is working! Canva can communicate with the backend." });
});

app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}`);
});
