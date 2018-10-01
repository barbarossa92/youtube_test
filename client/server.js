const express = require('express');
var path    = require("path");


const app = express();

app.use(express.static('dist'));

app.get('/', (req, res) => res.sendFile(path.join(__dirname+'/dist/index.html')));

app.listen(8000, '0.0.0.0');
console.log("Running at Port 8000");