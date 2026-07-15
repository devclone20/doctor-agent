# Python Roadmap

## Aiohttp

# AIOHTTP

aiohttp is a Python 3.5+ library that provides a simple and powerful asynchronous HTTP client and server implementation.

Visit the following resources to learn more:

- [@official@aiohttp docs](https://docs.aiohttp.org/en/stable/)
- [@article@Creating a RESTful API with Python and aiohttp](https://tutorialedge.net/python/create-rest-api-python-aiohttp/)
- [@video@Python Asyncio, Requests, Aiohttp | Make faster API Calls](https://www.youtube.com/watch?v=nFn4_nA_yk8)

## Arrays And Linked Lists

# Arrays and Linked lists

Arrays store elements in contiguous memory locations, resulting in easily calculable addresses for the elements stored and this allows faster access to an element at a specific index. Linked lists are less rigid in their storage structure and elements are usually not stored in contiguous locations, hence they need to be stored with additional tags giving a reference to the next element. This difference in the data storage scheme decides which data structure would be more suitable for a given situation.

Visit the following resources to learn more:

- [@article@Arrays in Python](https://www.edureka.co/blog/arrays-in-python/)
- [@article@Linked List Python](https://realpython.com/linked-lists-python/)
- [@video@Array Data Structure | Illustrated Data Structures](https://www.youtube.com/watch?v=QJNwK2uJyGs)
- [@video@Linked List Data Structure | Illustrated Data Structures](https://www.youtube.com/watch?v=odW9FU8jPRQ)

## Asynchrony

# Asynchrony

Asynchronous programming, supported by asyncio, allows code to be executed without blocking, using async and await. This is especially useful for I/O tasks such as networking or file manipulation, allowing thousands of connections to be handled without blocking the main thread.

Visit the following resources to learn more:

- [@official@Python AsyncIO library](https://docs.python.org/3/library/asyncio.html)
- [@article@Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)

## Basic Syntax

# Basic Syntax

Setup the environment for python and get started with the basics.

Visit the following resources to learn more:

- [@article@Python Basics](https://www.tutorialspoint.com/python/python_basic_syntax.htm)
- [@article@Learn X in Y Minutes / Python](https://learnxinyminutes.com/docs/python/)
- [@video@Python for Beginners - Learn Python in 1 Hour](https://www.youtube.com/watch?v=kqtD5dpn9C8)

## Binary Search Tree

# Binary Search Trees

A binary search tree, also called an ordered or sorted binary tree, is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree

Visit the following resources to learn more:

- [@article@Binary search in Python 101: Implementation and use cases](https://roadmap.sh/python/binary-search)
- [@article@How to Implement Binary Search Tree in Python](https://web.archive.org/web/20230601181553/https://www.section.io/engineering-education/implementing-binary-search-tree-using-python/)
- [@article@Binary Search Tree in Python](https://www.pythonforbeginners.com/data-structures/binary-search-tree-in-python)
- [@video@Tree Data Structure | Illustrated Data Structures](https://www.youtube.com/watch?v=S2W3SXGPVyU)

## Black

# black

Black is a python code formatter that automatically formats code according to a consistent style. By removing formatting decisions from developers, Black helps maintain uniform codebases, improves readability, and reduces time spent on style discussions during code reviews.

Visit the following resources to learn more:

- [@official@Getting Started with Black](https://black.readthedocs.io/en/stable/getting_started.html)
- [@official@Black Documentation](https://black.readthedocs.io/en/stable/)

## Builtin

# Builtin Modules

Python has a rich standard library of built-in modules that provide a wide range of functionality. Some of the most commonly used built-in modules include: sys, os, math, datetime, random, re, itertools, etc.

Visit the following resources to learn more:

- [@official@Python Module Index](https://docs.python.org/3/py-modindex.html)
- [@article@Python Modules](https://www.digitalocean.com/community/tutorials/python-modules)
- [@article@Python - Built-In Modules](https://www.knowledgehut.com/tutorials/python-tutorial/python-built-in-modules)

## Classes

# Classes

A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by their class) for modifying their state.

Visit the following resources to learn more:

- [@official@Classes in Python](https://docs.python.org/3/tutorial/classes.html)
- [@video@Python OOP Tutorial](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)

## Code Formatting

# Code Formatting

Python code formatting is crucial for maintaining readability, consistency, and reducing errors. Black is a code formatter for Python. It is a tool that automatically formats Python code to adhere to the PEP 8 style guide. It is a great tool to use in your Python projects to ensure that your code is formatted consistently and correctly.

Visit the following resources to learn more:

- [@official@Pylint for Python](https://www.pylint.org/)
- [@official@Black Documentation](https://black.readthedocs.io/en/stable/)

## Common Packages

# Common Packages and Modules

Python has a rich ecosystem of packages and modules that can be used to get the most out of the language. A package is essentially a directory that contains multiple modules and subpackages. A module is a single file that contains a collection of related functions, classes, and variables. Modules are the basic building blocks of Python code organization. A module can be thought of as a container that holds a set of related code.

Visit the following resources to learn more:

- [@official@requests](https://docs.python-requests.org/en/latest/)
- [@official@pathlib](https://docs.python.org/3/library/pathlib.html)
- [@official@asyncio](https://docs.python.org/3/library/asyncio.html)
- [@official@dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [@official@python-dotenv](https://pypi.org/project/python-dotenv/)
- [@official@numpy](https://numpy.org/doc/stable/)
- [@official@pandas](https://pandas.pydata.org/docs/)

## Concurrency

# Concurrency

Concurrency in Python allows multiple tasks to be executed simultaneously using different approaches. GIL (Global Interpreter Lock) limits thread execution, making multithreading less efficient for computational tasks, but suitable for I/O. Multiprocessing, using the multiprocessing module, allows multiple cores to be utilized, providing true parallelism. Asynchrony via asyncio is optimal for I/O operations, allowing thousands of connections to be processed simultaneously without blocking. The choice of approach depends on the nature of the task.

Visit the following resources to learn more:

- [@official@Concurrent Execution](https://docs.python.org/3/library/concurrency.html)
- [@article@Python Concurrency](https://realpython.com/python-concurrency/)

## Conda

# Conda

Conda is an open source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.

Visit the following resources to learn more:

- [@official@Conda Documentation](https://docs.conda.io/en/latest/)

## Conditionals

# Conditionals

Conditional Statements in Python perform different actions depending on whether a specific condition evaluates to true or false. Conditional Statements are handled by _if-elif-else_ statements and MATCH-CASE statements in Python.

Visit the following resources to learn more:

- [@article@Conditional Statements in Python](https://realpython.com/python-conditional-statements/)
- [@article@Python Conditional Statements](https://www.guru99.com/if-loop-python-conditional-structures.html)
- [@article@Python Switch Statement 101: Match-case and alternatives](https://roadmap.sh/python/switch)
- [@article@How to Use a Match Statement in Python](https://learnpython.com/blog/python-match-case-statement/)

## Context Manager

# Context Manager

Context Managers are a construct in Python that allows you to set up context for a block of code, and then automatically clean up or release resources when the block is exited. It is most commonly used with the `with` statement.

Visit the following resources to learn more:

- [@official@Context Libraries](https://docs.python.org/3/library/contextlib.html)
- [@article@Context Managers in Python](https://www.freecodecamp.org/news/context-managers-in-python/)
- [@article@Context Managers](https://book.pythontips.com/en/latest/context_managers.html)

## Custom

# Custom Modules

Modules refer to a file containing Python statements and definitions. A file containing Python code, for example: `example.py`, is called a module, and its module name would be example. We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.

Visit the following resources to learn more:

- [@official@Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [@article@Modules in Python](https://www.programiz.com/python-programming/modules)
- [@article@Python Modules and Packages](https://realpython.com/python-modules-packages/)

## Data Structures  Algorithms

# Data Structures and Algorithms

A data structure is a named location that can be used to store and organize data. And, an algorithm is a collection of steps to solve a particular problem. Learning data structures and algorithms allow us to write efficient and optimized computer programs.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated DSA Roadmap](https://roadmap.sh/datastructures-and-algorithms)
- [@article@Learn DS & Algorithms](https://www.programiz.com/dsa)
- [@video@Data Structures Illustrated](https://www.youtube.com/playlist?list=PLkZYeFmDuaN2-KUIv-mvbjfKszIGJ4FaY)
- [@video@DSA Python Playlist](https://www.youtube.com/playlist?list=PLKYEe2WisBTFEr6laH5bR2J19j7sl5O8R)

## Decorators

# Decorators

Decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

Visit the following resources to learn more:

- [@article@Learn Decorators in Python](https://pythonbasics.org/decorators/)
- [@article@Python Decorators](https://www.datacamp.com/tutorial/decorators-python)
- [@video@Decorators in Python](https://www.youtube.com/watch?v=FXUUSfJO_J4)
- [@video@Python Decorators in 1 Minute](https://www.youtube.com/watch?v=BE-L7xu8pO4)

## Dictionaries

# Dictionaries

In Python, a dictionary is a built-in data type that allows you to store key-value pairs. Each key in the dictionary is unique, and each key is associated with a value. Starting from Python 3.7, dictionaries maintain the order of items as they were added.

Visit the following resources to learn more:

- [@official@Dictionaries in Python](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [@article@Dictionaries in Python](https://realpython.com/python-dicts/)
- [@article@Hashmaps in Python: Master Implementation and Use Cases](https://roadmap.sh/python/hashmap)

## Django

# Django

Django is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern. It is maintained by the Django Software Foundation, an independent organization established in the US as a 501 non-profit

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Django Roadmap](https://roadmap.sh/django)
- [@official@Django Website](https://www.djangoproject.com/)
- [@official@Getting Started](https://www.djangoproject.com/start/)
- [@article@Is Django Synchronous or Asynchronous?](https://stackoverflow.com/questions/58548089/django-is-synchronous-or-asynchronous)
- [@video@Python Django Tutorial for Beginners](https://www.youtube.com/watch?v=rHux0gMZ3Eg)
- [@feed@Explore top posts about Django](https://app.daily.dev/tags/django?ref=roadmapsh)

## Doctest

# Doctest

Python’s standard library comes equipped with a test framework module called doctest. The doctest module programmatically searches Python code for pieces of text within comments that look like interactive Python sessions. Then, the module executes those sessions to confirm that the code referenced by a doctest runs as expected.

Visit the following resources to learn more:

- [@official@Doctest Module](https://docs.python.org/3/library/doctest.html)
- [@article@How To Write Doctests in Python](https://www.digitalocean.com/community/tutorials/how-to-write-doctests-in-python)

## Encapsulation

# Encapsulation

Encapsulation is a way to bundle data (attributes) and the methods that operate on that data into a single unit, known as a class. It restricts direct access to some of the object's components and prevents the accidental modification of data. This is achieved by declaring some attributes or methods as private, meaning they can only be accessed from within the class itself.

Visit the following resources to learn more:

- [@article@Encapsulation in Python: All You Need to Know](https://roadmap.sh/python/encapsulation)
- [@article@Encapsulation in Python: A Comprehensive Guide](https://www.datacamp.com/tutorial/encapsulation-in-python-object-oriented-programming)
- [@article@Encapsulation](https://programming-25.mooc.fi/part-9/3-encapsulation)
- [@video@Encapsulation - Advanced Python Tutorial #5](https://www.youtube.com/watch?v=dzmYoSzL8ok)

## Exceptions

# Exceptions

Exceptions are runtime errors that occur during program execution in Python. Instead of immediately stopping the program, Python allows developers to handle these errors using `try`, `except`, `else`, and `finally` blocks. Proper exception handling helps manage unexpected situations such as invalid input, missing files, or network failures, improving program reliability and allowing applications to fail gracefully.

Visit the following resources to learn more:

- [@official@Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html#exceptions)
- [@article@Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)
- [@article@Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [@article@Python Exception Handling](https://www.programiz.com/python-programming/exception-handling)
- [@video@Exception Handling in Python](https://www.youtube.com/watch?v=V_NXT2-QIlE)

## Fast Api

# FastAPI

FastAPI is a modern Python web framework used for building APIs with high performance and automatic documentation. It leverages Python type hints for request validation, serialization, and editor support, making API development faster and less error-prone. FastAPI is commonly used for backend services, microservices, and machine learning model deployment due to its speed and ease of use.

Visit the following resources to learn more:

- [@official@FastAPI Documentation](https://fastapi.tiangolo.com/)
- [@video@Create an API with Fast-API (Full 19 Hour Course)](https://www.youtube.com/watch?v=0sOvCWFmrtA)
- [@feed@Explore top posts about FastAPI](https://app.daily.dev/tags/fastapi?ref=roadmapsh)

## File Handling

# File Handling in Python

File handling in Python involves reading data from and writing data to files. It allows programs to interact with files stored on a computer's storage. You can open files in different modes like read, write, or append, and then perform operations like reading the entire file content, reading line by line, or writing new data. A common use case is working with structured data, and Python provides built-in modules like `json` to easily read and write data in JSON format, which is frequently used for data exchange.

Visit the following resources to learn more:

- [@article@Pyhton File open](https://www.w3schools.com/python/python_file_handling.asp)
- [@article@Working With Files in Python](https://realpython.com/working-with-files-in-python/)
- [@article@Python JSON](https://www.w3schools.com/python/python_json.asp)
- [@article@Working With JSON Data in Python](https://realpython.com/python-json/)
- [@video@Python File Handling for Beginners](https://www.youtube.com/watch?v=BRrem1k3904)
- [@video@Python Tutorial: Working with JSON Data using the json Module](https://www.youtube.com/watch?v=9N6a-VLBa2I)

## Flask

# Flask

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. Instead, it provides flexibility by requiring you to choose and integrate the best libraries for your project's needs.

Visit the following resources to learn more:

- [@official@Flask Website](https://flask.palletsprojects.com/)
- [@official@Flask Tutorial](https://flask.palletsprojects.com/en/3.0.x/tutorial/)
- [@feed@Explore top posts about Flask](https://app.daily.dev/tags/flask?ref=roadmapsh)

## Functions Builtin Functions

# Functions

In programming, a function is a reusable block of code that executes a certain functionality when it is called. Functions are integral parts of every programming language because they help make your code more modular and reusable. In Python, we define a function with the `def` keyword, then write the function identifier (name) followed by parentheses and a colon.

Example
-------

    def greet(name):
        print(f"Hello, {name}!")
    
    
    greet("Roadmap.sh")

Visit the following resources to learn more:

- [@official@Built-in Functions in Python](https://docs.python.org/3/library/functions.html)
- [@article@Defining Python Functions](https://realpython.com/defining-your-own-python-function/)

## Generator Expressions

# Generator Expressions

Generator expressions are a concise way to create a generator using a single line of code in Python. They are similar to list comprehensions, but instead of creating a list, they create a generator object that produces the values on-demand, as they are needed. Generator expressions are a useful tool for efficiently producing large sequence of values, as they allow you to create the generator without creating the entire sequence in memory at once. This tends to use less memory, especially for large sequences.

Visit the following resources to learn more:

- [@official@Python Official Documentation on Generator Expressions](https://docs.python.org/3/tutorial/classes.html#generator-expressions)
- [@article@Python Generator Expressions](https://www.pythontutorial.net/advanced-python/python-generator-expressions/)
- [@article@List Comprehensions in Python and Generator Expressions](https://djangostars.com/blog/list-comprehensions-and-generator-expressions/)

## Gevent

# gevent

gevent is a Python library that provides a high-level interface to the event loop. It is based on non-blocking IO (libevent/libev) and lightweight greenlets. Non-blocking IO means requests waiting for network IO won't block other requests; greenlets mean we can continue to write code in synchronous style.

Visit the following resources to learn more:

- [@official@gevent Website](http://www.gevent.org/)
- [@opensource@gevent/gevent](https://github.com/gevent/gevent)
- [@article@gevent For the Working Python Developer](https://sdiehl.github.io/gevent-tutorial/)

## Gil

# GIL

GIL is a mechanism that allows only one thread to execute Python code at a time. This limitation is related to memory management in CPython and can reduce the efficiency of multithreaded applications on multi-core systems.

Visit the following resources to learn more:

- [@article@What is GIL?](https://realpython.com/python-gil/)

## Glob

# Glob Module in Python

The `glob` module in Python is a handy tool for finding files and directories whose names match a specific pattern. It uses Unix shell rules for pattern matching, allowing you to easily search for files with certain extensions, files starting with a particular name, or any other combination of criteria you define using wildcards. The main function in this module, also named `glob`, takes a pattern as input and returns a list of all the pathnames that match it.

Visit the following resources to learn more:

- [@article@Python glob Module: File Pattern Matching Explained](https://roadmap.sh/python/glob)
- [@article@glob](https://realpython.com/ref/stdlib/glob/)

## Hashmaps

# HashMaps

HashMap, HashTable, Map, Dictionary, or Associative are all the names of the same data structure. It is a data structure that implements a set abstract data type, a structure that can map keys to values.

Visit the following resources to learn more:

- [@article@Hashmaps in Python: Master Implementation and Use Cases](https://roadmap.sh/python/hashmap)
- [@article@Build a Hash Table in Python](https://realpython.com/python-hash-table/)
- [@article@Hash Tables and Hashmaps in Python](https://www.edureka.co/blog/hash-tables-and-hashmaps-in-python/)
- [@video@Hash Table Data Structure | Illustrated Data Structures](https://www.youtube.com/watch?v=jalSiaIi8j4)

## Heaps Stacks And Queues

# Heaps Stacks and Queues

**Stacks:** Operations are performed LIFO (last in, first out), which means that the last element added will be the first one removed. A stack can be implemented using an array or a linked list. If the stack runs out of memory, it’s called a stack overflow.

**Queue:** Operations are performed FIFO (first in, first out), which means that the first element added will be the first one removed. A queue can be implemented using an array.

**Heap:** A tree-based data structure in which the value of a parent node is ordered in a certain way with respect to the value of its child node(s). A heap can be either a min heap (the value of a parent node is less than or equal to the value of its children) or a max heap (the value of a parent node is greater than or equal to the value of its children).

Visit the following resources to learn more:

- [@article@Heaps, Stacks, Queues](https://stephanosterburg.gitbook.io/scrapbook/coding/coding-interview/data-structures/heaps-stacks-queues)
- [@article@How to Implement Python Stack?](https://realpython.com/how-to-implement-python-stack/)
- [@article@Python Stacks, Queues, and Priority Queues in Practice](https://realpython.com/queue-in-python/)
- [@article@Heap Implementation in Python](https://www.educative.io/answers/heap-implementation-in-python)
- [@video@Stack Data Structure | Illustrated Data Structures](https://www.youtube.com/watch?v=I5lq6sCuABE)
- [@video@Queue Data Structure | Illustrated Data Structures](https://www.youtube.com/watch?v=mDCi1lXd9hc)

## Inheritance

# Inheritance

Inheritance is a fundamental concept in object-oriented programming where a new class (the child class or subclass) is derived from an existing class (the parent class or superclass). The child class inherits attributes and methods from the parent class, allowing for code reuse and the creation of hierarchical relationships between classes. This promotes a more organized and maintainable codebase by establishing a clear structure and reducing redundancy.

Visit the following resources to learn more:

- [@official@Python Official Documentation on Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)

## Iterators

# Iterators

An iterator is an object that contains a countable number of values. An iterator is an object that can be iterated upon, meaning that you can traverse through all the values. Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods **iter**() and **next**() .

Visit the following resources to learn more:

- [@official@Python Official Documentation on Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)
- [@article@Python Iterators](https://www.programiz.com/python-programming/iterator)
- [@article@Iterators and Iterables in Python](https://realpython.com/python-iterators-iterables/)

## Lambdas

# Lambdas

Python Lambda Functions are anonymous function means that the function is without a name. As we already know that the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python.

Visit the following resources to learn more:

- [@article@How to use Lambda functions](https://realpython.com/python-lambda/)
- [@video@Python Lambda Functions](https://www.youtube.com/watch?v=KR22jigJLok)

## Learn A Framework

# Python Frameworks

Frameworks automate the common implementation of common solutions which gives the flexibility to the users to focus on the application logic instead of the basic routine processes. Frameworks make the life of web developers easier by giving them a structure for app development. They provide common patterns in a web application that are fast, reliable and easily maintainable.

Visit the following resources to learn more:

- [@article@Pyscript: A Browser-Based Python Framework](https://thenewstack.io/pyscript-a-browser-based-python-framework/)
- [@feed@Explore top posts about Python](https://app.daily.dev/tags/python?ref=roadmapsh)

## Learn The Basics

# Python

Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.

Visit the following resources to learn more:

- [@official@Python Website](https://www.python.org/)
- [@article@Python - Wiki](https://en.wikipedia.org/wiki/Python_(programming_language))
- [@article@Tutorial Series: How to Code in Python](https://www.digitalocean.com/community/tutorials/how-to-write-your-first-python-3-program)
- [@article@Google's Python Class](https://developers.google.com/edu/python)
- [@video@Learn Python - Full Course](https://www.youtube.com/watch?v=4M87qBgpafk)
- [@feed@Explore top posts about Python](https://app.daily.dev/tags/python?ref=roadmapsh)

## List Comprehensions

# List Comprehensions

List comprehensions are a concise way to create a list using a single line of code in Python. They are a powerful tool for creating and manipulating lists, and they can be used to simplify and shorten code.

Visit the following resources to learn more:

- [@official@Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [@article@What Exactly are List Comprehensions in Python? - CodeGuage](https://www.codeguage.com/courses/python/lists-list-comprehensions)
- [@article@Python List Comprehensions Quiz](https://realpython.com/quizzes/list-comprehension-python/)

## Lists

# Lists in Python

Lists are fundamental data structures in Python used to store an ordered collection of items. These items can be of different data types (numbers, strings, or even other lists), and lists are mutable, meaning you can change their contents after they are created by adding, removing, or modifying elements. They are defined using square brackets `[]` and elements are separated by commas.

Visit the following resources to learn more:

- [@official@Python Official Documentation on Listsc](https://docs.python.org/3/tutorial/introduction.html#lists)
- [@article@Tuples vs. Lists vs. Sets in Python](https://jerrynsh.com/tuples-vs-lists-vs-sets-in-python/)
- [@article@Python for Beginners: Lists](https://thenewstack.io/python-for-beginners-lists/)
- [@article@Python for Beginners: When and How to Use Tuples](https://thenewstack.io/python-for-beginners-when-and-how-to-use-tuples/)
- [@video@Difference Between List, Tuple, Set and Dictionary in Python](https://www.youtube.com/watch?v=n0krwG38SHI)

## Loops

# Loops

Loops are used to execute a block of code repeatedly.

Visit the following resources to learn more:

- [@article@Python "while" Loops (Indefinite Iteration)](https://realpython.com/python-while-loop/)
- [@article@Python "for" Loops (Definite Iteration)](https://realpython.com/python-for-loop/#the-guts-of-the-python-for-loop)
- [@video@Python For Loops](https://www.youtube.com/watch?v=KWgYha0clzw)

## Methods

# Methods and Dunder

A method in python is somewhat similar to a function, except it is associated with object/classes. Methods in python are very similar to functions except for two major differences.

*   The method is implicitly used for an object for which it is called.
*   The method is accessible to data that is contained within the class.

Dunder or magic methods in Python are the methods that have two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. Few examples for magic methods are: **`__init__`**, **`__add__`**, **`__len__`**, **`__repr__`** etc.

Visit the following resources to learn more:

- [@article@Method vs Function in Python](https://www.tutorialspoint.com/difference-between-method-and-function-in-python)
- [@article@Python - Magic or Dunder Methods](https://www.tutorialsteacher.com/python/magic-methods-in-python)

## Modules

# Modules

Modules refer to a file containing Python statements and definitions. A file containing Python code, for example: `example.py`, is called a module, and its module name would be example. We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.

Visit the following resources to learn more:

- [@official@Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [@article@Modules in Python](https://www.programiz.com/python-programming/modules)

## Multiprocessing

# Multiprocessing

Multiprocessing utilizes multiple processes, each with its own GIL. This allows full utilization of multiple processor cores, which is effective for computationally intensive tasks. Python's multiprocessing module supports creating processes and exchanging data between them.

Visit the following resources to learn more:

- [@official@Python Documentation](https://docs.python.org/3/library/multiprocessing.html)
- [@article@Multiprocessing in Python with Example](https://www.digitalocean.com/community/tutorials/python-multiprocessing-example)
- [@article@Multiprocessing in Python](https://realpython.com/python-multiprocessing/)

## Mypy

# mypy

mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking. Mypy type checks standard Python programs; run them using any Python VM with basically no runtime overhead.

Visit the following resources to learn more:

- [@official@mypy documentation](https://mypy-lang.org/)
- [@opensource@python/mypy](https://github.com/python/mypy)

## Object Oriented Programming

# OOP

In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphism, encapsulation, etc., in programming. The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.

Visit the following resources to learn more:

- [@article@Object Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [@video@Object Oriented Programming (OOP) In Python - Beginner Crash Course](https://www.youtube.com/watch?v=-pEs-Bss8Wc/)
- [@video@OOP in Python One Shot](https://www.youtube.com/watch?v=Ej_02ICOIgs)
- [@video@Python OOP Tutorial](https://www.youtube.com/watch?v=IbMDCwVm63M)

## Operators

# Operators

Operators are symbols or keywords that perform operations on values and variables. Python includes several types: arithmetic operators (+, -, \*, /) for math calculations, comparison operators (==, !=, <, >) for evaluating relationships between values, and logical operators (and, or, not) for combining conditions. There are also assignment operators (=, +=, -=) for storing and updating values, bitwise operators for working with binary data, and membership operators (in, not in) for checking whether a value exists within a sequence like a list or string.

Visit the following resources to learn more:

- [@article@Python Operators](https://www.w3schools.com/python/python_operators.asp)
- [@article@Python Operators with examples](https://www.programiz.com/python-programming/operators)
- [@article@Python Division: Operators, Floor Division, and Examples](https://roadmap.sh/python/division)
- [@article@Python Modulo Operator (%): Complete Guide with Examples](https://roadmap.sh/python/modulo)
- [@article@Python not Operator: The Complete Guide to Logical Negation](https://roadmap.sh/python/not-operator)

## Package Managers

# Package Managers

Package managers allow you to manage the dependencies (external code written by you or someone else) that your project needs to work correctly.

`PyPI` and `Pip` are the most common contenders but there are some other options available as well.

Visit the following resources to learn more:

- [@opensource@pypa/pipx](https://github.com/pypa/pipx)
- [@feed@Explore top posts about Python](https://app.daily.dev/tags/python?ref=roadmapsh)

## Paradigms

# Python Paradigms

Python is a multi-paradigm programming language, which means that it supports several programming paradigms. Some of the main paradigms supported by Python are:

*   Imperative programming: This paradigm focuses on telling the computer what to do, step by step. Python supports imperative programming with features such as variables, loops, and control structures.
*   Object-oriented programming (OOP): This paradigm is based on the idea of objects and their interactions. Python supports OOP with features such as classes, inheritance, and polymorphism.
*   Functional programming: This paradigm is based on the idea of functions as first-class citizens, and it emphasizes the use of pure functions and immutable data. Python supports functional programming with features such as higher-order functions, lambda expressions, and generators.
*   Aspect-oriented programming: This paradigm is based on the idea of separating cross-cutting concerns from the main functionality of a program. Python does not have built-in support for aspect-oriented programming, but it can be achieved using libraries or language extensions.

Visit the following resources to learn more:

- [@article@Python Paradigms](https://opensource.com/article/19/10/python-programming-paradigms)
- [@video@Learn Functional Programming - Python Course](https://www.youtube.com/watch?v=5QZYGU0C2OA)

## Pdm

# PDM

PDM is a modern Python package manager that supports PEP 582, which allows packages to be installed in a `__pypackages__` directory instead of the traditional `site-packages` directory. It aims to provide a streamlined and improved experience for managing dependencies, building, and publishing Python projects. PDM also includes features like dependency resolution, virtual environment management, and project scaffolding.

Visit the following resources to learn more:

- [@official@pdm](https://pdm-project.org/en/latest/)
- [@opensource@pdm](https://github.com/pdm-project/pdm)
- [@article@Introduction to PDM: A Python Project and Dependency Manager](https://betterstack.com/community/guides/scaling-python/pdm-explained/)

## Pip

# Pip

The standard package manager for Python is pip. It allows you to install and manage packages that aren’t part of the Python standard library.

Visit the following resources to learn more:

- [@official@pip Documentation](https://pip.pypa.io/en/stable/installation/)
- [@article@Using Pythons pip to Manage Your Projects Dependencies](https://realpython.com/what-is-pip/)
- [@feed@Explore top posts about PIP](https://app.daily.dev/tags/pip?ref=roadmapsh)

## Pipenv

# pipenv

Pipeline Environment (pipenv) is a tool that aims to bring the best of all packaging worlds (bundled, requirements.txt, [setup.py](https://docs.python.org/3.11/distutils/setupscript.html), setup.cfg, etc.) to the Python world. It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the ever-important Pipfile.lock, which is used to produce deterministic builds.

Visit the following resources to learn more:

- [@official@Pipenv Documentation](https://pipenv.pypa.io/en/latest/)

## Plotly Dash

# Plotly Dash

Plotly Dash is a Python framework that allows you to build analytical web applications. It's a high-level library that enables you to create interactive, web-based data visualization dashboards without requiring extensive knowledge of web development.

Visit the following resources to learn more:

- [@official@Plotly Dash Documentation](https://dash.plotly.com/)
- [@official@20 Minutes Tutorial](http://dash.plotly.com/tutorial)

## Poetry

# Poetry

Poetry is a dependency management and packaging tool for Python that runs on Windows, macOS, and Linux. Poetry efficiently installs, manages, and updates packages and their dependencies. Poetry seamlessly creates, saves, loads, and switches between project environments on your local computer. It is designed specifically for Python projects, providing a streamlined workflow for managing dependencies, virtual environments, and building packages.

Poetry as a package manager helps you find and install packages. If you need a specific version of a package or a different version of Python, Poetry handles both dependency management and virtual environments effortlessly. With just a few commands, you can set up a completely isolated environment to run a different version of Python or package configuration, while maintaining your usual development environment. Poetry’s lock file ensures consistent installs across different environments, enhancing reproducibility and stability of your projects.

Visit the following resources to learn more:

- [@official@Poetry Docs](https://python-poetry.org/docs/)
- [@video@Python Poetry - Basics](https://www.youtube.com/watch?v=Ji2XDxmXSOM)

## Pydantic

# Pydantic

Pydantic is a python library for data validation and settings management using python type annotations.

Visit the following resources to learn more:

- [@official@Pydantic Documentation](https://docs.pydantic.dev/latest/)

## Pyenv

# pyenv

pyenv is a tool for managing multiple versions of the Python programming language on Unix-like systems. It works by setting environment variables to point to the directory where the desired version of Python is installed. This allows you to switch between different versions of Python without having to modify your system's default Python installation.

Visit the following resources to learn more:

- [@opensource@pyenv/pyenv](https://github.com/pyenv/pyenv)

## Pypi

# PyPI

PyPI, typically pronounced pie-pee-eye, is a repository containing several hundred thousand packages. These range from trivial Hello, World implementations to advanced deep learning libraries.

Visit the following resources to learn more:

- [@official@PyPI Website](https://pypi.org/)
- [@article@How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/)
- [@video@Getting Started with Pip and PyPI in Python](https://www.youtube.com/watch?v=bPSfNKvhooA)
- [@feed@Explore top posts about Python](https://app.daily.dev/tags/python?ref=roadmapsh)

## Pyprojecttoml

# pyproject.toml

This file is used to define the project configuration and dependencies. It is a configuration file that contains metadata about the project, such as its name, version, dependencies, and build settings. The `pyproject.toml` file is used by tools like `poetry` and `flit` to manage Python projects and their dependencies.

Visit the following resources to learn more:

- [@official@Writing pyproject.toml files](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

## Pyramid

# Pyramid

Pyramid is a general, open source, web application development framework built in python. It allows python developer to create web applications with ease. Pyramid is backed by the enterprise knowledge Management System KARL (a George Soros project).

Visit the following resources to learn more:

- [@official@Pyramid Website](https://trypyramid.com/)
- [@official@Pyramid Documentation](https://trypyramid.com/documentation.html)
- [@article@Pyramid Framework Introduction](https://www.tutorialspoint.com/python_web_development_libraries/python_web_development_libraries_pyramid_framework.htm)

## Pyre

# pyrefly

pyrefly is a static type checker for Python. It is a tool that helps you find type errors in your Python code. Pyre is designed to be fast, scalable, and easy to use. It is used at Facebook to help developers catch type errors before they make it to production.

Visit the following resources to learn more:

- [@official@pyrefly Documentation](https://pyrefly.org)

## Pyright

# pyright

pyright is a static type checker for Python. It is a Microsoft product and is written in TypeScript. It is a language server that uses the Language Server Protocol (LSP) to communicate with the editor. It is a good alternative to mypy and pytype.

Visit the following resources to learn more:

- [@official@Pyright Documentation](https://microsoft.github.io/pyright/)

## Pytest

# pytest

pytest is a mature full-featured Python testing tool that helps you write better programs.

Visit the following resources to learn more:

- [@official@Pytest Docs](https://docs.pytest.org/)
- [@article@Pytest Tutorial](https://www.tutorialspoint.com/pytest/index.htm)
- [@article@Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
- [@video@Pytest Tutorial – How to Test Python Code](https://www.youtube.com/watch?v=cHYq1MRoyI0)
- [@feed@Explore top posts about Python](https://app.daily.dev/tags/python?ref=roadmapsh)

## Recursion

# Recursion

Recursion is a method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem. Recursion solves such recursive problems by using functions that call themselves from within their own code.

Visit the following resources to learn more:

- [@article@Recursion in Python: An Introduction](https://realpython.com/python-recursion/)
- [@feed@Explore top posts about Recursion](https://app.daily.dev/tags/recursion?ref=roadmapsh)

## Regular Expressions

# Regular Expressions

A regular expression is a sequence of characters that specifies a search pattern in text. Usually such patterns are used by string-searching algorithms for "find" or "find and replace" operations on strings, or for input validation.

Visit the following resources to learn more:

- [@official@Regular Expressions in Python](https://docs.python.org/3/library/re.html)
- [@article@Python Regular Expressions](https://developers.google.com/edu/python/regular-expressions)
- [@article@Python - Regular Expressions](https://www.tutorialspoint.com/python/python_reg_expressions.htm)

## Ruff

# ruff

Ruff is a fast Python linter and code quality tool written in Rust that combines the functionality of multiple linting and formatting tools into a single, high-performance utility. It helps detect errors, enforce coding standards, and improve code quality while running significantly faster than traditional Python linters.

Visit the following resources to learn more:

- [@official@Ruff documentation](https://docs.astral.sh/ruff/)

## Sanic

# Sanic

Sanic is a Python 3.7+ web server and web framework that's written to go fast. It allows the usage of the async/await syntax added in Python 3.5, which makes your code non-blocking and speedy.

Visit the following resources to learn more:

- [@official@Sanic Website](https://sanic.dev/en/)

## Sets

# Sets

Python Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.

Visit the following resources to learn more:

- [@official@Python Official Documentation on Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [@article@An In-Depth Guide to Working with Python Sets](https://learnpython.com/blog/python-sets/)
- [@video@Python Sets tutorial for Beginners](https://www.youtube.com/watch?v=t9j8lCUGZXo)

## Sorting Algorithms

# Sorting Algorithms

Sorting refers to arranging data in a particular format. Sorting algorithm specifies the way to arrange data in a particular order. Most common orders are in numerical or lexicographical order. The importance of sorting lies in the fact that data searching can be optimized to a very high level, if data is stored in a sorted manner.

Visit the following resources to learn more:

- [@article@Sorting Algorithms in Python](https://realpython.com/sorting-algorithms-python/)
- [@article@Python - Sorting Algorithms](https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm)
- [@feed@Explore top posts about Algorithms](https://app.daily.dev/tags/algorithms?ref=roadmapsh)

## Sphinx

# sphinx

Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license.

Visit the following resources to learn more:

- [@official@Sphinx Website](https://www.sphinx-doc.org/en/master/)

## Static Typing

# Static Typing

Static typing can be a powerful tool to help you catch bugs before they happen. It can also help you understand the code you're working with, and make it easier to maintain and refactor.

Visit the following resources to learn more:

- [@official@Static Typing in Python](https://typing.readthedocs.io/en/latest/index.html)

## Testing

# Testing

Testing in programming means checking if your code works as expected. It's a systematic way to find and fix errors (bugs) before your code goes live. Imagine building a beautiful house without checking if the walls are straight or the roof doesn't leak—that's what coding without testing can feel like!

Visit the following resources to learn more:

- [@official@Unit Testing in Python](https://docs.python.org/3/library/unittest.html)
- [@article@Python Testing Tutorial](https://realpython.com/python-testing/)

## Threading

# Threading

[Multithreading](https://roadmap.sh/python/multithreading) allows multiple threads within a single process. However, because of GIL, threads cannot run in parallel on different cores, which makes multithreading suitable for I/O tasks (e.g., network requests) but not for computational tasks.

Visit the following resources to learn more:

- [@official@Python Threading Library](https://docs.python.org/3/library/threading.html)
- [@article@Python Multithreading: The Most Practical Intro](https://roadmap.sh/python/multithreading)
- [@article@Introduction to Threading in Python](https://realpython.com/intro-to-python-threading/)

## Tornado

# Tornado

Tornado is a scalable, non-blocking web server and web application framework written in Python. It was developed for use by FriendFeed; the company was acquired by Facebook in 2009 and Tornado was open-sourced soon after.

Visit the following resources to learn more:

- [@official@Tornado Website](https://www.tornadoweb.org/)
- [@article@A Step-by-Step Tutorial on Python Tornado](https://phrase.com/blog/posts/tornado-web-framework-i18n/)
- [@video@Tornado Python Framework](https://www.youtube.com/watch?v=-gJ21qzpieA)

## Tox

# Tox

Tox is a tool for automating test environment management and testing against multiple interpreter configurations. It is particularly useful for Python codebase that need to support multiple versions of Python.

Visit the following resources to learn more:

- [@official@Tox Documentation](https://tox.wiki/en/)

## Tuples

# Tuples

A tuple is an ordered and immutable collection of elements in Python. Unlike lists, tuples cannot be modified after creation, making them useful for storing fixed data such as coordinates, configuration values, or records that should remain unchanged. Tuples support indexing, iteration, and unpacking, and because they are immutable, they can also be used as dictionary keys or returned safely from functions as multiple values.

Visit the following resources to learn more:

- [@official@Tuples Documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [@article@When and How to Use Tuples](https://thenewstack.io/python-for-beginners-when-and-how-to-use-tuples/)
- [@article@Python's tuple Data Type: A Deep Dive With Examples](https://realpython.com/python-tuple/#getting-started-with-pythons-tuple-data-type)
- [@video@why are Tuples even a thing?](https://www.youtube.com/watch?v=fR_D_KIAYrE)

## Type Casting

# Typecasting

The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion: Implicit and Explicit.

Visit the following resources to learn more:

- [@article@Type Conversion and Casting](https://www.programiz.com/python-programming/type-conversion-and-casting)

## Typing

# Typing

The `typing` module provides support for type hints in Python, allowing developers to specify expected data types for variables, function parameters, and return values. Type hints improve code readability, enable better editor support and static analysis, and help catch potential bugs early without changing how Python executes programs at runtime.

Visit the following resources to learn more:

- [@official@Typing Module](https://docs.python.org/3/library/typing.html)

## Unittest  Pyunit

# PyUnit / Unittest

PyUnit is an easy way to create unit testing programs and UnitTests with Python. (Note that [docs.python.org](http://docs.python.org) uses the name "unittest", which is also the module name.)

Visit the following resources to learn more:

- [@official@PyUnit Docs](https://wiki.python.org/moin/PyUnit%C2%A0)
- [@article@How To Use unittest to Write a Test Case for a Function in Python](https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python)
- [@article@A Gentle Introduction to Unit Testing in Python](https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/)

## Uv

# uv

uv is an "extremely fast" python package installer and resolver.

Visit the following resources to learn more:

- [@opensource@astral-sh/uv](https://github.com/astral-sh/uv)
- [@article@@UV for Python](https://www.youtube.com/watch?v=qh98qOND6MI&t)

## Variable Scope

# Variable Scope

Variable scope refers to the region of a program where a particular variable can be accessed. It determines the visibility and lifetime of a variable. Understanding scope is crucial for avoiding naming conflicts and ensuring that variables are used correctly within different parts of your code.

Visit the following resources to learn more:

- [@article@Python Nonlocal Keyword Explained by Our Experts](https://roadmap.sh/python/nonlocal)
- [@article@Python Variable Scope And The LEGB Rule Explained](https://www.datacamp.com/tutorial/scope-of-variables-python)
- [@article@Python Scope](https://www.w3schools.com/python/python_scope.asp)
- [@video@Python Tutorial: Variable Scope - Understanding the LEGB rule and global/nonlocal statements](https://www.youtube.com/watch?v=QVdf0LgmICw)

## Variables And Data Types

# Variables

Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information. Their sole purpose is to label and store data in memory. This data can then be used throughout your program.

Visit the following resources to learn more:

- [@article@Variables in Python](https://realpython.com/python-variables)
- [@article@Python for Beginners: Data Types](https://thenewstack.io/python-for-beginners-data-types/)
- [@video@Python Variables and Data Types](https://www.youtube.com/playlist?list=PLBlnK6fEyqRhN-sfWgCU1z_Qhakc1AGOn)

## Virtualenv

# virtualenv

`virtualenv` is a tool to create isolated Python environments. It creates a folder which contains all the necessary executables to use the packages that a Python project would need.

Visit the following resources to learn more:

- [@official@Virtual Environments](https://virtualenv.pypa.io/en/latest/)

## Working With Strings

# Working with Strings

Strings in Python are sequences of characters used to represent text. You can create them by enclosing characters within single quotes, double quotes, or triple quotes. Once created, strings are immutable, meaning their values cannot be changed directly. Common operations include accessing individual characters using indexing, slicing to extract substrings, concatenating strings using the `+` operator, and using built-in methods to manipulate and format the text they contain.

Visit the following resources to learn more:

- [@official@string — Common string operations](https://docs.python.org/3/library/string.html)
- [@article@Python Strings](https://www.w3schools.com/python/python_strings.asp)
- [@article@Python Print New Line: Methods, Examples, and Best Practices](https://roadmap.sh/python/print-new-line)
- [@article@Python Multiline Strings: The Complete Guide](https://roadmap.sh/python/multiline-strings)
- [@video@String methods in Python are easy 〰️](https://www.youtube.com/watch?v=tb6EYiHtcXU)
- [@video@Python Tutorial for Beginners 2: Strings - Working with Textual Data](https://www.youtube.com/watch?v=k9TUPpGqYTo)

## Yapf

# yapf

yapf is a formatter for Python files. It is a tool that automatically formats Python code to conform to the PEP 8 style guide. It is similar to black but has more configuration options.

Visit the following resources to learn more:

- [@opensource@google/yapf](https://github.com/google/yapf)
