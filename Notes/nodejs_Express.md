#Node.JS and Express Tutorial
nvm is a package manager for node so you can install specific version of it
express is a framework

##Install and Setup
    $npm install express-generator -g
    - This install express-generator as a global package
    $express --view=pug myapp
    - This will build the folder structure
    - --view=pug means we're using pug as an html engine
###Install Dependencies
    $npm install
    - this will read the package.json file and install all dependencies for the app

###Folder Structure
    /public
    - All assets that are publically facing
    /routes
    - Handles requests
    /views
    - The pug templates for building the html
    /bin
    - Code for all of the compiling
    app.js
    - Entry point for the entire web application


