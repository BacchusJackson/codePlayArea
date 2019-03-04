const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const cors = require('cors');
const passport = require('passport');
const mongoose = require('mongoose');
const config = require('./config/database');

//connect to the database in the database config file
mongoose.connect(config.database);

//on connected
mongoose.connection.on('connected', () => {
    console.log('connected to database ' + config.database)
})

//catch any errors
mongoose.connection.on('error', (err) => {
    console.log('database error: ' + err);
})

const app = express();

const users = require('./routes/users');

//sets the port to be used
const port = 3000;

//Allow cross origin requests
app.use(cors());

//Set static folder
app.use(express.static(path.join(__dirname, 'public')));

// body parser middleware
app.use(bodyParser.json());

// Passport Middleware
app.use(passport.initialize());
app.use(passport.session());

require('./config/passport')(passport);

//allows the app to use the users js file
app.use('/users', users);

//index route request handling
app.get('/', (req, res) => {
    res.send('invalid End Point');
});

//starts the server
app.listen( port, () => {
    console.log('server started on port ' + port)
})

