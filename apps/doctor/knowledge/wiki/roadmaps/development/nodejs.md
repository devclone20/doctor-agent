# Nodejs Roadmap

##   Watch

# --watch

The `--watch` flag in Node.js is a powerful feature introduced in Node.js version 19 that enables automatic reloading of your Node.js application whenever changes are detected in the specified files.

Here's How it works:

*   You run your Node.js script with the `--watch` flag: `$ node --watch your_script.js`
*   Node.js starts watching the specified file (or directory) for changes.
*   Whenever a change is detected, Node.js automatically restarts the script

Visit the following resources to learn more:

- [@official@Node.js CLI](https://nodejs.org/api/cli.html)
- [@official@Node.js --watch Docs](https://nodejs.org/api/cli.html#--watch)
- [@article@Medium - Watch Mode](https://medium.com/@khaled.smq/built-in-nodejs-watch-mode-52ffadaec8a8)

##   Dirname

# __dirname

The `__dirname` in a node script returns the path of the folder where the current JavaScript file resides. `__filename` and `__dirname` are used to get the filename and directory name of the currently executing file.

Visit the following resources to learn more:

- [@official@__dirname](https://nodejs.org/docs/latest/api/modules.html#__dirname)
- [@article@How to use __dirname](https://www.digitalocean.com/community/tutorials/nodejs-how-to-use__dirname)

##   Filename

# __filename

The `__filename` in Node.js returns the filename of the executed code. It gives the absolute path of the code file. The following approach covers implementing `__filename` in the Node.js project.

Visit the following resources to learn more:

- [@official@__filename](https://nodejs.org/docs/latest/api/modules.html#__filename)

## Assertion Errors

# Assertion Errors

An `AssertionError` in Node.js is an error that is thrown when the `assert` module determines that a given expression is not truthy. The `assert` module is a built-in Node.js module that provides a simple set of assertion tests that can be used to test the behavior of your code.

Visit the following resources to learn more:

- [@official@Node.js Assert](https://nodejs.org/api/assert.html#new-assertassertionerroroptions)
- [@article@Node.js Error Handling - AssertionError](https://blog.airbrake.io/blog/nodejs-error-handling/assertionerror-nodejs)

## Async Programming

# Async Programming

Asynchronous code means that things can happen independently of the main program flow, async functions in JavaScript are processed in the background without blocking other requests. It ensures non-blocking code execution. Asynchronous code executes without having any dependency and no order. This improves the system efficiency and throughput. Making web apps requires knowledge of asynchronous concepts since we will be dealing with actions that require some time to get processed.

Visit the following resources to learn more:

- [@article@Introduction to Async JS](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Introducing/)
- [@video@Asynchronous Vs Synchronous Programming](https://www.youtube.com/watch?v=Kpn2ajSa92c)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Asyncawait

# Async/Await

Async/Await is a special syntax to work with promises in a more comfortable fashion. It's easy to understand and use. Adding the keyword async before a function ensures that the function returns a promise and the keyword await makes JavaScript wait until that promise settles and returns the result.

Visit the following resources to learn more:

- [@official@Async/Await Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [@article@More on async await](https://javascript.info/async-await)
- [@article@W3Docs Async/Await](https://www.w3docs.com/learn-javascript/async-await.html)
- [@video@Using async await](https://www.youtube.com/watch?v=V_Kr9OSfDeU)

## Axios

# Axios

Axios is a promise-based HTTP Client for node.js and the browser. Used for making requests to web servers. On the server-side it uses the native node.js http module, while on the client (browser) it uses XMLHttpRequests.

Visit the following resources to learn more:

- [@official@Axios Documentation](https://axios-http.com/docs/intro)
- [@video@Axios Tutorial](https://www.youtube.com/watch?v=6LyagkoRWYA)
- [@feed@Explore top posts about Axios](https://app.daily.dev/tags/axios?ref=roadmapsh)

## Building  Consuming Apis

# APIs

API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other.

Visit the following resources to learn more:

- [@article@What is an API?](https://aws.amazon.com/what-is/api/)
- [@video@What is an API (in 5 minutes)](https://youtu.be/ByGJQzlzxQg?si=9EB9lgRvEOgt3xPJ)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Callbacks

# Callbacks

Node.js, being an asynchronous platform, doesn't wait around for things like file I/O to finish - Node.js uses callbacks. A callback is a function called at the completion of a given task; this prevents any blocking, and allows other code to be run in the meantime.

Visit the following resources to learn more:

- [@official@Asynchronicity in Programming Languages](https://nodejs.org/en/learn/asynchronous-work/javascript-asynchronous-programming-and-callbacks)
- [@article@What are Callbacks?](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)

## Callstack  Stack Trace

# Stack Trace

The stack trace is used to trace the active stack frames at a particular instance during the execution of a program. The stack trace is useful while debugging code as it shows the exact point that has caused an error.

## Chalk Package

# Chalk

Chalk is a clean and focused library used to do string styling in your terminal applications. With it, you can print different styled messages to your console such as changing font colors, font boldness, font opacity, and the background of any message printed on your console.

Visit the following resources to learn more:

- [@opensource@Chalk Docs](https://github.com/chalk/chalk#readme)

## Child Process

# Child Process

The child\_process module gives the node the ability to run the child process, established through IPC (inter-process communication) by accessing operating system commands.

The three main methods inside this module are : `child_process.spawn()` `child_process.fork()` `child_process.exec()`

Visit the following resources to learn more:

- [@official@Child Process Docs](https://nodejs.org/api/child_process.html#child-process)
- [@article@Securing Node.js Against Command Injection](https://www.nodejs-security.com/blog/securing-your-nodejs-apps-by-analyzing-real-world-command-injection-examples)

## Chokidar

# Chokidar

Chokidar is a fast open-source file watcher for node. js. You give it a bunch of files, it watches them for changes and notifies you every time an old file is edited; or a new file is created.

Visit the following resources to learn more:

- [@official@chokidar](https://www.npmjs.com/package/chokidar)

## Cli Progress

# Cli progress

CLI-Progress is a package that provides a custom progress bar for CLI applications.

Visit the following resources to learn more:

- [@official@CLI-Progress Documentation](https://www.npmjs.com/package/cli-progress)
- [@feed@Explore top posts about CLI](https://app.daily.dev/tags/cli?ref=roadmapsh)

## Cluster

# Cluster

The Cluster module allows you to easily create child processes that each runs simultaneously on their own single thread, to handle workloads among their application threads.

Visit the following resources to learn more:

- [@official@Node.js Cluster](https://nodejs.org/api/cluster.html#cluster)

## Command Line Apps

# Command Line Applications

Command Line Applications are applications that can be run from the command line. They are also called CLI (Command Line Interface) applications. Users can interact with clients entirely by terminal commands. They are very useful for automation and building tools.

Visit the following resources to learn more:

- [@article@Build a Command Line Application with Node.js](https://developer.okta.com/blog/2019/06/18/command-line-app-with-nodejs)
- [@video@5-Minute Node.js CLI Project](https://www.youtube.com/watch?v=_oHByo8tiEY)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Commander

# Commander.js

Commander is a light-weight, expressive, and powerful command-line framework for node.js. with Commander.js you can create your own command-line interface (CLI).

Visit the following resources to learn more:

- [@official@commander package](https://www.npmjs.com/package/commander)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Common Built In Modules

# Nodejs core modules

These are the core modules that come with `Node.js` out of the box. This module provides tools or APIs for performing out certain standard `Node.js` operations. like interacting with the file system, url parsing, or logging information to the console.

Visit the following resources to learn more:

- [@official@fs module](https://nodejs.org/api/fs.html)
- [@official@url module](https://nodejs.org/api/url.html)
- [@official@console module](https://nodejs.org/api/console.html)
- [@official@util module](https://nodejs.org/api/util.html)
- [@official@events module](https://nodejs.org/api/events.html)
- [@official@os module](https://nodejs.org/api/os.html)
- [@official@worker threads module](https://nodejs.org/api/worker_threads.html)
- [@official@child process module](https://nodejs.org/api/child_process.html)
- [@official@process object](https://nodejs.org/api/process.html)
- [@official@crypto module](https://nodejs.org/api/crypto.html)

## Commonjs

# CommonJS vs ESM

CommonJS and ES (EcmaScript) are module systems used in Node. CommonJS is the default module system. However, a new module system was recently added to NodeJS - ES modules. CommonJS modules use the require() statement for module imports and module.exports for module exports while it's import and export for ES.

Visit the following resources to learn more:

- [@article@CommonJS vs ESM](https://blog.logrocket.com/commonjs-vs-es-modules-node-js/)
- [@article@Using CommonJS](https://www.javascripttutorial.net/nodejs-tutorial/nodejs-modules/)
- [@article@Using ES Modules](https://blog.logrocket.com/es-modules-in-node-today/)
- [@article@CommonJS vs. ES Modules: Modules and Imports in NodeJS](https://reflectoring.io/nodejs-modules-imports/)
- [@video@Using Modules](https://www.youtube.com/watch?v=pP4kjXykbio)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Creating  Importing

# Custom Modules

Modules are the collection of JavaScript codes in a separate logical file that can be used in external applications based on their related functionality. There are two ways to create modules in Node.js i.e. either via CommonJS or ESM.

Visit the following resources to learn more:

- [@article@CommonJS vs ESM in Node.js](https://blog.logrocket.com/commonjs-vs-es-modules-node-js/)
- [@article@Modules and Imports in Node.js](https://reflectoring.io/nodejs-modules-imports/)
- [@video@Creating a Module in Node.js](https://www.youtube.com/watch?v=Cxo4UKpHv5s)

## Creating Packages

# Creating Packages

npm packages allow you to bundle some specific functionality into a reusable package which can then be uploaded to some package registry such as npm or GitHub packages and then be installed and reused in projects using npm.

Visit the following resources to learn more:

- [@article@Best practices for creating a modern npm package](https://snyk.io/blog/best-practices-create-modern-npm-package/)

## Cypress

# Cypress

Cypress is a new front end testing tool built for the modern web. It enables you to write faster, easier and more reliable tests.

Visit the following resources to learn more:

- [@official@Cypress](https://www.cypress.io/)
- [@article@Cypress Documentation](https://docs.cypress.io/)
- [@feed@Explore top posts about Cypress](https://app.daily.dev/tags/cypress?ref=roadmapsh)

## Debugging

# More Debugging

Debugging is a concept to identify and remove errors from software applications. Here, we will learn about the technique to debug a Node.js application.

Why not to use `console.log()` for debugging?

Using `console.log` to debug the code generally dives into an infinite loop of “stopping the app and adding a console.log, and start the app again” operations. Besides slowing down the development of the app, it also makes the writing dirty and creates unnecessary code. Finally, trying to log out variables alongside with the noise of other potential logging operations, may make the process of debugging difficult when attempting to find the values you are debugging.

Visit the following resources to learn more:

- [@official@Node.js - Getting Started](https://nodejs.org/en/learn/getting-started/debugging)
- [@article@Wikipedia - What is Debugging?](https://en.wikipedia.org/wiki/Debugging)

## Dotenv Package

# dotenv

dotenv is a zero-dependency module that loads environment variables from a `.env` file into `process.env`. Storing configuration in the environment separate from code is based on The Twelve-Factor App methodology.

Visit the following resources to learn more:

- [@official@process.env Documentation](https://nodejs.org/docs/latest/api/process.html#process_process_env)
- [@official@Dotenv package](https://www.npmjs.com/package/dotenv)
- [@opensource@dotenv Docs](https://github.com/motdotla/dotenv#readme)
- [@article@The Twelve-Factor App Methodology](https://12factor.net/config)
- [@article@Dotenv tutorial](https://zetcode.com/javascript/dotenv/)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Drizzle

# Drizzle

Drizzle lets you build your project the way you want, without interfering with your project or structure. Using Drizzle you can define and manage database schemas in TypeScript, access your data in a SQL-like or relational way, and take advantage of opt-in tools to make your developer experience amazing.

Visit the following resources to learn more:

- [@official@Drizzle](https://orm.drizzle.team/)
- [@official@Drizzle Documentation](https://orm.drizzle.team/docs/overview)
- [@opensource@Drizzle GitHub](https://github.com/drizzle-team/drizzle-orm)
- [@article@Getting Started with Drizzle](https://dev.to/franciscomendes10866/getting-started-with-drizzle-orm-a-beginners-tutorial-4782)

## Ejs

# EJS

EJS is a template language or engine that allows you to generate HTML markup with pure JavaScript. And this is what makes it perfect for Nodejs applications. In simple words, the EJS template engine helps to easily embed JavaScript into your HTML template.

Visit the following resources to learn more:

- [@official@EJS](https://ejs.co/)
- [@official@EJS Documentation](https://ejs.co/#docs)
- [@official@EJS Package](https://www.npmjs.com/package/ejs)
- [@article@Try EJS Online](https://ionicabizau.github.io/ejs-playground/)
- [@article@How to use EJS](https://www.digitalocean.com/community/tutorials/how-to-use-ejs-to-template-your-node-application)
- [@article@Step-by-Step EJS Guide](https://codeforgeek.com/ejs-template-engine-in-nodejs/)

## Error Handling

# Error Handling

Error handling is a way to find bugs and solve them as quickly as humanly possible. The errors in Node.js can be either operation or programmer errors. Read the articles linked below to understand how to handle different types of errors in Node.js

Visit the following resources to learn more:

- [@article@Node.js Error Handling Best Practices](https://sematext.com/blog/node-js-error-handling)
- [@article@Error handling in Node.js](https://blog.logrocket.com/error-handling-node-js/)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Esm

# ESM

ESM (ECMAScript Modules) is a standardized module system in JavaScript that allows for the organized, maintainable, and reusable structuring of code. It uses import and export statements for including and sharing functions, objects, or primitives between files. ESM supports static analysis, enabling better optimization and tooling, and is always in strict mode to reduce common JavaScript issues. Node.js fully supports ESM, which can be used with .mjs file extensions or configured in the package.json for .js files, making it easier to write modular and efficient JavaScript applications.

Visit the following resources to learn more:

- [@official@ESM Documentation](https://nodejs.org/api/esm.html)

## Event Emitter

# Event Emitter

In Node.js, an event can be described simply as a string with a corresponding callback. An event can be "emitted" (or, in other words, the corresponding callback be called) multiple times or you can choose to only listen for the first time it is emitted.

Visit the following resources to learn more:

- [@official@What are Event Emitters?](https://nodejs.org/en/learn/asynchronous-work/the-nodejs-event-emitter)
- [@article@Using Event Emitters in Node.js](https://www.digitalocean.com/community/tutorials/using-event-emitters-in-node-js)

## Event Loop

# Event Loop

The Event Loop is one of the most critical aspects of Node.js. Why is this so important? Because it explains how Node.js can be asynchronous and have non-blocking I/O, it explains the "killer feature" of Node.js, which made it this successful.

Visit the following resources to learn more:

- [@official@The Node.JS Event Loop](https://nodejs.org/learn/asynchronous-work/event-loop-timers-and-nexttick)
- [@official@Don't Block the Event Loop](https://nodejs.org/learn/asynchronous-work/dont-block-the-event-loop)
- [@article@JavaScript Visualized: Event Loop](https://dev.to/lydiahallie/javascript-visualized-event-loop-3dif)
- [@article@Event Loop in Node.js - Mixu's Node book](https://book.mixu.net/node/ch2.html#the-event-loop-understanding-how-node-executes-javascript-code)

## Exitting  Exit Codes

# Exiting and exit codes

Exiting is a way of terminating a Node.js process by using node.js process module.

Visit the following resources to learn more:

- [@official@Exit Documentation](https://nodejs.org/api/process.html#event-exit)
- [@article@How to Exit a Process in Node.js](https://betterstack.com/community/questions/how-to-exit-in-node-js/)

## Expressjs

# Express.js

Express is a node js web application framework that provides broad features for building web and mobile applications. It is used to build a single page, multi-page, and hybrid web application.

Visit the following resources to learn more:

- [@official@Express.js](https://expressjs.com/)
- [@official@Getting Started Guide](https://expressjs.com/en/starter/installing.html)
- [@article@Express Full Guide](https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm)
- [@article@Sample Project](https://auth0.com/blog/create-a-simple-and-stylish-node-express-app/)
- [@feed@Explore top posts about Express.js](https://app.daily.dev/tags/express?ref=roadmapsh)

## Fastify

# Fastify

Fastify is a web framework highly focused on providing the best developer experience with the least overhead and a powerful plugin architecture, inspired by Hapi and Express.

Visit the following resources to learn more:

- [@official@Fastify](https://www.fastify.io/)
- [@official@Fastify Documentation](https://www.fastify.io/docs/latest/)
- [@video@Beginner Fastify Tutorial](https://www.youtube.com/watch?v=Lk-uVEVGxOA)
- [@feed@Explore top posts about Fastify](https://app.daily.dev/tags/fastify?ref=roadmapsh)

## Fetch

# fetch

The `fetch()` method in JavaScript is used to request to the server and load the information on the webpages. The request can be of any APIs that return the data of the format JSON or XML. This method returns a promise.

Visit the following resources to learn more:

- [@official@MDN - Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [@official@NodeJS globals: fetch](https://nodejs.org/api/globals.html#fetch)
- [@official@MDN - Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [@article@freeCodeCamp on avoiding callback hell](https://www.freecodecamp.org/news/how-to-deal-with-nested-callbacks-and-avoid-callback-hell-1bc8dc4a2012/)

## Figlet Package

# Figlet

This package aims to fully implement the FIGfont spec in JavaScript, which represents the graphical arrangement of characters representing larger characters. It works in the browser and with Node.js.

Visit the following resources to learn more:

- [@opensource@figlet](https://github.com/patorjk/figlet.js)

## Fs Extra

# fs-extra

fs-extra adds file system methods that aren't included in the native fs module and adds promise support to the fs methods. It also uses graceful-fs to prevent EMFILE errors. It should be a drop in replacement for fs.

Visit the following resources to learn more:

- [@official@fs-extra package](https://www.npmjs.com/package/fs-extra)
- [@article@fs-extra vs fs](https://ar.al/2021/03/07/fs-extra-to-fs/)

## Fs Module

# fs module

File System or `fs` module is a built in module in Node that enables interacting with the file system using JavaScript. All file system operations have synchronous, callback, and promise-based forms, and are accessible using both CommonJS syntax and ES6 Modules.

Visit the following resources to learn more:

- [@official@fs module](https://nodejs.org/api/fs.html)
- [@video@Using fs](https://www.youtube.com/watch?v=ZySsdm576wE)

## Garbage Collection

# Garbage Collection

Memory management in JavaScript is performed automatically and invisibly to us. We create primitives, objects, functions… All that takes memory. The main concept of memory management in JavaScript is reachability.

Visit the following resources to learn more:

- [@article@JavaScript Garbage Collection](https://javascript.info/garbage-collection)
- [@article@Memory Management in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management)

## Glob

# Glob

The glob pattern is most commonly used to specify filenames, called wildcard characters, and strings, called wildcard matching.

Visit the following resources to learn more:

- [@official@NPM Glob](https://www.npmjs.com/package/glob)

## Global Installation

# Global Install vs Local Install

NodeJS and NPM allow two methods of installing dependencies/packages: Local and Global. This is mainly used when adding a package or dependency as part of a specific project you're working on. The package would be installed (with its dependencies) in `node_modules` folder **under your project**. In addition, in `package.json` file there will be a new line added for the installed dependency under the label `dependencies`. At this point - you can start using the package in your NodeJS code by importing the package. Unlike the local install, you can install packages and dependencies **globally**. This would install it in a system path, and these packages would be available to any program which runs on **this specific** computer. This method is often used for installing command line tools (for example, even `npm` program is a Globally installed npm package).

Visit the following resources to learn more:

- [@official@Downloading and installing packages locally](https://docs.npmjs.com/downloading-and-installing-packages-locally)
- [@official@Downloading and installing packages globally](https://docs.npmjs.com/downloading-and-installing-packages-globally)
- [@official@NPM Install Docs](https://docs.npmjs.com/cli/commands/npm-install)

## Global Keyword

# global keyword

In browsers, the top-level scope is the global scope, and its global object is called the `window` object. Within the browser, `var something` will define a new global variable inside the `window` object. In Node.js, this is different. The top-level scope is **not** the global scope; `var something` inside a Node.js module will be local to that module.

Visit the following resources to learn more:

- [@official@global Keyword in Node.js](https://nodejs.org/api/globals.html#global)
- [@article@What is the 'global' object in NodeJS](https://stackoverflow.com/questions/43627622/)
- [@video@What is Global Object?](https://www.youtube.com/watch?v=jn8PZNBmKm0)
- [@video@Global Object in Node](https://www.youtube.com/watch?v=PY-AycMkEAg)

## Globby

# Globby

_User-friendly glob matching_

Based on fast-glob but adds a bunch of useful features.

Visit the following resources to learn more:

- [@official@NPM Globby](https://www.npmjs.com/package/globby)
- [@opensource@GitHub Globby](https://github.com/sindresorhus/globby)

## Got Package

# Got

Got is a lighter, human-friendly, and powerful HTTP request library explicitly designed to work with Node.js. It supports pagination, RFC compliant caching, makes an API request again if it fails, supports cookies out of the box, etc.

Visit the following resources to learn more:

- [@official@Got Documentation](https://www.npmjs.com/package/got)
- [@article@How to consume APIs using GOT in Node.js?](https://rapidapi.com/guides/call-apis-got)

## Handling Async Errors

# Async errors

Errors must always be handled. If you are using synchronous programming you could use a try catch. But this does not work if you work asynchronous! Async errors will only be handled inside the callback function!

Visit the following resources to learn more:

- [@article@Async Errors](https://www.mariokandut.com/handling-errors-in-asynchronous-functions-node-js/)
- [@article@The best way to handle errors in asynchronous javascript](https://dev.to/m__mdy__m/the-best-way-to-handle-errors-in-asynchronous-javascript-16bb)

## History Of Nodejs

# History of Node.js

Node.js was written initially by Ryan Dahl in 2009, about thirteen years after the introduction of the first server-side JavaScript environment, Netscape's LiveWire Pro Web. The initial release supported only Linux and macOS X. Its development and maintenance were led by Dahl and later sponsored by Joyent.

Visit the following resources to learn more:

- [@article@Rising Stack - History of Node.js on a Timeline](https://blog.risingstack.com/history-of-node-js/)
- [@article@SAP Press - How Did Node.js Come About?](https://blog.sap-press.com/how-did-node.js-come-about)
- [@video@Node.js: The Documentary | An Origin Story](https://youtu.be/LB8KwiiUGy0)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Hono

# Hono

Hono is a lightweight, simple, and fast web framework for Cloudflare Workers, Deno, Bun, and other applications. It is a modern web application that is both fast and flexible. It offers inbuilt support for TypeScript, and easy development in a local environment. Using Hono, It is easy to create publishable web applications with Deno, Bun, and Cloudflare Workers.

Visit the following resources to learn more:

- [@official@Hono Documentation](https://hono.dev/docs/)
- [@article@Build a web application with Hono](https://blog.logrocket.com/build-web-application-hono/)

## Http Module

# Making API calls with HTTP

You can make API calls using the `http` module in Node.js as well. Here are the two methods that you can use:

*   `http.get()` - Make http GET requests.
*   `http.request()` - Similar to `http.get()` but enables sending other types of http requests (GET requests inclusive).

Visit the following resources to learn more:

- [@official@Node.js http.get() documentation](https://nodejs.org/docs/latest-v16.x/api/http.html#httpgeturl-options-callback)
- [@official@Node.js http.request() documentation](https://nodejs.org/docs/latest-v16.x/api/http.html#httprequesturl-options-callback)
- [@article@How To Create an HTTP Client with Core HTTP in Node.js](https://www.digitalocean.com/community/tutorials/how-to-create-an-http-client-with-core-http-in-node-js)

## Inquirer Package

# Inquirer

Inquirer.js is a collection of common interactive command line interfaces for taking inputs from user. It is promise based and supports chaining series of prompt questions together, receiving text input, checkboxes, lists of choices and much more.

You can use it to empower your terminal applications that need user input or to build your own CLI.

Visit the following resources to learn more:

- [@opensource@Inquirer](https://github.com/SBoudrias/Inquirer.js#readme)
- [@article@How To Create Interactive Command-line Prompts with Inquirer.js](https://www.digitalocean.com/community/tutorials/nodejs-interactive-command-line-prompts)
- [@video@How to make a CLI in Node.js with Inquirer](https://www.youtube.com/watch?v=0xjfkl9nODQ)

## Introduction To Nodejs

# Node.js Introduction

Node.js is an open source, cross-platform runtime environment and library that is used for running web applications outside the client’s browser.

It is used for server-side programming, and primarily deployed for non-blocking, event-driven servers, such as traditional web sites and back-end API services, but was originally designed with real-time, push-based architectures in mind. Every browser has its own version of a JS engine, and node.js is built on Google Chrome’s V8 JavaScript engine.

Visit the following resources to learn more:

- [@official@Node.js](https://nodejs.org/en/)
- [@official@Node.js Documentation](https://nodejs.org/en/docs/)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Javascript Errors

# Javascript Errors

JavaScript Errors are used by JavaScript to inform developers about various issue in the script being executed. These issues can be syntax error where the developer/programmer has used the wrong syntax, it can be due to some wrong user input or some other problem.

JavaScript has six types of errors that may occur during the execution of the script:

*   EvalError
*   RangeError
*   ReferenceError
*   SyntaxError
*   TypeError
*   URIError

Visit the following resources to learn more:

- [@article@Error Types in JavaScript](https://blog.bitsrc.io/types-of-native-errors-in-javascript-you-must-know-b8238d40e492)
- [@article@JavaScript error reference - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Jest

# Jest

Jest is a delightful JavaScript Testing Framework with a focus on simplicity. It works with projects using: Babel, TypeScript, Node, React, Angular, Vue and more!

Visit the following resources to learn more:

- [@official@Jest](https://jestjs.io)
- [@official@Jest Documentation](https://jestjs.io/docs/getting-started)
- [@feed@Explore top posts about Jest](https://app.daily.dev/tags/jest?ref=roadmapsh)

## Jsonwebtoken

# JSON Web Token

JWT, or JSON-Web-Token, is an open standard for sharing security information between two parties — a client and a server. Each JWT contains encoded JSON objects, including a set of claims. JWTs are signed using a cryptographic algorithm to ensure that the claims cannot be altered after the token is issued.

Visit the following resources to learn more:

- [@official@JSON Package Documentation](https://www.npmjs.com/package/jsonwebtoken)
- [@article@What is JWT](https://www.akana.com/blog/what-is-jwt)
- [@video@JWT Implementation](https://www.youtube.com/watch?v=mbsmsi7l3r4)

## Keep App Running

# Keep your app running in Production

PM2 lets you run your nodejs scripts forever. In the event that your application crashes, PM2 will also restart it for you.

Visit the following resources to learn more:

- [@article@Keep a Node Application Constantly Running](https://devtut.github.io/nodejs/keep-a-node-application-constantly-running.html#use-pm2-as-a-process-manager)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Knex

# Knex

Knex.js is a "batteries included" SQL query builder for PostgreSQL, CockroachDB, MSSQL, MySQL, MariaDB, SQLite3, Better-SQLite3, Oracle, and Amazon Redshift designed to be flexible, portable, and fun to use.

Visit the following resources to learn more:

- [@official@Knex.js](https://knexjs.org)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Ky

# Ky

Ky is a tiny and elegant HTTP client based on the browser Fetch API. Ky targets modern browsers and Deno.For older browsers, you will need to transpile and use a fetch polyfill.For Node.js, check out Got.. 1 KB (minified & gzipped), one file, and no dependencies.

Visit the following resources to learn more:

- [@official@Ky Package](https://www.npmjs.com/package/ky/v/0.9.0)
- [@opensource@Ky Docs](https://github.com/sindresorhus/ky)

## Local Installation

# Local Installation

Locally installed packages are available only to the project where the packages are installed, while the globally installed packages can be used any where without installing them into a project. Another use case of the global packages is when using CLI tools.

Visit the following resources to learn more:

- [@official@Downloading and installing packages locally](https://docs.npmjs.com/downloading-and-installing-packages-locally)
- [@official@Downloading and installing packages globally](https://docs.npmjs.com/downloading-and-installing-packages-globally)

## Logging

# Node.js Logging

**Logging** is an essential part of understanding the complete application life cycle of the `Node.js` application. We can much more easily and quickly fix errors by looking at logs throughout the development process, from creating to debugging to designing new features. **Error**, **warn**, **info**, and **debug** are the four basic logging levels in `Node.js`. Logging involves persistently collecting information about an application's runtime behaviour.

Visit the following resources to learn more:

- [@article@Node.js Logging](https://stackify.com/node-js-logging/)
- [@article@Logging best practices](https://blog.appsignal.com/2021/09/01/best-practices-for-logging-in-nodejs.html)
- [@article@Logging](https://stackify.com/node-js-logging/)
- [@feed@Explore top posts about Logging](https://app.daily.dev/tags/logging?ref=roadmapsh)

## Marko

# Marko

Marko is a fast and lightweight HTML-based templating engine that compiles templates to CommonJS modules and supports streaming, async rendering, and custom tags. It is HTML re-imagined as a language for building dynamic and reactive user interfaces.

Visit the following resources to learn more:

- [@official@Marko Documentation](https://markojs.com/docs/guides-overview/)

## Memory Leaks

# Memory Leaks

Memory leaks are caused when your Node.js app’s CPU and memory usage increases over time for no apparent reason. In simple terms, a Node.js memory leak is an orphan block of memory on the Heap that is no longer used by your app because it has not been released by the garbage collector. It’s a useless block of memory. These blocks can grow over time and lead to your app crashing because it runs out of memory.

Visit the following resources to learn more:

- [@article@Memory Leaks in Node.js](https://sematext.com/blog/nodejs-memory-leaks/)
- [@article@Memory Leaks Causes](https://sematext.com/blog/nodejs-memory-leaks/#what-causes-them-common-node-js-memory-leaks)
- [@article@Memory Leaks Detectors](https://sematext.com/blog/nodejs-memory-leaks/#node-js-memory-leak-detectors)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Modules

# Node.js Modules

We split our code into different files to maintain, organize and reuse code whenever possible. A module system allows us to split and include code and import code written by other developers whenever required. In simple terms, a module is nothing but a JavaScript file. Node.js has many built-in modules that are part of the platform and comes with Node.js installation, for example, HTTP, fs, path, and more.

Visit the following resources to learn more:

- [@official@Modules: CommonJS modules](https://nodejs.org/api/modules.html#modules-commonjs-modules)
- [@article@CommonJS vs. ES Modules in Node.js](https://blog.logrocket.com/commonjs-vs-es-modules-node-js/)
- [@video@Modules in Node.js](https://www.youtube.com/watch?v=9Amxzvq5LY8&)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Mongoose

# Mongoose

Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js. Mongoose provides a straight-forward, schema-based solution to model your application data. It includes built-in type casting, validation, query building, business logic hooks and more, out of the box.

Visit the following resources to learn more:

- [@official@Mongoose](https://mongoosejs.com)
- [@official@Mongoose Documentation](https://mongoosejs.com/docs/guide.html)
- [@article@Getting Started with MongoDB and Mongoose](https://www.mongodb.com/developer/languages/javascript/getting-started-with-mongodb-and-mongoose/)
- [@feed@Explore top posts about Mongoose](https://app.daily.dev/tags/mongoose?ref=roadmapsh)

## Monitor Changes Dev

# Keep App Running

In Node.js, you need to restart the process to make changes take effect. This adds an extra step to your workflow. You can eliminate this extra step by using `nodemon` to restart the process automatically.

Since Node.js 18.11.0, you can run Node with the `--watch` flag to reload your app every time a file is changed. So you don't need to use `nodemon` anymore.

Visit the following resources to learn more:

## Morgan

# Morgan

Morgan is a NodeJS and express.js middleware to log the HTTP request and error, simplifying the debugging process. It provides flexibility in defining the format of log messages and helps override the output destination for your logs.

Visit the following resources to learn more:

- [@official@morgan package](https://www.npmjs.com/package/morgan)
- [@article@How to Use Morgan | DigitalOcean](https://www.digitalocean.com/community/tutorials/nodejs-getting-started-morgan)

## Native Drivers

# Native Drivers

Another way to connect to different databases in Node.js is to use the official native drivers provided by the database.

Visit the following resources to learn more:

- [@official@MongoDB Drivers](https://www.mongodb.com/docs/drivers/)

## Native Drivers

# Native drivers

Another way to connect to different databases in Node.js is to use the official native drivers provided by the database.

## Nestjs

# NestJS

NestJS is a progressive Node.js framework for creating efficient and scalable server-side applications.

Visit the following resources to learn more:

- [@official@NestJS](https://nestjs.com)
- [@official@NestJS Documentations](https://docs.nestjs.com)
- [@video@Beginner NestJS Tutorial](https://www.youtube.com/watch?v=GHTA143_b-s)
- [@feed@Explore top posts about NestJS](https://app.daily.dev/tags/nestjs?ref=roadmapsh)

## Node   Inspect

# Node Inspect

Node.js provides a built-in DevTools-based debugger to allow debugging Node.js applications.

Visit the following resources to learn more:

- [@article@Debugging Node.js with Chrome DevTools](https://medium.com/@paul_irish/debugging-node-js-nightlies-with-chrome-devtools-7c4a1b95ae27)

## Nodejs Vs Browser

# Nodejs vs Browser

Both the browser and Node.js use JavaScript as their programming language. Building apps that run in the browser is entirely different than building a Node.js application. Even though it's always JavaScript, some key differences make the experience radically different.

Visit the following resources to learn more:

- [@official@Differences between Node.js and the Browser](https://nodejs.org/en/learn/getting-started/differences-between-nodejs-and-the-browser/)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Nodemon

# Nodemon

In Node.js, you need to restart the process to make changes take effect. This adds an extra step to your workflow. You can eliminate this extra step by using nodemon or PM2 to restart the process automatically.

`nodemon` is a command-line interface (CLI) utility developed by rem that wraps your Node app, watches the file system, and automatically restarts the process.

Visit the following resources to learn more:

- [@official@Nodemon](https://nodemon.io/)
- [@article@PM2](https://pm2.keymetrics.io/docs/usage/quick-start/)
- [@article@How To Restart Your Node.js Apps Automatically with nodemon](https://www.digitalocean.com/community/tutorials/workflow-nodemon)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Nodetest

# node:test

`node:test` is a built-in module in Node.js that provides a simple, asynchronous test runner. It's designed to make writing tests as straightforward as writing any other code.

Key Features

*   Simplicity: Easy to use and understand.
*   Asynchronous Support: Handles asynchronous code gracefully.
*   Subtests: Allows for organizing tests into hierarchical structures.
*   Hooks: Provides beforeEach and afterEach hooks for setup and teardown.

Visit the following resources to learn more:

- [@official@Test Runner API Docs](https://nodejs.org/api/test.html)
- [@official@Node.js Test Runner](https://nodejs.org/en/learn/test-runner/using-test-runner)

## Npm Workspaces

# npm workspaces

Workspace is a generic term that refers to the set of npm CLI features that support managing multiple packages from your local file system from within a singular top-level root package.

Visit the following resources to learn more:

- [@official@npm workspaces](https://docs.npmjs.com/cli/using-npm/workspaces)
- [@article@Getting Started with Npm Workspaces](https://ruanmartinelli.com/blog/npm-7-workspaces-1/)
- [@feed@Explore top posts about NPM](https://app.daily.dev/tags/npm?ref=roadmapsh)

## Npm

# npm

npm is the standard package manager for Node.js.

It is two things: first and foremost, it is an online repository for the publishing of open-source Node.js projects; second, it is a command-line utility for interacting with said repository that aids in package installation, version management, and dependency management. A plethora of Node.js libraries and applications are published on npm, and many more are added every day

Visit the following resources to learn more:

- [@official@NPM Documentation](https://docs.npmjs.com/)
- [@official@What is npm?](https://nodejs.org/en/learn/getting-started/an-introduction-to-the-npm-package-manager)
- [@official@An introduction to the npm package manager](https://nodejs.org/en/learn/getting-started/an-introduction-to-the-npm-package-manager)
- [@video@NPM Crash Course](https://www.youtube.com/watch?v=jHDhaSSKmB0)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Npx

# npx

npx is a very powerful command that's been available in npm starting version 5.2, released in July 2017. If you don't want to install npm, you can install npx as a standalone package. npx lets you run code built with Node.js and published through the npm registry, without needing to install the package itself. This is particularly useful for trying out new tools, running one-time commands, or using packages in shared environments where global installations are undesirable. npx takes care of downloading the package on-the-fly, running the desired command, and then cleaning up the temporary installation. This keeps your project's dependencies lean and avoids version conflicts.

Visit the following resources to learn more:

- [@official@npx](https://docs.npmjs.com/cli/commands/npx/)
- [@article@Introduction to the npx Node.js Package Runner](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b)

## Passportjs

# Passport js

Passport.js is authentication middleware for Node.js. It makes implementing authentication in express apps really easy and fast. It is extremely flexible and modular. It uses "strategies" to support authentication using a username and password, Facebook, Twitter, and a lot of other sites.

Visit the following resources to learn more:

- [@official@PassportJS](https://www.passportjs.org/)
- [@official@PassportJS Documentation](https://www.passportjs.org/docs/)
- [@video@Implementation of OAuth using passportjs](https://www.youtube.com/watch?v=sakQbeRjgwg&list=PL4cUxeGkcC9jdm7QX143aMLAqyM-jTZ2x)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Path Module

# path module

The `path` module provides utilities for working with file and directory paths. It's built-in to Node.js core and can simply be used by requiring it.

Visit the following resources to learn more:

- [@official@Path Documentation](https://nodejs.org/api/path.html)
- [@official@Learn Node.js File Paths](https://nodejs.org/en/learn/manipulating-files/nodejs-file-paths)
- [@video@Path Module in Node.js](https://youtu.be/j95Lwxvi9JY)

## Playwright

# Playwright

Playwright is an open-source automation library developed by Microsoft for testing and automating web applications. 1 It offers a unified API to control Chromium, Firefox, and WebKit browsers, making it a versatile choice for cross-browser testing.

Playwright provides a high-level API to interact with web pages. You can write scripts to simulate user actions, such as clicking buttons, filling forms, and navigating through different pages. Playwright handles the underlying browser interactions, making it easy to write and maintain tests.

Visit the following resources to learn more:

- [@official@Playwright](https://playwright.dev/)
- [@official@Playwright Docs](https://playwright.dev/docs/getting-started-vscode)
- [@article@Getting Started with Playwright](https://learn.microsoft.com/en-us/shows/getting-started-with-end-to-end-testing-with-playwright/)

## Pm2

# Pm2

PM2 is a production process manager for Node.js applications with a built-in load balancer. It allows you to keep applications alive forever, to reload them without downtime and to facilitate common system admin tasks.

Visit the following resources to learn more:

- [@official@Pm2](https://pm2.keymetrics.io/)
- [@official@Pm2 Documentation](https://pm2.keymetrics.io/docs/usage/quick-start/)

## Prisma

# Prisma

Prisma provides an open source next-generation ORM in the TypeScript ecosystem. It offers a dedicated API for relation filters. It provides an abstraction layer that makes you more productive compared to writing SQL. Prisma currently supports `PostgreSQL`, `MySQL`, `SQL Server`, `SQLite`, `MongoDB` and `CockroachDB`.

Visit the following resources to learn more:

- [@official@Prisma](https://www.prisma.io/)
- [@video@Prisma & MongoDB Youtube Tutorial](https://www.youtube.com/watch?v=-7r4whMKt1s)
- [@feed@Explore top posts about Prisma](https://app.daily.dev/tags/prisma?ref=roadmapsh)

## Prisma

# Prisma

Prisma is an ORM that helps app developers build faster and make fewer errors. Combined with its Data Platform developers gain reliability and visibility when working with databases.

Visit the following resources to learn more:

- [@official@Prisma](https://www.prisma.io/)
- [@official@Prisma Documentation](https://www.prisma.io/docs/)
- [@feed@Explore top posts about Prisma](https://app.daily.dev/tags/prisma?ref=roadmapsh)

## Processargv

# process.argv

`process.argv` is an array of parameters that are sent when you run a Node.js file or Node.js process.

Visit the following resources to learn more:

- [@official@process.argv](https://nodejs.org/docs/latest/api/process.html#processargv)
- [@video@Command Line Arguments - Cave of Programming](https://youtu.be/nr7i2HOAjeE)

## Processcwd

# process.cwd()

The `process.cwd()` method returns the current working directory of the Node.js process.

Visit the following resources to learn more:

- [@official@process.cwd()](https://nodejs.org/api/process.html#processcwd)
- [@article@Whats the difference between process.cwd() vs __dirname?](https://stackoverflow.com/questions/9874382/whats-the-difference-between-process-cwd-vs-dirname)

## Processenv

# process.env

In Node. js, process. env is a global variable that is injected during runtime. It is a view of the state of the system environment variables. When we set an environment variable, it is loaded into process.env during runtime and can later be accessed.

Visit the following resources to learn more:

- [@official@Node.js Learn Environment Variables](https://nodejs.org/en/learn/command-line/how-to-read-environment-variables-from-nodejs)
- [@article@Process.env Node](https://www.knowledgehut.com/blog/web-development/node-environment-variables)

## Processnexttick

# process.nextTick()

Every time the event loop takes a full trip, we call it a tick. When we pass a function to `process.nextTick()`, we instruct the engine to invoke this function at the end of the current operation before the next event loop tick starts.

Visit the following resources to learn more:

- [@official@Understanding Process.NextTick()](https://nodejs.org/en/learn/asynchronous-work/understanding-processnexttick)
- [@official@The Node.js process.nextTick()](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)
- [@video@The process.nextTick Function](https://www.youtube.com/watch?v=-niA5XOlCWI)

## Processstdin

# process.stdin

`process.stdin` is a stream in Node.js that represents the standard input, typically the keyboard. It allows your Node.js programs to receive text input from the command line. The `readline` module provides a convenient interface for reading input from `process.stdin` line by line, making it easier to handle user input in interactive command-line applications.

Visit the following resources to learn more:

- [@official@process.stdin](https://nodejs.org/api/process.html#processstdin)
- [@official@Accept input from the command line in Node.js](https://nodejs.org/en/learn/command-line/accept-input-from-the-command-line-in-nodejs#accept-input-from-the-command-line-in-nodejs)
- [@article@Node.js Process stdin & stdout](https://nodecli.com/node-stdin-stdout)

## Promises

# Promises

A promise is commonly defined as a proxy for a value that will eventually become available.

Asynchronous functions use promise behind the scenes, so understanding how promises work is fundamental to understanding how "async" and "await" works.

Once a promise has been called, it will start in a pending state. This means that the calling function continues executing, while the promise is pending until it resolves, giving the calling function whatever data was being requested.

Creating a Promise:

The Promise API exposes a Promise constructor, which you initialize using new Promise().

Using resolve() and reject(), we can communicate back to the caller what the resulting Promise state was, and what to do with it.

Visit the following resources to learn more:

- [@official@Promises](https://www.promisejs.org/)
- [@article@Promise Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [@video@Asynchronous JavaScript - Promises](https://www.youtube.com/watch?v=a_8nrslImo4/)

## Prompts Package

# Prompts

Prompts is a higher level and user friendly interface built on top of Node.js's inbuilt `Readline` module. It supports different type of prompts such as text, password, autocomplete, date, etc. It is an interactive module and comes with inbuilt validation support.

Visit the following resources to learn more:

- [@official@Prompts](https://www.npmjs.com/package/prompts)

## Pug

# Pug

Pug is a JavaScript template engine. It is a high-performance template engine heavily influenced by Haml and implemented with JavaScript for Node.js and browsers. Pug was formerly called Jade.

Pug is a high-performance template engine heavily influenced by Haml and implemented with JavaScript for Node.js and browsers

Visit the following resources to learn more:

- [@official@Getting started with PugJs](https://pugjs.org/api/getting-started.html)
- [@article@How to Build a Node Application Using a Pug Template](https://blog.bitsrc.io/how-to-build-a-node-application-using-a-pug-template-7319ab1bba69?gi=40b338891148)
- [@article@Pug.js tutorial](https://zetcode.com/javascript/pugjs/)
- [@video@Node.js + Express - Tutorial - PugJS Templating Engine](https://www.youtube.com/watch?v=DSp9ExFw3Ig)

## Running Nodejs Code

# Running Node.js Code

The usual way to run a Node.js program is to run the globally available `node` command (once you install Node.js) and pass the name of the file you want to execute.

Visit the following resources to learn more:

- [@official@Run Node.js from Command Line](https://nodejs.org/en/learn/command-line/run-nodejs-scripts-from-the-command-line/)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Running Scripts

# Running Scripts

In Node.js, npm scripts are used for the purpose of initiating a server, starting the build of a project, and also for running the tests. We can define this scripts in the package.json file of the folder. Also, we can split the huge scripts into many smaller parts if it is needed.

Visit the following resources to learn more:

- [@official@Running Scripts](https://docs.npmjs.com/cli/using-npm/scripts)
- [@article@Example of Running Scripts](https://riptutorial.com/node-js/example/4592/running-scripts)

## Semantic Versioning

# Semantic Versioning

Semantic Versioning is a standard for versioning software that's widely adopted in the npm ecosystem. It provides a clear and consistent way to communicate changes in a software package to users.

Version Format
--------------

A semantic version number consists of three parts separated by dots:

*   MAJOR: Incremented when there are incompatible API changes.
*   MINOR: Incremented when new functionality is added in a backwards-compatible manner.
*   PATCH: Incremented when bug fixes are made without affecting the API.

### Example: 1.2.3

*   1 is the major version.
*   2 is the minor version.
*   3 is the patch version.

Visit the following resources to learn more:

- [@official@Semver.org](https://semver.org/)
- [@article@Medium - Understanding Semantic Versioning](https://medium.com/codex/understanding-semantic-versioning-a-guide-for-developers-dad5f2b70583)
- [@article@Devopedia - Semver](https://devopedia.org/semantic-versioning)

## Sequelize

# Sequelize

Sequelize is an easy-to-use and promise-based Node.js ORM tool for Postgres, MySQL, MariaDB, SQLite, DB2, Microsoft SQL Server, and Snowflake. It features solid transaction support, relations, eager and lazy loading, read replication and more.

What is an ORM ?

An ORM is known as Object Relational Mapper. This is a tool or a level of abstraction which maps(converts) data in a relational database into programmatic objects that can be manipulated by a programmer using a programming language (usually an OOP language). ORMs solely exist to map the details between two data sources which due to a mismatch cannot coexist together.

Visit the following resources to learn more:

- [@official@Sequelize](https://sequelize.org/)
- [@official@Sequelize - NPM Package](https://www.npmjs.com/package/sequelize)
- [@official@Sequelize Docs](https://sequelize.org/docs/v6/getting-started/)
- [@article@Getting started with Sequelize](https://levelup.gitconnected.com/the-ultimate-guide-to-get-started-with-sequelize-orm-238588d3516e)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Setimmediate

# setImmediate

The `setImmediate` function delays the execution of a function to be called after the current event loops finish all their execution. It's very similar to calling `setTimeout` with 0 ms delay.

Visit the following resources to learn more:

- [@official@Understanding setImmediate](https://nodejs.org/en/learn/asynchronous-work/understanding-setimmediate)
- [@article@Understanding setImmediate](https://developer.mozilla.org/en-US/docs/Web/API/Window/setImmediate)

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

## Stdout  Stderr

# Process stdout

The `process.stdout` property is an inbuilt application programming interface of the process module which is used to send data out of our program. A Writable Stream to stdout. It implements a `write()` method. `console.log()` prints to the `process.stdout.write()` with formatted output or new line.

Visit the following resources to learn more:

- [@official@process.stdout](https://nodejs.org/api/process.html#processstdout)
- [@article@process.stdout vs console.log](https://stackoverflow.com/questions/4976466/difference-between-process-stdout-write-and-console-log-in-node-js/4984464#4984464)

## Streams

# Nodejs streams

Streams are a type of data handling methods and are used to read, write or transform chunks of data piece by piece without keeping it in memory all at once. There are four types of streams in Node.js.

*   **Readable**: streams from which data can be read.
*   **Writable**: streams to which we can write data.
*   **Duplex**: streams that are both Readable and Writable.
*   **Transform**: streams that can modify or transform the data as it is written and read.

Multiple streams can be chained together using `pipe()` method.

Visit the following resources to learn more:

- [@official@Stream API Documentation](https://nodejs.org/api/stream.html)
- [@article@Understanding Streams in Node.js](https://nodesource.com/blog/understanding-streams-in-nodejs)
- [@video@Node.js Streams tutorial](https://www.youtube.com/watch?v=GlybFFMXXmQ)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## System Errors

# System Errors

Node.js generates system errors when exceptions occur within its runtime environment. These usually occur when an application violates an operating system constraint. For example, a system error will occur if an application attempts to read a file that does not exist.

Below are the system errors commonly encountered when writing a Node.js program:

1.  EACCES - Permission denied
2.  EADDRINUSE - Address already in use
3.  ECONNRESET - Connection reset by peer
4.  EEXIST - File exists
5.  EISDIR - Is a directory
6.  EMFILE - Too many open files in system
7.  ENOENT - No such file or directory
8.  ENOTDIR - Not a directory
9.  ENOTEMPTY - Directory not empty
10.  ENOTFOUND - DNS lookup failed
11.  EPERM - Operation not permitted
12.  EPIPE - Broken Pipe
13.  ETIMEDOUT - Operation timed out

Visit the following resources to learn more:

- [@official@Node.js Errors](https://nodejs.org/api/errors.html#errors_class_systemerror)
- [@article@@Article@16 Common Errors in Node.js and How to Fix Them](https://betterstack.com/community/guides/scaling-nodejs/nodejs-errors/)

## Template Engines

# Template Engines

Template engine helps us to create an HTML template with minimal code. Also, it can inject data into HTML template at client side and produce the final HTML.

Some examples of template engines in Node.js are:

*   Nunjucks
*   Jade
*   Vash
*   EJS
*   Handlebars
*   HAML

Visit the following resources to learn more:

- [@official@Getting Started with Pug](https://pugjs.org/api/getting-started.html)
- [@official@Handlebars Package](https://www.npmjs.com/package/handlebars)
- [@official@EJS Package](https://www.npmjs.com/package/ejs)

## Testing

# Testing

Software testing is the process of verifying that what we create is doing exactly what we expect it to do. The tests are created to prevent bugs and improve code quality.

The two most common testing approaches are unit testing and end-to-end testing. In the first, we examine small snippets of code, in the second, we test an entire user flow.

Visit the following resources to learn more:

- [@official@Vitest](https://vitest.dev/)
- [@official@Jest](https://jest.io)
- [@article@Software Testing](https://en.wikipedia.org/wiki/Software_testing)

## Threads

# Nodejs Threads

Node.js is a single-threaded language and gives us ways to work parallelly to our main process. Taking note of nowadays multicore system single threading is very memory efficient.

Visit the following resources to learn more:

- [@article@Single Thread vs Child Process vs Worker Threads vs Cluster in Node.js](https://alvinlal.netlify.app/blog/single-thread-vs-child-process-vs-worker-threads-vs-cluster-in-nodejs)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Typeorm

# TypeORM

TypeORM is an ORM that can run in NodeJS, Browser, Cordova, PhoneGap, Ionic, React Native, NativeScript, Expo, and Electron platforms and can be used with TypeScript and JavaScript (ES5, ES6, ES7, ES8). Its goal is to always support the latest JavaScript features and provide additional features that help you to develop any kind of application that uses databases - from small applications with a few tables to large scale enterprise applications with multiple databases.

Visit the following resources to learn more:

- [@official@TypeORM Docs](https://typeorm.io)
- [@video@TypeORM Crash Course](https://www.youtube.com/watch?v=JaTbzPcyiOE)

## Uncaught Exceptions

# Uncaught Exceptions

When a JavaScript error is not properly handled, an uncaughtException is emitted. These suggest the programmer has made an error, and they should be treated with the utmost priority.

The correct use of `uncaughtException` is to perform synchronous cleanup of allocated resources (e.g. file descriptors, handles, etc) before shutting down the process. It is not safe to resume normal operation after `uncaughtException` because system becomes corrupted. The best way is to let the application crash, log the error and then restart the process automatically using nodemon or pm2.

Visit the following resources to learn more:

- [@official@Uncaught Exception Error Events](https://nodejs.org/api/process.html#event-uncaughtexception)
- [@article@Let It Crash: Best Practices for Handling Node.js Errors on Shutdown](https://blog.heroku.com/best-practices-nodejs-errors)
- [@article@Uncaught Exceptions in Node.js](https://shapeshed.com/uncaught-exceptions-in-node/)

## Updating Packages

# Updating Packages

npm provides various features to help install and maintain the project's dependencies. Dependencies get updates with new features and fixes, so upgrading to a newer version is recommended. We use `npm update` commands for this.

Visit the following resources to learn more:

- [@official@Updating packages downloaded from the registry](https://docs.npmjs.com/updating-packages-downloaded-from-the-registry)
- [@article@How to Update Npm Packages Safely With Npm Check Updates](https://chrispennington.blog/blog/how-to-update-npm-packages-safely-with-npm-check-updates/)
- [@video@How to Update All NPM Dependencies At Once](https://www.youtube.com/watch?v=Ghdfdq17JAY)

## User Specified Errors

# User Specified Errors

User specified errors can be created by extending the base Error object, a built-in error class. When creating errors in this manner, you should pass a message string that describes the error. This message can be accessed through the message property on the object. The Error object also contains a name and a stack property that indicate the name of the error and the point in the code at which it is created.

Visit the following resources to learn more:

- [@article@A Comprehensive Guide To Error Handling In Node.js](https://www.honeybadger.io/blog/errors-nodejs/)

## Using Apm

# Using APM

As much fun as it is to intercept your container requests with inspect and step through your code, you won’t have this option in production. This is why it makes a lot of sense to try and debug your application locally in the same way as you would in production.

In production, one of your tools would be to login to your remote server to view the console logs, just as you would on local. But this can be a tedious approach. Luckily, there are tools out there that perform what is called log aggregation, such as Stackify.

These tools send your logs from your running application into a single location. They often come with high-powered search and query utilities so that you can easily parse your logs and visualize them.

Visit the following resources to learn more:

- [@article@APM Logs: How to Get Started for Faster Debugging](https://last9.io/blog/apm-logs-for-faster-debugging/)
- [@article@Debugging using APM](https://stackify.com/node-js-debugging-tips/)
- [@feed@Explore top posts about APM](https://app.daily.dev/tags/apm?ref=roadmapsh)

## Using Debugger

# Using Debugger

Node.js includes a command-line debugging utility. The Node.js debugger client is not a full-featured debugger, but simple stepping and inspection are possible. To use it, start Node.js with the inspect argument followed by the path to the script to debug.

Example - `$ node inspect myscript.js`

Visit the following resources to learn more:

- [@official@Debugger](https://nodejs.org/api/debugger.html)
- [@official@Inspect Docs](https://nodejs.org/en/learn/getting-started/debugging)
- [@article@Freecodecamp.org - Debugging](https://www.freecodecamp.org/news/how-to-debug-node-js-applications/)

## Vitest

# Vitest

Vitest is a Vite-native unit testing framework that's Jest-compatible. Vitest is a powerful testing library built on top of Vite that is growing in popularity. You can use Vitest for a range of testing needs, such as unit, integration, end-to-end (E2E), snapshot, and performance testing of functions and components. ESM, TypeScript, JSX. Out-of-box ESM, TypeScript and JSX support powered by esbuild. Vitest is free and open source.

Visit the following resources to learn more:

- [@official@Vitest](https://vitest.dev/)
- [@official@Vitest Documentation](https://vitest.dev/guide/)

## What Is Nodejs

# What is Node.js

Node.js is an open-source and cross-platform JavaScript runtime environment. It is a popular tool for almost any kind of project! Node.js runs the V8 JavaScript engine, Google Chrome's core, outside the browser. This allows Node.js to be very performant. A Node.js app runs in a single process, without creating a new thread for every request.

Node.js provides a set of asynchronous I/O primitives in its standard library that prevent JavaScript code from blocking and generally, libraries in Node.js are written using non-blocking paradigms, making blocking behavior the exception rather than the norm.

Visit the following resources to learn more:

- [@official@Node.js](https://nodejs.org/en/about/)
- [@official@Node.js - Getting Started](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- [@video@What is Node.js?](https://www.youtube.com/watch?v=uVwtVBpw7RQ)
- [@video@How Node.js Works?](https://www.youtube.com/watch?v=jOupHNvDIq8)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Why Use Nodejs

# Why Node.js

Node.js is a cross-platform runtime, perfect for a wide range of use cases. Its huge community makes it easy to get started. It uses the V8 engine to compile JavaScript and runs at lightning-fast speeds. Node.js applications are very scalable and maintainable. Cross-platform support allows the creation of all kinds of applications - desktop apps, software as a service, and even mobile applications. Node.js is perfect for data-intensive and real-time applications since it uses an event-driven, non-blocking I/O model, making it lightweight and efficient. With such a huge community, a vast collection of Node.js packages is available to simplify and boost development.

Visit the following resources to learn more:

- [@official@Learn Node.js](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- [@article@Why Choose Node.js?](https://medium.com/selleo/why-choose-node-js-b0091ad6c3fc)
- [@article@5 Reasons to Choose Node.js](https://www.bitovi.com/blog/5-reasons-to-choose-nodejs)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)

## Winston

# Winston

winston is designed to be a simple and universal logging library with support for multiple transports. A transport is essentially a storage device for your logs. Each winston logger can have multiple transports configured at different levels. For example, one may want error logs to be stored in a persistent remote location (like a database), but all logs output to the console or a local file.

Visit the following resources to learn more:

- [@opensource@winston](https://github.com/winstonjs/winston?tab=readme-ov-file#readme)
- [@article@A Complete Guide to Winston Logging in Node.js](https://betterstack.com/community/guides/logging/how-to-install-setup-and-use-winston-and-morgan-to-log-node-js-applications/)

## Worker Threads

# Worker Threads

Worker thread is a continuous parallel thread that runs and accepts messages until it is explicitly closed or terminated. With worker threads, we can achieve a much efficient application without creating a deadlock situation. Workers, unlike children's processes, can exchange memory.

Visit the following resources to learn more:

- [@official@Worker Threads](https://nodejs.org/api/worker_threads.html#worker-threads)

## Working With Databases

# What is Database

A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS).

Visit the following resources to learn more:

- [@article@What is Database?](https://en.wikipedia.org/wiki/Database)
- [@article@What is Database - AWS](https://aws.amazon.com/what-is/database/)

## Working With Files

# Working with Files

You can programmatically manipulate files in Node.js with the built-in `fs` module. The name is short for “file system,” and the module contains all the functions you need to read, write, and delete files on the local machine.

Visit the following resources to learn more:

- [@official@File System Module](https://nodejs.org/docs/latest/api/fs.html)
- [@article@How To Work with Files using the fs Module in Node.js](https://www.digitalocean.com/community/tutorials/how-to-work-with-files-using-the-fs-module-in-node-js)
- [@feed@Explore top posts about Node.js](https://app.daily.dev/tags/nodejs?ref=roadmapsh)
