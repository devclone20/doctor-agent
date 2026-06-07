# Kotlin Roadmap

---
renderer: editor
---

---

## Abstract Class

# Abstract Class

An abstract class in Kotlin is a class that cannot be instantiated directly. It's designed to be a blueprint for other classes. Abstract classes can contain both abstract members (methods and properties without implementation) and concrete members (with implementation). Subclasses (derived classes) must implement the abstract members, providing their specific behavior, unless the subclass itself is also declared abstract. This enforces a certain structure and behavior across a family of related classes.

Visit the following resources to learn more:

- [@official@Abstract classes](https://kotlinlang.org/docs/classes.html#abstract-classes)
- [@article@Kotlin Abstract Class](https://www.programiz.com/kotlin-programming/abstract-class)
- [@video@Kotlin Newbie to Pro - ABSTRACT CLASSES](https://www.youtube.com/watch?v=ju-LDSDwGC8)

## Aggregate Operations

# Aggregate Operations

Aggregate operations in Kotlin collections transform a collection into a single result. These operations combine the elements of a collection using a specific function. Common examples include finding the sum, average, minimum, or maximum value within a collection. They provide a concise way to derive a summary value from a set of data.

Visit the following resources to learn more:

- [@official@Aggregate operations](https://kotlinlang.org/docs/collection-aggregate.html)
- [@video@Collections | fold | reduce | aggregate functions](https://www.youtube.com/watch?v=2dteZg_1TZ0)

## Ai Development

# AI Development

Kotlin provides a modern and pragmatic foundation for building AI-powered applications.
It can be used across platforms, integrates well with established AI frameworks, and supports common AI development patterns through its AI agentic framework, Koog. There are many use cases where Kotlin can help with AI development, from integrating language models into backend services to building AI-powered user interfaces.

Visit the following resources to learn more:

- [@official@Kotlin for AI-powered app development](https://kotlinlang.org/docs/kotlin-ai-apps-development-overview.html)
- [@opensource@Kotlin AI Examples](https://github.com/Kotlin/Kotlin-AI-Examples)

## Android Jetpack

# Android Jetpack

Android Jetpack is a suite of libraries, tools, and architectural guidance designed to help developers build robust, testable, and maintainable Android applications more easily. It addresses common Android development challenges by providing pre-built components for tasks like managing UI, data persistence, background processing, and navigation, allowing developers to focus on writing unique application logic. These components are designed to work together seamlessly and are backward-compatible, ensuring apps work across a wide range of Android versions.

Visit the following resources to learn more:

- [@article@Kotlin for Jetpack](https://developer.android.com/develop/ui/compose/kotlin)
- [@course@Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)

## Android Sdk

# Android SDK

The Android SDK (Software Development Kit) is a set of tools, libraries, documentation, and sample code provided by Google that allows developers to create applications for the Android operating system. It provides the necessary APIs and development environment to build, test, and debug Android apps. The SDK includes tools for compiling code, debugging, emulating devices, and packaging applications for distribution.

Visit the following resources to learn more:

- [@official@Kotlin for Android](https://kotlinlang.org/docs/android-overview.html)
- [@article@Develop Android apps with Kotlin](https://developer.android.com/kotlin)
- [@official@Android & Kotlin Development Masterclass – Full Course](https://www.youtube.com/watch?v=blKkRoZPxLc&ab_channel=freeCodeCamp.org)

## Android Studio

# Android Studio

Android Studio is the official Integrated Development Environment (IDE) for Android app development, and it fully supports Kotlin. It provides tools for coding, debugging, testing, and designing user interfaces for Android applications. With features like code completion, refactoring, and a visual layout editor, Android Studio streamlines the process of building Kotlin-based Android apps.

Visit the following resources to learn more:

- [@official@Kotlin for Android](https://kotlinlang.org/docs/android-overview.html)
- [@article@Develop Android apps with Kotlin](https://developer.android.com/kotlin)
- [@course@Introduction to programming in Kotlin](https://developer.android.com/courses/pathways/android-basics-compose-unit-1-pathway-1)

## Android Studio

# Android Studio

Android Studio is the official Integrated Development Environment (IDE) for Android app development, built on JetBrains' IntelliJ IDEA. It provides a comprehensive suite of tools for designing, developing, debugging, and testing Android applications. It includes features like a visual layout editor, code completion, debugging tools, and integration with the Android SDK and emulator.

Visit the following resources to learn more:

- [@official@Android Studio](https://developer.android.com/studio)
- [@official@Develop Android apps with Kotlin](https://developer.android.com/kotlin)
- [@video@Android & Kotlin Development Masterclass – Full Course](https://www.youtube.com/watch?v=blKkRoZPxLc)

## Anonymous Functions

# Anonymous Functions

Anonymous functions in Kotlin are functions without a name. They are defined using a lambda expression but with an explicit return type and the `return` keyword for returning values. They are useful when you need to define a function inline, often as an argument to another function or when assigning a function to a variable, especially when the function logic is more complex than a simple expression.

Visit the following resources to learn more:

- [@official@Anonymous Functions](https://kotlinlang.org/docs/lambdas.html#anonymous-functions)
- [@article@Kotlin Lambda Expressions + Kotlin Anonymous Functions](https://medium.com/huawei-developers/kotlin-lambda-expressions-kotlin-anonymous-functions-example-tutorial-88a4b622f8b9)

## Arrays

# Arrays in Kotlin

Arrays in Kotlin are used to store a fixed-size, sequential collection of elements of the same data type. Think of them as a container that holds multiple values of the same kind, like a list of integers, strings, or even custom objects. You can access each element in the array using its index, which starts from zero. Arrays are fundamental for organizing and manipulating collections of data in your programs.

Visit the following resources to learn more:

- [@official@Arrays](https://kotlinlang.org/docs/arrays.html)

## Asynchronous Flow

# Asynchronous Flow

Asynchronous Flow in Kotlin is a feature built upon coroutines that allows you to represent a stream of data that is computed asynchronously. It's designed to handle sequences of values emitted over time, enabling you to perform operations on each emitted value in a non-blocking manner. This is particularly useful for handling data streams from sources like network requests, database queries, or sensor readings, where values become available at different times.

Visit the following resources to learn more:

- [@official@Asynchronous Flow](https://kotlinlang.org/docs/flow.html)
- [@article@Kotlin flows on Android](https://developer.android.com/kotlin/flow)
- [@video@Kotlin Flows in practice](https://www.youtube.com/watch?v=fSB6_KE95bU)

## Booleans

# Booleans

Booleans represent truth values: either `true` or `false`. They are fundamental for decision-making in code, allowing programs to execute different blocks of code based on whether a condition is met. In Kotlin, the `Boolean` type is used to declare variables that can hold these two values, enabling logical operations and conditional statements.

Visit the following resources to learn more:

- [@official@Booleans](https://kotlinlang.org/docs/booleans.html)

## Break  Continue

# Break and Continue in Kotlin Loops

In Kotlin, `break` and `continue` are control flow statements used within loops. The `break` statement immediately terminates the loop's execution and transfers control to the next statement after the loop. Conversely, the `continue` statement skips the rest of the current iteration of the loop and proceeds to the next iteration. They provide a way to alter the normal flow of a loop based on certain conditions.

Visit the following resources to learn more:

- [@official@Break and continue labels](https://kotlinlang.org/docs/returns.html#break-and-continue-labels)
- [@video@Break | Continue | Return - A fresh look](https://www.youtube.com/watch?v=qMyJd0ihUTg)

## Buffered Streams

# Buffered Streams

Buffered streams in Kotlin enhance the efficiency of reading from and writing to data sources. Instead of directly interacting with the underlying input or output stream for every read or write operation, buffered streams use an internal buffer. This buffer temporarily stores data, reducing the number of actual I/O operations and improving performance, especially when dealing with small, frequent read/write requests.

Visit the following resources to learn more:

- [@article@https://developer.android.com/reference/kotlin/java/io/BufferedInputStream](https://developer.android.com/reference/kotlin/java/io/BufferedInputStream)
- [@article@BufferedOutputStream](https://developer.android.com/reference/kotlin/java/io/BufferedOutputStream)
- [@video@Efficient IO With Buffered Reading & Writing In Kotlin - IO Essentials](https://www.youtube.com/watch?v=GFo5KPaY-zU)

## Build Tool Api

# Build Tool API

The Build Tool API in Kotlin provides a way for build tools like Gradle or Maven to interact with the Kotlin compiler and related tooling. It allows these tools to configure the compilation process, access compiler options, and integrate Kotlin code into the overall build lifecycle. This API enables build tools to manage dependencies, generate code, and perform other tasks necessary for building Kotlin projects. Currently, the BTA supports Kotlin/JVM only.

Visit the following resources to learn more:

- [@official@Build tools API](https://kotlinlang.org/docs/build-tools-api.html)

## Build Tools

# Build Tools

Build tools in Kotlin automate tasks like compiling code, running tests, and packaging applications. They manage dependencies, ensuring your project has all the necessary libraries. Popular choices include Gradle and Maven, which use configuration files to define the build process and handle project structure, making it easier to build and distribute Kotlin applications.

Visit the following resources to learn more:

- [@article@Understanding Kotlin Build Tools Made Simple](https://www.dhiwise.com/post/understanding-kotlin-build-tools-made-simple)

## C Interoperability

# C Interoperability in Kotlin/Native

C Interoperability in Kotlin/Native allows Kotlin code to interact with C libraries and code. This means you can use existing C libraries within your Kotlin/Native projects, and also expose Kotlin/Native code to be used from C. It involves mapping C data types and functions to their Kotlin equivalents, enabling seamless communication between the two languages.

Visit the following resources to learn more:

- [@official@Interoperability with C](https://kotlinlang.org/docs/native-c-interop.html)

## Catching Exceptions

# Catching Exceptions

Catching exceptions handle the unexpected exception manually by resolving the issue or notifying the developer or application user. When an exception is thrown, it interrupts the normal execution of the program. You can handle exceptions gracefully with the `try` and `catch` keywords to keep your program stable. The `try` block contains the code that might throw an exception, while the `catch` block catches and handles the exception if it occurs. The exception is caught by the first `catch` block that matches its specific type or a superclass of the exception.

Visit the following resources to learn more:

- [@official@Handle exceptions using try-catch blocks](https://kotlinlang.org/docs/exceptions.html#handle-exceptions-using-try-catch-blocks)

## Characters

# Characters

Characters in Kotlin represent single symbols, like letters, numbers, or punctuation marks. They are denoted by the `Char` type and are enclosed in single quotes (e.g., `'A'`, `'7'`, `'$'`).  You can use characters to store and manipulate individual text elements within your programs. Kotlin supports Unicode characters, allowing you to represent a wide range of symbols from different languages.

Visit the following resources to learn more:

- [@official@Characters](https://kotlinlang.org/docs/characters.html)

## Cicd Tools

# CI/CD Tools

CI/CD tools are software that automates building, testing, and deploying code changes in a software development workflow, enabling faster and more reliable releases of high-quality software. They are the backbone of continuous integration (CI) and continuous delivery/deployment (CD) practices, which automate the software delivery pipeline to reduce risks and deliver value to customers more quickly. TeamCity, for example, is a CI/CD server that can be used to automate these processes for Kotlin projects.

## Class Generics

# Class Generics

Generics in Kotlin allow you to define classes that can work with different types of data without specifying those types upfront. Think of it like a template for a class. Instead of writing separate classes for handling integers, strings, or other data types, you can create a single generic class that can handle any type you specify when you create an instance of the class. This makes your code more reusable and type-safe, as the compiler can check that you're using the correct types with your generic class.

Visit the following resources to learn more:

- [@official@Generics: in, out, where](https://kotlinlang.org/docs/generics.html)
- [@video@Kotlin Generics - How to create generic classes](https://www.youtube.com/watch?v=tddbTT_v1BE)

## Class Members

# Class Members in Kotlin

In Kotlin, a class member refers to the variables (properties) and functions (methods) that belong to a class. Properties hold data associated with the class, defining its state, while methods define the behavior or actions that the class can perform. These members are accessed using the dot notation on an instance of the class. They can be declared as either mutable (using `var`) or read-only (using `val`), and their visibility can be controlled using modifiers like `public`, `private`, and `protected`.

Visit the following resources to learn more:

- [@official@Class members](https://kotlinlang.org/docs/classes.html#class-members)
- [@video@Kotlin Classes & Objects Explained 🚀 | OOP in Kotlin | Kotlin Crash Course](https://www.youtube.com/watch?v=1WF2Q_UJgps)

## Code Organization

# Code Organization

In pure Kotlin projects, the recommended directory structure follows the package structure with the common root package omitted. For example, if all the code in the project is in the `org.example.kotlin` package and its subpackages, files with the `org.example.kotlin` package should be placed directly under the source root, and files in `org.example.kotlin.network.socke
t` should be in the `network/socket` subdirectory of the source root.

If a Kotlin file contains a single class or interface (potentially with related top-level declarations), its name should be the same as the name of the class, with the .kt extension appended. It applies to all types of classes and interfaces. If a file contains multiple classes, or only top-level declarations, choose a name describing what the file contains, and name the file accordingly. Use upper camel case, where the first letter of each word is capitalized. For example, ProcessDeclarations.kt

Visit the following resources to learn more:

- [@official@Source code organization](https://kotlinlang.org/docs/coding-conventions.html#source-code-organization)
- [@video@Full 2025 Kotlin Crash Course For Beginners](https://www.youtube.com/watch?v=dzUc9vrsldM)

## Collections

# Collections

Collections in Kotlin are structures that hold multiple items together. Think of them as containers for data. They can be lists of things, sets of unique items, or maps that pair keys with values. Kotlin provides built-in collection types like `List`, `Set`, and `Map`, along with functions to easily add, remove, and manipulate the data within them. These collections can be either mutable (changeable) or immutable (read-only), offering flexibility in how you manage your data.

Visit the following resources to learn more:

- [@official@Collections](https://kotlinlang.org/docs/basic-syntax.html#collections)
- [@article@Collections Overview](https://kotlinlang.org/docs/collections-overview.html)
- [@video@Kotlin Collections](https://www.youtube.com/watch?v=NuuMC4mmzzQ)

## Comments

# Comments

Comments are explanatory notes added to code to make it easier to understand. In Kotlin, you can add single-line comments using `//`. Anything after `//` on the same line is ignored by the compiler. For multi-line comments, you can use `/*` to begin the comment and `*/` to end it. Everything between `/*` and `*/` will be treated as a comment and not executed as code.

Visit the following resources to learn more:

- [@official@Comments](https://kotlinlang.org/docs/basic-syntax.html#comments)

## Competitive Programming

# Competitive Programming with Kotlin

Kotlin can be used for competitive programming due to its concise syntax, standard library, and interoperability with Java. It allows programmers to write efficient and readable code, which is crucial for solving algorithmic problems quickly. Kotlin's features like data classes, extension functions, and null safety can help reduce boilerplate and improve code quality in a competitive programming environment.

Visit the following resources to learn more:

- [@official@Kotlin for competitive programming](https://kotlinlang.org/docs/competitive-programming.html)
- [@article@Start Competitive Programming with Kotlin](https://medium.com/codex/start-competitive-programming-with-kotlin-ab704fb5bcda)

## Compose Multiplatform

# Compose Multiplatform

Compose Multiplatform is a declarative UI framework that allows developers to share user interface code across multiple platforms, including Android, iOS, desktop (Windows, macOS, Linux), and web. It's based on Jetpack Compose, Google's modern UI toolkit for Android, and leverages Kotlin's multiplatform capabilities to enable code reuse while maintaining a native look and feel on each target platform. This approach streamlines UI development by reducing platform-specific code and promoting consistency across different applications.

Visit the following resources to learn more:

- [@official@Compose Multiplatform](https://www.jetbrains.com/compose-multiplatform/)
- [@opensource@Compose Multiplatform](https://github.com/JetBrains/compose-multiplatform)
- [@video@The Compose Multiplatform Crash Course for 2025](https://www.youtube.com/watch?v=WT9-4DXUqsM)

## Conditional Expressions

# Conditional Expressions

Conditional expressions allow you to execute different blocks of code based on whether a condition is true or false. They provide a way to make decisions within your program, enabling it to respond differently to various inputs or situations. In Kotlin, this is primarily achieved using `if` and `when` expressions. These expressions evaluate a boolean condition and execute the corresponding code block.

Visit the following resources to learn more:

- [@official@If expression](https://kotlinlang.org/docs/control-flow.html#if-expression)

## Constructors

# Constructors

Constructors in Kotlin are special member functions within a class that are used to initialize objects of that class. They define how an object is created and what initial values its properties will have. Kotlin has two types of constructors: primary and secondary. The primary constructor is part of the class header, while secondary constructors are defined inside the class body using the `constructor` keyword. A class can have one primary constructor and multiple secondary constructors.

Visit the following resources to learn more:

- [@official@Constructors](https://kotlinlang.org/docs/classes.html#constructors)
- [@article@Define a constructor](https://developer.android.com/codelabs/basic-android-kotlin-compose-classes-and-objects#5)
- [@video@Kotlin Classes and Constructors - Primary vs Secondary](https://www.youtube.com/watch?v=Ly_onmXpDiw)

## Coroutines Behavior

# Coroutines Behavior

Launching a coroutine from a `CoroutineScope` creates a context that governs its execution. Builder functions like `.launch()` and `.async()` automatically create a set of elements that define how the coroutine behaves, including the `Job` interface, which tracks the coroutine's lifecycle and enables structured concurrency; `CoroutineDispatcher`, which controls where the coroutine runs; and `CoroutineExceptionHandler`, which handles uncaught exceptions.

Visit the following resources to learn more:

- [@official@Coroutine concepts](https://kotlinlang.org/docs/coroutines-basics.html)
- [@video@Coroutine Contexts - Kotlin Coroutines](https://www.youtube.com/watch?v=71NrkkRNXG4)

## Coroutines Best Practices

# Coroutines Best Practices

Coroutines in Kotlin simplify asynchronous programming, but using them effectively requires following certain best practices. These include using structured concurrency to manage coroutine lifecycles and prevent leaks, avoiding `GlobalScope` for most tasks and preferring `CoroutineScope` tied to specific components, handling exceptions properly within coroutines, and offloading long-running or blocking operations to appropriate dispatchers like `Dispatchers.IO` to avoid blocking the main thread.  Additionally, it's important to cancel coroutines when they are no longer needed to free up resources and prevent unnecessary work.

Visit the following resources to learn more:

- [@article@Coroutine: Best Practices](https://medium.com/@vivekbansal19/coroutine-best-practices-affddb50ae1b)
- [@article@Best practices for coroutines in Android](https://developer.android.com/kotlin/coroutines/coroutines-best-practices)

## Coroutines Builders

# Coroutine Builders

Coroutine builders in Kotlin are functions that start a new coroutine. They bridge the gap between regular, blocking code and the non-blocking, concurrent world of coroutines. Common builders include `launch`, which starts a coroutine without blocking the current thread and returns a `Job`, and `runBlocking`, which blocks the current thread until the coroutine completes, primarily used for testing and main functions. Another builder, `async`, starts a coroutine and returns a `Deferred` object, which represents a future result. These builders allow you to execute code concurrently and manage the lifecycle of coroutines.

Visit the following resources to learn more:

- [@official@Coroutines basics](https://kotlinlang.org/docs/coroutines-basics.html#your-first-coroutine)
- [@article@Kotlin Coroutine builders](https://medium.com/@appdevinsights/kotlin-coroutine-builders-6a6639cc478d)

## Coroutines

# Kotlin Coroutines

To support efficient concurrency, Kotlin uses asynchronous programming built around coroutines, which let you write asynchronous code in a natural, sequential style using suspending functions. Coroutines are lightweight alternatives to threads. They can suspend without blocking system resources and are resource-friendly, making them better suited for fine-grained concurrency. Most coroutine features are provided by the `kotlinx.coroutines` library, which includes tools for launching coroutines, handling concurrency, working with asynchronous streams, and more.

Visit the following resources to learn more:

- [@official@Coroutines](https://kotlinlang.org/docs/coroutines-overview.html#coroutines-overview.md)
- [@opensource@kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines)
- [@video@WHAT IS A COROUTINE? - Kotlin Coroutines](https://www.youtube.com/watch?v=ShNhJ3wMpvQ)

## Coroutines

# Coroutines

Kotlin Coroutines provide a way to write asynchronous, non-blocking code in a sequential style. They allow you to perform long-running tasks, like network requests or database operations, without blocking the main thread, thus preventing your application from becoming unresponsive. Coroutines are lightweight threads that can be suspended and resumed, making it easier to manage concurrency and improve application performance.

Visit the following resources to learn more:

- [@official@Coroutines](https://kotlinlang.org/docs/coroutines-overview.html)
- [@opensource@kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines)
- [@article@Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines)
- [@video@Kotlin Coroutine (High-quality Course)](https://www.youtube.com/watch?v=lmRzRKIsn1g)

## Creating Files

# Creating Files

In Kotlin, you can create new files using the `File` class from the `java.io` package. To do this, you first create a `File` object representing the desired file path. Then, you call the `createNewFile()` method on that `File` object. This method attempts to create a new, empty file at the specified location. It returns `true` if the file was successfully created and `false` if a file with that name already exists or if there was an error during creation.

Visit the following resources to learn more:

- [@article@Working With Files In Kotlin - IO Essentials](https://www.youtube.com/watch?v=MSeI7XVzrvo)

## Creating Instances

# Creating Instances

In Kotlin, creating an instance of a class is straightforward. You simply use the class name followed by parentheses, similar to calling a function. This invokes the class's constructor, which initializes the object. If the class has a primary constructor, you'll need to provide the required arguments within the parentheses. If there's no explicit constructor defined, Kotlin provides a default one.

Visit the following resources to learn more:

- [@official@Creating instances of classes](https://kotlinlang.org/docs/classes.html#creating-instances-of-classes)
- [@article@Create an instance of a class](https://developer.android.com/codelabs/basic-android-kotlin-compose-classes-and-objects#2)
- [@video@Kotlin Classes & Objects Explained 🚀 | OOP in Kotlin | Kotlin Crash Course](https://www.youtube.com/watch?v=1WF2Q_UJgps)

## Data Analysis

# Data Analysis with Kotlin

Data analysis involves examining raw data to draw conclusions about that information. Kotlin, primarily known for Android development, can also be used for data analysis. With Kotlin's Exploratory Data Analysis (EDA) tools, such as Kotlin notebooks, Kotlin DataFrame, and Kandy, you have at your disposal a rich set of capabilities to enhance your analytics skills and support you across different scenarios:

Visit the following resources to learn more:

- [@official@Kotlin for data analysis](https://kotlinlang.org/docs/data-analysis-overview.html)
- [@official@Kotlin and Java libraries for data analysis](https://kotlinlang.org/docs/data-analysis-libraries.html)
- [@article@A Step-by-Step Guide to Performing Data Analysis With Kotlin DataFrame](https://blog.jetbrains.com/kotlin/2024/04/a-step-by-step-guide-to-performing-data-analysis-with-kotlin-dataframe/)
- [@video@Data Analytics With Kotlin Notebooks](https://www.youtube.com/watch?v=_RYV7ZvMKpE)

## Data Classes

# Data Classes

Data classes in Kotlin are special classes designed to hold data. The compiler automatically generates useful methods like `equals()`, `hashCode()`, `toString()`, `componentN()` functions (for destructuring), and `copy()` for you. This reduces boilerplate code when you primarily need a class to store and manage data.

Visit the following resources to learn more:

- [@official@Data classess](https://kotlinlang.org/docs/data-classes.html#data-classes.md)
- [@video@Data classes - Kotlin Vocabulary](https://www.youtube.com/watch?v=PlywDf1dAnA)

## Data Types

# Data Types in Kotlin

Kotlin, like other programming languages, uses data types to classify different kinds of values. These types define what operations can be performed on the data and how much memory it occupies. In Kotlin, everything is an object in the sense that you can call member functions and properties on any variable. While certain types have an optimized internal representation as primitive values at runtime (such as numbers, characters, and booleans), they appear and behave like regular classes to you.

Visit the following resources to learn more:

- [@official@Basic Types](https://kotlinlang.org/docs/basic-types.html)
- [@article@Data types in Kotlin](https://www.w3schools.com/kotlin/kotlin_data_types.php)

## Date  Time

# Date & Time

Kotlin leverages Java's `java.time` package (introduced in Java 8) for handling dates and times, offering classes like `LocalDate`, `LocalTime`, and `LocalDateTime`.  Kotlin also provides extensions and convenience functions within its standard library, such as the kotlinx.datetime library, to work with dates and times. This allows you to easily represent, manipulate, and format date and time information in your Kotlin applications.

Visit the following resources to learn more:

- [@opensource@kotlinx.datetime](https://github.com/Kotlin/kotlinx-datetime)
- [@official@Time measurement](https://kotlinlang.org/docs/time-measurement.html)
- [@official@java.time](https://docs.oracle.com/javase/8/docs/api/java/time/package-summary.html)
- [@video@The Full Guide About the DateTime API in Kotlin](https://www.youtube.com/watch?v=gzHy6wKAJh8)

## Default Imports

# Default Imports

Default imports are a set of pre-defined classes, functions, and interfaces that are automatically available in every Kotlin file without needing explicit import statements. These imports provide access to commonly used functionalities, reducing boilerplate code and making development more convenient. They include core language features and essential utilities that are frequently used in Kotlin programs.

Visit the following resources to learn more:

- [@official@Default Imports](https://kotlinlang.org/docs/packages.html#default-imports)

## Defining Classess

# Defining Classes

In Kotlin, a class is a blueprint for creating objects (instances). You define a class using the `class` keyword, followed by the class name and curly braces. A class consists of three major parts:
* Properties. Variables that specify the attributes of the class's objects.
* Methods. Functions that contain the class's behaviors and actions.
* Constructors. A special member function that creates instances of the class throughout the program in which it's defined.

Visit the following resources to learn more:

- [@official@Classes](https://kotlinlang.org/docs/classes.html)
- [@article@Define a class](https://developer.android.com/codelabs/basic-android-kotlin-compose-classes-and-objects#1)
- [@video@Kotlin Classes & Objects Explained 🚀 | OOP in Kotlin | Kotlin Crash Course](https://www.youtube.com/watch?v=1WF2Q_UJgps)

## Documentation

# Documentation

Kotlin uses KDoc, a documentation generation tool, to create API documentation from comments in your code. These comments, similar to Javadoc, are placed above declarations (classes, functions, properties, etc.) and use a specific syntax to describe the element's purpose, parameters, return values, and other relevant information. Tools like Dokka then process these KDoc comments to generate HTML or other formats of documentation, making your code easier to understand and use by other developers.

## Dokka

# Dokka

Dokka is a documentation engine for Kotlin, similar to Javadoc for Java. It generates API documentation in various formats (like HTML, Markdown, and more) from Kotlin source code. Dokka uses KDoc comments within your code to create comprehensive and navigable documentation, making it easier for developers to understand and use your Kotlin libraries and applications.

Visit the following resources to learn more:

- [@official@Dokka](https://kotlinlang.org/docs/dokka-introduction.html)
- [@official@Get started with Dokka](https://kotlinlang.org/docs/dokka-get-started.html)
- [@article@From Code to Clarity: How Dokka Transforms Kotlin and Java Documentation](https://thekaailashsharma.medium.com/dokka-docuemntation-ed08d5e37935)

## Enum Class

# Enum Class

An enum class in Kotlin is a special type of class that represents a fixed set of possible values, often called "enumerations". Think of it like a list of named constants. Each constant in the enum class is an instance of that class. They're useful when you need to represent a limited number of choices, like days of the week, directions (North, South, East, West), or status codes (e.g., Success, Pending, Failed).

Visit the following resources to learn more:

- [@official@Enum classes](https://kotlinlang.org/docs/enum-classes.html)
- [@video@Sealed Classes VS. Enum Classes VS. Sealed Interfaces - When to Use Which?](https://www.youtube.com/watch?v=kLJRZpRhX1o)

## Exceptions

# Exceptions

Exceptions in Kotlin are a way to handle errors that occur during the execution of a program. When an error happens, an exception object is created and "thrown." This disrupts the normal flow of the program. To handle these exceptions, you can use `try`, `catch`, and `finally` blocks. The `try` block contains the code that might throw an exception. If an exception occurs, the `catch` block that matches the exception type will execute. The `finally` block contains code that will always execute, regardless of whether an exception was thrown or caught, and is often used for cleanup operations.

Visit the following resources to learn more:

- [@official@Exceptions](https://kotlinlang.org/docs/exceptions.html)
- [@video@Kotlin: Beyond the Try/Catch (Exception Handling)](https://www.youtube.com/watch?v=ThlFnnaxsuE)

## Extension Functions

# Extension Functions

Extension functions in Kotlin provide a way to add new functions to existing classes without inheriting from them or using any type of design pattern such as Decorator. This is achieved by defining a function that can be called as if it were a member of the class, even though it's defined outside of the class's original declaration. They are declared with a receiver type, which specifies the class to which the extension function is being added.

Visit the following resources to learn more:

- [@official@Extension Functions](https://kotlinlang.org/docs/extensions.html)
- [@video@5 Fun Ways to Use Extension Functions in Kotlin](https://www.youtube.com/watch?v=Q0RYVV9rZBI)

## Extension Functions

# Extension Functions

Extension functions in Kotlin provide a way to add new functions to existing classes without inheriting from them or using any type of design pattern such as Decorator. This is achieved by defining a function that can be called as if it were a member of the class, even though it's defined outside of it. Extension functions are resolved statically, meaning the function call is determined by the declared type of the receiver, not its runtime type.

Visit the following resources to learn more:

- [@official@Extension functions](https://kotlinlang.org/docs/extensions.html#extension-functions)

## Filtering

# Filtering in Kotlin Collections

Filtering in Kotlin collections involves selecting elements from a collection based on a specific condition. This process creates a new collection containing only the elements that satisfy the given predicate, leaving the original collection unchanged. Kotlin provides various built-in functions to perform filtering operations efficiently and concisely.

Visit the following resources to learn more:

- [@official@Collection Filtering](https://kotlinlang.org/docs/collection-filtering.html)
- [@video@Kotlin For Beginners - Collection Filtering](https://www.youtube.com/watch?v=ZK9_qMxpqvk)

## Floats

# Floats in Kotlin

Floats in Kotlin represent single-precision (Float) and double-precision (Double) floating-point numbers, used to store numbers with decimal points. `Float` uses 32 bits of memory, offering a smaller range and precision, while `Double` uses 64 bits, providing a larger range and higher precision. You use them when you need to represent non-integer values like measurements, scientific data, or financial values.

Visit the following resources to learn more:

- [@official@Floating-point types](https://kotlinlang.org/docs/numbers.html#floating-point-types)

## For

# Kotlin For Loop

The `for` loop in Kotlin is used to iterate over a range, collection, or any other iterable object. It executes a block of code for each element in the sequence. You can use it to go through numbers in a specific range, items in a list, or characters in a string, performing the same action on each one. The `for` loop simplifies repetitive tasks by automatically handling the iteration process.

Visit the following resources to learn more:

- [@official@For Loops](https://kotlinlang.org/docs/control-flow.html#for-loops)
- [@video@Control Flow | for loop | in, rangeTo, downTo, step, until](https://www.youtube.com/watch?v=ghOI_etcjSk)

## Function Types

# Function Types

In Kotlin, functions can be treated as data. A function type represents a specific kind of function, defined by the types of its parameters and its return type. You can assign a function to a variable, pass it as an argument to another function, or return it from a function. This allows for more flexible and dynamic code, enabling you to write higher-order functions and implement functional programming paradigms.

Visit the following resources to learn more:

- [@official@Function types](https://kotlinlang.org/docs/lambdas.html#function-types)
- [@article@Use functions as a data type](https://developer.android.com/codelabs/basic-android-kotlin-compose-function-types-and-lambda#3)
- [@article@Function types](https://kt.academy/article/fk-function-types)

## Gradle Pluggins

# Gradle Plugins in Kotlin

Gradle plugins are reusable components that extend Gradle's build capabilities. They automate tasks like compiling code, running tests, and packaging applications. In Kotlin projects, plugins are often written in Kotlin itself, allowing for type-safe build configurations and leveraging Kotlin's features for more expressive and maintainable build scripts. These plugins can be applied to a project to customize the build process and integrate with various tools and libraries.

Visit the following resources to learn more:

- [@official@Configure a Gradle project](https://kotlinlang.org/docs/gradle-configure-project.html)
- [@official@Using Plugins](https://docs.gradle.org/current/userguide/plugins.html)

## Gradle

# Gradle

Gradle is an open-source build automation tool known for its flexibility and performance. It's used to automate tasks like compiling, testing, and deploying software. Gradle uses a Domain Specific Language (DSL) based on Groovy or Kotlin to define build scripts, allowing developers to customize the build process extensively. It supports dependency management, allowing projects to easily incorporate external libraries and frameworks.

Visit the following resources to learn more:

- [@official@Gradle](https://kotlinlang.org/docs/gradle.html)
- [@official@Gradle user manual](https://docs.gradle.org/current/userguide/userguide.html)
- [@official@Get started with Gradle and Kotlin/JVM](https://kotlinlang.org/docs/get-started-with-jvm-gradle-project.html)
- [@video@The Ultimate Gradle Kotlin Beginner's Crash Course For 2025](https://www.youtube.com/watch?v=RCRQlz78wCg)

## Grouping

# Grouping

Grouping in Kotlin involves organizing elements from a collection into subgroups based on a specific criterion. This operation creates a map where the keys represent the grouping criteria, and the values are lists of elements that satisfy that criteria. It's a way to categorize and structure data within a collection for easier analysis or processing.

Visit the following resources to learn more:

- [@official@Grouping](https://kotlinlang.org/docs/collection-grouping.html)
- [@article@A Comprehensive Guide to Kotlin GroupBy: Mastering Grouping Operations](https://www.dhiwise.com/post/comprehensive-guide-to-kotlin-groupby-mastering-grouping)
- [@video@Collections Grouping | groupBy | groupingBy](https://www.youtube.com/watch?v=iYb_Yu8D4HQ)

## Higher Order Functions

# Higher-Order Functions

Higher-order functions in Kotlin are functions that can take other functions as arguments, return functions, or both. This means you can pass a function into another function, treat functions like any other data type (like integers or strings), and even create functions that generate and return new functions. This allows for more flexible and reusable code by abstracting behavior and logic.

Visit the following resources to learn more:

- [@official@Higher-order functions](https://kotlinlang.org/docs/lambdas.html#higher-order-functions)
- [@article@Higher-order functions with collections](https://developer.android.com/codelabs/basic-android-kotlin-compose-higher-order-functions#0)
- [@article@Higher-Order Functions in Kotlin](https://medium.com/@anandgaur2207/higher-order-functions-in-kotlin-b35fc6b23f8e)

## History Of Kotlin

# History of Kotlin

Kotlin is a modern, statically typed programming language developed by JetBrains. It was initially conceived as a new language for the JVM, aiming to address some of the shortcomings of Java while maintaining full interoperability. The project started in 2010 and was open source from very early on. The first official 1.0 release was in February 2016. The language's design emphasizes conciseness, safety, and versatility, making it suitable for a wide range of applications, including Android development, server-side applications, and more.

Visit the following resources to learn more:

- [@official@10 Years of Kotlin](https://kotlinlang.org/lp/10yearsofkotlin/past/)
- [@article@Kotlin | Wikipedia](https://en.wikipedia.org/wiki/Kotlin_(programming_language))

## Ides

# IDEs

Integrated Development Environments (IDEs) provide developers with tools to write, test, and debug code more efficiently. Popular IDEs for Kotlin development include IntelliJ IDEA, which is developed by JetBrains (the creators of Kotlin) and offers excellent support for the language, including code completion, refactoring, and debugging. Android Studio, also based on IntelliJ IDEA, is the official IDE for Android development and provides specific tools for building Kotlin-based Android applications. Eclipse with the Kotlin plugin is another option, offering a familiar environment for developers already using Eclipse.

Visit the following resources to learn more:

- [@official@IDEs for Kotlin development](https://kotlinlang.org/docs/kotlin-ide.html)
- [@article@What is an IDE (Integrated Development Environment)?](https://.amazon.com/what-is/ide/)

## If

# if

To use `if` in Kotlin, add the condition to check within parentheses `()` and the action to take if the result is true within curly braces `{}`. You can use `else` and `else if` for additional branches and checks.

Also, you can also write `if` as an expression, which lets you assign its returned value directly to a variable. In this form, an `else` branch is required. The `if` expression serves the same purpose as the ternary operator (`condition ? then : else`) found in other languages.

Visit the following resources to learn more:

- [@official@https://kotlinlang.org/docs/control-flow.html#if-expression](https://developer.android.com/codelabs/basic-android-kotlin-compose-conditionals#1)
- [@article@Use if/else statements to express conditions](https://developer.android.com/codelabs/basic-android-kotlin-compose-conditionals#1)
- [@article@Use if/else and when as expressions](https://developer.android.com/codelabs/basic-android-kotlin-compose-conditionals#3)
- [@video@Control Flows | if else | when - the cooler switch](https://www.youtube.com/watch?v=Wp2UU4yKjqM)

## Importing Packages

# Importing Packages

Packages in Kotlin are namespaces that provide a way to organize and manage code, preventing naming conflicts and improving code reusability. Importing packages allows you to access classes, functions, and other declarations defined within those packages directly, without needing to specify the fully qualified name every time you use them. This simplifies your code and makes it more readable.

Visit the following resources to learn more:

- [@official@Imports](https://kotlinlang.org/docs/packages.html#imports)
- [@video@Exploring Kotlin -Package](https://arunpandianm.medium.com/5-exploring-kotlin-package-2cb8c3e4438a)

## Inheritance

# Inheritance in Kotlin

Inheritance in Kotlin allows you to create new classes (child classes or subclasses) based on existing classes (parent classes or superclasses). The child class inherits properties and functions from the parent class, and can also add its own unique properties and functions or override the parent's behavior. This promotes code reuse and establishes a hierarchical relationship between classes, making your code more organized and maintainable.

Visit the following resources to learn more:

- [@official@Inheritance](https://kotlinlang.org/docs/inheritance.html)
- [@article@Implement a relationship between classes](https://developer.android.com/codelabs/basic-android-kotlin-compose-classes-and-objects#6)
- [@video@Kotlin Newbie to Pro - INHERITANCE](https://www.youtube.com/watch?v=Xk3IPNHbLVk)

## Inline Class

# Inline Class

An inline class in Kotlin is a special type of class that holds only one property. At runtime, instances of inline classes are represented as the underlying value, avoiding the overhead of object allocation. This allows you to create type-safe wrappers around primitive types or other values without incurring the performance cost of creating a new object.

Visit the following resources to learn more:

- [@official@Inline value classes](https://kotlinlang.org/docs/inline-classes.html#inline-classes.md)
- [@video@Inline functions - Kotlin Vocabulary](https://www.youtube.com/watch?v=wAQCs8-a6mg&list=PLWz5rJ2EKKc_T0fSZc9obnmnWcjvmJdw_)

## Integers

# Integers in Kotlin

Integers in Kotlin are whole numbers without any fractional or decimal parts. Kotlin provides several integer types, each differing in the range of values they can represent. These types include `Byte`, `Short`, `Int`, and `Long`. The choice of which type to use depends on the size of the number you need to store; using a smaller type can save memory if the range of possible values is limited. `Int` is the most commonly used integer type, offering a good balance between size and range for most general-purpose calculations.

Visit the following resources to learn more:

- [@article@Integer types](https://kotlinlang.org/docs/numbers.html#integer-types)

## Intellij Idea

# IntelliJ IDEA

IntelliJ IDEA is a popular Integrated Development Environment (IDE) specifically designed for software development. It provides a comprehensive suite of tools for coding, debugging, testing, and deploying applications. It offers features like code completion, refactoring, and integration with version control systems, making it a powerful tool for developers to streamline their workflow and improve productivity.

Visit the following resources to learn more:

- [@official@IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [@opensource@IntelliJ IDEA](https://github.com/JetBrains/intellij-community)
- [@video@IntelliJ IDEA Tutorial](https://www.youtube.com/watch?v=XCqVCq249Iw)

## Interfaces

# Interfaces

Interfaces in Kotlin are blueprints for classes, defining a set of properties and abstract methods that implementing classes must provide. They allow you to define a contract, ensuring that any class implementing the interface will have specific functionalities. Unlike classes, interfaces cannot store state; they only declare what a class *should* do, not *how* it should do it. A class can implement multiple interfaces, enabling a form of multiple inheritance of behavior.

Visit the following resources to learn more:

- [@official@Interfaces](https://kotlinlang.org/docs/interfaces.html#interfaces.md)
- [@video@What are Kotlin Interfaces Used For and Why?](https://www.youtube.com/watch?v=x_VBFdit6Iw)

## Introduction To Kotlin

# Introduction to Kotlin

Kotlin is an open-source statically typed programming language that targets the JVM, Android, JavaScript, Wasm, and Native. Kotlin is an open-source, statically-typed programming language that supports both object-oriented and functional programming. It's designed to be concise, safe, and interoperable with Java, making it easy to adopt for existing Java projects. Kotlin can be used for any kind of development, be it server-side, client-side web, Android, or multiplatform library. With Kotlin/Native currently in the works, support for other platforms such as embedded systems, macOS, and iOS. People are using Kotlin for mobile and server-side applications, client-side with JavaScript or JavaFX, and data science, just to name a few possibilities.

Visit the following resources to learn more:

- [@official@Kotlin Docs](https://kotlinlang.org/docs/home.html)
- [@article@Kotlin overview](https://developer.android.com/kotlin/overview)
- [@official@Teach Computer Science with Kotlin](https://kotlinlang.org/education/)
- [@course@Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course)
- [@video@Full 2025 Kotlin Crash Course For Beginners](https://www.youtube.com/watch?v=dzUc9vrsldM)

## Io Library

# I/O Library

Kotlin leverages both its own `kotlin.io` package and the standard Java `java.io` package for input and output operations. `kotlin.io` provides a set of extension functions and utilities that simplify common I/O tasks, offering a more Kotlin-idiomatic way to interact with files, streams, and the console. While `kotlin.io` offers convenient abstractions, `java.io` remains fully accessible and usable within Kotlin code, providing a broader range of classes and functionalities for more complex I/O scenarios.

Visit the following resources to learn more:

- [@official@kotlin.io](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/)
- [@opensource@kotlinx.io](https://github.com/Kotlin/kotlinx-io)
- [@official@java.io](https://docs.oracle.com/javase/tutorial/essential/io/)
- [@video@Working With Files In Kotlin - IO Essentials](https://www.youtube.com/watch?v=MSeI7XVzrvo)

## Io

# I/O in Kotlin

Input/Output (I/O) in Kotlin refers to how a program interacts with the outside world. This involves reading data from sources like files, the keyboard, or network connections, and writing data to destinations such as files, the console, or network sockets. Kotlin leverages Java's extensive I/O libraries, providing classes and functions for handling various input and output operations. These operations allow programs to receive data, process it, and then present or store the results.

Visit the following resources to learn more:

- [@official@kotlin.io](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/)
- [@video@Working With Files In Kotlin - IO Essentials](https://www.youtube.com/watch?v=MSeI7XVzrvo)

## Iterators

# Iterators

Iterators are objects that allow you to traverse through the elements of a collection (like a list or a set) one by one. They provide a way to access each item in the collection sequentially without needing to know the underlying structure of the collection. You can use iterators to read the elements, and in some cases, to remove elements from the collection as you iterate.

Visit the following resources to learn more:

- [@official@Iterators](https://kotlinlang.org/docs/iterators.html)
- [@official@Iterator](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-iterator/)
- [@article@Mastering Kotlin Iterators: A Complete Guide For Developers](https://www.dhiwise.com/post/mastering-kotlin-iterators-a-complete-guide-for-developers)
- [@video@Iterating Collections | for | forEach | Iterator](https://www.youtube.com/watch?v=MXRNAw6Uem0)

## Java From Kotlin

# Java Interoperability from Kotlin

Kotlin is designed to be fully interoperable with Java, meaning you can seamlessly use existing Java code within your Kotlin projects. This allows you to leverage existing Java libraries, frameworks, and codebases without needing to rewrite them in Kotlin. You can call Java code directly from Kotlin, accessing classes, methods, and fields as if they were written in Kotlin.

Visit the following resources to learn more:

- [@official@Calling Java from Kotlin](https://kotlinlang.org/docs/java-interop.html)

## Java Interoperability

# Java Interoperability

Kotlin is 100% interoperable with the Java programming language, and major emphasis has been placed on making sure that your existing codebase can interact properly with Kotlin. You can easily call Kotlin code from Java and Java code from Kotlin. This makes adoption much easier and lower-risk. There's also an automated Java-to-Kotlin converter built into the IDE that simplifies migration of existing code.

Visit the following resources to learn more:

- [@official@Kotlin Comparison to Java](https://kotlinlang.org/docs/comparison-to-java.html)
- [@official@Calling Java from Kotlin](https://kotlinlang.org/docs/java-interop.html)
- [@official@Calling Kotlin from Java](https://kotlinlang.org/docs/java-to-kotlin-interop.html)

## Jvm Metadata

# JVM Metadata

The `kotlin-metadata-jvm` library provides tools to read, modify, and generate metadata from Kotlin classes compiled for the JVM. This metadata, stored in the `@Metadata` annotation within `.class` files, is used by libraries and tools such as `kotlin-reflect` to inspect Kotlin-specific constructs such as properties, functions, and classes at runtime.

Visit the following resources to learn more:

- [@official@Kotlin Metadata JVM library](https://kotlinlang.org/docs/metadata-jvm.html)
- [@official@kotlin-metadata-jvm](https://kotlinlang.org/api/kotlinx-metadata-jvm/)

## Kandy

# Kotlin Kandy

Kandy is a Kotlin library designed for creating visualizations and performing data analysis. It provides a concise and expressive API for generating plots and charts directly from Kotlin code. Kandy simplifies the process of exploring and presenting data insights, allowing developers to create visually appealing and informative graphics without needing extensive knowledge of specialized plotting tools.

Visit the following resources to learn more:

- [@official@Kandy Overview](https://kotlin.github.io/kandy/overview.html)
- [@opensource@Kandy](https://github.com/Kotlin/kandy)
- [@video@Kotlin for Data Analysis: Exploring Dataframes and Visualizations in Notebooks](https://www.youtube.com/watch?v=PIxGmHjTdu8)

## Kdoc

# KDoc

KDoc is Kotlin's documentation generation tool, similar to Javadoc for Java. It allows developers to embed documentation directly within their code, using a specific syntax to describe classes, functions, properties, and other elements. This documentation can then be extracted and formatted into a readable, navigable website or other documentation formats, providing a clear and accessible reference for users of the code.

Visit the following resources to learn more:

- [@official@Document Kotlin code: KDoc](https://kotlinlang.org/docs/kotlin-doc.html)
- [@article@KDoc for Kotlin Documentation — Clean Code Comments](https://nameisjayant.medium.com/kdoc-for-kotlin-documentation-clean-code-comments-bfcec73ad237)

## Koog

# Koog

Koog is a Kotlin library designed to simplify the development of AI applications. It provides tools and abstractions for tasks such as neural network creation, training, and inference. Koog aims to make AI development more accessible and efficient within the Kotlin ecosystem by offering a high-level API and leveraging Kotlin's features for concise and expressive code.

Visit the following resources to learn more:

- [@official@Koog Overview](https://docs.koog.ai/)
- [@opensource@Koog](https://github.com/JetBrains/koog)
- [@video@Kickstarting AI Agent Development in Kotlin With Koog](https://www.youtube.com/watch?v=vysVNg4IuUo)
- [@video@Building AI Agents in Kotlin with Koog | Vadim Briliantov](https://www.youtube.com/watch?v=O8WQCrdza8E)

## Kotlin Dataframe

# Kotlin DataFrame

Kotlin DataFrame is a library designed for in-memory data manipulation and analysis. It provides a tabular data structure, similar to data frames in R or Python's Pandas, allowing you to organize data into columns of different types. This library offers functionalities for filtering, transforming, aggregating, and joining data, making it easier to perform complex data analysis tasks directly within Kotlin applications.

Visit the following resources to learn more:

- [@official@Kotlin DataFrame](https://kotlin.github.io/dataframe/home.html)
- [@opensource@DataFrame](https://github.com/Kotlin/dataframe)
- [@video@Kotlin DataFrame Overview | Data Science with Kotlin](https://www.youtube.com/watch?v=qGou8F2asNw)

## Kotlin From Java

# Kotlin from Java

Kotlin from Java refers to the process of using Kotlin code within existing Java projects. It allows developers to gradually introduce Kotlin into their codebase without requiring a complete rewrite. This interoperability enables leveraging the benefits of Kotlin, such as its concise syntax and null safety features, while still maintaining compatibility with existing Java libraries and frameworks.

Visit the following resources to learn more:

- [@official@Calling Kotlin from Java](https://kotlinlang.org/docs/java-to-kotlin-interop.html)

## Kotlin Libraries

# Kotlin Libraries

Kotlin benefits from a rich ecosystem of libraries, both those specifically designed for Kotlin and those written in Java. This interoperability allows Kotlin developers to seamlessly use existing Java libraries. Additionally, Kotlin offers its own set of libraries, often referred to as KLibs, which provide functionalities ranging from standard data structures and algorithms to more specialized tools for tasks like serialization, coroutines, and testing.

Visit the following resources to learn more:

- [@official@Kotlin libraries](https://kotlinlang.org/docs/kotlin-tour-intermediate-libraries-and-apis.html#kotlin-libraries)
- [@official@Klibs](https://klibs.io/)
- [@official@Calling Java from Kotlin](https://kotlinlang.org/docs/java-interop.html#how-to-enable-java-synthetic-property-references)

## Kotlin Multiplatform

# Kotlin Multiplatform

Kotlin Multiplatform (KMP) is a feature of the Kotlin programming language that allows developers to write code that can be shared across multiple platforms, such as Android, iOS, JVM, JavaScript, and Native. This means you can write common business logic, data models, and algorithms once in Kotlin and then reuse them in different applications targeting different operating systems and environments, reducing code duplication and development time.

Visit the following resources to learn more:

- [@official@Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform.html)
- [@article@Kotlin Multiplatform Overview](https://developer.android.com/kotlin/multiplatform)
- [@video@What Is Kotlin Multiplatform And How Does It Work?](https://www.youtube.com/watch?v=RSBO1C_Du2U)

## Kotlin Notebooks

# Kotlin Notebooks

Kotlin Notebooks provide an interactive environment for writing and executing Kotlin code, often within a web browser. They allow you to combine code, text, and visualizations in a single document, making them ideal for exploring data, prototyping ideas, and creating shareable reports. This interactive approach facilitates experimentation and iterative development, allowing you to see the results of your code changes immediately.

Visit the following resources to learn more:

- [@official@Kotlin Notebook](https://kotlinlang.org/docs/kotlin-notebook-overview.html)
- [@official@Get started with Kotlin Notebook](https://kotlinlang.org/docs/get-started-with-kotlin-notebooks.html)
- [@video@10:00 YouTube · Kotlin by JetBrains Kotlin Notebook: Visual, Interactive, Fun](https://www.youtube.com/watch?v=m4Cqz2_P9rI)

## Kotlin Scripting

# Kotlin Scripting

Kotlin Scripting allows you to use Kotlin as a scripting language. This means you can write Kotlin code that can be executed directly, without the need for a full-fledged application setup. It's useful for automating tasks, creating build scripts, or embedding custom logic into applications.

Visit the following resources to learn more:

- [@official@Get started with Kotlin custom scripting – tutorial](https://kotlinlang.org/docs/custom-script-deps-tutorial.html)
- [@article@State of Kotlin Scripting 2024](https://blog.jetbrains.com/kotlin/2024/11/state-of-kotlin-scripting-2024/)

## Kotline Notebook

# Kotlin Notebook

Kotlin Notebook is an interactive environment for writing and executing Kotlin code, similar to Jupyter Notebook for Python. It allows you to combine code, text, and visualizations in a single document, making it ideal for data exploration, prototyping, and creating interactive tutorials. You can execute code snippets (cells) individually and see the results immediately, facilitating experimentation and rapid development.

Visit the following resources to learn more:

- [@official@Kotline Notebook](https://kotlinlang.org/docs/kotlin-notebook-overview.html)
- [@official@Create your first Kotlin Notebook](https://kotlinlang.org/docs/kotlin-notebook-create.html)
- [@video@Kotlin Notebook: Visual, Interactive, Fun | Kotlin Notebook Tutorial](https://www.youtube.com/watch?v=m4Cqz2_P9rI)

## Kotlinjava

# Kotlin/Java

Kotlin/Java allows Kotlin code to seamlessly interact with Java code and libraries. This interoperability means you can use existing Java code in your Kotlin projects and vice versa. It leverages the Java Virtual Machine (JVM) to run both Kotlin and Java code, enabling developers to gradually migrate Java projects to Kotlin or use Kotlin for new features in existing Java applications.

Visit the following resources to learn more:

- [@official@Get started with Kotlin/JVM](https://kotlinlang.org/docs/jvm-get-started.html)
- [@official@Mixing Java and Kotlin in one project – tutorial](https://kotlinlang.org/docs/mixing-java-kotlin-intellij.html)
- [@video@Kotlin For Java Developers Complete Course](https://www.youtube.com/watch?v=dMyRywABp_c)

## Kotlinjavascript

# Kotlin/JavaScript

Kotlin/JavaScript (Kotlin/JS) allows you to compile Kotlin code into JavaScript. This enables you to use Kotlin to develop web applications, Node.js applications, and other JavaScript-based projects. The resulting JavaScript code can then be executed in any environment that supports JavaScript, such as web browsers or Node.js runtimes. Kotlin/JavaScript can also be used through the Kotlin Multiplatform Gradle plugin

Visit the following resources to learn more:

- [@official@Kotlin/JavaScript](https://kotlinlang.org/docs/js-overview.html)
- [@video@Let's Learn Kotlin/JS! (with Sebastian Aigner)](https://www.youtube.com/watch?v=_kM9Y6C0iRI)

## Kotlinnative

# Kotlin/Native

Kotlin/Native is a technology for compiling Kotlin code to native binaries, which can run without a virtual machine. This allows Kotlin to be used for developing applications for platforms where a JVM is not suitable or available, such as embedded systems, iOS, macOS, Windows, Linux, and WebAssembly. It achieves this by using the LLVM compiler infrastructure to translate Kotlin code into machine code.

Visit the following resources to learn more:

- [@official@Kotlin/Native](https://kotlinlang.org/docs/native-overview.html)
- [@official@Get started with Kotlin/Native](https://kotlinlang.org/docs/native-get-started.html)

## Kotlinwasm

# Kotlin/WASM

Kotlin/WASM allows you to compile Kotlin code to WebAssembly (WASM), a binary instruction format designed for efficient execution in web browsers and other environments. This enables Kotlin developers to build high-performance applications that can run directly in the browser, leveraging Kotlin's features and tooling for web development. It provides an alternative to JavaScript for client-side web development, and also opens up possibilities for using Kotlin in other WASM-compatible environments.

Visit the following resources to learn more:

- [@official@Kotlin/Wasm](https://kotlinlang.org/docs/wasm-overview.html)
- [@official@Get started with Kotlin/Wasm and Compose Multiplatform](https://kotlinlang.org/docs/wasm-get-started.html)
- [@video@Kotlin and WebAssembly: Unleashing Cross-Platform Power](https://www.youtube.com/watch?v=t3FUWfJWrjU)

## Ktor

# Ktor

Ktor is a framework for building asynchronous server-side applications, client applications, and more, in connected systems. It's built using Kotlin and coroutines, providing a simple and efficient way to handle concurrency and build scalable network applications. Ktor allows developers to create web applications, HTTP APIs, microservices, and other networked applications with ease.

Visit the following resources to learn more:

- [@official@ktor Docs](https://ktor.io/docs/welcome.html)
- [@opensource@ktor](https://github.com/ktorio/ktor)
- [@video@Managing Complexity With Ktor | Garth Gilmour](https://www.youtube.com/watch?v=RiNRQNLcpj8)
- [@video@Ktor Server Fundamentals](https://www.youtube.com/playlist?list=PL3_Xm4wcQKw1DCU1lPSVhuCMYHg-pLVKI)

## Label Loops

# Label Loops

Label loops in Kotlin allow you to control which loop is exited or continued when using `break` or `continue` statements within nested loops. By assigning a label (an identifier followed by `@`) to a loop, you can specify which loop the `break` or `continue` statement should affect. This is particularly useful when you want to exit or continue an outer loop from within an inner loop, providing more precise control over the flow of execution.

Visit the following resources to learn more:

- [@official@Returns and jumps](https://kotlinlang.org/docs/returns.html)

## Lambda Functions

# Lambda Functions

Lambda functions in Kotlin are essentially nameless functions that you can treat like values. Think of them as mini-functions you can pass around, store in variables, or execute directly. They're defined using curly braces `{}` and can take parameters and return a value.  They're particularly useful for short, concise operations, especially when working with collections or higher-order functions (functions that take other functions as arguments).

Visit the following resources to learn more:

- [@official@Lambda expressions and anonymous functions](https://kotlinlang.org/docs/lambdas.html#lambda-expressions-and-anonymous-functions)
- [@article@Kotlin Lambda Functions](https://medium.com/@guruprasadhegde4/kotlin-lambda-expressions-bb9d4e15b6fc)
- [@video@How to Use Simple Lambda Expressions in Kotlin](https://www.youtube.com/watch?v=unCjOegBSMI)
- [@video@Introduction to Lambdas](https://www.youtube.com/watch?v=S6oJgF_J9m4)

## Lists

# Lists in Kotlin

Lists in Kotlin are ordered collections of items. They can contain elements of the same type, and you can access these elements by their index (position) in the list. Kotlin provides both mutable (changeable) and immutable (read-only) lists, allowing you to choose the appropriate type based on whether you need to modify the list after its creation.

Visit the following resources to learn more:

- [@official@Lists](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/)
- [@article@Lists | Android](https://developer.android.com/codelabs/basic-android-kotlin-collections#2)

## Lists

# List Operations in Kotlin

Kotlin lists offer several operations beyond the general collection operations. These include accessing elements by index (using `get()` or the `[]` operator), adding or removing elements at specific positions (using `add()` or `removeAt()`), and finding the index of a particular element (using `indexOf()` or `lastIndexOf()`). Lists also support operations for sublisting (using `subList()`) and replacing elements at a given index (using `set()`). These operations are available for both mutable and immutable lists, with mutable lists allowing modifications to the list's content.

Visit the following resources to learn more:

- [@official@List-specific operations](https://kotlinlang.org/docs/list-operations.html#retrieve-list-parts)
- [@article@How To Use List In Kotlin](https://medium.com/@ajay_00/how-to-use-list-in-kotlin-ca9544df54c4)

## Local Functions

# Local Functions

Local functions in Kotlin are functions defined inside another function. They provide a way to organize and reuse code within a specific function's scope. This means a local function can only be called from within the function it's defined in, and it has access to the outer function's variables. They are useful for breaking down complex functions into smaller, more manageable parts, improving readability and maintainability.

Visit the following resources to learn more:

- [@official@Function scope](https://kotlinlang.org/docs/functions.html#function-scope)

## Loops

# Loops in Kotlin

Loops in Kotlin are used to execute a block of code repeatedly. They provide a way to automate repetitive tasks. Kotlin offers several types of loops, including `for` loops (for iterating over collections or ranges) and `while` loops (for executing a block as long as a condition is true), and `do-while` loops (similar to `while` and `do-while` loops. These loops help in efficiently processing data and controlling the flow of execution in your programs.

Visit the following resources to learn more:

- [@official@For Loops](https://kotlinlang.org/docs/control-flow.html#for-loops)
- [@official@While Loops](https://kotlinlang.org/docs/control-flow.html#while-loops)
- [@article@Kotlin Loops](https://www.codecademy.com/resources/docs/kotlin/loops)
- [@video@How to Improve Loops in Kotlin](https://www.youtube.com/watch?v=i-kyPp1qFBA)

## Main  Function

# Main Function

The `main` function serves as the entry point for a Kotlin program. When you execute a Kotlin application, the code within the `main` function is the first to be run. It's where the program's execution begins, and it typically orchestrates the overall flow and logic of the application.

Visit the following resources to learn more:

- [@official@Program Entry point](https://kotlinlang.org/docs/basic-syntax.html#program-entry-point)
- [@article@Kotlin Syntax](https://www.w3schools.com/kotlin/kotlin_syntax.php)

## Maps

# Maps in Kotlin

Maps are data structures that store collections of key-value pairs, where each key is unique. They allow you to efficiently retrieve a value based on its associated key. Think of them like dictionaries where you look up a word (the key) to find its definition (the value). Kotlin provides built-in support for maps, offering both mutable and immutable versions.

Visit the following resources to learn more:

- [@official@Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/)
- [@article@Map Collection | Android](https://developer.android.com/codelabs/basic-android-kotlin-collections#4)

## Maps

# Maps

Maps in Kotlin are collections that hold key-value pairs. Map-specific operations allow you to interact with these pairs in targeted ways. These operations include retrieving values based on their keys, adding new key-value pairs, removing pairs, checking if a key or value exists, and iterating through the map's entries, keys, or values. These operations provide efficient ways to manage and manipulate data stored in a map structure.

Visit the following resources to learn more:

- [@official@Map-specific operations](https://kotlinlang.org/docs/map-operations.html)
- [@video@Map Explained - Kotlin Collections](https://www.youtube.com/watch?v=ff8uuCHtiZ8)

## Maven

# Maven

Maven is a powerful build automation tool primarily used for Java projects, but it also works seamlessly with Kotlin. It simplifies dependency management by allowing you to declare external libraries your project needs, and Maven automatically downloads and includes them. Maven uses a Project Object Model (POM) file, typically named `pom.xml`, to describe the project's configuration, dependencies, and build process, making project builds consistent and reproducible across different environments.

Visit the following resources to learn more:

- [@official@Maven](https://kotlinlang.org/docs/maven.html)
- [@official@Apache Maven](https://maven.apache.org/)
- [@video@How to Add Kotlin to a Java Project with Maven](https://www.youtube.com/watch?v=4-qOxvjjF8g)

## Member Functions

# Member Functions

Member functions, also known as methods, are functions that are defined inside a class. They operate on the data of that class and can access its properties. You can think of them as actions that an object of that class can perform. They are declared using the `fun` keyword within the class body, just like regular functions, but they are associated with a specific class. Member functions are called with dot notation:
`
Sample().foo() // creates instance of class Sample and calls foo
`

Visit the following resources to learn more:

- [@official@Member functions](https://kotlinlang.org/docs/functions.html#member-functions)

## Methods

# Methods in Kotlin Classes

Methods in Kotlin classes are functions defined within the class that operate on the class's data (properties). They define the behavior of objects created from the class. Methods can perform actions, manipulate data, and return values. They are accessed using the dot notation on an object instance of the class.

Visit the following resources to learn more:

- [@official@Member functions](https://kotlinlang.org/docs/functions.html#member-functions)
- [@article@Define class methods](https://developer.android.com/codelabs/basic-android-kotlin-compose-classes-and-objects#3)

## Nested  Inner Classes

# Nested & Inner Classes

Kotlin allows you to define classes inside other classes. A nested class is declared inside another class but doesn't have access to the outer class's instance. An inner class, on the other hand, is declared with the `inner` keyword and *does* have access to the outer class's instance members. This provides a way to logically group classes and control access to data.

Visit the following resources to learn more:

- [@official@Nested and inner classes](https://kotlinlang.org/docs/nested-classes.html)
- [@article@Understanding Nested and Inner Classes in Kotlin](https://medium.com/@sandeepkella23/understanding-nested-and-inner-classes-in-kotlin-ae1c4d699053)
- [@video@Kotlin Nested Classes](https://www.youtube.com/watch?v=duTShX-EL5w)
- [@video@Kotlin Inner Classes](https://www.youtube.com/watch?v=L3pAmeYjrp8)

## Nullability Check Operators

# Nullability Check Operators

Nullability check operators in Kotlin are tools that allow you to safely handle variables that might contain null values. They provide a concise way to access properties or call methods on nullable variables, preventing `NullPointerException` errors at runtime. These operators include the safe call operator (`?.`), the Elvis operator (`?:`), and the not-null assertion operator (`!!`). They enable developers to write more robust and readable code when dealing with potentially null data.

Visit the following resources to learn more:

- [@official@Null safety](https://kotlinlang.org/docs/null-safety.html)
- [@video@Kotlin NULL Safe Operators | Best Explanation Ever | Elvis Operator and Non Null Assertion Operators](https://www.youtube.com/watch?v=fxQbpy-s3Bw)

## Nullable Vs Non Nullable

# Nullable vs. Non-nullable Types

In Kotlin, the type system distinguishes between variables that can hold null values (nullable types) and those that cannot (non-nullable types). By default, variables are declared as non-nullable, meaning they must always contain a value. To allow a variable to hold a null value, you must explicitly declare it as nullable by adding a question mark (?) after the type. This distinction helps prevent NullPointerExceptions, a common source of errors in many programming languages.

Visit the following resources to learn more:

- [@official@Nullable types and non-nullable types](https://kotlinlang.org/docs/null-safety.html#nullable-types-and-non-nullable-types)
- [@article@Use nullable variables](https://developer.android.com/codelabs/basic-android-kotlin-compose-nullability#1)
- [@video@Nullable & Non Nullable Types - Kotlin Programming](https://www.youtube.com/watch?v=0qWPmaOt3VU)

## Object Declarations

# Object Declarations

Object declarations in Kotlin provide a way to define a singleton object. This means you create a class and simultaneously declare a single instance of it. The object is initialized lazily when it's accessed for the first time. You can define properties, functions, and even inherit from classes and interfaces within an object declaration. They are useful for creating utility classes or managing shared resources where only one instance is needed.

Visit the following resources to learn more:

- [@official@Object declarations and expressions](https://kotlinlang.org/docs/object-declarations.html#object-declarations.md)
- [@article@Kotlin Object Declarations and Expressions](https://www.programiz.com/kotlin-programming/object-singleton)

## Opt In Requirements

# Opt-in Requirements

Opt-in requirements in Kotlin provide a mechanism to enforce that certain APIs or code constructs are used only when the developer explicitly acknowledges and understands the associated risks or special conditions. This is achieved by marking APIs with annotations that require explicit opt-in, forcing users to acknowledge the usage by adding an `@OptIn` annotation or compiler argument. This helps prevent accidental misuse of potentially unstable, experimental, or otherwise restricted features.

Visit the following resources to learn more:

- [@official@Opt in to APIs](https://kotlinlang.org/docs/kotlin-tour-intermediate-libraries-and-apis.html#opt-in-to-apis)

## Ordering

# Ordering in Kotlin Collections

Ordering in Kotlin collections involves arranging the elements within a collection (like lists or sets) based on a specific criterion. This can be done in ascending or descending order, either using the natural ordering of the elements themselves (if they are comparable) or by providing a custom comparison function that defines how the elements should be compared. Kotlin provides a rich set of functions to sort and order collections in various ways, making it easy to manipulate data based on specific requirements.

Visit the following resources to learn more:

- [@official@Ordering](https://kotlinlang.org/docs/collection-ordering.html)
- [@video@Collection Operations Finale | Ordering | sorted | sortedDescenting](https://www.youtube.com/watch?v=EDxJvHMtSJU)

## Parameters

# Function Parameters

Function parameters are values that you pass into a function when you call it. These parameters act as inputs, allowing the function to operate on different data each time it's invoked. In Kotlin, function parameters are defined using Pascal notation - name: type. Parameters are separated using commas, and each parameter must be explicitly typed:
`
fun powerOf(number: Int, exponent: Int): Int { /*...*/ }
`

Visit the following resources to learn more:

- [@official@Parameters](https://kotlinlang.org/docs/functions.html#parameters)

## Plus  Minus Operators

# Plus & Minus Operators in Kotlin Collections

The `plus` and `minus` operators in Kotlin collections provide a concise way to create new collections by adding or removing elements from existing ones. The `plus` operator (+) combines two collections or adds a single element to a collection, returning a new collection containing all elements. Conversely, the `minus` operator (-) removes elements from a collection, either by specifying individual elements or another collection of elements to remove, also returning a new collection.

Visit the following resources to learn more:

- [@official@plus & minus Operators](https://kotlinlang.org/docs/collection-plus-minus.html)
- [@video@Kotlin Collections | Operations | filter | plus/minus](https://www.youtube.com/watch?v=59DUAaZnU54)

## Print  Println

# Printing Data in Kotlin: `print` and `println`

In Kotlin, `print` and `println` are fundamental functions used to display output to the console. The `print` function displays its argument without adding a newline character at the end, meaning subsequent output will appear on the same line. Conversely, the `println` function displays its argument and then adds a newline character, ensuring that the next output appears on a new line.

Visit the following resources to learn more:

- [@official@Print to the standard output](https://kotlinlang.org/docs/basic-syntax.html#print-to-the-standard-output)

## Printing Data

# Printing Data in Kotlin

In Kotlin, you can display information to the console using the `println()` and `print()` functions. `println()` prints the given argument to the standard output and adds a newline character at the end, moving the cursor to the next line. `print()`, on the other hand, prints the argument without adding a newline, so subsequent output will appear on the same line. You can pass variables, strings, or any other expression as arguments to these functions to display their values.

Visit the following resources to learn more:

- [@official@Print to the standard output](https://kotlinlang.org/docs/basic-syntax.html#print-to-the-standard-output)

## Progressions

# Progressions

Progressions in Kotlin define a sequence of values within a specific range, typically with a defined step. They are most commonly used with numeric types like `Int`, `Long`, and `Char`. Progressions allow you to iterate over a series of numbers or characters in a controlled manner, either increasing or decreasing. Kotlin provides built-in classes like `IntProgression`, `LongProgression`, and `CharProgression` to represent these sequences.

Visit the following resources to learn more:

- [@official@Progression](https://kotlinlang.org/docs/ranges.html#progression)

## Properties

# Properties in Kotlin Classes

Properties in Kotlin classes are variables declared directly inside a class. They represent the state of an object. Each property has a name, a type, and can optionally have a getter and a setter. Getters are used to read the property's value, and setters are used to modify it. If you don't explicitly define them, Kotlin automatically provides default getters and setters for mutable properties (declared with `var`) and a default getter for read-only properties (declared with `val`).

Visit the following resources to learn more:

- [@official@Properties](https://kotlinlang.org/docs/properties.html)
- [@article@Define class properties](https://developer.android.com/codelabs/basic-android-kotlin-compose-classes-and-objects#4)
- [@video@How to Use Class Properties in Kotlin](https://www.youtube.com/watch?v=xD830WM4iIQ)

## Property Delegates

# Property Delegates

Property delegation in Kotlin lets you reuse the logic for getting and setting a property. Instead of putting the getter and setter logic directly inside a class, you create a separate class (the delegate) that handles this logic. Then, you "delegate" the property's access to this class. This helps avoid code duplication and makes your code more maintainable by centralizing property behavior.

Visit the following resources to learn more:

- [@official@Delegated properties](https://kotlinlang.org/docs/delegated-properties.html)
- [@article@Define property delegates](https://developer.android.com/codelabs/basic-android-kotlin-compose-classes-and-objects#8)
- [@video@Full Guide to Delegation in Kotlin - Android Studio Tutorial](https://www.youtube.com/watch?v=MfJB-JhRAoQ&t=185s)

## Quarkus

# Quarkus

Quarkus provides first class support for using Kotlin. The framework is open source and maintained by Red Hat. Quarkus was built from the ground up for Kubernetes and provides a cohesive full-stack framework by leveraging a growing list of hundreds of best-of-breed libraries.

Visit the following resources to learn more:

- [@article@Quarkus Docs](https://quarkus.io/guides/)
- [@official@Using Kotlin with Quarkus](https://quarkus.io/guides/kotlin)
- [@video@Quarkus for Kotlin Developers](https://www.youtube.com/watch?v=faVGvVLWMmk)

## Ranges

# Ranges

Ranges in Kotlin define an interval of values. You can create them using the `..` operator, for example, `1..5` creates a range from 1 to 5 (inclusive). Ranges are commonly used in `for` loops to iterate over a sequence of numbers or characters, and you can check if a value falls within a range using the `in` operator. Kotlin also provides functions like `step` to modify the increment and `downTo` to create a descending range.

Visit the following resources to learn more:

- [@official@Ranges](https://kotlinlang.org/docs/ranges.html#range)
- [@article@Essential Insights into Kotlin Range: Syntax, Types, and Functions](https://www.dhiwise.com/post/essential-insights-into-kotlin-range-syntax-and-functions)

## Read Only Vs Mutable

# Read-Only vs. Mutable Collections

Kotlin distinguishes between read-only and mutable collections. Read-only collections provide methods to access data but not to modify it, ensuring data integrity. Mutable collections, on the other hand, allow for adding, removing, and updating elements, offering flexibility when data manipulation is required. Choosing the right type depends on whether the collection's content needs to be changed after its creation.

Visit the following resources to learn more:

- [@official@Collection Types](https://kotlinlang.org/docs/collections-overview.html#collection-types)
- [@official@Collection](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/)
- [@official@MutableCollection](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-collection/)
- [@video@Mutable vs Immutable - What You Need to Know](https://www.youtube.com/watch?v=RogMd01DlLw)

## Retrieving Collection Parts

# Retrieving Collection Parts

The Kotlin standard library contains extension functions for retrieving parts of a collection. Functions like `slice()`,`take()`,`drop()`, and `chunked()`, provide a variety of ways to select elements for the result collection: listing their positions explicitly, specifying the result size, and others.

Visit the following resources to learn more:

- [@official@Retrieve collection parts](https://kotlinlang.org/docs/collection-parts.html)
- [@video@Retrieving parts of Collection | slice | drop | chunked | windowed](https://www.youtube.com/watch?v=mALsyqRUfMI)

## Retrieving Single Elements

# Retrieving single elements

Kotlin collections provide a set of functions for retrieving single elements from list and sets. You can select single elements by position, by condition, with selectors, and even using random selection.

Visit the following resources to learn more:

- [@official@Retrieve single elements](https://kotlinlang.org/docs/collection-elements.html)
- [@video@Collections | Retrieving Single element from Collection](https://www.youtube.com/watch?v=4BncuTvd3hc)

## Return

# Return in Kotlin Functions

In Kotlin, the `return` statement is used within a function to stop its execution and send a value back to the caller.  The value returned must match the function's declared return type. If a function doesn't explicitly return a value (its return type is `Unit`), the `return` statement is optional at the end of the function; otherwise, it's required to provide a value of the correct type.

Visit the following resources to learn more:

- [@official@Explicit return types](https://kotlinlang.org/docs/functions.html#explicit-return-types)
- [@official@Unit-returning functions](https://kotlinlang.org/docs/functions.html#unit-returning-functions)

## Safe Casts

# Safe Casts

Safe casts in Kotlin provide a way to convert a variable of one type to another, but unlike regular casts, they handle the possibility of the cast failing gracefully. Instead of throwing a `ClassCastException` if the cast is not possible, a safe cast returns `null`. This allows you to safely attempt a type conversion and handle the case where the object is not of the expected type without crashing your program.

Visit the following resources to learn more:

- [@official@Safe casts](https://kotlinlang.org/docs/null-safety.html#safe-casts)
- [@video@Kotlin Safe Casting with 'as?'](https://www.youtube.com/watch?v=3ZvJb_f9jrU)

## Sealed Class

# Sealed Class

A sealed class in Kotlin represents a restricted class hierarchy. It's used when a value can have one of a limited set of types, but no other types. Essentially, it's an abstract class that restricts which classes can inherit from it. All subclasses of a sealed class must be declared in the same file as the sealed class itself. This restriction enables the compiler to know all possible subtypes at compile time, allowing for exhaustive `when` expressions.

Visit the following resources to learn more:

- [@official@Sealed classes and interfaces](https://kotlinlang.org/docs/sealed-classes.html)
- [@video@Sealed classes - Kotlin Vocabulary](https://www.youtube.com/watch?v=OyIRuxjBORY)
- [@video@Sealed Classes VS. Enum Classes VS. Sealed Interfaces - When to Use Which?](https://www.youtube.com/watch?v=kLJRZpRhX1o)

## Sequences

# Sequences

Sequences in Kotlin provide a way to perform operations on collections of data in a lazy manner. Instead of processing each element immediately, sequences evaluate operations only when the final result is needed. This can lead to significant performance improvements, especially when dealing with large datasets or complex transformations, as intermediate collections are avoided. They are particularly useful when you have a chain of operations to perform on a collection.

Visit the following resources to learn more:

- [@official@Sequences](https://kotlinlang.org/docs/sequences.html)
- [@official@Classification of Sequences](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/)
- [@video@Sequence Explained - Kotlin Collections](https://www.youtube.com/watch?v=_F4ZzK2Iquc)

## Serialization

# Serialization

Serialization is the process of converting an object's state into a format that can be stored or transmitted, and then reconstructed later. This allows you to save data to a file, send it over a network, or store it in a database, and then recreate the original object from that stored representation. Deserialization is the reverse process, taking the serialized data and reconstructing the object. In Kotlin, data serialization tools are available in the `kotlinx.serialization` library.

Visit the following resources to learn more:

- [@official@Serialization](https://kotlinlang.org/docs/serialization.html)
- [@opensource@kotlinx.serialization](https://github.com/Kotlin/kotlinx.serialization)
- [@video@How to Deserialize Inconsistent JSON Data With a Custom Kotlinx Serializer](https://www.youtube.com/watch?v=_KQBp5pwUO0&t=28s)

## Server Side Apps

# Server-Side Applications in Kotlin

Kotlin is a great fit for developing server-side applications. It allows you to write concise and expressive code while maintaining full compatibility with existing Java-based technology stacks, all with a smooth learning curve:

Visit the following resources to learn more:

- [@official@Kotlin for server side](https://kotlinlang.org/docs/server-overview.html)
- [@video@Google's Journey from Java to Kotlin for Server Side Programming](https://www.youtube.com/watch?v=o14wGByBRAQ&t=1s)

## Sets

# Sets in Kotlin

Sets in Kotlin are unordered collections of unique elements. This means a set cannot contain duplicate values. Sets support basic operations like adding elements, removing elements, and checking for membership. They are useful when you need to ensure that you only have distinct values in a collection, and the order of elements is not important.

Visit the following resources to learn more:

- [@official@Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/)
- [@article@Sets | Android](https://developer.android.com/codelabs/basic-android-kotlin-collections#3)

## Sets

# Set Operations

Sets in Kotlin, like in mathematics, are collections of unique elements. Kotlin provides specific operations to manipulate these sets, including `union` (combining two sets), `intersect` (finding common elements), and `subtract` (finding elements present in one set but not the other). These operations create new sets based on the original sets without modifying them, ensuring immutability. They are useful for tasks like comparing data, filtering unique items, and performing mathematical set theory operations.

Visit the following resources to learn more:

- [@official@Set-specific operations](https://kotlinlang.org/docs/set-operations.html)
- [@video@Kotlin Set Collection Tutorial - Unleash the Power of Sets](https://www.youtube.com/watch?v=qtoJLkv4Zd0)

## Setting Up The Environment

# Setting up the Kotlin Environment

Setting up the Kotlin environment involves installing the necessary tools and configuring your system to compile and run Kotlin code. This typically includes installing a Java Development Kit (JDK), downloading the Kotlin compiler, and optionally setting up an Integrated Development Environment (IDE) like IntelliJ IDEA or Android Studio with Kotlin plugins for a more streamlined development experience. The setup process ensures you have the required components to write, compile, and execute Kotlin programs.

Visit the following resources to learn more:

- [@official@Get started with Kotlin](https://kotlinlang.org/docs/getting-started.html#install-kotlin)
- [@video@Writing, Compiling, and Running Your First Kotlin Program](https://www.youtube.com/watch?v=bUm51_whyL8)

## Spring Boot

# Spring Boot with Kotlin

Spring Boot simplifies building Java applications by providing auto-configuration and a streamlined setup process. When used with Kotlin, it allows developers to leverage Kotlin's concise syntax, null safety, and modern features within the familiar Spring ecosystem. This combination enables the creation of robust and efficient backend applications with less boilerplate code compared to traditional Java-based Spring projects.

Visit the following resources to learn more:

- [@official@Get started with Spring Boot and Kotlin](https://kotlinlang.org/docs/jvm-get-started-spring-boot.html)
- [@official@Building web applications with Spring Boot and Kotlin](https://spring.io/guides/tutorials/spring-boot-kotlin)
- [@video@Full 2025 Backend Dev Crash Course for Beginners With Spring Boot (Kotlin, JWT Auth, MongoDB)](https://www.youtube.com/watch?v=tXC9DQRWHUQ)

## Spring

# Spring

Spring is a popular, open-source application framework for building robust and scalable Java applications. It provides a comprehensive infrastructure support for developing enterprise applications, handling concerns like dependency injection, aspect-oriented programming, data access, and transaction management. Spring makes use of Kotlin's language features to offer more concise APIs, starting with version 5.0. The online project generator allows you to quickly generate a new project in Kotlin.

Visit the following resources to learn more:

- [@official@Spring Docs](https://docs.spring.io/spring-framework/reference/index.html)
- [@official@Introducing Kotlin support in Spring Framework](https://spring.io/blog/2017/01/04/introducing-kotlin-support-in-spring-framework-5-0)
- [@video@Kotlin and Spring: The modern server side stack | Rod Johnson](https://www.youtube.com/watch?v=NcAW-FZtpzk)

## Standard Functions

# Standard Functions

Kotlin functions are declared using the `fun` keyword. 
`
fun double(x: Int): Int {
    return 2 * x
}
`
To call a functions, just:
`
val result = double(2)
`

Visit the following resources to learn more:

- [@official@Functions](https://kotlinlang.org/docs/functions.html)
- [@article@Kotlin Functions](https://www.w3schools.com/kotlin/kotlin_functions.php)
- [@video@Kotlin Functions in 20 minutes](https://www.youtube.com/watch?v=GlUnpf7MaO8)
- [@video@Basics of Functions](https://www.youtube.com/watch?v=0Lo3DIAL2y8)

## Standard Library

# Kotlin Standard Library

The Kotlin Standard Library is a collection of pre-built functions and classes that are available for use in any Kotlin project. It provides essential tools for common programming tasks, such as working with collections, strings, input/output, and more. This library simplifies development by offering ready-made solutions, reducing the need to write code from scratch for basic operations.

Visit the following resources to learn more:

- [@official@kotlin-stdlib](https://kotlinlang.org/api/core/kotlin-stdlib/)
- [@official@The standard library](https://kotlinlang.org/docs/kotlin-tour-intermediate-libraries-and-apis.html#the-standard-library)

## String Templates

# String Templates

String templates in Kotlin allow you to embed variables and expressions directly within strings. Instead of using string concatenation, you can include variables by prefixing them with a dollar sign (`$`). For more complex expressions, you can enclose them in curly braces `${}`. This makes string construction more readable and concise.

Visit the following resources to learn more:

- [@official@String Templates](https://kotlinlang.org/docs/strings.html#string-templates)

## Strings

# Strings

Strings in Kotlin represent sequences of characters. They are used to store and manipulate text. You can create strings using double quotes (") or triple quotes ("""). Strings are immutable, meaning their value cannot be changed after they are created. Kotlin provides various built-in functions and properties to work with strings, such as concatenation, substring extraction, and searching.

Visit the following resources to learn more:

- [@official@Strings](https://kotlinlang.org/docs/strings.html)

## Suspending Functions

# Suspending Functions

Suspending functions are the foundation of Kotlin's coroutine-based concurrency. They represent a computation that can be paused and resumed later, potentially without blocking the thread. This allows you to write asynchronous, non-blocking code in a sequential, easy-to-read style, improving responsiveness and resource utilization.

Visit the following resources to learn more:

- [@official@Coroutines basics](https://kotlinlang.org/docs/coroutines-basics.html)
- [@official@Composing suspending functions](https://kotlinlang.org/docs/composing-suspending-functions.html)
- [@video@Suspend Functions - Kotlin Coroutines](https://www.youtube.com/watch?v=yc_WfBp-PdE)

## Swiftobjective C Interop

# Swift/Objective-C Interop in Kotlin/Native

Kotlin/Native allows you to use Swift and Objective-C code directly in your Kotlin projects, and vice versa. This means you can leverage existing iOS libraries and frameworks within your Kotlin/Native code, and also expose Kotlin code to be used in Swift/Objective-C projects. This interoperability is achieved through automatic generation of bindings that handle the translation between Kotlin and Swift/Objective-C types and function calls.

Visit the following resources to learn more:

- [@official@Interoperability with Swift/Objective-C](https://kotlinlang.org/docs/native-objc-interop.html#importing-swift-objective-c-libraries-to-kotlin)

## Tail Recursive Functions

# Tail-recursive Functions

Kotlin supports a style of functional programming known as tail recursion. For some algorithms that would normally use loops, you can use a recursive function instead without the risk of stack overflow. When a function is marked with the tailrec modifier and meets the required formal conditions, the compiler optimizes out the recursion, leaving behind a fast and efficient loop based version instead.

Visit the following resources to learn more:

- [@official@Tail-recursive Functions](https://kotlinlang.org/docs/functions.html#tail-recursive-functions)
- [@article@Kotlin Recursion (Recursive Function) and Tail Recursion](https://www.programiz.com/kotlin-programming/recursion)

## Teamcity

# TeamCity

TeamCity is a powerful and flexible continuous integration and continuous delivery (CI/CD) server developed by JetBrains. It automates the processes of building, testing, and deploying software, allowing development teams to streamline their workflows and deliver high-quality products faster. It integrates with various version control systems, build tools, and testing frameworks, providing a centralized platform for managing the entire software development lifecycle.

Visit the following resources to learn more:

- [@official@TeamCity](https://www.jetbrains.com/teamcity/)
- [@official@Kotlin and continuous integration with TeamCity](https://kotlinlang.org/docs/kotlin-and-ci.html)
- [@video@TeamCity Kotlin DSL tutorials](https://www.youtube.com/playlist?list=PLQ176FUIyIUaW-RqAJLbSZe59l6r7t8wp)

## Test Library

# Kotlin Test Library

`kotlin.test` is a library in Kotlin that provides a set of tools and functions for writing and running unit tests. It allows developers to verify that their code behaves as expected by defining test cases and assertions. These assertions check if the actual output of a function or code block matches the expected output, helping to ensure the correctness and reliability of Kotlin applications.

Visit the following resources to learn more:

- [@official@kotlin.test](https://kotlinlang.org/api/core/kotlin-test/)
- [@official@Test code using JUnit in JVM – tutorial](https://kotlinlang.org/docs/jvm-test-using-junit.html)

## Throwing Exceptions

# Throwing Exceptions

Throwing exceptions indicate when a problem occurs. You can manually throw exceptions with the `throw` keyword. Throwing an exception indicates that an unexpected runtime error has occurred in the code. Exceptions are objects, and throwing one creates an instance of an exception class. You can throw an exception without any parameters or by using precondition functions﻿, such as `require()`, `check()`, and `error()`

Visit the following resources to learn more:

- [@official@Throw exceptions](https://kotlinlang.org/docs/exceptions.html#throw-exceptions)

## Transformations

# Transformations in Kotlin Collections

Transformations in Kotlin collections involve modifying the elements within a collection to create a new collection. These operations allow you to apply a function to each element, changing its value or structure, without altering the original collection. Common transformations include mapping (changing the value of each element), flattening (combining nested collections into a single collection), and zipping (combining two collections element-wise).

Visit the following resources to learn more:

- [@official@Collection transformation operations](https://kotlinlang.org/docs/collection-transformations.html)
- [@video@Collection Operations | Transformation | map | zip](https://www.youtube.com/watch?v=eN4CS--hE1Q)

## Type Aliases

# Type Aliases

A type alias in Kotlin provides an alternative name for an existing type. It doesn't create a new type; instead, it introduces a new identifier that you can use interchangeably with the original type. This can improve code readability by providing more descriptive names for complex types or simplifying long type declarations. Type aliases are particularly useful when dealing with function types or generic types, making the code easier to understand and maintain.

Visit the following resources to learn more:

- [@official@Type aliases](https://kotlinlang.org/docs/type-aliases.html#type-aliases.md)
- [@video@Kotlin For Beginners - Type Alias](https://www.youtube.com/watch?v=4BLSDkXMIm0)

## Type Checks  Casts

# Type Checks & Casts

Kotlin allows you to check the type of a variable at runtime using the `is` operator. This operator returns `true` if a variable is of a certain type.  Furthermore, Kotlin's smart casts automatically cast a variable to a more specific type within a block of code if the compiler can guarantee that the variable is of that type due to a type check. This eliminates the need for explicit casting in many situations, making the code cleaner and safer.

Visit the following resources to learn more:

- [@official@Type checks and casts](https://kotlinlang.org/docs/typecasts.html)
- [@article@Navigating Kotlin’s Type System: A Guide to Type Checks and Casts with ‘is’ and ‘as’](https://medium.com/learn-to-earn/navigating-kotlins-type-system-a-guide-to-type-checks-and-casts-with-is-and-as-0368ae9e4337)

## Type Inference

# Type Inference

Kotlin, a statically typed language, introduces type inference to enhance code readability and reduce redundancy, making coding simpler without losing type safety. With Kotlin type inference, the Kotlin compiler automatically deduces types in various contexts, saving developers from explicitly declaring them each time.

Visit the following resources to learn more:

- [@article@Type inference](https://kotlinlang.org/spec/type-inference.html)
- [@article@Understanding Kotlin Type Inference: What You Need to Know](https://www.dhiwise.com/post/understanding-kotlin-type-inference-what-you-need-to-know)
- [@article@How Type Inference Works in Kotlin](https://www.youtube.com/watch?v=Hyq_yho2JD8)

## Understanding Packages

# Packages

Packages are namespaces that organize related classes, interfaces, functions, and other declarations in Kotlin. They provide a way to group code logically, prevent naming conflicts, and control visibility. By using packages, you can structure your project into manageable modules and improve code reusability.

Visit the following resources to learn more:

- [@official@Packages and imports](https://kotlinlang.org/docs/packages.html)
- [@video@Packages and Imports: Kotlin for Complete Beginners 045](https://www.youtube.com/watch?v=VGg3g2ZT9jQ)

## Unsigned Integers

# Unsigned Integers

Unsigned integers in Kotlin are data types that represent whole numbers that cannot be negative. Unlike regular integers (like `Int`), unsigned integers (like `UInt`) only store positive values and zero. This allows them to represent a larger range of positive numbers compared to their signed counterparts, given the same amount of memory. Kotlin provides specific unsigned integer types such as `UInt`, `ULong`, `UShort`, and `UByte` to handle scenarios where negative values are not needed, potentially improving performance and clarity.

Visit the following resources to learn more:

- [@official@Unsigned integer types](https://kotlinlang.org/docs/unsigned-integer-types.html)
- [@video@Kotlin Unsigned Integers Explained | UByte, UInt, UShort, ULong Tutorial](https://www.youtube.com/watch?v=L94nxNlI96s)

## Val Vs Var

# Val vs Var

In Kotlin, both `val` and `var` are used to declare variables, but they differ in mutability. A `val` variable is immutable, meaning its value cannot be changed after it's initially assigned. Conversely, a `var` variable is mutable, allowing its value to be reassigned multiple times throughout the program's execution. Choosing between `val` and `var` depends on whether the variable's value needs to be modified after its initial assignment.

Visit the following resources to learn more:

- [@official@Variables](https://kotlinlang.org/docs/basic-syntax.html#variables)
- [@article@Variable declaration](https://developer.android.com/kotlin/learn#:~:text=Kotlin%20uses%20two%20different%20keywords,variable%20whose%20value%20can%20change.)
- [@video@Learn Kotlin 02 Var vs Val Variables](https://www.youtube.com/watch?v=Klus0Uh40Lw)

## Varargs

# Varargs

Varargs (variable arguments) in Kotlin allow a function to accept a variable number of arguments of the same type. Instead of defining multiple function overloads for different numbers of arguments, you can use the `vararg` keyword in the function's parameter list. This creates a single function that can be called with any number of arguments (including zero) of the specified type, which are then accessible within the function as an array.

Visit the following resources to learn more:

- [@official@Variable number of arguments (varargs)](https://kotlinlang.org/docs/functions.html#variable-number-of-arguments-varargs)
- [@video@Function expression & vararg](https://www.youtube.com/watch?v=lQhTdcT650I)

## Variables

# Variables

Variables are named storage locations in a computer's memory that hold data. Think of them as containers that can store different types of information, like numbers, text, or boolean values (true/false). You give each variable a name so you can easily refer to the data it holds and modify it as needed throughout your program.

Visit the following resources to learn more:

- [@official@Variables](https://kotlinlang.org/docs/basic-syntax.html#variables)

## Vertx

# Vert.x

Vert.x is a toolkit for building reactive applications on the JVM. It provides a non-blocking, event-driven concurrency model, making it well-suited for building scalable and high-performance server-side applications. With Vert.x, you can handle a large number of concurrent connections using a small number of threads, leading to efficient resource utilization.

Visit the following resources to learn more:

- [@official@Vert.x Docs](https://vertx.io/docs/4.1.8/)
- [@official@Vert.x for Kotlin](https://vertx.io/docs/4.1.8/vertx-core/kotlin/)
- [@video@Using Vertx with Kotlin | Simon Billingsley](https://www.youtube.com/watch?v=S8nW4RzUQLs)

## Visibility Modifiers

# Visibility Modifiers

Visibility modifiers control the accessibility of classes, objects, interfaces, constructors, properties, and functions in Kotlin. They determine from where these declarations can be accessed. Kotlin provides four visibility modifiers: `private`, `protected`, `internal`, and `public`. Each modifier restricts access to different scopes, allowing you to encapsulate your code and control how it's used.

Visit the following resources to learn more:

- [@official@Visibility modifiers](https://kotlinlang.org/docs/visibility-modifiers.html#visibility-modifiers.md)
- [@article@Visibility modifiers](https://developer.android.com/codelabs/basic-android-kotlin-compose-classes-and-objects#7)
- [@video@Kotlin Newbie to Pro - VISIBILITY MODIFIERS](https://www.youtube.com/watch?v=Xk3IPNHbLVk)

## What Is Null Safety

# Null Safety

Null safety is a feature that helps prevent null pointer exceptions, a common cause of program crashes. Kotlin distinguishes between nullable and non-nullable types. By default, variables cannot hold null values. To allow a variable to hold null, you must explicitly declare it as nullable using a question mark (?). This allows the compiler to catch potential null pointer exceptions at compile time, making your code more robust.

Visit the following resources to learn more:

- [@official@Null safety](https://kotlinlang.org/docs/null-safety.html#null-safety.md)
- [@official@Nullability in Java and Kotlin](https://kotlinlang.org/docs/java-to-kotlin-nullability-guide.html)
- [@video@Kotlin NULL Safe Operators | Best Explanation Ever | Elvis Operator and Non Null Assertion Operators](https://www.youtube.com/watch?v=fxQbpy-s3Bw)

## When

# When Expression

In Kotlin, the `when` expression is a powerful control flow statement used to execute different blocks of code based on different conditions. It's similar to a `switch` statement in other languages, but more flexible and expressive. The `when` expression can be used as a statement or as an expression, returning a value based on the matched condition. It allows you to check for equality, ranges, types, or any arbitrary boolean condition, making it a versatile tool for handling multiple branches of logic.

Visit the following resources to learn more:

- [@official@When expressions and statements](https://kotlinlang.org/docs/control-flow.html#when-expressions-and-statements)
- [@article@Use a when statement for multiple branches](https://developer.android.com/codelabs/basic-android-kotlin-compose-conditionals#2)
- [@video@Control Flows | if else | when - the cooler switch](https://www.youtube.com/watch?v=Wp2UU4yKjqM)

## While

# While and Do-While Loops

In Kotlin, `while` and `do-while` loops are used to repeatedly execute a block of code based on a condition. The `while` loop checks the condition *before* each execution of the block; if the condition is true, the block executes, and the process repeats. The `do-while` loop, on the other hand, executes the block *at least once* and then checks the condition; the block continues to execute as long as the condition remains true.

Visit the following resources to learn more:

- [@official@While Loops](https://kotlinlang.org/docs/control-flow.html#while-loops)

## Why Use Kotlin

# Why Use Kotlin?

Kotlin is a modern programming language that makes coding easier and more efficient. It's designed to be simple to learn and use, helping developers write cleaner and more reliable code. Kotlin also works seamlessly with existing Java code, making it easy to integrate into current projects. Kotlin can be used for any kind of development, be it server-side, client-side web, Android, or multiplatform library. With Kotlin/Native currently in the works, support for other platforms such as embedded systems, macOS, and iOS. People are using Kotlin for mobile and server-side applications, client-side with JavaScript or JavaFX, and data science, just to name a few possibilities.

Visit the following resources to learn more:

- [@official@Kotlin FAQs](https://kotlinlang.org/docs/faq.html)
- [@video@Kotlin in 100 Seconds](https://www.youtube.com/watch?v=xT8oP0wy-A0)

## Writing  Reading Files

# Writing & Reading Files

Writing and reading files in Kotlin involves using classes from the `java.io` package. To write to a file, you typically create a `File` object and then use classes like `FileWriter` or `BufferedWriter` to write data. Reading from a file is similar, using `File` along with classes like `FileReader` or `BufferedReader` to read the file's contents line by line or as a whole. These operations allow you to persist data to disk and retrieve it later.

Visit the following resources to learn more:

- [@article@File Handling in Kotlin: Reading & Writing Files Made Simple!](https://medium.com/@YodgorbekKomilo/day-18-file-handling-in-kotlin-reading-writing-files-made-simple-da774d449459)
- [@video@Working With Files In Kotlin - IO Essentials](https://www.youtube.com/watch?v=MSeI7XVzrvo)
