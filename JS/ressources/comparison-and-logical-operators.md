# JAVASCRIPT - LOGICAL OPERATORS

<br>


## COMPARISON OPERATORS
> *[MDN - Comparison operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#Comparison)*

```js
let num = 3;

num == 3;		// true
num === '3';	// false
num > 3; 		//false
num >= 3;		//true
num < 3;		//false
num <= 3;		//true
num != 3;		//false
num !== '3';	//true
```
	

<br>

---

<br>


## LOGICAL OPERATORS
> *[MDN - Logical operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_Operators)*


**Examples**
```js
const a = 3;
const b = -2;

console.log(a > 0 && b > 0);
// expected output: false

console.log(a > 0 || b > 0);
// expected output: true

console.log(!(a > 0 || b > 0));
// expected output: false
```

<br>

**Operator precedence**
```js
true || false && false      // returns true, because && is executed first
(true || false) && false    // returns false, because operator precedence cannot apply
```

<br>

**Logical AND (&&)**
```js
a1 = true  && true       // t && t returns true
a2 = true  && false      // t && f returns false
a3 = false && true       // f && t returns false
a4 = false && (3 == 4)   // f && f returns false
a5 = 'Cat' && 'Dog'      // t && t returns "Dog"
a6 = false && 'Cat'      // f && t returns false
a7 = 'Cat' && false      // t && f returns false
a8 = ''    && false      // f && f returns ""
a9 = false && ''         // f && f returns false
```

<br>

**Logical OR (||)**
```js
o1 = true  || true       // t || t returns true
o2 = false || true       // f || t returns true
o3 = true  || false      // t || f returns true
o4 = false || (3 == 4)   // f || f returns false
o5 = 'Cat' || 'Dog'      // t || t returns "Cat"
o6 = false || 'Cat'      // f || t returns "Cat"
o7 = 'Cat' || false      // t || f returns "Cat"
o8 = ''    || false      // f || f returns false
o9 = false || ''         // f || f returns ""
o10 = false || varObject // f || object returns varObject
```

<br>

**Logical NOT (!)**
```js
n1 = !true               // !true returns false
n2 = !false              // !false returns true
n3 = !''                 // !false returns true
n4 = !'Cat'              // !true returns false
```

<br>

**Double NOT (!!)**
```js
n1 = !!true                   // !!truthy returns true
n2 = !!{}                     // !!truthy returns true: any object is truthy...
n3 = !!(new Boolean(false))   // ...even Boolean objects with a false .valueOf()!
n4 = !!false                  // !!falsy returns false
n5 = !!""                     // !!falsy returns false
n6 = !!Boolean(false)         // !!falsy returns false
```