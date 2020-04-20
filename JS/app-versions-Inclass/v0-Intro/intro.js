//Single line comment
/*
Multi
line
comment
*/

/**
 * DATA TYPES
 * All data types in JavaScript
 * ------------------------------------------
 */

/* STRINGS
---------------------------------*/
"I'm Sorin and glad to be"
'I\'am Sorin and maybe glad to be'

"Wrong string'

'<h1 class="bob" id="dada">I\'m Bob</h1>'


/* NUMBERS
---------------------------------*/
//integers
3
34
567856755555555
0
1

//decimals or floats
34.3

//negative numbers
-3 
-0.01


/* BOOLEANS
---------------------------------*/
true //also 1
false //also 0


/* NULL & UNDEFINED
---------------------------------*/
let bob = null;
let age;


/* OBJECTS
---------------------------------*/
//Array
["Bob", "Marc", "James"]

//Function
function myFunction() {
  return 'Something';
}

//Object
{
  "Name": 1,
  "Age": 52,
  "Country": "RO"
}


/**
 * VARIABLES
 * Variables are like boxes / containers
 * ------------------------------------------
 */
//let => when content will/can change
let name = "Marc";
let age = 39;

let person = name + age;

//const => when content must not change
const days = ["Monday", "Tuesday", "etc."];

//var => the old way, a global variable;
var bob = 3;

//RULES & CONVENTIONS (of naming variables)
let bob = 3; //GOOD practice
let BOB = 3; //bad practice
let Bob = 3; //bad practice

let 0bob = 3; //WRONG, starts with number
let bob the great = 3; //WRONG, have spaces
let aimé = 3; //WRONG, have special characters

//JS is case sensitive language
let bob = 3;
let BOB = 2; //not the same as bob !

//Long words and the Camel Case
let bob_the_great = 34; //could be like this
let bobthegreat = 34; //bad practice
let bobTheGreat = 34; //good practice, very used
