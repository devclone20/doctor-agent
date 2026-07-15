# Javascript Roadmap

## 

# Value Comparison Operators

In javascript, the `==` operator does the type conversion of the operands before comparison, whereas the `===` operator compares the values and the data types of the operands. The `Object.is()` method determines whether two values are the same value: `Object.is(value1, value2)`.

`Object.is()` is not equivalent to the `==` operator. The `==` operator applies various coercions to both sides (if they are not the same type) before testing for equality (resulting in such behavior as `"" == false` being `true`), but `Object.is()` doesn't coerce either value.

`Object.is()` is also not equivalent to the `===` operator. The only difference between `Object.is()` and `===` is in their treatment of signed zeros and `NaN` values. The `===` operator (and the `==` operator) treats the number values `-0` and `+0` as equal but treats `NaN` as not equal to each other.

Visit the following resources to learn more:

- [@article@Equality comparisons and sameness - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness#same-value_equality_using_object.is)

## 

# Strict Equality Operator (===)

In JavaScript, the strict equality operator `===` compares both the value and the type of two operands. This means that it will only return true if both the value and the type are identical.

```sh
"5" === "5"   // true
```

In this case, both the value and the type are the same, so the result is true.

```sh
"5" === 5   // false
```

Here, although the values might appear similar, the types are different (string and number), so the result is false. The strict equality operator does not perform type coercion; both the value and the type must be identical.

Learn more from the following resources:

- [@article@Strict equality - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)

## All About Variables

# Javascript Variables

Most of the time, a JavaScript application needs to work with information. To store and represent this information in the JavaScript codebase, we use variables. A variable is a container for a value.

Visit the following resources to learn more:

- [@article@JavaScript Variables](https://javascript.info/variables)
- [@article@Storing the information you need — Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Apply

# apply

The apply() method of Function instances calls this function with a given this value, and arguments provided as an array (or an array-like object).

Visit the following resources to learn more:

- [@article@apply() - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)

## Arguments Object

# Arguments object

The arguments object is an Array-like object accessible inside functions that contains the values of the arguments passed to that function, available within all non-arrow functions. You can refer to a function's arguments inside that function by using its arguments object. It has entries for each argument the function was called with, with the first entry's index at 0. But, in modern code, rest parameters should be preferred.

Visit the following resources to learn more:

- [@article@The arguments object - MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)

## Arithmetic Operators

# Arithmetic operators

The Arithmetic operators perform addition, subtraction, multiplication, division, exponentiation, and remainder operations.

Arithmetic operators in JavaScript are as follows:

- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `**` (Exponentiation)
- `/` (Division)
- `%` (Modulus i.e. Remainder)
- `++` (Increment)
- `--` (Decrement)

Visit the following resources to learn more:

- [@article@Arithmetic Operators - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#arithmetic_operators)
- [@article@Arithmetic Operators - JavaScript.info](https://javascript.info/operators#maths)

## Arrays

# Arrays

Arrays are objects that store a collection of items and can be assigned to a variable. They have their methods that can perform operations on the array.

Visit the following resources to learn more:

- [@article@Working with Arrays in JavaScript](https://javascript.info/array)
- [@article@JavaScript Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [@video@JavaScript Arrays](https://www.youtube.com/watch?v=oigfaZ5ApsM)

## Arrow Functions

# Arrow Functions

Arrow Function is a new way of creating functions with the '=>' operator with a shorter syntax.

## Example

```js
const sayHello = () => {
    console.log(`Hello from Arrow Function !`);
}
```

Visit the following resources to learn more:

- [@article@MDN - Arrow Function Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

## Assignment Operators

# Assignment Operators

An assignment operator assigns a value to its left operand based on the value of its right operand. The simple assignment operator is equal (`=`), which assigns the value of its right operand to its left operand. That is, `x = f()` is an assignment expression that assigns the value of `f()` to `x`.

Visit the following resources to learn more:

- [@article@Assignment Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#assignment_operators)
- [@article@Basic Operators](https://javascript.info/operators#assignment)

## Asyncawait

# Async/Await

`async/await` is a special syntax to work with promises in a more comfortable fashion.
We use `async` keyword to declare a async function that return a Promise, and the `await` keyword makes a function wait for a Promise.

Visit the following resources to learn more:

- [@article@Async/await](https://javascript.info/async-await)
- [@article@async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [@article@JavaScript Promises - Chaining](https://www.codeguage.com/courses/advanced-js/promises-chaining)

## Asynchronous Javascript

# Asynchronous JavaScript

Asynchronous programming is a technique that enables your program to start a potentially long-running task and still be able to be responsive to other events while that task runs, rather than having to wait until that task has finished. Once that task has finished, your program is presented with the result.

Many functions provided by browsers, especially the most interesting ones, can potentially take a long time, and therefore, are asynchronous. For example:

- Making HTTP requests using `fetch()`
- Accessing a user's camera or microphone using `getUserMedia()`
- Asking a user to select files using `showOpenFilePicker()`

So even though you may not have to implement your own asynchronous functions very often, you are very likely to need to use them correctly.

Visit the following resources to learn more:

- [@article@Asynchronous JavaScript - MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing)
- [@video@What The Hack is Event Loop and Asynchronous JavaScript - JSConf](https://youtu.be/8aGhZQkoFbQ)
- [@video@Asynchronous JavaScript - JavaScript Visualized](https://youtu.be/eiC58R16hb8)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Bigint Operators

# BigInt Operators

Most operators that can be used with the `Number` data type will also work with `BigInt` values (e.g. arithmetic, comparison, etc.). However, the unsigned right shift `>>>` operator is an exception and is not supported. Similarly, some operators may have slight differences in behaviour (for example, division with `BigInt` will round towards zero).

Visit the following resources to learn more:

- [@article@BigInt Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#bigint_operators)

## Bigint

# bigint

BigInt is a built-in JavaScript object that allows you to work with integers of arbitrary size.

Unlike the Number type, which can accurately represent integers only within the range of ±2^53 , BigInt can handle integers far beyond this limit. This makes it particularly useful for applications requiring high precision with very large numbers, such as cryptography or scientific computations.

Visit the following resources to learn more:

- [@article@BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
- [@video@The Whys and Hows Of BigInt](https://youtu.be/6I650PQfhMg?si=XyVGrmp4KWLRcHVj)

## Bind

# bind()

The `bind()` method in JavaScript allows you to create a new function with a specific context and optionally preset arguments. Unlike `call()` or `apply()`, `bind()` does not immediately invoke the function. Instead, it returns a new function that can be called later, either as a regular function or with additional arguments. This is particularly useful when you want to ensure that a function retains a specific context, regardless of how or when it's invoked.

Visit the following resources to learn more:

- [@article@bind()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)
- [@article@Function binding](https://javascript.info/bind)

## Bitwise Operators

# Bitwise operators

Bitwise operators treat arguments as 32-bits (zeros & ones) and work on the level of their binary representation.
Ex. Decimal number `9` has a binary representation of `1001`. Bitwise operators perform their operations on such binary representations, but they return standard JavaScript numerical values.

Bitwise operators in JavaScript are as follows:

- `&` (AND)
- `|` (OR)
- `^` (XOR)
- `~` (NOT)
- `<<` (Left SHIFT)
- `>>` (Right SHIFT)
- `>>>` (Zero-Fill Right SHIFT)

Visit the following resources to learn more:

- [@article@Bitwise Operators - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#bitwise_operators)
- [@article@Bitwise Operators - JavaScript.info](https://javascript.info/operators#bitwise-operators)

## Block

# Block Scope

This scope restricts the variable that is declared inside a specific block, from access by the outside of the block. The let & const keyword facilitates the variables to be block scoped. In order to access the variables of that specific block, we need to create an object for it. Variables declared with the var keyword, do not have block scope.

Visit the following resources to learn more:

- [@article@JavaScript Scope](https://www.w3schools.com/js/js_scope.asp)

## Boolean

# boolean

In JavaScript, a `boolean` is a simple data type that can hold one of two values: `true` or `false`. These values are used to represent logical states and are essential in controlling the flow of a program.

Booleans are commonly used in conditional statements (`if`, `else`, `while`, etc.) to determine whether a block of code should execute.

Visit the following resources to learn more:

- [@article@JavaScript Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
- [@video@Booleans in JavaScript](https://www.youtube.com/watch?v=B4ZCFdrBmbE)

## Break  Continue

# Break continue

`break` statement, without a label reference, can only be used to jump out of a loop or a switch block.

`continue` statement, with or without a label reference, can only be used to skip one loop iteration.

Visit the following resources to learn more:

- [@article@JavaScript MDN Docs - continue statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
- [@article@JavaScript MDN Docs - break statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)

## Built In Functions

# Built in functions

JavaScript offers a variety of built-in functions that simplify common tasks, available globally or within specific objects without requiring explicit definition. Functions like parseInt(), setTimeout(), and Math.random() can be used directly, while objects like Array, String, and Date include built-in methods for efficient data manipulation. Understanding these functions enhances development by leveraging JavaScript’s core features without reinventing the wheel.

Visit the following resources to learn more:

- [@article@JavaScript Built-in Functions](https://www.tutorialspoint.com/javascript/javascript_builtin_functions.htm)
- [@article@Built-in Methods in Javascript](https://dev.to/elpepebenitez/built-in-methods-in-javascript-4bll)
- [@article@Built-in Functions:](https://www.tutorialride.com/javascript/javascript-built-in-functions.htm)

## Built In Objects

# Built-in objects

Built-in objects, or "global objects", are those built into the language specification itself. There are numerous built-in objects with the JavaScript language, all of which are accessible at the global scope. Some examples are:

- `Number`
- `Math`
- `Date`
- `String`
- `Error`
- `Function`
- `Boolean`

Visit the following resources to learn more:

- [@article@Standard built-in objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)
- [@article@JavaScript Built-in Objects](https://www.tutorialride.com/javascript/javascript-built-in-objects.htm)

## Call

# call()

The `call()` method allows you to invoke a function with a given `this` value, and arguments provided individually.

Visit the following resources to learn more:

- [@article@Call Method - MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)

## Callback Hell

# Callback Hell

The callback hell is when we try to write asynchronous JavaScript in a way where execution happens visually from top to bottom, creating a code that has a pyramid shape with many **})** at the end.

Visit the following resources to learn more:

- [@article@Callbacks in Callbacks - Pyramid of Doom](https://javascript.info/callbacks#pyramid-of-doom)

## Callbacks

# Callbacks

A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.

Visit the following resources to learn more:

- [@article@Callbacks in JavaScript](https://javascript.info/callbacks)
- [@article@Callback Functions](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)

## Classes

# Classes

Classes are a template for creating objects. They encapsulate data with code to work on that data. Classes in JS are built on prototypes but have some syntax and semantics that are not shared with ES5 class-like semantics.

Visit the following resources to learn more:

- [@article@Classes in JavaScript](https://javascript.info/classes)
- [@article@JavaScript Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Closures

# Closures

Function closures are one of the most powerful, yet most misunderstood, concepts of JavaScript that are actually really simple to understand. A closure refers to a function along with its lexical environment. It is essentially what allows us to return a function `A`, from another function `B`, that remembers the local variables defined in `B`, even after `B` exits. The idea of closures is employed in nearly every other JavaScript program, hence, it's paramount for a JavaScript developer to know it really well.

Visit the following resources to learn more:

- [@article@JavaScript Closures - The Simplest Explanation](https://www.codeguage.com/courses/js/functions-closures)
- [@article@JavaScript Closures Explained in 3 Minutes](https://medium.com/learning-new-stuff/javascript-closures-explained-in-3-minutes-5aae8dce2014)

## Comma Operators

# Comma operators

The comma operator (`,`) evaluates each of its operands (from left to right) and returns the value of the last operand. This lets you create a compound expression in which multiple expressions are evaluated, with the compound expression's final value being the value of the rightmost of its member expressions. This is commonly used to provide multiple parameters to a `for` loop.

Visit the following resources to learn more:

- [@article@Comma operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comma_Operator)

## Commonjs

# CommonJS

CommonJS modules are the original way to package JavaScript code for Node.js. Node.js also supports the ESModules standard used by browsers and other JavaScript run-times, but CJS is still widely used in backend Node.js applications. Sometimes these modules will be written with a .cjs extension.

Visit the following resources to learn more:

- [@article@How the CJS Module System Works](https://blog.risingstack.com/node-js-at-scale-module-system-commonjs-require/)
- [@video@How to Import and Export Modules in CJS](https://www.youtube.com/watch?v=XTND4rjATXA)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Comparison Operators

# Comparison Operators

Comparison operators are the operators that compare values and return true or false. The operators include: `>`, `<`, `>=`, `<=`, `==`, `===`, `!=` and `!==`

Visit the following resources to learn more:

- [@article@JavaScript MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#comparison_operators)

## Conditional Operators

# Conditional operators

Conditional operator also known as Ternary operator is the only JS operator that takes three operands.

The operator can have one of two values based on a condition.

Syntax:

`condition ? val_for_true : val_for_false`

Visit the following resources to learn more:

- [@article@JavaScript MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#conditional_operator)

## Conditional Statements

# Conditional statements

When you write code, you often want to perform different actions for different decisions. You can use conditional statements in your code to do this. In JavaScript, we have three conditional statements: `if`, `if...else`, and `switch`.

Visit the following resources to learn more:

- [@article@Making decisions in your code — conditionals](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals)
- [@article@Conditional branching: if, ?](https://javascript.info/ifelse)

## Const

# [const] keyword

Constants are block-scoped, much like variables declared using the `let` keyword. The value of a constant can't be changed through reassignment (i.e. by using the assignment operator), and it can't be re-declared (i.e. through a variable declaration). However, if a constant is an object or array its properties or items can be updated or removed.

Visit the following resources to learn more:

- [@article@JavaScript Constants - CodeGuage](https://www.codeguage.com/courses/js/constants)
- [@article@const keyword - MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
- [@article@JavaScript Variables](https://javascript.info/variables)

## Control Flow

# Control Flow

In JavaScript, the `Control flow` is a way of how your computer runs code from top to bottom. It starts from the first line and ends at the last line unless it hits any statement that changes the control flow of the program such as loops, conditionals, etc.

We can control the flow of the program through any of these control structures:

- Sequential (default mode)
- Conditional Statements
- Exception Handling
- Loops and Iterations

Visit the following resources to learn more:

- [@article@Control Flow - MDN](https://developer.mozilla.org/en-US/docs/Glossary/Control_flow)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Data Structures

# Data Structures

A Data structure is a format to organize, manage and store data in a way that allows efficient access and modification. JavaScript has primitive (built-in) and non-primitive (not built-in) data structures. Primitive data structures come by default with the programming language and you can implement them out of the box (like arrays and objects). Non-primitive data structures don't come by default and you have to code them up if you want to use them.

Visit the following resources to learn more:

- [@video@Introduction to the Stack Data Structure](https://youtu.be/4F-BnR2XwqU)
- [@video@Introduction to the Queue Data Structure](https://youtu.be/GRA_3Ppl2ZI)
- [@video@Intro to Recursion: Anatomy of a Recursive Solution](https://youtu.be/yBWlPte6FhA)
- [@video@Binary Tree Algorithms for Technical Interviews - Full Course](https://youtu.be/fAAZixBzIAI)
- [@video@Graph Algorithms for Technical Interviews - Full Course](https://youtu.be/tWVWeAqZ0WU)
- [@video@Dynamic Programming - Learn to Solve Algorithmic Problems & Coding Challenges](https://youtu.be/oBt53YbR9Kk)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Data Types

# Datatypes

Data type refers to the type of data that a JavaScript variable can hold. There are seven primitive data types in JavaScript (Number, BigInt, String, Boolean, Null, Undefined and Symbol). Objects are non-primitives.

Visit the following resources to learn more:

- [@article@JavaScript Data Types - CodeGuage](https://www.codeguage.com/courses/js/data-types)
- [@article@JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [@article@JavaScript Data Types](https://javascript.info/types)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Debugging Issues

# Debugging issues

When you're just starting out with JavaScript development, you might use a lot of `console.log()` statement in your code to log and check values of variables while debugging. The results of these would show up in the **Console** panel, along with a reference to the line and file of code which originated it.

However, for quicker, more complex and easier to handler debugging (which also doesn't litter your codebase with `console.log()`s), breakpoints and the sources panel is your friend.

Visit the following resources to learn more:

- [@article@Debugging JavaScript in the sources panel](https://developer.chrome.com/docs/devtools/javascript/)

## Debugging Memory Leaks

# Debugging Memory Leaks

In JavaScript, memory leaks commonly occur within heap allocated memory, where short lived objects are attached to long lived ones and the Garbage Collector cannot safely de-allocate that memory as it is still referenced from the root set (the global object).

Visit the following resources to learn more:

- [@article@Catching memory leaks with Chrome DevTools](https://medium.com/coding-blocks/catching-memory-leaks-with-chrome-devtools-57b03acb6bb9)
- [@article@Effective Javascript Debugging](https://medium.com/swlh/effective-javascript-debugging-memory-leaks-75059b2436f6)
- [@article@Debugging JavaScript memory leaks](https://www.debugbear.com/blog/debugging-javascript-memory-leaks)
- [@article@Debugging Memory Leaks In Production JavaScript Applications](https://www.jackhoy.com/web-applications/2020/10/21/debugging-memory-leaks-in-nodejs.html)
- [@video@JavaScript Memory Leaks Visualized and How To Fix Them](https://youtu.be/IkoGmbNJolo)

## Debugging Performance

# Debugging performance

Enter the dev tools and check out the Lighthouse tab. This is essentially a series of tests which analyses the currently open website on a bunch of metrics related to performance, page speed, accessibility, etc. Feel free to run the tests by clicking the **Analyze Page Load** button (you might want to do this in an incognito tab to avoid errors arising from extensions you're using). Once you have the results, take your time and read through them (and do click through to the reference pages mentioned alongside each test result to know more about it!)

Visit the following resources to learn more:

- [@article@Analyze runtime performance](https://developer.chrome.com/docs/devtools/performance)

## Default Params

# Default Parameters

Default function parameters allow named parameters to be initialized with default values if no value or `undefined` is passed.

Visit the following resources to learn more:

- [@article@Default Parameters - MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)

## Dom Apis

# DOM APIs

With HTML DOM, JavaScript can access and change all the elements of an HTML document such as its attributes, CSS styles, remove elements, add and create new elements on the page. Web API means application programming interface for the web. All browsers have a set of built-in Web APIs to support complex operations, and to help accessing data. Like Geo-location API, Web Storage, Web History and others.

Visit the following resources to learn more:

- [@article@DOM- MDN Docs](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

## Dowhile

# do...while statement

The `do...while` statement creates a loop that executes a specified statement until the test condition evaluates to `false`. The condition is evaluated after executing the statement, resulting in the specified statement executing at least once.

Visit the following resources to learn more:

- [@article@do...while - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while)

## Equality Comparisons

# Equality Comparisons

Comparison operators are used in logical statements to determine equality or difference between variables or values. Comparison operators can be used in conditional statements to compare values and take action depending on the result.

Visit the following resources to learn more:

- [@article@JavaScript Equality Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#equality_operators)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Error Objects

# Utilizing error objects

When a runtime error occurs, a new `Error` object is created and thrown. With this `Error` object, we can determine the type of the Error and handle it according to its type.

## Types of Errors

Besides error constructors, Javascript also has other core Error constructors. Like

- AggregateError - A collection of errors thrown simultaneously.
- EvalError - An error occurred during the evaluation of a JavaScript expression.
- InternalError - An internal JavaScript error, often indicating a bug in the engine.
- RangeError - A value is outside the allowed range for a given operation.
- ReferenceError - A variable or object is referenced before it's declared or doesn't exist.
- SyntaxError - The code contains incorrect syntax, preventing it from being parsed.

## Example

```js
try {
  willGiveErrorSometime();
} catch (error) {
  if (error instanceof RangeError) {
    rangeErrorHandler(error);
  } else if (error instanceof ReferenceError) {
    referenceErrorHandle(error);
  } else {
    errorHandler(error);
  }
}
```

Visit the following resources to learn more:

- [@article@Error Object - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
- [@article@Control flow & Error handling - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [@article@AggregateError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AggregateError)
- [@article@EvalError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/EvalError)
- [@article@InternalError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/InternalError)
- [@article@RangeError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
- [@article@ReferenceError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
- [@article@SyntaxError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

## Esm

# ESModules

ESModules is a standard that was introduced with ES6 (2015). The idea was to standardize how JS modules work and implement these features in browsers. This standard is widely used with frontend frameworks such as react and can also be used in the backend with Node.js. Sometimes these modules will be written with a .mjs extension.

Visit the following resources to learn more:

- [@article@Full ESM module overview from MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
- [@article@Full ESM module overview from js.info](https://javascript.info/modules)
- [@article@Node.js documentation for ESModules](https://nodejs.org/api/esm.html)
- [@video@JavaScript ES6 Modules Simplified](https://www.youtube.com/watch?v=cRHQNNcYf6s)

## Event Loop

# Event Loop

The Event Loop is one of the most important aspects to understand about Node.js. Why is this so important? Because it explains how Node.js can be asynchronous and have non-blocking I/O, it explains the "killer feature" of Node.js, which made it this successful.

Visit the following resources to learn more:

- [@article@The Node.Js Event Loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#what-is-the-event-loop)
- [@article@JavaScript Visualized: Event Loop](https://dev.to/lydiahallie/javascript-visualized-event-loop-3dif)
- [@video@What the heck is the event loop anyway?](https://www.youtube.com/watch?v=8aGhZQkoFbQ)
- [@video@In the loop: JS conf 2018](https://www.youtube.com/watch?v=cCOL7MC4Pl0)

## Exceptional Handling

# Exception Handling

In JavaScript, all exceptions are simply objects. While the majority of exceptions are implementations of the global Error class, any old object can be thrown. With this in mind, there are two ways to throw an exception: directly via an Error object, and through a custom object. (excerpt from Rollbar)

Visit the following resources to learn more:

- [@article@Throwing Exceptions in JavaScript](https://rollbar.com/guides/javascript/how-to-throw-exceptions-in-javascript)
- [@video@try, catch, finally, throw (video)](https://youtu.be/cFTFtuEQ-10)

## Explicit Binding

# Explicit binding

Explicit binding is when you use the `call` or `apply` methods to explicitly set the value of `this` in a function. Explicit Binding can be applied using `call()`, `apply()`, and `bind()`.

Visit the following resources to learn more:

- [@article@Explicit Binding](https://medium.com/swlh/javascript-this-ac28f8e0f65d)
- [@article@Explicit Binding rule for this keyword](https://medium.com/@msinha2801/explicit-binding-rule-for-this-keyword-in-js-712405b0a11)

## Explicit Type Casting

# Explicit Type Casting

Type casting means transferring data from one data type to another by explicitly specifying the type to convert the given data to. Explicit type casting is normally done to make data compatible with other variables. Examples of typecasting methods are `parseInt()`, `parseFloat()`, `toString()`.

Visit the following resources to learn more:

- [@article@Type Conversion](https://www.c-sharpcorner.com/article/type-conversions-in-javascript/)
- [@video@Data Type Conversion](https://youtu.be/VQLYiFqetZM)
- [@article@Type conversion](https://developer.mozilla.org/en-US/docs/Glossary/Type_Conversion)
- [@article@What is typecasting in JavaScript](https://www.tutorialspoint.com/explain-typecasting-in-javascript)

## Expressions  Operators

# Expressions and Operators

At a high level, an expression is a valid unit of code that resolves to a value. There are two types of expressions: those that have side effects (such as assigning values) and those that purely evaluate. The expression `x = 7` is an example of the first type. This expression uses the `=` operator to assign the value seven to the variable x. The expression itself evaluates to 7. The expression `3 + 4` is an example of the second type. This expression uses the `+` operator to add `3` and `4` together and produces a value, `7`. However, if it's not eventually part of a bigger construct (for example, a variable declaration like `const z = 3 + 4`), its result will be immediately discarded `—` this is usually a programmer mistake because the evaluation doesn't produce any effects. As the examples above also illustrate, all complex expressions are joined by operators, such as `=` and `+`.

Visit the following resources to learn more:

- [@article@Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Fetch

# Fetch

The `fetch()` method in JavaScript is used to request to the server and load the information on the webpages. The request can be of any APIs that return the data of the format JSON or XML. This method returns a promise.

Visit the following resources to learn more:

- [@article@Fetch MDN Docs](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [@article@Network request - Fetch](https://javascript.info/fetch)
- [@article@Abort a fetch request manually in JavaScript](https://www.amitmerchant.com/abort-fetch-request-manually-in-javascript/)

## For

# The for loop

The `for` loop is a standard control-flow construct in many programming languages, including JavaScript. It's commonly used to iterate over given sequences or iterate a known number of times and execute a piece of code for each iteration.

Visit the following resources to learn more:

- [@article@JavaScript for Loop - CodeGuage](https://www.codeguage.com/courses/js/loops-for-loop)
- [@article@The for Loop - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)

## Forin Loop

# for...in statement

The for...in statement iterates over all enumerable properties of an object that are keyed by strings (ignoring ones keyed by Symbols), including inherited enumerable properties.

Visit the following resources to learn more:

- [@article@for...in statement - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)
- [@article@The for..in loop with examples](https://javascript.info/object#forin)

## Forof Loop

# for...of statement

The for...of statement executes a loop that operates on a sequence of values sourced from an iterable object. Iterable objects include instances of built-ins such as Array, String, TypedArray, Map, Set, NodeList (and other DOM collections), and the arguments object, generators produced by generator functions, and user-defined iterables.

Visit the following resources to learn more:

- [@article@for...of statement - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)

## Function Borrowing

# Function Borrowing

Function borrowing allows us to use the methods of one object on a different object without having to make a copy of that method and maintain it in two separate places. It is accomplished through the use of `.call()`, `.apply()`, or `.bind()`, all of which exist to explicitly set this on the method we are borrowing.

Visit the following resources to learn more:

- [@article@Function borrowing](https://medium.com/@ensallee/function-borrowing-in-javascript-4bd671e9d7b4)
- [@article@When would I use function borrowing](https://stackoverflow.com/questions/69892281/when-would-i-use-function-borrowing)

## Function Parameters

# Function Parameters

The parameter is the name given to the variable declared inside the definition of a function. There are two special kinds of syntax: default and rest parameters.

Visit the following resources to learn more:

- [@article@Function Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#function_parameters)
- [@article@Unlimited function parameters using Rest](https://www.amitmerchant.com/unlimited-function-parameters-with-using-rest-in-java-script/)

## Function

# Function Scope

When a variable is declared inside a function, it is only accessible within that function and cannot be used outside that function.

Visit the following resources to learn more:

- [@article@Function Scope & Block Scope in JS](https://medium.com/nerd-for-tech/function-scope-block-scope-in-js-d29c8e7cd216)

## Functions

# Functions

Functions exist so we can reuse code. They are blocks of code that execute whenever they are invoked. Each function is typically written to perform a particular task, like an addition function used to find the sum of two or more numbers. When numbers need to be added anywhere within your code, the addition function can be invoked as many times as necessary.

Visit the following resources to learn more:

- [@article@Functions - MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
- [@article@JavaScript Functions in Detail - CodeGuage](https://www.codeguage.com/courses/js/functions-basics)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Garbage Collection

# Garbage Collection

Memory management in JavaScript is performed automatically and invisibly to us. We create primitives, objects, functions… All that takes memory. The main concept of memory management in JavaScript is reachability.

Visit the following resources to learn more:

- [@article@JavaScript Garbage Collection](https://javascript.info/garbage-collection)
- [@article@Memory Management in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)

## Global

# Global Scope

Variables declared Globally (outside any function) have Global Scope. Global variables can be accessed from anywhere in a JavaScript program. Variables declared with `var`, `let` and `const` are quite similar when declared outside a block.

## Note

If you assign a value to a variable  that has not been declared i.e `potato = true`
it will automatically become a _GLOBAL_ variable.

Visit the following resources to learn more:

## History Of Javascript

# History of JavaScript

JavaScript was initially created by Brendan Eich of NetScape and was first announced in a press release by Netscape in 1995. It has a bizarre history of naming; initially, it was named Mocha by the creator, which was later renamed LiveScript. In 1996, about a year later after the release, NetScape decided to rename it to JavaScript with hopes of capitalizing on the Java community (although JavaScript did not have any relationship with Java) and released Netscape 2.0 with the official support of JavaScript.

Visit the following resources to learn more:

- [@roadmap.sh@Brief History of JavaScript](https://roadmap.sh/guides/history-of-javascript)
- [@article@The Weird History of JavaScript](https://dev.to/codediodeio/the-weird-history-of-javascript-2bnb)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Hoisting

# Hoisting

JavaScript Hoisting refers to the process whereby the interpreter appears to move the declaration of functions, variables, or classes to the top of their scope, prior to execution of the code.

Visit the following resources to learn more:

- [@article@What is Hoisting - MDN Docs](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)
- [@article@Understanding Hoisting](https://www.digitalocean.com/community/tutorials/understanding-hoisting-in-javascript)
- [@video@Learn JavaScript Hoisting In 5 Minutes](https://www.youtube.com/watch?v=EvfRXyKa_GI)

## How To Run Javascript

# How to Run Javascript

JavaScript can be run in the browser by including the external script file using the `script` tag, writing it within the HTML page using the `script` tag again, running it in the browser console or you can also use [REPL](https://www.digitalocean.com/community/tutorials/how-to-use-the-node-js-repl).

Visit the following resources to learn more:

- [@article@How To Add JavaScript to HTML](https://www.digitalocean.com/community/tutorials/how-to-add-javascript-to-html)
- [@article@How To Write Your First JavaScript Program](https://www.digitalocean.com/community/tutorials/how-to-write-your-first-javascript-program)
- [@article@How To Use the JavaScript Developer Console](https://www.digitalocean.com/community/tutorials/how-to-use-the-javascript-developer-console)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Ifelse

# If else

The `if` statement executes a statement if a specified condition is `truthy`. If the condition is `falsy`, another statement in the optional `else` clause will be executed.

## Example

```js
if (condition) {
  statement1;
} else {
  statement2;
}
```

Visit the following resources to learn more:

- [@article@if...else - MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
- [@article@Conditional branching: if, ? - javascript.info](https://javascript.info/ifelse)

## Iifes

# IIFE

Immediately-Invoked Function Expression is a function that is executed immediately after it is created.

## Example

```js
// An Async IIFE
( async() => {
    
    const x = 1;
    const y = 9;

    console.log(`Hello, The Answer is ${x+y}`);

})();
```

Visit the following resources to learn more:

- [@article@IIFE — MDN Docs](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
- [@article@JavaScript in Plain English - IIFE](https://javascript.plainenglish.io/https-medium-com-javascript-in-plain-english-stop-feeling-iffy-about-using-an-iife-7b0292aba174)

## Implicit Type Casting

# Implicit Type Casting

Implicit type conversion happens when the compiler or runtime automatically converts data types. JavaScript is loosely typed language and most of the time operators automatically convert a value to the right type.

Visit the following resources to learn more:

- [@article@TutorialsPoint - JavaScript Tutorials](https://www.tutorialspoint.com/explain-typecasting-in-javascript)
- [@article@What you need to know about JavaScript Implicit Coercion](https://dev.to/promisetochi/what-you-need-to-know-about-javascripts-implicit-coercion-e23)

## In A Function

# this in a function

The keyword `this` when used in a function refers to the global object.

_Note: in a browser window the global object is the `window` object._

Visit the following resources to learn more:

## In A Method

# this in a method

Methods are properties of an object which are functions. The value of this inside a method is equal to the calling object. In simple words, this value is the object “before dot”, the one used to call the method.

Visit the following resources to learn more:

- [@article@`this` in methods](https://javascript.info/object-methods#this-in-methods)

## In Arrow Functions

# this in arrow functions

The keyword `this` when used in an arrow function refers to the parent object.

Visit the following resources to learn more:

- [@article@this keyword and arrow function](https://stackoverflow.com/questions/66518020/javascript-this-keyword-and-arrow-function)

## In Event Handlers

# this in event handlers

The keyword `this` when used in an event handler refers to the element that received the event.

Visit the following resources to learn more:

## Indexed Collections

# Indexed collections

Indexed Collections are collections that have numeric indices i.e. the collections of data that are ordered by an index value. In JavaScript, an array is an indexed collection. An array is an ordered set of values that has a numeric index.

Visit the following resources to learn more:

- [@article@What is Indexed collections?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Indexed_collections)
- [@article@Indexed collections in JavaScript](https://www.tutorialspoint.com/indexed-collections-in-javascript)
- [@video@Javascript Arrays](https://youtu.be/XYq9QpgAx8g)

## Introduction To Javascript

# JavaScript

JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS. It lets us add interactivity to pages e.g. you might have seen sliders, alerts, click interactions, popups, etc on different websites -- all of that is built using JavaScript. Apart from being used in the browser, it is also used in other non-browser environments as well such as Node.js for writing server-side code in JavaScript, Electron for writing desktop applications, React Native for mobile applications, and so on.

Visit the following resources to learn more:

- [@article@JavaScript MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [@article@The Modern JavaScript Tutorial](https://javascript.info/)
- [@article@Exploring JS: JavaScript books for programmers](https://exploringjs.com/)
- [@article@Eloquent JavaScript textbook](https://eloquentjavascript.net/)
- [@opensource@You Don't Know JS Yet (book series)](https://github.com/getify/You-Dont-Know-JS)
- [@video@JavaScript Crash Course for Beginners](https://youtu.be/hdI2bqOjy3c?t=2)
- [@video@Build a Netflix Landing Page Clone with HTML, CSS & JS](https://youtu.be/P7t13SGytRk?t=22)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Islooselyequal

# isLooselyEqual

[isLooselyEqual](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality) checks whether its two operands are equal, returning a `Boolean` result. It attempts to convert and compare operands that are of different types.

Visit the following resources to learn more:

- [@article@Loosely Equality (==) Operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality)
- [@article@Comparison - javascript.info](https://javascript.info/comparison)

## Isstrictlyequal

# isStrictlyEqual

[isStrictlyEqual](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality) checks whether its two operands are equal, returning a `Boolean` result. It always considers operands of different types to be different.

Visit the following resources to learn more:

- [@article@Strictly Equality (===) Operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)
- [@article@Comparison - javascript.info](https://javascript.info/comparison)

## Iterators And Generators

# Javascript Iterators and Generators

Iterators and generators, introduced into JavaScript with ECMAScript 6, represent an extremely useful concept related to iteration in the language. Iterators are objects, abiding by the iterator protocol, that allows us to easily iterate over a given sequence in various ways, such as using the `for...of` loop. Generators, on the other hand, allow us to use functions and the `yield` keyword to easily define iterable sequences that are iterators as well.

Visit the following resources to learn more:

- [@article@Introduction to Iterators - Advanced JavaScript](https://www.codeguage.com/courses/advanced-js/iteration-introduction)
- [@article@A Detailed Discussion on Iterators - Advanced JavaScript](https://www.codeguage.com/courses/advanced-js/iteration-iterators)
- [@article@What Exactly Are Generators? - Advanced JavaScript](https://www.codeguage.com/courses/advanced-js/iteration-generators)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Javascript Versions

# Javascript Versions

JavaScript, invented by Brendan Eich, achieved the status of an ECMA standard in 1997 and adopted the official name ECMAScript. This language has evolved through several versions, namely ES1, ES2, ES3, ES5, and the transformative ES6. These updates have played a crucial role in improving and standardizing JavaScript, making it widely used and valuable in the ever-changing field of web development.

Visit the following resources to learn more:

- [@article@JavaScript Versions: How JavaScript has changed over the years](https://www.educative.io/blog/javascript-versions-history)
- [@roadmap.sh@Brief History of JavaScript](https://roadmap.sh/guides/history-of-javascript)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Json

# JSON

JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax. It is commonly used for transmitting data in web applications (e.g., sending some data from the server to the client, so it can be displayed on a web page, or vice versa).

Visit the following resources to learn more:

- [@article@Working with JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [@video@JSON Tutorial for Beginners](https://www.youtube.com/watch?v=iiADhChRriM)

## Keyed Collections

# Keyed Collections

Keyed collections are data collections that are ordered by key not index. They are associative in nature. Map and set objects are keyed collections and are iterable in the order of insertion.

Visit the following resources to learn more:

- [@article@Keyed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections)
- [@article@ES6 keyed collections- Maps and sets](https://blog.logrocket.com/es6-keyed-collections-maps-and-sets/)
- [@video@Creating keyed collection](https://youtu.be/4UqSqF4foy4)

## Let

# [let] keyword

The `let` declaration declares a block-scoped local variable, optionally initializing it to a value.

Visit the following resources to learn more:

- [@article@let keyword - MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
- [@article@JavaScript Variables](https://javascript.info/variables)

## Lexical Scoping

# Lexical scoping

Before one can make an intuition of closures in JavaScript, it's important to first get the hang of the term '**_lexical environment_**'. In simple words, the lexical environment for a function `f` simply refers to the environment enclosing that function's definition in the source code.

Visit the following resources to learn more:

- [@article@What is a lexical environment? - JavaScript - CodeGuage](https://www.codeguage.com/courses/js/functions-closures#What_is_a_lexical_environment)
- [@article@Lexical scoping - JavaScript - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures#lexical_scoping)

## Logical Operators

# Logical Operators

There are four logical operators in JavaScript: `||` (OR), `&&` (AND), `!` (NOT), `??` (Nullish Coalescing).

Visit the following resources to learn more:

- [@article@Logical Operators - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#binary_logical_operators)

## Loops And Iterations

# Loops and Iterations

Loops offer a quick and easy way to do something repeatedly.

You can think of a loop as a computerized version of the game where you tell someone to take X steps in one direction, then Y steps in another. For example, the idea "Go five steps to the east" could be expressed this way as a loop:

```js
for (let step = 0; step < 5; step++) {
  // Runs 5 times, with values of step 0 through 4.
  console.log('Walking east one step');
}
```

Visit the following resources to learn more:

- [@article@Loops and iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Map

# Map

[Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) is a collection of keyed data items, just like an `Object`. But the main difference is that `Map` allows keys of any type.

Visit the following resources to learn more:

- [@article@Map - Keyed Collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [@article@Map Data Type](https://javascript.info/map-set#map)

## Memory Lifecycle

# Memory lifecycle

Regardless of the programming language, the memory life cycle is pretty much always the same:

- Allocate the memory you need
- Use the allocated memory (read, write)
- Release the allocated memory when it is not needed anymore

The second part is explicit in all languages. The first and last parts are explicit in low-level languages but are mostly implicit in high-level languages like JavaScript.

Visit the following resources to learn more:

- [@article@MDN docs - Memory Management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)
- [@article@Lifecycle in Memory Management](https://medium.com/swlh/the-lifecycle-of-memory-in-javascript-5b5bffc5ff4c)

## Memory Management

# Memory Management

Low-level languages like C, have manual memory management primitives such as `malloc()` and `free()`. In contrast, JavaScript automatically allocates memory when objects are created and frees it when they are not used anymore (garbage collection). This automaticity is a potential source of confusion: it can give developers the false impression that they don't need to worry about memory management.

Visit the following resources to learn more:

- [@article@JavaScript Garbage Collection](https://javascript.info/garbage-collection)
- [@article@Memory Management in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Modules In Javascript

# Modules

Modules encapsulate all sorts of code like functions and variables and expose all this to other files. Generally, we use it to break our code into separate files to make it more maintainable. They were introduced into JavaScript with ECMAScript 6.

Visit the following resources to learn more:

- [@article@Modules, introduction](https://javascript.info/modules-intro)
- [@article@Export and Import](https://javascript.info/import-export)
- [@article@Dynamic imports](https://javascript.info/modules-dynamic-imports)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Null

# null

The `null` value in JavaScript signifies the deliberate absence of any object value. It is considered as one of JavaScript's primitive values and a `falsy` value.

*Deliberate absence* emphasises the intentional use of `null` to indicate that a variable does not point to any object. This explicit declaration conveys the purposeful nature of null, showing that the variable is meant to be empty or non-existent at execution time.

In essence, `null` is a way to reset a variable, signalling that it should not reference any object.

Visit the following resources to learn more:

- [@article@What is null in JavaScript](https://www.altcademy.com/blog/what-is-null-in-javascript/)
- [@article@null in JavaScript](https://masteringjs.io/tutorials/fundamentals/null)

## Number

# number

The `Number` data type in JavaScript represents floating-point numbers, such as 37 or -9.25. The `Number` constructor provides constants and methods to work with numbers, and values of other types can be converted to numbers using the `Number()` function.

## Example

```js
let num1 = 255; // integer
let num2 = 255.0; // floating-point number with no fractional part
let num3 = 0xff; // hexadecimal notation
let num4 = 0b11111111; // binary notation
let num5 = 0.255e3; // exponential notation

console.log(num1 === num2); // true
console.log(num1 === num3); // true
console.log(num1 === num4); // true
console.log(num1 === num5); // true
```

In this example:

- `255` and `255.0` are equivalent, as JavaScript treats both as the same number.
- `0xff` represents `255` in hexadecimal notation.
- `0b11111111` represents `255` in binary notation.
- `0.255e3` is `255` in exponential notation.
- All these different representations are equal to `255` in JavaScript.

## Object Prototype

# Prototypes

JavaScript is an object-oriented language built around a prototype model. In JavaScript, every object inherits properties from its prototype, if there are any. A prototype is simply an object from which another object inherits properties. To create complex programs using JavaScript, one has to be proficient in working with prototypes — they form the very core of OOP in the language.

Visit the following resources to learn more:

- [@article@Prototypes in JavaScript - A Comprehensive Guide](https://www.codeguage.com/courses/js/objects-prototypes)
- [@article@Prototypes, Inheritance](https://javascript.info/prototypes)
- [@article@Object prototypes - MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
- [@video@Prototype in Javascript - Object Prototype](https://www.youtube.com/watch?v=583MGxjypgU)

## Object

# Object

JavaScript object is a data structure that allows us to have key-value pairs; so we can have distinct keys and each key is mapped to a value that can be of any JavaScript data type. Comparing it to a real-world object, a pen is an object with several properties such as color, design, the material it is made of, etc. In the same way, JavaScript objects can have properties that define their characteristics.

Visit the following resources to learn more:

- [@article@Objects](https://javascript.info/object)
- [@article@Working with Objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects)

## Objectis

# Object.is

The Object.is() static method determines whether two values are the same value.

```js
console.log(Object.is('1', 1));
// Expected output: false

console.log(Object.is(NaN, NaN));
// Expected output: true

console.log(Object.is(-0, 0));
// Expected output: false

const obj = {};
console.log(Object.is(obj, {}));
// Expected output: false
```

Visit the following resources to learn more:

- [@article@Object.is() - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/is)

## Promises

# Promises

Promises are a much better way to work with asynchronous code in JavaScript than the old and error-prone callback approach. They were introduced into JavaScript with ECMAScript 6. Using promises, we can manage extremely complex asynchronous code with rigorous error-handling setup, write code in a more or less synchronous style, and keep ourselves from running into the so-called callback hell.

Visit the following resources to learn more:

- [@article@A Detailed Introduction to Promises](https://www.codeguage.com/courses/advanced-js/promises-introduction)
- [@article@JavaScript Promises - Basics](https://www.codeguage.com/courses/advanced-js/promises-basics)
- [@article@JavaScript Promises - Chaining](https://www.codeguage.com/courses/advanced-js/promises-chaining)
- [@article@JavaScript Promises - Error Handling](https://www.codeguage.com/courses/advanced-js/promises-error-handling)
- [@video@JavaScript Promises - Visualized](https://youtu.be/Xs1EMmBLpn4)

## Prototypal Inheritance

# Prototypal Inheritance

The Prototypal Inheritance is a feature in javascript used to add methods and properties in objects. It is a method by which an object can inherit the properties and methods of another object. Traditionally, in order to get and set the Prototype of an object, we use Object.getPrototypeOf and Object.setPrototypeOf.

Visit the following resources to learn more:

- [@article@JavaScript MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)
- [@article@Prototype Inheritance](https://javascript.info/prototype-inheritance)

## Recursion

# Recursion

One of the most powerful and elegant concept of functions, recursion is when a function invokes itself. Such a function is called a **_recursive function_**. As recursion happens, the underlying code of the recursive function gets executed again and again until a terminating condition, called the _base case_, gets fulfilled. As you dive into the world of algorithms, you'll come across recursion in many many instances.

Visit the following resources to learn more:

- [@article@Recursion and Stack](https://javascript.info/recursion)
- [@article@JavaScript Function Recursions - CodeGuage](https://www.codeguage.com/courses/js/functions-recursions)
- [@article@Recursion - MDN](https://developer.mozilla.org/en-US/docs/Glossary/Recursion)
- [@feed@Explore top posts about Recursion](https://app.daily.dev/tags/recursion?ref=roadmapsh)

## Rest

# Rest Parameters

The rest parameter syntax allows a function to accept an indefinite number of arguments as an array, providing a way to represent [variadic functions](https://en.wikipedia.org/wiki/Variadic_function) in JavaScript.

Visit the following resources to learn more:

- [@article@Rest Parameters - MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [@feed@Explore top posts about REST API](https://app.daily.dev/tags/rest-api?ref=roadmapsh)

## Samevalue

# Same value

[SameValue](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness#same-value_equality_using_object.is) equality determines whether two values are functionally identical in all contexts.

Visit the following resources to learn more:

- [@article@Same-value equality using Object.is()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness#same-value_equality_using_object.is)

## Samevaluezero

# Same value zero

[SameValueZero](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness#same-value-zero_equality) equality determines whether two values are functionally identical in all contexts with +0 and -0 are also considered equal.

Visit the following resources to learn more:

- [@article@Same-value-zero equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness#same-value-zero_equality)

## Scope  Function Stack

# Scope and function stack

## Scope

A space or environment in which a particular variable or function can be accessed or used. Accessibility of this variable or function depends on where it is defined.

JavaScript has the following kinds of scopes:

- **Global scope**: The default scope for all code running in script mode.
- **Module scope**: The scope for code running in module mode.
- **Function scope**: The scope created with a function.
- **Block scope**: The scope created with a pair of curly braces (a block).

## Function Stack (Call stack)

The function stack is how the interpreter keeps track of its place in a script that calls multiple functions, like which function is currently executing and which functions within that function are being called.

Visit the following resources to learn more:

- [@article@Function stack (call stack) - MDN](https://developer.mozilla.org/en-US/docs/Glossary/Call_stack)
- [@article@Kinds of Scope - MDN](https://developer.mozilla.org/en-US/docs/Glossary/Scope)

## Set

# Set

The `Set` object lets you store unique values of any type, whether [primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive) values or object references. A value in the `Set` may only occur once; it is unique in the `Set`'s collection.

Visit the following resources to learn more:

- [@article@Set - JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [@article@Set - ExploringJS](https://exploringjs.com/impatient-js/ch_sets.html)

## Setinterval

# setInterval

The `setInterval()` method helps us to repeatedly execute a function after a fixed delay. It returns a unique interval ID which can later be used by the `clearInterval()` method, which stops further repeated execution of the function.

`setInterval()` is similar to setTimeout, with a difference. Instead of running the callback function once, it will run it forever, at the specific time interval you specify (in milliseconds):

Visit the following resources to learn more:

- [@article@Scheduling: setTimeout and setInterval](https://javascript.info/settimeout-setinterval)

## Settimeout

# setTimeout

The setTimeout runs a function after the specified period expires. Times are declared in milliseconds.

Visit the following resources to learn more:

- [@article@JavaScript MDN Docs](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout)
- [@video@setInterval and setTimeout: timing events](https://www.youtube.com/watch?v=kOcFZV3c75I)
- [@video@Learn JavaScript setTimeout() in 6 minutes!](https://www.youtube.com/watch?v=shWr5DNVeCI)

## Strict Mode

# Strict Mode

JavaScript's strict mode is a way to opt-in to a restricted variant of JavaScript, thereby implicitly opting out of "sloppy mode". Strict mode isn't just a subset: it intentionally has different semantics from regular code. Browsers not supporting strict mode will run strict mode code with different behavior from browsers that do, so don't rely on strict mode without feature-testing for support for the relevant aspects of strict mode. Strict mode code and non-strict mode code can coexist so that scripts can opt into strict mode incrementally.

Strict mode makes several changes to normal JavaScript semantics:

- Eliminates some JavaScript silent errors by changing them to throw errors.
- Fixes mistakes that make it difficult for JavaScript engines to perform optimizations: strict mode code can sometimes run faster than identical code that's not strict mode.
- Prohibits some syntax likely to be defined in future versions of ECMAScript.

Visit the following resources to learn more:

- [@article@Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
- [@article@Strict mode in JavaScript](https://javascript.info/strict-mode)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## String Operators

# String Operators

In addition to the comparison operators, which can be used on string values, the concatenation operator (`+`) concatenates two string values together, returning another string that is the union of the two operand strings.

The shorthand assignment operator `+=` can also be used to concatenate strings.

Visit the following resources to learn more:

- [@article@JavaScript MDN Tutorials](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#string_operators)
- [@article@String Concatenation - JavaScript.info](https://javascript.info/operators#string-concatenation-with-binary)

## String

# String

String is a primitive type that holds a sequence of characters. String in Javascript is written within a pair of single quotation marks `''`, double quotation marks `""`, or backticks ` `` ` (template literals). All types of quotes can be used to contain a string but only if the starting quote is the same as the end quote.

Visit the following resources to learn more:

- [@article@String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
- [@article@JavaScript Strings](https://javascript.info/string)

## Structured Data

# Structured data

Structured data is used by search-engines, like Google, to understand the content of the page, as well as to gather information about the web and the world in general.

It is also coded using in-page markup on the page that the information applies to.

Visit the following resources to learn more:

- [@article@Google Developers docs](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)

## Switch

# Switch Case

The `switch` statement evaluates an expression, matching the expression's value against a series of `case` clauses, and executes statements after the first `case` clause with a matching value, until a `break` statement is encountered. The `default` clause of a `switch` statement will be jumped to if no `case` matches the expression's value.

## Example

```js
switch (expression) {
  case value1:
    //Statements executed when the result of expression matches value1
    break;
  case value2:
    //Statements executed when the result of expression matches value2
    break;
  ...
  case valueN:
    //Statements executed when the result of expression matches valueN
    break;
  default:
    //Statements executed when none of the values match the value of the expression
    break;
}
```

Visit the following resources to learn more:

- [@article@switch - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
- [@article@The `switch` Statement: Why, What and How - CodeGuage](https://www.codeguage.com/courses/js/conditions-switch)
- [@article@The switch statement - javascript.info](https://javascript.info/switch)

## Symbol

# Symbol

Symbols are a unique and immutable primitive data type in JavaScript, introduced in ECMAScript 6 (ES6). They are often used to create unique property keys for objects, ensuring no property key collisions occur. Each Symbol value is distinct, even when multiple are created with the same description. Symbols can be created using the Symbol() function, and their primary use case is to add hidden or special properties to objects that won’t interfere with other properties or methods.

Learn more from the following resources:

- [@article@Symbol data type in JavaScript](https://www.javascripttutorial.net/symbol/)
- [@article@Symbol type](https://javascript.info/symbol)
- [@article@Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
- [@video@Symbols in Javascript](https://www.youtube.com/watch?v=E5Bblr-SFbA)

## Throw Statement

# Throw Statement

The throw statement throws a user-defined exception. Execution of the current function will stop (the statements after throw won't be executed), and control will be passed to the first catch block in the call stack. If no catch block exists among caller functions, the program will terminate. (excerpt from MDN)

Visit the following resources to learn more:

- [@article@JavaScript MDN Docs](https://developer.mozilla.org/en-us/docs/web/javascript/reference/statements/throw)
- [@article@Error Handling](https://javascript.info/error-handling)
- [@article@"Throw" operator](https://javascript.info/try-catch#throw-operator)

## Trycatchfinally

# Try, Catch, Finally

These are ways of handling errors in your JavaScript code. Inside the try code block we have the code to run, inside the catch block we handle the errors, and inside the finally block we have code that runs after the execution of the previous code blocks, regardless of the result.

Visit the following resources to learn more:

## Type Casting

# Type Casting

Type conversion (or typecasting) means the transfer of data from one data type to another. Implicit conversion happens when the compiler (for compiled languages) or runtime (for script languages like [JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)) automatically converts data types. The source code can also explicitly require a conversion to take place.

Visit the following resources to learn more:

- [@article@Type Conversions](https://javascript.info/type-conversions)
- [@article@Type Casting in JavaScript](https://www.tutorialspoint.com/type-casting-in-javascript)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Type Conversion Vs Coercion

# Type Conversion/Coercion

Type coercion is the automatic or implicit conversion of values from one data type to another (such as strings to numbers). Type conversion is similar to type coercion because they convert values from one data type to another with one key difference — type coercion is implicit. In contrast, type conversion can be either implicit or explicit.

Visit the following resources to learn more:

- [@article@Type Conversion - MDN](https://developer.mozilla.org/en-US/docs/Glossary/Type_Conversion)
- [@article@Type Coercion - MDN](https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion)
- [@video@Type Conversion and Coercion video](https://www.youtube.com/watch?v=jfQyMPzPTjY)

## Typed Arrays

# Typed Arrays

In Javascript, a typed array is an array-like buffer of binary data. There is no JavaScript property or object named TypedArray, but properties and methods can be used with typed array objects.

Visit the following resources to learn more:

- [@article@JavaScript typed arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)
- [@video@Intro to Typed Arrays in JavaScript](https://www.youtube.com/watch?v=UYkJaW3pmj0)

## Typeof Operator

# `typeof` Operator

You can use the typeOf operator to find the data type of a JavaScript variable. It returns a string indicating the type of provided operand's value.

Visit the following resources to learn more:

- [@article@typeof Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)

## Unary Operators

# Unary Operators

JavaScript Unary Operators are the special operators that consider a single operand and perform all the types of operations on that single operand. These operators include unary plus, unary minus, prefix increments, postfix increments, prefix decrements, and postfix decrements.

Visit the following resources to learn more:

- [@article@Unary Operators in JavaScript](https://www.educba.com/unary-operators-in-javascript/)
- [@article@Unary Operators - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators#unary_operators)

## Undefined

# undefined

undefined is a Primitive data type in Javascript.

Whenever a variable is declared but not initialized or assigned a value, then it is stored as undefined. A function returns undefined if a value was not returned. A method or statement also returns undefined if the variable that is being evaluated does not have an assigned value.

Visit the following resources to learn more:

- [@video@undefined in JS](https://www.youtube.com/watch?v=B7iF6G3EyIk&list=PLlasXeu85E9cQ32gLCvAvr9vNaUccPVNP&index=8)

## Using Browser Devtools

# JavaScript Chrome Dev Tools

These are a set of tools built into the browser to aid frontend developers diagnose and solve various issues in their applications — such as JavaScript and logical bugs, CSS styling issues or even just making quick temporary alterations to the DOM.

To enter the dev tools, right click and click **Inspect** (or press `ctrl+shift+c`/`cmd+opt+c`) to enter the Elements panel. Here you can debug CSS and HTML issues. If you want to see logged messages or interact with javascript, enter the **Console** tab from the tabs above (or press `ctrl+shift+j` or `F12` / `cmd+opt+j` to enter it directly). Another very useful feature in the Chrome dev tools is the Lighthouse (for checking performance).

NOTE: This isn't a chrome-specific feature, and most browsers (Chromium based or otherwise) will have their own, largely-similar set of devtools.

Visit the following resources to learn more:

- [@official@Official Docs](https://developer.chrome.com/docs/devtools/)
- [@official@Debug JavaScript with Chrome Dev Tools](https://developer.chrome.com/docs/devtools/javascript/)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Using It Alone

# Using this alone

The keyword `this` when used alone refers to the global object.

_Note: in a browser window the global object is the `window` object._

Visit the following resources to learn more:

## Using This Keyword

# This Keyword

In JavaScript, the `this` keyword is a little different compared to other languages. It refers to an object, but it depends on how or where it is being invoked. It also has some differences between strict mode and non-strict mode.

- In an object method, `this` refers to the object
- Alone, `this` refers to the global object
- In a function, `this` refers to the global object
- In a function, in strict mode, `this` is undefined
- In an event, `this` refers to the element that received the event
- Methods like call(), apply(), and bind() can refer `this` to any object

Visit the following resources to learn more:

- [@article@This Keyword](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Var

# [var] keyword

The var statement declares a function-scoped or globally-scoped variable, optionally initializing it to a value.

Visit the following resources to learn more:

- [@article@var keyword - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
- [@article@JavaScript Variables](https://javascript.info/variables)
- [@video@Declaring Variables without Var, Let, Const - What Would Happen?](https://www.youtube.com/watch?v=6UAKBYpUC-Y)

## Variable Declarations

# Variable Declarations

To use variables in JavaScript, we first need to create it i.e. declare a variable. To declare variables, we use one of the `var`, `let`, or `const` keywords.

Visit the following resources to learn more:

- [@article@Storing the information you need — Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
- [@article@JavaScript Variables - CodeGuage](https://www.codeguage.com/courses/js/variables)

## Variable Naming Rules

# Naming Rules

A variable name should accurately identify your variable. When you create good variable names, your JavaScript code becomes easier to understand and easier to work with. Properly naming variables is really important. JavaScript also has some rules when it comes to naming variables; read about these rules through the links below.

Visit the following resources to learn more:

- [@article@JavaScript Variable Naming Tips - CodeGuage](https://www.codeguage.com/courses/js/variables#Tips_for_naming_variables)
- [@article@Understanding Variables in JavaScript](https://www.informit.com/articles/article.aspx?p=131025&seqNum=3)
- [@article@Naming JavaScript Variables](https://www.dummies.com/article/technology/programming-web-design/javascript/naming-javascript-variables-142522/)
- [@article@JavaScript Naming Conventions](https://www.robinwieruch.de/javascript-naming-conventions/)
- [@article@Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)

## Variable Scopes

# Scopes

In JavaScript, scope refers to the visibility of a variable or how it can be used after it is declared. The scope of a variable depends on the keyword that was used to declare it.

The three types of Scope are Global Scope, Function Scope, and Block Scope. Before ES6 (2015), JavaScript had only Global Scope and Function Scope with the `var` keyword. ES6 introduced `let` and `const` which allow Block Scope in JavaScript.

Global Scope: Variables declared outside any function or curly braces '{}' have Global Scope, and can be accessed from anywhere within the same Javascript code. `var`, `let` and `const` all provide this Scope.

Function Scope: Variables declared within a function can only be used within that same function. Outside that function, they are undefined. `var`, `let` and `const` all provide this Scope.

Block Scope: A block is any part of JavaScript code bounded by '{}'. Variables declared within a block can not be accessed outside that block. This Scope is only provided by the `let` and `const` keywords. If you declare a variable within a block using the `var` keyword, it will NOT have Block Scope.

Local Scope: Local variables are only recognized inside their functions, variables with the same name can be used in different functions. Local variables are created when a function starts, and deleted when the function is completed. `var`, `let` and `const` all provide this Scope.

Visit the following resources to learn more:

- [@article@javascript scope](https://wesbos.com/javascript/03-the-tricky-bits/scope)
- [@video@Understanding Global Local Function Block Scope](https://www.youtube.com/watch?v=_E96W6ivHng)

## Weak Map

# Weak map

[WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap) is a Map-like collection of key/value pairs whose keys must be objects, it removes them once they become inaccessible by other means

Visit the following resources to learn more:

- [@article@WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)
- [@article@WeakMap and WeakSet](https://javascript.info/weakmap-weakset)

## Weak Set

# WeakSet

`WeakSet` objects are collections of objects. Just as with `Sets`, each object in a `WeakSet` may occur only once; all objects in a `WeakSet`'s collection are unique.

Visit the following resources to learn more:

- [@article@WeakSet](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)
- [@article@WeakMap and WeakSet](https://javascript.info/weakmap-weakset)

## What Is Javascript

# What is JavaScript?

JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS. It lets us add interactivity to pages e.g. you might have seen sliders, alerts, click interactions, popups, etc on different websites -- all of that is built using JavaScript. Apart from being used in the browser, it is also used in other non-browser environments as well such as Node.js for writing server-side code in JavaScript, Electron for writing desktop applications, React Native for mobile applications, and so on.

Visit the following resources to learn more:

- [@article@JavaScript MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [@article@The Modern JavaScript Tutorial](https://javascript.info/)
- [@article@A Comprehensive Course on JavaScript with Quizzes and Exercises - CodeGuage](https://www.codeguage.com/courses/js/)
- [@article@Exploring JS: JavaScript books for programmers](https://exploringjs.com/)
- [@video@JavaScript Crash Course for Beginners](https://youtu.be/hdI2bqOjy3c?t=2)
- [@video@Build a Netflix Landing Page Clone with HTML, CSS & JS](https://youtu.be/P7t13SGytRk?t=22)
- [@video@Learn JavaScript - Full Course for Beginners](https://www.youtube.com/watch?v=PkZNo7MFNFg)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## While

# while statement

The `while` statement creates a loop that executes a specified statement as long as the test condition evaluates to `true`. The condition is evaluated before executing the statement.

Visit the following resources to learn more:

- [@article@While Statement - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
- [@article@The while Loop - CodeGuage](https://www.codeguage.com/courses/js/loops-while-loop)

## Working With Apis

# Working with APIs

When working with remote APIs, you need a way to interact with those APIs. Modern JavaScript provides two native ways to send HTTP requests to remote servers, `XMLHttpRequest` and `Fetch`.

Visit the following resources to learn more:

- [@article@Fetching data from the server](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data)
- [@article@XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)
- [@article@Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [@article@Is fetch API better than XMLHTTPRequest](https://medium.com/beginners-guide-to-mobile-web-development/the-fetch-api-2c962591f5c)
- [@article@Ajax Battle: XMLHttpRequest vs the Fetch API](https://blog.openreplay.com/ajax-battle-xmlhttprequest-vs-fetch/)

## Xmlhttprequest

# XMLHttpRequest

`XMLHttpRequest` (XHR) is a built-in browser object that can be used to interact with server. XHR allows you to update data without having to reload a web page. Despite the word XML in its name, XHR not only used to retrieve data with XML format, we can use it with any type of data, like JSON, file(s), and much more.

Visit the following resources to learn more:

- [@article@Using XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest)
- [@article@Network request - XMLHttpRequest](https://javascript.info/xmlhttprequest)
