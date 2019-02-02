//const fetch = require('node-fetch');

// const promise = fetch('https://jsonplaceholder.typicode.com/todos/1');

// promise
//     .then(res => res.json())
//     .then(user => console.log('txt', user.title))

// console.log('Synchronous');

// const getFruit = async(name) => {
//     const fruits = {
//         pineapple: 'spongebob\'s house!',
//         peach: 'from mario',
//         strawberry: 'festival'
//     }
//     return fruits[name];
// };

// getFruit('peach').then(console.log);

const companies= [
    {name: "Company One", category: "Finance", start: 1981, end: 2003},
    {name: "Company Two", category: "Auto", start: 1981, end: 2003},
    {name: "Company Three", category: "Retail", start: 1981, end: 2003},
    {name: "Company Four", category: "Auto", start: 1981, end: 2003},
    {name: "Company Five", category: "Finance", start: 1981, end: 2013},
    {name: "Company Six", category: "Technology", start: 1999, end: 2013},
    {name: "Company Seven", category: "Finance", start: 1981, end: 2001},
    {name: "Company Eight", category: "Retail", start: 1999, end: 2013},
    {name: "Company Nine", category: "Finance", start: 1981, end: 2013},
    {name: "Company Ten", category: "Technology", start: 1999, end: 2013},

];

const ages = [32, 34, 67, 32, 23, 45, 24 ,24 ,535, 35, 5,3 ,4,43 ,6 ,64]

// For Each

// companies.forEach(function(company) {
//     console.log(company.name);
// });

const canDrink = ages.filter(function(age) {
    if(age>=21) {
        return true;
    };
});

const under35 = canDrink.filter(age => age<=35);

console.log(ages);
console.log(canDrink);
console.log(under35);

const retailCompanies = companies.filter(companies => companies.category === "Retail");

// retailCompanies.forEach(function(company) {
//     console.log(company);
// });

retailCompanies.forEach(company => console.log(company.name));

//MAP

const companyNames = companies.map(company =>  `${company.name} is a ${company.category} company!`);

companyNames.forEach(company => console.log(company));
