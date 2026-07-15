# Cpp Roadmap

## Access Violations

# Access Violations

An access violation occurs when a program tries to read from or write to a memory location that it doesn't have permission to access. This is a common error in C++ that can arise from issues like dereferencing null or invalid pointers, accessing arrays beyond their bounds, or attempting to use memory that has already been freed. Debugging tools such as debuggers, static analyzers (like those in Visual Studio), and runtime memory error detectors (such as Valgrind or AddressSanitizer) are essential for identifying and resolving these violations by pinpointing the offending code.

## Algorithms

# STL Algorithms

The C++ Standard Template Library (STL) offers a rich collection of generic algorithms that operate on various container types. These algorithms, found primarily in the `<algorithm>` header, provide functionalities for common tasks like sorting, searching, and sequence manipulation. They promote code reusability and efficiency by working independently of the specific data structures they operate on.

## Argument Dependent Lookup Adl

# Argument Dependent Lookup (ADL)

Argument Dependent Lookup (ADL), also known as Koenig Lookup, is a feature in C++ that extends the function lookup process by allowing the compiler to search for functions in the namespaces of the function arguments' types. This is especially useful when working with overloaded operators and functions defined within namespaces, enabling more intuitive and concise code by automatically finding the appropriate function based on the argument types, even if it's not explicitly qualified.

Visit the following resources to learn more:

