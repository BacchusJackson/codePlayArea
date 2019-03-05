#Mean Stack Notes
These are the notes and steps for Mean Stack

What's included:
- Rest API using Node.js / Express
- Token Generation & Authentication
- CORS
- Mongoose Object Document Mapper (ODM)
- Angular 2 / Angular-CLI
- Angular Router, HTTP Module
- Angular2-JWT (handles tokens)
- Authitication Guard
- Angular Flash Message Module
- Compile & Deploy

#BACKEND
The backend consists of a node.js server to handle routing and a mongoDB database
##Install and Set up
1. Install NPM
2. Install Mongo DB
3. Add dependencies
    "express": "*",
    "mongoose": "*",
    "bcryptjs": "*",
    "cors": "*",
    "jsonwebtoken": "*",
    "body-parser": "*",
    "passport": "*",
    "passport-jwt": "*"
4. Add app.js file
    - const app = express();
5. Import dependencies with const express = require('express');
6. Const port = 3000;
7. add code to listen on the port
8. add code to handle requests and send resposes
9. use nodemon to auto refresh server

##Routes
There's a folder called routes with js files that handle requests to different 'pages'

###Example
const express = require('express');
const router = express.Router();

//register
router.get('/register', (req, res, next) => {
    res.send('REGISTER');
});

module.exports = router;

*don't forget to export the router object*

##MongoDB
We're using mongoDB for data storage.
in app.js make sure you build a connection using mongoose
The location configuration information is in a database.js file
1. mongoose.connect(config.database);
2. mongoose.connection.on('connected', () => {}
3. mongoose.connection.on('error', (err) => {}

###Models
models are how the objects are structured. is the models/ folder, there is a UserScheme = mongoose.Scheme({}); function

##Authentication
1. Get the user -> User.getUserByUserName(username, (err, user) =>{}
2. Compare input password (hashed) to hash in database
3. Create a token object with jwt.sign({data:user}, config.secret{
expiresIn: 604800 });
4. in the response, return the token and user object without password. 
    - The token has to be sent with the reponse

#Angular Frontend 
1. npm install -g angular-cli
2. The angular-cli.json file has all of the settings
    - Change the outDir to "../public
    - Once you build the app, Angular will compile your code from typescript and create the required frontend stuff in public
3. Navigate to the angular-src folder and do ng serve to launch the site
4. All development is done in the src/app/ directory
    - app.module.ts is where you list all of the components you create.
    -- put components in declarations: [];
    -- put modules in imports: [];
    -- put services in providers: [];
##Decorators
In Angular, your app.component.ts is where you build the pages. Using the decorator,
    @Component({
        selector: 'app-root',                       // HTML tag used to insert the component
        templateUrl: './app.component.html',        // This is the link to the html
        styleUrls: ['./app.component.css']          // Any styles to be applied to the page
    })
    export class AppComponent {
        title = 'app works!';                        // This will replace the {{title}} in the html
    }
##Components
Components are pieces of your application. Ex. Navbar

Create a folder src/app/components
    - you can generate components before manually creating them.

ng g component navbar
    - angular-cli generate component navbar

This will create a folder called navbar
    import { NavbarComponent } from './components/navbar/navbar.component';
    in @ngModule -> declarations: [AppComponent, NavbarComponent]
Angluar-cli auto adds the component to the app.module.ts file

To add this component to the page, add the selector to app.component.html
*Make sure you're in the src/app/components/ directory before use ng g component*

###Putting it Together
We created a bunch of components folders that can be edited to our liking
In the main index.html, we see <app-root>Loading...</app-root> that was the thing we replaced earlier

##Routes
instead of using a href in HTML, use [routerLink]="['/login']" or [routerLink]="['/']"

