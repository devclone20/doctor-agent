# Java Roadmap

## Abstraction

# Abstraction

The abstract keyword in Java is used to declare a class or a method that cannot be instantiated directly or must be implemented by subclasses, respectively. It is a key part of Java's abstraction mechanism, allowing developers to define abstract classes and methods that provide a blueprint for other classes.

Visit the following resources to learn more:

- [@article@Java Abstract Classes](https://jenkov.com/tutorials/java/abstract-classes.html)
- [@article@Java Interfaces vs. Abstract Classes](https://jenkov.com/tutorials/java/interfaces-vs-abstract-classes.html)

## Access Specifiers

# Access Specifiers

Access specifiers (or access modifiers) in Java are keywords that control the visibility or accessibility of classes, methods, constructors, and other members. They determine from where these members can be accessed. Java provides four access specifiers: `private`, `default` (no keyword), `protected`, and `public`, each offering a different level of access control.

Visit the following resources to learn more:

- [@article@Java Access Modifiers](https://jenkov.com/tutorials/java/access-modifiers.html)

## Annotations

# Annotations

Annotations are a form of metadata that provide data about a program. They are used to provide supplemental information about the code, but they are not a part of the program itself. Annotations can be used by the compiler to detect errors or suppress warnings, and they can also be used at runtime to modify the behavior of the program.

Visit the following resources to learn more:

- [@article@Java Annotations Tutorial](https://jenkov.com/tutorials/java/annotations.html)

## Array Vs Arraylist

# Array vs ArrayList

Arrays and ArrayLists are both ways to store collections of elements in Java. An array is a fixed-size, ordered sequence of elements of the same data type. Once you declare its size, you cannot change it. An ArrayList, on the other hand, is a dynamic, resizable array implementation. It can grow or shrink as needed, allowing you to add or remove elements without worrying about the initial size.

Visit the following resources to learn more:

- [@article@Java Arrays](https://jenkov.com/tutorials/java/arrays.html)
- [@article@Java ArrayLists](https://jenkov.com/tutorials/java-collections/list.html)

## Arrays

# Arrays

Arrays are fundamental data structures used to store a collection of elements of the same data type in contiguous memory locations. They provide a way to organize and access multiple values using a single variable name and an index. Each element in an array can be accessed directly using its index, starting from 0.

Visit the following resources to learn more:

- [@article@Java Arrays](https://jenkov.com/tutorials/java/arrays.html)
- [@video@Java Arrays Tutorial](https://www.youtube.com/watch?v=ei_4Nt7XWOw)

## Attributes And Methods

# Attributes and Methods

Attributes are variables that hold data about an object, defining its state or characteristics. Methods are functions that define the behavior of an object, allowing it to perform actions or operations. Together, attributes and methods encapsulate the data and behavior of an object within a class.

Visit the following resources to learn more:

- [@article@Java Classes](https://jenkov.com/tutorials/java/classes.html)
- [@article@Java Methods](https://jenkov.com/tutorials/java/methods.html)
- [@article@Java Properties](https://jenkov.com/tutorials/java-collections/properties.html)

## Basic Syntax

# Basic Syntax

Understanding the basics is the key to a solid foundation. In this section, learn the basic terminologies, naming conventions, reserved keywords, expressions, statements, data structures, OOP, packages, etc.

*   To print output use --> System.out.println();
*   To take input from user --> Scanner or BufferedReader class can be used

Visit the following resources to learn more:

- [@official@Java Language Basics](https://dev.java/learn/language-basics)
- [@video@Java - Basic Syntax](https://www.youtube.com/watch?v=81piDKqPxjQ)
- [@video@Java Tutorial for Beginners](https://www.youtube.com/watch?v=RRubcjpTkks)

## Basics Of Oop

# Basics of OOP

Object-Oriented Programming (OOP) is a programming paradigm centered around "objects," which contain data in the form of fields (attributes) and code in the form of procedures (methods). OOP focuses on creating reusable code by grouping related data and behavior into objects, allowing for modularity, abstraction, inheritance, and polymorphism. These concepts help in organizing and structuring code in a way that mirrors real-world entities and their interactions.

Visit the following resources to learn more:

- [@article@Java Classes and Objects](https://jenkov.com/tutorials/java/classes.html)

## Bazel

# Bazel

Bazel is an open-source build and test tool similar to Make, Maven, and Gradle. It uses a human-readable, high-level build language. Bazel supports projects in multiple languages and builds outputs for multiple platforms. It's designed for fast, reliable, and reproducible builds, making it suitable for large codebases and complex projects.

Visit the following resources to learn more:

- [@article@Getting started with Bazel](https://bazel.build/start)
- [@article@Build Java Projects with Bazel](https://earthly.dev/blog/build-java-projects-with-bazel/)
- [@article@Introduction to the Bazel Build Tool](https://www.baeldung.com/bazel-build-tool)

## Build Tools

# Build Tools

A build tool is a program or command-line utility that automates the process of compiling, assembling, and deploying software.

Build tools are not only limited to compiling code; they can also help with package management, dependency handling, and continuous integration systems.

## Classes And Objects

# Classes and Objects

Classes are blueprints for creating objects, which are instances of those classes. A class defines the characteristics (attributes) and behaviors (methods) that objects of that class will possess. Think of a class as a template and an object as a specific instance created from that template.

Visit the following resources to learn more:

- [@article@Java Class and Objects](https://www.programiz.com/java-programming/class-objects)
- [@video@Java Classes and Objects](https://www.youtube.com/watch?v=IUqKuGNasdM)

## Concurrency

# Concurrency

Concurrency is the ability of a program to execute multiple tasks seemingly simultaneously. This doesn't necessarily mean they are running at the exact same instant, but rather that their execution overlaps in time. This can be achieved through techniques like multithreading, where a single program is divided into multiple threads that can run concurrently, or through asynchronous programming, where tasks can be started and then the program can continue executing other tasks without waiting for the first task to complete.

Visit the following resources to learn more:

- [@article@Java Concurrency and Multithreading Tutorial](https://jenkov.com/tutorials/java-concurrency/index.html)
- [@article@Java Concurrency in Practice](https://www.baeldung.com/java-concurrency)

## Conditionals

# Conditionals

Java has the following conditional statements:

*   Use `if` to specify a block of code to be executed, if a specified condition is true
*   Use `else` to specify a block of code to be executed if the same condition is false
*   Use `else if` to specify a new condition to test; if the first condition is false
*   Use `switch` to specify many alternative blocks of code to be executed
*   Use `?,:` operator to specify one line condition

Visit the following resources to learn more:

- [@article@What are Conditional statements?](https://www.educative.io/answers/what-are-conditional-statements-in-programming)
- [@video@Conditionals and Loops in Java](https://youtu.be/ldYLYRNaucM)
- [@video@Switch Statements + Nested Case in Java](https://youtu.be/mA23x39DjbI)

## Cryptography

# Cryptography

Cryptography is the practice and study of techniques for secure communication in the presence of adversaries. It involves converting readable data (plaintext) into an unreadable format (ciphertext) through encryption, and then converting the ciphertext back into plaintext through decryption. Cryptography uses algorithms and keys to ensure confidentiality, integrity, authentication, and non-repudiation of information.

Visit the following resources to learn more:

- [@article@Java Cryptography Tutorial](https://jenkov.com/tutorials/java-cryptography/index.html)
- [@video@Cryptography 101 for Java developers](https://www.youtube.com/watch?v=itmNhVckTPc)

## Cucumber Jvm

# Cucumber JVM

Cucumber is a testing tool that supports Behavior Driven Development (BDD). It offers a way to write tests that anybody can understand, regardless of their technical knowledge.

Visit the following resources to learn more:

- [@official@Cucumber](https://cucumber.io/)
- [@official@Cucumber Documentation](https://cucumber.io/docs/cucumber/)
- [@article@Cucumber-JVM for Java](https://automationpanda.com/2017/10/24/cucumber-jvm-for-java/)
- [@video@Cucumber-JVM 5 with Enhanced Cucumber Expression](https://www.youtube.com/watch?v=jCzpxvAJoZM)
- [@feed@Explore top posts about JVM](https://app.daily.dev/tags/jvm?ref=roadmapsh)

## Data Types

# Data Types and Variables

Variable in Java is a data container that stores the data values during Java program execution. Every variable is assigned a data type, which designates the type and quantity of values it can hold. Variable is a memory location name of the data. The Java variables have mainly three types: Local, Instance and Static.

Data Types are divided into two group -

*   Primitive - byte,short,int,long,float,double,boolean and char
*   Non-Primitive - String, Arrays, Classes, Enums and Records

Visit the following resources to learn more:

- [@article@Java Data Types](https://jenkov.com/tutorials/java/variables.html)
- [@article@What are Data Types & Variables?](https://jenkov.com/tutorials/java/data-types.html)

## Database Access

# ORM (Object-Relational Mapping)

A programming method to map objects in Java to relational entities in a database. In other words, converting data between relational databases and object-oriented programming languages. Some popular ORM tools/frameworks in Java are:

*   Spring Data JPA
*   Hibernate
*   Ebean

Visit the following resources to learn more:

- [@article@ORM tutorial](https://www.altexsoft.com/blog/object-relational-mapping/)
- [@article@Java Databases: An Overview of Libraries & APIs](https://www.marcobehler.com/guides/java-databases)
- [@feed@Explore top posts about Java](https://app.daily.dev/tags/java?ref=roadmapsh)

## Date And Time

# Working with Date and Time in Java

Date and Time is a very important concept in programming. Java provides a rich set of classes to work with Date and Time.

Visit the following resources to learn more:

- [@article@Date and Time API in Java](https://chamalwr.medium.com/datetime-api-in-java-2aef5df1c39b)
- [@article@Introduction to Date and Time in Java](https://www.baeldung.com/java-8-date-time-intro)
- [@article@Java SE 8 Date and Time](https://www.oracle.com/technical-resources/articles/java/jf14-date-time.html)

## Dependency Injection

# Dependency Injection

Dependency Injection (DI) is a design pattern where objects receive their dependencies from external sources rather than creating them themselves. This means a class doesn't have to worry about how to obtain the objects it needs to function; instead, those objects are "injected" into the class, usually through its constructor, setter methods, or interface. This promotes loose coupling and makes code more testable and maintainable.

Visit the following resources to learn more:

- [@article@Dependency Injection Tutorial](https://jenkov.com/tutorials/dependency-injection/index.html)
- [@article@Java Dependency Injection Design Pattern Example Tutorial](https://www.digitalocean.com/community/tutorials/java-dependency-injection-design-pattern-example-tutorial)

## Dequeue

# Dequeue

A Dequeue (pronounced "dee-queue") is a double-ended queue, a data structure that allows you to add and remove elements from both the front (head) and the back (tail) of the queue. Unlike a regular queue (FIFO - First-In, First-Out), a dequeue provides flexibility for both FIFO and LIFO (Last-In, First-Out) operations. This makes it useful for implementing various algorithms and data management tasks where elements need to be accessed or modified from either end.

Visit the following resources to learn more:

- [@article@Java Deque Tutorial](https://jenkov.com/tutorials/java-collections/deque.html)
- [@article@Java Deque](https://www.programiz.com/java-programming/deque)

## Ebean

# Ebean

Ebean is an object-relational mapping tool written in Java. It supports the standard JPA annotations for declaring entities. However, it provides a much simpler API for persisting. In fact, one of the points worth mentioning about the Ebean architecture is that it is sessionless, meaning it does not fully manage entities.

Visit the following resources to learn more:

- [@official@Ebean](https://ebean.io/)
- [@official@Ebean Documentation](https://ebean.io/docs/)
- [@article@Guide to Ebean](https://www.baeldung.com/ebean-orm)

## Encapsulation

# Encapsulation

Encapsulation is a fundamental concept in object-oriented programming where data and the methods that operate on that data are bundled together as a single unit. This unit, often a class, hides the internal state of the object from the outside world and only exposes a controlled interface for interacting with it. This protects the data from accidental modification and allows for easier maintenance and modification of the code.

Visit the following resources to learn more:

- [@article@Java - Encapsulation](https://www.tutorialspoint.com/java/java_encapsulation.htm)

## Enums

# Enums

Enums, short for enumerations, are a special data type in Java that represent a group of named constants. They allow you to define a type that can only take on a specific set of predefined values. This makes your code more readable and less prone to errors by restricting the possible values a variable can hold.

Visit the following resources to learn more:

- [@article@Java Enums](https://jenkov.com/tutorials/java/enums.html)
- [@article@Java Enums](https://www.programiz.com/java-programming/enums)

## Exception Handling

# Exception Handling

Exception Handling in Java is one of the effective means to handle the runtime errors so that the regular flow of the application can be preserved. Java Exception Handling is a mechanism to handle runtime errors such as ClassNotFoundException, IOException, SQLException, RemoteException, etc.

There are three types of exceptions -

1.  Checked Exception - exceptions checked at compile time. Example - IOException
2.  Unchecked Exception - exceptions checked at run time. Example - NullPointerException
3.  Error - It is irrecoverable. Example - OutOfMemoryError

Visit the following resources to learn more:

- [@video@Understanding Java Exceptions](https://www.youtube.com/watch?v=W-N2ltgU-X4)
- [@video@Java Exception Handling](https://www.youtube.com/watch?v=1XAfapkBQjk)

## File Operations

# Files and APIs

Learn how to work with files i.e., reading, writing and deleting, files and folders, etc. Also, learn how to make API calls, parse the incoming response, and so on.

*   `FileWriter` - this class is useful to create a file by writing characters into it
*   `FileReader` - this class is useful to read data in form of characters from file
*   `Files.lines(Paths.get("file.txt")))` - processing the files as a stream. Since Java 8
*   `Files.readString / Files.writeString` - reads the whole file and puts it into a string - since Java 11

Visit the following resources to learn more:

- [@article@How To Work With Files In Java](https://www.marcobehler.com/guides/java-files)
- [@article@(old) Java HttpURLConnection Example - Java HTTP Request GET, POST](https://www.digitalocean.com/community/tutorials/java-httpurlconnection-example-java-http-request-get-post)
- [@article@New Java HttpClient](https://www.baeldung.com/java-9-http-client)
- [@article@5 ways to make HTTP requests in Java](https://www.twilio.com/blog/5-ways-to-make-http-requests-in-java)
- [@article@Read a file line by line in Java](https://mkyong.com/java8/java-8-stream-read-a-file-line-by-line/)
- [@article@Various ways to read a file to String in Java](https://howtodoinjava.com/java/io/java-read-file-to-string-examples/)

## Final Keyword

# Final Keyword

The `final` keyword in Java is a non-access modifier used to apply restrictions on a variable, method, or class. When applied to a variable, it makes the variable's value constant after initialization. When applied to a method, it prevents the method from being overridden in a subclass. When applied to a class, it prevents the class from being subclassed (inherited).

Visit the following resources to learn more:

- [@article@Java Final Keyword](https://www.baeldung.com/java-final)
- [@article@How does the final keyword in Java work? I can still modify an object](https://stackoverflow.com/questions/15655012/how-does-the-final-keyword-in-java-work-i-can-still-modify-an-object)

## Functional Composition

# Functional Composition

Functional composition is the process of combining two or more functions to produce a new function. The resulting function applies each function in order, passing the output of one function as the input to the next. This allows you to build complex operations by chaining together simpler, reusable functions.

Visit the following resources to learn more:

- [@article@Functional Composition in Java](https://jenkov.com/tutorials/java-functional-programming/functional-composition.html)
- [@article@Java Functional Programming](https://www.baeldung.com/java-functional-programming)

## Functional Interfaces

# Functional Interfaces

Functional interfaces are interfaces that contain only one abstract method. They can have multiple default or static methods, but only one method that needs to be implemented. These interfaces can be used with lambda expressions and method references, allowing for concise and readable code when dealing with single-method operations.

Visit the following resources to learn more:

- [@article@Java Functional Interfaces](https://jenkov.com/tutorials/java-functional-programming/functional-interfaces.html)
- [@article@Java Functional Interfaces](https://www.baeldung.com/java-8-functional-interfaces)

## Generic Collections

# Generics

Java Generic methods and generic classes enable programmers to specify, with a single method declaration, a set of related methods, or with a single class declaration, a set of related types, respectively.

Visit the following resources to learn more:

- [@article@Java - Generics](https://www.tutorialspoint.com/java/java_generics.htm)
- [@video@Generics in Java](https://www.youtube.com/watch?v=XMvznsY02Mk)

## Gradle

# Gradle

Gradle is an open-source build automation tool that helps software engineers to test, build, and release high-performance software products. In addition, Gradle also supports multi-language development. Currently, the supported languages for Gradle include Java, Kotlin, Groovy, Scala, C/C++, and JavaScript.

Visit the following resources to learn more:

- [@official@Gradle](https://gradle.org/)
- [@article@Building Spring Boot Projects with Gradle](https://www.baeldung.com/spring-boot-gradle-plugin)
- [@video@Gradle Tutorial](https://youtu.be/kONQCIAcWeI)
- [@video@Working with Gradle](https://youtu.be/6V6G3RyxEMk)
- [@feed@Explore top posts about Gradle](https://app.daily.dev/tags/gradle?ref=roadmapsh)

## Hibernate

# Hibernate

Hibernate is an open source object-relational mapping tool that provides a framework to map object-oriented domain models to relational databases for web applications. Hibernate implements the specifications of JPA. Performance is key so Hibernate supports first-level and second-level caching

Visit the following resources to learn more:

- [@official@Hibernate](https://hibernate.org/)
- [@article@Second-level caching explained](https://hazelcast.com/glossary/hibernate-second-level-cache/)

## High Order Functions

# High Order Functions

High Order Functions are functions that can either accept other functions as arguments or return functions as their results. This capability allows for more flexible and reusable code by enabling you to abstract over operations. Essentially, you can pass behavior as data, making your code more dynamic and adaptable to different situations.

Visit the following resources to learn more:

- [@article@Java High Order Functions](https://jenkov.com/tutorials/java-functional-programming/higher-order-functions.html)

## Inheritance

# Inheritance

Inheritance is a fundamental concept in object-oriented programming where a new class (called a subclass or derived class) acquires properties and behaviors from an existing class (called a superclass or base class). This allows for code reuse and the creation of hierarchical relationships between classes, promoting a more organized and maintainable codebase. The subclass can extend the superclass by adding new attributes and methods or overriding existing ones.

Visit the following resources to learn more:

- [@article@Java Inheritance](https://jenkov.com/tutorials/java/inheritance.html)
- [@article@Inheritance in Java with Example](https://www.digitalocean.com/community/tutorials/inheritance-java-example)

## Initializer Block

# Initializer Block

An initializer block in Java is a block of code, enclosed in curly braces `{}` , that is executed when an instance of a class is created. It's used to initialize instance variables or perform setup tasks before the constructor is called. There are two types: instance initializer blocks, which run every time a new object is created, and static initializer blocks, which run only once when the class is first loaded.

Visit the following resources to learn more:

- [@article@Static and Instance Initializer Blocks in Java](https://www.baeldung.com/java-static-instance-initializer-blocks)
- [@article@All About Java Instance Initializer Blocks](https://blogs.oracle.com/javamagazine/post/java-instance-initializer-block)
- [@article@What is an initialization block?](https://stackoverflow.com/questions/3987428/what-is-an-initialization-block)

## Interfaces

# Interfaces

An interface in Java is a blueprint of a class. It specifies a set of methods that a class must implement if it claims to implement the interface. Think of it as a contract: any class that "signs" the contract (implements the interface) agrees to provide specific behaviors (methods). Interfaces can also contain constants (static final variables). They help achieve abstraction and multiple inheritance in Java.

Visit the following resources to learn more:

- [@article@Interfaces in Java](https://jenkov.com/tutorials/java/interfaces.html)
- [@article@A Guide to Java Interfaces](https://www.baeldung.com/java-interfaces)

## Io Operations

# I/O Operations

I/O Operations, short for Input/Output Operations, deal with how a program interacts with the outside world. This involves reading data from sources like files, network connections, or the keyboard, and writing data to destinations such as files, the console, or network sockets. Essentially, it's the mechanism by which a program receives information and sends results.

Visit the following resources to learn more:

- [@article@Java IO Tutorial](https://jenkov.com/tutorials/java-io/index.html)

## Iterator

# Iterator

An Iterator is an object that enables you to traverse through a collection (like a List or Set) one element at a time. It provides a standard way to access elements sequentially without needing to know the underlying structure of the collection. You can use methods like `hasNext()` to check if there's a next element and `next()` to retrieve it.

Visit the following resources to learn more:

- [@article@Java Iterator Tutorial](https://jenkov.com/tutorials/java-collections/iterator.html)
- [@article@Java Iterable Tutorial](https://jenkov.com/tutorials/java-collections/iterable.html)

## Java Memory Model

# Java Memory Model

The Java Memory Model (JMM) defines how threads in Java interact with memory. It specifies how and when different threads can see writes to shared variables, addressing issues like data visibility and race conditions in concurrent programs. The JMM ensures that multithreaded Java programs behave predictably across different hardware architectures by establishing rules for memory synchronization and ordering.

Visit the following resources to learn more:

- [@article@Java Memory Model](https://jenkov.com/tutorials/java-concurrency/java-memory-model.html)

## Javalin

# Javalin

Javalin is a lightweight web framework for Java and Kotlin that's designed to be simple, intuitive, and fun to use. It allows developers to quickly build web applications and APIs with minimal boilerplate code. Javalin focuses on providing a straightforward approach to routing, request handling, and response generation, making it a good choice for projects where speed of development and ease of understanding are important.

Visit the following resources to learn more:

- [@official@Javalin Website](https://javalin.io/)
- [@article@Creating a REST API with Javalin](https://www.baeldung.com/javalin-rest-microservices)

## Jdbc

# Java JDBC

JDBC is an API(Application programming interface) used in java programming to interact with databases. The classes and interfaces of JDBC allow the application to send requests made by users to the specified database.

Visit the following resources to learn more:

- [@article@IBM: What is JDBC](https://www.ibm.com/docs/en/informix-servers/12.10?topic=started-what-is-jdbc)
- [@feed@Explore top posts about Java](https://app.daily.dev/tags/java?ref=roadmapsh)

## Jmeter

# JMeter

Apache JMeter is an Apache project that can be used as a load testing tool for analyzing and measuring the performance of a variety of services, with a focus on web applications.

Visit the following resources to learn more:

- [@article@Apache JMeter Website](https://jmeter.apache.org/)
- [@feed@Explore top posts about Testing](https://app.daily.dev/tags/testing?ref=roadmapsh)

## Junit

# JUnit

JUnit is a testing framework for Java.

Visit the following resources to learn more:

- [@official@JUnit](https://junit.org/junit5)
- [@official@JUnit Documentation](https://junit.org/junit5/docs/current/user-guide/)
- [@article@JUnit tutorial](https://www.guru99.com/junit-tutorial.html)
- [@article@Basic JUnit tutorial](https://www.baeldung.com/junit-5)
- [@video@Testing with JUnit crash course](https://www.youtube.com/watch?v=flpmSXVTqBI)

## Lambda Expressions

# Lambda Expressions

Lambda expressions are essentially short blocks of code that you can pass around to be executed. They allow you to treat functionality as a method argument, or code as data. Think of them as anonymous methods – methods without a name – that can be written directly in the place where they are needed, making your code more concise and readable, especially when dealing with functional interfaces.

Visit the following resources to learn more:

- [@article@Java Lambda Expressions](https://jenkov.com/tutorials/java/lambda-expressions.html)

## Learn The Basics

# Java Fundamentals

Java is a programming language and computing platform first released by Sun Microsystems in 1995. Java is a general-purpose, class-based, object-oriented programming language designed for having lesser implementation dependencies. It is a computing platform for application development. Java is fast, secure, and reliable. Therefore, it is widely used for developing Java applications in laptops, data centers, game consoles, scientific supercomputers, cell phones, etc.

Learn about the fundamentals of Java such as basic syntax, data types, variables, conditionals, functions, data structures, packages, etc.

Visit the following resources to learn more:

- [@course@Introduction to Java by Hyperskill (JetBrains Academy)](https://hyperskill.org/tracks/8)
- [@article@Head First Java](https://www.amazon.co.uk/Head-First-Java-3rd-Brain-Friendly/dp/1491910771)
- [@article@Thinking in Java](https://www.amazon.co.uk/Thinking-Java-Eckel-Bruce-February/dp/B00IBON6C6)
- [@article@Effective Java](https://www.amazon.com/Effective-Java-Joshua-Bloch/dp/0134685997)
- [@article@Java: A Beginners Guide](https://www.amazon.co.uk/Java-Beginners-Guide-Herbert-Schildt/dp/1260463559)
- [@article@Java: The Complete Reference](https://www.amazon.co.uk/gp/product/B09JL8BMK7/ref=dbs_a_def_rwt_bibl_vppi_i2)
- [@video@Java Tutorial for Beginners](https://youtu.be/eIrMbAQSU34)
- [@video@Java + DSA + Interview Preparation Course (For beginners)](https://youtube.com/playlist?list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ)
- [@feed@Explore top posts about Java](https://app.daily.dev/tags/java?ref=roadmapsh)

## Lifecycle Of A Program

# Lifecycle of a Program

In Java, the program lifecycle consists of several distinct phases that work together to execute code. The process begins with developers writing Java source code in `.java` files using an IDE or text editor. This code is then compiled by the Java compiler (javac) into bytecode stored in `.class` files, with syntax and type checking performed during compilation. When the program runs, the Java Virtual Machine (JVM) loads these compiled class files into memory through a process involving loading of binary data, linking for verification and preparation, and initialization of class elements. The JVM then verifies the bytecode's security compliance, performs Just-In-Time (JIT) compilation to translate bytecode into native machine code for better performance, and executes the program instructions while managing system resources. Throughout execution, the JVM handles garbage collection by reclaiming memory from unused objects, and finally releases all resources upon program termination. This architecture enables Java's "write once, run anywhere" capability since the bytecode can execute on any device with a compatible JVM.

Visit the following resources to learn more:

- [@article@Life Cycle of a Java Program](https://www.startertutorials.com/corejava/life-cycle-java-program.html)
- [@article@How the JVM Executes Java Code](https://www.cesarsotovalero.net/blog/how-the-jvm-executes-java-code.html)
- [@article@JIT vs. AOT Compilation in Java](https://bell-sw.com/blog/compilation-in-java-jit-vs-aot/)

## Log4J2

# Log4j2

Apache Log4j is a Java-based logging utility. Log4j Java library's role is to log information that helps applications run smoothly, determine what's happening, and help with the debugging process when errors occur. Logging libraries typically write down messages to the log file or a database.

Log4j2 is the updated version of the popular and influential log4j library, used extensively throughout the Java ecosystem for so many years. Version 2. x keeps all the logging features of its predecessor and builds on that foundation with some significant improvements, especially in the area of performance.

Visit the following resources to learn more:

- [@article@Official Website](https://logging.apache.org/log4j/2.x/manual/configuration.html)
- [@article@Log4j explained: Everything you need to know](https://www.techtarget.com/whatis/feature/Log4j-explained-Everything-you-need-to-know)

## Logback

# Logback

Logback is one of the most widely used logging frameworks in the Java Community. It's a replacement for its predecessor, Log4j. Logback offers a faster implementation, provides more options for configuration, and more flexibility in archiving old log files.

Visit the following resources to learn more:

- [@article@Official Website](https://logback.qos.ch/manual/configuration.html)

## Logging Frameworks

# Logging Frameworks

Logging is an important feature that helps developers to trace out the errors. It provides the ability to capture the log file. Logging provides the complete tracing information of the application and also records the critical failure if any occur in an application. There are three components of Logging: Logger, Logging handlers or Appenders and Layouts or logging formatters.

Visit the following resources to learn more:

- [@article@Introduction to Java Logging](https://www.baeldung.com/java-logging-intro)
- [@article@Java Logging Frameworks](https://en.wikipedia.org/wiki/Java_logging_framework)
- [@article@How to Do Logging In Java](https://www.marcobehler.com/guides/java-logging)
- [@feed@Explore top posts about Java](https://app.daily.dev/tags/java?ref=roadmapsh)

## Loops

# Loops

In Java and other programming languages, loops are used to iterate a part of the program several times. There are four types of loops in Java, `for`, `forEach`, `while`, and `do...while`.

*   Syntax of `for` loop is `for(initialization;condition;increment/decrement){}`
*   Syntax of `forEach` loop is `for(data_type variable:array_name){}`

Visit the following resources to learn more:

- [@article@Loops in Java.](https://www.programiz.com/java-programming/for-loop)

## Map

# Map

A Map is a data structure that stores data in key-value pairs. Each key is unique, and it maps to a specific value. Think of it like a dictionary where you use a word (the key) to look up its definition (the value). Maps allow you to efficiently retrieve, add, or remove values based on their associated keys.

Visit the following resources to learn more:

- [@article@Generic Map in Java](https://jenkov.com/tutorials/java-generics/generic-map.html)
- [@article@Java Map](https://jenkov.com/tutorials/java-collections/map.html)
- [@article@Java ConcurrentMap](https://jenkov.com/tutorials/java-util-concurrent/concurrentmap.html)
- [@article@Java SortedMap](https://jenkov.com/tutorials/java-collections/sortedmap.html)

## Math Operations

# Math Operations

Math operations involve performing calculations using numbers. These operations include addition, subtraction, multiplication, division, and modulus (finding the remainder). They are fundamental building blocks for solving numerical problems and manipulating data in programming.

Visit the following resources to learn more:

- [@article@Java Math](https://jenkov.com/tutorials/java/math-operators-and-math-class.html)

## Maven

# Maven

Maven is an open-source build tool, used primarily for Java projects.

Visit the following resources to learn more:

- [@article@Getting started](https://maven.apache.org/guides/getting-started/)
- [@article@Building Spring Projects with Maven](https://www.baeldung.com/spring-with-maven)
- [@feed@Explore top posts about Maven](https://app.daily.dev/tags/maven?ref=roadmapsh)

## Method Chaining

# Method Chaining

Method chaining is a programming technique where multiple method calls are made sequentially on the same object, one after another, in a single statement. Each method in the chain returns an object, allowing the next method to be called on that returned object. This approach enhances code readability and conciseness by reducing the need for temporary variables and intermediate steps.

Visit the following resources to learn more:

- [@article@@GeeksforGeeks@Method Chaining In Java with Examples](https://www.geeksforgeeks.org/java/method-chaining-in-java-with-examples/)
- [@article@How to achieve method chaining in Java](https://stackoverflow.com/questions/21180269/how-to-achieve-method-chaining-in-java)

## Method Overloading  Overriding

# Method Overloading and Overriding

Method overloading allows you to define multiple methods in the same class with the same name but different parameters (different number, types, or order of parameters). Method overriding, on the other hand, occurs when a subclass provides a specific implementation for a method that is already defined in its superclass. The method signature (name and parameters) must be the same in both the superclass and the subclass for overriding to occur.

Visit the following resources to learn more:

- [@article@Overriding vs Overloading in Java](https://www.digitalocean.com/community/tutorials/overriding-vs-overloading-in-java)
- [@article@Java Inheritance Tutorial](https://jenkov.com/tutorials/java/inheritance.html)

## Mocking  Mockito

# Mocking

Mocking removes external dependencies from a unit test to create a sense of an entire controlled environment. The traditional method of mocks involves mocking all other classes that interact with the class we want to test. The common targets for mocking are:

*   Database connections
*   Web services
*   Slow Classes
*   Classes with side effects
*   Classes with non-deterministic behavior

Visit the following resources to learn more:

- [@article@Mockito - Mocking Framework for Java](https://site.mockito.org/)
- [@feed@Explore top posts about Testing](https://app.daily.dev/tags/testing?ref=roadmapsh)

## Modules

# Modules

Modules in Java are a way to organize code into reusable and independent units. They provide a higher level of abstraction than packages, allowing you to control which parts of your code are exposed to other modules and which are kept private. This enhances encapsulation, improves security, and simplifies dependency management by explicitly declaring dependencies between modules.

Visit the following resources to learn more:

- [@article@Java Modules](https://jenkov.com/tutorials/java/modules.html)
- [@article@A Guide to Java 9 Modularity](https://www.baeldung.com/java-modularity)

## Nested Classes

# Nested Classes

Nested classes are classes defined inside another class. The class that contains the inner class is known as the outer class. Nested classes can access members of the outer class, even if they are declared private. They are a way to logically group classes that are only used in one place, increasing encapsulation and maintainability.

Visit the following resources to learn more:

- [@article@Java Nested Classes](https://jenkov.com/tutorials/java/nested-classes.html)
- [@article@Guide to Nested Classes in Java](https://www.baeldung.com/java-nested-classes)

## Networking

# Networking sockets

*   Java Networking is a concept of connecting two or more computing devices together so that we can share resources.
*   Java socket programming provides facility to share data between different computing devices.
*   A socket is one endpoint of a two-way communication link between two programs running on the network. A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to.

Visit the following resources to learn more:

- [@article@Sockets](https://docs.oracle.com/javase/tutorial/networking/sockets/index.html)
- [@article@Java Networking](https://www.tutorialspoint.com/java/java_networking.htm)
- [@video@What is Socket Programming?](https://youtu.be/BqBKEXLqdvI)
- [@feed@Explore top posts about Networking](https://app.daily.dev/tags/networking?ref=roadmapsh)

## Object Lifecycle

# Object Lifecycle

The object lifecycle refers to the series of stages an object goes through from its creation (allocation of memory) to its destruction (reclaiming of memory). These stages typically include object creation, initialization, usage, and eventual garbage collection when the object is no longer needed. Understanding this lifecycle is crucial for efficient memory management and preventing resource leaks.

## Optionals

# Optionals

Optionals are a container object that may or may not contain a non-null value. They are primarily used to represent the absence of a value, avoiding the need to return null, which can lead to NullPointerExceptions. Optionals provide methods to explicitly check if a value is present and to handle cases where a value is absent in a more controlled and readable manner.

Visit the following resources to learn more:

- [@article@Guide To Optionals](https://www.baeldung.com/java-optional)
- [@article@Java Optional](https://dzone.com/articles/optional-in-java)

## Packages

# Packages

A package is a namespace that mainly contains classes and interfaces. For instance, the standard class `ArrayList` is in the package `java.util`. For this class, `java.util.ArrayList` is called its fully qualified name because this syntax has no ambiguity. Classes in different packages can have the same name. For example, you have the two classes `java.util.Date` and `java.sql.Date`, which are different. If no package is declared in a class, its package is the default package.

To create package use this command -> javac -d directory javafilename

Visit the following resources to learn more:

- [@article@Packages in Java](https://docs.oracle.com/javase/8/docs/api/java/lang/Package.html)

## Pass By Value  Pass By Reference

# Pass by Value / Pass by Reference

Pass by value and pass by reference are two different ways of passing arguments to a function or method. In pass by value, a copy of the variable's value is passed to the function, so any changes made to the parameter inside the function do not affect the original variable. In pass by reference, a direct reference to the variable is passed, meaning that changes made to the parameter inside the function will directly affect the original variable.

Visit the following resources to learn more:

- [@article@Java is Pass-by-Value, Not Pass-by-Reference](https://www.baeldung.com/java-pass-by-value-or-pass-by-reference)
- [@article@Is Java "pass-by-reference" or "pass-by-value"?](https://stackoverflow.com/questions/40480/is-java-pass-by-reference-or-pass-by-value)

## Play Framework

# Play Framework

Play Framework is a high-productivity web application framework that allows the model-view-controller pattern. It is written in Scala but can also be used for other programming languages that are compiled and run on the JVM. e.g.Java.

Visit the following resources to learn more:

- [@official@Play Framework Website](https://www.playframework.com/)
- [@article@What is Play Framework?](https://en.wikipedia.org/wiki/Play_Framework)
- [@article@Intro to Play Framework](https://www.baeldung.com/java-intro-to-the-play-framework)
- [@video@Introduction to Play Framework](https://youtu.be/bLrmnjPQsZc)

## Quarkus

# Quarkus

Visit the following resources to learn more:

- [@official@Official Website](https://quarkus.io/)
- [@feed@Explore top posts about Quarkus](https://app.daily.dev/tags/quarkus?ref=roadmapsh)

## Queue

# Queue

A queue is a fundamental data structure that follows the First-In, First-Out (FIFO) principle. Think of it like a line at a store: the first person to join the line is the first person to be served. Elements are added to the rear (enqueue) and removed from the front (dequeue) of the queue.

Visit the following resources to learn more:

- [@article@Java Queue](https://jenkov.com/tutorials/java-collections/queue.html)

## Record

# Record

A record is a special type of class in Java that is designed to hold immutable data. It automatically generates methods like `equals()`, `hashCode()`, and `toString()` based on the components declared in its header, reducing boilerplate code. Records are useful for creating data transfer objects (DTOs) or simple data aggregates where the primary purpose is to store and access data.

Visit the following resources to learn more:

- [@article@Java Records](https://jenkov.com/tutorials/java/record.html)
- [@video@Java Records](https://www.youtube.com/watch?v=xs7DiEIHW0U)

## Regular Expressions

# Regular Expressions

Regular expressions, often shortened to "regex," are sequences of characters that define a search pattern. These patterns are used to match character combinations in strings. They can be used to search, edit, or manipulate text and data. Regular expressions provide a powerful and flexible way to work with text-based data.

Visit the following resources to learn more:

- [@article@Java Regular Expressions Tutorial](https://jenkov.com/tutorials/java-regex/index.html)

## Rest Assured

# Rest assured

Testing and validating REST services in Java is harder than in dynamic languages such as Ruby and Groovy. REST Assured brings the simplicity of using these languages into the Java domain.

Visit the following resources to learn more:

- [@official@Rest-assured](https://rest-assured.io/)
- [@opensource@Rest-assured Documentation](https://github.com/rest-assured/rest-assured/wiki)
- [@article@A Guide to REST-assured](https://www.baeldung.com/rest-assured-tutorial)
- [@feed@Explore top posts about REST API](https://app.daily.dev/tags/rest-api?ref=roadmapsh)

## Set

# Set

A Set is a data structure that stores a collection of unique elements. This means that no duplicate values are allowed within a Set. Sets provide efficient ways to check for membership (if an element exists in the set) and perform operations like union, intersection, and difference.

Visit the following resources to learn more:

- [@article@Java Set](https://jenkov.com/tutorials/java-collections/set.html)
- [@article@Java Set Interface and Implementation](https://www.digitalocean.com/community/tutorials/java-set)

## Slf4J

# Slf4j

The SLF4J or the Simple Logging Facade for Java is an abstraction layer for various Java logging frameworks, like Log4j 2 or Logback. This allows for plugging different logging frameworks at deployment time without the need for code changes.

Visit the following resources to learn more:

- [@article@Official Website](https://www.slf4j.org/)

## Spring Data Jpa

# Spring data jpa

Spring Data JPA aims to significantly improve the implementation of data access layers by reducing the effort to the amount that's actually needed. As a developer you write your repository interfaces, including custom finder methods, and Spring will provide the implementation automatically.

Visit the following resources to learn more:

- [@official@Spring Data JPA](https://spring.io/projects/spring-data-jpa)
- [@article@Introduction to Spring Data JPA](https://www.baeldung.com/the-persistence-layer-with-spring-data-jpa)
- [@video@Spring Data JPA Tutorial](https://youtu.be/XszpXoII9Sg)
- [@video@Spring Boot Tutorial - Spring Data JPA](https://youtu.be/8SGI_XS5OPw)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Spring Spring Boot

# Spring Boot

Spring Boot is an open source, microservice-based Java web framework. The Spring Boot framework creates a fully production-ready environment that is completely configurable using its prebuilt code within its codebase. The microservice architecture provides developers with a fully enclosed application, including embedded application servers.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Spring Boot Roadmap](https://roadmap.sh/spring-boot)
- [@official@Spring Boot](https://spring.io/projects/spring-boot/)
- [@article@What is Spring Boot?](https://www.ibm.com/cloud/learn/java-spring-boot)
- [@article@Spring Boot Tutorial](https://www.javaguides.net/2021/07/spring-boot-tutorial-for-beginners.html)
- [@article@Learn Spring Boot](https://www.baeldung.com/spring-boot)
- [@video@Spring Boot Tutorial](https://youtu.be/vtPkZShrvXQ)
- [@video@Spring Boot for Beginners](https://youtu.be/UfOxcrxhC0s)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Stack

# Stack

A stack is a fundamental data structure that follows the Last-In, First-Out (LIFO) principle. Imagine a stack of plates; you can only add or remove plates from the top. This means the last element added to the stack is the first one to be removed. Stacks are used to manage function calls, evaluate expressions, and implement undo/redo functionality.

Visit the following resources to learn more:

- [@article@Java Stack Tutorial](https://jenkov.com/tutorials/java-collections/stack.html)
- [@article@Guide to Java Stack](https://www.baeldung.com/java-stack)

## Static Keyword

# Static Keyword

The `static` keyword in Java is used to create members (variables and methods) that belong to the class itself, rather than to any specific instance of the class. This means there's only one copy of a static variable shared by all objects of that class, and you can access static members directly using the class name without needing to create an object. Static methods can only access static variables and call other static methods.

Visit the following resources to learn more:

- [@article@Java Static Keyword Explained With Examples](https://www.freecodecamp.org/news/java-static-keyword-explained/)
- [@article@Static and Non-static Fields in Java](https://jenkov.com/tutorials/java/fields.html#static-and-non-static-fields)
- [@article@Guide to the Java 'static' Keyword](https://www.baeldung.com/java-static)

## Static Vs Dynamic Binding

# Static vs Dynamic Binding

Static binding, also known as early binding, happens at compile time. The compiler knows exactly which method will be called based on the type of the variable. Dynamic binding, or late binding, occurs at runtime. The specific method to be called is determined based on the actual object type, not the variable type, allowing for more flexibility and polymorphism.

Visit the following resources to learn more:

- [@article@Static and Dynamic Binding in Java](https://www.baeldung.com/java-static-dynamic-binding)
- [@article@Static and Dynamic Binding in Java with Examples](https://beginnersbook.com/2013/04/java-static-dynamic-binding/)

## Stream Api

# Streams

Java provides a new additional package in Java 8 called java.util.stream. This package consists of classes, interfaces and enum to allows functional-style operations on the elements. You can use stream by importing java.util.stream package.

Visit the following resources to learn more:

- [@article@The Java 8 Stream API Tutorial](https://www.baeldung.com/java-8-streams)
- [@video@Streams API Tutorial in Java 8+](https://www.youtube.com/watch?v=VNovNwHr9jY)
- [@video@Java 8 Streams Tutorial](https://www.youtube.com/watch?v=t1-YZ6bF-g0)

## Strings And Methods

# Strings and Methods

Strings are sequences of characters, like words or sentences, used to represent text in programming. Methods are actions you can perform on these strings, such as finding their length, changing their case (uppercase or lowercase), or extracting parts of them. These methods allow you to manipulate and work with text data effectively.

Visit the following resources to learn more:

- [@article@Java Strings](https://jenkov.com/tutorials/java/strings.html)

## Testing

# Testing

A key to building software that meets requirements without defects is testing. Software testing helps developers know they are building the right software. When tests are run as part of the development process (often with continuous integration tools), they build confidence and prevent regressions in the code.

Visit the following resources to learn more:

- [@article@What is Software Testing?](https://www.guru99.com/software-testing-introduction-importance.html)
- [@article@Testing Pyramid](https://www.browserstack.com/guide/testing-pyramid-for-test-automation)
- [@feed@Explore top posts about Java](https://app.daily.dev/tags/java?ref=roadmapsh)

## Testng

# Testng

TestNG is a testing framework inspired from JUnit and NUnit but introducing some new functionalities that make it more powerful and easier to use.

Visit the following resources to learn more:

- [@official@Testng](https://testng.org)
- [@official@Testng Documentation](https://testng.org/doc/documentation-main.html)
- [@article@Testng tutorial](https://www.guru99.com/all-about-testng-and-selenium.html)

## Threads

# Basics of Threads

A thread in Java is the direction or path that is taken while a program is being executed. Generally, all the programs have at least one thread, known as the main thread, that is provided by the JVM or Java Virtual Machine at the starting of the program’s execution.

Writing correct multi-threaded application is complex and it's an advanced topic. Things like ParallelStreams, thread-safe Collections and ExecutorService can be helpful.

Visit the following resources to learn more:

- [@article@Threads in Java](https://jenkov.com/tutorials/java-concurrency/index.html)
- [@video@Java Threads Tutorial](https://www.youtube.com/watch?v=TCd8QIS-2KI)

## Tinylog

# Tinylog

Tinylog is a lightweight open-source logging framework for Java and Android, optimized for ease of use.

Visit the following resources to learn more:

- [@official@Official Website](https://tinylog.org/v1/)
- [@official@TinyLog v2](https://tinylog.org/v2/)

## Type Casting

# Type Casting

Type casting is the process of converting a variable from one data type to another. This is often necessary when you need to perform operations between variables of different types, or when you need to store a value of one type in a variable of another type. In Java, type casting can be either implicit (automatic) or explicit (requiring a cast operator).

Visit the following resources to learn more:

- [@article@Type Casting in Java: Everything You Need to Know](https://www.simplilearn.com/tutorials/java-tutorial/type-casting-in-java)
- [@article@Java Type Casting (With Examples)](https://www.programiz.com/java-programming/typecasting)

## Variables And Scopes

# Variables and Scopes

Variables are like containers that hold data in a program. Each variable has a name, a type (like integer, text, or boolean), and a value. The scope of a variable determines where in your code you can access and use that variable. Understanding scope is crucial to avoid naming conflicts and ensure data is accessed correctly within different parts of your program.

Visit the following resources to learn more:

- [@article@Java Variables](https://jenkov.com/tutorials/java/variables.html)
- [@article@Java Variable Scope](https://www.baeldung.com/java-variable-scope)

## Virtual Threads

# Virtual Threads

Virtual Threads are lightweight threads managed by the Java Virtual Machine (JVM). Unlike traditional operating system threads, which are relatively expensive to create and manage, virtual threads are designed to be extremely lightweight, allowing for the creation of millions of them. They are intended to improve the scalability and concurrency of Java applications by making it easier to write code that can handle a large number of concurrent operations without the overhead associated with traditional threads.

Visit the following resources to learn more:

- [@article@Java 21 Virtual Threads: Dude, Where's My Lock?](https://netflixtechblog.com/java-21-virtual-threads-dude-wheres-my-lock-3052540e231d)
- [@article@Virtual Thread vs Thread in Java](https://www.baeldung.com/java-virtual-thread-vs-thread)
- [@article@The Ultimate Guide to Java Virtual Threads](https://rockthejvm.com/articles/the-ultimate-guide-to-java-virtual-threads)

## Volatile Keyword

# Volatile Keyword

The `volatile` keyword in Java is a modifier that can be applied to instance variables. It ensures that all threads see the most up-to-date value of a variable. Without `volatile`, each thread might cache its own copy of the variable, leading to inconsistencies when multiple threads access and modify it concurrently. Using `volatile` forces the thread to read the variable's value directly from main memory, and write changes directly back to main memory, bypassing the thread's local cache.

Visit the following resources to learn more:

- [@article@Java Volatile Keyword](https://jenkov.com/tutorials/java-concurrency/volatile.html)
- [@article@Guide to the Volatile Keyword in Java](https://www.baeldung.com/java-volatile)

## Web Frameworks

# Web Frameworks

Frameworks are tools with pre-written code, that act as a template or skeleton, which can be reused to create an application by simply filling with your code as needed which enables developers to program their application with no overhead of creating each line of code again and again from scratch.
