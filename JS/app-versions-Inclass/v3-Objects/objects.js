//A SIMPLE OBJECT
let simpleObject = {

  myNumber    : 35,
  myString    : "Lorem ipsum ipso facto",
  myArray     : [2,3,4,"Bla"],
  myFunction  : function () {
    return "Something from a function";
  },
  myObject    : {
    name : "Sorin Paun",
    country: "Romania" 
  }

};

// console.log( "My Object:", simpleObject );
// console.log( "My number:", simpleObject.myNumber );
// console.log( "My Array:", simpleObject.myArray );
// console.log( "My Array Index:", simpleObject.myArray[1] );

// console.log( "My Function:", simpleObject.myFunction() );

// console.log( "My Inside Object key:", simpleObject.myObject.name );
// console.log( "My Inside Object key:", simpleObject.myObject.country );


//MY PERSONS OBJECT
let persons = {

  person1 : {
    name: "Sorin Paun",
    gender: "Male",
    country: "Romania"
  },
  person2 : {
    name: "Marc Martel",
    gender: "Male",
    country: "Canada"
  },
  person3 : {
    name: "Véronique Paun",
    gender: "Female",
    country: "Switzerland"
  },

  person4 : ["Sorin Paun", "male", "RO"]

};

// console.log( persons.person1.name );
// console.log( persons.person1.gender );
// console.log( persons.person1.country );

// console.log( persons.person4[0] );
// console.log( persons.person4[1] );