- [@article@Argument Dependent Lookup (ADL)](https://en.cppreference.com/w/cpp/language/adl.html)
- [@video@C++ Weekly - Ep 160 - Argument Dependent Lookup (ADL)](https://backoffice.roadmap.sh/tree/cpp)

## Arithmetic Operators

# Arithmetic Operators

Arithmetic operators are fundamental building blocks in C++ programming, allowing you to perform mathematical calculations directly within your code. These operators work on numeric data types such as integers and floating-point numbers, enabling addition (+), subtraction (-), multiplication (\*), division (/), and modulus (%) operations. Furthermore, increment (++) and decrement (--) operators provide concise ways to increase or decrease variable values by one.

Visit the following resources to learn more:

- [@article@Arithmetic Operators](https://www.w3schools.com/cpp/cpp_operators_arithmetic.asp)

## Auto Automatic Type Deduction

# Auto Type Deduction

`auto` is a keyword in C++ introduced in C++11 that enables automatic type deduction. It allows the compiler to infer the data type of a variable from its initialization expression at compile time. This simplifies code by reducing the need to explicitly declare types, particularly when dealing with complex or less predictable types, leading to cleaner and more maintainable code. In C++14, `auto` can also be used to deduce function return types based on the return expression.

Visit the following resources to learn more:

- [@article@Automatic Type Deduction: auto](https://www.educative.io/courses/cpp-fundamentals-for-professionals/automatic-type-deduction-auto)
- [@video@The "auto" keyword in C++](https://www.youtube.com/watch?v=2vOPEuiGXVo)

## Basic Operations

# Basic Operations

Understanding fundamental operations is crucial for any C++ developer. This foundational knowledge includes arithmetic operations such as addition, subtraction, multiplication, and division, as well as comparison operations (e.g., equal to, not equal to, greater than) used in conditional logic. Mastering these operations forms the bedrock upon which more complex algorithms and data structures are built.

## Bitwise Operators

# Bitwise Operators

Bitwise operators in C++ allow direct manipulation of individual bits within integer data types. These operators work by treating values as sequences of bits and performing operations at the bit level. Common bitwise operators include AND (&), OR (|), XOR (^), NOT (~), left shift (<<), and right shift (>>). They are utilized for tasks such as setting, clearing, or toggling specific bits, optimizing performance in certain algorithms, and low-level system programming.

Visit the following resources to learn more:

- [@video@Intro to Binary and Bitwise Operators in C++](https://youtu.be/KXwRt7og0gI)
- [@video@Bitwise AND (&), OR (|), XOR (^) and NOT (~) in C++](https://youtu.be/HoQhw6_1NAA)

## Boost

# Boost

Boost is a set of peer-reviewed, portable C++ source libraries. It provides a wide range of utilities and tools that can significantly enhance your C++ development, covering areas like data structures, algorithms, mathematical functions, concurrency, and more. Boost libraries are designed to integrate well with the C++ Standard Library and often serve as incubators for features that eventually make their way into the standard.

Visit the following resources to learn more:

- [@official@Boost Libraries](https://www.boost.org/)

## Build Systems

# Build Systems

Build systems in C++ automate the compilation, linking, and execution of source code, managing the complexity of the build process to produce executables or libraries. Common examples include GNU Make, which uses Makefiles to track dependencies and timestamps, and CMake, a cross-platform system that generates build files for various platforms. Autotools is another option for creating portable software across different Unix-based systems. SCons leverages Python for more expressive build scripts, while Ninja focuses on speed by efficiently building targets specified in a simple text file. Each system offers different approaches to streamlining the software construction process.

## C 0X

# C++11

C++11, formerly known as C++0x, represents a significant evolution of the C++ language standard, finalized in 2011. This version introduced features like automatic type inference with `auto`, simplified container iteration using range-based for loops, the ability to create anonymous functions via lambda expressions, and a safer way to represent null pointers using `nullptr`. Furthermore, C++11 optimized temporary object handling through rvalue references and move semantics, enabled templates to accept a variable number of arguments with variadic templates, facilitated compile-time assertions via static assertions, and integrated thread support for concurrent programming.

## C 11  14

# C++11 and C++14

C++11 and C++14 are significant updates to the C++ language, introducing features to enhance its power and usability. C++11 brought in features like `auto` for type inference, range-based for loops for simpler iteration, lambda functions for creating anonymous functions, `nullptr` for safer null pointer representation, and a standard thread support library. Building upon this, C++14 refined these features and added new capabilities, including generic lambdas, binary literals, `decltype(auto)` for precise type deduction, and variable templates. These standards made C++ more modern, expressive, and efficient.

## C 17

# C++17

C++17 is a significant update to the C++ language, offering new features and enhancements that improve code expressiveness and efficiency. This version introduces features such as structured bindings for easier data unpacking, `if` and `constexpr if` statements for compile-time conditional logic, and inline variables for simplified header usage. Furthermore, C++17 incorporates the `std::filesystem` library for file system operations, as well as `std::string_view`, `std::any`, `std::optional`, and `std::variant` for enhanced data handling, alongside parallel algorithms to boost performance.

## C 20

# C++20

C++20 represents a significant evolution of the C++ language, introducing key features aimed at improving code clarity, efficiency, and concurrency. Highlights include Concepts, which enforce constraints on template parameters for better error messages; Ranges, a new way to work with sequences of values enhancing standard library algorithms; Coroutines, for writing asynchronous code with improved readability; and enhancements to compile-time evaluation with `constexpr` and `consteval`. These additions, along with other library improvements, empower developers to create more expressive, robust, and high-performance applications.

## C 23

# C++23

C++23 is the latest version of the C++ standard, building upon previous iterations to introduce new features, library enhancements, and language improvements. It aims to simplify development, improve performance, and provide more modern tools for C++ programmers. This standard incorporates features like `std::expected`, stackable coroutines, and improvements to the standard library, making C++ more robust and expressive.

Visit the following resources to learn more:

- [@official@The Standard](https://isocpp.org/std/the-standard)
- [@article@C++23](https://en.wikipedia.org/wiki/C%2B%2B23)
- [@article@Overview of New Features in C++23](https://medium.com/@threehappyer/overview-of-new-features-in-c-23-68c5bc668958)
- [@video@C++23: An Overview of Almost All New and Updated Features - Marc Gregoire - CppCon 2023](https://www.youtube.com/watch?v=Cttb8vMuq-Y)

## C Vs C

# C vs C++

C and C++ are both programming languages, with C++ evolving from C. C is a procedural language focused on structured programming using functions. C++ expands upon C by adding object-oriented programming (OOP) features like classes, inheritance, and polymorphism, enabling more complex and modular software design. C++ also introduces features like operator overloading, templates, and exception handling, offering greater flexibility and abstraction compared to C.

Visit the following resources to learn more:

- [@article@C++ vs. C: When (and when not) to use each language](https://roadmap.sh/cpp/vs-c)

## Catch2

# Catch2

Catch2 is a modern, C++-native, header-only framework for writing unit tests, benchmarks, and even simple command-line applications. It provides a simple and expressive syntax for defining test cases, assertions, and sections, making it easy to write and maintain comprehensive tests for your C++ code. It supports features like test case discovery, parameterized tests, and integration with various IDEs and build systems.

Visit the following resources to learn more:

- [@official@Catch2](https://catch2.org/)
- [@opensource@Catch2](https://github.com/catchorg/Catch2)

## Cmake

# CMake

CMake is a cross-platform build system generator. It uses configuration files (CMakeLists.txt) to describe the build process and generates native build files like Makefiles or project files for IDEs like Visual Studio. CMake simplifies the build process, especially for complex projects, by abstracting the underlying build tools and providing a consistent interface across different platforms and compilers. It manages dependencies, specifies compiler flags, and handles the overall structure of your project's build process without actually building the project itself.

Visit the following resources to learn more:

- [@article@CMAKE Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)
- [@video@CMake, How it Works (At Three Different Levels)](https://www.youtube.com/watch?v=SDX0oYqdv_g)

## Code Editors  Ides

# Code Editors / IDEs

Choosing the right code editor or IDE is a crucial first step for any C++ developer. These tools provide a platform for writing, editing, and managing your code, often including features like syntax highlighting, code completion, debugging tools, and build automation. Popular options range from lightweight and customizable editors like Visual Studio Code and Sublime Text, to more comprehensive IDEs like Visual Studio and CLion, each with its own strengths and features. Selecting the best one for you often comes down to personal preference and your specific development needs.

Visit the following resources to learn more:

- [@article@Using C++ on Linux in VSCode](https://code.visualstudio.com/docs/cpp/config-linux)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Compiler Stages

# Compiler Stages

The compilation process in C++ transforms human-readable source code into an executable program through four distinct stages. These stages are: Preprocessing, which handles directives like `#include` and macro replacements; Compilation, where the preprocessed code is translated into assembly language; Assembly, which converts the assembly code into object code; and Linking, where object code is combined with libraries to create the final executable. Each stage performs a specific set of tasks to ensure the code is properly transformed for execution on the target platform.

## Compilers And Features

# Compilers and Features

C++ compilers translate human-readable C++ code into machine-executable code. They offer various features, including optimization techniques to improve program performance by eliminating redundancies and restructuring code, debugging information generation to aid in troubleshooting, and warning systems to flag potentially problematic code. Popular compilers include GCC, a versatile open-source option; Clang, known for its compatibility and diagnostics; Microsoft Visual C++, integrated within the Visual Studio IDE; and the Intel C++ Compiler, part of the Intel Parallel Studio XE suite. Familiarizing yourself with your chosen compiler's documentation is essential to fully leverage its capabilities.

## Compilers

# Compilers

A compiler is a program that translates source code from one programming language into another, often machine code, enabling a computer to execute the instructions. In C++, compilers take your human-readable code and convert it into an executable program. Popular options include GCC, Clang, MSVC, and ICC, each with its own strengths in terms of platform support, optimization, and diagnostics. Compilers work with linkers and standard libraries to produce the final executable, combining compiled code and providing common functionalities.

## Conan

# Conan

Conan is a package manager specifically designed for C and C++ projects. It helps developers manage dependencies, build configurations, and share pre-built libraries across different platforms and build systems like CMake and Visual Studio. Using Conan, you can easily declare project dependencies, fetch them from remote repositories, and integrate them into your build process, simplifying the overall dependency management workflow.

Visit the following resources to learn more:

- [@opensource@conan](https://github.com/conan-io/conan)
- [@article@A Beginner’s Guide to Conan 2: C and C++ Package Manager](https://medium.com/@milan.pultar/a-beginners-guide-to-conan-2-c-and-c-package-manager-b0cbc1f99175)
- [@video@Introduction to Conan 2 - The Best C++ Package Manager?](https://www.youtube.com/watch?v=U-_RbUqDSTc)

## Const Cast

# const_cast

`const_cast` is a C++ casting operator that allows you to explicitly add or remove the `const` or `volatile` qualifier from a variable's type. This essentially enables you to modify an object that was initially declared as `const` or pass a `const` object to a function that expects a non-`const` argument. It's a powerful tool but should be used with caution, as modifying a truly `const` object directly can lead to undefined behavior.

## Containers

# C++ Containers

C++ Containers are a part of the Standard Template Library (STL) that provide data structures to store and organize data. There are several types of containers, each with its own characteristics and use cases. Here, we discuss some of the commonly used containers:

1\. Vector
----------

Vectors are dynamic arrays that can resize themselves as needed. They store elements in a contiguous memory location, allowing fast random access using indices.

Example
-------

    #include <iostream>
    #include <vector>
    
    int main() {
        std::vector<int> vec = {1, 2, 3, 4, 5};
    
        vec.push_back(6); // Add an element to the end
    
        std::cout << "Vector contains:";
        for (int x : vec) {
            std::cout << ' ' << x;
        }
        std::cout << '\n';
    }
    

2\. List
--------

A list is a doubly-linked list that allows elements to be inserted or removed from any position in constant time. It does not support random access. Lists are better than vectors for scenarios where you need to insert or remove elements in the middle frequently.

Example
-------

    #include <iostream>
    #include <list>
    
    int main() {
        std::list<int> lst = {1, 2, 3, 4, 5};
    
        lst.push_back(6); // Add an element to the end
        
        std::cout << "List contains:";
        for (int x : lst) {
            std::cout << ' ' << x;
        }
        std::cout << '\n';
    }
    

3\. Map
-------

A map is an associative container that stores key-value pairs. It supports the retrieval of values based on their keys. The keys are sorted in ascending order by default.

Example
-------

    #include <iostream>
    #include <map>
    
    int main() {
        std::map<std::string, int> m;
    
        m["one"] = 1;
        m["two"] = 2;
    
        std::cout << "Map contains:\n";
        for (const auto &pair : m) {
            std::cout << pair.first << ": " << pair.second << '\n';
        }
    }
    

4\. Unordered\_map
------------------

Similar to a map, an unordered map stores key-value pairs, but it is implemented using a hash table. This means unordered\_map has faster average-case performance compared to map, since it does not maintain sorted order. However, worst-case performance can be worse than map.

Example
-------

    #include <iostream>
    #include <unordered_map>
    
    int main() {
        std::unordered_map<std::string, int> um;
    
        um["one"] = 1;
        um["two"] = 2;
    
        std::cout << "Unordered map contains:\n";
        for (const auto &pair : um) {
            std::cout << pair.first << ": " << pair.second << '\n';
        }
    }
    

These are just a few examples of C++ containers. There are other container types, such as `set`, `multiset`, `deque`, `stack`, `queue`, and `priority_queue`. Each container has its own use cases and unique characteristics. Learning about these containers and when to use them can greatly improve your efficiency and effectiveness in using C++.

## Control Flow  Statements

# Control Flow & Statements

Control flow in C++ dictates the order in which statements are executed. It allows programs to make decisions, repeat actions, and execute different code blocks based on conditions. Statements like `if`, `else if`, and `else` enable conditional execution, while loops such as `for`, `while`, and `do-while` facilitate repetition. `switch` statements offer a multi-way branching mechanism based on the value of an expression. These constructs are fundamental for creating programs that respond dynamically to input and perform complex tasks.

## Copy And Swap

# Copy and Swap

Copy and Swap is a C++ idiom used to implement the assignment operator in a safe and efficient manner. It works by creating a copy of the right-hand side object, then swapping the internal state of the copy with the object being assigned to. The temporary copy, now holding the original state, is then destroyed when the function exits, ensuring proper resource management and exception safety. This leverages existing copy constructors and swap functions, leading to cleaner and more robust code.

Visit the following resources to learn more:

- [@video@Copying and Copy Constructors in C++](https://www.youtube.com/watch?v=BvR1Pgzzr38)

## Copy On Write

# Copy on Write

The Copy-on-Write (CoW) idiom is an optimization technique used to defer or eliminate the cost of copying resources until the first write operation. Instead of creating a new copy of an object immediately, the original object and the "copy" share the same underlying resource. Only when one of the objects attempts to modify the shared resource is a true copy created. This can significantly improve performance by avoiding unnecessary copying, especially for large objects.

## Crtp

# CRTP

The Curiously Recurring Template Pattern (CRTP) is a C++ idiom where a class template inherits from its own specialization. This technique achieves static polymorphism, offering an alternative to runtime polymorphism using virtual functions. CRTP allows customization of base class behavior without virtual function call overhead, enabling compile-time polymorphism for improved performance. It's useful when you need to extend or modify functionality in derived classes while maintaining efficiency by avoiding the runtime cost associated with virtual functions.

Visit the following resources to learn more:

- [@article@CRTP (Curiously Recurring Template Pattern) in C++](https://medium.com/@sagar.necindia/crtp-curiously-recurring-template-pattern-in-c-90981941bf38)
- [@video@C++ Tutorial: How to use CRTP to speed up your code](https://www.youtube.com/watch?v=Srx4eiBdpdQ)

## Data Types

# Data Types

Data types in C++ categorize the kind of values a variable can hold, influencing memory usage and allowable operations. C++ offers fundamental types like `int` for integers, `float` and `double` for floating-point numbers, `char` for single characters, and `bool` for logical values. Beyond these basics, derived types such as arrays, pointers, and references provide more complex data handling capabilities. Finally, users can define their own types using structures, classes, and unions to create custom data organizations.

Visit the following resources to learn more:

- [@article@Data Types](https://www.w3schools.com/cpp/cpp_data_types.asp)

## Date  Time

# Date / Time

The C++ `chrono` library, part of the Standard Template Library (STL), offers tools for handling dates and times. It allows you to represent time spans as `durations` (e.g., seconds, minutes, hours), specific moments as `time_points` based on clocks, and access the current time using different `clock` types like `system_clock`, `steady_clock`, and `high_resolution_clock`. You can also convert `time_points` to calendar time for human-readable formats.

## Debuggers

# Debuggers

Debuggers are indispensable tools in C++ development, enabling developers to identify, analyze, and resolve defects within their code. These tools allow you to step through your code, inspect variables, and understand the program's execution flow, ultimately leading to more robust and reliable software. Several options are available, including GDB (GNU Debugger), LLDB, Microsoft Visual Studio Debugger, Intel Debugger (IDB), and TotalView Debugger, each offering unique features and catering to different development environments and application types.

## Debugging Symbols

# Debugging Symbols

Debugging symbols are essential for effective debugging in C++. They provide debuggers with information about the program's structure, source code relationships, and variable representations, allowing developers to step through code, inspect variables, and understand the program's behavior. These symbols can be embedded directly within the compiled binary (internal) or stored in separate files (external), such as `.pdb` on Windows or `.dSYM` on macOS. Tools like `g++` offer flags like `-g` (for internal symbols) and `-gsplit-dwarf` (for external symbols) to generate these symbols during compilation, while the `strip` command can be used to remove internal symbols from production binaries.

## Diamond Inheritance

# Diamond Inheritance

Diamond inheritance arises in C++ when a class inherits from multiple classes that, in turn, inherit from a common base class, creating a diamond-shaped hierarchy. This can lead to ambiguity because the derived class inherits multiple copies of the base class's members. To resolve this issue, virtual inheritance is used, ensuring only one instance of the base class exists in the final derived class, eliminating ambiguity and ensuring proper member access.

Visit the following resources to learn more:

- [@article@Understanding Virtual Inheritance and the Diamond Problem in C++](https://medium.com/@antilogatharv/understanding-virtual-inheritance-and-the-diamond-problem-in-c-da7c63d76723)

## Dynamic Polymorphism

# Dynamic Polymorphism

Dynamic polymorphism is a feature in C++ that allows objects of different classes to be treated as objects of a common type. This is achieved through virtual functions, where a derived class can override a function defined in its base class. When a virtual function is called through a base class pointer or reference, the correct function implementation for the derived class object is executed at runtime, enabling flexible and extensible code.

Visit the following resources to learn more:

- [@article@Understanding Dynamic Polymorphism in C++](https://hackernoon.com/understanding-dynamic-polymorphism-in-c)
- [@video@Dynamic Binding (Polymorphism) With The Virtual Keyword | C++ Tutorial](https://www.youtube.com/watch?v=-FUhG98hdLI)

## Dynamic Typing

# Dynamic Typing

While C++ is fundamentally a statically-typed language where data types are checked at compile time, it provides mechanisms to achieve a degree of dynamic typing. This involves determining the data types of variables during runtime, primarily through the use of `void*` pointers, which can point to any data type (requiring explicit casting), and the `std::any` class (introduced in C++17), a type-safe container capable of holding values of any type. Both approaches enable flexibility but require careful consideration due to potential runtime overhead and type-related errors.

Visit the following resources to learn more:

- [@article@Dynamic Typing in C++](https://codesignal.com/learn/courses/advanced-functional-programming-techniques/lessons/dynamic-type-declaration-in-cpp)
- [@video@Static vs Dynamic Typing](https://www.youtube.com/watch?v=GqXpFycPWLE)

## Dynamic Cast

# Dynamic Cast

`dynamic_cast` is a C++ casting operator primarily used within polymorphic class hierarchies to safely convert pointers or references from a base class to a derived class. Unlike static casts, it performs a runtime check to ensure the validity of the conversion. If the object being cast is not actually an instance of the target derived class, `dynamic_cast` returns a null pointer (for pointer casts) or throws a `std::bad_cast` exception (for reference casts), preventing undefined behavior and enabling safer downcasting.

## Erase Remove

# Erase-Remove

The Erase-Remove idiom is a common C++ technique used to efficiently remove elements from a container (like `std::vector`, `std::list`, etc.). It involves using `std::remove` (or `std::remove_if`) to move the elements to be removed to the end of the container, followed by using the container's `erase()` method to actually remove those elements, effectively shrinking the container.

Visit the following resources to learn more:

- [@article@std::remove, std::remove_if](https://en.cppreference.com/w/cpp/algorithm/remove.html)
- [@video@C++ STL algorithm - erase-remove idiom -- std::remove(_if, _copy_if) | Modern Cpp Series Ep. 154](https://www.youtube.com/watch?v=btyuTSb_238)

## Exception Handling

# Exception Handling

Exception handling in C++ is a mechanism for managing runtime errors and unexpected events, preventing abrupt program termination. It uses `try`, `catch`, and `throw` keywords to monitor code blocks for exceptions, handle specific exception types, and signal error conditions, respectively. The `noexcept` specifier ensures a function doesn't throw exceptions. Standard exception classes in `<stdexcept>`, like `std::exception`, `std::logic_error`, and `std::runtime_error`, offer a structured approach to representing and handling various error types.

Visit the following resources to learn more:

- [@article@Exception Handling](https://www.w3schools.com/cpp/cpp_exceptions.asp)
- [@video@Exception handling in C++ (How to handle errors in your program?)](https://www.youtube.com/watch?v=kjEhqgmEiWY)

## Exceptions

# Exceptions

Exception handling in C++ provides a mechanism to manage runtime errors, ensuring program stability. This is achieved using `try`, `catch`, and `throw` blocks. The `try` block encloses code that might generate an exception. If an error occurs, a `throw` statement creates an exception object, which is then caught and handled by an appropriate `catch` block designed to deal with that specific exception type, thus preventing program termination.

## Exit Codes

# Exit Codes

Exit codes are numerical values returned by a program to the operating system upon completion, signaling whether the execution was successful or encountered errors. A return value of 0 typically indicates success, while non-zero values denote failure, with the specific meaning of each non-zero code being application-dependent. In C++, you can specify the exit code using the `return` statement within the `main` function or by calling the `exit()` function from the `<cstdlib>` header.

## Fmt

# fmt

`fmt` is a modern formatting library for C++. It provides a simple and efficient way to format text, similar to Python's `str.format()` or C#'s `string.Format()`. It offers compile-time checks for format string correctness and generally results in faster and safer string formatting compared to traditional methods like `printf`.

Visit the following resources to learn more:

- [@official@fmt](https://fmt.dev/12.0/)
- [@opensource@fmt](https://github.com/fmtlib/fmt)

## For  While  Do While Loops

# Loops

Loops are fundamental control flow structures that enable the repetition of code blocks based on a condition. C++ provides three primary loop types: `for`, `while`, and `do-while`. The `for` loop is ideal when the number of iterations is known beforehand, while the `while` loop continues execution as long as a specified condition remains true. The `do-while` loop is similar to the `while` loop, but guarantees at least one execution of the code block, as the condition is checked at the end of the loop.

Visit the following resources to learn more:

- [@article@C++ For Loop](https://www.w3schools.com/cpp/cpp_for_loop.asp)
- [@article@C++ While Loop](http://w3schools.com/cpp/cpp_while_loop.asp)
- [@article@C++ Do While Loop](https://www.w3schools.com/cpp/cpp_do_while_loop.asp)

## Forward Declaration

# Forward Declaration

Forward declaration is declaring an identifier (like a class, function, or variable) to the compiler before its full definition is provided. This informs the compiler about the existence and type of the identifier, allowing it to be used in limited contexts, such as pointer or reference usage, without requiring the full definition to be immediately available. This technique helps to manage dependencies, reduce compilation times, and resolve circular dependencies between different parts of a codebase.

## Full Template Specialization

# Full Template Specialization

Full template specialization in C++ provides a way to define specific implementations of a template (class or function) for particular types. This allows you to customize the behavior of a template when it's instantiated with a specific set of template arguments, enabling optimized code or special handling for certain types while the generic template handles other cases. This involves creating a specialized version of the template for a specific type or set of types.

## Function Overloading

# Function Overloading

Function overloading in C++ allows multiple functions to share the same name, provided they differ in the number or types of parameters. This facilitates compile-time polymorphism, enhancing code readability and maintainability by enabling functions to perform similar operations on different data types or argument counts.

Visit the following resources to learn more:

- [@official@Function Overloading - Microsoft Learn](https://learn.microsoft.com/en-us/cpp/cpp/function-overloading)

## Functions

# Functions

Functions in C++ are self-contained blocks of code designed to perform specific tasks, promoting code reusability and modularity. They come in two main types: standard library functions (pre-built functions like `sort()` and `sqrt()`) and user-defined functions (created by the programmer). Defining a function involves specifying its return type, name, and a list of parameters it accepts. To use a function before its definition, a function prototype can be declared, informing the compiler about the function's signature.

Visit the following resources to learn more:

- [@article@C++ Functions](https://www.w3schools.com/cpp/cpp_functions.asp)
- [@article@introduction to functions in c++](https://www.learncpp.com/cpp-tutorial/introduction-to-functions/)
- [@video@Learn C++ With Me #20 - Functions](https://www.youtube.com/watch?v=C83tPpvxIJA)

## Gdb

# GDB: GNU Debugger

GDB, the GNU Project Debugger, is a command-line tool essential for debugging C and C++ programs. It allows developers to examine a program's execution, set breakpoints, step through code, inspect variables, and analyze call stacks to identify and fix bugs. By using GDB, developers gain deep insight into the runtime behavior of their programs, making it an indispensable part of the C++ development workflow.

Visit the following resources to learn more:

- [@video@GDB is REALLY easy! Find Bugs in Your Code with Only A Few Commands](https://www.youtube.com/watch?v=Dq8l1_-QgAc)

## Grpc

# gRPC

gRPC is a high-performance, open-source framework developed by Google for building remote procedure calls (RPCs). It uses Protocol Buffers as its Interface Definition Language (IDL) and relies on HTTP/2 for transport. gRPC enables client applications to directly call methods on a server application on a different machine as if it were a local object, making it easier to create distributed applications and microservices.

Visit the following resources to learn more:

- [@official@Quick start](https://grpc.io/docs/languages/cpp/quickstart/)
- [@official@Basic Tutorial](https://grpc.io/docs/languages/cpp/basics/)
- [@opensource@grpc](https://github.com/grpc/grpc)

## Gtest  Gmock

# Google Test and Google Mock

Google Test and Google Mock are open-source C++ unit testing frameworks developed by Google. Google Test is a standalone framework for writing and running unit tests, while Google Mock extends it with powerful mocking capabilities. GMock is especially useful for testing components that interact with external or third-party utilities.

Visit the following resources to learn more:

- [@official@Google test github pages](https://google.github.io/googletest/)
- [@video@Google C++ Testing, GTest, GMock Framework playlist](https://youtube.com/playlist?list=PL_dsdStdDXbo-zApdWB5XiF2aWpsqzV55&si=TR8ESbH1-epTl6VM)
- [@video@Back to Basics: Unit Testing in C++ - Dave Steffen - CppCon 2024](https://youtu.be/MwoAM3sznS0?si=pumn99IobfU4AZ1I)

## Headers  Cpp Files

# Headers / CPP Files

In C++, organizing code effectively involves splitting programs into header and source files. Header files (with extensions like `.h` or `.hpp`) declare interfaces such as classes, functions, and variables, acting as blueprints for other parts of the code. Source files (with the `.cpp` extension) then implement the functionality declared in the headers. This separation supports modularity, reduces compilation times through separate compilation, and enhances code readability and maintainability by clearly defining interfaces and implementations.

Visit the following resources to learn more:

- [@article@Header files (C++)](https://learn.microsoft.com/en-us/cpp/cpp/header-files-cpp?view=msvc-170)
- [@video@What are header files in C++ ( PROGRAMMING TUTORIAL for beginners)](https://www.youtube.com/watch?v=qaGzc56Rekg)

## Idioms

# C++ Idioms

C++ idioms are established patterns and techniques used by developers to solve common programming challenges in a standardized and effective manner. These idioms promote code that is more efficient, maintainable, and less prone to errors by leveraging the features and principles of C++. Examples include Resource Acquisition Is Initialization (RAII) for managing resources, the Rule of Five for proper object lifecycle management, the PImpl idiom for hiding implementation details, and the Non-Virtual Interface (NVI) pattern for controlling inheritance behavior. Understanding and applying these idioms is crucial for writing robust and high-quality C++ code.

Visit the following resources to learn more:

- [@article@Idioms](https://medium.com/@amalpp42/idioms-in-c-f6b1c19fa605)

## If Else  Switch  Goto

# Conditional Statements and Unconditional Jump

`if-else`, `switch`, and `goto` are fundamental control flow mechanisms in C++. `if-else` constructs enable programs to execute different code blocks based on boolean conditions. The `switch` statement provides a way to efficiently handle multiple possible values of a single variable. The `goto` statement allows for an unconditional jump to a labeled point in the code, but its use is generally discouraged due to potential impacts on code readability and maintainability.

Visit the following resources to learn more:

- [@video@The 'if-else' Statement in C++](https://www.youtube.com/watch?v=9-BjXs1vMSc)
- [@video@Learn C++ With Me - Switch Statement](https://www.youtube.com/watch?v=uOlLs1OYSSI)
- [@video@Why is it illegal to use "goto"?](https://youtu.be/AKJhThyTmQw?si=gjEqAsDZVMDGVAT2)

## Installing C

# Installing C++

To use C++, you need to set up the necessary tools on your system to compile and run C++ code. This typically includes a compiler (like GCC or Clang), a build system (like Make or CMake), and an Integrated Development Environment (IDE) or text editor for writing code. The specific steps vary depending on your operating system (Windows, macOS, or Linux).

## Introduction To Language

# Introduction to Language

C++ is a general-purpose programming language known for its performance, efficiency, and control over hardware. It supports both procedural and object-oriented programming paradigms, making it versatile for a wide range of applications, from system programming to game development. C++ builds upon the C language, adding features like classes, templates, and exception handling.

Visit the following resources to learn more:

- [@article@Learn C++](https://www.learncpp.com/)
- [@article@Get Started with CPP!](https://isocpp.org/get-started)
- [@video@C++ Full Course by freeCodeCamp](https://youtu.be/vLnPwxZdW4Y)
- [@video@C++ Programming Course - Beginner to Advanced](https://www.youtube.com/watch?v=8jLOx1hD3_o)
- [@course@Modern Cpp Series By Mike Shah](https://courses.mshah.io/courses/cpp-programming-language)

## Iostream

# iostream

`iostream` is a fundamental header in the C++ Standard Library that handles input and output (I/O) operations. It provides classes like `istream` for input, `ostream` for output, and `iostream` for combined I/O. `cin`, `cout`, `cerr`, and `clog` are predefined objects within `iostream` for standard input, standard output, standard error output, and buffered logging, respectively. Use the `#include <iostream>` directive to incorporate this functionality into your programs.

## Iterators

# Iterators

Iterators in C++'s Standard Template Library (STL) are essential tools for traversing and accessing elements within containers like vectors, lists, and arrays. They act as generalized pointers, offering a way to interact with container elements without needing to know the container's underlying implementation. C++ provides different iterator types, including input, output, forward, bidirectional, reverse, and random access iterators, each with specific capabilities for reading, writing, and navigating through container elements. For most use cases, you would use `auto` keyword with `begin()` and `end()` methods to work with iterators. C++ algorithms often leverage iterators for tasks such as searching and sorting.

## Lambdas

# Lambdas

Lambdas, also known as lambda expressions, are a concise way to define anonymous functions directly within the code where they are needed. They are essentially nameless functions that can capture variables from the surrounding scope. Lambdas are particularly useful for short, self-contained operations, making code more readable and efficient by eliminating the need to define separate named functions for simple tasks, often used with algorithms like `std::sort` or `std::for_each`.

Visit the following resources to learn more:

- [@article@Lambda Expressions](https://en.cppreference.com/w/cpp/language/lambda)
- [@video@Lambdas in C++](https://youtu.be/MH8mLFqj-n8)
- [@feed@Explore top posts about AWS Lambda](https://app.daily.dev/tags/aws-lambda?ref=roadmapsh)

## Language Concepts

# Language Concepts

C++'s foundation rests on several core language concepts that enable the creation of efficient and robust applications. These concepts encompass fundamental building blocks like variables and data types for storing information, control structures for managing program flow with conditionals and loops, and functions for modularizing code into reusable blocks. Furthermore, C++ provides data structures such as arrays and vectors for managing collections of data, powerful memory manipulation through pointers, and object-oriented programming features via structures and classes, supporting inheritance and polymorphism. Finally, exception handling allows for graceful recovery from runtime errors, creating a well-rounded and reliable programming experience.

## Library Inclusion

# Library Inclusion

In C++, library inclusion is the process of making external code available to your program. This is achieved primarily through the `#include` preprocessor directive, which allows you to incorporate header files containing declarations of functions, classes, and other entities. Header files from the standard library are included using angle brackets (`<iostream>`), while user-defined or third-party headers are included using double quotes (`"myheader.h"`). While less common, source files can also be included, though this practice is generally discouraged due to potential issues with multiple definitions and longer compile times.

## Licensing

# Licensing

Licensing governs how you can use, modify, and distribute software libraries, particularly crucial when integrating third-party code into your C++ projects. Common open-source licenses like MIT, GPL, and Apache 2.0 each provide different levels of freedom and obligations. The MIT License is permissive, allowing almost any use with minimal requirements. The GPL is copyleft, requiring that modifications and derivative works also be licensed under GPL. The Apache License 2.0 is permissive, but includes terms relating to patents and requires documentation of modifications. Understanding and adhering to these licenses is essential to avoid legal issues.

## Lifetime Of Objects

# Lifetime of Objects

Object lifetime in C++ dictates when an object comes into existence and when it ceases to exist. This crucial concept influences memory management and program correctness. C++ defines four storage durations: static (exists for the program's duration), thread (exists for a thread's duration), automatic (exists within a scope), and dynamic (controlled by `new` and `delete`). Managing object lifetimes effectively, especially dynamic objects, is essential for preventing memory leaks and ensuring stable application behavior.

Visit the following resources to learn more:

- [@article@Lifetime](https://en.cppreference.com/w/cpp/language/lifetime.html)
- [@article@Object Lifetime in C++ (Stack/Scope Lifetimes)](http://youtube.com/watch?v=iNuTwvD6ciI)

## Logical Operators

# Logical Operators

Logical operators in C++ allow you to combine or modify boolean expressions, resulting in a final boolean value of either true (1) or false (0). These operators are crucial for controlling the flow of your program based on multiple conditions. C++ provides three main logical operators: AND (`&&`), which returns true only if both operands are true; OR (`||`), which returns true if at least one operand is true; and NOT (`!`), which reverses the boolean value of its operand. They enable you to create complex conditional statements.

Visit the following resources to learn more:

- [@article@Logical Operators](https://www.w3schools.com/cpp/cpp_operators_logical.asp)

## Macros

# C++ Macros

Macros in C++ are preprocessing directives that instruct the preprocessor to perform text substitutions before compilation. Defined using `#define`, they enable you to create symbolic constants, function-like constructs, and control conditional compilation. Macros can help in code optimization and customization, but it's essential to use them judiciously due to potential debugging and scope issues.

Visit the following resources to learn more:

- [@article@Macros in C++](https://www.youtube.com/watch?v=j3mYki1SrKE)
- [@video@C++ Macros](https://www.codecademy.com/resources/docs/cpp/macros)

## Makefile

# Makefile

A Makefile is a configuration file used by the `make` utility to automate the process of compiling and linking code in a project. It defines a set of rules and dependencies that specify how to build the final executable or library from source code. It consists of variables, rules with targets, prerequisites, recipes, and phony targets, which do not represent actual files, but execute related actions. Makefiles streamline the build process, reducing errors and ensuring consistency by specifying dependencies between source files and the commands to generate output files, such as object files and executables.

## Memory Leakage

# Memory Leakage

Memory leakage occurs when dynamically allocated memory is no longer accessible by the program, but the program fails to release it back to the operating system. This results in the memory being unusable by other parts of the program or other applications, gradually reducing the available memory and potentially leading to performance degradation or even program crashes.

## Memory Model

# Memory Model

The C++ memory model defines how a program organizes and manages memory during execution. It divides memory into different segments, each serving a specific purpose: the stack for function calls and local variables, the heap for dynamic memory allocation, the data segment for global and static variables, and the code segment for executable instructions. Understanding this model is crucial for writing efficient and bug-free C++ code, especially when dealing with memory management and resource allocation.

Visit the following resources to learn more:

- [@video@Memory Segments in C/C++](https://www.youtube.com/watch?v=2htbIR2QpaM)

## Multiple Inheritance

# Multiple Inheritance

Multiple inheritance in C++ allows a class to inherit from multiple base classes, combining their properties and behaviors into a single derived class. This means a class can inherit data members and member functions from several parent classes, offering a way to create more complex and specialized classes. However, it's essential to use multiple inheritance carefully, as it can introduce complexities like ambiguity and the diamond problem, requiring a good understanding of class hierarchies and potential conflict resolution.

Visit the following resources to learn more:

- [@article@Multiple Inheritance](https://www.w3schools.com/cpp/cpp_inheritance_multiple.asp)
- [@video@Multiple Inheritance Deep Dive | C++ Tutorial](https://www.youtube.com/watch?v=sswTE0u0r7g)

## Multithreading

# Multithreading

Multithreading allows concurrent execution of multiple threads within a single process, enhancing application performance by enabling parallel task execution. C++ provides multithreading support through the `<thread>` library (introduced in C++11), enabling thread creation, argument passing, and synchronization mechanisms like mutexes and locks to manage shared resource access and prevent data races. This introduction covers basic thread creation, passing arguments to threads, and using mutexes for thread synchronization; more advanced topics such as thread pools, condition variables, and atomic operations, exist for advanced synchronization and performance tuning.

Visit the following resources to learn more:

- [@video@Build your first multithreaded application - Introduction to multithreading in modern C++](https://www.youtube.com/watch?v=xPqnoB2hjjA)

## Name Mangling

# Name Mangling

Name mangling, also known as name decoration, is a technique compilers use to encode extra information like scope, type, and linkage into identifier names (like function and variable names). This allows C++ to support function overloading, where multiple functions can share the same name but have different parameters. The compiler generates a mangled name based on these details, though the exact mangling rules vary between compilers and platforms. Tools like `c++filt` can demangle these names back to their original form, which is useful for debugging. While you usually don't need to understand the details of name mangling, it can be important when working with external libraries or linking object files from different compilers.

Visit the following resources to learn more:

- [@article@C++ Name Mangling](https://medium.com/@abhishek.ec/c-name-mangling-ce3d0fedf88d)
- [@video@Name Mangling In C++](https://www.youtube.com/watch?v=FUIle4Ghasw)

## Namespaces

# Namespaces

Namespaces in C++ provide a way to organize code into logical groups, preventing naming conflicts when using code from different libraries or parts of a large project. They act as containers for variables, functions, classes, and even other namespaces. You can access elements within a namespace using the scope resolution operator `::`, nest namespaces for further organization, and selectively import elements or entire namespaces into the current scope using the `using` keyword to simplify code while being mindful of potential name collisions.

Visit the following resources to learn more:

- [@article@Namespaces](https://learn.microsoft.com/en-us/cpp/cpp/namespaces-cpp?view=msvc-170)
- [@video@What are C++ namespaces? 📛](https://www.youtube.com/watch?v=2lcIKzFHjSM)

## Newdelete Operators

# New/Delete Operators

The `new` and `delete` operators in C++ are used for dynamic memory allocation and deallocation. `new` allocates a block of memory on the heap and returns a pointer to the beginning of that block. `delete` then releases the memory block previously allocated by `new`, making it available for other uses. Proper use of `new` and `delete` is crucial to prevent memory leaks.

## Ninja

# Ninja

Ninja is a small, fast build system designed for speed and efficiency. Instead of directly interpreting project structure, it executes pre-generated build plans. This allows it to build only what's necessary, leading to significantly faster build times, particularly in large projects. It's commonly used with meta-build systems like CMake, which generate the `build.ninja` files that Ninja then uses to perform the actual build process.

Visit the following resources to learn more:

- [@official@Ninja](https://ninja-build.org/manual.html)
- [@video@CMake vs Ninja - a real-life comparison with actual code](https://www.youtube.com/watch?v=AkGt0fsQ17o)

## Non Copyable  Non Moveable

# Non-Copyable / Non-Moveable

The non-copyable/non-moveable idiom in C++ prevents objects of a class from being copied or moved. This is achieved by deleting the copy constructor, copy assignment operator, move constructor, and move assignment operator. It's useful for classes that manage exclusive resources, ensuring that only one instance controls the resource at a time, preventing issues like resource duplication or double deletion. By disabling copying and moving, you enforce a unique ownership model for instances of the class.

Visit the following resources to learn more:

- [@article@Dealing with non-copyable objects - (C++ Tutorial)](https://dev.to/dabretema/the-day-i-forbade-copy-semantics-to-an-object-nkl)

## Nuget

# NuGet

NuGet is a package manager initially designed for the .NET ecosystem, but it also extends its functionality to C++ projects through the `PackageReference` format. It simplifies the process of adding, updating, and managing external libraries and dependencies within your C++ projects, whether you're using Visual Studio's GUI, its integrated command-line tools, or the standalone `nuget.exe` executable. With NuGet, managing dependencies becomes more streamlined and efficient, allowing you to focus on your core C++ code.

Visit the following resources to learn more:

- [@article@Creating Cross-Platform NuGet Package To Wrap Native C++ Libraries](https://medium.com/@yooonatan/creating-cross-platform-nuget-package-to-wrap-native-c-libraries-b2ee71c34164)
- [@video@What is NuGet? | Nuget 101 [1 of 5]](https://www.youtube.com/watch?v=WW3bO1lNDmo)

## Object Oriented Programming

# Object-Oriented Programming (OOP)

Object-oriented programming is a style of programming centered around "objects," which combine data (attributes) and functions (methods) that operate on that data. OOP enables you to create modular, reusable, and maintainable code by organizing your programs around these objects and their interactions. Key concepts in OOP include classes (blueprints for objects), encapsulation (bundling data and methods), inheritance (creating new classes from existing ones), and polymorphism (using a single interface for different types).

Visit the following resources to learn more:

- [@article@C++ OOP](https://www.w3schools.com/cpp/cpp_oop.asp)
- [@video@Object Oriented Programming (OOP) in C++ Course](https://www.youtube.com/watch?v=wN0x9eZLix4)

## Opencl

# OpenCL

OpenCL (Open Computing Language) is a framework for writing programs that execute across heterogeneous platforms consisting of CPUs, GPUs, and other processors. It allows developers to harness the parallel processing power of different types of hardware using a unified API, enabling acceleration of computationally intensive tasks. With OpenCL, you can write code that can run on a variety of devices, making it a versatile tool for parallel programming.

Visit the following resources to learn more:

- [@official@Introduction](https://github.khronos.org/OpenCL-CLHPP/)
- [@opensource@Basic examples of OpenCL with the C++ API](https://github.com/Dakkers/OpenCL-examples)

## Opencv

# OpenCV

OpenCV (Open Source Computer Vision Library) is a comprehensive collection of programming functions primarily aimed at real-time computer vision. It encompasses a vast array of algorithms for image processing, object detection, video analysis, and machine learning, providing developers with tools to analyze and manipulate visual data.

Visit the following resources to learn more:

- [@official@OpenCV](https://opencv.org/)
- [@video@Setup OpenCV in Visual Studio 2022 for C/C++ Development](https://www.youtube.com/watch?v=unSce_GPwto)

## Operator Overloading

# Operator Overloading in C++

Operator overloading in C++ is a feature that allows you to redefine the way operators work for user-defined types (such as classes and structs). It lets you specify how operators like +, -, \*, ==, etc., behave when applied to objects of your class. Visit the following resources to learn more:

Visit the following resources to learn more:

- [@official@Operator Overloading - Microsoft Learn](https://learn.microsoft.com/en-us/cpp/cpp/operator-overloading)
- [@article@operator overloading - cppreference.com](https://en.cppreference.com/w/cpp/language/operators)

## Orbit Profiler

# Orbit Profiler

Orbit Profiler is a performance analysis tool designed to help developers identify bottlenecks and optimize the performance of their applications. It provides detailed insights into CPU usage, memory allocation, and other performance metrics through sampling and tracing. This helps pinpoint areas where code can be made more efficient.

Visit the following resources to learn more:

- [@official@ORBIT PROFILER](https://orbitprofiler.com/)

## Package Managers

# Package Managers

Package managers are essential tools that streamline the process of incorporating external libraries and dependencies into C++ projects. They automate the tasks of installing, updating, and managing these components, simplifying development and promoting code reuse. Popular options in the C++ ecosystem include Conan, a decentralized, cross-platform solution; vcpkg, a package manager developed by Microsoft; and cppan, which is now part of the build2 build toolchain. These tools help developers efficiently manage dependencies, improving code quality and accelerating development.

## Partial Template Specialization

# Partial Template Specialization

Partial template specialization in C++ allows you to create specialized versions of a template for specific subsets of types. This is achieved by providing a new template definition that is selected by the compiler when the template arguments match the specified criteria. It offers a way to customize template behavior for certain type categories, like pointers or specific data types, without needing complete specializations for every possible type.

## Pimpl

# Pimpl Idiom

The Pimpl (Pointer to Implementation) idiom is a C++ technique used to hide the implementation details of a class. This is achieved by declaring a private implementation class and holding a pointer to it within the main class. The public interface remains clean, and compile-time dependencies are significantly reduced. This promotes better code organization, reduces recompilation times, and improves binary compatibility.

Visit the following resources to learn more:

- [@article@Pointer To Implementation(PIMPL) Idiom By Using Smart Pointer in C++](https://cengizhanvarli.medium.com/pointer-to-implementation-pimpl-idiom-by-using-smart-pointer-in-c-07dcd535d0ce)
- [@video@Classes Part 30 - pIMPL (pointer to implementation) - More Stable APIs| Modern Cpp Series Ep. 67](https://www.youtube.com/watch?v=3mFpXNEB_AA)

## Poco

# POCO

POCO (Portable Components) is a C++ class library that simplifies network-centric, portable applications. It offers a comprehensive set of tools and components for tasks such as networking, data processing, and basic utilities. POCO focuses on being modular and cross-platform.

Visit the following resources to learn more:

- [@official@POCO Docs](https://pocoproject.org/documentation.html)
- [@video@Writing a Network Client with POCO](https://www.youtube.com/watch?v=rRR9RTUEn4k)

## Pointers And References

# Pointers and References

Pointers and references are fundamental concepts in C++ that allow indirect access to variables. A pointer stores the memory address of another variable, enabling dynamic memory management and manipulation. A reference, on the other hand, acts as an alias for an existing variable, providing a direct way to access and modify its value. Understanding the difference between pointers and references, including constant pointers and pointers to constants, is crucial for writing efficient and safe C++ code.

Visit the following resources to learn more:

- [@article@C++ Pointers](https://www.youtube.com/watch?v=slzcWKWCMBg)
- [@article@Function Pointer in C++](https://www.scaler.com/topics/cpp/function-pointer-cpp/)
- [@video@C++ pointers explained easy 👈](https://www.youtube.com/watch?v=slzcWKWCMBg)

## Protobuf

# Protobuf

Protobuf (Protocol Buffers) is a language-neutral, platform-neutral, extensible mechanism for serializing structured data. You define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of data streams, using a variety of languages. Think of it as a more efficient and flexible alternative to XML or JSON.

Visit the following resources to learn more:

- [@opensource@protobuf](https://github.com/protocolbuffers/protobuf)
- [@article@Protocol Buffer Basics: C++](https://protobuf.dev/getting-started/cpptutorial/)

## Pybind11

# pybind11

pybind11 is a lightweight header-only library that allows you to create Python bindings for your existing C++ code. It essentially lets you expose C++ functions, classes, and data structures to Python, enabling seamless interoperability between the two languages. This allows you to leverage the performance of C++ while utilizing the flexibility and ease of use of Python.

Visit the following resources to learn more:

- [@opensource@pybind11](https://github.com/pybind/pybind11)
- [@article@Pybind11 Tutorial: Binding C++ Code to Python](https://medium.com/@ahmedfgad/pybind11-tutorial-binding-c-code-to-python-337da23685dc)

## Pytorch C

# PyTorch C++

PyTorch C++ provides a front-end for the PyTorch machine learning framework, allowing you to build and deploy models using C++ instead of Python. This enables you to leverage the performance and control of C++ for computationally intensive tasks, especially in production environments where low latency and resource efficiency are critical. It involves using a C++ API to define and execute PyTorch operations.

Visit the following resources to learn more:

- [@official@PyTorch C++ API](https://docs.pytorch.org/cppdocs/)
- [@article@LibTorch: The C++ Powerhouse Driving PyTorch](https://medium.com/@pouyahallaj/libtorch-the-c-powerhouse-driving-pytorch-ee0d4f7b8743)

## Qt

# Qt

Qt is a cross-platform application development framework widely used for creating graphical user interfaces (GUIs) and applications that run on various operating systems, such as Windows, macOS, Linux, and embedded systems. It provides a set of tools and libraries that simplify the development process, offering features like widgets, networking, database access, and multimedia support. Qt uses C++ as its primary programming language, extending it with its own meta-object compiler (moc) and signal/slot mechanism for event handling.

Visit the following resources to learn more:

- [@official@Qt for Beginners](https://wiki.qt.io/Qt_for_Beginners)

## Raii

# RAII

RAII (Resource Acquisition Is Initialization) is a C++ idiom that ties the management of resources to the lifetime of objects. Resources are acquired during object construction and automatically released when the object is destroyed, typically in the destructor. This ensures resources are properly managed, even in the face of exceptions, preventing leaks and simplifying code by automating resource cleanup.

Visit the following resources to learn more:

- [@article@RAII](https://en.cppreference.com/w/cpp/language/raii.html)
- [@video@What is RAII (Resource Acquisition Is Initialization)?](https://www.youtube.com/watch?v=q6dVKMgeEkk)

## Ranges V3

# Ranges v3

Ranges v3 is a modern C++ library that provides tools for working with sequences of elements in a more composable and expressive way. It introduces concepts like views and algorithms that operate on ranges, allowing you to chain operations together to process data efficiently and elegantly without relying heavily on iterators. Ranges v3 simplifies common data manipulation tasks such as filtering, transforming, and sorting by offering a higher-level abstraction over traditional iterator-based code.

Visit the following resources to learn more:

- [@opensource@range-v3](https://github.com/ericniebler/range-v3)
- [@article@A GentleIntroductiontoRangesv3](https://www.daixtrose.de/talks/gentle-intro-to-ranges/talk/A%20Gentle%20Introduction%20to%20Ranges%20v3.pdf)

## Raw Pointers

# Raw Pointers

Raw pointers are variables that store the memory address of another variable. They directly hold the location in memory where a value is stored, allowing you to access and manipulate that value. Using raw pointers requires careful memory management as you are responsible for allocating and deallocating the memory they point to.

Visit the following resources to learn more:

- [@article@Raw pointers (C++)](https://learn.microsoft.com/en-us/cpp/cpp/raw-pointers?view=msvc-170)

## References

# References

In C++, a reference is an alias for an existing variable. It provides an alternative name to access the same memory location. References are similar to pointers in some ways, but they have key differences: a reference must be initialized when it's created, and once initialized, it cannot be changed to refer to a different variable. References are commonly used to pass arguments to functions by reference, allowing the function to modify the original variable.

Visit the following resources to learn more:

- [@article@References](https://en.cppreference.com/w/cpp/language/reference)
- [@article@C++ References](https://www.w3schools.com/cpp/cpp_references.asp)
- [@video@REFERENCES in C++](https://www.youtube.com/watch?v=IzoFn3dfsPA)

## Reinterpret Cast

# reinterpret_cast

`reinterpret_cast` is a powerful but potentially dangerous type of casting operator in C++. It allows you to convert between unrelated pointer types, integer types, or between pointers and integers. Unlike other casts, it doesn't perform any type checking or data conversion. Its primary function is to reinterpret the bit pattern of an expression as a different type, making it useful for low-level operations, but also requiring extreme caution to avoid undefined behavior. Use it only when absolutely necessary and understand the underlying memory layout involved.

## Rtti

# Run-Time Type Identification (RTTI)

Run-Time Type Identification (RTTI) in C++ allows you to determine the type of an object during program execution. This is particularly useful when working with polymorphism and inheritance. C++ provides two primary mechanisms for RTTI: the `typeid` operator, which retrieves type information, and the `dynamic_cast` operator, which safely converts pointers or references between types at runtime, handling potential casting failures gracefully. While powerful, be mindful that RTTI can introduce some performance overhead due to the runtime checks involved.

Visit the following resources to learn more:

- [@article@What Is Runtime Type Identification (RTTI) in C++?](https://www.codeguru.com/cplusplus/what-is-runtime-type-identification-rtti-in-c/)
- [@video@Dynamic cast c++ Runtime Type Identification example why we use dynamic cast - RTTI](https://www.youtube.com/watch?v=2PXN7Zk9v80)

## Rule Of Zero Five Three

# Rule of Zero, Five, Three

The Rule of Zero, Three, and Five are guidelines for managing resources within C++ classes and structs. The Rule of Zero suggests letting the compiler handle resource management if your class doesn't explicitly manage any. If your class manages resources, pre-C++11 it adhered to the Rule of Three, requiring you to define a destructor, copy constructor, and copy assignment operator. Modern C++ with move semantics extends this to the Rule of Five, which adds a move constructor and move assignment operator to efficiently transfer ownership of resources.

Visit the following resources to learn more:

- [@article@The rule of three/five/zero](https://en.cppreference.com/w/cpp/language/rule_of_three.html)
- [@article@The Rule of 0/3/5](https://medium.com/@Farhan11637/the-rule-of-0-3-5-2e608a717811)

## Running Your First Program

# Running Your First Program

This involves configuring your system to compile and execute C++ code. You'll need a compiler (like GCC or Clang), an IDE or text editor for writing code, and potentially a build system to manage the compilation process. A basic "Hello, World!" program is typically used to verify the setup and demonstrate the fundamental syntax.

Visit the following resources to learn more:

- [@article@Get Started With C++](https://www.w3schools.com/cpp/cpp_getstarted.asp)

## Scope

# Scope

Scope in C++ defines the visibility and lifetime of variables, functions, and other identifiers within a program. It dictates where these entities can be accessed and how long they persist in memory. C++ employs several types of scope, including global scope (accessible program-wide), local scope (confined to a function or block), namespace scope (organized within named groups), and class scope (specific to class members). Understanding scope is vital for preventing naming conflicts and managing the lifespan of objects, thus contributing to cleaner and more maintainable code.

Visit the following resources to learn more:

- [@article@C++ Variable Scope](https://www.w3schools.com/cpp/cpp_scope.asp)

## Setting Up Your Environment

# Setting up your Environment

Setting up your environment in C++ involves configuring your computer with the necessary tools and software to write, compile, and run C++ programs. This typically includes installing a C++ compiler (like GCC or Clang), an integrated development environment (IDE) or text editor, and potentially a build system for managing larger projects. Proper setup is key to a smooth and efficient development workflow.

Visit the following resources to learn more:

- [@article@C++ Getting Started](https://www.w3schools.com/cpp/cpp_getstarted.asp)
- [@video@How to set up C++ in Visual Studio Code](https://www.youtube.com/watch?v=DMWD7wfhgNY)

## Sfinae

# SFINAE (Substitution Failure Is Not An Error)

SFINAE is a core principle in C++ template metaprogramming that enables the compiler to choose the most suitable function or class template specialization during compilation. It leverages the idea that when the compiler attempts to substitute template arguments into a template and the substitution results in an invalid type or expression, this failure is not immediately treated as a compilation error. Instead, the compiler silently discards that specialization and continues searching for other viable options, thus allowing for conditional compilation based on type traits and other compile-time properties.

## Shared Ptr

# shared_ptr

`shared_ptr` is a smart pointer in C++ that manages dynamically allocated memory. It enables multiple pointers to safely own and share the same object. When the last `shared_ptr` pointing to an object goes out of scope, the managed object is automatically deleted, preventing memory leaks. It achieves this by maintaining a reference count that tracks the number of `shared_ptr` instances pointing to the same memory location.

## Smart Pointers

# Smart Pointers

Smart pointers are classes that behave like regular pointers but provide automatic memory management. They help prevent memory leaks by automatically deallocating the memory they point to when they are no longer needed. This is achieved through techniques like reference counting and RAII (Resource Acquisition Is Initialization). Essentially, they encapsulate a raw pointer and ensure that the memory it points to is freed when the smart pointer goes out of scope or is reset.

Visit the following resources to learn more:

- [@article@Smart Pointers](https://en.cppreference.com/book/intro/smart_pointers)
- [@video@SMART POINTERS in C++ (std::unique_ptr, std::shared_ptr, std::weak_ptr)](https://www.youtube.com/watch?v=UOB7-B2MfwA)

## Spack

# Spack

Spack is a package manager designed for flexibility and support for multiple versions, configurations, platforms, and compilers, making it especially useful in High Performance Computing (HPC) environments. It automates the process of installing and managing dependencies, enabling users to build complex software stacks with fine-grained control over their components. Spack supports a variety of platforms, including Linux, macOS, and supercomputers, along with compilers like GCC, Clang, and Intel. Its key features include multi-version support, compiler support, platform support, and automatic dependency management.

Visit the following resources to learn more:

- [@official@Spack](https://spack.io/)
- [@opensource@spack](https://github.com/spack/spack)
- [@video@Tutorials 2025: Spack, Part 1 (Basics, Environments, Configuration)](https://www.youtube.com/watch?v=Uoi3-_xMPtk)

## Spdlog

# spdlog

spdlog is a fast and cross-platform C++ logging library. It provides a simple interface for writing log messages to different destinations such as the console, files, or custom sinks. It supports various log levels, formatting options, and asynchronous logging, making it suitable for projects that require efficient and flexible logging capabilities.

Visit the following resources to learn more:

- [@opensource@spdlog](https://github.com/gabime/spdlog)

## Standard Library  Stl

# C++ Standard Library and STL

The C++ Standard Library is a comprehensive collection of classes and functions, extending the core language with ready-to-use tools for common programming tasks. A crucial part of the Standard Library is the Standard Template Library (STL), which offers pre-built, templatized components like containers (vectors, lists, maps), algorithms (sorting, searching), and iterators to work with those containers. The STL promotes code reuse and efficiency by providing generic implementations that can work with various data types, saving developers significant time and effort.

Visit the following resources to learn more:

- [@book@Mastering STL in C++23: New Features, Updates, and Best Practices](https://simplifycpp.org/books/Mastering_STL.pdf)
- [@video@C++ Standard Template Library (STL) Short Overview](https://www.youtube.com/watch?v=Id6ZEb_Lg58)

## Standards

# C++ Standards

C++ standards are sets of rules and guidelines that define the C++ programming language. These standards ensure consistency and portability across different compilers and platforms. Each standard introduces new features, improvements, and sometimes deprecates older functionalities. The current standard is C++23.

## Static Polymorphism

# Static Polymorphism

Static polymorphism, also known as compile-time polymorphism, enables the execution of different code depending on the type of data it's handling, but this determination happens at compile time. In C++, static polymorphism is primarily achieved through function overloading, which allows defining multiple functions with the same name but different parameter lists, and templates, which facilitate writing generic functions and classes that operate on various data types without runtime overhead.

Visit the following resources to learn more:

- [@article@Static Polymorphism in C++](https://medium.com/@kateolenya/static-polymorphism-in-c-9e1ae27a945b)
- [@video@Advanced C++: Static Polymorphism](https://www.youtube.com/watch?v=-WV9vWjhI3g)

## Static Typing

# Static Typing

Static typing, as implemented in C++, is a system where the data type of a variable is known and checked at compile time, before the program runs. This means each variable is declared with a specific type (like `int`, `double`, or `char`), and the compiler enforces that only values of that type are assigned to it. While C++ allows for type conversion, attempting to assign an incompatible type will result in either an implicit conversion (if possible) or a compilation error, ensuring type safety and helping catch errors early in the development process.

Visit the following resources to learn more:

- [@article@Type-Coversion](https://www.programiz.com/cpp-programming/type-conversion)
- [@article@Static Vs Dynamic](https://www.techtarget.com/searchapparchitecture/tip/Static-vs-dynamic-typing-The-details-and-differences)

## Static Cast

# static_cast

`static_cast` is a C++ casting operator primarily used for performing conversions between related types at compile time. This includes converting between primitive data types like `int` and `float`, and upcasting or downcasting within inheritance hierarchies. It offers a level of type safety over C-style casts by performing checks to ensure the conversion is valid, preventing potentially unsafe reinterpretation of data and allowing for more predictable behavior.

## Structures And Classes

# Structures and Classes

Structures and classes in C++ are blueprints for creating user-defined data types. They allow you to group variables (members) of different data types under a single name, enabling you to represent complex entities. The key distinction lies in their default access control: structure members are public by default, while class members are private, influencing how their data is accessed and manipulated.

Visit the following resources to learn more:

- [@article@Clases y structs (C++)](https://learn.microsoft.com/es-es/cpp/cpp/classes-and-structs-cpp?view=msvc-170)
- [@video@CLASSES vs STRUCTS in C++](https://www.youtube.com/watch?v=fLgTtaqqJp0)

## Structuring Codebase

# Structuring Codebase

Structuring your codebase involves organizing and modularizing code for better maintainability, efficiency, and readability. This enhances collaboration, simplifies feature addition, and accelerates debugging. In C++, techniques like namespaces, include guards, header/source file separation, and consistent code formatting are vital for effective codebase structure.

## Template Specialization

# Template Specialization

Template specialization in C++ allows you to provide custom implementations of templates for specific types or type patterns. This becomes useful when the generic template implementation doesn't suit a particular type, requiring tailored logic for optimization or specific behavior. Template specialization comes in two primary forms: full specialization, where a completely new implementation is defined for a specific type, and partial specialization, where a more specialized implementation is provided for a subset of types matching a given pattern.

## Templates

# C++ Templates

C++ Templates provide a way to write generic code by allowing functions and classes to operate with different data types without being rewritten for each type. This is achieved by using type parameters or placeholders that are later replaced with actual data types when the template is instantiated, promoting code reuse and flexibility. Templates can be specialized to provide custom behavior for specific data types.

Visit the following resources to learn more:

- [@article@Templates](https://en.cppreference.com/w/cpp/language/templates.html)
- [@article@C++ Templates](https://www.w3schools.com/cpp/cpp_templates.asp)
- [@video@Templates in C++](https://www.youtube.com/watch?v=I-hZkUa9mIs)

## Tensorflow

# Tensorflow

TensorFlow is an open-source software library developed by Google, primarily used for numerical computation and large-scale machine learning. It allows developers to create and train machine learning models using a variety of tools, libraries, and community resources. TensorFlow focuses on deep learning tasks like image recognition, natural language processing, and time series analysis.

Visit the following resources to learn more:

- [@opensource@Tensor Flow](https://github.com/tensorflow/tensorflow)
- [@article@How to Deploy Tensorflow Models in C++ in 3 different ways](https://towardsdatascience.com/how-to-deploy-tensorflow-models-in-c-in-3-different-ways-f7e25046be29/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- [@video@TensorFlow in 100 Seconds](https://www.youtube.com/watch?v=i8NETqtGHms)

## Type Casting

# Type Casting

Type casting in C++ involves converting a variable's data type to another. C++ provides several casting methods: C-style casting (inherited from C), `static_cast` (for explicit conversions at compile time), `dynamic_cast` (for safe downcasting in class hierarchies), `reinterpret_cast` (for low-level bitwise reinterpretation), and `const_cast` (to modify the constness of variables). Choosing the appropriate cast is crucial for safe and efficient code execution.

Visit the following resources to learn more:

- [@article@Type Casting](https://www.w3schools.com/cpp//cpp_type_casting.asp)
- [@video@Casting in C++](https://youtu.be/pWZS1MtxI-A)

## Type Traits

# Type Traits

Type traits in C++ are a powerful set of tools, implemented as template classes, found in the `<type_traits>` header. They provide a mechanism to inspect and query the properties of types at compile time, such as whether a type is a pointer, arithmetic type, or function. This allows you to write generic code that adapts its behavior based on the characteristics of the types it's working with, enabling compile-time branching and more robust template metaprogramming.

## Undefined Behavior Ub

# Undefined Behavior (UB)

Undefined behavior in C++ arises when a program violates the rules defined by the C++ standard, leading to unpredictable and unspecified outcomes. This can stem from actions such as accessing uninitialized variables, dereferencing null pointers, performing out-of-bounds memory access, or dividing by zero. The compiler is free to interpret such situations in any manner, potentially resulting in crashes, incorrect results, or even security vulnerabilities, making its avoidance a critical aspect of writing robust and reliable C++ code.

Visit the following resources to learn more:

- [@article@Undefined Behavior (UB)](https://en.cppreference.com/w/cpp/language/ub.html)

## Understanding Debugger Messages

# Understanding Debugger Messages

Debugger messages are notifications from a debugger that aid in identifying issues within C++ code. These messages manifest as warnings, errors, or informational outputs, offering insight into the program's state and specific problems encountered during debugging. Error messages flag code issues preventing compilation or execution, while warnings highlight potential problems. Informational messages provide general information about the program's execution, such as breakpoints, watchpoints, variable values, and the call stack.

## Unique Ptr

# unique_ptr

`unique_ptr` is a smart pointer in C++ that provides exclusive ownership of a dynamically allocated object. It ensures that only one `unique_ptr` can point to a given object at any time, preventing memory leaks by automatically deleting the managed object when the `unique_ptr` goes out of scope or is explicitly reset. Ownership can be transferred to another `unique_ptr` using `std::move`, but copying is disallowed to enforce the single-ownership principle.

Visit the following resources to learn more:

- [@official@std::unique_ptr - Detailed Reference](https://en.cppreference.com/w/cpp/memory/unique_ptr)
- [@article@Smart Pointers – unique_ptr](https://www.learncpp.com/cpp-tutorial/stdunique_ptr/)
- [@video@When should you use std::unique_ptr? - StackOverflow Discussion](https://stackoverflow.com/questions/13782051/when-should-you-use-stdunique-ptr)

## Variadic Templates

# Variadic Templates

Variadic templates, introduced in C++11, provide a way to create templates that can accept a variable number of arguments. Using the ellipsis (`...`) notation, you can define parameter packs that represent zero or more arguments of potentially different types. This allows for the creation of functions and classes that can operate on varying numbers of inputs, enhancing code flexibility and reusability, as demonstrated by use cases such as summing multiple arguments or creating tuple-like structures.

## Vcpkg

# vcpkg

`vcpkg` is an open-source, cross-platform package manager for C and C++ libraries that simplifies the acquisition and building of dependencies. Supporting Windows, Linux, and macOS, it streamlines the integration of external libraries into your projects through search, installation, and removal commands. It also offers integration with Visual Studio for Windows-based development, making dependency management more efficient.

Visit the following resources to learn more:

- [@official@vcpkg Docs](https://learn.microsoft.com/en-gb/vcpkg/)
- [@video@vcpkg Crash Course | Visual Studio 2022 | C++ libraries simplified!](https://www.youtube.com/watch?v=0h1lC3QHLHU)

## Virtual Methods

# Virtual Methods

Virtual methods are the cornerstone of dynamic polymorphism in C++ classes. They enable a derived class to provide its own specific implementation of a function that is already defined in a base class. When you call a virtual function through a base class pointer or reference, the runtime determines which version of the function to execute based on the actual type of the object being pointed to, not the type of the pointer or reference itself. This mechanism, known as dynamic dispatch, allows for flexible and extensible code where behavior can be tailored at runtime.

Visit the following resources to learn more:

- [@official@C++ Virtual Functions Documentation](https://en.cppreference.com/w/cpp/language/virtual)
- [@video@Virtual Functions Explained (YouTube)](https://www.youtube.com/watch?v=oIV2KchSyGQ&ab_channel=TheCherno)

## Virtual Tables

# Virtual Tables

Virtual tables (vtables) are compiler-generated lookup tables used in C++ to implement dynamic polymorphism, especially with virtual functions. Each class that declares or inherits virtual functions has a vtable, which contains pointers to the most derived versions of those virtual functions for that class. When a virtual function is called through a pointer or reference to a base class, the vtable is consulted at runtime to determine the actual function to execute based on the object's dynamic type.

Visit the following resources to learn more:

- [@article@Understandig Virtual Tables in C++](https://pabloariasal.github.io/2017/06/10/understanding-virtual-tables/)
- [@video@Classes part 18 - Understanding the vtable (Popular interview question) | Modern Cpp Series Ep. 54](https://www.youtube.com/watch?v=hS7kPtVB1vI)

## Weak Ptr

# weak_ptr

`weak_ptr` is a smart pointer in C++ that holds a non-owning reference to an object managed by a `shared_ptr`. It doesn't participate in the object's ownership count, meaning that it doesn't prevent the object from being destroyed if the `shared_ptr`s owning the object go out of scope. Its primary use is to detect if the object managed by the `shared_ptr` still exists. You can obtain a `shared_ptr` from a `weak_ptr` using `lock()`, but this might return an empty `shared_ptr` if the object has already been destroyed.

## What Is C

# What is C++?

C++ is a powerful, general-purpose programming language. It is an extension of the C language, adding features like object-oriented programming, which allows you to structure code into reusable components. C++ is known for its high performance, efficiency, and control over system resources, making it suitable for a wide range of applications, including game development, operating systems, and high-performance computing.

Visit the following resources to learn more:

- [@article@Learn C++](https://www.learncpp.com/)
- [@video@C++ Tutorial for Beginners - Full Course](https://youtu.be/vLnPwxZdW4Y)
- [@feed@Explore top posts about C++](https://app.daily.dev/tags/c++?ref=roadmapsh)

## Why Use C

# Why Use C++

C++ is a powerful, general-purpose programming language known for its performance and control over system resources. It combines high-level and low-level features, allowing developers to write efficient code for a wide range of applications. This includes operating systems, game development, embedded systems, high-performance computing, and more.

## Windbg

# WinDbg

WinDbg, a debugger included in the Microsoft Windows SDK, is a powerful tool for analyzing and debugging Windows applications, both in user mode and kernel mode. It offers a graphical interface and a comprehensive set of features for tasks like analyzing crash dumps, setting breakpoints, and stepping through code execution to identify and resolve issues in your C++ programs. Familiarity with WinDbg enables developers to delve deep into the runtime behavior of their applications and pinpoint the root cause of bugs.

Visit the following resources to learn more:

- [@video@Debugging C/C++ Programs from Scratch with WinDbg: A Beginner's Guide](https://www.youtube.com/watch?v=AgtgZDsADUI)

## Working With Libraries

# Working with Libraries

Libraries in C++ are collections of pre-written code designed to be reused in different programs, offering functionalities like specialized algorithms, data structures, or system interfaces. These libraries come in two main types: static libraries, which are linked directly into your executable at compile time, and dynamic libraries, which are loaded at runtime. Utilizing libraries involves including their header files in your source code and linking them during compilation, allowing you to extend the capabilities of your C++ programs without rewriting common functionalities from scratch.
