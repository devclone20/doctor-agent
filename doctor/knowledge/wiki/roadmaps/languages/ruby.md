# Ruby Roadmap

## Arithmetic

# Arithmetic Operators

Arithmetic operators are symbols that perform mathematical calculations on numerical values. These operators allow you to perform addition, subtraction, multiplication, division, and other common arithmetic operations. They take one or more operands (the values being operated on) and produce a result based on the operation performed.

Visit the following resources to learn more:

- [@article@Arithmetical operators](https://ruby-for-beginners.rubymonstas.org/operators/arithmetical.html)
- [@article@Ruby - Operators](https://www.tutorialspoint.com/ruby/ruby_operators.htm)

## Arrays

# Arrays

Arrays in Ruby are ordered collections of items. They can hold any type of data, including numbers, strings, symbols, or even other arrays. You create an array using square brackets `[]`, with elements separated by commas. Arrays are dynamic, meaning their size can change as you add or remove elements. You can access elements in an array using their index, starting from 0 for the first element.

Visit the following resources to learn more:

- [@official@class Array](https://docs.ruby-lang.org/en/master/Array.html)
- [@article@Arrays](https://launchschool.com/books/ruby/read/arrays#whatisanarray)
- [@article@Arrays - Odin Project](https://www.theodinproject.com/lessons/ruby-arrays)
- [@article@Arrrays](https://ruby-for-beginners.rubymonstas.org/built_in_classes/arrays.html)
- [@video@Arrays are Easy in Ruby for Beginners 9](https://www.youtube.com/watch?v=PeyodDIfLeE)
- [@video@Arrays | Ruby | Tutorial 13](https://www.youtube.com/watch?v=SP3Vf2KcYeU)

## Assignment

# Assignment Operators

Assignment operators in Ruby are used to assign values to variables. The most basic assignment operator is the equals sign (=), which assigns the value on the right-hand side to the variable on the left-hand side. Ruby also provides compound assignment operators that combine assignment with arithmetic or bitwise operations, such as +=, -=, \*=, /=, and %=. These operators modify the variable's value by performing the specified operation with the right-hand side operand and then assigning the result back to the variable.

Visit the following resources to learn more:

- [@article@Assignment operators](https://kddnewton.com/2023/07/20/ruby-operators.html#assignment-operators)
- [@article@Ruby - Operators](https://www.tutorialspoint.com/ruby/ruby_operators.htm)

## Attributes Accessors

# Attributes Accessors

Attributes accessors provide a convenient way to access and modify the instance variables of a class. They automatically generate methods for reading (getting) and writing (setting) the values of these variables. The three main types are `attr_reader`, which creates a getter method; `attr_writer`, which creates a setter method; and `attr_accessor`, which makes both a getter and a setter method. These accessors simplify code and encapsulate the internal state of objects.

Visit the following resources to learn more:

- [@article@Accessors and Attributes of Class in Ruby](https://www.naukri.com/code360/library/accessors-and-attributes-of-class-in-ruby)
- [@article@What is an accessor?](https://ruby-doc.org/docs/ruby-doc-bundle/UsersGuide/rg/accessors.html)
- [@article@Understanding attr methods in Ruby!](https://dev.to/kateh/understanding-attr-methods-in-ruby-412)
- [@video@How to Use Attribute Accessors in Ruby](https://www.youtube.com/watch?v=C4O7bcbItw4)

## Begin Rescue Ensure

# Exception Handling with begin, rescue, and ensure

Exception handling is a mechanism to deal with errors that occur during the execution of a program. In Ruby, the `begin`, `rescue`, and `ensure` keywords provide a structured way to handle these exceptions. The `begin` block encloses the code that might raise an exception. If an exception occurs, the `rescue` block catches and handles it. The `ensure` block, if present, guarantees that its code will always be executed, regardless of whether an exception was raised or not, making it suitable for cleanup operations.

Visit the following resources to learn more:

- [@article@How to Use The “Begin” & “Rescue” Keywords in Ruby](https://www.rubyguides.com/2019/06/ruby-rescue-exceptions/)
- [@article@Understanding Ruby Error Handling](https://betterstack.com/community/guides/scaling-ruby/ruby-error-handling/)
- [@article@Unlocking Ruby Keywords: Begin, End, Ensure, Rescue](https://vaidehijoshi.github.io/blog/2015/08/25/unlocking-ruby-keywords-begin-end-ensure-rescue/)
- [@video@Handling Errors | Ruby | Tutorial 28](https://www.youtube.com/watch?v=J7R94i2bhlI)

## Blocks

# Blocks

Blocks are chunks of code that can be passed to methods as if they were arguments. They are defined using either `do...end` or curly braces `{}`. Blocks are not objects themselves, but they can be converted into objects called Procs. Methods can then execute the code within the block using the `yield` keyword. Blocks are a fundamental part of Ruby's expressiveness, allowing for powerful iteration and control flow patterns.

Visit the following resources to learn more:

- [@article@The Ultimate Guide to Blocks, Procs & Lambdas](https://www.rubyguides.com/2016/02/ruby-procs-and-lambdas/)
- [@article@Blocks and Procs](https://launchschool.com/books/ruby/read/more_stuff#blocksandprocs)
- [@article@Blocks - Odin Project](https://www.theodinproject.com/lessons/ruby-blocks)
- [@article@The two common ways to call a Ruby block](https://www.codewithjason.com/two-common-ways-call-ruby-block/)
- [@video@Blocks, Procs, and Lambda Functions in Ruby](https://www.youtube.com/watch?v=Dh3cSYjHITI)
- [@video@Ruby Blocks, Procs, and Lambdas 🦁🐅🐻](https://www.youtube.com/watch?v=SADF5diqAJk)

## Booleans

# Booleans

Booleans represent truth values: either `true` or `false`. They are fundamental for decision-making in Ruby code, allowing programs to execute different blocks of code based on whether a condition is true or false. Boolean values are the result of logical operations and comparisons.

Visit the following resources to learn more:

- [@article@Booleans - Odin Project](https://www.theodinproject.com/lessons/ruby-basic-data-types#booleans)
- [@article@True, False, and Nil](https://ruby-for-beginners.rubymonstas.org/built_in_classes/true_false_nil.html)
- [@video@True or False Booleans in Ruby for Beginners 4](https://www.youtube.com/watch?v=zzDNAu3IVpQ)

## Break

# Break Statement in Ruby

The `break` statement in Ruby is a control flow tool used to exit a loop prematurely. When `break` is encountered within a loop (like `for`, `while`, `until`, or `each`), the loop's execution is immediately terminated, and the program continues with the next statement after the loop. It's useful for stopping a loop when a specific condition is met, preventing unnecessary iterations.

Visit the following resources to learn more:

- [@article@Understanding The Ruby Next & Break Keywords](https://www.rubyguides.com/2019/09/ruby-next-break-keywords/)
- [@article@Controlling Loop Execution](https://launchschool.com/books/ruby/read/loops_iterators#controllloop)
- [@article@Ruby Explained: Iteration](https://eriktrautman.com/posts/ruby-explained-iteration)

## Bundler

# Bundler

Bundler is a dependency manager for Ruby. It ensures that an application uses the exact versions of gems (Ruby libraries) that it needs to function correctly. It tracks and installs the specific gem versions required by a project, creating a consistent environment across different machines and deployments. This prevents conflicts and ensures that the application behaves as expected, regardless of where it's run.

Visit the following resources to learn more:

- [@official@Bundler](https://bundler.io/)
- [@official@What is Bundler?](https://bundler.io/guides/getting_started.html)
- [@article@The Beginner's Guide to Bundler and Gemfiles](https://www.moncefbelyamani.com/the-beginner-s-guide-to-bundler-and-gemfiles/)
- [@video@Introduction to Ruby Bundler Gem](https://www.youtube.com/watch?v=nGKAa04hpZE)

## Byebug

# Byebug

Byebug is a powerful debugger for Ruby programs. It allows you to step through your code line by line, inspect variables, set breakpoints, and evaluate expressions in real-time. This helps you understand the flow of your program, identify the source of bugs, and fix them more efficiently.

Visit the following resources to learn more:

- [@opensource@byebug](https://github.com/deivid-rodriguez/byebug)
- [@article@Debugging with ‘ByeBug’ gem](https://medium.com/le-wagon-tokyo/debugging-with-byebug-gem-6a47b2a210bb)
- [@video@Debugging Ruby With Byebug](https://www.youtube.com/watch?v=toZrovVX4ug)

## Case

# Case Statements

A `case` statement in Ruby provides a way to execute different blocks of code based on the value of a variable or expression. It's an alternative to using multiple `if/elsif/else` statements, especially when you need to check for several different possible values. The `case` statement compares a given value against multiple `when` clauses, and executes the code block associated with the first matching clause. An optional `else` clause can be included to handle cases where none of the `when` clauses match.

Visit the following resources to learn more:

- [@article@Case statements](https://www.theodinproject.com/lessons/ruby-conditional-logic#case-statements)
- [@article@The Many Uses Of Ruby Case Statements](https://www.rubyguides.com/2015/10/ruby-case/)
- [@video@case..when in Ruby](https://www.youtube.com/watch?v=gsmexAC2eoM)

## Chaining Methods

# Chaining Methods

Chaining methods in Ruby lets you call multiple methods on an object in a single line of code. This works because most methods in Ruby return an object (often `self`, the object the method was called on). By returning an object, the next method in the chain can be immediately called on the result of the previous method. This creates a fluent and readable way to perform a series of operations on a single object.

Visit the following resources to learn more:

- [@article@Chaining Methods](https://launchschool.com/books/ruby/read/methods#chainingmethods)
- [@article@Chaining methods - Odin Project](https://www.theodinproject.com/lessons/ruby-methods#chaining-methods)
- [@article@A Guide to Method Chaining](https://www.sitepoint.com/a-guide-to-method-chaining/)
- [@video@How to Read, Analyze & Understand Ruby Method Chains](https://www.youtube.com/watch?v=toeX_3cHqYg)

## Closures

# Closures

A closure is a block of code that can be passed around and executed later, even after the scope in which it was originally defined has ended. It "closes over" its surrounding environment, capturing the values of variables that were in scope when the closure was created. This allows the closure to access and use those variables even when it's executed in a different context.

Visit the following resources to learn more:

- [@article@Understanding Ruby closures](https://www.codewithjason.com/ruby-closures/)
- [@article@Closures in Ruby: Blocks, Procs and Lambdas](https://blog.appsignal.com/2018/09/04/ruby-magic-closures-in-ruby-blocks-procs-and-lambdas.html)
- [@video@Understanding Ruby closures](https://www.youtube.com/watch?v=1OrZ2edTHGQ)
- [@video@An Introduction to Procs, Lambdas and Closures in Ruby](https://www.youtube.com/watch?v=VBC-G6hahWA)

## Comments

# Comments

Comments are notes in your code that the Ruby interpreter ignores. They're used to explain what the code does, making it easier for you and others to understand. You can create a single-line comment by starting a line with a `#`. For multi-line comments, you can use `=begin` and `=end` blocks; anything between these markers is treated as a comment.

Visit the following resources to learn more:

- [@official@Code Comments](https://docs.ruby-lang.org/en/master/syntax/comments_rdoc.html)
- [@article@How To Use Comments in Ruby](https://www.digitalocean.com/community/tutorials/how-to-use-comments-in-ruby)
- [@video@Comments | Ruby | Tutorial 25](https://www.youtube.com/watch?v=7wbX3OMgqn0)

## Comparison

# Comparison Operators

Comparison operators are symbols used to compare two values. These operators evaluate to either `true` or `false` based on the relationship between the values being compared. Common comparison operators include equal to (`==`), not equal to (`!=`), greater than (`>`), less than (`<`), greater than or equal to (`>=`), and less than or equal to (`<=`).

Visit the following resources to learn more:

- [@article@Comparison operators](https://ruby-for-beginners.rubymonstas.org/operators/comparison.html)
- [@article@Ruby - Operators](https://www.tutorialspoint.com/ruby/ruby_operators.htm)

## Concurrency

# Concurrency & Parallelism

Concurrency and parallelism are techniques for improving the performance and responsiveness of programs by executing multiple tasks seemingly or actually at the same time. Concurrency deals with managing multiple tasks within a single program, allowing them to make progress even if one task is blocked. Parallelism, on the other hand, involves physically executing multiple tasks simultaneously, typically by distributing them across multiple processor cores.

Visit the following resources to learn more:

- [@article@Ruby Concurrency and Parallelism: A Practical Tutorial](http://toptal.com/developers/ruby/ruby-concurrency-and-parallelism-a-practical-primer)
- [@article@Parallelism and concurrency in Ruby](https://msuliq.medium.com/concurrency-and-parallin-ruby-91d10045d2fe)
- [@video@RailsConf 2016 - Introduction to Concurrency in Ruby by Thijs Cadier](https://www.youtube.com/watch?v=5AxtY4dfuwc)

## Concurrent Ruby

# Concurrent Ruby

Concurrent Ruby is a library that provides tools and abstractions for concurrent and parallel programming in Ruby. It offers features like actors, promises, dataflow variables, and thread pools to help developers write efficient and thread-safe code, enabling them to take advantage of multi-core processors and improve application performance.

Visit the following resources to learn more:

- [@official@Concurrent Ruby](https://ruby-concurrency.github.io/concurrent-ruby/1.3.6/index.html)
- [@opensource@concurrent-ruby](https://github.com/ruby-concurrency/concurrent-ruby)

## Conditional Statements

# Conditional Statements

Conditional statements allow you to execute different blocks of code based on whether a certain condition is true or false. They provide a way to control the flow of your program, enabling it to make decisions and respond differently to various inputs or situations. Common conditional statements include `if`, `elsif`, and `else`, which let you define different code paths depending on the evaluation of boolean expressions.

Visit the following resources to learn more:

- [@article@Conditional Logic](https://www.theodinproject.com/lessons/ruby-conditional-logic#case-statements)
- [@article@Conditionals](https://launchschool.com/books/ruby/read/flow_control#conditionals)
- [@article@Ruby Explained: Conditionals and Flow Control](https://eriktrautman.com/posts/ruby-explained-conditionals-and-flow-control)

## Conditional Statements

# Conditional Statements

Conditional statements allow you to execute different blocks of code based on whether a certain condition is true or false. They provide a way to control the flow of your program, enabling it to make decisions and respond differently to various inputs or situations. Common conditional statements include `if`, `elsif`, `else`, and `unless`.

Visit the following resources to learn more:

- [@article@Conditional Logic](https://www.theodinproject.com/lessons/ruby-conditional-logic)
- [@article@The Beginner's Guide to Ruby If & Else Statements](http://rubyguides.com/ruby-tutorial/ruby-if-else/)
- [@article@Ruby - if...else, case, unless](https://www.tutorialspoint.com/ruby/ruby_if_else.htm)

## Constants  Variables

# Constants & Variables

In Ruby, variables are named storage locations that hold data, and their values can be changed during the program's execution. Constants, on the other hand, are also named storage locations, but their values are intended to remain fixed throughout the program's runtime. While Ruby technically allows you to reassign a constant (it will issue a warning), the convention is to treat them as immutable values that should not be altered. Variables are typically named using snake\_case, while constants are named using SCREAMING\_SNAKE\_CASE.

Visit the following resources to learn more:

- [@article@Variables](https://ruby-for-beginners.rubymonstas.org/variables.html)
- [@article@Ruby Variables](https://www.tutorialspoint.com/ruby/ruby_variables.htm)
- [@article@Everything You Need to Know About Ruby Constants](https://www.rubyguides.com/2017/07/ruby-constants/)
- [@article@Getting Started with Ruby Variables: A Beginner’s Guide](https://medium.com/@sz.soczewka/getting-started-with-ruby-variables-a-beginners-guide-d90a53eb5139)
- [@video@Variables | Ruby | Tutorial 6](https://www.youtube.com/watch?v=4mWc6Q9shcQ)
- [@video@Ruby Programming Tutorial - 20 - Constants](https://www.youtube.com/watch?v=qAqGIMKIMcA)

## Data Types

# Naming Conventions

Naming conventions are a set of rules or guidelines for choosing names for variables, methods, classes, and other entities in a programming language. These conventions promote code readability, maintainability, and consistency across a project. Following a standard naming scheme helps developers understand the purpose and scope of different elements within the code, making it easier to collaborate and debug.

Visit the following resources to learn more:

- [@article@Ruby Naming Convention](https://namingconvention.org/ruby/)
- [@article@Naming conventions in Ruby language](https://dhanusir.com/ruby/section-two/naming-conventions/)

## Date  Time

# Date & Time

Date and Time represent specific points in time. They allow you to work with dates (year, month, day) and times (hour, minute, second) and perform operations like calculating durations, formatting dates for display, and comparing different points in time. They are essential for handling events, scheduling tasks, and managing temporal data.

Visit the following resources to learn more:

- [@official@class Date](https://docs.ruby-lang.org/en/master/Date.html)
- [@official@class Time](https://docs.ruby-lang.org/en/master/Time.html)
- [@article@How to Use Ruby Time & Date Classes](https://www.rubyguides.com/2015/12/ruby-time/)
- [@article@Ruby - Date & Time](https://www.tutorialspoint.com/ruby/ruby_date_time.htm)
- [@video@Ruby Tutorial For Beginners - Date and Time in Ruby](https://www.youtube.com/watch?v=noUaGvexdok)
- [@video@#62 Ruby Tutorial : Date and DateTime Class Part - 3](https://www.youtube.com/watch?v=htxjcfvGmu4)

## Debug

# Debug

`debug` is a powerful debugging tool integrated directly into Ruby. It allows developers to step through code execution, inspect variables, set breakpoints, and evaluate expressions in real-time. This helps in identifying and resolving errors or unexpected behavior within Ruby programs.

Visit the following resources to learn more:

- [@official@debug](https://github.com/ruby/debug)
- [@article@ruby/debug cheatsheet](https://st0012.dev/2022/09/08/ruby-debug-cheatsheet/)

## Define Method

# define_method

`define_method` is a method used to dynamically create new methods within a class or module. Instead of explicitly writing out the method definition with the `def` keyword, `define_method` allows you to generate methods at runtime, often based on data or logic that isn't known until the program is running. This provides a powerful way to reduce code duplication and create more flexible and adaptable code.

Visit the following resources to learn more:

- [@article@Dynamic method definition with ruby’s .define_method](https://medium.com/@camfeg/dynamic-method-definition-with-rubys-define-method-b3ffbbee8197)
- [@article@Explain Ruby's define_method like I'm five](https://dev.to/tiffanywismer/explain-rubys-definemethod-like-im-five-2807)
- [@video@define_method - Metaprogramming in Ruby](https://www.youtube.com/watch?v=I0itVuoprAY)
- [@video@Ruby Tutorial | Metaprogramming in Ruby - Dynamic Method Definition](https://www.youtube.com/watch?v=bg2KvfwxDnM)

## Defining Classes

# Defining Classes

A class is a blueprint for creating objects. It defines the attributes (data) and behaviors (methods) that objects of that class will possess. Defining a class involves specifying its name and the characteristics that its instances will have. This includes declaring instance variables to hold data and defining methods to perform actions on that data.

Visit the following resources to learn more:

- [@article@How to Write Your Own Classes in Ruby (Explained Clearly)](https://www.rubyguides.com/2019/02/ruby-class/)
- [@article@A Beginner’s Guide to Ruby Classes (Part 1)](https://medium.com/@grahamwatson/a-beginners-guide-to-ruby-classes-f8dec30d5821)
- [@article@Ruby Classes Refresher](https://codesignal.com/learn/courses/ruby-classes-basics-revision/lessons/understanding-ruby-classes-a-refresher-on-attributes-and-methods)
- [@video@Classes & Objects | Ruby | Tutorial 29](https://www.youtube.com/watch?v=sc5RhTIBf4c)
- [@video@Learn classes in Ruby in less than 20 minutes](https://www.youtube.com/watch?v=XyoOOxGR54A)

## Defining Methods

# Defining Methods

Methods, also known as functions in other programming languages, are reusable blocks of code designed to perform a specific task. Defining a method involves specifying its name, the parameters it accepts (if any), and the sequence of instructions it executes. This allows you to organize your code into logical units, making it more readable, maintainable, and reusable throughout your program.

Visit the following resources to learn more:

- [@official@Methods](https://docs.ruby-lang.org/en/master/syntax/methods_rdoc.html)
- [@article@Methods - Odin Project](https://www.theodinproject.com/lessons/ruby-methods)
- [@article@Objects, Classes, Methods](https://ruby-for-beginners.rubymonstas.org/objects.html)
- [@article@Ruby - Methods](https://www.tutorialspoint.com/ruby/ruby_methods.htm)
- [@video@Methods | Ruby | Tutorial 15](https://www.youtube.com/watch?v=e1EpXUgSfN8)

## Dowhile

# do/while Loops

`do/while` loops are a type of control flow statement that executes a block of code at least once, and then repeatedly executes the block as long as a specified condition is true. The condition is checked _after_ the code block is executed, ensuring the block runs at least one time regardless of the initial state of the condition. This is different from a `while` loop, where the condition is checked _before_ the code block is executed.

Visit the following resources to learn more:

- [@article@Ruby Loops](https://www.codecademy.com/resources/docs/ruby/loops)
- [@video@Ruby For Beginners #5 - Loops | For, While, Do, Do While](https://www.youtube.com/watch?v=Q_zP40toAMY)

## Each

# Each

`each` is a fundamental method in Ruby used to iterate over elements within a collection, such as an array or a hash. It applies a given block of code to each element in the collection, allowing you to perform operations on every item. The `each` method does not modify the original collection; it simply iterates through it.

Visit the following resources to learn more:

- [@official@Iterators](https://www.ruby-lang.org/en/documentation/faq/5/)
- [@article@Iterators](https://launchschool.com/books/ruby/read/loops_iterators#iterators)
- [@article@Ruby Explained: Iteration](https://eriktrautman.com/posts/ruby-explained-iteration)

## Enumerable

# Enumerable

Enumerable is a module in Ruby that provides a collection of useful iteration methods. It's designed to be mixed into classes that represent collections of data, such as arrays and hashes. By including Enumerable, a class gains the ability to iterate over its elements and perform operations like searching, filtering, sorting, and transforming data in a concise and readable way.

Visit the following resources to learn more:

- [@official@module Enumerable](https://ruby-doc.org/3.4.1/Enumerable.html)
- [@article@Basic Enumerable Methods](https://www.theodinproject.com/lessons/ruby-basic-enumerable-methods)
- [@article@Enumerable](https://rubyreferences.github.io/rubyref/builtin/types/enumerable.html)
- [@article@An Introduction to Ruby Enumerators and the Enumerable Module](https://betterstack.com/community/guides/scaling-ruby/enumerators-enumerable/)
- [@video@How to use Enumerable with Ruby Classes](https://www.youtube.com/watch?v=zALFRuKZQYc)

## Enumerable

# Conditional Statements

Conditional statements allow you to execute different blocks of code based on whether a certain condition is true or false. They provide a way to control the flow of your program, enabling it to make decisions and respond differently to various inputs or situations. Common conditional statements include `if`, `elsif`, `else`, and `unless`.

Visit the following resources to learn more:

- [@article@Conditional Logic](https://www.theodinproject.com/lessons/ruby-conditional-logic)
- [@article@The Beginner's Guide to Ruby If & Else Statements](http://rubyguides.com/ruby-tutorial/ruby-if-else/)
- [@article@Ruby - if...else, case, unless](https://www.tutorialspoint.com/ruby/ruby_if_else.htm)

## Everything Is An Object

# Everything is an Object

In Ruby, everything you encounter – numbers, strings, arrays, even classes and methods – is treated as an object. This means that each of these entities is an instance of a class and possesses both state (data) and behavior (methods) that can be invoked. This unified object model is a fundamental characteristic of Ruby's design.

Visit the following resources to learn more:

- [@article@Understanding the Ruby Object Model In Depth](https://www.honeybadger.io/blog/ruby-object-model/)
- [@article@Everything is object in Ruby](https://medium.com/@pk60905/everything-is-object-in-ruby-559475ce71dd)
- [@article@Ruby: Everything Is An Object?](https://reinteractive.com/articles/tutorial-series-new-to-rails/ruby-everything-is-an-object)
- [@video@Ruby Programming Tutorial - 9 - Everything is an Object!](https://www.youtube.com/watch?v=F75wFJIa368)

## Fetching

# Fetching

`Enumerable` comes with some methods that allow you to retrieve entries from the Enumerable, without modifying it. This includes methods to get leading and trailing elements, extract minimum and maximum value elements, as well as conduct groups, slices, and partitions.

Visit the following resources to learn more:

- [@article@https://ruby-doc.org/3.4.1/Enumerable.html#top](https://ruby-doc.org/3.4.1/Enumerable.html#top)
- [@article@Getting to know Ruby's Enumerable Module](https://www.rafaelmontas.com/getting-to-know-ruby-enumerable-module/)
- [@article@The Simple Yet Powerful Ruby Enumerable Module](https://www.cloudbees.com/blog/the-enumerable-module)

## Fibers

# Fibers

Fibers are a lightweight way to achieve concurrency. They are essentially blocks of code that can be paused and resumed, allowing you to switch between different execution contexts within a single thread. This enables cooperative multitasking, where the programmer explicitly controls when to switch between different parts of the program.

## Fibers

# Fibers

Fibers are a lightweight concurrency construct that allows you to create code blocks that can be paused and resumed. They provide a way to implement cooperative multitasking within a single thread, enabling you to manage multiple tasks without the overhead of creating and managing multiple threads or processes. Fibers are useful for scenarios where you need fine-grained control over the execution flow and want to avoid the complexities of thread synchronization.

Visit the following resources to learn more:

- [@book@Magesh, "Concurrency in Ruby: Threads, Fibers, and Ractors Demystified"](https://www.youtube.com/watch?v=LVHiq_SbQOE)
- [@official@class Fiber](https://docs.ruby-lang.org/en/master/Fiber.html)
- [@article@How to use Ruby Fibers for Background Jobs](https://medium.com/@alieckaja/unleashing-the-power-of-fibers-for-background-jobs-8a22e3a38cd1)
- [@article@Ruby Fibers 101](https://blog.saeloun.com/2022/03/01/ruby-fibers-101/)

## File Io

# File I/O

File I/O involves reading data from and writing data to files. It allows your Ruby programs to interact with files on your computer's file system. You can open files, read their contents line by line or in chunks, write new data to them, or append data to existing files. This interaction is essential for tasks like reading configuration files, processing data from external sources, and saving program output.

Visit the following resources to learn more:

- [@official@class IO](https://docs.ruby-lang.org/en/master/IO.html)
- [@article@Input & Output (IO) In Ruby: The Definitive Guide](https://www.rubyguides.com/2019/02/ruby-io/)
- [@article@Ruby - FIlei/o](https://www.tutorialspoint.com/ruby/ruby_input_output.htm)
- [@video@Reading Files | Ruby | Tutorial 26](https://www.youtube.com/watch?v=92li0A8d4io)
- [@video@Writing Files | Ruby | Tutorial 27](https://www.youtube.com/watch?v=FW9hDsMY1is)

## Floats

# Floats

Floats represent real numbers with fractional parts in Ruby. They are used to store numerical values that require more precision than integers can provide. Floats are typically represented using a decimal point or in scientific notation.

Visit the following resources to learn more:

- [@official@class Floar](https://docs.ruby-lang.org/en/master/Float.html)
- [@article@Numbers](https://ruby-for-beginners.rubymonstas.org/built_in_classes/numbers.html)
- [@article@Numbers - Odin Project](https://www.theodinproject.com/lessons/ruby-basic-data-types#numbers)
- [@video@03 Ruby Learning Path Integers and Floats](https://www.youtube.com/watch?v=FScOX-TavfA)

## For

# For Loop

The `for` loop in Ruby provides a way to iterate over a sequence of values, such as elements in an array or a range. It executes a block of code for each item in the sequence. While functional, the `for` loop is not as commonly used in Ruby as other iteration methods like `each`, `map`, or `select`, which are often considered more idiomatic and flexible.

Visit the following resources to learn more:

- [@article@For Loops](https://launchschool.com/books/ruby/read/loops_iterators#forloops)
- [@article@For loop](https://www.theodinproject.com/lessons/ruby-loops#for-loop)
- [@video@Ruby For Beginners #5 - Loops | For, While, Do, Do While](https://www.youtube.com/watch?v=Q_zP40toAMY)

## Handling Exceptions

# Handling Exceptions

Exception handling is a mechanism to deal with errors that occur during the execution of a program. It involves identifying potential error-prone sections of code, anticipating possible exceptions, and implementing specific blocks of code to gracefully handle these exceptions, preventing the program from crashing and allowing it to continue execution or terminate in a controlled manner.

Visit the following resources to learn more:

- [@official@Exceptions](https://docs.ruby-lang.org/en/master/language/exceptions_md.html)
- [@official@Exception Handling](https://docs.ruby-lang.org/en/3.4/syntax/exceptions_rdoc.html)
- [@article@Handling Exceptions in Ruby (begin/rescue)](https://medium.com/@alexfarmer/handling-exceptions-in-ruby-b4ba93caf538)
- [@article@Understanding Ruby Error Handling](https://betterstack.com/community/guides/scaling-ruby/ruby-error-handling/)
- [@video@Handling Errors | Ruby | Tutorial 28](https://www.youtube.com/watch?v=J7R94i2bhlI)

## Hashes

# Ruby Hashes

Hashes are collections of key-value pairs. Think of them like dictionaries, where each word (the key) has a definition (the value). Keys are unique within a hash, and they are used to quickly access their corresponding values. Hashes can store any type of data as keys and values, making them a versatile way to organize and retrieve information.

Visit the following resources to learn more:

- [@official@class Hash](https://docs.ruby-lang.org/en/master/Hash.html)
- [@article@What is a Hash](https://launchschool.com/books/ruby/read/hashes#whatisahash)
- [@article@Hashes - Odin Project](https://www.theodinproject.com/lessons/ruby-hashes)
- [@video@Hashes | Ruby | Tutorial 14](https://www.youtube.com/watch?v=BtHKhsDUPwQ)
- [@video@Ruby Programming Tutorial - 31 - Hashes](https://www.youtube.com/watch?v=imns9_XncQU)

## If Elsif Else

# Conditional Statements (if, elsif, else)

Conditional statements allow you to execute different blocks of code based on whether a certain condition is true or false. The `if` statement executes a block of code if a condition is true. The `elsif` statement (optional) allows you to check additional conditions if the initial `if` condition is false. The `else` statement (optional) provides a block of code to execute if none of the preceding conditions are true.

Visit the following resources to learn more:

- [@article@Conditionals](https://ruby-for-beginners.rubymonstas.org/conditionals.html)
- [@article@The Beginner's Guide to Ruby If & Else Statements](https://www.rubyguides.com/ruby-tutorial/ruby-if-else/)
- [@article@Conditional logic](https://www.theodinproject.com/lessons/ruby-conditional-logic)
- [@video@If Statements | Ruby | Tutorial 17](https://www.youtube.com/watch?v=Ss-IHmrSTow)

## Inheritance

# Inheritance

Inheritance in Ruby allows a class (the subclass or derived class) to inherit properties and behaviors from another class (the superclass or base class). This promotes code reuse and establishes an "is-a" relationship. The subclass automatically gains the methods and attributes of the superclass, and can also add its own or override existing ones to customize its behavior.

Visit the following resources to learn more:

- [@article@Inheritance](https://launchschool.com/books/oo_ruby/read/inheritance)
- [@article@Ruby — Inheritance and Module](https://medium.com/swlh/ruby-inheritance-and-module-cc0132348dcd)
- [@article@Ruby Inheritance Explained – Learn OOP Today!](https://www.rubyguides.com/2019/01/what-is-inheritance-in-ruby/)
- [@video@Inheritance | Ruby | Tutorial 33](https://www.youtube.com/watch?v=Zkk7whVb3f4)
- [@video@Ruby Programming Tutorial - 6 - Inheritance](https://www.youtube.com/watch?v=mKXGMdWa1Ow)

## Installers

# Installers

Installers are software packages designed to simplify the process of setting up Ruby on your computer. They typically handle downloading the necessary files, configuring your system environment, and ensuring that Ruby and its related tools are ready to use. Using an installer avoids the complexities of manual installation, making it easier for beginners to get started with Ruby development.

Visit the following resources to learn more:

- [@official@Installers - Ruby Docs](https://www.ruby-lang.org/en/documentation/installation/#installers)
- [@official@RubyInstaller (Windows)](https://rubyinstaller.org/)
- [@official@Ruby Stack](https://bitnami.com/stack/ruby/installer)
- [@opensource@ruby-build (macOS, Linux, UNIX OS)](https://github.com/rbenv/ruby-build#readme)
- [@opensource@ruby-install (macOS, Linux, UNIX OS)](https://github.com/postmodern/ruby-install#readme)

## Installing Ruby

# Installing Ruby

Installing Ruby involves setting up the Ruby interpreter and related tools on your system so you can run Ruby programs. This typically includes downloading a Ruby distribution, configuring your environment, and verifying the installation to ensure everything is working correctly. Different operating systems (like Windows, macOS, and Linux) have their own preferred methods for installing Ruby, often involving package managers or dedicated installers.

Visit the following resources to learn more:

- [@official@Installing Ruby](https://www.ruby-lang.org/en/documentation/installation/)
- [@article@Installing Ruby](https://www.theodinproject.com/lessons/ruby-installing-ruby)
- [@article@How to Install Ruby on Windows, macOS, and Linux](https://dev.to/luigi_ichi/how-to-install-ruby-on-windows-macos-and-linux-35o3)
- [@article@Setting up Ruby on WSL2 using Rbenv](https://codex.org/2022/08/19/setting-up-ruby-wsl2.html)
- [@video@Ruby Beginner Tutorial 2 | How To Install Ruby On Windows](https://www.youtube.com/watch?v=XC1ccTyhLPI)
- [@video@Ruby Beginner Tutorial 3 | How To Install Ruby On MacOS](https://www.youtube.com/watch?v=2pycF6hMy0s)

## Instance Variables

# Instance Variables

Instance variables in Ruby are variables that hold data specific to an object. They are defined within a class but belong to individual instances (objects) of that class. You create an instance variable by prefixing a variable name with an `@` symbol (e.g., `@name`). Each object of the class will have its own copy of these variables, allowing you to store different values for each object's attributes.

Visit the following resources to learn more:

- [@article@Read This If You Want to Understand Instance Variables in Ruby](https://www.rubyguides.com/2019/07/ruby-instance-variables/)
- [@article@Understanding Ruby Objects and Instance Variables](https://dev.to/bhumi/understanding-ruby-objects-and-instance-variables-4157)
- [@video@Instances and Instance Variables in Ruby Programming](https://www.youtube.com/watch?v=H27i3WuAEVI)

## Integers

# Integers

Integers are whole numbers, meaning they don't have any fractional or decimal parts. They can be positive, negative, or zero. In programming, integers are used to represent countable quantities, indices, and other discrete values.

Visit the following resources to learn more:

- [@official@class Integer](https://docs.ruby-lang.org/en/master/Integer.html)
- [@article@Numbers](https://ruby-for-beginners.rubymonstas.org/built_in_classes/numbers.html)
- [@article@Numbers - Odin Project](https://www.theodinproject.com/lessons/ruby-basic-data-types#numbers)
- [@video@03 Ruby Learning Path Integers and Floats](https://docs.ruby-lang.org/en/master/Integer.html)

## Interactive Ruby Irb

# Interactive Ruby (irb)

Interactive Ruby (irb) is a command-line tool that allows you to execute Ruby code interactively. It provides a read-eval-print loop (REPL) environment where you can type in Ruby expressions, and irb will immediately evaluate and display the result. This makes it a valuable tool for experimenting with code, testing ideas, and quickly checking the behavior of Ruby methods and objects.

Visit the following resources to learn more:

- [@article@How To Use IRB to Explore Ruby](https://www.digitalocean.com/community/tutorials/how-to-use-irb-to-explore-ruby)
- [@article@Interactive Ruby](https://ruby-for-beginners.rubymonstas.org/your_tools/irb.html)
- [@article@Interactive Ruby](https://ruby-doc.org/docs/ruby-doc-bundle/Tutorial/part_01/first_steps.html)
- [@video@Interactive Ruby (irb) | Ruby | Tutorial 35](https://www.youtube.com/watch?v=9pKLGhh5mrM)

## Introduction

# Ruby

Ruby is a dynamic, open-source programming language known for its simplicity and productivity. It emphasizes human readability, using a syntax that is easy to learn and write. Ruby is object-oriented, meaning everything is treated as an object, and it supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

Visit the following resources to learn more:

- [@book@The Ruby Programming Language](https://github.com/maniramakumar/the-best-ruby-books/blob/master/books/The%20Ruby%20Programming%20Language.pdf)
- [@official@Ruby](https://www.ruby-lang.org/en/)
- [@official@Documentation](https://www.ruby-lang.org/en/documentation/)
- [@official@Ruby in Twenty Minutes](https://www.ruby-lang.org/en/documentation/quickstart/)
- [@article@Ruby Tutorial](https://www.tutorialspoint.com/ruby/index.htm)
- [@article@Learn Ruby Online](https://www.learnrubyonline.org/)
- [@video@Ruby Programming Language - Full Course](https://www.youtube.com/playlist?list=PL_EzhIKp343lBMH4UuklrMRL_WkilGoXe)
- [@video@Masterclass | Ruby Programming in 1 video | Beginners Ruby HandsOn Crash Course Interview FAQs |](https://www.youtube.com/watch?v=xyDoP5a_dvo)
- [@feed@Explore top posts about Ruby](https://app.daily.dev/tags/ruby?ref=roadmapsh)

## Irb

# Debugging with IRB

IRB (Interactive Ruby) is a powerful tool for debugging Ruby code. It allows you to execute Ruby code line by line, inspect variables, and test code snippets in real-time. This interactive environment helps you understand how your code behaves, identify errors, and experiment with different solutions without having to run your entire program. You can use IRB to step through your code, set breakpoints, and examine the state of your application at any point during execution.

Visit the following resources to learn more:

- [@official@Debugging with IRB](https://ruby.github.io/irb/#label-Debugging+with+IRB)
- [@article@A Beginner’s Guide to Debugging in Ruby](https://medium.com/@claire_logan/a-beginners-guide-to-debugging-in-ruby-b8103d7ad35b)
- [@video@Ruby Debugging Tools: irb, pry, byebug, debug | Talk.rb](https://www.youtube.com/watch?v=Jx5SdGUezY0)

## Iterating

# Iterating with Enumerable

The `Enumerable` module in Ruby provides a collection of methods that allow you to traverse and process elements within a collection (like an array or hash). These iterating methods, such as `each`, `map`, `select`, and `reject`, simplify the process of performing actions on each item in the collection, transforming the collection, or filtering elements based on specific conditions. They abstract away the need for manual indexing and provide a more concise and readable way to work with collections.

Visit the following resources to learn more:

- [@article@module Enumerable](https://ruby-doc.org/3.4.1/Enumerable.html#top)
- [@article@Programación Iterating in Ruby: Enumerable and Enumerators](https://libreim.github.io/blog/2015/08/24/ruby-enumerators/)
- [@article@Understanding Ruby - Enumerable - Iterating and Taking](https://dev.to/baweaver/understanding-ruby-enumerable-iterating-and-taking-1fga)

## Lambdas

# Lambdas

Lambdas are anonymous functions, meaning they are functions without a name. They are objects in Ruby and can be treated like any other object, such as being passed as arguments to methods or stored in variables. Lambdas are defined using the `lambda` keyword or the shorthand `->` syntax, and they are similar to procs but differ in how they handle arguments and `return` statements.

Visit the following resources to learn more:

- [@article@An Introduction to Lambdas in Ruby](https://blog.appsignal.com/2023/06/21/an-introduction-to-lambdas-in-ruby.html)
- [@article@https://www.rubyguides.com/2016/02/ruby-procs-and-lambdas/](https://www.rubyguides.com/2016/02/ruby-procs-and-lambdas/)
- [@article@How to Use Lambdas in Ruby](https://www.scoutapm.com/blog/how-to-use-lambdas-in-ruby)
- [@video@Ruby Blocks, Procs, and Lambdas 🦁🐅🐻](https://www.youtube.com/watch?v=SADF5diqAJk)
- [@video@Blocks, Procs, and Lambda Functions in Ruby](https://www.youtube.com/watch?v=Dh3cSYjHITI)

## Logical

# Logical Operators in Ruby

Logical operators in Ruby let you combine or modify boolean expressions (true or false). The main ones are `&&` (and), `||` (or), and `!` (not). `&&` returns true only if both operands are true. `||` returns true if at least one operand is true. `!` reverses the boolean value of its operand, turning true into false and vice versa. These operators are fundamental for controlling program flow based on different conditions.

Visit the following resources to learn more:

- [@article@Logical operators](https://ruby-for-beginners.rubymonstas.org/operators/logical.html)
- [@article@Ruby - Operators](https://www.tutorialspoint.com/ruby/ruby_operators.htm)

## Loops  Enumerations

# Loops & Enumerations

Loops in Ruby allow you to execute a block of code repeatedly. Enumerations, on the other hand, are methods that iterate over collections like arrays and hashes, applying a block of code to each element. Both loops and enumerations provide ways to process data and perform actions multiple times, but enumerations are often preferred for their conciseness and readability when working with collections.

Visit the following resources to learn more:

- [@article@Loops and Iterators](https://launchschool.com/books/ruby/read/loops_iterators#simpleloop)
- [@article@Loops](https://www.theodinproject.com/lessons/ruby-loops)
- [@article@Ruby Loops: Repeating Something Many Times](https://www.rubyguides.com/ruby-tutorial/loops/)
- [@article@Ruby - Loops](https://www.tutorialspoint.com/ruby/ruby_loops.htm)

## Managers

# Ruby Version Managers

Ruby version managers are tools that allow you to install and manage multiple versions of Ruby on the same system. This is useful because different projects may require different Ruby versions, and using a version manager prevents conflicts and simplifies switching between them. They typically work by modifying your shell environment to point to the desired Ruby installation.

Visit the following resources to learn more:

- [@official@Managers - Ruby Docs](https://www.ruby-lang.org/en/documentation/installation/#managers)

## Metaprogramming

# Metaprogramming

Metaprogramming is essentially writing code that manipulates other code. It allows you to define methods, classes, or even modify existing ones at runtime. This means your program can dynamically adapt and change its behavior based on conditions or data it encounters while running, rather than being fixed at compile time.

Visit the following resources to learn more:

- [@book@Metaprogramming Ruby.pdf](https://theswissbay.ch/pdf/Gentoomen%20Library/Programming/Ruby/Metaprogramming%20Ruby.pdf)
- [@article@Ruby Metaprogramming: How to Write Dynamic Code](https://betterstack.com/community/guides/scaling-ruby/metaprogramming/)
- [@article@An Introduction to Metaprogramming in Ruby](https://blog.appsignal.com/2023/07/26/an-introduction-to-metaprogramming-in-ruby.html)
- [@article@Ruby Metaprogramming: Real-World Examples](https://www.rubyguides.com/2016/04/metaprogramming-in-the-wild/)
- [@article@Ruby Metaprogramming Secrets](https://www.rubyguides.com/guides/metaprogramming-guide.pdf)
- [@video@RubyConf 2022: In Defense of Ruby Metaprogramming By Noel Rappin](https://www.youtube.com/watch?v=D_ZRaZucjm4)

## Method Lookup

# Method Lookup

Method lookup is the process a programming language uses to determine which method to execute when a method is called on an object. It involves searching through the object's class and its ancestors (inheritance hierarchy) to find the appropriate method definition. The search typically starts with the object's class and proceeds up the inheritance chain until a matching method is found.

Visit the following resources to learn more:

- [@article@Understanding Ruby Method Lookup](https://www.honeybadger.io/blog/ruby-method-lookup/)
- [@article@Better Know A Ruby Thing: Method Lookup](https://noelrappin.com/blog/2025/03/better-know-a-ruby-thing-method-lookup/)

## Method Parameters

# Method Parameters

Method parameters, also called arguments, are the values you pass into a method when you call it. There are several types: required parameters, which must be provided; optional parameters, which have default values if not provided; and variable-length arguments (using `*args`), which allow you to pass in an arbitrary number of arguments as an array. Arbitrary keyword arguments (using `**args`) allow you to pass arguments by name, and can also be required or optional. Block parameters (using `&block`) allow you to pass a block of code to a method.

Visit the following resources to learn more:

- [@official@Arguments](https://docs.ruby-lang.org/en/master/syntax/methods_rdoc.html#label-Arguments)
- [@article@Parameters and arguments](https://www.theodinproject.com/lessons/ruby-methods#parameters-and-arguments)
- [@article@Methods](https://launchschool.com/books/ruby/read/methods)
- [@video@How to Use Method Arguments in Ruby](https://www.youtube.com/watch?v=rwVWKx-fQDg)

## Method Missing

# method_missing

`method_missing` is a Ruby method that gets called when you try to invoke a method on an object that doesn't exist. Instead of raising a `NoMethodError`, Ruby gives you a chance to handle the missing method call yourself. This allows you to dynamically respond to method calls based on the method name and arguments provided, enabling flexible and expressive code.

Visit the following resources to learn more:

- [@article@Metaprogramming in Ruby: method_missing](https://josh-works.medium.com/metaprogramming-in-ruby-method-missing-f6d7f7f6aef5)
- [@article@Ruby Metaprogramming - Method Missing](https://www.leighhalliday.com/ruby-metaprogramming-method-missing)
- [@video@How and why to use Ruby’s method_missing](https://www.youtube.com/watch?v=rp1luOKyT9g)
- [@video@Ruby Tutorial | Metaprogramming in Ruby - Method Missing](https://www.youtube.com/watch?v=AVfp6V-lEZo)

## Minitest

# Minitest

Minitest is a complete testing suite for Ruby. It provides support for test-driven development (TDD), behavior-driven development (BDD), mocking, and benchmarking. It's a lightweight and fast testing framework that's included in the Ruby standard library, making it readily available for use in Ruby projects without requiring additional installations.

Visit the following resources to learn more:

- [@roadmap@Ruby Minitest Tutorial](https://www.youtube.com/watch?v=Reso8FlRRAc)
- [@opensource@minitest](https://github.com/minitest/minitest)
- [@article@MiniTest - Writing Test Code In Ruby (2/3)](https://dev.to/exampro/minitest-writing-test-code-in-ruby-part-2-of-3-4306)
- [@article@Getting Started with Minitest](https://www.cloudbees.com/blog/getting-started-with-minitest)

## Modules  Mixins

# Modules & Mixins

Modules in Ruby are collections of methods, classes, and constants. They provide a way to namespace and prevent naming conflicts. Mixins allow you to incorporate module functionality into classes, enabling code reuse and multiple inheritance-like behavior. By including a module in a class, the class gains access to the module's methods, effectively "mixing in" the module's functionality.

Visit the following resources to learn more:

- [@official@Module](https://ruby-doc.org/core-2.5.0/Module.html)
- [@article@A Beginner's Guide to Ruby Modules and Mixins](https://betterstack.com/community/guides/scaling-ruby/modules-mixins/)
- [@article@Mixing in Modules](https://launchschool.com/books/oo_ruby/read/inheritance#mixinginmodules)
- [@article@Ruby — Inheritance and Module](https://medium.com/swlh/ruby-inheritance-and-module-cc0132348dcd)
- [@video@Modules | Ruby | Tutorial 34](https://www.youtube.com/watch?v=Cq_dKYAqMrI&pp=ygUMcnVieSBtb2R1bGVz)

## Monkey Patching

# Monkey Patching

Monkey patching is a technique that allows you to add, modify, or replace existing code in a class or module at runtime. This means you can change the behavior of classes and modules, even those defined in external libraries, without directly altering their source code. It's a powerful tool for extending functionality or fixing bugs, but it should be used with caution as it can lead to unexpected side effects and make code harder to maintain.

Visit the following resources to learn more:

- [@article@Responsible Monkeypatching in Ruby](https://blog.appsignal.com/2021/08/24/responsible-monkeypatching-in-ruby.html)
- [@video@Introduction to Monkey Patching In Ruby](https://www.youtube.com/watch?v=BH8-1SK7ZYI)

## Mutex

# Mutex

A mutex (mutual exclusion) is a synchronization primitive that provides exclusive access to a shared resource. It essentially acts as a lock, ensuring that only one thread or process can access a critical section of code at any given time. This prevents race conditions and data corruption that can occur when multiple threads try to modify the same data simultaneously.

## Naming Conventions

# Naming Conventions

Naming conventions are a set of rules or guidelines for choosing names for variables, methods, classes, and other entities in a programming language. These conventions promote code readability, maintainability, and consistency across projects. Following a standard naming style helps developers understand the purpose and scope of different elements within the code more easily.

Visit the following resources to learn more:

- [@article@Ruby Naming Convention](https://namingconvention.org/ruby/)
- [@article@Naming conventions in Ruby language](https://dhanusir.com/ruby/section-two/naming-conventions/)

## Naming Conventions

# Naming Conventions

Naming conventions are a set of rules or guidelines for choosing names for variables, methods, classes, and other entities in a programming language. These conventions promote code readability, maintainability, and consistency across a project. Following a standard naming scheme helps developers understand the purpose and scope of different elements within the code, making it easier to collaborate and debug.

Visit the following resources to learn more:

- [@article@Ruby Naming Convention](https://namingconvention.org/ruby/)
- [@article@Naming conventions in Ruby language](https://dhanusir.com/ruby/section-two/naming-conventions/)

## Next

# Next Keyword in Loops

The `next` keyword in Ruby provides a way to skip the current iteration of a loop and proceed directly to the next iteration. When `next` is encountered within a loop (like `for`, `while`, `until`, or iterators like `each`), the remaining code in the current loop cycle is bypassed, and the loop immediately begins its next cycle, if one exists. This is useful for skipping certain elements or conditions within a collection or range.

Visit the following resources to learn more:

- [@article@Controlling Loop Execution](https://launchschool.com/books/ruby/read/loops_iterators#controllloop)
- [@article@Ruby Explained: Iteration](https://eriktrautman.com/posts/ruby-explained-iteration)
- [@article@Understanding The Ruby Next & Break Keywords](https://www.rubyguides.com/2019/09/ruby-next-break-keywords/)

## Nil

# Nil

`nil` represents the absence of a value or a non-existent object. It's a special object in Ruby that signifies emptiness or the lack of a meaningful result. Think of it as a placeholder indicating that a variable or expression doesn't currently hold a valid value.

Visit the following resources to learn more:

- [@article@Nothingness and the truth](http://ruby-for-beginners.rubymonstas.org/conditionals/nothing_and_truth.html)
- [@article@Everything You Need to Know About Nil](https://www.rubyguides.com/2018/01/ruby-nil/)
- [@article@True, False, and Nil](https://ruby-for-beginners.rubymonstas.org/built_in_classes/true_false_nil.html)
- [@video@Ruby Nil Explained](https://www.youtube.com/watch?v=mBJrQ84f6-4)

## Operators

# Operators

Operators are special symbols in Ruby that perform operations on one or more operands (values or variables). These operations can include arithmetic calculations (like addition and subtraction), comparisons (like checking if two values are equal), logical evaluations (like determining if a condition is true or false), and assignment of values to variables. They are fundamental building blocks for creating expressions and controlling the flow of logic in Ruby programs.

Visit the following resources to learn more:

- [@official@Operators](https://docs.ruby-lang.org/en/3.4/syntax/operators_rdoc.html)
- [@article@Everything You Need to Know About Ruby Operators](https://www.rubyguides.com/2018/07/ruby-operators/)
- [@article@Ruby - Operators](https://www.tutorialspoint.com/ruby/ruby_operators.htm)

## Package Managers

# Package Managers

Package managers simplify the process of installing and managing software, including Ruby, on your system. Instead of manually downloading and configuring Ruby, you can use a package manager specific to your operating system. For example, on macOS, you might use Homebrew, while on Debian/Ubuntu Linux, you'd use apt. These tools handle dependencies and ensure Ruby is installed correctly, making the setup process much easier.

Visit the following resources to learn more:

- [@official@Package Management Systems](https://www.ruby-lang.org/en/documentation/installation/#package-management-systems)

## Procs

# Procs

A Proc in Ruby is an object that represents a block of code that can be stored, passed around, and executed later. Think of it as a named, reusable chunk of code. Unlike regular methods, Procs are objects, allowing them to be treated like any other variable, passed as arguments to methods, and stored in data structures. They capture the surrounding context in which they are defined, meaning they have access to variables and methods available at the time of their creation.

Visit the following resources to learn more:

- [@official@class Proc](https://docs.ruby-lang.org/en/master/Proc.html)
- [@article@The Ultimate Guide to Blocks, Procs & Lambdas](https://www.rubyguides.com/2016/02/ruby-procs-and-lambdas/)
- [@article@Understanding Ruby Proc objects](https://www.codewithjason.com/ruby-procs/)
- [@video@Blocks, Procs, and Lambda Functions in Ruby](https://www.youtube.com/watch?v=Dh3cSYjHITI)
- [@video@Ruby Blocks, Procs, and Lambdas 🦁🐅🐻](https://www.youtube.com/watch?v=SADF5diqAJk)

## Pry

# Pry

Pry is a powerful Ruby runtime developer console and an alternative to `irb`. It offers features like syntax highlighting, code browsing, documentation lookup, and the ability to step through code execution. Pry allows developers to pause program execution at any point, inspect variables, and even modify code on the fly, making it an invaluable tool for debugging and understanding Ruby code.

Visit the following resources to learn more:

- [@article@Debugging Ruby Code with Pry](https://laflamablanc.medium.com/debugging-ruby-code-with-pry-a0bf1f5e97ca)
- [@article@Debugging in Ruby with pry-byebug](https://blog.appsignal.com/2024/05/08/debugging-in-ruby-with-pry-byebug.html)
- [@article@Pry debugging](https://docs.gitlab.com/development/pry_debugging/)
- [@video@Debugging Ruby with PRY](https://www.youtube.com/watch?v=dPDrgpWakrA)

## Puts Print P

# Puts, Print, and P

`puts`, `print`, and `p` are methods in Ruby used to display output to the console. `puts` prints the given arguments followed by a newline character, `print` prints the arguments as they are without adding a newline, and `p` prints a human-readable representation of the given object, which is useful for debugging.

Visit the following resources to learn more:

- [@article@Understanding The Differences Between Puts, Print & P](https://www.rubyguides.com/2018/10/puts-vs-print/)
- [@article@puts vs print vs p in Ruby](https://flexiple.com/ruby-on-rails/puts-vs-p-vs-print-ruby)
- [@video@Differences Between Print, Puts & P in Ruby](https://www.youtube.com/watch?v=9jSwVvyjAKE)

## Querying

# Querying Enumerable Collections

Enumerable querying methods in Ruby allow you to gather information _about_ a collection without necessarily extracting or transforming its elements. These methods check for the presence of elements that meet certain conditions, determine the size or characteristics of the collection, or verify if all or any elements satisfy a given criteria. They return boolean values, counts, or other summary data about the Enumerable itself, rather than returning a modified Enumerable.

Visit the following resources to learn more:

- [@article@Methods for Querying](https://ruby-doc.org/3.4.1/Enumerable.html#module-Enumerable-label-Methods+for+Querying)
- [@article@Getting to know Ruby's Enumerable Module](https://www.rafaelmontas.com/getting-to-know-ruby-enumerable-module/)

## Rack

# Rack

Rack provides a minimal interface between web servers and Ruby frameworks. By abstracting the connection between the server and the application, Rack allows developers to write Ruby web applications that can run on a variety of web servers with minimal configuration. It essentially provides a common API for handling HTTP requests and responses.

Visit the following resources to learn more:

- [@opensource@rack](https://github.com/rack/rack)
- [@article@The Basics of Rack for Ruby](https://blog.appsignal.com/2024/10/30/the-basics-of-rack-for-ruby.html)
- [@article@What is Ruby Rack? — Build your first Rack app](https://cdragon.medium.com/what-is-ruby-rack-build-your-first-rack-app-32771cde34d9)
- [@video@What is Rack? How does it work? A brief guide for Ruby on Rails Developers](https://www.youtube.com/watch?v=C4wy8L--FmE)
- [@video@Rack - The BEST Ruby Web Framework](https://www.youtube.com/watch?v=PzMNycHMmws)

## Ractors

# Ractors

Ractors are an actor-model-based concurrency abstraction in Ruby, designed to allow for parallel execution. They provide a way to isolate data and execution between different parts of a program, minimizing shared mutable state and thus simplifying concurrent programming by preventing common issues like race conditions. Each Ractor runs in its own thread and has its own isolated heap, communicating with other Ractors through message passing.

Visit the following resources to learn more:

- [@official@Ractor](https://docs.ruby-lang.org/en/3.4/ractor_md.html)
- [@article@An Introduction to Ractors in Ruby](https://blog.appsignal.com/2022/08/24/an-introduction-to-ractors-in-ruby.html)

## Ranges

# Ranges

Ranges in Ruby are used to create a sequence of values. They are defined using two endpoints, which can be numbers, characters, or any objects that can be compared using the `<=>` operator. Ranges can be inclusive (including the last value) or exclusive (excluding the last value), denoted by `..` and `...` respectively. They are commonly used for iterating over a sequence, creating subsets of arrays, and checking if a value falls within a specific interval.

Visit the following resources to learn more:

- [@article@Range operators](https://kddnewton.com/2023/07/20/ruby-operators.html#range-operators)
- [@article@Ruby - Operators](https://www.tutorialspoint.com/ruby/ruby_operators.htm)

## Rbenv

# Rbenv

Rbenv is a command-line tool that allows you to easily manage multiple Ruby environments (versions) on a single system. It works by intercepting Ruby commands and determining which Ruby version to use based on the current directory or a global setting. This enables you to work on different projects that require different Ruby versions without conflicts.

Visit the following resources to learn more:

- [@official@Rbenv](https://rbenv.org/)
- [@opensource@rbenv](https://github.com/rbenv/rbenv)
- [@article@Rbenv — How it works](https://medium.com/@Sudhagar/rbenv-how-it-works-e5a0e4fa6e76)
- [@article@rbenv cheatsheet](https://devhints.io/rbenv)
- [@article@rbenv vs RVM: Picking Your Ruby Version Manager Buddy](https://dev.to/lovestaco/rbenv-vs-rvm-picking-your-ruby-version-manager-buddy-4130)

## Rdoc

# RDoc

RDoc is a documentation generator for Ruby source code. It parses Ruby files and creates HTML or other formatted documentation based on comments and code structure. It's the standard tool for generating API documentation for Ruby projects, allowing developers to easily understand and use libraries and applications.

Visit the following resources to learn more:

- [@official@RDoc - Ruby Documentation System](https://ruby.github.io/rdoc/)
- [@opensource@rdoc](https://github.com/ruby/rdoc)
- [@video@Reading and using Ruby Documentation - Rdoc](https://www.youtube.com/watch?v=opvB-_vycTs)

## Recursion

# Recursion

Recursion is a programming technique where a function calls itself within its own definition. This creates a loop-like behavior, but instead of using explicit loops (like `for` or `while`), the function breaks down a problem into smaller, self-similar subproblems until it reaches a base case, which stops the recursion and returns a value. The results from each recursive call are then combined to produce the final solution.

Visit the following resources to learn more:

- [@article@How to Use Recursion & Memoization in Ruby](https://www.rubyguides.com/2015/08/ruby-recursion-and-memoization/)
- [@article@Simple Recursion in Practice with Ruby](https://codesignal.com/learn/courses/easy-interview-coding-practice-in-ruby/lessons/simple-recursion-in-practice-with-ruby)
- [@video@Ruby Recursion Explained!](https://www.youtube.com/watch?v=5JyJWdOP8PM)

## Redo

# Redo

`redo` is a control flow statement in Ruby used within loops (like `for`, `while`, `until`) and iterators (like `each`, `map`). When `redo` is encountered, it restarts the current iteration of the loop or iterator from the beginning, without evaluating any remaining code in that iteration. It essentially repeats the current step.

Visit the following resources to learn more:

- [@article@Ruby's redo, retry and next keywords](https://blog.appsignal.com/2018/06/05/redo-retry-next.html)
- [@article@The redo Keyword in Ruby](https://medium.com/rubycademy/the-redo-keyword-in-ruby-3f150d69e3c2)
- [@video@#23 Ruby Tutorial - NEXT and REDO statements with codes in Ruby](https://www.youtube.com/watch?v=oHlSMSawyc8)

## Refinements

# Refinements

Refinements provide a way to modify the behavior of a class or module within a specific scope, without affecting the global definition of that class or module. This allows you to introduce changes or extensions to existing code in a localized manner, preventing unintended side effects in other parts of your application. Refinements are particularly useful for managing dependencies and avoiding conflicts when working with shared code or libraries.

Visit the following resources to learn more:

- [@article@The Pros and Cons of Ruby Refinements](https://www.cloudbees.com/blog/ruby-refinements)
- [@article@Understanding Ruby refinements and lexical scope](https://www.honeybadger.io/blog/understanding-ruby-refinements-and-lexical-scope/)
- [@article@Refinement: The Correct Way To Monkey-Patch in Ruby](https://reinteractive.com/articles/tutorial-series-for-experienced-rails-developers/ruby-refinements-vs-monkey-patching-best-practices)

## Regex

# Regular Expressions in Ruby

Regular expressions (regex) are patterns used to match character combinations in strings. In Ruby, you can use regex to search, replace, or validate text within strings. They are defined using forward slashes (`/pattern/`) or the `%r{pattern}` syntax and provide a powerful way to manipulate and analyze text data based on specific patterns.

Visit the following resources to learn more:

- [@official@class Regexp](https://docs.ruby-lang.org/en/master/Regexp.html)
- [@article@Mastering Ruby Regular Expressions](https://www.rubyguides.com/2015/06/ruby-regex/)
- [@article@Regular Expressions](https://ruby-for-beginners.rubymonstas.org/advanced/regular_expressions.html)
- [@article@Cool Ruby regex tricks](https://www.honeybadger.io/blog/ruby-regex-tricks/)
- [@video@Ruby for Newbies: Regular Expressions](https://www.youtube.com/watch?v=hy6KUoU34_w)
- [@video@Ruby Programming Tutorial - 23 - Beginning Regular Expressions](https://www.youtube.com/watch?v=q70q-QyIios)

## Rspec

# RSpec

RSpec is a testing tool for Ruby. It provides a domain-specific language (DSL) for writing tests in a clear and readable format. RSpec focuses on behavior-driven development (BDD), allowing developers to describe the expected behavior of their code in a way that is easy to understand and maintain.

Visit the following resources to learn more:

- [@official@RSpec](https://rspec.info/)
- [@article@Getting Started with RSpec](https://semaphore.io/community/tutorials/getting-started-with-rspec)
- [@article@Introduction to RSpec](https://www.theodinproject.com/lessons/ruby-introduction-to-rspec)
- [@video@RSpec Ruby Tutorial](https://www.youtube.com/watch?v=FgGOa7Mxoxg&list=PL_noPv5wmuO9Z3h_Nq4aEPfzGqrJzhthb)
- [@video@How to Test Your Ruby Code With RSpec](https://www.youtube.com/watch?v=LdutLs5-ObI)

## Rubocop

# RuboCop

RuboCop is a static code analyzer and formatter for Ruby. It inspects Ruby code and reports style issues, potential errors, and code smells based on a community-driven Ruby style guide. RuboCop can also automatically correct many of these issues, ensuring code consistency and improving overall code quality.

Visit the following resources to learn more:

- [@official@RuboCop](https://rubocop.org/)
- [@official@RuboCop Docs](https://docs.rubocop.org/rubocop/1.82/index.html)
- [@opensource@rubocop](https://github.com/rubocop/rubocop)
- [@article@Using RuboCop for Effective Ruby Code Linting](https://betterstack.com/community/guides/scaling-ruby/rubocop/)
- [@video@RubyConf 2022: Analyzing an analyzer - A dive into how RuboCop works by Kyle d'Oliveira](https://www.youtube.com/watch?v=LAo-PYs6bp0)

## Ruby Dsl

# Ruby DSLs

A Domain Specific Language (DSL) is a programming language designed for a particular kind of application. Instead of being a general-purpose language that can solve a wide range of problems, a DSL is focused on solving problems in a specific domain, making code more readable and maintainable within that domain. Ruby's flexible syntax makes it well-suited for creating internal DSLs, which are DSLs implemented within Ruby itself, leveraging Ruby's features to create a more expressive and concise syntax for a specific task.

Visit the following resources to learn more:

- [@article@Creating a Ruby DSL: A Guide to Advanced Metaprogramming](https://www.toptal.com/developers/ruby/ruby-dsl-metaprogramming-guide)
- [@article@Writing a Domain-Specific Language in Ruby](https://thoughtbot.com/blog/writing-a-domain-specific-language-in-ruby)
- [@article@Crafting a Ruby configuration DSL: Lessons learned](https://vaisakhvm.medium.com/crafting-a-ruby-configuration-dsl-lessons-learned-8bbb0958c670)

## Ruby On Rails

# Ruby on Rails

Ruby on Rails is a server-side web application framework written in Ruby under the MIT License. Rails is a model-view-controller (MVC) framework, providing default structures for a database, a web service, and web pages. It encourages the use of web standards such as JSON or XML for data transfer, and HTML, CSS, and JavaScript for the user interface.

Visit the following resources to learn more:

- [@official@Ruby on Rails](https://rubyonrails.org/)
- [@official@Getting Started with Rails](https://guides.rubyonrails.org/getting_started.html)
- [@opensource@rails](https://github.com/rails/rails)
- [@article@Ruby vs Ruby on Rails: What’s the Difference?](https://kinsta.com/blog/ruby-vs-ruby-on-rails/)
- [@article@Visit the Dedicated Ruby on Rails Roadmap](https://roadmap.sh/ruby-on-rails)
- [@video@Learn Ruby on Rails - Full Course](https://www.youtube.com/watch?v=fmyvWz5TUWg)
- [@video@Ruby on Rails in 100 Seconds](https://www.youtube.com/watch?v=2DvrRadXwWY)

## Rubygems

# RubyGems

RubyGems is a package management system for the Ruby programming language. It provides a standard format for distributing Ruby programs and libraries (called "gems"), a tool for easily installing gems, and a central repository ([RubyGems.org](http://RubyGems.org)) for finding and sharing them. It simplifies the process of managing dependencies and distributing reusable code in the Ruby ecosystem.

Visit the following resources to learn more:

- [@official@RubyGems](https://rubygems.org/)
- [@official@Libraries](https://www.ruby-lang.org/en/libraries/)
- [@official@RubyGems Basics](https://guides.rubygems.org/rubygems-basics/)
- [@opensource@rubygems](https://github.com/ruby/rubygems)
- [@video@What Are RubyGems - Explained](https://www.youtube.com/watch?v=M4szKwqFHKs)

## Rubymine

# RubyMine

RubyMine is an Integrated Development Environment (IDE) specifically designed for Ruby and Ruby on Rails development. It provides a comprehensive suite of tools for coding, testing, debugging, and deploying Ruby applications, aiming to enhance developer productivity through features like intelligent code completion, refactoring, and integration with various testing frameworks and version control systems.

Visit the following resources to learn more:

- [@official@RubyMine](https://www.jetbrains.com/ruby/)
- [@article@Introduction to RubyMine — A Powerful Ruby Development Tool](https://medium.com/@AlexanderObregon/introduction-to-rubymine-a-powerful-ruby-development-tool-4127851de5f9)
- [@video@RubyMine vs VSCode (2026): Which Is The Best IDE For Ruby on Rails?](https://www.youtube.com/watch?v=WIc1de6_1MM)
- [@video@Episode #526 - RubyMine](https://www.youtube.com/watch?v=j3hv7pz1ROc)

## Running Ruby

# Running Ruby

Running Ruby code involves executing instructions written in the Ruby programming language. This can be done through various methods, including using the Ruby interpreter directly from the command line, executing Ruby scripts, or running Ruby code within a web server environment like Rails. The interpreter reads and executes the code line by line, producing the desired output or performing the specified actions.

Visit the following resources to learn more:

- [@official@Ruby in Twenty Minutes](https://www.ruby-lang.org/en/documentation/quickstart/)
- [@article@Ruby Programming/Hello world](https://en.wikibooks.org/wiki/Ruby_Programming/Hello_world)
- [@article@How To Write Your First Ruby Program](https://www.digitalocean.com/community/tutorials/how-to-write-your-first-ruby-program)
- [@video@Ruby - Install and Hello World](https://www.youtube.com/watch?v=zmBNDZyYVpM)

## Rvm

# RVM

RVM (Ruby Version Manager) is a command-line tool that allows you to easily manage multiple Ruby environments on a single system. It enables you to install, manage, and work with different Ruby versions (like Ruby 2.7, 3.0, or JRuby) and gemsets (isolated collections of gems) independently. This prevents conflicts between projects that require different Ruby versions or gem dependencies.

Visit the following resources to learn more:

- [@official@RVM](https://rvm.io/)
- [@opensource@rvn](https://github.com/rvm/rvm)
- [@article@What’s an RVM and Why You Should Use it for Rails Apps?](https://medium.com/@moulayjam/whats-an-rvm-and-why-you-should-use-it-for-rails-apps-b5cced2469a8)
- [@article@rbenv vs RVM: Picking Your Ruby Version Manager Buddy](https://dev.to/lovestaco/rbenv-vs-rvm-picking-your-ruby-version-manager-buddy-4130)

## Scope

# Scope

Scope refers to the visibility and accessibility of variables within different parts of a program. It determines where a variable can be accessed and used. Understanding scope is crucial for avoiding naming conflicts and ensuring that data is accessed and modified correctly within different parts of your Ruby code.

Visit the following resources to learn more:

- [@official@Scope](https://docs.ruby-lang.org/en/master/syntax/methods_rdoc.html#label-Scope)
- [@article@Variable Scope and Access in Ruby: The Important Parts](https://ethanweiner.medium.com/variable-scope-and-access-in-ruby-the-important-parts-dc2d146977b3)
- [@article@Method Definition and Local Variable Scope](https://launchschool.com/books/ruby/read/methods)
- [@video@Methods & Variable Scope in Ruby](https://www.youtube.com/watch?v=rzZK79C6nSI)

## Search Algorithms

# Search Algorithms

Search algorithms are methods used to find a specific element within a collection of data, like an array or a hash. These algorithms work by systematically checking each element in the data structure until the desired element is found or it's determined that the element is not present. Common examples include linear search, which checks each element sequentially, and binary search, which efficiently finds elements in sorted data by repeatedly dividing the search interval in half.

Visit the following resources to learn more:

- [@article@Search algorithms with Ruby](https://dev.to/daviducolo/search-algorithms-in-ruby-3nbj)
- [@article@Search Algorithms in Ruby](https://medium.com/@limichelle21/search-algorithms-in-ruby-c3b8c9b70451)
- [@article@Introduction to Binary Search](https://codesignal.com/learn/courses/sorting-and-searching-algorithms-in-ruby/lessons/introduction-to-binary-search-in-ruby)
- [@video@Binary Search & Linear Search: Algorithms With Ruby](https://www.youtube.com/watch?v=7RPr83FYEkE)

## Searching  Filtering

# Searching and Filtering in Enumerable

`Enumerable` comes with some methods that allow you to select specific elements from a collection based on certain criteria. This allows you to extract subsets of data that meet your desired conditions, making it easier to work with large datasets or focus on relevant information. Common operations include finding the first element that satisfies a condition, selecting all elements that match a pattern, or rejecting elements that don't meet specific requirements.

Visit the following resources to learn more:

- [@article@module Enumerable](https://ruby-doc.org/3.4.1/Enumerable.html#top)
- [@article@Getting to know Ruby's Enumerable Module](https://www.rafaelmontas.com/getting-to-know-ruby-enumerable-module/)
- [@article@Understanding Ruby - Enumerable - Searching and Filtering](https://dev.to/baweaver/understanding-ruby-enumerable-searching-and-filtering-23o7)

## Send

# Send

`send` in Ruby is a method that allows you to call other methods on an object dynamically by their name, which is passed as a symbol or string. It essentially bypasses the usual method call syntax, enabling you to invoke methods at runtime based on conditions or data. This provides a powerful way to write flexible and adaptable code.

Visit the following resources to learn more:

- [@article@Metaprogramming with the send Method in Ruby](https://medium.com/nyc-ruby-on-rails/meta-programming-with-the-send-method-in-ruby-e88d568f868)
- [@video@send in ruby](https://www.youtube.com/watch?v=cY-wxg5z5bA)

## Setting Things Up

# Installing Ruby

Installing Ruby involves setting up the Ruby interpreter and related tools on your system so you can run Ruby programs. This typically includes downloading a Ruby distribution, configuring your environment, and verifying the installation to ensure everything is working correctly. Different operating systems (like Windows, macOS, and Linux) have their own preferred methods for installing Ruby, often involving package managers or dedicated installers.

Visit the following resources to learn more:

- [@official@Installing Ruby](https://www.ruby-lang.org/en/documentation/installation/)
- [@article@Installing Ruby](https://www.theodinproject.com/lessons/ruby-installing-ruby)
- [@article@How to Install Ruby on Windows, macOS, and Linux](https://dev.to/luigi_ichi/how-to-install-ruby-on-windows-macos-and-linux-35o3)
- [@article@Setting up Ruby on WSL2 using Rbenv](https://codex.org/2022/08/19/setting-up-ruby-wsl2.html)
- [@video@Ruby Beginner Tutorial 2 | How To Install Ruby On Windows](https://www.youtube.com/watch?v=XC1ccTyhLPI)
- [@video@Ruby Beginner Tutorial 3 | How To Install Ruby On MacOS](https://www.youtube.com/watch?v=2pycF6hMy0s)

## Sinatra

# Sinatra

Sinatra is a lightweight and flexible Domain Specific Language (DSL) for creating web applications in Ruby with minimal effort. It provides a simple way to map routes to Ruby code, allowing developers to quickly build web applications without the complexity of larger frameworks. Sinatra emphasizes convention over configuration, making it easy to get started and build small to medium-sized web applications.

Visit the following resources to learn more:

- [@official@Sinatra](https://sinatrarb.com/)
- [@opensource@sinatra](https://github.com/sinatra/sinatra)
- [@article@How to Use Sinatra to Build a Ruby Application](https://blog.appsignal.com/2023/05/31/how-to-use-sinatra-to-build-a-ruby-application.html)
- [@article@Tutorial: Run a Sinatra application](https://www.jetbrains.com/help/ruby/sinatra.html)
- [@video@Sinatra Ruby Gem](https://www.youtube.com/watch?v=sfw5ZPowLJY&list=PL1sGH26TWrxot1_zsMNqb1lYbS54-OzVU)

## Singleton Classes

# Singleton Classes

A singleton class in Ruby is a special kind of class that is associated with a single object. It allows you to define methods that are specific to that particular object, without affecting other objects of the same class. Think of it as a way to add unique behavior to an individual object instance.

Visit the following resources to learn more:

- [@article@Explaining Ruby's Singleton Class (Eigenclass) to confused beginners](https://dev.to/samuelfaure/explaining-ruby-s-singleton-class-eigenclass-to-confused-beginners-cep)
- [@article@Better Know A Ruby Thing: Singleton Classes](https://noelrappin.com/blog/2025/01/better-know-a-ruby-thing-singleton-classes/)
- [@video@The Singleton Pattern in Ruby](https://www.youtube.com/watch?v=IP3I_t2rR6A)

## Sorting Algorithms

# Sorting Algorithms

Sorting algorithms are methods used to rearrange a collection of items (like numbers, strings, or objects) into a specific order, such as ascending or descending. These algorithms work by comparing elements and swapping their positions until the entire collection is ordered according to the desired criteria. Different sorting algorithms have varying efficiencies and are suitable for different types and sizes of data.

Visit the following resources to learn more:

- [@article@Sorting Algorithms with Ruby](https://dev.to/daviducolo/sorting-algorithms-with-ruby-4o18)
- [@article@Sorting Algorithms in Ruby](https://www.sitepoint.com/sorting-algorithms-ruby/)
- [@video@Ruby Sorting Algorithms](https://www.youtube.com/playlist?list=PLVVKl6q0Euw62GGkbh5PNSlEm37Lft9Re)

## Sorting

# Sorting in Enumerable

The `Enumerable` module in Ruby provides several methods for sorting collections. These methods allow you to arrange elements in ascending or descending order based on their natural ordering or a custom comparison logic. The most common sorting methods include `sort`, which returns a new sorted array, and `sort_by`, which sorts based on the result of a block applied to each element. You can also use `min`, `max`, `minmax` to find the smallest, largest, or both smallest and largest elements in a collection, respectively.

Visit the following resources to learn more:

- [@article@module Enumerable](https://ruby-doc.org/3.4.1/Enumerable.html#top)
- [@article@Understanding Ruby - Enumerable - Sorting and Comparing](https://dev.to/baweaver/understanding-ruby-enumerable-sorting-and-comparing-fff)
- [@article@Sorting short sequences with Enumerable#sort_by](https://silvercat.com/blog/sort-by-unexpected-ordering)

## Stacks   Queues

# Stacks & Queues

Stacks and queues are fundamental data structures used to manage collections of items. A stack operates on the Last-In, First-Out (LIFO) principle, where the last element added is the first one removed, like a stack of plates. Conversely, a queue follows the First-In, First-Out (FIFO) principle, where the first element added is the first one removed, similar to a waiting line. In Ruby, these can be implemented using arrays or custom classes to manage data in a specific order.

Visit the following resources to learn more:

- [@article@Introduction: Stacks and Queues](https://codesignal.com/learn/courses/mastering-complex-data-structures-in-ruby/lessons/exploring-stacks-and-queues-in-ruby)
- [@article@Stack, Queue and Deque Data Structures in Ruby](https://medium.com/@paulndemo/stack-queue-and-deque-data-structures-in-ruby-64ce9a546247)
- [@article@How to Use Stacks in Ruby to Solve Problems](https://www.rubyguides.com/2017/03/computer-science-in-ruby-stacks/)
- [@video@Introduction to Stacks and Queues (Data Structures & Algorithms #12)](https://www.youtube.com/watch?v=A3ZUpyrnCbM)

## Standard

# Standard

Standard is a Ruby gem that automatically formats and lints Ruby code, aiming to enforce a consistent style across projects. It combines the functionality of linters like RuboCop with an auto-formatter, providing a single tool to ensure code adheres to a predefined set of style rules. By automatically fixing style issues, Standard helps developers focus on writing code rather than debating formatting preferences.

Visit the following resources to learn more:

- [@opensource@standard](https://github.com/standardrb/standard)
- [@article@Getting Started with StandardRB](https://betterstack.com/community/guides/scaling-ruby/standardrb-explained/)
- [@video@Lint & Format Messy Ruby Code Using Standard](https://www.youtube.com/watch?v=zQ4BiObOf2U&t=28s)

## Strings

# Strings

Strings are sequences of characters used to represent text. They are a fundamental data type for storing and manipulating textual information. Strings can contain letters, numbers, symbols, and spaces, and are typically enclosed within single or double quotes.

Visit the following resources to learn more:

- [@official@class String](https://docs.ruby-lang.org/en/master/String.html)
- [@article@Strings](https://ruby-for-beginners.rubymonstas.org/built_in_classes/strings.html)
- [@article@Strings - Odin Project](https://www.theodinproject.com/lessons/ruby-basic-data-types#strings)
- [@video@Working With Strings | Ruby | Tutorial 8](https://www.youtube.com/watch?v=9HB4iIAxuh0)
- [@video@Strings and Variables in Ruby for Beginners 2](https://www.youtube.com/watch?v=cSwq_lcCs78)

## Symbols

# Symbols

Symbols are lightweight, immutable strings often used as identifiers or names within a Ruby program. Unlike regular strings, symbols are guaranteed to be unique; Ruby only creates one copy of a symbol, regardless of how many times it's referenced. This makes them efficient for tasks like hash keys or representing states, where comparing identity is more important than comparing content. They are typically written with a colon prefix, like `:my_symbol`.

Visit the following resources to learn more:

- [@official@class Symbol](https://docs.ruby-lang.org/en/master/Symbol.html)
- [@article@Symbols](https://ruby-for-beginners.rubymonstas.org/built_in_classes/symbols.html)
- [@article@What Are Ruby Symbols & How Do They Work?](https://www.rubyguides.com/2018/02/ruby-symbols/)
- [@video@Ruby's Symbols Explained](https://www.youtube.com/watch?v=mBXGBbEbXZY&t=16s&pp=ygUMc3ltbm9scyBydWJ5)

## Testunit

# Test::Unit

Test::Unit is a testing framework for Ruby, providing a structure for writing and running tests. It allows developers to define test cases as methods within classes, making it easy to organize and execute tests to verify the correctness of their code. Test::Unit includes assertions to check expected outcomes and report failures, helping ensure code quality and reliability.

Visit the following resources to learn more:

- [@article@Test::Unit](https://ruby-doc.org/stdlib-3.1.0/libdoc/test-unit/rdoc/Test/Unit.html)
- [@article@TestUnit - Writing Test Code In Ruby (1/3)](https://dev.to/exampro/testunit-writing-test-code-in-ruby-part-1-of-3-44m2)

## Threads

# Threads

Threads are a way to achieve concurrency within a single process. They allow multiple parts of a program to execute seemingly simultaneously by sharing the same memory space. This can improve performance by utilizing multiple CPU cores or by allowing a program to remain responsive while performing long-running tasks.

## Threads

# Threads

Threads allow you to run multiple blocks of code seemingly at the same time within a single program. Think of them as lightweight processes that share the same memory space. This means they can access the same variables and objects, making it easier to share data, but also requiring careful management to avoid conflicts when multiple threads try to modify the same data simultaneously.

Visit the following resources to learn more:

- [@official@Thread](https://docs.ruby-lang.org/en/master/Thread.html)
- [@article@How to Use Ruby Threads: An Easy To Understand Tutorial](https://www.rubyguides.com/2015/07/ruby-threads/)
- [@article@Untangling Ruby Threads](https://thoughtbot.com/blog/untangling-ruby-threads)
- [@video@Magesh, "Concurrency in Ruby: Threads, Fibers, and Ractors Demystified"](https://www.youtube.com/watch?v=LVHiq_SbQOE)

## Times

# Times Loop

The `times` method in Ruby is a simple way to execute a block of code a specified number of times. It's called on an integer, and the block is executed that many times, with an optional block variable representing the current iteration number (starting from zero). It provides a concise way to repeat actions without needing to explicitly manage a counter variable.

Visit the following resources to learn more:

- [@article@Times loop](https://www.theodinproject.com/lessons/ruby-loops#times-loop)
- [@article@Ruby Explained: Iteration](https://eriktrautman.com/posts/ruby-explained-iteration)
- [@video@#20 Ruby Tutorial - For Loop and its Alternative .each loop](https://www.youtube.com/watch?v=0Bp-91lv-zw)

## Type Casting

# Type Casting

Type casting, also known as type conversion, is the process of changing a value from one data type to another. This is often necessary when you need to perform operations that require specific data types or when you want to represent data in a different format. For example, you might need to convert a string representation of a number into an actual integer or float to perform mathematical calculations.

Visit the following resources to learn more:

- [@article@Ruby type conversion](https://kddnewton.com/2021/09/09/ruby-type-conversion.html)
- [@article@How To Convert Data Types in Ruby](https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-ruby)
- [@article@Confident Code - Ruby Implicit and Explicit Type Converters](https://whatapalaver.co.uk/ruby-implicit-explicit-type-conversion)

## Type Casting

# Type Casting

Type casting, also known as type conversion, is the process of changing a value from one data type to another. This is often necessary when you need to perform operations that require specific data types or when you want to represent data in a different format. For example, you might need to convert a string representation of a number into an actual integer or float to perform mathematical calculations.

Visit the following resources to learn more:

- [@article@Ruby type conversion](https://kddnewton.com/2021/09/09/ruby-type-conversion.html)
- [@article@How To Convert Data Types in Ruby](https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-ruby)
- [@article@Confident Code - Ruby Implicit and Explicit Type Converters](https://whatapalaver.co.uk/ruby-implicit-explicit-type-conversion)

## Unless

# Unless

`unless` is a conditional statement in Ruby that executes a block of code only if a specified condition is false. It's essentially the opposite of `if`. If the condition provided to `unless` evaluates to false, the code block is executed; otherwise, the code block is skipped. It provides a more readable way to express negative conditions.

Visit the following resources to learn more:

- [@article@Unless statements](https://www.theodinproject.com/lessons/ruby-conditional-logic#unless-statements)
- [@article@Read This Post 'Unless' You're Not A Ruby Developer](https://jesseduffield.com/Unless/)
- [@video@Ruby Programming Tutorial - 16 - unless](https://www.youtube.com/watch?v=2iysMciUQpw)

## Until

# Until Loop

The `until` loop in Ruby executes a block of code as long as a specified condition is false. It repeatedly runs the code within the loop until the condition becomes true. Think of it as the opposite of a `while` loop; where `while` loops continue as long as the condition is true, `until` loops continue as long as the condition is false.

Visit the following resources to learn more:

- [@article@Until loop](https://www.theodinproject.com/lessons/ruby-loops#until-loop)
- [@article@5.3 Until Loops](https://www.oreilly.com/library/view/computer-science-programming/9781449356835/fivedot3_until_loops.html)
- [@article@Ruby - Loops](https://www.tutorialspoint.com/ruby/ruby_loops.htm)
- [@video@Ruby Programming Tutorial | Until Loops](https://www.youtube.com/watch?v=Y32UnAPHJm4)

## Vs Code

# VS Code Ruby Extension

The VS Code Ruby extension enhances the Visual Studio Code editor with features specifically designed for Ruby development. It provides functionalities like syntax highlighting, code completion, debugging support, linting, and formatting, making it easier for developers to write, test, and maintain Ruby code within the VS Code environment. This extension streamlines the development workflow and improves code quality by offering real-time feedback and assistance.

Visit the following resources to learn more:

- [@official@Ruby in Visual Studio Code](https://code.visualstudio.com/docs/languages/ruby)
- [@article@Best Visual Studio Code extensions and settings for Ruby and Rails](https://achris.me/posts/setup-ruby-vscode/)
- [@article@Ruby Development with VS Code](https://medium.com/@terrenceong/ruby-development-with-vs-code-fab258db5f1d)
- [@video@How to Set Up VS Code for Ruby](https://www.youtube.com/watch?v=Zw4wdDLMAIw)

## While

# While Loops in Ruby

A `while` loop in Ruby repeatedly executes a block of code as long as a specified condition is true. It checks the condition before each iteration, and if the condition is false from the start, the code block is never executed. This makes it suitable for situations where you want to execute code an unknown number of times until a certain condition is met.

Visit the following resources to learn more:

- [@article@While Loops](https://www.theodinproject.com/lessons/ruby-loops#while-loop)
- [@article@Ruby while Loop](https://www.programiz.com/ruby/while-loop)
- [@video@While Loops | Ruby | Tutorial 21](https://www.youtube.com/watch?v=3bXd6h8Zsfk)

## Yard

# YARD

YARD (Yet Another Ruby Documentation) is a documentation generation tool for the Ruby programming language. It allows developers to create comprehensive and consistent documentation for their Ruby projects by parsing source code and extracting information based on specially formatted comments. YARD generates output in various formats, including HTML, making it easy to browse and share project documentation.

Visit the following resources to learn more:

- [@official@YARD](https://yardoc.org/)
- [@official@Getting Started](https://rubydoc.info/gems/yard/file/docs/GettingStarted.md)
- [@opensource@yard](https://github.com/lsegal/yard)
- [@article@YARD for Ruby Beginners: A Documentation Guide](https://medium.com/@swastik.thapaliya/yard-for-ruby-beginners-a-documentation-guide-d276b919fc12)
