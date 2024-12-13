const express = require('express');
const app = express();
const data = require('./data.json');

app.get('/api/data', (req, res) => {
    res.json(data);
});

const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
