
let fName = prompt("Enter your first name:");
let lName = prompt("Enter your last name:");
let nickname = prompt("Enter your nickname:");

console.log(`Hello! My name is ${fName} ${lName}, but you can call me ${nickname}.`);

let fullName = `${fName} ${lName}`;
console.log(`Your full name has ${fullName.length} characters.`);


let heightCm = Number(prompt("Enter your height in cm:"));
let weightKg = Number(prompt("Enter your weight in kg:"));

let heightInches = (heightCm / 2.54).toFixed(2);
let weightLbs = (weightKg * 2.20462).toFixed(2);

console.log(`Your height in inches is ${heightInches}.`);
console.log(`Your weight in pounds is ${weightLbs}.`);

let randomNum = Math.floor(Math.random() * 3) + 1; 
let funFactValue = randomNum * 10;

console.log(`Fun Fact: Did you know ${funFactValue} is a cool number about me?`);

let careerGoal = prompt("What is one of your career goals?");
console.log(`One of my goals is ${careerGoal}.`);
console.log(`This goal has ${careerGoal.length} characters.`);

let birthYear = Number(prompt("What year were you born?"));
let currentYear = new Date().getFullYear();

let age = currentYear - birthYear;
let daysLived = age * 365;
                                                                                                  
console.log(`I am ${age} years old, and I’ve lived approximately ${daysLived} days so far.`);

let today = new Date();
let month = today.getMonth() + 1; 
let day = today.getDate();
let year = today.getFullYear();

let formattedDate = `${month}/${day}/${year}`;

let endOfYear = new Date(year, 11, 31); 
let diffTime = endOfYear - today;
let daysRemaining = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

console.log(`Today’s date is ${formattedDate}, and there are ${daysRemaining} days left in the year.`);