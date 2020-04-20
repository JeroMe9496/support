# JAVASCRIPT - BUILT IN OBJECTS
Useful JavaScript built-in objects

<br>

## String()
Examples with **String** object

* **String.length()**<br>
	*Returns the length of the string. Example :*

  ```js
  let str = "Apples";
  str.length;
  ```

* **String.split()**<br>
	*Splits a String object into an array of strings by separating the string into substrings. Example :*

  ```js
  let str = "Apples";
  str.split(""); // A,p,p,l,e,s
  
  let str = "Apples are round, and apples are juicy.";
  str.split(" ", 3); // Apples,are,round,
  ```

* **String.toLowerCase()**<br>
	*Returns the calling string value converted to lower case. Example :*

  ```js
  let str = "Apples are round, and Apples are Juicy.";
  str.toLowerCase(); // apples are round, and apples are juicy.
  ```

* **String.toUpperCase()**<br>
	*Returns the calling string value converted to upper case. Example :*

  ```js
  let str = "Apples are round, and Apples are Juicy.";
  str.toUpperCase(); // APPLES ARE ROUND, AND APPLES ARE JUICY.
  ```

* **String.substr()**<br>
	*Returns the characters in a string beginning at the specified location through the specified number of characters. Example :*

  ```js
  let str = "Apples are round, and Apples are Juicy.";
  str.substr(1, 2)); // pp
  str.substr(-2, 2)); // y.
  ```

<br>

## Math() & Number()
Examples with **Math** and **Number** objects

* **Math.random()**<br>
	*Returns a random number between 0 and 1. Example :*

  ```js
  Math.random() * 50;
  ```

* **Math.floor()**<br>
	*Takes a decimal number, and rounds down to the nearest whole number. Example :*

	```js
  Math.floor(Math.random() * 50);
  ```
	
* **Math.ceil()**<br>
  *Round UP to closer integer*

	```js
  Math.ceil(43.8); //44
  ```

* **Math.floor()**<br>
  *Round DOWN to closer integer*

	```js
  Math.floor(43.8); //43
  ```

* **Number.isInteger()**<br>
  *Check if number is integer (no decimals)*

	```js
  Number.isInteger(2017) //true

  Number.isInteger(43.2) //false
  ```